# Run: Claude Opus 5.5, medium effort

The first run of the method, finished 2026-11-18. Its skill is the current default, at [`skills/developer-docs/`](../../skills/developer-docs/). This folder has no `skill/` copy of its own while it's the default.

## What was used

| | |
| - | - |
| Model | Claude Opus 5.5 (`claude-opus-5-5`), medium effort, 1M-token context |
| File listing (step 3) | Claude Sonnet 5.5 sub-agents |
| Harness | Claude Code v2.1.311 |
| agent-skills | The copy in [`method/vendor/agent-skills/`](../../method/vendor/agent-skills/), from commit `92b2e67` of the author's skills repo, installed at `~/.agents/skills/agent-skills` |
| Sources | The seven in [`method/sources.toml`](../../method/sources.toml), at the commits pinned there |

## Slots as run

| Slot | Value in this run |
| - | - |
| `${SRC}` | `~/Developer` |
| `${WORK}` | `~/Developer/developer-docs-deltas` |
| `${RUN}` | `~/Developer/technical-writing-agent-skill/claude/opus/5.5/medium` (the layout before `runs/`) |
| `${AGENT_SKILLS}` | `~/.agents/skills/agent-skills` |

## What's here

| Path | Step | What it is |
| - | - | - |
| `baseline/technical-writing/` | 2 | The skill the model wrote from memory. Its `evals/` were written with it and aren't used; eval 1 is missing its input file. |
| `pipeline/findings/` | 4 | One comparison per source, with quoted evidence |
| `pipeline/abstracted-full.md` | 5 | The audit's anonymized rules |
| `pipeline/merged.md` | 6, 8 | The merge, after the check was applied |
| `pipeline/often-broken-check.md` | 7 | The check, with evidence |
| `pipeline/for-the-writer.md` | 8 | The check's writer-safe section |
| `pipeline/kept.md` | 8 | The writer's only input: 47 rules |
| `PLACEMENT.md` | 9 | Where the skill states each rule. Paths are relative to `skills/`. |

Check placement: `uv run method/scripts/check_placement.py runs/claude-opus-5.5-medium/PLACEMENT.md runs/claude-opus-5.5-medium/pipeline/kept.md skills`.

## How this run differed from the method as written

- The first three reading forks (React, Ember, Rails) were asked for "Observed, not counted" and told to grep for evidence in follow-up messages; later ones had both in the template.
- Rails and PostgreSQL each crashed once at the context limit and were redone with narrower or split scopes. See `method/sources.md`.
- Step 7's checker used the "deliberate" test before it was tightened. It also agreed with a by-hand check on only 9 of 13 entries, and its results were used.
- Django's reading prompt asked for every page. The sub-agent returned 6.5 MB, and the fork was given the fixed scope now in `method/sources.toml` as its answer.
- The writer wrote the skill straight into the run folder, and wrote the shared `evals/developer-docs/` as part of step 9.
- The writer named the skill `technical-writing`, as its prompt said. It was renamed `developer-docs` afterwards, a name that says which documentation it covers. The baseline keeps the name the model gave it.
- After the run, the maintainer ruled that no skill may direct an agent to write placeholders to disk. The skill's "Mark anything you couldn't verify" became "Leave out anything you couldn't verify", and the writer prompt now forbids such rules.
- The three rules in `method/maintainer-rules.md` were added to the skill by hand, as its last section, after the run. Later runs get them through `build_kept.py --rules`.
- Output evals and trigger evals haven't been run.
