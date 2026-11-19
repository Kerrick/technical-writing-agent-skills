---
name: agent-skills
description: Use when creating, editing, reviewing, or validating an Agent Skill (a folder with a SKILL.md file), or when the user mentions skills, SKILL.md, skill frontmatter, a skill description that doesn't trigger, bundling scripts or references into a skill, or testing whether a skill works. Covers the format specification, writing effective instructions, tuning descriptions for triggering, eval-driven iteration, and bundled scripts.
license: CC-BY-4.0. Adapted from agentskills.io; NOTICE.md has attribution and changes
metadata:
  author: setdef
  version: "1.0"
---

# Agent Skills

A skill is a folder containing a `SKILL.md` file: YAML frontmatter with at least `name` and `description`, then Markdown instructions. It may also bundle `scripts/`, `references/`, `assets/`, or any other files.

Agents load skills progressively: only `name` and `description` at startup, the `SKILL.md` body when a task matches the description, and other files only when the instructions call for them. So the description alone decides whether a skill triggers, and every line of the body costs context on every run.

For supporting clients and the community, see [agentskills.io](https://agentskills.io/home).

## Creating or editing a skill

1. Read [the specification](references/specification.md) before writing frontmatter or laying out files. It has the field rules and length limits.
2. Read [best practices](references/best-practices.md) before drafting or substantially revising the body.
3. Validate, fix any errors, and repeat until it passes:
   ```bash
   uv run scripts/validate.py path/to/skill-dir
   ```
   Requires [uv](https://docs.astral.sh/uv/), which supplies Python and the pinned `skills-ref` reference library. Run `uv run scripts/validate.py --help` for options and exit codes.
4. If the skill bundles or runs code, read [using scripts](references/using-scripts.md).

## Testing a skill

- If the skill doesn't trigger when it should, or triggers when it shouldn't, read [optimizing descriptions](references/optimizing-descriptions.md).
- To check whether the skill improves outputs, or to compare two versions of it, read [evaluating skills](references/evaluating-skills.md).

## Gotchas

- `name` must exactly match the skill's directory name.
- The PyPI package `skills-ref` provides the command `agentskills`, not `skills-ref`: `uvx --from skills-ref@0.1.1 agentskills validate <dir>`. Prefer `scripts/validate.py`, which also handles `.` as a path.
