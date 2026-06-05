# Migration Report

## Inventory

- Org posts found: 11
- Converted Markdown posts: 11
- Metadata date range: 2020-07-02 to 2025-10-15
- Generated post date range: 2020-07-02 to 2025-10-15
- Posts missing title/date metadata: 4
- Missing images: 0
- Broken local links: 0

## Converted Posts

- `ai-agriculture/ai-agriculture.org` -> `_posts/2024-05-14-ai-and-ml-in-soil-agriculture.md` (2024-05-14, `MANUAL`): missing date; date from file mtime fallback; review constructs
- `bridge-ai-2025/bridge-ai-2025.org` -> `_posts/2025-06-05-bridge-ai-independent-scientific-advisor-first-100-days.md` (2025-06-05, `/2025/06/05/bridge-ai-independent-scientific-advisor-first-100-days/`): ok
- `c-interface/blog.org` -> `_posts/2022-03-07-coding-sensible-interfaces.md` (2022-03-07, `/2022/03/07/coding-sensible-interfaces/`): ok
- `data-driven-rl/data-driven-rl.org` -> `_posts/2024-06-22-data-driven-reinforcement-learning.md` (2024-06-22, `MANUAL`): missing date; date from file mtime fallback; review constructs
- `drawing/drawing.org` -> `_posts/2022-06-20-drawing-diagrams-and-figures-for-research-articles-and-theses.md` (2022-06-20, `/2022/06/20/drawing-diagrams-and-figures-for-research-articles-and-theses/`): review constructs
- `ev-rl/ev-rl.org` -> `_posts/2021-05-10-keeping-your-cool-while-saving-the-planet.md` (2021-05-10, `/2021/05/10/keeping-your-cool-while-saving-the-planet/`): ok
- `gap-e/gap-e.org` -> `_posts/2022-06-07-the-gap-in-our-ethical-infrastructure-and-know-how-for-smart-cities.md` (2022-06-07, `/2022/06/07/the-gap-in-our-ethical-infrastructure-and-know-how-for-smart-cities/`): review constructs
- `iot-security/iot-security-old.org` -> `_posts/2023-04-19-iot-security-old.md` (2023-04-19, `MANUAL`): missing title, date; date from file mtime fallback; review constructs
- `iot-security/iot-security.org` -> `_posts/2023-04-19-iot-security-and-privacy-should-be-a-national-concern.md` (2023-04-19, `MANUAL`): missing date; date from file mtime fallback; review constructs
- `llm-evaluation/llm-eval.org` -> `_posts/2025-10-15-evaluating-agentic-systems.md` (2025-10-15, `/2025/10/15/evaluating-agentic-systems/`): ok
- `rep-tables/blog.org` -> `_posts/2020-07-02-making-tables-reproducible.md` (2020-07-02, `/2020/07/02/making-tables-reproducible/`): review constructs

## Posts Needing Manual Review

- `ai-agriculture/ai-agriculture.org`: missing date; publish date inferred from file mtime fallback; old permalink could not be inferred; org citation syntax; org citation/bibliography directive: #+BIBLIOGRAPHY; org citation/bibliography directive: #+CSL_STYLE; org citation/bibliography directive: #+PRINT_BIBLIOGRAPHY
- `data-driven-rl/data-driven-rl.org`: missing date; publish date inferred from file mtime fallback; old permalink could not be inferred; org citation/bibliography directive: #+BIBLIOGRAPHY; org citation/bibliography directive: #+CITE_EXPORT
- `drawing/drawing.org`: org table
- `gap-e/gap-e.org`: elisp org link
- `iot-security/iot-security-old.org`: missing title, date; publish date inferred from file mtime fallback; old permalink could not be inferred; org citation syntax
- `iot-security/iot-security.org`: missing date; publish date inferred from file mtime fallback; old permalink could not be inferred; local variables block; org citation syntax; org citation/bibliography directive: #+BIBLIOGRAPHY; org citation/bibliography directive: #+CITE_EXPORT; org citation/bibliography directive: #+PRINT_BIBLIOGRAPHY; org table
- `rep-tables/blog.org`: raw org export directive

## Image And Link Issues

- No missing images or broken local links detected during conversion.

## Unusual Org Constructs

- `ai-agriculture/ai-agriculture.org`: org citation syntax, org citation/bibliography directive: #+BIBLIOGRAPHY, org citation/bibliography directive: #+CSL_STYLE, org citation/bibliography directive: #+PRINT_BIBLIOGRAPHY
- `data-driven-rl/data-driven-rl.org`: org citation/bibliography directive: #+BIBLIOGRAPHY, org citation/bibliography directive: #+CITE_EXPORT
- `drawing/drawing.org`: org table
- `gap-e/gap-e.org`: elisp org link
- `iot-security/iot-security-old.org`: org citation syntax
- `iot-security/iot-security.org`: local variables block, org citation syntax, org citation/bibliography directive: #+BIBLIOGRAPHY, org citation/bibliography directive: #+CITE_EXPORT, org citation/bibliography directive: #+PRINT_BIBLIOGRAPHY, org table
- `rep-tables/blog.org`: raw org export directive

## URL Preservation

Posts with metadata dates receive explicit `/:year/:month/:day/:slug/` permalinks. Posts without reliable publish dates are converted without explicit permalinks and need manual WordPress URL decisions.

## Commands

```sh
python3 scripts/convert_org_to_jekyll.py
python3 scripts/check_site.py
bundle exec jekyll build
```

Original org files are retained. Markdown/Jekyll files are canonical after migration.
