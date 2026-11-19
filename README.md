# Technical writing agent skills

Two [Agent Skills](https://agentskills.io) that help an AI coding agent write documentation for developers:

- **technical-writing**, for tutorials, how-to guides, API and CLI reference, explanations, books, courses, and video scripts.
- **readme-rewrite**, for READMEs, which technical-writing leaves out.

technical-writing leaves out the standard advice on writing docs, since your agent already has it. It holds only 47 rules: the ones seven well-known documentation sets follow and Claude Opus 5.5 doesn't. Without them, the model would miss some, get some wrong, and skip others despite knowing them. [METHOD.md](METHOD.md) explains how the rules were found.

A style linter such as [Vale](https://vale.sh) is a different tool. It checks wording against rules, but doesn't plan pages, check claims against the code, or run examples. The two work together: readme-rewrite runs your project's Vale rules when the repository has a `.vale.ini`.

## A first example

readme-rewrite includes a script that finds the phrasing its style rules ban. On a README that grew by appending, it reports:

```
$ python3 ~/.claude/skills/readme-rewrite/scripts/hunt.py README.md
README.md:3: [announced honesty] honestly
README.md:3: [em dash] —
README.md:3: [vague size or speed] fast
README.md:3: [vague size or speed] lightweight
README.md:3: [self-praise] powerful
README.md:15: [non-agentic subject] decides
README.md:15: [internal citation] ADR 3
README.md:23: [em dash] —
README.md:23: [non-agentic subject] handles
2 em dashes: two or more per page is too many
```

The agent runs it after drafting, then fixes or defends each hit. technical-writing's rules are instructions like these, from its `SKILL.md`:

- **Show the wrong form beside the right one.**
- **Show the longhand before the shortcut.**
- **Refer by stable label, never by position.**

## Compatibility

| | |
| - | - |
| Agents | Any agent that loads Agent Skills. The [skills CLI](https://github.com/vercel-labs/skills) installs them for [Claude Code](https://claude.com/claude-code), [Codex](https://github.com/openai/codex), [Cursor](https://cursor.com), [Cline](https://cline.bot), and dozens more. |
| Models | technical-writing was made for Claude Opus 5.5 at medium effort. Another model may already follow some of its rules, or need rules it lacks. |
| readme-rewrite's script | Python 3.11 or later. [uv](https://docs.astral.sh/uv/) is optional. |

Neither skill's evals have been run yet, so how much each improves an agent's docs hasn't been measured.

## Installation

With the skills CLI, on any platform:

```
npx skills add Kerrick/technical-writing-agent-skills -g
```

The CLI asks which skills to install, and for which agents. `-g` installs them for your user account rather than one project. Add `--skill technical-writing` or `--skill readme-rewrite` to install only one.

With git, on macOS or Linux, clone the repository and link the skills into your agent's skills folder. A `git pull` then updates them.

```
git clone https://github.com/Kerrick/technical-writing-agent-skills.git ~/src/technical-writing-agent-skills
ln -s ~/src/technical-writing-agent-skills/skills/technical-writing ~/.claude/skills/technical-writing
ln -s ~/src/technical-writing-agent-skills/skills/readme-rewrite ~/.claude/skills/readme-rewrite
```

`~/.claude/skills` is the folder for Claude Code. For an agent that reads `~/.agents/skills`, such as [Codex](https://github.com/openai/codex), link into that folder instead.

## Usage

Ask your agent for documentation the way you normally would: "write the API reference for the Client class", "turn these notes into a tutorial", "our README is a mess, clean it up". The agent picks the skill whose description matches the request. To be sure, name the skill in your request.

To check a README yourself, run readme-rewrite's script on it, as in the example above. The path depends on where you installed the skill.

## Documentation

- [skills/technical-writing/SKILL.md](skills/technical-writing/SKILL.md) and [skills/readme-rewrite/SKILL.md](skills/readme-rewrite/SKILL.md): the skills themselves.
- [METHOD.md](METHOD.md): how technical-writing was made, what's been tested, and how to make one for another model.
- [runs/claude-opus-5.5-medium/README.md](runs/claude-opus-5.5-medium/README.md): the run that made the current skill.
- [CONTRIBUTING.md](CONTRIBUTING.md): how to contribute a run, eval results, or fixes.

## Reporting problems

Open an issue at <https://github.com/Kerrick/technical-writing-agent-skills/issues>. Say which agent, model, and effort level you used, what you asked for, what the agent did, and what you expected.

## Contributing

Each model needs a separate run of the method, and a run is a dozen or so long agent sessions. A run on Fable 5.2, Sonnet 5.5, Astra 6.2, Sol 6.2, Gemini 4 Neon, or any other model would help, and so would running the evals for the first run. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

You can use the skills, and the documentation you write with them, without conditions. technical-writing and the rest of the repository are dedicated to the public domain under [CC0 1.0](LICENSES/CC0-1.0.txt). readme-rewrite is under [MIT-0](LICENSES/MIT-0.txt), which also requires no attribution.

A few files that record how technical-writing was made quote their sources, and keep those sources' licenses. The vendored agent-skills skill in `method/vendor/` is under CC BY 4.0. The skills you install contain neither. [REUSE.toml](REUSE.toml) gives the license of every file, and [METHOD.md](METHOD.md#licensing-of-the-run-files) explains the exceptions.

## How this was made

> I use three words for how code and prose comes to exist. Code or prose I wrote, I typed by hand, with nothing generated. Code or prose I wrought, an AI agent generated while I iterated with it, and I reviewed every change before committing it, so I take responsibility for every diff. Code or prose I requested, an agent built with little or no review from me, in the style of a "dark factory."

I wrote the prompts that start the method: the recall and baseline prompts in `method/prompts/01-recall.md` and `method/prompts/02-baseline.md`, and the reading-order prompts in `method/sources.toml`. Everything else I requested. Agents (Claude Opus 5.5, with Claude Sonnet 5.5 listing files to read) wrote the technical-writing skill and its baseline, the findings and pipeline files, the evals, the other prompts, the scripts, `REUSE.toml`, METHOD.md, and this README, which an agent rewrote with readme-rewrite. Agents also wrote readme-rewrite, at my request, outside the method. The idea of a skill made only of the gap between a model's baseline and famous documentation is mine, and so is each decision along the way; much of the pipeline's design came from an agent's proposals that I accepted, changed, or rejected. In place of my review stand the agent-skills validator, `method/scripts/leak_check.py`, `method/scripts/check_placement.py`, `reuse lint`, and an agent's spot checks of each findings file's evidence against its source checkout. Under [declare-ai](https://declare-ai.org/1.0.0/assess.html), this is creative assistance.
