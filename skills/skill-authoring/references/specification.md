# Specification

Read this before writing frontmatter or laying out a skill's files. Adapted from the Agent Skills specification; [NOTICE.md](../NOTICE.md) gives the credit and the changes.

## Layout

A skill is a directory holding at least a `SKILL.md` file. It may hold any other files. The conventional folders:

| Folder | Holds |
| - | - |
| `scripts/` | Code the agent runs. Self-contained, or with its dependencies documented; helpful error messages; edge cases handled. |
| `references/` | Documentation the agent reads on demand. Keep each file focused: smaller files cost less context. |
| `assets/` | Static resources: templates, images, data files such as schemas or lookup tables. |

## Frontmatter

`SKILL.md` starts with YAML frontmatter, then Markdown.

| Field | Required | Constraints |
| - | - | - |
| `name` | Yes | 1–64 characters. Lowercase letters, digits, and hyphens. No leading, trailing, or consecutive hyphens. Must match the parent directory's name. |
| `description` | Yes | 1–1024 characters. Says what the skill does and when to use it, with the keywords that identify its tasks. |
| `license` | No | A license name, or the name of a bundled license file. Keep it short. |
| `compatibility` | No | 1–500 characters. Environment requirements: intended product, system packages, network access. Most skills don't need it. |
| `metadata` | No | A map from string keys to string values, for properties the spec doesn't define. Use key names unlikely to clash. |
| `allowed-tools` | No | A space-separated string of pre-approved tools, such as `Bash(git:*) Read`. Experimental; support varies by agent. |

No other top-level fields are allowed.

```markdown
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
compatibility: Requires Python 3.11+ and uv
metadata:
  author: example-org
  version: "1.0"
---
```

Valid names: `pdf-processing`, `data-analysis`, `code-review`. Invalid: `PDF-Processing` (uppercase), `-pdf` (leading hyphen), `pdf--processing` (consecutive hyphens).

A weak description: `Helps with PDFs.` A strong one says what and when: `Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.`

## Body

The body has no format restrictions. Steps, examples of inputs and outputs, and edge cases are the usual content. The agent loads the whole file when the skill activates.

## Progressive disclosure

Agents load a skill in three stages:

1. **Metadata** (about 100 tokens): `name` and `description`, for every installed skill, at startup.
2. **Instructions** (under 5,000 tokens recommended): the `SKILL.md` body, when the skill activates.
3. **Resources** (as needed): other files, only when the instructions call for them.

Keep `SKILL.md` under 500 lines, and move detailed material to separate files.

## File references

Refer to the skill's own files by paths relative to the skill root, such as `references/REFERENCE.md` or `scripts/extract.py`. Keep references one level deep from `SKILL.md`; avoid chains of files that point to more files.

## Validation

The skill's `scripts/validate.py` checks the frontmatter against these rules with the reference library, `skills-ref`. To run the library directly, use `uvx --from skills-ref@0.1.1 agentskills validate ./my-skill`: the package is `skills-ref`, but its command is `agentskills`.
