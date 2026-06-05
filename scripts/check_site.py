#!/usr/bin/env python3
"""Validate the generated Jekyll site."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "_posts"
POST_NAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")


def parse_front_matter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def split_target(raw: str) -> str:
    if raw.startswith("<") and ">" in raw:
        return raw[1:].split(">", 1)[0]
    if " " in raw:
        return raw.split(" ", 1)[0]
    return raw


def local_target_exists(source: Path, target: str) -> bool:
    parsed = urlparse(target)
    if parsed.scheme in {"http", "https", "mailto", "tel", "cite"} or target.startswith("#"):
        return True
    path = unquote(parsed.path)
    if not path:
        return True
    if path.startswith("/"):
        candidate = ROOT / path.lstrip("/")
    else:
        candidate = source.parent / path
    if candidate.exists():
        return True
    if parsed.fragment and (candidate.with_suffix(candidate.suffix + ".html")).exists():
        return True
    return False


def validate_posts() -> list[str]:
    errors: list[str] = []
    posts = sorted(POSTS_DIR.glob("*.md"))
    if not posts:
        return ["No Markdown posts found in _posts/"]
    for post in posts:
        rel = post.relative_to(ROOT).as_posix()
        if not POST_NAME_RE.match(post.name):
            errors.append(f"{rel}: filename does not match YYYY-MM-DD-slug.md")
        front, body = parse_front_matter(post)
        for required in ("layout", "title", "date"):
            if not front.get(required):
                errors.append(f"{rel}: missing front matter field `{required}`")
        if front.get("layout", "").strip('"') != "post":
            errors.append(f"{rel}: layout should be `post`")
        for match in LINK_RE.finditer(body):
            target = split_target(match.group(3))
            if not local_target_exists(post, target):
                errors.append(f"{rel}: broken local link/image `{target}`")
        for line_number, line in enumerate(body.splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("#+") or stripped.startswith("[[") or "BEGIN_SRC" in stripped or "END_SRC" in stripped:
                errors.append(f"{rel}:{line_number}: possible remaining org syntax `{stripped[:80]}`")
    return errors


def run_jekyll_build() -> tuple[bool, str]:
    completed = subprocess.run(
        ["bundle", "exec", "jekyll", "build"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    output = (completed.stdout + completed.stderr).strip()
    return completed.returncode == 0, output


def main() -> int:
    errors = validate_posts()
    build_ok, build_output = run_jekyll_build()
    if not build_ok:
        errors.append("bundle exec jekyll build failed")
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        if build_output:
            print("\nJekyll output:")
            print(build_output)
        return 1
    print("Validation passed.")
    if build_output:
        print(build_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
