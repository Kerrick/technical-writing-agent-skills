---
name: developer-docs
description: Write, edit, structure, or review developer-facing documentation and teaching material - tutorials, how-to guides, API and CLI reference, conceptual explanations, migration guides, changelogs, error-message docs, programming book chapters, and video or screencast scripts. Use this skill whenever the user wants to explain code, a library, an API, or a technical concept to other people, or wants docs, a guide, a course, a chapter, or a tutorial script, even if they don't say "documentation." Not for README files (use readme-rewrite) or for code comments alone.
---

# Developer documentation and technical teaching

Good docs come from two things: knowing exactly who is reading and what they are trying to do, and never saying anything about the software that you haven't verified. Most bad docs fail on one of those two.

## Workflow

1. **Pin down the reader and the job.** Write down, in one line each: who the reader is (what they already know), what they want to accomplish, and what state they're in (evaluating, learning, mid-task, debugging). If the user hasn't said, infer from the repo and state your assumption at the top of your reply, not in the doc.
2. **Choose one mode per page** (below). Mixing modes is the most common structural failure.
3. **Gather ground truth.** Read the code, types, tests, config, and existing docs. Run the thing. Do not describe behavior from memory or from how similar libraries work.
4. **Outline before drafting.** Headings should be the reader's tasks or questions ("Retry failed requests"), not your internals ("RetryManager").
5. **Draft to the mode's rules.** Load the matching reference file:
   - Tutorials, courses, lessons, anything meant to teach: [teaching.md](references/teaching.md)
   - API/CLI/config reference, how-to guides, explanations, migration guides, changelogs, error docs: [reference-and-guides.md](references/reference-and-guides.md)
   - Book chapters or video/screencast scripts: [books-and-video.md](references/books-and-video.md)
6. **Verify, then review** (see the end of this file). Do not hand over a draft whose code you haven't run.

## The four modes

| Mode | Reader is... | Job | Tone |
| - | - | - | - |
| Tutorial | new, learning by doing | Get a guaranteed first success; build confidence | "We" - guided, concrete, no choices |
| How-to guide | competent, has a goal | Solve one specific problem | Imperative steps, minimal explanation |
| Reference | working, needs a fact | Look up exact, complete, neutral facts | Terse, uniform, structured like the code |
| Explanation | curious, away from the keyboard | Understand why and how it fits together | Discursive; may discuss tradeoffs and history |

Rules of thumb: a tutorial that stops to explain design has become an explanation; a reference that tells a story has become an explanation; a how-to that teaches basics has become a tutorial. Link between modes instead of merging them.

## Principles that hold in every mode

- **Lead with the answer.** The first paragraph says what the page is for and who it's for. Put the most common case first, edge cases later.
- **One idea per paragraph, one task per procedure.** Procedures are numbered, one action per step, with the expected result stated after steps whose outcome isn't obvious.
- **Show, then name.** Give a minimal working example before the abstract description. Examples are the most-read part of any page.
- **Use the reader's words,** then introduce the project's term once, defined at first use. Pick one term per concept and never vary it for style; synonyms read as different things in technical text.
- **State prerequisites and versions** explicitly: language/runtime version, OS differences, required accounts, permissions, and the version of the software the page is true for.
- **Be specific.** "Returns `null` if the key is absent" beats "handles missing keys gracefully." Numbers, units, defaults, limits, and error names beat adjectives.
- **Cut filler and marketing.** Drop "simply," "just," "easy," "obviously," "of course," and "please note." They make stuck readers feel stupid. Say what is true instead.
- **Active voice, present tense, second person.** "The server returns a 404," not "A 404 will be returned." Short sentences, but vary rhythm so it doesn't read as a list.
- **Make code copy-paste safe.** Complete enough to run, one command per block, no `$` prompts inside copyable blocks, real-looking placeholders in an obvious format (`YOUR_API_KEY`), output shown in a separate block, language tag on every fence.
- **Warn before the hazard,** not after it. Destructive or irreversible steps get the warning in the step before, with how to undo it if possible.
- **Write for scanning and for search.** Descriptive headings, front-loaded link text ("see the [retry policy](...)", never "click here"), alt text for images, exact error strings and command names in the text so people can find the page by pasting them.
- **Every example should be one a user could actually need.** Avoid `foo`/`bar` when a domain example (orders, users, invoices) costs nothing and carries meaning. Use one running domain across a doc set.

## Gotchas

- Docs rot where they restate code. Prefer generating reference from source (OpenAPI, type signatures, `--help`, docstrings) and write only what generation can't: purpose, constraints, interactions, examples. If you hand-write a parameter table, say in your reply that it needs a drift check.
- Don't document intended behavior as if it were actual behavior. If the code and an existing doc disagree, tell the user which one you believe and why; don't silently pick.
- Placeholder values in examples that look real (a plausible-looking token, real domains, real emails) get copied into production. Use reserved ones: `example.com`, `192.0.2.x`, clearly fake keys.
- Don't invent outputs. Run the command and paste what it printed, trimmed with an explicit `...`. If you can't run it, mark the output as illustrative and say so to the user.
- Translators and non-native readers are most of the audience: avoid idioms, jokes, culture-specific references, and phrasal verbs ("spin up", "bail out") where a plain verb works.
- Don't explain what the reader's stated level already covers (what a function is, what HTTP is) but do define anything specific to this project, however small.
- Headings written as nouns ("Authentication") are fine in reference; in guides prefer verbs ("Authenticate a request").
- Changing a name, flag, or URL in one place means searching for every other occurrence. Grep the docs before finishing.
- One-sentence "why" beats a rule. If a convention (for example, "always pass an idempotency key") is non-obvious, say what goes wrong without it.

## Verify before handing over

Run through these in order and fix what fails:

1. Every code sample was executed (or type-checked/compiled at minimum) against the version the docs claim, and output matches what's shown.
2. Every command, flag, field, status code, default, and limit was checked against source or a real run.
3. A reader following only this page, starting from its stated prerequisites, reaches the stated result with no step missing. Walk it literally, as a fresh machine would.
4. Terms are consistent; each is defined at or before first use.
5. Every internal link and anchor resolves; every external link is to a stable, versioned URL where possible.
6. The page stays in its mode; stray explanation in a how-to or stray steps in a reference are moved or linked.
7. Nothing in the page will be wrong in a month for avoidable reasons (hard-coded versions in prose, screenshots of text, duplicated tables).

When delivering, tell the user what you ran and what you could not verify. Don't claim "tested" for anything you didn't execute.
