Source: MDN JavaScript Guide, plus the Promise and Map reference pages, commit 54ef250b

> Quotes and descriptions in this file are from [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) ([mdn/content](https://github.com/mdn/content)), by Mozilla Contributors, licensed under [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/). Quotes are short, and used to compare and criticize. Because it quotes and describes that material, this file is licensed under the same license.

# MDN JavaScript Guide vs. the baseline developer-docs skill

The skill was not touched. Its line numbers below refer to the files as I wrote them before reading MDN.

**Path shorthand.** Source files are under `sources/content/files/en-us/`.
- `G/` = `web/javascript/guide/`
- `P/` = `web/javascript/reference/global_objects/promise/`
- `M/` = `web/javascript/reference/global_objects/map/`
- `W/` = `mdn/writing_guidelines/`

Skill files are under `work/developer-docs/`.
- `SKILL.md`
- `ref.md` = `references/reference-and-guides.md`
- `teach.md` = `references/teaching.md`

**What I read.** All 37 Guide pages, the 16 Promise pages, the 17 Map pages, four JavaScript reference templates and the seven writing-guideline pages you named. I used grep for counts and line numbers. I did not read the HTML, CSS, Shell or Learn guidelines, the Live samples page, or the other page templates, except where a grep matched them.

---

## 1. Missed principles

**1.1 Look at the nearest sibling page before drafting, and copy its structure.**
- Evidence: every JavaScript template carries the same note saying the most important rule for consistency is to "look around" and copy the structure of similar pages (`W/page_structures/page_types/javascript_static_method_page_template` L71; the class, constructor and instance-method templates carry it too). It adds that related pages share structure beyond what the template requires.
- Skill: absent. `SKILL.md:14` has the agent read existing docs for facts about the software, not for page structure. `ref.md:21` and `ref.md:89` are the nearest.
- Carries over because any doc set has habits no template captures.

**1.2 Every page declares a type, and every type has a template, including the non-reference types.**
- Evidence:
  - `W/page_structures/page_types/index.md` L53-57: a `page-type` key exists "to clearly identify the type".
  - L11-15: the three broad kinds are reference (organized by the structure of the thing), guide (organized by the reader's goal) and navigation.
  - L488-494: a landing page is a menu, opening with a short summary and then a list of links.
  - L473-476: a glossary entry has a first paragraph of at most a couple of sentences, and if it outgrows about a screen it is converted to a conceptual page.
- Skill: `SKILL.md:24-31` has four modes only. `ref.md:21` asks for a template per kind of reference entry. There is no navigation page type, no short definition-entry type, and no size trigger for changing type.
- Carries over because a page whose type is declared can be checked against its type.
- Where MDN breaks it is covered under "Consistency".

**1.3 A hub page lists every child with the child's own lead sentence, and the two are kept in sync.**
- Evidence:
  - The static-method and instance-method templates (L75): "Keep this in sync with the constructor's landing page".
  - `P/index.md` L204-223 and `P/all/index.md` L10 carry the same sentence for `all()`.
  - `M/index.md` L347-370 and `M/get/index.md` L10 do the same for `get()`.
  - `G/index.md` L12-203 lists every chapter with bullets to its sections.
  - `W/writing_style_guide/index.md` L648: a landing page lists its subpages "with descriptions of each page".
- Skill: absent. `ref.md:9`, `:22` and `:86` are the nearest, and none says to reuse or sync the summary.

**1.4 State what separates look-alike siblings inside each entry, and summarize the contrast on the hub.**
- Evidence:
  - `P/all/index.md` L50: "In comparison" with `allSettled()`, then a direct instruction on which to use when.
  - `P/allsettled/index.md` L60 does the reverse.
  - `P/any/index.md` L49-51 compares with `all()` and `race()`.
  - `P/race/index.md` L249-293 has a whole example section comparing it with `any()`.
  - `P/index.md` L161-170 gives a four-line contrast list: all / allSettled / any / race.
  - The Map-vs-Object table sits at `M/index.md` L48.
- Skill: `ref.md:17` says to list "sibling entries easily confused with it" under Related. It does not say to state the condition that decides between them.

**1.5 Every example has a title naming what it shows, a lead-in saying what it does and why, and an explanation after it.**
- Evidence:
  - `W/writing_style_guide/index.md` L462-464 lists a heading naming the scenario, a description before the code and a result explanation after it.
  - `W/page_structures/code_examples/index.md` L48-49 repeats "precede" and "follow", and L50 says to break large examples into pieces with prose between.
  - The templates (L133) say a generic title like "A simple example" says nothing.
  - Good practice: `P/race/index.md` L177 and L249.
- Skill: `SKILL.md:37` and `ref.md:15` say to show an example, but nothing about titling, lead-ins, after-text or splitting.

**1.6 Mark counterexamples as wrong, visibly, next to the right version.**
- Evidence:
  - `W/code_style_guide/index.md` L180-184 gives a distinct visual mark for good and bad blocks.
  - 29 uses of the bad/good marks across 15 Guide pages, for example `G/functions/index.md` L204, `G/using_promises/index.md` L112 and L127.
- Skill: absent. `teach.md:28` and `SKILL.md:43` are the nearest.
- The marking mechanism is house convention, but the rule is not. The reader who skims or copies cannot mistake a wrong pattern for advice.

**1.7 Examples are future production code.**
- Evidence:
  - `W/code_style_guide/index.md` L21-22: readers will copy examples and may ship them.
  - L27: if an example is not production-worthy, say so in a code comment and in the prose.
  - L36-37: no needless libraries, and do not assume knowledge of frameworks.
  - L40: when combining several components, say which feature comes from where.
  - `W/code_style_guide/javascript/index.md` L855-857 gives the reason for avoiding an unsafe call even in a demo: "fewer security flaws" end up copied.
  - L846-848: do not use deprecated features for brevity.
- Skill: `SKILL.md:43` only covers the format of copyable code. `:52` covers placeholder values. Nothing says an example must model current, safe practice, or flag itself when it does not.

**1.8 Comments inside examples state intent, not mechanics.**
- Evidence: `W/code_style_guide/javascript/index.md` L76-113 says restating code in prose is not a good use of comments (L91), and comments are unnecessary when a name already says it (L103-113).
- Skill: absent. `SKILL.md:3` excludes "code comments alone" from the skill's trigger. That is about when the skill loads, not about comments inside examples.

**1.9 Delegate code layout to an automatic formatter, and let the style guide cover only what the formatter cannot.**
- Evidence: `W/code_style_guide/index.md` L106-107 (formatting debates are "a distraction from creating and maintaining content") and `W/code_style_guide/javascript/index.md` L19-21 ("there are a few additional rules").
- Skill: `ref.md:88` lints prose. Nothing covers code formatting.

**1.10 Keep version and support facts out of running prose, in one structured place maintained from a data source.**
- Evidence:
  - `W/code_style_guide/index.md` L44: do not state supported versions in prose or comments because they go stale.
  - Reference pages end with generated specification and compatibility sections driven by one data key (class template L40-41; `P/all/index.md` L325-331).
  - Status flags "should not be set manually" (class template L38).
- Skill: `SKILL.md:39` and `ref.md:16` ask for version information on each entry without saying where it lives. `SKILL.md:70` says not to hard-code versions in prose. The skill never reconciles the two.

**1.11 Pages meant to be read in order carry previous/next links at both ends.**
- Evidence:
  - 20 of 37 Guide pages open and close with a previous/next pair, for example `G/functions/index.md` L8 and L649, and `G/typed_arrays/index.md` L8 and L303.
  - `W/page_structures/page_types/index.md` L463 says to link conceptual pages that continue one discussion.
- Skill: absent. `ref.md:86` links up to a parent and across to neighbouring modes, not along a sequence.

**1.12 Do not let sibling pages become word-swapped copies, and do not ship thin pages.**
- Evidence: `W/writing_style_guide/index.md` L173-181 (near-identical pages are read by search as the same page, so write distinct concepts and examples), L183 (a floor of about 300 words, "don't artificially inflate"), L186-191 (avoid stubs, cover every parameter and exception).
- Skill: `ref.md:21` ("Sameness is the feature") covers structure only.
- MDN's own practice is mixed: `M/keys/index.md`, `M/values/index.md` and `M/entries/index.md` have near-identical bodies and examples.

**1.13 Heading hygiene, and a lead-in sentence under every heading and before every list.**
- Evidence:
  - `W/writing_style_guide/index.md` L549-553: no lone subsection, and no "bumping" heading directly followed by a subheading.
  - L545: a fourth level means split the page.
  - L568: every list gets a lead-in sentence.
  - L685-691: titles are specific, single-idea, parallel at each level, do not repeat the parent's words and do not start with an article.
- Skill: `SKILL.md:15` and `:56` cover only the task-versus-internals shape of headings.

**1.14 Do not refer to position ("above", "below", "here").**
- Evidence: `W/writing_style_guide/index.md` L138-151. Position words break for screen readers, for translated text and for layouts that reflow. Name the section by its title or the example by what it shows.
- Skill: absent. `SKILL.md:45` covers link text only.

**1.15 Neutral wording about people.**
- Evidence:
  - `W/writing_style_guide/index.md` L92-134: avoid loaded terms and violent idioms.
  - Use singular "they".
  - "The best solution" is to rewrite the sentence so no pronoun is needed. It also eases translation.
- Skill: `SKILL.md:54` covers idioms for translators. Nothing covers inclusivity.

**1.16 A related-links section is a disciplined list.**
- Evidence:
  - `W/writing_style_guide/index.md` L606-643: link text equals the target's title, items are terms, not sentences, any description follows a colon, reference pages come before guides, and internal links come before external ones.
  - L635: external items name the source and year.
  - L527-537: no third-party shorteners.
  - L507-525: prefer durable, non-promotional targets, and disclose any relationship.
  - Practice: `P/index.md` L543-547 ("on web.dev (2013)").
- Skill: `ref.md:17` and `SKILL.md:68` are the nearest. Nothing covers the form.

---

## 2. Corrections

**2.1 "Complete enough to run" (`SKILL.md:43`) is too absolute.**
- Evidence:
  - `W/code_style_guide/index.md` L27: a snippet is fine if it is made clear that it is a snippet.
  - L29-30: the aim is "reduced working examples".
  - `W/code_style_guide/javascript/index.md` L191-212: mark elisions with a comment, never a bare ellipsis, so copied code stays valid.
  - The Guide uses labelled placeholders freely, for example `G/control_flow_and_error_handling/index.md` L27-33.
- Fix: partial is fine if labelled partial.

**2.2 "Output shown in a separate block" (`SKILL.md:43`) is wrong for output of program logging.**
- Evidence:
  - `W/code_style_guide/javascript/index.md` L141-158 puts the expected output as a comment after the line that logs it, and calls a comment before it the wrong form.
  - Used throughout: `P/all/index.md` L24, `G/functions/index.md` L92.
- Scope: I have not read MDN's shell-session guidance, so I do not claim anything about commands.

**2.3 "No opinions, no 'you should'" in reference (`ref.md:24`) is too absolute.**
- Evidence:
  - `P/all/index.md` L50 tells the reader which sibling to use.
  - `P/race/index.md` L195 says to prefer the cancellation mechanism.
  - `P/symbol.species/index.md` L13 warns "Avoid relying on it if possible".
  - Template L125 says the Description alone must make the API understandable.
- Neutrality that MDN enforces is about vendors (`W/what_we_write/index.md` L25), not about advice on choosing or avoiding.

**2.4 "One-line purpose" (`ref.md:9`) is a ceiling, not a target.**
- Evidence:
  - `W/writing_style_guide/index.md` L58-61 calls a one-clause lead "far too short" because it never says what the term means.
  - L63-64 calls a long one equally wrong.
  - L83-88 shows the target: what it is, what it depends on, then links to the guides.
  - Templates ask for "1 or 2 short sentences".
  - Practice: `M/get/index.md` L10 carries the key caveat in sentence two.

**2.4a "List all error cases" (`ref.md:38`; `ref.md:13`) is too absolute for a library reference.**
- Evidence:
  - Templates L119 and L127 say to be comprehensive, but not to list errors that come from caller-supplied code or from wrong-type arguments such as a non-function callback.
  - `W/page_structures/page_types/index.md` L283-293 puts "how to fix it" on a separate error page.
- The skill's rule fits HTTP status codes, which are part of the contract. For calls into a library, errors the caller caused are noise on the entry page.

---

## 3. House conventions (kept short)

- The macro vocabulary for linking, specification and compatibility sections, live samples (blocks of one language are concatenated), a single interactive example per reference page at a fixed height, and embeds from a code repository (`W/page_structures/code_examples/index.md` L16-40, L87-92; style guide L467).
- Inclusion tied to standards tracks and a stable cross-vendor release, and neutrality between vendors (`W/what_we_write/index.md` L25-29, L50-55). Using new features in demos only once all major engines ship them (`W/code_style_guide/javascript/index.md` L25).
- Language idioms enforced in samples: `const`/`let`, arrow callbacks, template literals, strict equality, no vendor prefixes, no `alert()`, no `innerHTML` for plain text (`W/code_style_guide/javascript/index.md` L23-27, L829-875).
- One page per member, with title, slug and sentence-case rules (`W/writing_style_guide/index.md` L660-667). The terminology rules "parameters" not "arguments" (L430) and "element" not "tag" (L422).
- English prose mechanics: American spelling, serial comma, straight quotes, date format (style guide L282-408).
- Contribution policy: low-effort generated text is not accepted, and a human reviews everything (`W/what_we_write/index.md` L16, L33-34; style guide L199-203).
- Return-value wording for promise-returning functions, "already fulfilled" versus "asynchronously fulfilled" (method templates L107).
- The `lorem ipsum` placeholder (`W/code_style_guide/index.md` L220).

---

## 4. Where MDN falls short (the skill's advice is better)

**4.1 `foo`/`bar` placeholders.**
- Skill: `SKILL.md:46`.
- Evidence:
  - `W/code_style_guide/javascript/index.md` L716 asks for meaningful names and allows `foo`/`bar` only for simple, contrived cases.
  - The Map reference pages use `foo`, `bar` or `baz` 105 times across 13 of 17 pages, for example `M/get/index.md` L44-50.
  - The Promise pages use them 19 times across 7 pages.
- Caveat: reference examples demonstrate mechanism, so contrived names are partly defensible.

**4.2 One concept, two names, sometimes on the same page.**
- Skill: `SKILL.md:38`, `:67`.
- Evidence:
  - `M/foreach/index.md` calls the callback `callbackFn` in Syntax and Parameters (L34-49) and `callback` in the Description (L57-75).
  - `P/index.md` L30-42 defines "resolved" as different from "fulfilled". Yet `P/race/index.md` L114, `P/all/index.md` L122, `P/catch/index.md` L66 and `G/using_promises/index.md` L492 say "already resolved" about fulfilled promises.
  - The guide's own "parameters, not arguments" rule (L430) is broken at `P/try/index.md` L26 and `M/foreach/index.md` L62.

**4.3 An example contradicts a sibling page, and output formats drift.**
- Skill: `SKILL.md:64`, `:67`.
- Evidence:
  - `P/index.md` L329 passes a parameter to a `finally` callback, while `P/finally/index.md` L61 says it "does not receive any argument".
  - `P/then/index.md` L312-315 shows the retired `[[PromiseStatus]]` format, while `P/all/index.md` L97 shows `<state>: "fulfilled"`.

**4.4 A loose word in the middle of a precise page.**
- Skill: `SKILL.md:40`.
- Evidence: `P/all/index.md` L76 says non-promise values "will be ignored, but still counted", while the Parameters entry at L36 says they are "returned as-is".

**4.5 Time-bound claims in prose, against its own rule.**
- Skill: `SKILL.md:70`.
- Evidence:
  - `P/index.md` L531 ("Currently, incumbent realm tracking is fully implemented in Firefox").
  - `G/introduction/index.md` L75 ("Recent versions of" four browsers).
  - `G/resource_management/index.md` L129 ("At the time of writing").
  - Against `W/code_style_guide/index.md` L44.

**4.6 Prerequisites mostly unstated in guides.**
- Skill: `SKILL.md:39`, `teach.md:8`.
- Evidence: the style guide (L56) requires a guide's intro to state prerequisite knowledge. Of 37 Guide pages, only `G/introduction/index.md` L12-14 and `G/using_classes/index.md` L16 state any, by grep.

**4.7 Filler that tells the reader the answer was obvious.**
- Skill: `SKILL.md:41`.
- Evidence: `G/memory_management/index.md` L114 ("Obviously, none can be garbage-collected"), `G/closures/index.md` L77 ("obviously not the case"), `G/equality_comparisons_and_sameness/index.md` L205 and `G/internationalization/index.md` L190 ("Of course").
- MDN's style guide does not ban these words. This is the skill's added discipline.

**4.8 One concept defined twice in different words.**
- Skill: `SKILL.md:38`, `ref.md:23`.
- Evidence: `G/functions/index.md` L346-350 ("any piece of source code ... that refers to some variables") against `G/closures/index.md` L8 ("the combination of a function bundled together ... with references to its surrounding state").

**4.9 The guide lags the reference.**
- Skill: `SKILL.md:57`, `ref.md:88`.
- Evidence: `G/using_promises/index.md` L367 says "four composition tools". `P/index.md` L174 lists two more keyed methods. No Guide page mentions them (grep).

---

## Consistency: what many authors under one style guide look like

**What holds, and why.**
- Reference member pages share one skeleton. All 17 Map pages open with a bold-name sentence at L9-13.
- Fixed headings run Syntax, Parameters, Return value, then Description and Examples, with "None." for an empty list.
- Most example titles follow "Using X()".
- The generated Specifications and Compat sections end every page.
- Micro-style also holds: sentence-case headings, the marking of bad and good samples, and straight quotes.
- Cause: a template per page type plus automated formatting and linting. Almost everything that is consistent is something a template fixes or a tool checks.

**What does not hold.**
- Syntax boxes use two forms for instance methods. `M/delete/index.md` L29 writes `mapInstance.delete(key)` and `P/catch/index.md` L28 writes `promiseInstance.catch(...)`, against bare `get(key)` and `then(...)` (the template, L87, uses bare).
- The interactive example is missing from 8 of 33 pages. One is the `Map()` constructor page, although the constructor template (L77-79) asks for one.
- `M/getorinsertcomputed/index.md` L46-49 lists a non-callable-callback error that the template (L119) says not to list.
- Example titles break the template rule on "A simple example" (L133): `P/index.md` L245, L266, L332 ("Basic Example", "Example with diverse situations", "Advanced Example"), and six "Example 1/2" headings in `G/loops_and_iteration/index.md` (L170, L198, L251, L308, L332, plus "Example 2: Breaking to a label" at L264).
- Position words survive: `G/grammar_and_types/index.md` L98, `G/using_promises/index.md` L77 and L178.
- Heading hygiene breaks at `G/grammar_and_types/index.md` L244-246.
- Formatting inside one page can differ: `G/numbers_and_strings/index.md` uses pipe tables at L117, L128 and L139, and an HTML table at L163.
- Terminology breaks as shown in 4.2.

**The Guide is the less consistent half.**
- The page-type list has no template for conceptual, landing or Learn pages (`W/page_structures/page_types/index.md` L459-469, L488-494). Reference types have about two dozen.
- Without a template the Guide's endings vary: 15 pages have a "See also" section, two use other endings ("More information" at `G/grammar_and_types/index.md` L716, "What's next" at `G/introduction/index.md` L126), and the remaining 20 have none.
- Only 20 of 37 pages carry previous/next links, and none of the nine Advanced topics pages do.
- Prose voice varies by chapter, from the casual loop chapter to the formal module-graph chapter.

**How the Guide and the reference treat the same ideas, and what each leaves to the other.**
- The Guide teaches by use and sends exhaustive detail to the reference. Examples: `G/index.md` L8, `G/control_flow_and_error_handling/index.md` L14-15, `G/functions/index.md` L12. Its reference-like tables are labelled as summaries (`G/numbers_and_strings/index.md` L115 "summarizes").
- The reference defines formal vocabulary the Guide uses only loosely. `P/index.md` L17-42 and L134-157 define states, "resolved" versus "settled", and thenables. `G/using_promises/index.md` never defines them.
- The reference sends newcomers back to the Guide (`P/index.md` L11).
- Map versus Object appears in both. The Guide has four bullets and three rules of thumb (`G/keyed_collections/index.md` L42-55). The reference has a nine-row table covering security, order, serialization and performance (`M/index.md` L48). The Guide leaves the exhaustive comparison to the reference and the reference leaves the decision rule to the Guide.
- The key-equality rule is stated in both (`G/keyed_collections/index.md` L149, `M/index.md` L46), and each links to the Guide's equality page.
- Neither holds the other's updates: see 4.9.

---

## Confirmed (one line each, only where it backs something unusual in the skill)

- `SKILL.md:46`: `W/code_style_guide/javascript/index.md` L716 prefers meaningful names over `foo`/`bar`.
- `SKILL.md:64`, `:72`: `W/code_style_guide/index.md` L24-25 says run and test every example, whatever tool produced it, and do not paste unverified code.
- `SKILL.md:70`: `W/code_style_guide/index.md` L44 keeps supported versions out of prose.
- `SKILL.md:54`: `W/writing_style_guide/index.md` L133-134 and L138 tie wording choices to translation.
- `ref.md:23`: the method templates (L123) say to move description shared by many pages onto the class page and link to it.
- `ref.md:29`: the class template (L38-41) says status flags are set from data and the compatibility sections are populated from one key, not hand-written.
- `SKILL.md:37`: `W/page_structures/code_examples/index.md` L67-68 puts a runnable example near the top of reference pages for readers who do not want to read the full page.

---

## Observed, not counted

**Pages that combine explanation, how-to and reference.**
- A member page such as `P/race/index.md` holds all three:
  - Syntax, Parameters and Return value are reference.
  - Description (L45-53) is explanation: when to use it, how handlers accumulate.
  - Examples are how-to: a timeout recipe at L177-195, a state-detection recipe at L197-247, and a comparison with a sibling at L249-293.
- The class page `M/index.md` has reference lists (L319-370), a nine-row Object-vs-Map explanation (L48-242), a gotcha with a fix (L244-282) and recipes (L465-547).
- `P/all/index.md` L181-270 is a full how-to with a bad and a good version, inside a reference page.
- Guide pages mix as well. `G/numbers_and_strings/index.md` teaches and also carries reference tables for two built-in objects (L117-285). `G/using_promises/index.md` L367-426 lists the composition methods.
- The template makes this deliberate: "Readers should be able to understand the API in its entirety from this section without reading the examples section" (method templates L125).

**Skill rule it differs from.**
- `SKILL.md:13` ("Choose one mode per page. Mixing modes is the most common structural failure").
- `SKILL.md:31` ("Link between modes instead of merging them").
- `SKILL.md:69` ("The page stays in its mode").
- `ref.md:5` ("no narrative").
- `ref.md:58`.

**Where MDN keeps them apart.**
- Reference prose sits in labelled sections in a fixed order, so the three modes occupy different sections of the same page.
- Long-form teaching lives in the Guide and in a separate learning section, which the Guide introduction points to (`G/introduction/index.md` L22-26).
- The Guide hands exhaustive detail to the reference (`G/index.md` L8) and the reference hands newcomers to the Guide (`P/index.md` L11).
- A narrative regular-expressions page is split from four sibling pages and a cheatsheet (`G/regular_expressions/`).
- Shared explanation moves up to the hub rather than being repeated (templates L123).
- Navigation pages hold no teaching.

**Would I count it as a correction?**
- Yes, narrowly: the rule should be one dominant mode per page, with any other mode confined to its own labelled section in a fixed place, because the reader who lands on a single entry page from search needs the caveat there.
- The purpose of the skill's rule survives: a tutorial that stops to lecture is still a failure, and MDN does not interleave modes inside a procedure.
- It is carried into Abstracted as the last item.

---

## Abstracted

**Page structure and navigation**

1. Before you write a page, find the closest existing page of the same kind and follow its section order, heading style and phrasing habits. Depart from them only for a stated reason.
2. Give every page a declared type, and keep a template with required sections in a fixed order for each type. Cover navigation pages, short definition entries and long-form prose guides, not only reference entries. Set a size limit that triggers moving a short entry up to a fuller type.
3. A hub page lists every child with the same summary sentence the child opens with, so the two come from one source and are updated together. Put explanation shared by many children on the hub and link to it instead of repeating it.
4. When entries look alike, each one states the condition that separates it from its nearest alternative and links to it. The hub summarizes the contrast in one line per entry.
5. For pages meant to be read in order, put previous and next links at the top and bottom of every page in the sequence, including the later pages.
6. Do not give sibling pages near-identical text and examples. Write substance each page owns, so a search tool and a reader can tell them apart. Do not publish stubs.
7. Each page keeps one dominant kind of content. Other kinds are allowed only in their own labelled sections in a fixed place, and long material of another kind goes on its own page.

**Headings, lists, links and wording**

8. Never leave a lone subsection, never put a heading directly under a heading with no text between, and split the page if you need a fourth level. Open every heading and every list with a sentence of context. Make titles specific, single-purpose, parallel at each level, free of the parent's words and free of a leading article.
9. Do not refer to location with words like above, below, here or right. Name the target by its title or by what it contains, because layout differs by device, by assistive tool and by translation.
10. Use neutral wording about people: avoid gendered pronouns when gender is irrelevant (prefer rewriting so no pronoun is needed), avoid loaded terms and violent idioms.
11. A related-links section is a list of terms, not sentences. Link text equals the target's title. Put your own docs before outside ones and reference before guides, order within a group simple to advanced, and give each outside link its source and year. Prefer links you can maintain, avoid link shorteners and self-promotion, and disclose any relationship to a target.
12. Keep version and support information out of running prose. Hold it in one structured place per page, ideally generated from a data source, so it is corrected once.
13. A lead sentence must say enough that the reader knows what the thing is and its most important caveat. Treat "one line" as a ceiling to approach, not a floor. Too short fails as surely as too long; push neighbouring detail out through links.
14. Reference entries may carry guidance on choosing between siblings and on hazards, in a neutral tone. Keep longer advice in a guide and link to it.
15. List the errors a feature raises under its own contract. Leave out errors caused by caller-supplied code or wrong-type arguments. Put causes on the entry and fixes on a separate troubleshooting page.

**Examples and code**

16. Give every example a title that says what it demonstrates (never a bare number or generic label), a sentence before it saying what it does and why, and an explanation after it of the result. Split long examples into pieces with prose between them.
17. When you show a discouraged pattern, mark it visibly as wrong next to the right one and say why, so a skimming or copying reader cannot mistake it for advice.
18. Write every example as code that will be copied into production. Model current, safe, non-deprecated practice. Depend on as little outside the subject as you can, and name which parts belong to which component when you combine several. If an example is not production-grade, say so both in a code comment and in the prose.
19. A snippet may be partial if it is labelled partial and its omissions are written as comments, so the code stays valid when copied. Require completeness only where the reader is meant to run it as is.
20. Show program output as a trailing comment on the line that produces it, so the reader can follow without running. Reserve a separate output block for command sessions, where the output must not be copied with the command.
21. In example code, comments state intent or a non-obvious fact. They never narrate what a line plainly does, and a well-named call needs no comment.
22. Let an automatic formatter settle code layout, and use the style guide only for the rules a formatter cannot enforce.
