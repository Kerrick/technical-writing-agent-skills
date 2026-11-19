Source: Ember Guides (release), Getting Started and Tutorial sections, commit 919777db2

> Quotes and descriptions in this file are from the [Ember Guides](https://guides.emberjs.com/release/) ([ember-learn/guides-source](https://github.com/ember-learn/guides-source)), copyright (c) 2019 Ember Learning Team, licensed under the [MIT License](https://github.com/ember-learn/guides-source/blob/master/LICENSE). Quotes are short, and used to compare and criticize.

# Comparison with the technical-writing baseline

## 1. Missed principle

- **Give the material a deliberate, welcoming and inclusive voice.** The contribution guide calls for a friendly tone and gender-neutral pronouns (`guides-source/CONTRIBUTING.md:57`). The tutorial sustains a conversational guide voice through direct encouragement and reassurance (for example, `tutorial/part-1/automated-testing.md:128`, `tutorial/part-2/recap.md:37`). The baseline asks for direct language but does not specify voice or inclusive language (`technical-writing/SKILL.md:16`; absent for an explicit tone rule).
- **Plan for readers with different levels of prior experience, including within the same material.** The stated audience spans beginners with some jQuery experience through experienced Ember developers learning a feature, and the guide says to meet both needs (`guides-source/CONTRIBUTING.md:61`). Getting Started establishes a baseline and links out to refresh HTML, CSS, and JavaScript (`guides-source/guides/release/getting-started/index.md:41`, `guides-source/guides/release/getting-started/working-with-html-css-and-javascript.md:1`); later chapters explain new ideas while linking to deeper topics. The baseline asks the writer to identify a reader and activate prior knowledge, but does not explain how to serve a range of experience levels (`technical-writing/SKILL.md:12`, `:34`).
- **Scope each page around the common path and defer comprehensive or rare detail to the right reference.** The contribution guide says the Guides are practical rather than comprehensive, prioritizes the “Ember happy path,” and leaves rare features to API documentation (`guides-source/CONTRIBUTING.md:63`). The introduction distinguishes practical guides from comprehensive API documentation (`guides-source/guides/release/getting-started/index.md:24-27`); the EmberData chapter likewise labels its coverage a starting point and links to its dedicated section (`tutorial/part-2/ember-data.md:431`). The baseline distinguishes content forms and cautions against irrelevant exhaustive lists, but never explicitly tells writers to prioritize a common path and route exhaustive detail elsewhere (`technical-writing/SKILL.md:13`, `:49`).
- **Use short examples liberally alongside explanations, and add a second example when it makes a distinction clearer.** The style guide says examples often explain more clearly than prose and recommends using them liberally, sometimes two (`guides-source/CONTRIBUTING.md:67`). The chapters repeatedly pair explanations with code, visible output, and contrasting states; for example, the interactive-components chapter shows both image states and a failing test (`tutorial/part-1/interactive-components.md:3-11`, `:270-274`, `:331`). The baseline says to use examples, but only conditionally (“when useful”) and has no expectation to make them a regular companion to explanations (`technical-writing/SKILL.md:36`).
- **Link readers to authoritative documentation and useful background at the point of need.** The style guide explicitly calls for API links and encourages authoritative background sources (`guides-source/CONTRIBUTING.md:65`). The Getting Started overview routes readers to API documentation (`guides-source/guides/release/getting-started/index.md:24-27`), and the prerequisite guide points to MDN material (`getting-started/working-with-html-css-and-javascript.md:12-24`). The baseline says to ground claims in authoritative sources, but does not say to expose those sources as links in the material (`technical-writing/SKILL.md:14`; absent).
- **Keep prose brief without sacrificing clarity, and split a page when its length makes it hard to use.** The style guide states both parts directly (`guides-source/CONTRIBUTING.md:59`). The baseline recommends removing unrelated material and managing cognitive load, but does not give a page-level brevity or splitting rule (`technical-writing/SKILL.md:18`, `:39`; absent).

## 2. Correction

- None identified. The examples support the baseline’s conditional advice to adapt structure to reader needs and do not show that any of its general rules is false or too absolute.

## 3. House convention

- **Ember’s source-format conventions:** code fences carry Ember-specific `data-filename` and `data-diff` metadata, and examples use its template and file conventions. The contribution guide prescribes these formats (`guides-source/CONTRIBUTING.md:77-100`); the tutorial uses them throughout. These conventions belong to this documentation system, not to technical writing generally.

## 4. Where the Ember Guides fall short

- **Page length:** the contribution guide suggests splitting guides that run beyond a couple of screens (`guides-source/CONTRIBUTING.md:59`), yet several tutorial chapters are very long: `tutorial/part-1/reusable-components.md` has 636 lines, `tutorial/part-2/provider-components.md` 543, and `tutorial/part-2/route-params.md` 516. The sustained build may justify some length, but these pages make the guide’s own brevity and chunking advice difficult to follow.

The baseline is stronger here: it explicitly asks writers to review whether readers can locate a section and to remove material that does not advance the task (`technical-writing/SKILL.md:18`, `:69`).

## Also confirmed

- State a visible outcome and check that the reader can recognize success: chapter introductions preview the result, and the tutorial repeatedly checks the UI and test suite (`tutorial/part-1/automated-testing.md:3-7`, `:124-130`; baseline `technical-writing/SKILL.md:33`, `:80`).
- Explain the reasoning behind a step instead of only giving commands: the router-service chapter explains why `window.location.href` fails in tests before introducing the router service (`tutorial/part-2/service-injection.md:299-319`; baseline `technical-writing/SKILL.md:35`).
- Distinguish stable concepts from implementation details that depend on context: the share-button chapter avoids brittle implementation-level assertions in its acceptance test and reserves those specifics for component tests (`tutorial/part-2/service-injection.md:303`; baseline `technical-writing/SKILL.md:50`, `:71`).

## Observed, not counted

The tutorial chapters combine how-to instructions, conceptual explanation, and reference-like details. For example, `tutorial/part-1/working-with-data.md` has a sequence of file edits and fetch steps, explains model hooks and JSON:API structure, and includes full code and data shapes (`:15-47`, `:63-86`, `:247-271`, `:275-383`). `tutorial/part-2/service-injection.md` combines implementing a feature, explaining router-service behavior, and enumerating the share URL’s query parameters and testing contract (`:11-45`, `:226-319`). The pages also point readers to dedicated references for deeper treatment, such as the EmberData section (`tutorial/part-2/ember-data.md:431`).

The baseline has no rule that a page must contain only one documentation type. Its closest rule says to separate forms only when one page cannot serve their different reader needs (`technical-writing/SKILL.md:13`). The observed blending does not contradict that conditional rule: each chapter has one concrete learning task, and its explanation and reference details support that task. The Getting Started section does keep distinct entry points for overview, quick start, prerequisite background, and application anatomy (`guides-source/guides/release/getting-started/index.md:29-43`; `guides-source/guides/release/pages.yml` entries for `getting-started/index`, `quick-start`, `working-with-html-css-and-javascript`, and `anatomy-of-an-ember-app`). I would not count this as a correction.

## Abstracted

- Choose a voice that is welcoming, respectful, and inclusive, and use it consistently.
- Design for the actual range of reader experience; give newcomers enough explanation while helping experienced readers find the new or advanced material they need.
- Keep each page centered on the common, intended path. Link to comprehensive references for exhaustive details and uncommon cases.
- Pair explanations of nontrivial ideas with concrete examples; use more than one when comparison makes the idea easier to understand.
- Link readers to authoritative references and prerequisite material where those links will help them continue or fill a knowledge gap.
- Keep pages as concise as clarity allows, and divide material when its length makes it hard to scan or follow.
