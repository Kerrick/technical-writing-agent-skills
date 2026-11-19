Source: Ember Guides (release), commit 919777db2

> Quotes and descriptions in this file are from the [Ember Guides](https://guides.emberjs.com/release/) ([ember-learn/guides-source](https://github.com/ember-learn/guides-source)), copyright (c) 2019 Ember Learning Team, licensed under the [MIT License](https://github.com/ember-learn/guides-source/blob/master/LICENSE). Quotes are short, and used to compare and criticize.

# Ember Guides compared with the `technical-writing` skill

Scope: the 127 pages in `guides/release/pages.yml`, read in "next" order, plus the "Style Guide" and "Writing" sections of `CONTRIBUTING.md`. File paths below are relative to `guides/release/` unless they start with `CONTRIBUTING.md`. Skill references are to `~/.agents/skills/technical-writing/`.

## 1. Missed principles

### M1. Let learners do it the manual way first, so the abstraction removes pain they have felt

The tutorial repeatedly has the reader build something by hand, lets the cost show, and only then introduces the tool that removes it. The jumbo header is copied into three pages before `component-basics.md` extracts it. The nav bar is added to every page and then moved to the application template because doing it per page "is a bit error-prone". In `working-with-data.md` the reader fetches and reshapes JSON:API data by hand, the text promises "a more convenient way" in Part 2, and `ember-data.md` opens by showing the two duplicated route files and calling the duplication "technical debt". Chapters also end on a planted gap: `route-params.md` closes with a share button "that doesn't actually work. We'll address this in the next chapter."

Skill: absent. `references/learning-science.md:65` says to open with the reader's problem. It never says to have the learner create that problem in an earlier step, or to sequence chapters around it.

### M2. Explain the judgment call at the moment the learner makes it

The tutorial stops briefly to explain decisions that aren't syntax: how much to test, what's worth testing at which level, and why order matters. Examples: `more-about-components.md` ("Because we already tested `<RentalImage>` extensively on its own, we can omit the details here"), `component-basics.md` (testing the nav bar in isolation "would not make a lot of sense"), `service-injection.md` (too many specific details make a "brittle" acceptance test), and `reusable-components.md` ("The ordering is important here!", about attribute placement).

Skill: `references/tutorials.md:48` ("say just enough to keep going, and link to the explanation page") and `references/tutorials.md:71` (detours belong on other pages) imply that this reasoning should go elsewhere.

### M3. A refactoring step needs a checkpoint too: unchanged output plus passing tests

Refactor steps tell the reader outright that nothing should change, then confirm it with a screenshot and the test run. Examples: `component-basics.md` ("nothing changed? Well, that's exactly what we wanted to happen this time!"), `ember-data.md` ("The end result looks exactly the same as before"), and `provider-components.md` ("Awesome, it looks exactly the same!").

Skill: `references/tutorials.md:47` asks for a visible checkpoint but assumes progress is visible. It doesn't cover steps whose correct result is no visible change.

### M4. A running example can span a reference-like section, provided each page re-establishes it

The Components section carries one messaging-app example from page to page. `components/introducing-components.md` points back to it ("that we introduced in the previous chapter, if you're reading the guides in order") and then reprints the full starting code. `component-arguments-and-html-attributes.md`, `conditional-content.md`, `block-content.md`, `helper-functions.md` and `looping-through-lists.md` each restate the components they build on, so a reader who arrives from search isn't lost.

Skill: `references/tutorials.md:50` and `references/books.md:16` limit running examples to tutorials and books. `SKILL.md:81` requires pages to stand alone and never reconciles the two.

### M5. Put optional depth in visually distinct asides, separate from warnings

Most callouts aren't warnings. They hold shortcuts, tangents and next-level detail, so the main text can stay on the common path. Examples: the `ember g` shorthand in `tutorial/part-1/automated-testing.md`, the `-gc` flag in `reusable-components.md`, `@service('router') emberRouter` in `service-injection.md`, and the yield tangent in `components/block-content.md` ("if you're in the mood for a tangent").

Skill: `SKILL.md:79` treats callouts only as warnings ("Reserve warnings for data loss, security, and money. A page of callouts trains readers to skip them.").

### M6. Give the assumed baseline its own page and teach only the gap

`getting-started/index.md` states the baseline (working knowledge of HTML, CSS and JavaScript). It then points to `working-with-html-css-and-javascript.md`, which sends beginners to outside tutorials and teaches only the language features the framework depends on that competent JavaScript developers may not know: class fields and decorators. The page invites readers to "come back to this page" when they get stuck.

Skill: `references/tutorials.md:18` and `SKILL.md:81` say to state prerequisites. Neither says to provide a page that bridges the gap between the general prerequisite and what the material actually needs.

### M7. Build good practice into every example, with one line of why

Accessibility isn't left to its own section. It's the default in ordinary examples, each with a short reason. Examples: `interactive-components.md` switches `<div>` to `<button>` "for accessibility reasons", `component-basics.md` asserts `<nav>` exists because screen readers use it, `quick-start.md` and `orientation.md` pass `--lang en`, and `built-in-components.md` says every input should have a label. `looping-through-lists.md` attaches the security caveat to the example that uses triple curlies.

Skill: absent. `references/style.md:42-48` covers the accessibility of the documentation itself, not of the code it teaches.

### M8. Show legacy forms so readers can recognize them, labeled as legacy, without teaching them

Examples: `working-with-html-css-and-javascript.md` ("Classic classes are deprecated, but it is still useful to be able to recognize them when looking at older code or blog posts"), the "Classic Helpers" section of `components/helper-functions.md` ("Before Ember 4.5, this was the only way"), and the aside in `reusable-components.md` about "classic" components in legacy codebases.

Skill: `references/api-reference.md:104` covers deprecation only in reference entries. Teaching material has nothing on helping readers decode older code they'll find elsewhere.

### M9. Teach where names come from, so readers can search for help

When a new name first appears, the tutorial says which package it comes from and why that matters. `automated-testing.md`: "You can tell what comes from which package based on the import paths … helpful when you need to search for documentation." Also in `building-pages.md` (`<LinkTo>` "is imported from the `@ember/routing` package that is part of Ember") and `interactive-components.md` (the `{{on}}` modifier "is imported from the `@ember/modifier` package").

Skill: absent.

### M10. Route readers by situation on section landing pages

`typescript/index.md` opens with "Not sure where to get started?" and a list keyed to the reader's situation: new to TypeScript, starting a new app, converting an app, working on legacy code, not ready to switch. `typescript/application-development/index.md` and `getting-started/index.md` ("If you're brand new to Ember, we recommend you start off…") do the same.

Skill: `SKILL.md:23` asks how the reader arrives, but nothing turns that into a page whose job is sending different readers to different starting points.

### M11. Say where to get human help, and how to report doc bugs, where trouble is likely

`quick-start.md` puts a "having trouble" pointer to the community right after the first `npm start`. `getting-started/index.md` explains how to report doc bugs (the edit pencil, issues). `contributing/index.md` says where to ask questions.

Skill: absent. `references/tutorials.md:52` covers self-recovery from known errors, not escalating to people.

### M12. Link background concepts only to authoritative, maintained sources

`CONTRIBUTING.md` encourages links to authoritative sources for background concepts and says "Do not link to other outside content like blog posts or meetup slides". Its reasoning is that those are better left to content aggregators. The pages follow this mostly: MDN and javascript.info throughout `working-with-html-css-and-javascript.md` and the tutorial's linked terms.

Skill: absent. `references/style.md:14-18` covers link text, not which sources are worth linking.

### M13. Set a page-length budget and split by subtopic when a page goes over

`CONTRIBUTING.md`: "If a guide is more than a couple screens of scrolling, consider breaking it into multiple pages." The structure follows it: Ember Inspector is 12 short pages, Accessibility is 6, and `routing/rendering-a-template.md` is a single short page.

Skill: absent.

### M14. Write prose source with one sentence per line

`CONTRIBUTING.md` requires manual line breaks at every new sentence and after long clauses. This keeps review diffs to the sentence that changed. It's visible in hand-written files such as `routing/index.md` and `getting-started/quick-start.md`.

Skill: absent.

## 2. Corrections

### C1. One page can serve novices and experts if it's ordered from common to rare

`CONTRIBUTING.md` asks each guide to be "thorough enough for the beginner, while including more advanced topics for the experienced developer". It also says to start each guide and each section "with the simplest, most commonly-used features" and to leave edge cases to the API documentation. The pages work this way. `components/block-content.md` runs from the default block, to conditional blocks, to block parameters, to named blocks. `routing/defining-your-routes.md` runs from basic, to nested, to index, to dynamic segments, to wildcard routes.

Skill: `SKILL.md:25` ("Don't serve both on one page; write two and link them") is too absolute.

### C2. A feature page may combine modes in a fixed internal order

`components/conditional-content.md` gives each feature a "Motivation" subsection (a worked refactor) followed by a "Usage" subsection (a compact syntax summary for return visits), for both block `if` and inline `if`. `components/component-state-and-actions.md` teaches by building a counter step by step and stops for a design explanation (derived getters versus push-based state). These pages read cleanly because the mix has a predictable order.

Skill: `SKILL.md:44` and `SKILL.md:117` ("When a page wants to do two jobs, split it") are too absolute.

### C3. Repeated failures are fine when each one motivates the next concept

The tutorial has the reader hit failures many times, and each one introduces something new. `automated-testing.md` asks the reader to delete the `<LinkTo>` to see a failing test. `route-params.md` shows links going to `/rentals/undefined`, which is how the `id` gets introduced. `service-injection.md` lets a test fail on `window.location`, which motivates the router service. `ember-data.md` shows failing tests with 404s, which motivates request handlers. `testing/testing-components.md` warns "we expect this to fail", which motivates `@tracked` and `rerender`.

Skill: `references/tutorials.md:53` ("More than once is a detour") is too absolute.

### C4. For short files, showing the whole file with change markers can beat showing a fragment

Tutorial steps reprint the whole file with removed and added lines marked, and `quick-start.md` explains the notation once ("The lines you need to remove have a minus sign in front of them…"). A reader who went off track can bring the whole file back in line with the tutorial. Examples: every `app/router.js` and template change in `building-pages.md` and `component-basics.md`.

Skill: `SKILL.md:89` ("Not the whole file every time") is too absolute for short files. (Long files are covered under F4.)

### C5. "Make them type" should apply only to what is being taught

Assets that aren't the lesson come ready to download: the stylesheet and image in `orientation.md` (with an aside saying the CSS is too long to show) and the JSON data archive in `working-with-data.md`. `tutorial/part-1/index.md` also offers the finished app up front, as a lifeline: "If you get stuck at any point during the tutorial, feel free to download…".

Skill: `references/tutorials.md:51` ("avoid 'download the finished project' until the end") is too absolute.

### C6. When tools and file paths use an older name, introduce the alias. Don't pretend there's only one term

The tooling uses older names (`ember generate acceptance-test`, `tests/integration/`), so the guides map the terms explicitly. `testing/test-types.md` has "Rendering tests (previously known as integration tests)", and `automated-testing.md` has "Acceptance tests, also known as _application tests_".

Skill: `SKILL.md:76` ("One term per concept … never vary it") doesn't allow for an alias the reader will see in commands and directory names. (Inconsistent use after the mapping is under F10.)

### C7. A deliberately unrealistic name is the right choice when the point is that the name is arbitrary

`provider-components.md` uses `as |banana|` to show that a block parameter's name is the caller's choice. `working-with-data.md` makes the same point in prose ("We could have just as easily called it something else").

Skill: `SKILL.md:91` (always use realistic domain names) needs this exception.

### C8. In a build-along tutorial, "we" and "let's" for shared work is a legitimate voice

`CONTRIBUTING.md` asks for a "friendly tone of voice". The tutorial and the component guides narrate shared work in the first person plural, as in `building-pages.md` ("let's add another one!") and `component-state-and-actions.md` ("Let's start with a small example"), and save "you" for what the reader alone does or sees.

Skill: `SKILL.md:70` ("Use second person") is stated as a universal rule.

## 3. House conventions

- **Named mascot callouts.** Asides are framed as "Zoey says…" or "Tomster says…" with a mascot image throughout the guides. The principle underneath is M5. The mascot is branding.
- **Title case for headings.** `CONTRIBUTING.md`: "Use title case for all titles and headers." This differs from `SKILL.md:75` (sentence case) as a style choice, not a principle.
- **Fence and link mechanics.** These are specific to the site's renderer and tooling: `data-filename` and `data-diff` attributes on fences, Prism language codes, relative links with set depths, inline links instead of reference-style, `/release/` in API links, and the custom spellcheck dictionary (`CONTRIBUTING.md`).

## 4. Where the Ember Guides fall short

### F1. Examples that couldn't have been run

- `testing/testing-components.md` renders `@tracked colorValue = 'red'` but asserts 'Pretty Color: orange'.
- The comment-form test in the same file has a syntax error (`actual = data; });`).
- `testing/unit-testing-basics.md` expects `'Answer 4'` from code that returns `` `Answer: ${z}` ``, and its employees test looks up `service:some-thing`.
- `services/index.md` has `remove(item)` with no opening brace.
- The wildcard-route example in `routing/defining-your-routes.md` has an unclosed `.catch(` and uses `this.router` inside a `function` callback.

Skill: `SKILL.md:60-62` and `SKILL.md:112` would have caught all of these.

### F2. Prose that drifted from its code

- `route-params.md` says the test uses `setProperties`, but the code uses a `State` class. `provider-components.md` repeats the same mistake.
- `interactive-components.md` tells the reader to edit `app/components/rental/image.js`, but the file is `.gjs`.
- `service-injection.md` describes the mock URL as `/foo/bar/baz?some=page#anchor`, but the code uses `/foo/bar?baz=true#some-section`.
- The Part 2 recap lists "Using Ember's built-in `<Input>` component" and "Working with adapters and serializers", but those chapters teach forms with `FormData` and request handlers.

Skill: `SKILL.md:111` (verify every name this session) and `references/api-reference.md:93` (duplicated content drifts).

### F3. Sections written against different eras of the API

The tutorial imports `Model` from `@warp-drive/legacy/model` and loads data with `store.request(query(...))`. `models/defining-models.md` and `models/relationships.md` import from `@ember-data/model`, and `routing/specifying-a-routes-model.md` uses `store.findAll`. Most of the guides use `.gjs`, but `routing/linking-between-routes.md` and `routing/controllers.md` still show `.hbs` templates, and `specifying-a-routes-model.md` talks about rendering in a route's "`hbs` template".

Skill: `SKILL.md:52` (record the version you documented).

### F4. Untrimmed real output and very long diffs

- `orientation.md` prints a 59-file tree that includes `dist/` hashed assets and `tmp/`, and `npm start` output with "Slowest Nodes" build lines. None of that is the lesson.
- The `map-test.gjs` diffs in `reusable-components.md` mark more than 100 lines, interleaving removed and added code, so the actual change is buried.

Skill: `SKILL.md:62` (trim with a visible elision) and `SKILL.md:89` (show the change in context).

### F5. A quickstart that is neither quick nor a single path

`quick-start.md` covers installing, a route, a component, events, `fn`, tracked state, a production build, and two Netlify deploy methods. It also offers alternatives at several points: global install or `npx`, "There are 2 ways to do so" for URL handling, and "There are two ways to do this" for deploying.

Skill: `references/tutorials.md:5` (one visible result, under five minutes) and `references/tutorials.md:46` (one path).

### F6. Minimizing words and marketing adjectives

- "Simply define a template called `loading`" (`routing/loading-and-error-substates.md`).
- "Simply add `await pauseTest();`" (`testing/index.md`).
- "a powerful (but optional) library" (`routing/specifying-a-routes-model.md`).
- "A robust development toolkit" (`getting-started/index.md`).

Skill: `SKILL.md:73` and `SKILL.md:80`.

### F7. Boilerplate openings and summaries that restate the page

- Openings: "In this section, we will cover…" (`testing/index.md`) and "In this section, you will learn about…" (`accessibility/application-considerations.md`).
- "## Summary" sections that repeat the page: `testing/index.md`, `testing/testing-tools.md`, `testing/test-types.md` and `components/introducing-components.md`.

Skill: `SKILL.md:74` and `SKILL.md:101`.

### F8. Time-relative claims that have aged

- `in-depth-topics/native-classes-in-depth.md` calls class fields and decorators "still in development".
- `working-with-html-css-and-javascript.md` says they "have not yet been fully finalized".
- `glossary/index.md` says "some even have ES6 (also known as ES2015) support" and calls Shadow DOM "still a work in progress".

Skill: `references/books.md:73` (avoid "new" and "recently"; isolate claims that age).

### F9. Images without alt text

The `<img>` tags in `ember-inspector/installation.md`, `ember-inspector/object-inspector.md` and `ember-inspector/component-tree.md`, and the console screenshot in `configuring-ember/handling-deprecations.md`, have no `alt`.

Skill: `SKILL.md:104` and `references/style.md:44`.

### F10. Terms that keep varying after the alias is introduced

After mapping the test names, the guides keep switching between them. The tutorial says "component test, also known as a rendering test" (`component-basics.md`). `testing/testing-controllers.md` and `testing/unit-testing-basics.md` introduce "container tests" without ever defining how they differ from unit tests.

Skill: `SKILL.md:76`.

## Confirmations

- `references/books.md:17` (pull listings from tested code): the tutorial pages are generated from a separate source repository, and their command output shows CI paths. Those pages have none of the broken examples found in F1.
- `references/explanation.md:14` (refute a misconception directly): `components/component-state-and-actions.md` names the urge to make `total` tracked and update it by hand, then explains why that "push-based" approach causes bugs.
- `references/learning-science.md:25` (give a second, different example): `CONTRIBUTING.md` says "it is often helpful to give two examples".
- `references/learning-science.md:65` (open with the reader's problem): almost every component guide opens with two near-duplicate components and refactors them into one.
- `references/tutorials.md:48` (name a concept on first use and link it): the tutorial italicizes each new term and links it to its guide page, for example "_[route](../../../routing/defining-your-routes/)_" and "_[component](…)_".
- `references/books.md:67` (say what can be skipped): `automated-testing.md` tells readers in a hurry they can skip the testing sections and still follow along.

## Abstracted

1. Order material so learners first do a task the laborious way and notice what it costs, then introduce the abstraction that removes that cost. End a unit on a known gap that the next unit fills.
2. When a step involves a judgment call (how much to verify, which level to test at, why order or element choice matters), explain the reasoning briefly at that step, not on a separate page.
3. Give refactoring steps a checkpoint: say in advance that nothing visible should change, and confirm it with the unchanged result and passing automated checks.
4. A running example can carry through a sequenced set of conceptual pages, not just a tutorial, as long as each page restates the starting code it builds on so a reader arriving from search can follow.
5. Use one consistent, visually distinct aside for optional depth: shortcuts, tangents, advanced options. Keep it separate from warnings, so the main text stays on the common path without hiding detail from advanced readers.
6. When the material relies on features the stated audience may not know, even within a skill they're assumed to have, write a dedicated bridging page that teaches only those features, links out for the rest, and invites readers to return when stuck.
7. Write every example the way you'd want production code written (accessible markup, safe handling of untrusted input, tests), with one line of reasoning, instead of saving good practice for its own chapter.
8. Show the older forms of an API that readers will meet in existing code, clearly labeled as legacy, so they can recognize and translate them. Don't teach them as an option.
9. When a new name appears in code, say which package or module it comes from, and tell learners that knowing this is how they search for help and documentation.
10. Give each section a landing page that sends readers to different starting points according to their situation and goal.
11. Right after the first step likely to fail, point readers to where they can get help from people, and tell them how to report a mistake in the documentation.
12. Link background concepts only to authoritative, maintained sources. Leave out posts and talks you can't keep current.
13. Set a length budget for a page, roughly a couple of screens, and split by subtopic when a page goes over.
14. In plain-text documentation source, start each sentence on a new line, so a review diff shows only the sentences that changed.
15. One page can serve beginners and experienced readers if it starts with the simplest, most common use, moves steadily to advanced uses, and leaves rare edge cases to the reference.
16. A page about a single feature may combine a motivating worked example, a short explanation and a compact usage summary, provided every feature on the page follows the same internal order.
17. Let learners run into failures as often as each failure introduces the next concept. Stop when a failure teaches nothing new.
18. For short files, showing the whole file with changed lines marked is better than a fragment, because readers can bring the whole file back in line. Explain the marking notation once, the first time it appears.
19. Have learners type what's being taught, and hand them everything else (stylesheets, sample data, images) ready-made. Offer a complete reference solution up front as a lifeline for anyone stuck.
20. When commands, directories or tools use a different or older name for a concept than your prose does, state the alias once, prominently, then use one term consistently.
21. When the lesson is that a name is the author's choice, use a deliberately absurd name to make that obvious.
22. In a build-along tutorial, narrate shared work as "we" or "let's", and keep "you" for what the reader alone does or observes.
