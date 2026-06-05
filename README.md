# Blog

This repository is a Jekyll/GitHub Pages migration of an org2blog WordPress archive.

The original org-mode files are retained for reference. Markdown posts in `_posts/` are canonical after migration.

## Local setup

Install Ruby and Bundler, then install the GitHub Pages-compatible dependency set. Ruby 3.3 was used for this migration; macOS system Ruby 2.6 is too old for the current `github-pages` gem.

```sh
bundle install
```

Preview the site locally:

```sh
bundle exec jekyll serve
```

Build the site:

```sh
bundle exec jekyll build
```

## Conversion

Regenerate Markdown posts and copied assets from the org sources:

```sh
python3 scripts/convert_org_to_jekyll.py
```

Validate the generated site:

```sh
python3 scripts/check_site.py
```

The conversion is repeatable and idempotent. It does not delete or move org sources.

## GitHub Pages

This repository is set up for the standard GitHub Pages Jekyll build from the repository branch. Configure Pages in GitHub to publish from `main` after merging this migration branch.
