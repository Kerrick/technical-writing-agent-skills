# Technical writing agent skills

Three [Agent Skills](https://agentskills.io/) that make a coding agent write better developer documentation, and better Agent Skills:

- **developer-docs** guides tutorials, quickstarts, how-to guides, API and CLI reference, docstrings, conceptual explanations, docs-site landing pages, programming books, courses, and video scripts.
- **readme-rewrite** rewrites, reviews, or writes from scratch a project README, so that it tells readers why to try the project, gets them started, and links to the rest of the docs, with every claim checked against the code.
- **skill-authoring** creates, edits, reviews, and tests Agent Skills: what a skill should hold, its description, its evals, and how to check it.

They're for developers who have an AI agent such as [Claude Code](https://claude.com/claude-code) write or revise their docs, and who want docs that are accurate and readable instead of stock AI prose. An Agent Skill is a folder with a `SKILL.md` file of instructions. Your agent loads one when a request matches its description, and follows it. Each of these two tells the agent to use the other for the other kind of page.

## How they differ from other options

- **No skill at all.** A current model already knows the usual advice: know your audience, use active voice, show examples. developer-docs leaves that out. Its 47 rules come from comparing a docs skill that [Claude Opus 5.5](https://www.anthropic.com/claude) at medium effort wrote from memory with seven documentation sets: [React Learn](https://react.dev/learn), the [Ember Guides](https://guides.emberjs.com/), the [Django docs](https://docs.djangoproject.com/), the [Rails Guides](https://guides.rubyonrails.org/), [The Rust Programming Language](https://doc.rust-lang.org/book/), [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), and the [PostgreSQL manual](https://www.postgresql.org/docs/current/). A rule got in only if two or more of those sets practice it. Rules the model's first skill already stated were left out, unless two or more of the sets break them by mistake.
- **[Diátaxis](https://diataxis.fr/)** sorts documentation into tutorials, how-to guides, reference, and explanation. developer-docs uses the same kinds of page, and adds rules for each one, such as how to mark a code sample that is meant to fail.
- **A style guide** such as the [Google developer documentation style guide](https://developers.google.com/style) is written for people, and covers grammar and word choice at length. developer-docs is 161 lines, plus three reference files of 20 to 36 lines that the agent reads only for the kind of page it is writing. It covers how to plan, check, and finish a page: run every example, verify every fact against the code, and never leave a placeholder in a file.
- **[Vale](https://vale.sh/)** lints prose against a style guide. readme-rewrite includes a script that checks for banned patterns, and when your project has a `.vale.ini`, the skill tells the agent to run Vale too and follow its rules where the two disagree.

In the first round of evals, graded blind on Claude Opus 5.5 at medium effort, developer-docs passed 87% of its 71 assertions, against 56% for the docs skill the model wrote from memory and 46% with no skill. readme-rewrite passed all 19 of its assertions, against 74% with no skill. Graders ranked the skill's output first in all eight evals. Agents using a skill spent about 3.5 times the tokens of agents using none. The [results](runs/claude-opus-5.5-medium/workspace/iteration-1/benchmark.json) include every output and grade.

## Example: checking a README draft

readme-rewrite includes `scripts/hunt.py`, which the agent runs on each README draft. You can run it yourself. Here it is on a test README in this repository, run from the skill's folder:

```
$ uv run scripts/hunt.py ../../evals/readme-rewrite/files/tallyho/README.md
2 em dashes: two or more per page is too many
../../evals/readme-rewrite/files/tallyho/README.md:3: [announced honesty] honestly
../../evals/readme-rewrite/files/tallyho/README.md:3: [em dash] —
../../evals/readme-rewrite/files/tallyho/README.md:3: [vague size or speed] fast
../../evals/readme-rewrite/files/tallyho/README.md:3: [vague size or speed] lightweight
../../evals/readme-rewrite/files/tallyho/README.md:3: [self-praise] powerful
../../evals/readme-rewrite/files/tallyho/README.md:15: [non-agentic subject] decides
../../evals/readme-rewrite/files/tallyho/README.md:15: [internal citation] ADR 3
../../evals/readme-rewrite/files/tallyho/README.md:23: [em dash] —
../../evals/readme-rewrite/files/tallyho/README.md:23: [non-agentic subject] handles
```

Each hit is a phrase for the agent to fix or defend, not proof of a mistake. Line 15 of that README says "the counter decides how to break ties". A counter doesn't decide anything, so the agent rewrites the sentence to name what does. The script skips code blocks and inline code, exits with 1 when it finds hits and 0 when it finds none, and prints JSON when you add `--json`.

## Compatibility

| Requirement | Details |
| - | - |
| Format | The [Agent Skills specification](https://agentskills.io/specification). All three skills pass the format validator that this repository's checks run. |
| Agent | Any agent that loads Agent Skills. |
| Model | developer-docs was made for Claude Opus 5.5 at medium effort. A variant made the same way for Claude Sonnet 5.5 at medium effort is in [`runs/claude-sonnet-5.5-medium/skill/developer-docs/`](runs/claude-sonnet-5.5-medium/skill/developer-docs/). Another model may already follow some of their rules, or miss others they don't list. |
| Installing | [Node.js](https://nodejs.org/), for `npx skills`. Or copy the folders by hand. |
| `hunt.py` (readme-rewrite only) | [uv](https://docs.astral.sh/uv/), or Python 3.11 or later with `python3 scripts/hunt.py`. It uses only the standard library. |

Neither skill has been through its evals yet, so there are no measured results on how much either one changes an agent's output. The evals are in [`evals/`](evals/), and [Evaluating](method/README.md#evaluating) explains how to run them.

## Installation

Install all three skills for your user account with the [`skills`](https://github.com/vercel-labs/skills) command-line tool:

```
npx skills add Kerrick/technical-writing-agent-skills -g -a claude-code --skill '*' -y
```

This copies each skill into `~/.claude/skills/`. To install into the current project instead, leave out `-g`, and the skills go in `.claude/skills/` in that folder. To install only one, name it, as in `--skill readme-rewrite`. For another agent, change `claude-code` after `-a`, or leave out `-a` to choose from the agents the tool detects. Run `npx skills add --help` for the other options. To see which skills the repository holds before you install, run:

```
npx skills add Kerrick/technical-writing-agent-skills --list
```

To install by hand on macOS or Linux, clone this repository and link the folders in `skills/` to where your agent looks for skills, so a `git pull` updates them. For Claude Code:

```
git clone https://github.com/Kerrick/technical-writing-agent-skills.git ~/src/technical-writing-agent-skills
ln -s ~/src/technical-writing-agent-skills/skills/developer-docs ~/.claude/skills/developer-docs
ln -s ~/src/technical-writing-agent-skills/skills/readme-rewrite ~/.claude/skills/readme-rewrite
ln -s ~/src/technical-writing-agent-skills/skills/skill-authoring ~/.claude/skills/skill-authoring
```

On Windows, use `npx skills`, which copies the folders for you.

To use the variant made for Claude Sonnet 5.5 in place of the default developer-docs, install it from its folder:

```
npx skills add https://github.com/Kerrick/technical-writing-agent-skills/tree/main/runs/claude-sonnet-5.5-medium/skill/developer-docs -g
```

Or, from a clone, link it instead of the default:

```
ln -s ~/src/technical-writing-agent-skills/runs/claude-sonnet-5.5-medium/skill/developer-docs ~/.claude/skills/developer-docs
```

Each [release](https://github.com/Kerrick/technical-writing-agent-skills/releases) also has a ZIP of each skill, holding its folder, for installing without git or Node.js: unzip it into your agent's skills folder.

## Usage

Ask your agent for documentation the way you usually would, such as "write a quickstart for this library", "document the CLI flags", or "the README has turned into a changelog, can you clean it up?" Your agent picks a skill by comparing your request with each skill's description. To be sure it uses one, name it: "use readme-rewrite to review README.md".

With **developer-docs**, the agent names the kind of page first and reads the reference file for that kind. It gathers sources (code, `--help`, tests, changelog), drafts, and then works through a checklist that starts with running every example as written.

With **readme-rewrite**, the agent works in one of three modes:

- **Draft blind, then reconcile**, the default. It drafts from the code without reading the old README, then reads the old one to recover anything true and useful that the draft lacks.
- **From scratch**, when the project has no README or you ask for a fresh start. It never reads the old README.
- **Edit**, for a review or a narrow change. It reads every README-like file in full first, and changes only what you asked.

In every mode it runs the commands it plans to show, runs `hunt.py` on the draft, works through a review checklist, and tells you where the code and the old docs disagree. If it can't tell from your repository or your other projects whether AI agents wrote parts of your project, it asks you, so it can add a disclosure.

With **skill-authoring**, the agent decides what the skill should hold before writing it: what the target model already does, what it gets wrong, and which corrections keep recurring. It writes the description for the requests that should and shouldn't trigger it, validates the skill, and sets up evals that compare it with no skill.

To get newer versions of skills you installed with `-g`, run:

```
npx skills update -g
```

## Documentation

- [`skills/developer-docs/SKILL.md`](skills/developer-docs/SKILL.md) and its [references](skills/developer-docs/references/): the rules, so you can read what your agent will do.
- [`skills/readme-rewrite/SKILL.md`](skills/readme-rewrite/SKILL.md) and its [references](skills/readme-rewrite/references/): the steps, the style rules, the section plan, and the review checklist.
- [`skills/skill-authoring/SKILL.md`](skills/skill-authoring/SKILL.md) and its [references](skills/skill-authoring/references/): the workflow, the rules for every skill, and how to evaluate one.
- [How the skill is made](method/README.md): the method that produced developer-docs, its status, how to repeat it for another model, and what the first run taught.
- [Sources](method/sources.md): the seven documentation sets, and why each was read the way it was.
- [The Sonnet run](runs/claude-sonnet-5.5-medium/README.md): the same method on Claude Sonnet 5.5 at medium effort, run entirely by headless sessions, and the variant it made.
- [The first run](runs/claude-opus-5.5-medium/README.md): the model, settings, and every intermediate file from making the current developer-docs, from the skill the model wrote from memory to the [47 rules](runs/claude-opus-5.5-medium/pipeline/kept.md) it kept.
- [`evals/`](evals/): for each skill, test prompts with input files and assertions, and sample requests marked with whether the skill should trigger on them.

## Reporting problems

Open an issue at [github.com/Kerrick/technical-writing-agent-skills/issues](https://github.com/Kerrick/technical-writing-agent-skills/issues). Include the agent and model you used, the prompt you gave it, and what the agent wrote that broke a rule or missed one. If you used a skill on a real project, a report of what happened helps too.

## Contributing

The most useful contributions are eval results for the existing skill and runs of the method on other models. [CONTRIBUTING.md](CONTRIBUTING.md) says what each needs and how to check it before you open a pull request.

## License

What you write with the skills is yours, without conditions. developer-docs is dedicated to the public domain under [CC0 1.0](LICENSES/CC0-1.0.txt), as is most of the repository. readme-rewrite is under [MIT No Attribution](LICENSES/MIT-0.txt), so you can copy, change, and redistribute it without giving credit. skill-authoring adapts the Agent Skills documentation, so it's under [CC BY 4.0](LICENSES/CC-BY-4.0.txt): if you redistribute it, keep its `NOTICE.md`, which gives the credit.

A few files keep other licenses. The vendored copy of the agent-skills skill in `method/vendor/agent-skills/` is under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). The findings files in `runs/*/pipeline/findings/` quote the documentation they compare, and each keeps its source's license, as its opening notice states. The three that quote Rails and MDN are share-alike, per file. [`REUSE.toml`](REUSE.toml) gives every file's license, following the [REUSE specification](https://reuse.software/), and [`LICENSES/`](LICENSES/) holds the texts.

## How this was made

I use three words for how code and prose comes to exist. Code or prose I wrote, I typed by hand, with nothing generated. Code or prose I wrought, an AI agent generated while I iterated with it, and I reviewed every change before committing it, so I take responsibility for every diff. Code or prose I requested, an agent built with little or no review from me, in the style of a "dark factory."

I wrote the prompts that start the method: the recall and baseline prompts, and the reading-order prompts. Everything else was requested, including all three skills, the rest of the method, the evals, and this README. Agents built it from my goals and decisions, with little review of the diffs. In place of review, the repository's rules require `mise run check` before every commit: it runs the Agent Skills validator on each skill, checks that developer-docs and the run's clean-room files carry no source wording, checks that every kept rule is placed in the skill, and runs `reuse lint`. [declare-ai.org](https://declare-ai.org/1.0.0/creative.html).
