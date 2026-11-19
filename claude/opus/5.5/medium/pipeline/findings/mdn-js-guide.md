Source: MDN JavaScript Guide, plus the Promise and Map reference pages, commit 54ef250b

> Quotes and descriptions in this file are from [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) ([mdn/content](https://github.com/mdn/content)), by Mozilla Contributors, licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/). Quotes are short, and used to compare and criticize. Because it quotes and describes that material, this file is licensed under the same license.

# Deltas: technical-writing skill vs. MDN JavaScript Guide

Paths below are relative to `~/Developer/content/files/en-us/` unless they start with `sidebars/`. Shorthand: `G/` = `web/javascript/guide/`, `R/` = `web/javascript/reference/global_objects/`, `WG/` = `mdn/writing_guidelines/`. Skill paths are relative to `~/.agents/skills/technical-writing/`.

## 1. Missed principles

### M1. Put the wrong version next to the right one, labeled, especially when the wrong version seems to work

MDN pairs mistaken code with corrected code and labels each as bad or good (`example-bad` / `example-good`). It uses this most for mistakes that run without errors but give wrong results. 15 of the Guide's index.md files and 18 of the Guide/Promise/Map files contain a labeled bad example. Examples:
- `G/using_promises/index.md`, about lines 112–175: a `then` handler that forgets `return`. The page shows that the next step gets `undefined`, or runs before the work finishes, and then shows the fix.
- `R/map/index.md`, lines 244–282: setting bracket properties on a Map seems to work, but `has()` and `delete()` don't see them. The correct `set()` usage follows.
- `R/promise/all/index.md`, around line 223: awaiting independent tasks one after another, then the concurrent fix. Also passing functions instead of promises.

The guidelines ask for this explicitly: `WG/code_style_guide/index.md:180–184`.

Skill: absent as a general technique. The nearest line is `references/tutorials.md:53` ("Teach one error on purpose… More than once is a detour"), which limits it to once per tutorial. `references/explanation.md:14` covers wrong mental models, not wrong code.

### M2. Show the expected value next to the expression that produces it

Snippets put the result in a trailing comment on the same line, so the code still runs when pasted and a reader can predict output without running it. The guideline is `WG/code_style_guide/javascript/index.md:143–167`. Examples:
- `G/grammar_and_types/index.md:110` (`console.log(x); // logs "undefined"`)
- `G/expressions_and_operators/index.md`, the `&&`, `||` and `??` tables at about lines 728–757
- `R/map/get/index.md:48–49`

When output depends on ordering, pages add a block comment that lists the log lines in order (`G/using_promises/index.md:497`; `R/promise/all/index.md:136–139`).

Skill: `SKILL.md:88` says to show output "after the code", and `SKILL.md:92` says to keep output in separate blocks. Both are written with commands in mind. Neither covers annotating values inline, inside the code.

### M3. Explain a feature by showing equivalent code written with simpler parts, and label where the equivalence stops

Reference and guide pages often describe a feature by showing the longer code it replaces. They also say how exact the match is.
- `R/promise/withresolvers/index.md:35`: exactly equivalent.
- `R/map/getorinsert/index.md:44–58`: equivalent, plus a looser form described as "slightly less reliable" when null values are allowed.
- `R/promise/promise/index.md:144–162`: "roughly equivalent", followed by a numbered list of exactly where the two differ.
- `R/promise/try/index.md:61–73`: "almost exactly equivalent", and a second form that looks equivalent but isn't.
- `G/grammar_and_types/index.md:169`: hoisted code rewritten as the order in which it actually runs.

When the equivalent code is only an illustration, the page says so: `R/promise/finally/index.md:71–72` and `G/memory_management/index.md:214–215` (each says it is not a polyfill), and `R/promise/symbol.species/index.md:30`.

Skill: absent. `references/explanation.md:11` ("Make the machine visible") is the closest, but it talks about diagrams and component names, not code.

### M4. A reference entry's prose must be complete without its examples

All three member-page templates say readers should understand the API fully from the Description section without reading the examples. Examples in the description should be short and need not be realistic. Sources: `WG/page_structures/page_types/javascript_constructor_page_template/index.md:133`, and the same sentence in the static- and instance-method templates (line 125 of each). The Promise pages follow this. For example, `R/promise/then/index.md:61–80` states the return rules, how the returned value is resolved, and subclassing before any example appears.

Skill: absent. `references/api-reference.md` covers what each parameter description must contain, but says nothing about whether prose or examples carry the definition.

### M5. Document behavior at the edges and the things that don't happen

Promise return values are documented by case: empty input, all inputs already settled, pending input, and whether the result arrives at once or later. Examples:
- `R/promise/all/index.md:42–44`
- `R/promise/any/index.md:41–43` (empty input rejects)
- `R/promise/race/index.md:43` (empty input stays pending forever)
- `R/promise/then/index.md:50–59`

Pages also state the effects a reader might expect that don't occur. Three pages say settling the combined promise does not cancel the remaining work (`R/promise/all/index.md:54`, `R/promise/any/index.md:55`, `R/promise/race/index.md:53`). `R/map/symbol.species/index.md:26–27` says the property is currently unused.

Skill: `references/api-reference.md:77–84` lists default, range, interactions and "when you'd set it". It doesn't mention boundary inputs, timing, or expected effects that don't happen.

### M6. For readers coming from other systems, map each concept to the one they know and flag where it differs

`G/language_overview/index.md` is aimed at "readers with background in other languages" (line 10). It compares features to other languages throughout:
- line 107: template literals compared with f-strings and interpolated strings
- line 200: says that most other languages would print 1 and 2 here, then explains why this one throws
- line 294: there is no `elif`
- line 346: unlike Rust, control flow is not an expression
- line 545: compared with `*args`, and why there is no `**kwargs`

`G/closures/index.md:43` does the same for readers from block-scoped languages.

Skill: `references/explanation.md:13` covers bounding analogies. `SKILL.md:21–25` covers naming what the reader knows. Neither tells you to use the reader's prior system as the reference point and mark where it diverges.

### M7. Refer to other parts of a page by name, not by position

The style guide forbids "above", "below", "here" and similar directional words. It asks writers to name the section or describe what the example shows, because layout differs across screens, screen readers and translations (`WG/writing_style_guide/index.md:136–151`).

Skill: absent for written text. `references/video-scripts.md:35` bans "as shown above" only in narration.

### M8. Give every example a heading that says what it shows, an introduction, and an explanation afterward

`WG/writing_style_guide/index.md:459–466` requires each example to have a descriptive heading, a short lead-in, and an explanation of the result. `WG/page_structures/code_examples/index.md:48–49` says the same. The templates reject headings such as "A simple example" (for example, `javascript_static_method_page_template/index.md:133`). Reference pages follow this: "Using NaN as Map keys" and "Cloning and merging Maps" (`R/map/index.md:400, 488`), and "Using Promise.race() to implement request timeout" (`R/promise/race/index.md:177`).

Skill: absent. Heading rules (`SKILL.md:75`) cover page and task headings, not example headings.

### M9. Comments in example code should state intent, not restate the code

`WG/code_style_guide/javascript/index.md:78–113` says to comment why or what for, and shows bad examples that just narrate the loop or repeat a self-explaining function name.

Skill: absent. `SKILL.md:84–93` has no rule about comments in code.

### M10. Mark omitted code with a comment so the snippet still runs when pasted

`WG/code_style_guide/javascript/index.md:191–212` puts `…` inside a comment, and says what the reader should add, because a bare ellipsis makes pasted code fail. The Guide follows this: `G/control_flow_and_error_handling/index.md:31`, and `G/using_classes/index.md:660`.

Skill: `SKILL.md:62` covers elision in output only. It says nothing about code that must stay valid.

### M11. Examples must model safe, current practice, because readers paste them into production

`WG/code_style_guide/index.md:21–22` says readers will copy examples into production, so examples must not be insecure, inefficient or inaccessible. Line 39 bans deprecated features used to save space. `WG/code_style_guide/javascript/index.md:846–875` lists the risky APIs to avoid and why.

Skill: `SKILL.md:86–93` covers whether code runs, its size and its names. It doesn't cover whether examples model good practice.

### M12. Navigation pages are their own kind of page

MDN treats pages whose main job is to route readers as a separate type: a short summary followed by a structured list of child pages, each with a description (`WG/page_structures/page_types/index.md:15, 488–494`; `WG/writing_style_guide/index.md:645–658`). `G/index.md` is one. Each chapter gets a one-line overview link and links to its key sections (lines 12–189).

Skill: absent. The four modes in `SKILL.md:31–36` give a landing page nowhere to belong.

### M13. Sibling pages need their own content

`WG/writing_style_guide/index.md:173–181` warns that near-identical pages for related members get confused with each other by search and readers. It asks for different examples and an explanation of how each member differs.

Skill: absent.

### M14. When readers commonly blur two terms, define the difference and acknowledge the loose usage

`R/promise/index.md:30–42` separates "resolved" from "fulfilled". It says people colloquially treat them as the same, then gives code where a promise is resolved but still pending. `R/promise/resolve/index.md:42` and `R/promise/promise/index.md:46` repeat the distinction where it matters.

Skill: `SKILL.md:76` says to define a term on first use and not vary it. It doesn't address terms that readers already use loosely.

## 2. Corrections

### C1. "Never foo/bar" is too absolute

`WG/code_style_guide/javascript/index.md:716` prefers realistic names but allows `foo` and `bar` "when the example is simple and contrived". In practice, 41 of the files read use `foo` or `bar`. They appear mostly where the point is a syntax mechanism with no domain at all: `G/grammar_and_types/index.md:100`, `R/map/get/index.md:46–49`, `G/meta_programming/index.md:224–228`. In those snippets a domain noun would add something to think about without teaching anything.

Skill: `SKILL.md:91` ("never `foo`/`bar`").

### C2. "One term per concept" needs an exception for declared synonyms

`G/agent_communication_and_coordination/index.md:15` uses two terms on purpose. It states once that it will use them interchangeably, says which one is technically precise, and gives the reason: the precise term reads unnaturally for general concepts. The rest of the page uses both without confusion.

Skill: `SKILL.md:76` ("never vary it").

### C3. Warnings are also justified for code that hangs, crashes, or silently misbehaves

MDN uses only 5 warnings in the Guide, against 83 notes. It reserves them for traps that look harmless:
- an object literal at the start of a statement is parsed as a block (`G/grammar_and_types/index.md:471–472`)
- infinite recursion (`R/promise/resolve/index.md:172–173`)
- freezing the page (`G/agent_communication_and_coordination/index.md:775–776`)
- illustrative code that must not be copied (`R/promise/finally/index.md:71–72`)

The sparing use supports the skill's reason for the rule. The categories show its list is too narrow.

Skill: `SKILL.md:79` ("Reserve warnings for data loss, security, and money").

### C4. Don't write availability versions into prose when they vary by implementation; keep them in one maintained data source

The style guide bans browser versions in prose and code comments "as this information quickly becomes outdated" (`WG/code_style_guide/index.md:44`). None of the 33 reference pages has a "since" line. Each ends with a generated compatibility section instead. When behavior changed, the prose tells readers to check that section rather than naming versions (`R/map/index.md:46`).

Skill: `references/api-reference.md:103` ("Version every entry that changed: 'Since 2.3.0'"), and the template at line 69. That advice holds when there is one implementation, but it is too absolute when there are several.

### C5. Reference pages shouldn't be "austere" in their description

See "Observed, not counted" below. Member templates say "Be as comprehensive as possible" (`javascript_constructor_page_template/index.md:131`). Class pages carry the concept explanation that all member pages link to. The structure is uniform; the prose isn't minimal.

Skill: `references/api-reference.md:3` ("Be austere and consistent").

## 3. House conventions (don't carry over)

- **Macros and generated sections.** Link macros (`jsxref`), one `InteractiveExample` per reference page placed after the introduction (`WG/page_structures/code_examples/index.md:36–37, 92`), live samples that join code blocks before running them (`WG/writing_style_guide/index.md:467`), and generated Specifications and Browser compatibility sections.
- **Inclusion rule.** Document only standards-track features shipped in at least one engine (`WG/what_we_write/index.md:50–55`).
- **Mechanics.** American spelling, the serial comma, "parameters" rather than "arguments", straight quotes only, the "January 1, 1900" date format, and Prettier-enforced code formatting (`WG/writing_style_guide/index.md:309–438`; `WG/code_style_guide/index.md:107`).
- **JavaScript idioms in examples.** `const`/`let`, `for...of`, `===`, `textContent` instead of `innerHTML`, and no `alert()` (`WG/code_style_guide/javascript/index.md`, throughout).
- **Minimum length.** About a 300-word floor per page, for search ranking (`WG/writing_style_guide/index.md:183`).

## 4. Where MDN falls short

### F1. Broken back link

`G/working_with_objects/index.md:8` correctly links back to Keyed collections. The matching links at line 517 point back to Regular expressions, which skips Indexed and Keyed collections.

Skill: `SKILL.md:110` (every prerequisite is stated and linked), `SKILL.md:117` (anything that isn't this page's job moves to its own page, with a link).

### F2. Dead end after Modules, and pages with no sequence at all

`G/modules/index.md:8, 734` has only a "previous" link. The three Modules sub-pages, the five regular-expression sub-pages, the Temporal cookbook and all nine advanced pages have no previous/next links (grep for `PreviousNext|Previous|Next` in those files returns nothing). The regular-expression sub-pages also have no sidebar entry: `sidebars/jssidebar.yaml:31–32` gives Regular expressions no children, while Dates and Modules list theirs (lines 27–30, 51–57). A reader going page by page stops at Modules.

Skill: `SKILL.md:81` (every page must stand alone and link its prerequisites), plus `references/books.md` on sequencing.

### F3. Two different orders for the same pages

`G/index.md:195–203` lists the advanced topics as Language overview, Data structures, Enumerability, Inheritance, Equality, Closures, and so on, all under one heading. `sidebars/jssidebar.yaml:59–82` splits them into Intermediate and Advanced and orders them differently: Equality before Enumerability, and Closures before Inheritance.

Skill: `SKILL.md:116` (headings alone outline the page).

### F4. Examples that weren't run

- `R/promise/catch/index.md:87` resolves with `"Success"`, but the comments at lines 91 and 104 say the log shows `"Success!"`.
- `G/internationalization/index.md:491, 495` declares `const lf` twice in one block, which is a syntax error.
- The same page at lines 327–330 logs one formatter but shows the output comments for three.

`WG/code_style_guide/index.md:24` requires running every example.

Skill: `SKILL.md:60–62`.

### F5. Words the skill bans, which the style guide allows

- "Easy": `G/loops_and_iteration/index.md:10` ("quick and easy").
- "Obviously": `G/memory_management/index.md:114`, `G/closures/index.md:77`.
- "Powerful": `G/using_classes/index.md:745`, `G/iterators_and_generators/index.md:78`, `G/representing_dates_times/index.md:234`, `G/inheritance_and_the_prototype_chain/index.md:10`.

MDN's style guide doesn't ban these words, so this is a gap in the guide, not a lapse by contributors.

Skill: `SKILL.md:73, 80`.

### F6. Prerequisites stated on some pages only

- `G/introduction/index.md:12` and `G/using_classes/index.md:16` state what the reader should know.
- `G/agent_communication_and_coordination/index.md:12` names the page to read first.
- `G/loops_and_iteration/index.md`, `G/keyed_collections/index.md` and `G/closures/index.md` state none, though readers arrive at them from search.

`WG/writing_style_guide/index.md:56` asks guides to state prerequisites.

Skill: `SKILL.md:81`.

### F7. An ending that repeats the page

`G/inheritance_and_the_prototype_chain/index.md:622–630` ("Conclusion") restates the lookup mechanism the page has already traced in detail. `G/resource_management/index.md:437–443` is different: it lists the components the reader now has, which is closer to what the skill allows.

Skill: `SKILL.md:101`.

### F8. Generic example headings

`G/loops_and_iteration/index.md` has "Example", "Example 1" and "Example 2" headings (lines 63–378). `G/control_flow_and_error_handling/index.md:36, 171` does the same. Both contradict MDN's own rule (M8).

Skill: `SKILL.md:116`.

## How well one style guide holds many contributors together

**What it keeps consistent:**
- All 33 Promise and Map reference pages have the same section order: Syntax, Parameters, Return value, (Exceptions), Description, Examples, Specifications, Browser compatibility, See also. Sections that don't apply are still present ("None.", as in `R/map/clear/index.md:37`).
- Every opening sentence follows one formula ("The **`x()`** method of `Map` instances…").
- Headings use sentence case.
- Good and bad examples are labeled the same way.
- Code formatting is uniform, enforced by Prettier.
- Omitted code is marked with `// …`.

**What it doesn't keep consistent:**
- Directional words, despite `WG/writing_style_guide/index.md:138`. There are more than 30 hits, including `G/indexed_collections/index.md:49, 51, 128, 149`, `G/internationalization/index.md:110–130` and `G/agent_communication_and_coordination/index.md:336–895`.
- "And" in titles, despite `WG/writing_style_guide/index.md:687`. Five early chapter titles break it: Grammar and types, Control flow and error handling, Loops and iteration, Expressions and operators, Numbers and strings.
- Generic example headings (F8).
- Banned APIs in examples. `alert()` appears in `G/introduction/index.md:116` and `G/control_flow_and_error_handling/index.md:182`, against `WG/code_style_guide/javascript/index.md:875`. `XMLHttpRequest` appears in `R/promise/index.md:414` and `R/promise/promise/index.md:175`, against line 852 of the same guide.
- Legacy API in a teaching example. `G/using_classes/index.md:22–28` opens with the legacy `Date` object, though `G/representing_dates_times/index.md:606` calls it legacy and says to avoid it.
- Prerequisites (F6).
- Previous/next navigation (F2).

**The pattern:** rules a tool or template can enforce (section skeletons, formatting, labels) hold everywhere. Rules that depend on each writer remembering them (wording, headings, API choice, navigation links) hold only on recently revised pages.

## Confirmations (only where they back something unusual in the skill)

- **Split concept from task and link both ways.** The dates guide sends snippet-seekers to the cookbook, and the cookbook sends readers back to the guide for concepts (`G/representing_dates_times/index.md:12`; `.../cookbook/index.md:11`). This backs `SKILL.md:44`.
- **Write shared topics once and link to them.** Concurrency and thenables are explained once on the class page (`R/promise/index.md:134–190`), and all, any, race and others link there. This backs `references/api-reference.md:91`.
- **Refute the wrong model directly.** The equality page names the "loose-to-strict spectrum" model and shows the case that breaks it (`G/equality_comparisons_and_sameness/index.md:150–152`). This backs `references/explanation.md:14`.
- **Match nearby pages before following generic rules.** Every template says "look around" and copy the structure of similar pages (`javascript_class_page_template/index.md:68`). This backs `SKILL.md:27`.

## Observed, not counted

Both kinds of page mix modes, in two different ways.

**Reference pages hold explanation and how-to in clearly separated sections.**
- `R/promise/index.md` puts a conceptual account (states, how "resolved" relates to "fulfilled", thenables, the job queue, concurrency, and incumbent settings objects at lines 464–531) in Description. It ends with member lists and task-style examples ("Loading an image with XHR").
- `R/map/index.md:48–242` has an explanation-style Object-versus-Map comparison table. Its examples on cloning and merging (lines 488–547) are small how-tos.
- `R/promise/promise/index.md:128–164` explains the internal resolve algorithm.
- `R/promise/catch/index.md:116–155` adds a "Gotchas" set.

Because the headings fix where each kind of content goes, a reader looking something up can skip the explanation. Shared concepts live on the class page, which saves repeating them on every member page.

**Guide chapters embed reference material inline.**
- `G/expressions_and_operators/index.md:69–86, 332–434, 453–535` reproduces operator tables.
- `G/numbers_and_strings/index.md:117–143, 163–285` lists every `Number` and `Math` member.
- `G/representing_dates_times/index.md:329–383, 459–504` has two large property and method grids.
- The regular-expression sub-pages are mostly reference tables, and `cheatsheet/index.md` copies all four of them again.

Skill line: `SKILL.md:44` ("When a page wants to do two jobs, split it and link the halves").

I count the reference-page pattern as a correction (C5): a reference landing page can rightly hold the shared explanation, as long as it sits in its own section separate from the member lists. I don't count the Guide pattern, because copying reference tables into explanation chapters creates a second copy to maintain. The cheat sheet duplicating the sub-pages shows the cost, so it supports the skill rather than correcting it.

## Abstracted

1. Show a mistaken version next to the corrected one, with each clearly labeled, whenever readers commonly make that mistake. Do this especially when the mistaken version runs without error but gives a wrong result. Use it as many times as there are real traps, not once per document.
2. Annotate snippets with the value each expression produces, as a comment on the same line or right after it. The code should stay runnable when pasted, and readers should be able to predict the result without running it. When order matters, list the outputs in the order they appear.
3. Explain a construct by showing the longer code built from simpler parts that it stands for. Say whether the equivalence is exact, approximate or only illustrative, and list where it breaks. Mark any illustrative implementation as unfit to copy.
4. Write each reference entry's description so it fully defines the behavior without its examples. Examples illustrate; they must not be the only place a rule is stated.
5. In reference entries, document behavior at the edges: empty input, input that is already complete, whether results arrive at once or later, and what happens when nothing qualifies. State plainly which effects a reader might expect that do not happen.
6. For readers experienced in another system, explain each concept by pointing to its counterpart there, and call out exactly where the two behave differently.
7. Refer to other parts of a document by section name or by what an example shows, never by position such as "above" or "below". Position changes with layout, screen readers and translation.
8. Give every example a heading that says what it demonstrates, an introductory sentence on what to watch for, and an explanation afterward of the result and how it works.
9. In example code, use comments to state intent or why something is done. Don't use them to restate what the next line obviously does.
10. When you omit part of a code sample, mark the gap in a form the language accepts, such as a comment, and say what belongs there. A pasted snippet should still run.
11. Assume every example will be pasted into production. Model current, safe and accessible practice even when a shortcut would be shorter, and never use a deprecated or risky construct just to save space.
12. Treat navigation pages as their own page type. Open with a short summary of the area, then give a structured list of child pages with one line on what each covers.
13. Give each sibling page (related members, paired options) its own explanation and its own examples. Near-identical sibling pages are hard to tell apart for both search engines and readers.
14. When readers routinely use two terms as if they meant the same thing, define the difference, say that loose usage exists, and show a case where the difference matters.
15. Placeholder names are acceptable when an example has no domain and exists only to show a mechanism. Use realistic names when the example models real use.
16. A precise term may share a page with a more natural synonym, as long as you declare the equivalence once at the start, say which term is exact, and give the reason.
17. Use warning callouts for any trap that silently gives wrong results, hangs, crashes, or invites copying code that isn't meant for use. Not only for data loss, security and money. Keep them rare enough that readers still notice them.
18. When support or availability varies across several implementations, keep that information in one maintained, structured source and point to it from the prose. Don't hand-write version numbers into the text, where they go stale.
19. A reference landing page can hold the conceptual explanation that all its member entries share, as long as that explanation sits in its own clearly labeled section, separate from the member listing. Keep member entries uniform in structure but substantive in content, not minimal.
