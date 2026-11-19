Source: Ember Guides (release), commit 919777db2

> Quotes and descriptions in this file are from the [Ember Guides](https://guides.emberjs.com/release/) ([ember-learn/guides-source](https://github.com/ember-learn/guides-source)), copyright (c) 2019 Ember Learning Team, licensed under the [MIT License](https://github.com/ember-learn/guides-source/blob/master/LICENSE). Quotes are short, and used to compare and criticize.

# Ember Guides compared with the baseline `developer-docs` skill

Scope and method:

- Compared the 127 pages read in navigation order against the baseline skill as written (`work/developer-docs/`, unchanged).
- Page paths are relative to `guides/release/`, so `tutorial/part-1/orientation.md` means `guides/release/tutorial/part-1/orientation.md`.
- Skill lines are `SKILL.md:N`, `teaching.md:N` (`references/teaching.md`), `reference-and-guides.md:N`, and `books-and-video.md:N`.
- `CONTRIBUTING.md:N` is the repository's "Style Guide" and "Writing" sections, which state the intent.
- That intent, in short:
  - friendly voice, and complete sentences (`:57`);
  - brief but never at the cost of clarity, and split pages longer than a couple of screens (`:59`);
  - one audience that spans beginner to experienced, so pages explain enough for the beginner and also cover advanced topics (`:61`);
  - cover the happy path, not everything, with simplest and most common first and edge cases left to the API docs (`:63`);
  - each guide explains its feature and links to API docs, with no outside blog posts (`:65`);
  - many short examples, often two (`:67`);
  - edit twice, and check grammar, clarity, examples, and links (`:163-168`).
- Sentence counts and line counts below come from searches, not from memory.

## 1. Missed principle

**1.1 Open every lesson with the list of concepts it teaches, and reuse those items in the recap.**

- Evidence:
  - Every tutorial chapter, 12 in all, opens with a "you will learn about:" bullet list. Examples: `tutorial/part-1/orientation.md:7`, `tutorial/part-2/service-injection.md:9`.
  - `tutorial/part-1/recap.md` and `tutorial/part-2/recap.md` repeat those bullets per chapter, with a link to each chapter.
- Skill:
  - `teaching.md:14` opens with what you'll build, time, prerequisites, and versions. It has no concept list.
  - `teaching.md:19` closes with a recap "in a few lines". It doesn't say to reuse the opener's wording.
  - `books-and-video.md:17` has outcomes for books only.

**1.2 Show the problem before the feature.**

- Evidence:
  - `components/conditional-content.md:47` and `:168` are literally headed "### Motivation". Each shows two near-identical pieces, then unifies them with the feature.
  - `components/block-content.md` opens its argument with two almost-identical message pieces, then asks "Instead of having two different components…".
  - `components/helper-functions.md` shows repetitive arguments first, then computes them.
- Skill:
  - `SKILL.md:37` says to give a minimal working example before the abstract description.
  - `teaching.md:25` says concrete before abstract.
  - `books-and-video.md:45` has "show wrong or naive approaches first", but only in the book file.
  - So the skill implies the opposite order for ordinary feature pages.

**1.3 Say when to use a feature, when not to, and what to use instead. Name the recommended option, and answer outside rumours.**

- Evidence:
  - `applications/ember-engines.md:23`: "Engines are not the right solution" for one stated goal, with an alternative named.
  - `in-depth-topics/autotracking-in-depth.md:441`: "avoid using @cached unless you have confirmed…".
  - `in-depth-topics/making-api-requests.md:36`: "The drawback is…" for loading data in the less usual place.
  - `routing/controllers.md:99` and `:103`: headings "Should we use controllers…? I've heard they're going away!" and "When should we create a Controller?".
  - `components/built-in-components.md` says "We recommend using the `{{on}}` modifier".
  - `in-depth-topics/patterns-for-actions.md` says two forms are "functionally equivalent and are used interchangeably".
- Skill:
  - `reference-and-guides.md:55` asks for tradeoffs and alternatives, only on explanation pages.
  - `reference-and-guides.md:24` says to put recommendations in guides but never says guides must contain them.
  - Absent for feature pages in general.

**1.4 Give legacy forms a short, labelled place after the current approach.**

- Evidence:
  - `components/helper-functions.md:241` "### Classic Helpers", with the note "Before Ember 4.5, this was the only way…".
  - `components/helper-functions.md:282` "### Class Helpers".
  - `getting-started/working-with-html-css-and-javascript.md:210` "### Classic Classes": "deprecated, but it is still useful to be able to recognize them".
  - That page then links to a frozen older edition of the guides.
- Skill: absent. `reference-and-guides.md` covers migration guides and deprecations, but not a recognition section inside a current page.

**1.5 Make each sample follow the domain's best practice, and give a one-clause reason.**

- Evidence:
  - `tutorial/part-1/interactive-components.md:264`: `<div>` becomes `<button>` "(this is important for accessibility reasons)", plus keyboard handling "for free".
  - `tutorial/part-1/component-basics.md:371`: asserts a `<nav>` "important for accessibility".
  - `tutorial/part-1/orientation.md:36`: `--lang en` "improves the website's accessibility".
  - `components/built-in-components.md`: every `<Input>` sample is paired with a label, and the page explains three ways to label.
- Skill:
  - `SKILL.md:43-45` make samples copy-paste safe and add alt text.
  - Nothing says to build accessibility or similar qualities into the samples themselves.

**1.6 Declare the scope: the common path only, with rare cases left to the reference.**

- Evidence:
  - `getting-started/index.md`: "not intended to be comprehensive… see the API documentation".
  - `in-depth-topics/making-api-requests.md`: "These Guides do not cover how to load data in components, since the majority of data fetching should be done in a route's `model`."
  - `CONTRIBUTING.md:63`.
- Skill:
  - `SKILL.md:35` says "edge cases later", which implies they stay on the page.
  - `reference-and-guides.md:59` says to name scope, for explanations only.
  - `reference-and-guides.md:49` has how-tos cover the unhappy path.

**1.7 Cap page length and split.**

- Evidence:
  - `CONTRIBUTING.md:59`: more than "a couple screens of scrolling" means split.
  - Many pages are short, for example `routing/rendering-a-template.md` at 20 lines, `configuring-ember/handling-deprecations.md` at 20 lines, and `configuring-ember/specifying-url-type.md` at 45 lines.
  - The rule is not kept everywhere. See 4.10.
- Skill:
  - `reference-and-guides.md:50` splits by task only.
  - No length rule.

**1.8 Write prose with one sentence per line.**

- Evidence:
  - `CONTRIBUTING.md:72-75` (manual line breaks at the start of each sentence).
  - Visible in `getting-started/quick-start.md:1-3` and `tutorial/part-1/orientation.md`'s early paragraphs.
  - Uneven: many pages hard-wrap at about 80 columns, for example `components/introducing-components.md`.
- Skill:
  - Absent.
  - `reference-and-guides.md:88` says to treat docs as code and lint them, but has no line-break convention.

**1.9 Treat a wrong sample or typo as a bug, with a one-step route to fix it from every page.**

- Evidence:
  - `getting-started/index.md:53-62`: "Typos, missing words, and code samples with errors are all considered documentation bugs."
  - The same text points to the pencil icon on every page, which opens the editor on the source.
- Skill:
  - `reference-and-guides.md:90` has feedback widgets, as measurement.
  - It has no stance that sample errors are bugs, and no per-page edit path.

## 2. Correction

**2.1 "Use one running domain across a doc set" (`SKILL.md:46`) is too broad.**

- Evidence:
  - The component pages share one messaging scenario: "message" appears 83 times in `components/introducing-components.md` and 67 times in `components/looping-through-lists.md`.
  - The routing pages use unrelated posts/photos/articles scenarios: `routing/defining-your-routes.md` has 64 hits and `routing/specifying-a-routes-model.md` has 37.
  - The testing pages use a different small scenario per page.
  - The tutorial uses its own app throughout.
- Reading: the running scenario is scoped to a group of pages that build on each other. Independent pages each use a small fresh one.

**2.2 "Every external link is to a stable, versioned URL where possible" (`SKILL.md:68`) is wrong for docs that are themselves versioned.**

- Evidence:
  - `CONTRIBUTING.md:119`: "always use `/release/` when linking API docs".
  - 89 API links in 24 pages use that alias.
  - The only two pinned links are stale or arbitrary: `in-depth-topics/native-classes-in-depth.md:499` points at `/ember/3.27/`, and `in-depth-topics/autotracking-in-depth.md:401` points at `/ember/6.8/`.
- Reading: a page for release N should link to the alias that moves with N. Frozen archive pages are the only ones that should pin.

**2.3 "Avoid idioms, jokes…" (`SKILL.md:54`) is too absolute for teaching text.**

- Evidence:
  - `CONTRIBUTING.md:57` makes a "friendly tone of voice" a rule.
  - `tutorial/part-1/automated-testing.md:22` "Small Tweak™" and `:126` "I told you the robot has really, really fast hands!".
  - `tutorial/part-2/service-injection.md:313` "Gotta love computers!".
- Skill: `books-and-video.md:43` allows light humour in books.
- Reading: the skill's translation concern is sound. The Guides show the voice is a deliberate tool in teaching material and absent from the reference-like pages. I'm less sure of this one than of 2.1 and 2.2, because the Guides give no evidence either way on translation.

(The mode-mixing correction is under "Observed, not counted" below.)

## 3. House convention

- "Zoey says…" and "Tomster says…" mascot callout boxes for tips and asides. They are a style for tips, not the idea of an aside.
- Fence metadata `data-filename` and `data-diff` (`CONTRIBUTING.md:83-93`) and relative-link and `toc_` anchor rules (`:101-117`).
- The Super Rentals tutorial app: a map from a third-party static-image API, a social-share button, and JSON served from the public folder.
- Generated-tutorial header comment on every tutorial page (`tutorial/part-1/index.md:1`) and `<!-- eof … -->` markers.
- Title Case headings (`CONTRIBUTING.md:57`). They are applied unevenly, for example `tutorial/part-2/provider-components.md` has "## Add input".
- CLI generator output blocks and `ember g` shortcuts.

## 4. Where the Ember Guides fall short

**4.1 Samples with errors, against `SKILL.md:64` (run every sample).**

- `components/conditional-content.md:57` and `:79`: a `<template>` opener where the closer belongs. `:106` leaves `<Username … >` unclosed.
- `testing/testing-components.md:193`: asserts `'Pretty Color: orange'` while the data is `'red'`.
- `testing/unit-testing-basics.md:169` returns `` `Answer: ${z}` `` but `:195` asserts `'Answer 4'`.
- `testing/testing-models.md:28`: says the test starts at level 4, but `:20` and `:48` start at the default level.
- `routing/linking-between-routes.md:246`: opens `<LinkTo>`, closes `</Link>`.
- `components/looping-through-lists.md:132` and `:289`: `@userLocaltime` where the data key is `localTime`.

**4.2 Tutorial prose out of step with its code, against `SKILL.md:66-67` and `:70`.**

- `tutorial/part-1/interactive-components.md:120` says to edit `…/image.js`, but the file is `.gjs`.
- `tutorial/part-2/route-params.md:134` and `tutorial/part-2/provider-components.md:529` say the tests use `setProperties`. The code uses a tracked `State` class.
- `tutorial/part-2/recap.md:32` says "Using Ember's built-in `<Input>` component", but chapter 12 uses a form and `FormData`.
- `tutorial/part-2/recap.md:28` and `tutorial/part-2/index.md:14` list adapters and serializers. Chapter 11 teaches request builders and handlers.

**4.3 Two vintages of the same API in one release, against `SKILL.md:64` and `:67`.**

- `models/defining-models.md:18` imports `@ember-data/model`.
- `tutorial/part-2/ember-data.md:98` imports `@warp-drive/legacy/model`.
- `routing/linking-between-routes.md` has 6 fences tagged `.hbs`, and `routing/controllers.md` has 2.
- Component pages use `.gjs`.
- The console output for the dev server shows `VITE v6.3.6` in `getting-started/quick-start.md:64` and `VITE v8.0.11` in `tutorial/part-1/orientation.md:226`.

**4.4 Warning comes after the hazard, against `SKILL.md:44`.**

- `components/looping-through-lists.md:134` shows the unescaped-HTML sample, and `:144` and `:155` explain the risk afterwards ("not recommended for production apps").

**4.5 Filler and reassurance words, against `SKILL.md:41`.**

- "simply", "easy", "easily", and "obviously" occur 70 times in 38 pages in the guide sections.
- Examples: `getting-started/quick-start.md:48` "Ember makes starting new projects a breeze", and "Simply define a template" in `routing/loading-and-error-substates.md`.
- Some uses are literal, and the count includes them.

**4.6 Prerequisites and versions are not stated, against `SKILL.md:39` and `teaching.md:14`.**

- `getting-started/quick-start.md:25` offers only "Don't have npm?" and a link.
- The Node version appears only inside example output, at `tutorial/part-1/orientation.md:28`.

**4.7 Commands and output share a fence with `$` prompts, against `SKILL.md:43`.**

- `tutorial/part-1/orientation.md:19-30` and `:38-97`.
- `getting-started/quick-start.md:53-56` puts two commands in one fence.
- The Guides do not use one convention, since `quick-start.md` also uses separate command and output fences.

**4.8 Step-by-step walkthrough of a third party's UI with screenshots, against `SKILL.md:70`.**

- `getting-started/quick-start.md` Netlify section: "Click the button that says 'New site from Git'", with screenshots under `/images/quick-guide/netlify/`.

**4.9 Almost no practice for the learner, against `teaching.md:27` and `:33`.**

- The only prompts are `getting-started/quick-start.md:296` ("an additional exercise (that we won't cover)") and `tutorial/part-2/provider-components.md:536` ("If you're looking for a challenge…").
- There are no questions, no solutions, and no recall checks.

**4.10 Pages over the Guides' own length rule, against `reference-and-guides.md:50` and `CONTRIBUTING.md:59`.**

- `models/customizing-serializers.md` has 788 lines (several serializer types, conventions, embedded records, and authoring).
- `in-depth-topics/native-classes-in-depth.md` has 736 lines.
- `testing/testing-components.md` has 617 lines.

**4.11 Style-guide rule not followed, against `SKILL.md:68`.**

- `CONTRIBUTING.md:65` says no outside blog posts.
- `getting-started/quick-start.md:175` links a blog article for JavaScript classes.

## Confirmations (one line each)

- `SKILL.md:50` (generate reference from source): `contributing/index.md` says API pages are fixed by editing the comment block in the source file, so the reference is generated and the Guides carry none of it.
- `SKILL.md:53` and `books-and-video.md:26` (real output, tested code): `tutorial/part-1/orientation.md:27-29` shows real versions and build times, and the page header says the file is generated from a separate tutorial repo with a finished-app tag (`tutorial/part-1/index.md:9`).
- `SKILL.md:52` and `:43` (obviously fake placeholders): `'paste your TomTom API key here'` (`tutorial/part-1/reusable-components.md:73`) and `super-rentals.example` (`tutorial/part-2/service-injection.md:25`).
- `teaching.md:31` (trigger and read an error on purpose): failing tests are shown and diagnosed at `tutorial/part-2/service-injection.md:309-313` and `tutorial/part-2/ember-data.md:333-340`.
- `teaching.md` (supply bulky assets instead of typing): `tutorial/part-1/orientation.md:303` and `:345` hand over the stylesheet as a download.

## Observed, not counted

Pages that combine explanation, how-to, and reference:

- `components/helper-functions.md`:
  - explains why helpers exist;
  - walks through creating local and shared helpers;
  - ends with a catalogue under "Built-in and Common Helpers" that says "For the full list… check the … documentation".
- `routing/defining-your-routes.md`: concept, steps, and special cases on one page.
- `models/customizing-serializers.md`: format conventions, customization steps, and an "Authoring Serializers" explanation.
- Tutorial chapters carry bounded explanation sections:
  - `tutorial/part-2/service-injection.md` has "## Ember Services vs. Global Variables".
  - `tutorial/part-2/ember-data.md` has "## What is EmberData?".
  - `tutorial/part-2/provider-components.md` has a long passage on block parameters.
  - Each explanation sits next to what was just built and links to the full guide.

Skill rules they differ from:

- `SKILL.md:13`: "Mixing modes is the most common structural failure."
- `SKILL.md:31`: "a tutorial that stops to explain design has become an explanation… Link between modes instead of merging them."
- `SKILL.md:69`: the verify item that the page stays in its mode.
- `teaching.md:30`: the why in a clause, not a paragraph.

Where the docs keep the modes apart:

- The exhaustive reference lives off the Guides entirely. `getting-started/index.md` points to the API docs for "every Ember feature and API", and `contributing/index.md` describes editing them from the source.
- Tutorial, feature guides, in-depth topics, and testing are separate sections with their own entry points.
- Inside a guide, headings mark each shift and pages run from simplest to advanced (`CONTRIBUTING.md:63`). Pages are written for one range of readers (`CONTRIBUTING.md:61`).
- The Guides do not put long lookup tables in a guide, and each cross-mode explanation links out.

Would I count it as a correction? Yes, for the wording of the rule only. Explanation and how-to share a page without harm when ordered simple to advanced under clear headings, and a lesson may include a short explanation of what it just built if it links to the full treatment. I would not count the mixing of exhaustive reference into guides as a correction, because the Guides don't do that. I have no reader data, so "without harm" is inferred from how consistently the Guides do it, not measured.

## Abstracted

Missed principles:

1. Open each lesson with the list of concepts it teaches, and close the series with a recap that reuses those same items in the same words, so each idea is named twice and the reader can check it against what they did.
2. When you introduce a feature, first show the situation without it (repetition, near-duplicates, or a pain the reader can see), then show the feature resolving it, so the reader knows what problem it solves before learning how it is written.
3. For every feature, say when to use it, when not to, and what to use instead. When several options work, name the one you recommend and say whether the others are equivalent. Answer the doubts readers bring with them from outside your docs, such as hearsay about whether a feature is still worth learning, in a short question-and-answer section.
4. After the current approach, give older or deprecated forms a short, clearly labelled place, enough to recognize them in old code and posts, with a pointer to where the old documentation lives.
5. Make each sample itself follow the best practice your readers' domain demands (accessible markup, safe handling of untrusted input, and similar), and add a one-clause reason when the choice is not obvious, because readers copy samples, not the prose around them.
6. State that a guide covers the common path only and say where the rare cases are documented. Start each page and each section with the simplest, most common case, then advance, instead of appending edge cases.
7. Set a page-length limit, for example a couple of screens, and split pages that exceed it. Prefer many short pages over a few long ones.
8. Put each sentence of the prose source on its own line, so a review shows which sentence changed.
9. Declare that wrong samples and typos are documentation bugs, and put a one-step route to the editable source or a report button on every page.

Corrections:

1. Scope a running example to a group of pages that build on each other. Pages that don't build on each other may each use their own small scenario. Don't force a single scenario on an entire set.
2. When your docs are published once per release, link to the alias that moves with the same release instead of a numbered version, so links and pages update together. Pin a version only inside frozen archive pages.
3. Treat a warm, lightly humorous voice as a legitimate choice for teaching material. Keep wording plain and joke-free in lookup material and in text that will be machine-translated. Don't ban warmth outright.
4. Explanation and task steps may share a page if headings mark the shift and the order runs from simplest to most advanced. A lesson may include a short explanation of what it just built, if it links to the full treatment. Keep exhaustive lookup tables out of such pages.
