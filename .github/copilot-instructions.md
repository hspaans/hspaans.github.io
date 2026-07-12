# Copilot Instructions for hspaans.github.io

## Project Overview
This is a personal blog and portfolio site built with **Sphinx** and hosted on GitHub Pages. Blog posts are written in **ReStructuredText** (.rst files) and organized by year under `docs/blog/`.

## Key Structure
- `docs/` — Sphinx source files, blog content (organized by year in `docs/blog/2025/`, `docs/blog/2026/`, etc.)
- `_build/` — Built HTML output (generated; do not edit)
- `src/` — Python package code (if any)
- `tests/` — Test files
- `.github/workflows/` — CI/CD: CodeQL, dependency review, Pages deployment

## Build & Run
- **Build HTML**: `sphinx-build -M html docs _build`
- **Clean build**: `sphinx-build -M clean docs _build`
- **Dev server**: `sphinx-autobuild --port 8000 docs/ _build/` (auto-rebuilds on file changes)
- **Link check**: `sphinx-build -M linkcheck docs _build`

## Project Conventions
- Blog posts use **ReStructuredText** format (.rst)
- All blog metadata (title, author, date, category, tags) goes in the post's .rst file header/directives
- Posts are final once in `docs/blog/YYYY/` — avoid rewriting published content
- URLs are derived from filenames; use hyphens not underscores (`fluent-interface.rst` not `fluent_interface.rst`)
- Configuration is in `docs/conf.py` (Sphinx settings)
- The site uses **Furo** theme for styling

## When You Help
- If asked to add a new blog post, create it under `docs/blog/YYYY/` with proper .rst structure
- If asked to edit docs, rebuild with `sphinx-build -M html docs _build` and test with the dev server
- Link checks are automated in CI; prefer fixing broken references rather than ignoring them
- Keep Python dependencies minimal and documented in `pyproject.toml`
