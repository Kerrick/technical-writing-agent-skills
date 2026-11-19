---
name: technical-writing
description: Plans, drafts, and revises developer-facing teaching and reference material (tutorials, quickstarts, how-to guides, API and CLI reference, docstrings, conceptual explanations, docs sites, programming books and chapters, courses and workshops, tutorial video and screencast scripts) using documentation structure and learning science. Use when writing, outlining, restructuring, or reviewing any of these, or when the user wants to teach or explain a library, API, tool, or language to other developers, even if they never say "docs" or "tutorial". Not for rewriting a README (use readme-rewrite) or for UI microcopy.
---

# Technical writing

Docs fail in two ways. The reader can't find the page that answers their question, or the page answers it in a shape they can't use. A novice following steps, an expert looking up a default, and a lead weighing a design all need different pages. Most of this skill is choosing the shape, then proving every claim in it.

## Workflow

Progress:
- [ ] 1. Name the reader
- [ ] 2. Pick one mode per page
- [ ] 3. Write the outcome
- [ ] 4. Gather ground truth
- [ ] 5. Draft from the mode's reference file
- [ ] 6. Run every example
- [ ] 7. Revise against the checklist

### 1. Name the reader

Write one line before anything else: who they are, what they already know, what they are trying to do right now, and how they arrive (reading in order, from search, from an error message, from a link in another page). If the user hasn't said and the answer changes the work, ask. Otherwise state your assumption at the top of the draft so the user can correct it.

Novices and experts need opposite shapes for the same facts. Step-by-step scaffolding that helps a novice slows an expert down, and the terse table an expert wants leaves a novice stranded. Don't serve both on one page; write two and link them.

If the project has a style guide, a Vale config, a docs template, or existing pages, read them and match them. They outrank the defaults in this skill.

### 2. Pick one mode per page

| Mode | The reader is | They need | Read |
| - | - | - | - |
| Tutorial | learning, at study | a guaranteed path to a first success | [tutorials](references/tutorials.md) |
| How-to guide | working, with a goal | steps to a result, assuming competence | [how-to guides](references/how-to-guides.md) |
| Reference | working, looking something up | complete, accurate, identically structured entries | [API reference](references/api-reference.md) |
| Explanation | studying, stepping back | why: context, design decisions, trade-offs | [explanation](references/explanation.md) |

These are the four Diátaxis modes. Long-form work strings them together:

- A book, course, or workshop: also read [books and courses](references/books.md).
- A video series or screencast: also read [video scripts](references/video-scripts.md).
- Either of those, or any tutorial longer than one page: also read [learning science](references/learning-science.md).

Most bad pages mix modes: a tutorial that stops to list every option, a reference entry that tells a story, a how-to that explains the history of the protocol. When a page wants to do two jobs, split it and link the halves.

### 3. Write the outcome

Before drafting, write what the reader can do afterward, as an observable action: "deploy a Rails app with a Postgres database to Fly.io," not "understand deployment." For a reference page, the outcome is the question it answers: "what does `timeout` default to, and what happens when it's hit?" If you can't write the outcome, you don't yet know what the page is for. Ask.

### 4. Gather ground truth

Read the source code, schema, OpenAPI spec, `--help` output, tests, and changelog. Every name, type, default, error, version, and command output in the draft must come from something you looked at in this session, not from memory. Record the version you documented. When you can't verify a claim, mark it `TODO(verify): …` in the draft and tell the user, rather than writing something plausible.

### 5. Draft

Open the reference file for the mode and follow it. Apply the prose and code rules below to every draft. For mechanics (formatting UI labels, placeholders, link text, numbers, accessibility, inclusive and global English), read [style](references/style.md) when the project has no style guide of its own.

For anything longer than a single page, show the user an outline (headings plus one-line outcomes) and get agreement before writing the body. Restructuring an outline is cheap; restructuring a drafted chapter is not.

### 6. Run every example

Run each command and snippet, in order, from the starting state the page declares. Tutorials break between steps more often than within them: a variable defined in step 2 and renamed in step 5, a file the reader was never told to create, a server that needs a restart. Paste real output, trimmed with a visible elision (`...`) when long. If you can't run something, say so to the user and leave a `TODO(verify)`.

### 7. Revise

Read the draft as the reader from step 1, then work through the [revision checklist](#revision-checklist).

## Prose rules

- Use second person, present tense, active voice. Steps are imperatives.
- One action per numbered step. Put the action first, then what the reader should see: "Run `bin/setup`. The output ends with `Ready.`"
- Put the condition before the instruction: "If you use Windows, run …", not "Run … if you use Windows."
- Cut *simply*, *just*, *easy*, *obviously*, *of course*, *basically*, and *note that*. To a stuck reader they say the reader is the problem.
- Open with the answer or the outcome, not "In this guide, we will explore …"
- Headings: tasks as verb phrases ("Rotate an API key"), reference entries as the exact name (`Client#retry`), explanation as a topic or question ("Why jobs are retried at least once"). Sentence case.
- One term per concept. Choose it, define it on first use, and never vary it for elegance. "Workspace," "project," and "org" on one page reads as three things.
- Show, then tell. A short concrete example comes before the abstraction it illustrates.
- Use numbered lists for sequences and bullets for parallel items. Keep reasoning in paragraphs; an argument chopped into bullets loses its *because*.
- Reserve warnings for data loss, security, and money. A page of callouts trains readers to skip them.
- No marketing adjectives: *powerful*, *seamless*, *robust*, *blazing fast*, *best-in-class*.
- Every page must stand alone for someone who landed on it from search. State its prerequisites and link them instead of assuming the previous page was read.
- State facts plainly. Put genuine uncertainty in one sentence where it applies, not as a hedge on every sentence.

## Code rules

- Complete enough to run: include imports, setup, and the file name or directory it belongs in.
- Mark what the reader must replace (`YOUR_API_KEY`) and say where to get it.
- Show the output or the visible result after the code.
- When a step changes existing code, show the change in context: a diff, or the changed lines with a few surrounding lines and the file name. Not the whole file every time, and not an unanchored fragment.
- Use one concept per example, with the shortest code that shows it.
- Use realistic domain names (`invoice`, `customer_id`), never `foo`/`bar`, and keep them consistent across a running example.
- Keep commands and their output in separate blocks so copying a command doesn't copy the output or a `$` prompt.
- Pin versions in install commands.
- Tag every fence with its language.

## Gotchas

- You will invent plausible parameters, flags, defaults, and error messages. Step 4 exists because of this; don't skip it for "well-known" APIs, which change.
- You will default to one template for every page: intro, bullets, conclusion. Pick structure by mode instead.
- The steps an author finds too obvious to write are the ones readers get stuck on: which directory to run a command in, where a config file lives, that a server must restart, that an environment variable must be exported in the same shell, how to get a credential.
- Don't end pages with a summary that restates them. Tutorials end with what the reader learned and where to go next; how-tos end with how to verify the result; reference entries just end.
- Don't present every option as equal. Give the default path and mention alternatives briefly, with when to choose them.
- Document error messages by their literal text so search finds the page.
- Screenshots go stale and can't be searched or copied. Prefer text; when a screenshot is needed, crop it to the relevant region and give it alt text that states what it shows.
- A reader's question in a support thread or issue is evidence of a missing or misfiled page. If the user gives you any, use them to decide what to write.

## Revision checklist

- [ ] The page has one mode, and its title and opening say what the reader will get.
- [ ] Prerequisites, versions, and starting state are stated and linked.
- [ ] Every name, default, and output was verified this session, or is marked `TODO(verify)`.
- [ ] Every example ran in order from the declared starting state.
- [ ] Each term means one thing and is defined at first use.
- [ ] No step depends on knowledge the page neither gives nor links.
- [ ] Banned words and marketing adjectives are gone.
- [ ] Headings alone outline the page; a skimmer could find their step.
- [ ] Anything that's not this page's job has moved to its own page, with a link.
