---
name: changelog-entry
description: Use when the user asks you to write a changelog entry. Not for release notes (use release-notes).
license: MIT-0
metadata:
  author: Platform team
  version: "1.2.0"
---

# Changelog entries

Our changelog is `CHANGES.md` at the repository root. It follows Keep a Changelog, with one exception: the newest unreleased changes sit under `## Next`, not `## Unreleased`.

## Steps

1. Read `CHANGES.md` in full, and the diff or pull request the entry describes.
2. Choose the section under `## Next`: Added, Changed, Deprecated, Removed, Fixed, or Security. A bug fix that changes documented behavior goes under Changed, not Fixed.
3. Write one line per user-visible change, starting with the area in bold: `- **cli:** …`. Leave out refactors, test changes, and CI changes; users can't see them.
4. End the line with the pull request number in parentheses: `(#1234)`.
5. If `## Next` doesn't exist, add it above the newest release heading.

## Gotchas

- `CHANGES.md` is generated into the docs site by `bin/docs`, which fails on a heading level it doesn't expect. Use only `##` for versions and `###` for sections.
- Security entries need the advisory ID (`GHSA-…`) as well as the pull request number.
