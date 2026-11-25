---
name: readme-rewrite
description: Use when rewriting, substantially editing, restructuring, or reviewing a project README (README.md, README.rdoc, or similar), rewriting one from scratch, or writing the first one for a project that has none, including when a README has grown by appending or reads like stock AI prose. Use it to make the README work for marketing, onboarding, and indexing, with every claim checked against the code. Not for other documentation pages, such as tutorials, guides, or API reference (use developer-docs). Load prose-style as well, for the sentences.
license: MIT-0
metadata:
  author: Kerrick Long
  version: "1.2.0"
---

# Rewrite a README

A README goes bad when people append to it. In each session, an agent adds a paragraph without reading the whole, and the file turns into a log. Fix that by rewriting for coherence, not by adding to it.

## Step 0: Choose the mode

- **Draft blind, then reconcile (default).**
  1. Draft from the code alone (steps 1 to 9), without reading the old README in any form: not the file, not `git show`, `git log -p` or `git diff` on it, not a search whose output prints its lines, not its rendered page. If you read it first, you'll copy its structure and phrasing. Write the draft to a new file, so you never have to open the old one to replace it.
  2. When the draft has passed step 9, read the old README in full, as a checklist rather than a model. For each thing it says that the draft doesn't, check it against the code and ask whether the reader needs it. Add what passes, in the draft's structure. Keep wording the maintainer chose on purpose, such as an existing disclosure. Then move the draft over the old file.
- **From-scratch mode.** If the project has no README, or the maintainer wants a fresh start ("rewrite it from scratch", "start over", "throw out the old one"), do part 1 only, and never read the old README.
- **Edit mode.** For a review, or a narrow change the maintainer asked for ("fix the install section"), read every README-like file in full first: README.md, README.rdoc, README.txt, and any sibling that describes the project. Do not search for the paragraph to change and patch it. Change what was asked, so the whole file stays coherent.

If you are about to append a paragraph to a README you have not read in full, stop.

In the first two modes, anything in the repository besides the code's behavior may echo the old README: other docs, package metadata, docstrings, comments, CLI help text. Use it only to find what to check. Take nothing from it as fact, structure, or wording.

Never write a placeholder, a question, or a note to the maintainer into any file. The maintainer asked for the writing so they don't have to do it: what you write is final. Bring up in chat only what truly needs their judgment, where a wrong call would cause real harm, and keep that as short as you can. For everything else, take the answer the evidence supports that claims the least on the maintainer's behalf, and list those calls in your report, so the maintainer can overturn one at a glance.

## Step 1: Ground every claim in the code

- Read the entry points, the CLI definition, the config schema, the manifest and lockfile, the tests, and the CI configuration.
- Run the commands you plan to show. Copy the output you rely on. A command you did not run does not go in. Run install commands in a scratch directory or container, not the user's environment.
- Treat other documentation (design notes, plans, older READMEs, changelogs) as leads, not evidence. Each can be out of date. Confirm against code or a run.
- If the docs say something the code doesn't do, trust the code. Report the disagreement to the maintainer.
- If something is not built yet, check the code, then say so in one sentence (step 5).
- Check where else the README is shown. If the project publishes it to a package registry (for example, through `readme` in `pyproject.toml`), the registry shows it without the repository around it, and relative image paths and links can break there; PyPI doesn't resolve them. Use absolute URLs for those.

## Step 2: Name the audience and the three purposes

Write down who reads this: the person who might use the project, in their words ("a developer with a finished script who wants to ship it"). Not maintainers, not you. Every sentence must matter to that reader.

A README has three jobs:

1. **Marketing.** Convince the reader to try it. Say what problem it solves, who it is for, how it compares with the alternatives they know, and answer their likely questions. Show evidence (step 6).
2. **Onboarding.** Get them started, and show the whole path: install, first run, everyday use, release or upgrade. They should see the journey before taking it.
3. **Index.** Link to the API docs, guides, changelog, issue tracker, and CONTRIBUTING. Say in plain words what each linked page holds.

Anything that's for none of the three, or for a different reader, belongs elsewhere (step 7).

## Step 3: Plan the sections

Use a conventional order. Readers scan for the headings they expect. See [references/section-plan.md](references/section-plan.md) for the template and what each section holds.

In each heading, name the section's content in the reader's terms. "Compatibility" is better than "What CI checks". Skip cleverness. A reader who skips a heading because it looks internal will miss the section.

## Step 4: Draft in plain style

Load the prose-style skill and follow it for every sentence: who acts, plain words, the banned patterns, and how to state claims. For a README, also:

- Do not explain a term the audience already knows. Do explain every term they do not, the first time it appears (a config file, a tool name). Say what it is, where it goes, and whether it is optional.
- Show a concrete first example early, with the output.
- Put each proper noun (tools, projects, platforms) in a link the first time it appears in a section.
- Put the reader's goal before the mechanism. Lead with what they can do.
- Do not tell readers to create what they already have. Start from where the reader is. A reader of a packaging tool has a program already, so start from "In your project folder, run ...".

## Step 5: Handle unproven claims without a confessional tone

- State limits as facts with a scope: "Each build runs on the platform it's for. Building for Windows needs a Windows machine." No apology, no self-praise.
- Keep caveats in a section for caveats (Compatibility, Limitations). Do not mix them into "Who it is for" or "Alternatives".
- Write status for users: what works today, on which platforms, what is planned. Use a version badge instead of "version X is the latest".
- Do not claim what you have not tested. Mark unbuilt features as not available, with one line, or leave them out.
- State a limit only when it changes what the reader can do or should expect: a platform, a version, a model, a prerequisite, a risk to their data.
- Don't narrate the project's proof, as prose-style defines it. Cut it, or move it to contributor docs (step 7). The AI disclosure (step 8) is the one place to name the project's checks.

## Step 6: Use evidence, not invented proof

Use what exists: CI badges, release downloads, real projects that use it (only if you can verify), benchmarks you ran, with their numbers. No made-up testimonials, user counts, or logos. If there is no social proof yet, show a working example with its output. A CI badge is all the evidence of testing a reader needs, since it links to the runs.

## Step 7: Keep contributor material out, without losing it

Build instructions for the project itself, test commands, architecture decision records, release procedure, internal CI details, and design history don't belong in the README. The README's Contributing section is a pointer: one or two sentences and a link. Do not cite internal records (ADR numbers, plan files) in a user-facing README.

Move that material; don't delete it. Remove only what you've confirmed against the code is false or obsolete, and report each removal. To choose where each piece goes, take the first of these that fits:

1. Where the repository already keeps that kind of material: an existing CONTRIBUTING, docs folder, changelog, ADR folder, or wiki.
2. Beside what it describes: a folder's README for material about that folder, or the docstrings and `--help` text for detail about an API or CLI.
3. `CONTRIBUTING.md`, for how to contribute: setup, tests, and releases.
4. The ecosystem's documentation location, only if the project's tooling uses it (for example, Sphinx's `docs/`, or RDoc's and YARD's `doc/`).
5. Otherwise, the closest fit to the options above. Say which you chose and why in your report.

Don't invent a new location, and don't copy one from another project because it worked there. Link each moved piece from the README's Documentation section, and say in your report what moved where.

## Step 8: Disclose AI involvement as a fact

If agents wrote or changed the code or docs, and the maintainer discloses AI involvement (they do in their other projects, or they say so; ask if you can't tell), say so near the end, in a short paragraph, in the project's terms. See [references/ai-provenance.md](references/ai-provenance.md). Follow the maintainer's existing house pattern if one exists. Do not apologize and do not boast.

## Step 9: Hunt for problems, then review

1. Run the prose-style skill's `scripts/hunt.py` on the draft, as that skill describes. For each hit, fix the sentence or defend it. Run it again until every remaining hit is one you can defend.
2. If the repository has a Vale configuration (`.vale.ini`), run `vale` on the draft too. Its rules are the project's style guide: where they and the prose-style rules differ, follow Vale's.
3. Read the draft once as the target reader who has never heard of the project. Note where you would stop reading.
4. Run the review checklist in [references/review-checklist.md](references/review-checklist.md). It comes from detailed maintainer feedback on a real first draft.
5. Re-run every command shown. Confirm every link resolves.
6. If the maintainer reviews by file, edit the file at its real path, not a copy.

When you change a README in a repo that has agent instructions, follow them. If they lack a rule against append-only edits, propose adding: "Editing README.md or README.rdoc requires reading both files in full first, then rewriting for coherence, not appending."
