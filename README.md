# Technical writing agent skills

Two [Agent Skills](https://agentskills.io) that give a coding agent rules for writing documentation: **developer-docs** for tutorials, guides, and reference, and **readme-rewrite** for project READMEs.

## What they are

You use a coding agent, such as [Claude Code](https://claude.com/claude-code), and you want the docs it writes for your projects to be accurate and readable. An Agent Skill is a folder with a `SKILL.md` file of instructions. Your agent loads one when a task matches its description, and follows it.

- **developer-docs** covers tutorials, quickstarts, how-to guides, API and CLI reference, docstrings, conceptual explanations, docs-site landing pages, books, courses, and video scripts. It holds 47 rules. Each rule had to be practiced by at least two of seven well-known documentation sets, such as the [Rust book](https://doc.rust-lang.org/book/), the [Django docs](https://docs.djangoproject.com/), and [MDN](https://developer.mozilla.org/). Before reading them, the model wrote a skill from memory, and the [method](method/README.md) left out every rule that first skill already stated, unless two or more of the documentation sets broke it by mistake.
- **readme-rewrite** rewrites or reviews a README so it does three jobs: tell readers why to try the project, get them started, and link to the rest of the docs. It checks every claim against the code, runs every command it shows, and comes with a script that finds stock AI phrasing in a draft.

Each skill tells the agent to use the other for the other kind of page.

### How they compare with other guides

- With no skill, your agent writes docs from what it already knows about writing them. developer-docs adds only rules the model didn't already follow when the method measured it, and readme-rewrite adds a procedure and checks for one kind of page. Evals that would show how much that changes an agent's output haven't been run yet.
- The [Diátaxis](https://diataxis.fr/) framework sorts documentation into tutorials, how-to guides, reference, and explanation. developer-docs uses the same kinds of page, and adds rules for each one, such as how to mark a code sample that is meant to fail.
- The [Google developer documentation style guide](https://developers.google.com/style) is written for people and covers grammar and word choice at length. developer-docs leaves out what the model already does, so it stays at 161 lines, plus three reference files of 20 to 36 lines that the agent reads only for the kind of page it is writing.
- [Vale](https://vale.sh/) lints prose against a style guide. readme-rewrite doesn't replace it: if your project has a `.vale.ini`, the skill tells the agent to run Vale too and to follow its rules where the two disagree.

## Example: checking a README draft

readme-rewrite includes `scripts/hunt.py`, which the agent runs on each draft. You can run it yourself. Here is a three-line README:

```markdown
# Widget

Widget is a powerful, seamless way to ship apps. The config file decides which targets build.
```

In the skill's folder, run the script on it:

```
$ cd ~/.claude/skills/readme-rewrite
$ uv run -q scripts/hunt.py ~/code/widget/README.md
/Users/you/code/widget/README.md:3: [non-agentic subject] decides
/Users/you/code/widget/README.md:3: [self-praise] powerful
/Users/you/code/widget/README.md:3: [self-praise] seamless
```

Each hit is a phrase to fix or defend. A config file doesn't decide anything, so the agent rewrites the sentence to name what does: "Widget builds the targets you list in the config file." The script exits with 1 when it finds hits and 0 when it finds none.

## Compatibility

| | |
| - | - |
| Format | The [Agent Skills specification](https://agentskills.io/specification). Both skills pass the format validator that this repository's checks run. |
| Agents | Any agent that loads Agent Skills. The install below was tested with Claude Code. |
| Model | developer-docs was made for Claude Opus 5.5 at medium effort. Another model may already follow some of its rules, or miss others it doesn't list. |
| Installing | [Node.js](https://nodejs.org/), for `npx skills`. Or copy the folders by hand. |
| `hunt.py` | Python 3.11 or later, or [uv](https://docs.astral.sh/uv/). It uses only the standard library. |

The evals in [`evals/`](evals/) haven't been run yet for either skill, so there are no results yet on how much each skill changes an agent's output.

## Installation

Install both skills for your user account with the [skills CLI](https://github.com/vercel-labs/skills):

```
npx skills add Kerrick/technical-writing-agent-skills -g -a claude-code -s developer-docs -s readme-rewrite -y
```

This copies each skill into `~/.claude/skills/`. For another agent, change `-a claude-code`; run `npx skills add --help` for the options. To install into the current project instead, leave out `-g`; the skills go in `.claude/skills/` in that folder. To see which skills the repository holds before you install, run:

```
npx skills add Kerrick/technical-writing-agent-skills --list
```

To install by hand on macOS or Linux, clone this repository and link the folders in `skills/` to where your agent looks for skills, so a `git pull` updates them. For Claude Code:

```
git clone https://github.com/Kerrick/technical-writing-agent-skills.git ~/src/technical-writing-agent-skills
ln -s ~/src/technical-writing-agent-skills/skills/developer-docs ~/.claude/skills/developer-docs
ln -s ~/src/technical-writing-agent-skills/skills/readme-rewrite ~/.claude/skills/readme-rewrite
```

On Windows, use `npx skills`, which copies the folders for you.

## Usage

Ask your agent for documentation the way you usually would. Your agent picks a skill by comparing your request with each skill's description. developer-docs describes requests like "write a quickstart for this library" or "document the CLI flags", and readme-rewrite describes requests like "rewrite this README". To be sure, name the skill: "use readme-rewrite to review README.md".

With **developer-docs**, the agent names the kind of page first, reads the reference file for that kind, gathers sources (code, `--help`, tests, changelog), drafts, and then works through a checklist that starts with running every example as written.

With **readme-rewrite**, the agent works in one of three modes:

- **Draft blind, then reconcile**, the default. It drafts from the code without reading the old README, then reads the old one to recover anything true and useful that the draft lacks.
- **From scratch**, when the project has no README or you ask for a fresh start. It never reads the old README.
- **Edit**, for a review or a narrow change. It reads every README-like file in full first, and changes only what you asked.

In every mode it runs the commands it plans to show, runs `hunt.py` on the draft, and works through a review checklist. If the repository doesn't say whether AI agents wrote parts of your project, expect the agent to ask you, so it can add a disclosure.

To get newer versions of the skills, run:

```
npx skills update -g
```

## Documentation

- [skills/developer-docs/SKILL.md](skills/developer-docs/SKILL.md) and its [references](skills/developer-docs/references/): the rules, for reading what your agent will do.
- [skills/readme-rewrite/SKILL.md](skills/readme-rewrite/SKILL.md) and its [references](skills/readme-rewrite/references/): the steps, the style rules, the section plan, and the review checklist.
- [method/README.md](method/README.md): how developer-docs was made, how to make one for another model, and what the first run taught.
- [runs/claude-opus-5.5-medium/](runs/claude-opus-5.5-medium/): every file from the first run, from the skill the model wrote from memory to the 47 rules it kept.
- [evals/](evals/): for each skill, test prompts with input files and assertions, and sample requests marked with whether the skill should trigger on them.

## Reporting problems

Open an issue on [GitHub](https://github.com/Kerrick/technical-writing-agent-skills/issues). Include the prompt you gave your agent, the agent and model, and what it wrote that broke a rule or missed one. If you used a skill on a real project, a report of what happened helps too.

## Contributing

The most useful contributions are eval results for the existing skill and runs of the method on other models. [CONTRIBUTING.md](CONTRIBUTING.md) says what each needs and how to check it before you open a pull request.

## License

You can use the skills, and what you write with them, without conditions. developer-docs is dedicated to the public domain under [CC0 1.0](LICENSES/CC0-1.0.txt), as is most of the repository. readme-rewrite is under [MIT-0](LICENSES/MIT-0.txt), which also requires no attribution.

A few files keep other licenses. The findings files in `runs/*/pipeline/findings/` quote the documentation they compare, and each keeps its source's license; the three that quote Rails and MDN are share-alike, per file. `method/vendor/agent-skills/` is under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). [`REUSE.toml`](REUSE.toml) gives every file's license, following the [REUSE specification](https://reuse.software/), and [`LICENSES/`](LICENSES/) holds the texts.

## How this was made

I use three words for how code and prose comes to exist. Code or prose I wrote, I typed by hand, with nothing generated. Code or prose I wrought, an AI agent generated while I iterated with it, and I reviewed every change before committing it, so I take responsibility for every diff. Code or prose I requested, an agent built with little or no review from me, in the style of a "dark factory."

I wrote the prompts that start the method: the recall and baseline prompts, and the reading-order prompts. Everything else was requested, including both skills, the rest of the method, the evals, and this README. Agents built it from my goals and decisions, with little review of the diffs. In place of review, the repository's rules require `mise run check` before every commit: it runs the Agent Skills validator on each skill, checks that developer-docs and the run's clean-room files carry no source wording, checks that every kept rule is placed in the skill, and runs `reuse lint`. [declare-ai.org](https://declare-ai.org/1.0.0/creative.html).
