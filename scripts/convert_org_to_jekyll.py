#!/usr/bin/env python3
"""Convert org2blog/org-mode posts to Jekyll Markdown posts."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "_posts"
ASSETS_DIR = ROOT / "assets" / "images"
REPORT = ROOT / "MIGRATION_REPORT.md"

SKIP_DIRS = {".git", "_site", "_posts", "assets", "vendor", ".bundle"}
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})(?:\s+\w+)?(?:\s+(\d{1,2}):(\d{2})(?::(\d{2}))?)?")
META_RE = re.compile(r"^\s*#\+([A-Za-z0-9_]+):\s*(.*)$")
MD_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")


@dataclass
class Post:
    source: Path
    metadata: dict[str, list[str]]
    body: str
    title: str
    date: dt.datetime
    date_source: str
    slug: str
    categories: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    permalink: str | None = None
    post_id: str | None = None
    missing: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    copied_images: list[str] = field(default_factory=list)
    missing_images: list[str] = field(default_factory=list)
    local_links: list[str] = field(default_factory=list)
    broken_local_links: list[str] = field(default_factory=list)
    unusual: list[str] = field(default_factory=list)
    output: Path | None = None


def find_org_files() -> list[Path]:
    org_files: list[Path] = []
    for path in ROOT.rglob("*.org"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        org_files.append(path)
    return sorted(org_files)


def parse_org(path: Path) -> tuple[dict[str, list[str]], str]:
    metadata: dict[str, list[str]] = {}
    body_lines: list[str] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = META_RE.match(line)
        if match:
            key = match.group(1).upper()
            metadata.setdefault(key, []).append(match.group(2).strip())
        else:
            body_lines.append(line)
    return metadata, "\n".join(body_lines).strip() + "\n"


def first(metadata: dict[str, list[str]], key: str) -> str | None:
    values = metadata.get(key.upper(), [])
    for value in values:
        if value.strip():
            return value.strip()
    return None


def split_terms(value: str | None) -> list[str]:
    if not value:
        return []
    parts = re.split(r"[,;]", value)
    return [part.strip() for part in parts if part.strip()]


def parse_date(value: str | None, source: Path) -> tuple[dt.datetime, str, list[str]]:
    missing: list[str] = []
    if value:
        match = DATE_RE.search(value)
        if match:
            year, month, day, hour, minute, second = match.groups()
            parsed = dt.datetime(
                int(year),
                int(month),
                int(day),
                int(hour or 0),
                int(minute or 0),
                int(second or 0),
                tzinfo=dt.timezone.utc,
            )
            return parsed, "metadata", missing
    missing.append("date")
    stat = source.stat()
    fallback = dt.datetime.fromtimestamp(stat.st_mtime, tz=dt.timezone.utc)
    return fallback.replace(microsecond=0), "file mtime fallback", missing


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"['`]", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def detect_unusual(body: str, metadata: dict[str, list[str]]) -> list[str]:
    unusual: set[str] = set()
    for key in metadata:
        if key in {"BIBLIOGRAPHY", "CSL_STYLE", "CITE_EXPORT", "PRINT_BIBLIOGRAPHY"}:
            unusual.add(f"org citation/bibliography directive: #+{key}")
    patterns = {
        "org citation syntax": r"(?:\[cite:|cite:)",
        "elisp org link": r"\[\[elisp:",
        "raw org export directive": r"^\s*#\+BEGIN_|^\s*#\+END_",
        "org table": r"^\|",
        "local variables block": r"^# Local Variables:",
    }
    for label, pattern in patterns.items():
        if re.search(pattern, body, flags=re.MULTILINE):
            unusual.add(label)
    return sorted(unusual)


def org_image_targets(body: str) -> list[str]:
    targets: list[str] = []
    for raw in re.findall(r"\[\[(?:file:)?([^\]\[]+\.(?:png|jpe?g|gif|svg|pdf))(?:\]\[[^\]]*\])?\]\]", body, flags=re.I):
        targets.append(raw.strip())
    return targets


def org_local_links(body: str) -> list[str]:
    targets: list[str] = []
    for raw in re.findall(r"\[\[([^\]\[]+)\]", body):
        target = raw.split("][", 1)[0]
        parsed = urlparse(target)
        if parsed.scheme in {"http", "https", "mailto", "elisp", "cite"}:
            continue
        if target.startswith("#"):
            continue
        targets.append(target)
    return targets


def infer_title(path: Path, metadata: dict[str, list[str]]) -> tuple[str, list[str]]:
    title = first(metadata, "TITLE")
    if title:
        return title, []
    return path.with_suffix("").name.replace("-", " ").replace("_", " ").title(), ["title"]


def infer_permalink(date: dt.datetime, slug: str, date_source: str) -> str | None:
    if date_source != "metadata":
        return None
    return f"/{date:%Y/%m/%d}/{slug}/"


def build_post(path: Path) -> Post:
    metadata, body = parse_org(path)
    title, missing = infer_title(path, metadata)
    date, date_source, date_missing = parse_date(first(metadata, "DATE"), path)
    missing.extend(date_missing)
    slug = slugify(first(metadata, "SLUG") or first(metadata, "PERMALINK") or title)
    post = Post(
        source=path,
        metadata=metadata,
        body=body,
        title=title,
        date=date,
        date_source=date_source,
        slug=slug,
        categories=split_terms(first(metadata, "CATEGORY")),
        tags=split_terms(first(metadata, "TAGS")),
        permalink=first(metadata, "PERMALINK"),
        post_id=first(metadata, "POSTID"),
        missing=missing,
        unusual=detect_unusual(body, metadata),
    )
    if not post.permalink:
        post.permalink = infer_permalink(post.date, post.slug, post.date_source)
    post.images = org_image_targets(body)
    post.local_links = org_local_links(body)
    return post


def pandoc_to_markdown(post: Post) -> str:
    cmd = ["pandoc", "--from=org", "--to=gfm", "--wrap=none"]
    completed = subprocess.run(
        cmd,
        input=post.body,
        cwd=post.source.parent,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"pandoc failed for {post.source}: {completed.stderr}")
    return completed.stdout.strip() + "\n"


def is_external(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto", "tel", "cite"} or target.startswith("#")


def copy_and_rewrite_links(markdown: str, post: Post) -> str:
    image_exts = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf"}
    asset_base = ASSETS_DIR / post.source.parent.relative_to(ROOT)

    def repl(match: re.Match[str]) -> str:
        bang, text, raw_target = match.groups()
        target, suffix = split_markdown_target(raw_target)
        if is_external(target):
            return match.group(0)
        parsed = urlparse(target)
        path_text = unquote(parsed.path)
        if not path_text or path_text.startswith("/assets/"):
            return match.group(0)
        ext = Path(path_text).suffix.lower()
        source_file = (post.source.parent / path_text).resolve()
        if ext in image_exts or bang:
            dest = asset_base / path_text
            if source_file.exists() and source_file.is_file():
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_file, dest)
                rel_dest = "/" + dest.relative_to(ROOT).as_posix()
                post.copied_images.append(rel_dest)
                return f"{bang}[{text}]({rel_dest}{suffix})"
            post.missing_images.append(path_text)
            return match.group(0)
        if not source_file.exists():
            post.broken_local_links.append(path_text)
        return match.group(0)

    return MD_LINK_RE.sub(repl, markdown)


def split_markdown_target(raw: str) -> tuple[str, str]:
    if " " in raw and not raw.startswith("<"):
        target, rest = raw.split(" ", 1)
        return target, " " + rest
    if raw.startswith("<") and ">" in raw:
        target, rest = raw[1:].split(">", 1)
        return target, rest
    return raw, ""


def yaml_array(values: list[str]) -> str:
    return json.dumps(values, ensure_ascii=False)


def front_matter(post: Post) -> str:
    lines = [
        "---",
        "layout: post",
        f"title: {json.dumps(post.title, ensure_ascii=False)}",
        f"date: {post.date:%Y-%m-%d %H:%M:%S} +0000",
        f"categories: {yaml_array(post.categories)}",
        f"tags: {yaml_array(post.tags)}",
    ]
    if post.permalink:
        lines.append(f"permalink: {json.dumps(post.permalink, ensure_ascii=False)}")
    if post.post_id:
        lines.append(f"wordpress_id: {json.dumps(post.post_id, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def write_post(post: Post, markdown: str) -> None:
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{post.date:%Y-%m-%d}-{post.slug}.md"
    post.output = POSTS_DIR / filename
    post.output.write_text(front_matter(post) + markdown, encoding="utf-8")


def write_report(posts: list[Post]) -> None:
    metadata_dates = [p.date for p in posts if p.date_source == "metadata"]
    all_dates = [p.date for p in posts]
    missing_meta = [p for p in posts if p.missing]
    missing_images = [(p, img) for p in posts for img in sorted(set(p.missing_images))]
    broken_links = [(p, link) for p in posts for link in sorted(set(p.broken_local_links))]
    manual = [p for p in posts if p.date_source != "metadata" or not p.permalink or p.missing or p.unusual]

    lines = [
        "# Migration Report",
        "",
        "## Inventory",
        "",
        f"- Org posts found: {len(posts)}",
        f"- Converted Markdown posts: {len([p for p in posts if p.output])}",
        f"- Metadata date range: {date_range(metadata_dates)}",
        f"- Generated post date range: {date_range(all_dates)}",
        f"- Posts missing title/date metadata: {len(missing_meta)}",
        f"- Missing images: {len(missing_images)}",
        f"- Broken local links: {len(broken_links)}",
        "",
        "## Converted Posts",
        "",
    ]
    for post in posts:
        output = post.output.relative_to(ROOT).as_posix() if post.output else "(not written)"
        source = post.source.relative_to(ROOT).as_posix()
        permalink = post.permalink or "MANUAL"
        flags = []
        if post.missing:
            flags.append("missing " + ", ".join(post.missing))
        if post.date_source != "metadata":
            flags.append(f"date from {post.date_source}")
        if post.unusual:
            flags.append("review constructs")
        flag_text = "; ".join(flags) if flags else "ok"
        lines.append(f"- `{source}` -> `{output}` ({post.date:%Y-%m-%d}, `{permalink}`): {flag_text}")

    lines.extend(["", "## Posts Needing Manual Review", ""])
    if manual:
        for post in manual:
            reasons = []
            if post.missing:
                reasons.append("missing " + ", ".join(post.missing))
            if post.date_source != "metadata":
                reasons.append(f"publish date inferred from {post.date_source}")
            if not post.permalink:
                reasons.append("old permalink could not be inferred")
            reasons.extend(post.unusual)
            lines.append(f"- `{post.source.relative_to(ROOT).as_posix()}`: {'; '.join(reasons)}")
    else:
        lines.append("- None")

    lines.extend(["", "## Image And Link Issues", ""])
    if missing_images:
        for post, image in missing_images:
            lines.append(f"- Missing image in `{post.source.relative_to(ROOT).as_posix()}`: `{image}`")
    if broken_links:
        for post, link in broken_links:
            lines.append(f"- Broken local link in `{post.source.relative_to(ROOT).as_posix()}`: `{link}`")
    if not missing_images and not broken_links:
        lines.append("- No missing images or broken local links detected during conversion.")

    lines.extend(
        [
            "",
            "## Unusual Org Constructs",
            "",
        ]
    )
    unusual_posts = [p for p in posts if p.unusual]
    if unusual_posts:
        for post in unusual_posts:
            lines.append(f"- `{post.source.relative_to(ROOT).as_posix()}`: {', '.join(post.unusual)}")
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## URL Preservation",
            "",
            "Posts with metadata dates receive explicit `/:year/:month/:day/:slug/` permalinks. Posts without reliable publish dates are converted without explicit permalinks and need manual WordPress URL decisions.",
            "",
            "## Commands",
            "",
            "```sh",
            "python3 scripts/convert_org_to_jekyll.py",
            "python3 scripts/check_site.py",
            "bundle exec jekyll build",
            "```",
            "",
            "Original org files are retained. Markdown/Jekyll files are canonical after migration.",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def date_range(values: list[dt.datetime]) -> str:
    if not values:
        return "none"
    return f"{min(values):%Y-%m-%d} to {max(values):%Y-%m-%d}"


def main() -> int:
    posts = [build_post(path) for path in find_org_files()]
    if not posts:
        print("No org files found", file=sys.stderr)
        return 1
    for post in posts:
        markdown = pandoc_to_markdown(post)
        markdown = copy_and_rewrite_links(markdown, post)
        write_post(post, markdown)
    write_report(posts)
    print(f"Converted {len(posts)} org files into {POSTS_DIR.relative_to(ROOT)}")
    print(f"Wrote {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
