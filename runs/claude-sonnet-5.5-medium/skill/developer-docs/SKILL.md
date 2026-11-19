---
name: developer-docs
description: Use when writing, editing, restructuring or reviewing developer-facing tutorials, guides, how-tos, reference, explanations, books, courses or video scripts, including requests that don't say "docs", such as "write a walkthrough", "explain how this API works" or "turn this into a lesson". Not for READMEs (use readme-rewrite) or UI microcopy.
metadata:
  author: Kerrick Long
  version: "0.1"
---

# Developer docs

Rules for developer documentation. You already know standard technical writing practice; this covers what goes wrong or differs from it.

## Workflow

1. Name the page's job and its one dominant kind of content: tutorial, how-to, reference, explanation, book, or documentation set.
2. Read the reference file for that kind, if there is one:
   - Tutorial, how-to, course, video script, book or documentation set: [references/walkthroughs-and-books.md](references/walkthroughs-and-books.md)
   - Reference or troubleshooting page: [references/reference-pages.md](references/reference-pages.md)
3. Write, applying the rules below.
4. Run the checklist. Fix what fails, then run it again.

## Pre-publish checklist

- [ ] Every code sample and command was run, or at least compiled or type-checked, against the version the page claims. The real output was compared with what the text shows. Names, arguments, status codes and sample data agree between sample, prose and output.
- [ ] Pasted output comes from a real run of the exact code and version shown, and matches the code.
- [ ] No version numbers, support facts or time-relative words ("currently", "new", "recently") in running prose.
- [ ] One term per concept, spelled identically everywhere. Every rename was searched for and updated in all pages, including sibling pages.
- [ ] Every internal link, anchor and named cross-reference (listing, section, function) resolves and names the right target. In a versioned set, links land on the reader's own version.
- [ ] No placeholder, question or note to the maintainer in any file.
- [ ] For tutorials, how-tos and books, also the checklist in the walkthroughs reference.

## Rules for every page

### Judge a page by the reader's job

Each page has one job and one dominant kind of content. Other kinds (a short explanation of what was just built, rationale, internals, advanced depth, a short catalogue) may appear only as short, bounded sections that are labelled, sit off the numbered steps in a consistent position (after the thing they explain), can be skipped without losing the thread, and link to the full treatment. Exhaustive lookup tables, setup and cross-cutting topics go on their own page. Long material of another kind gets its own page.

### Avoid content that goes stale

Keep version numbers, support and compatibility facts, and time-relative words out of running prose. Hold version and support facts in one structured, ideally generated, place per page. Don't hard-code environment-specific output, and don't keep statements that a newer page contradicts.

The exception is a change note saying what changed in which version and what an upgrader must do. It may sit beside the rule it affects as a short, self-contained, set-apart block that can be deleted without touching the surrounding text, always with an explicit version, and removed after a fixed number of releases. When defaults or behaviour change, record the history both beside the setting and in a per-release roll-up.

### State what a page leaves out and where the rest lives

- Say where an explanation is a simplification, and make sure every skipped edge case lands on an exhaustive page that the simple page links to.
- Say that a guide covers only the common path and where the rare cases are documented.
- Say when a table or list is a selection, and point to the complete source.
- State the environment the page assumes.
- Put the omission in one sentence where the reader would look, with a link to the exact section.

### One term per concept, everywhere

Use one term per concept and spell it identically, parameter names included, across prose, code, output, sibling pages and cross-references. Define a concept once. When you rename or change anything, search the docs and update every occurrence, including related pages (a guide must not lag its reference). Examples must not contradict sibling pages, and output formats must match across pages. Prose that names a listing, function or section must name the right one.

### Links, anchors and versions

- Every internal link, anchor and named cross-reference must resolve and name the right target. Recheck after any restructuring or renaming.
- In a documentation set published in several versions, cross-links land on the version the reader is reading, using the alias that tracks the same release. Pin to a specific version only when the sentence is about that release or points to legacy docs.
- When a page leans on an idea defined elsewhere, link to the specific section that defines it. Give headings stable explicit identifiers. When you rename a heading, keep the old anchor in place and mark it as retained so nobody removes it.

### Define terms

Mark a term typographically at the point you define it, in one consistent style. Where you give an everyday word a narrow technical meaning, say so once and use a different phrase for the broad idea.

### State shared facts once

Shared facts (setup steps, authentication, shared lists) belong in one place that other pages link to. Don't paste the same instructions, generated method lists or passages into several pages. The one exception is the single costliest trap: repeat it where a reader first meets the feature, in the length that suits the page (a clause in a lesson, a paragraph in a guide, the exact rule in reference), because readers often arrive without passing through the overview. Treat each copy as something to recheck when its source changes.

### Keep prose literal

Keep wording literal enough to survive translation and a non-native reader: avoid idioms, figurative phrasing, culture-bound references, phrasal verbs and jokes that need cultural context.

In teaching and community pages (tutorials, books) a warm, personal voice is legitimate: write as one person to another, pose the problem before the answer, prefer concrete statements to stacked superlatives, and check after any editing pass that these qualities survived. Light humour is acceptable there. Keep lookup pages plain.

### Gender-neutral wording

When writing about hypothetical or unspecified people, avoid gendered pronouns: use singular "they" or reword so no pronoun is needed.

### No placeholders on disk

Never write a placeholder, a question, or a note to the maintainer into any file. The maintainer asked for the writing so they don't have to do it, so what you write is final. Bring up in chat only what truly needs their judgment, where a wrong call would do real harm, and keep that as short as you can. For everything else, take the answer the evidence supports that claims the least on the maintainer's behalf, write it as final, and list those calls in your report.

### State verified facts plainly

Before you qualify, shrink, or cut a sentence, name the specific false or unverified fact it states. If you can't name one, it isn't an overclaim, so leave it as written. A statement of what something is for, or what it does, is not an overclaim. Never attach how narrow the proof was ("tested with", "in our testing", "as far as we know", "should work").

### State a limit only where it changes what the reader can do

State a limit only when it changes what the reader can do or should expect: a platform, a version, a model, a prerequisite, a risk to their data. State it once, as a fact, where the page keeps its caveats. Work the maintainer hasn't done yet, such as tests or benchmarks not yet run, isn't a limit for the reader. It belongs in contributor documentation.

## Rules for pages with code or examples

### Show wrong code as wrong, inside the block

When you show a wrong or discouraged pattern, mark it as wrong inside the code block itself (a short comment prefix), so a copied snippet still carries the warning. Put the right version next to it, and say in the next sentence why the wrong one fails.

### Teach the current approach first

Examples teach habits. Write every example in the currently recommended, non-deprecated, safe style as if it will be copied into production, and order the favoured approach first. Put superseded or older forms after it, short and labelled as superseded, naming what replaces them, so readers recognise them in existing code. Where an older edition of the docs exists, point to it. When you remove documentation for a retired feature, leave a short pointer to the archived version and any migration note.

### Annotate only what isn't obvious

After a code sample, list only the lines or choices whose purpose isn't obvious, one short point each, and say the rest is self-explanatory. In example code, don't comment what a line plainly does. A very small example may be walked through line by line.

### Say what each example shows

Give every example, listing or figure a title or caption that says what it demonstrates, including that it doesn't work yet when that is the point. Never use a bare number or generic label. Number only the listings that later text refers back to.

### Show what a convenience expands to

When a call or shortcut hides several steps, show the lower-level steps or result it produces next to it, and label the shortcut as doing the same thing, so the reader can check their mental model.

### Scope the running example

Declare the example domain near the start of a page. Keep one domain through a sequence that builds on itself (a chapter, a section or a learning path) and evolve the same example across it. Change domain across pages that don't build on each other, or when a concept needs differently shaped data. In that case use a small purpose-built dataset shown inline. Reference examples are self-contained and must not depend on a lesson's data. Don't force one scenario on a whole documentation set.

### Let readers check claims themselves

Show the input data, the operation and the exact result together, so a reader can verify the result by hand. Teach a concrete method for tracing behaviour by hand (substitute values, list events in order) and reuse it across pages. Where a documented default or built-in list can be inspected, give the command that shows the live value on the reader's own system.

## Rules by kind of content

### Help readers choose between overlapping options (how-to, reference, explanation)

Where features or approaches overlap, say how to choose. Each entry states the condition, or the one difference that matters, that separates it from its nearest alternative, and links to it. Where there are many options, give a decision aid keyed to the reader's circumstances that names the recommended option, ordered from least to most effort or control with when to move up. Say when not to use something and what to use instead. In a page's opening, say what the subject is not and name the neighbour it is most often confused with.

### Gloss background briefly (tutorial, guide, explanation, book)

Link out for background the target reader is assumed to have. At first use, give a one- or two-sentence gloss of general terms or language features, with an outside link, set apart where the page's conventions allow so experienced readers can skip it. Where a topic's own explanation depends on small background the reader may lack, teach it in a bounded, titled aside that says what it leaves out. Never teach background at length.

### State a feature's limits and silent failures (reference, guide, explanation)

Where docs present a safeguard, guarantee, filter or check as protecting the reader, state its limits: what it does not catch (a test run may miss cases), which operations bypass it, and what outside mechanism must complement it. Document failures that produce no error (silent no-ops, dropped work, quiet fallbacks) where they occur.

## Gotchas

- Samples whose syntax, values or output don't match the prose are the typical failure. A misspelled name, the wrong status or helper named in prose, or a wrong argument is what a run or a reread catches.
- Writing "as of 3.2, …" or "recently added" into running prose goes stale. Banning upgrade notes outright loses useful information. Use the set-apart change note.
- A partial list reads as complete, and skipped cases are silently missing, unless the page says what it leaves out.
- Names, values and cross-references drift between prose, code and sibling pages after a rename.
- Pinning links to one version leaves readers on the wrong release.
- A heading rename silently breaks inbound links.
- Readers can't tell a defined term from an ordinary word unless it is marked.
- Showing the bad version with the caveat only in prose gets it copied as correct.
- Leading with an outdated or unsafe pattern gets it copied.
- Narrating every line of a sample buries the lines that need explaining.
- Labelling examples "Example 1" tells readers nothing about what each is for.
- Without the expansion shown, readers can't see what a shortcut does, and their mental model is wrong.
- Reader must take results and defaults on trust unless the data, operation and result are shown together.
- Listing overlapping options as equals leaves the reader to pick wrongly.
- Bending unrelated pages into one scenario, or writing a reference example that only runs on a lesson's data, breaks the running-example rule.
- Pasting the same setup everywhere lets the copies drift. Linking everything misses the costliest trap.
- Assuming every term is known, or detouring into a long lesson on prerequisites, both fail the reader.
- Without stated limits the reader assumes protection that isn't there.
- Defaulting to "he" for a hypothetical user or developer.
- Cold teaching text, or idioms and jokes that non-native readers trip on.
- Leaving a marker such as `TODO(verify)` or `[TO CONFIRM]` in a file hands the work back to the person who asked for it.
- Qualifying, shrinking or cutting sentences that were true as written makes readers trust the page less than the evidence deserves.
- Apologizing for unfinished work in user-facing pages tells the reader nothing they can act on.
