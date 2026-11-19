---
name: developer-docs
description: >-
  Use when planning, drafting, revising, or reviewing developer-facing teaching
  and reference material: tutorials, quickstarts, how-to guides, API and CLI
  reference, docstrings, conceptual explanations, docs-site landing pages,
  programming books and chapters, courses and workshops, and tutorial video or
  screencast scripts. Use it whenever the user wants to teach or explain a
  library, API, tool, or language to other developers, even if they never say
  "docs", "documentation", or "tutorial". Not for writing or rewriting a README
  (use readme-rewrite) or for UI microcopy.
license: CC0-1.0
metadata:
  author: Kerrick Long
  version: "1.0.0"
---

# Developer docs

These rules add to standard developer-docs practice; they don't restate it. Where a rule here conflicts with advice you would usually follow, follow the rule here.

## Workflow

1. Name the page's kind and its one primary job (see **One primary job per page**). Then read the reference file for that kind:
   - Tutorial, quickstart, lesson, book chapter, course module, workshop, video or screencast script, or exercises: read [references/lessons.md](references/lessons.md).
   - API, CLI, or configuration reference entries, or docstrings: read [references/reference-entries.md](references/reference-entries.md).
   - Anything made of several pages, such as a docs site or section, a landing page, a tutorial series, a book, or a course: read [references/sets-and-sequences.md](references/sets-and-sequences.md).
   - How-to guides and explanations need only this file.
2. Apply the rules for every page below, plus the rules in **Rules for several kinds of page** tagged with your page's kind.
3. Gather sources before drafting: code, schema, `--help`, tests, changelog. Note the version you are documenting.
4. Draft.
5. Work through the **Pre-publish checklist** and fix every item that fails before you hand the page over.

## Rules for every page

### Structure

**One primary job per page.** Give each page one primary job: teaching by doing, getting a task done, supporting lookup, or explaining why. A page may carry a short piece of another kind of material when that piece serves the primary job. It must sit in a clearly labeled section or a skippable aside, in the same position on every page of that kind. For example:
- brief rationale and a quick recap woven into a lesson that is read in order;
- a labeled section of shared concepts on a reference landing page, kept apart from the member listing;
- a motivating example, a short explanation, and a compact usage summary on a single-feature page, in the same order for every feature.

When the other material is large, or readers need it on its own, give it its own page and link both ways. Don't paste reference catalogs or copies of reference tables into a walkthrough. Don't let a task exist only inside a reference entry: give every common task its own task page.

**One page can serve beginners and experts.** Start with the simplest, most common use, move steadily to advanced uses, set material only some readers need apart in clearly titled sidebars they can skip, and leave rare edge cases to the reference. This matters most on feature guides.

**Say what isn't covered or done.** State plainly what the tool or feature does not do, and which responsibilities stay with the reader. When a page leaves out something a reader might expect, say so at that point and link to where it's covered.

**No restating conclusions.** Outside a sequence of lessons, don't end a page with a conclusion that restates it. (Lessons in a sequence get a fixed closing; see [references/lessons.md](references/lessons.md).)

**Keep one maintained copy of anything that changes**, and point to it instead of copying it:
- For a step that depends on another project's software, document only how it connects to yours and link to that project's own instructions.
- Keep FAQ answers to a sentence or two, with a link to the page that holds the full answer.
- When teaching a subset of a large API, say it's a subset and link the complete list.
- Teach the command or introspection that prints the current, complete answer.
- Keep support, compatibility, and availability data in one structured source, rather than hand-writing version numbers into prose.

**Refer by stable label, never by position.** Refer to other parts of a document by a number for code samples and figures, a section name, or what an example shows. Never write "above" or "below". When returning to a sample after a long gap, show it again instead of sending the reader back. Recheck numbered references whenever samples are added or removed.

### Examples and code

**Frame every example.** Introduce every example with a heading or a sentence naming the task or behavior it demonstrates and what to watch for, and follow it with an explanation of the result.

**Realistic names for real use; neutral names only for pure mechanism.** Use realistic domain names (`invoice`, `customer_id`) when an example models real use, shows a task, or works on data the reader can't see. Use neutral placeholder names only when all three hold: the example demonstrates pure structure or mechanism (nesting, inheritance, how an operator behaves), no domain fits, and the data is tiny and fully shown. Keep names consistent across a running example.

**Write every example as if it will be copied into production.** Use the currently recommended approach, with current safe and accessible practice built into ordinary examples, and give a line of reasoning where a practice isn't obvious. Attach each caveat, such as a security risk, to the example that raises it. Never use a deprecated or risky construct to save space. Move superseded approaches out of the main text, leaving a one-line pointer to the documentation for the version that used them.

**Show the wrong form beside the right one.** Wherever readers predictably reach for a plausible but wrong form, show it next to the correct one, label which is wrong, and explain why it fails. Do this on every page type, including reference and conceptual pages, as often as real traps occur, and especially when the wrong form runs without error but gives a wrong result. Naive attempt, its failure, why it fails, then the fix: a regular teaching move, not a one-time device.

**Mark wrong and failing samples inside the block.** Mark every sample that is incorrect, discouraged, or meant to fail inside the code block itself, for example with a `# Wrong:` comment, and use the same marking every time. Warn before the reader runs a sample that is meant to fail. Someone who copies or runs only the block should still see the warning.

**Elisions must be valid code.** When you omit part of a sample, mark the gap with something the language accepts, usually a comment, and say what belongs there, so a pasted snippet still parses and runs.

**Show commands and output the way readers will copy them.** Use separate blocks for command and output when the docs platform's copy action would pick up prompts and output along with the command. When the copy action strips them, or the material is print-first narrative, use one transcript block showing command and result together. Explain the prompt marker once.

**Pin versions unless the docs track the current release.** When the docs are versioned with each release, or always describe the current release, install the newest release without a pin, adding a constraint such as a minimum only where a minimum version is actually required. When the docs are written against one version and not updated with each release, pin the version the page was written and tested against.

### Callouts and terms

**Warn about silent and breaking failures too.** Use a warning callout for data loss, security, and money, and also for anything that breaks the application or silently gives a wrong result: code that looks right but does something else, mistakes that fail silently, skipped or overwritten files, settings unsafe in production, hangs, crashes, and code that isn't meant to be copied. Each warning names one failure. Use lighter types (note, tip) for everything else, and keep warnings rare enough that readers still notice them.

**Put optional depth in titled, consistent asides.** Put shortcuts, tangents, and advanced options in one consistent, visually distinct kind of aside, separate from warnings. Give each aside a descriptive title saying what's inside, such as the question it answers, so readers can choose to skip it. Give each callout type a fixed meaning that tells readers whether they can skip it: essential context, optional extra, or warning. Keep asides few.

**One term per concept.** Use one term per concept, define it on first use, and never vary it for elegance. When a second name is unavoidable, declare the equivalence once, prominently, near the start, saying which term is exact and why:
- When commands, directories, or tools use a different or older name, keep your one term in prose.
- When a precise term has a more natural synonym, both may appear once the synonym is declared.

**Settle easily confused pairs where the confusion happens.** Where two forms, components, methods, options, or terms are easy to confuse, including terms readers use as if they meant the same thing, put the distinction at the point of confusion. A side-by-side table that labels which is which works well. Say that the loose usage exists, show a case where the difference matters, and link each item to the other. Don't leave the distinction only on a separate comparison page.

## Rules for several kinds of page

Each rule lists the kinds it applies to.

**Show the longhand before the shortcut** (tutorial, explanation, reference, book). Introduce a convenience API, or a construct that seems like magic, by first showing the longer code it stands for, built from parts the reader already knows. A tiny reimplementation also works, if it is readable in one sitting and written without the library being explained. Then show the short form and say plainly whether the two are exactly equivalent, approximately equivalent, or only illustrative, and list where the equivalence breaks. Mark illustrative implementations as not for real use. Repeat the equivalence in the reference entry for the convenience API.

**Connect new concepts to what readers already know** (explanation, reference, tutorial, book). When readers bring knowledge or habits from another tool, standard, specification, or competing product, connect each new concept to its nearest counterpart there. Say where the two conform and where they differ, and put an inline warning wherever the old habit leads readers astray. Open a concept guide with the underlying technology or idea the reader already knows, then show what your tool adds on top of it.

**Definitions first in lookup material** (reference; tutorial, explanation, book). In reference and other lookup material, put the definition before the examples, and make it complete on its own: the description fully defines the behavior, and the examples only illustrate it. In teaching material, either give a concrete example before the abstraction it illustrates, or a one-sentence definition followed immediately by an example.

**One shared sample domain per set of examples** (reference, how-to, explanation).
- On a long page whose examples share a setup, define that setup once near the top and have every later example refer to it.
- Across a set of reference entries, use one small shared sample domain, so names match and examples can be compared.
- Across a feature's guide and its reference pages, keep the same domain.

**Give reasoning where the reader will wonder** (tutorial, how-to, reference). When a step involves a judgment call (how much to verify, which level to test at, why an order or a choice of element matters), or a design choice that will puzzle readers at that point, give the reasoning right there: a few sentences in a titled box or a single clearly marked paragraph that can be skipped. Move anything longer to an explanation page.

**Cross-cutting topics: full treatment once, local consequences everywhere** (reference, how-to). Explain each cross-cutting topic (security, authentication, errors, pagination, and so on) fully on one page. In every entry or feature page it affects, still state in a line or two the specific requirement, consequence, or hazard that applies there, with a link to the full treatment.

**Ask for predictions at the point of the concept** (tutorial, explanation, book, video). Where a concept is shown, not only in end-of-chapter exercises, stop and ask the reader what will happen before you show it. Or invite them to change one specific value or line, predict the result, and check it with the real tool.

**Flag teaching shortcuts** (tutorial, explanation, book, video). When a teaching example takes a shortcut (skipped error handling, a simplified algorithm, ignored edge cases, incomplete markup, a partial implementation), say so next to it and say what production code would do instead.

**Show legacy forms for recognition** (reference, tutorial, book). Show the older forms of an API that readers will meet in existing code, labeled as older or legacy, so readers can recognize and translate them. Keep the emphasis on the current way, usually by placing older forms last, and don't present them as an equal option.

**Say where each name comes from** (tutorial, reference, book). When a new name appears in code, say which package, module, or import provides it. In reference for a library that loads in pieces, state for each item which module provides it. Tell learners that this is what to search for when they need help or documentation.

**Change one thing at a time to show variants** (reference, explanation). To show what an option or variant changes, keep the input fixed, change one thing at a time, and show the real output for each, one after another. Mark exactly which parts of the output the option adds or changes.

**Collect known limits** (reference, explanation). For features and options whose misuse is costly, document why they exist, their known limitations and caveats, and their interactions, in a clearly titled section of the feature's or entry's documentation.

## Pre-publish checklist

- [ ] **Run every example as written.** Run every command and code sample in page order, starting from the state the page declares. Check that each one runs without syntax errors, produces the output the page shows, and needs no code the page never gives. Setup data may live in a separate file that ships with the material, as long as the page says where it is and that data produces the output shown. Repeat the run on a clean environment whenever a dependency changes.
- [ ] **Verify every fact against its source, and keep facts consistent.** Take every name, type, default, error, output, and version from a source you have checked: code, schema, `--help`, tests, or changelog. Make prose agree with the code it describes, check every cross-reference against the content it points to, record which version you documented, and keep facts and version statements consistent across pages. Leave out anything you couldn't verify; never write a placeholder for it. If the reader needs it, say in chat what you'd need to confirm it.
- [ ] **Avoid claims that age.** Remove statements that depend on when they were written ("new", "recently", "currently", "as of this writing"); they become false later, and readers can't tell when. Keep version-specific details in a few places so updates touch little, and remove dated material when it expires. Books need this most.
- [ ] No gotcha below, or in the reference file you read, describes the draft.

## Gotchas

- Publishing snippets that fail, or that show output the code doesn't produce, because they were never run.
- Writing plausible names and outputs from memory; letting sections drift onto different versions of the API.
- Writing "the new X API", which becomes false and confusing a release later.
- Moving every sentence of rationale to a separate page, leaving lessons choppy; or the opposite, pasting whole reference tables into tutorials.
- Splitting a topic into separate novice and expert pages instead of one page that progresses.
- Describing only what the tool does, so readers assume it handles things it doesn't.
- Copying third-party install steps, full FAQ answers, or version tables into many pages, where the copies drift.
- Writing "as shown above", which breaks with layout changes, screen readers, translation, and reflow.
- Dropping in unlabeled examples.
- Using `foo`/`bar` in task examples, or forcing an invented business domain onto a pure mechanism demo so the mechanism is hidden.
- Writing the shortest code that demonstrates the point, which readers then copy with its insecure or outdated shortcuts.
- Showing only correct code, so readers who already hold the wrong form never learn why it's wrong.
- Labeling wrong code only in the surrounding prose; readers who copy the block take the wrong version.
- Writing a bare `...` inside code, so pasted snippets fail with syntax errors.
- Always splitting commands from their output, even where one transcript would read better and copy cleanly.
- Pinning every install, so current-release docs install outdated packages; or leaving one-version docs unpinned, so they break on the next major release.
- Leaving silent wrong-result traps unflagged because they don't involve data loss, security, or money.
- Cluttering the main path with optional detail, or cutting it, so readers can't tell what is safe to skip.
- Using undeclared synonyms that read as different things, or hiding that the tools use another name.
- Documenting easily confused items each in isolation.
- Presenting a shortcut API as opaque magic.
- Explaining everything from scratch, losing what readers could transfer from tools they know and leaving their wrong habits unflagged.
- Leading every reference entry with an example, and leaving some rules stated only in the examples.
- Inventing new data for every example, so readers learn a new domain each time and can't compare entries.
- Cutting the why to one clause or a link at exactly the moment the reader makes the judgment call.
- Leaving only a bare link to the security (or other cross-cutting) page, so readers configuring one feature miss its consequences.
- Saving all prediction and retrieval for end-of-chapter exercises.
- Simplifying examples silently, so readers ship the simplification.
- Showing only the current form of an API, so readers can't read the older code they'll inherit.
- Using names without saying which package or module provides them.
- Showing each option on different input, so readers can't see what the option itself does.
- Trimming entries to an austere minimum that leaves out the limits that make misuse expensive.

## Rules set by the maintainer

These apply to every page, and override anything above that disagrees.

**No placeholders on disk.** Never write a placeholder, a question, or a note to the maintainer into any file. The maintainer asked for the writing so they don't have to do it, so what you write is final. Bring up in chat only what truly needs their judgment, where a wrong call would do real harm, and keep that as short as you can. For everything else, take the answer the evidence supports that claims the least on the maintainer's behalf, write it as final, and list those calls in your report.

**State verified facts plainly.** Most sentences an agent feels the urge to qualify aren't overclaiming anything. Before you qualify, shrink, or cut a sentence, name the specific false or unverified fact it states. If you can't name one, it isn't an overclaim, so leave it as written. A statement of what something is for, or what it does, is not an overclaim. Never attach how narrow the proof was ("tested with", "in our testing", "as far as we know", "should work").

**State a limit only where it changes what the reader can do.** State a limit only when it changes what the reader can do or should expect: a platform, a version, a model, a prerequisite, a risk to their data. State it once, as a fact, where the page keeps its caveats. Work the maintainer hasn't done yet, such as tests or benchmarks not yet run, isn't a limit for the reader. It belongs in contributor documentation.
