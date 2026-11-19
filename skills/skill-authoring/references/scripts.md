# Scripts in skills

Read this when a skill runs a command or bundles code. Adapted from the Agent Skills guide to using scripts; [NOTICE.md](../NOTICE.md) gives the credit and the changes.

## Commands, or a bundled script

When an existing package does the job, have the skill run it directly with a runner that resolves dependencies on demand, and pin an exact version so the command behaves the same over time:

| Runner | Example | Ships with |
| - | - | - |
| `uvx` (default for Python tools) | `uvx ruff@0.8.0 check .` | uv |
| `pipx run` | `pipx run 'black==24.10.0' .` | OS package managers |
| `npx` | `npx eslint@9.0.0 --fix .` | Node.js |
| `bunx` | `bunx eslint@9.0.0 --fix .` | Bun, for Bun environments only |
| `deno run` | `deno run --allow-read npm:eslint@9.0.0 -- --fix .` | Deno; needs permission flags, and `--` before the tool's own flags |
| `go run` | `go run golang.org/x/tools/cmd/goimports@v0.28.0 .` | Go |

State prerequisites the skill relies on ("Requires Node.js 18+"), and put runtime requirements in the `compatibility` field. When a command grows too complex to get right on the first try, move it into a tested script.

## Referencing scripts

Refer to scripts by paths relative to the skill root, also inside reference files: the agent runs commands from the skill directory. List the scripts in `SKILL.md` with one line each on what it does, and give the exact command at the step that uses it.

## Self-contained scripts

Declare dependencies inside the script, so one command runs it with no install step.

- **Python (default):** a [PEP 723](https://peps.python.org/pep-0723/) block, run with `uv run scripts/x.py`. Pin with [PEP 508](https://peps.python.org/pep-0508/) specifiers, set `requires-python`, and use `uv lock --script` for a lockfile. `pipx run` also reads the block. Prefer the standard library, so the script also runs with plain `python3`.
  ```python
  # /// script
  # requires-python = ">=3.11"
  # dependencies = ["beautifulsoup4>=4.12,<5"]
  # ///
  ```
- **Deno:** `npm:` and `jsr:` import specifiers, such as `import * as cheerio from "npm:cheerio@1.0.0"`. Packages with native addons may fail.
- **Bun:** versioned imports, such as `from "cheerio@1.0.0"`, auto-install when no `node_modules` exists up the tree; if one does, auto-install is off.
- **Ruby:** `require 'bundler/inline'` with a `gemfile do … end` block. Pin every gem, since there's no lockfile; a `Gemfile` or `BUNDLE_GEMFILE` in the working directory can interfere.

## Design for an agent

The agent decides its next step from what the script prints.

- **No interactive prompts.** Agents run in non-interactive shells, so a prompt hangs forever. Take all input from flags, environment variables, or stdin, and fail with the usage line when something's missing.
- **`--help`** is how the agent learns the interface: a one-line description, the flags, examples, and the exit codes. Keep it short. Make the usage line show the command the skill gives (for Python's `argparse`, set `prog`).
- **Error messages** say what went wrong, what was expected, and what to try: `--format must be one of: json, csv, table. Received: "xml"`.
- **Structured output.** Data goes to stdout in JSON, CSV, or TSV; progress and warnings go to stderr. A `--json` flag works well beside a readable default.
- **Exit codes** distinguish failure types (not found, invalid arguments, check failed), documented in `--help`.
- **Idempotent.** Agents retry; "create if missing" beats "fail on duplicate".
- **Strict input.** Reject ambiguous input with a clear error rather than guessing; use closed sets.
- **Dry runs and safe defaults.** Give destructive operations `--dry-run`, and require `--force` or `--confirm` where the risk warrants it.
- **Bounded output.** Harnesses often truncate tool output past 10,000–30,000 characters. Default to a summary or a limit, with flags such as `--offset` for more, or require `--output FILE`.

## Before you ship it

Run the script the way an agent will: from the skill directory, with the exact command the skill gives, plus `--help` and one bad argument. Then delete what the test left behind, such as `__pycache__/`, so it isn't installed with the skill.
