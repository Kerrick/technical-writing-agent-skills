# Check of the "baseline, often broken" entries

Input: the 15 entries in `merged.md` whose Kind includes "baseline, often broken", and each source listed as breaking them (47 entry-source pairs). The baseline skill in `developer-docs/` was read only, not changed.

Classes, as defined for this check:
- **Lapse**: objectively wrong (can't run, factual error, stale or contradictory text), or the source's own style guide states the same rule.
- **Deliberate**: by design and contrary to the skill's rule: in the source's template or style guide, or on at least 80% of pages of that kind, counted.
- **Unexamined**: on some pages and not others, and the style guide says nothing either way.

Evidence tags: **[checked]** means I opened the source checkout under `sources/` and confirmed it. **[report]** means I relied on the comparison file and did not re-open the checkout.

## Reading notes

1. **Absence is not treated as design.** When the breakage is an element a source leaves out (exercises, stated versions, recovery steps), I classed it Deliberate only if a template or style guide prescribes the omission. A high count of pages without the element was not enough, because every unrequired element is absent by default. This reading affects entries 19 and 20. If omission on 80% or more of pages should count as design, both could gain two Deliberate sources and become correction candidates. I did not do those counts.
2. **Entry 34, source C.** The report's finding is output sharing a block with its command, which is 1 of 16 console blocks. The entry's rule also says "without prompts", and that clause is broken in 16 of 16 blocks by a style-guide directive. I classed on the prompt clause.
3. **Where a checkout disagreed with a report:** G's tutorial data (entries 12 and 35) is supplied in a script with a pointer, which meets the entries' "or is supplied" clause, so that breach is weak. C's version-in-prose finding (entry 4) is narrower than the report implied, because the style-guide rule covers Django versions, not Python versions.
4. Entries 4 and 21 carry a folded-in correction. This check tests only the baseline breakage and leaves the folded-in correction as `merged.md` has it.

## Table

### 1. Cut words that say it is easy or obvious (SKILL.md:41, :42)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 1 | B | Unexamined | Words like simply, easy, obviously, of course on 47 of 188 guide pages (85 lines) [checked]. `CONTRIBUTING.md` has no rule on them; its only hit is ordinary use at :6 [checked]. |
| 1 | C | Lapse | `howto/windows.txt:89`, `topics/forms/formsets.txt:778`, `howto/custom-management-commands.txt:99`, `intro/tutorial06.txt:21` [report]. `internals/contributing/writing-documentation.txt:445-449` says to avoid words that minimise difficulty, naming "easily", "simply", "just" [checked]. |
| 1 | D | Unexamined | `getting_started.md:171`, `:1878`, `:1943`; filler counts in `security.md` and `engines.md`, some literal [report]. Neither `ruby_on_rails_guides_guidelines.md` nor `api_documentation_guidelines.md` has a rule on such words [checked]. |
| 1 | E | Unexamined | `ch17-05:339` "obviously", `ch09-02:404` "Of course" [report]. Neither `style-guide.md` nor `CONTRIBUTING.md` has a rule on them [checked]. |
| 1 | F | Unexamined | `G/memory_management` L114, `G/closures` L77 and others [report]. `writing_style_guide/index.md` has no ban and itself uses easy, easily, Obviously, of course (L174, L181, L186, L189) [checked]. |
| 1 | G | Unexamined | 26 matches across five chapters, 17 in `ddl` [report]. `docguide.sgml` has no rule and itself says "simply use" at :183 [checked]. |

### 2. Run every sample and check it against its text (SKILL.md:64, :65)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 2 | A | Lapse | `choosing-the-state-structure.md:1066-1072` gives key 39 `id: 40`, the same id as key 40; the later copies at `:1402-1408` are consistent [checked]. |
| 2 | B | Lapse | `components/conditional-content.md:57` has `<template>` where the closing tag belongs [checked]. `testing-components.md:193` asserts 'orange' on data 'red' [report]. |
| 2 | D | Lapse | `layouts_and_rendering.md:192-193` names the status "303 Unprocessable Content" while the code uses `:unprocessable_content` [checked]. `form_helpers.md:677` and `association_basics.md:1494` [report]. |
| 2 | E | Lapse | `appendix-04-useful-development-tools.md:38` has `let mut x = 42`; the pasted warning at `:52` shows `let mut x = 0` [checked]. |
| 2 | F | Lapse | `promise/index.md:329` passes `info` to a `finally` callback; `promise/finally/index.md:61` says the callback "does not receive any argument" [checked]. |

**Result: 5 lapses. Keep as "baseline, often broken".**

### 4. Avoid stale content (SKILL.md:70)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 4 | B | Lapse | `quick-start.md:64` shows `VITE v6.3.6`; `orientation.md:226` and `reusable-components.md:109` show `VITE v8.0.11` [checked]. `native-classes-in-depth.md:499` pins `/ember/3.27/` [report]. |
| 4 | C | Unexamined | `howto/windows.txt:21` "At the time of writing, Python 3.15 is the latest version" [checked], on one page; `intro/tutorial01.txt:26` uses a substitution. `writing-documentation.txt:809-813` bans naming a Django version outside a version-change block, which is narrower than this case. |
| 4 | D | Lapse | `install_ruby_on_rails.md:109` shows Rails 8.1.0 while `getting_started.md:75-76` requires Rails 8.2.0 and Ruby 3.4, and `:196` prints ruby 3.3.5 [checked]. `tuning_performance_for_deployment.md:136` vs `configuring.md:658`; `engines.md:1659` vs `asset_pipeline.md:80` [report]. |
| 4 | F | Lapse | `promise/index.md:531` "Currently...", `resource_management:129` "At the time of writing", `introduction:75` "Recent versions of..." [checked]. `code_style_guide/index.md:44`: "Do not specify supported browsers and their versions in code comments or prose, as this information quickly becomes outdated" [checked]. |
| 4 | G | Lapse | `start.sgml:365` prints a gcc 4.9.2 (Debian) compiler string and `:371` prints `current_date` 2016-01-07 [checked]; stale. 24 "Currently" in six reference pages [report]. `docguide.sgml` is silent, so this rests on staleness, not a style-guide rule. |

**Result: 4 lapses. Keep as "baseline, often broken".**

### 10. State shared facts once (reference-and-guides.md:23, SKILL.md:70)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 10 | D | Unexamined | `action_mailbox_basics.md:84-100`, `:180-196`, `:254-270` repeat one setup for three servers; `association_basics.md:710-765` vs `:1241-1299` [report]. The two guides' guidelines have nothing on duplication [checked]. |
| 10 | F | Lapse | `map/keys` and `map/values` are word-swapped copies: same sections, same example, only the method name and result differ [checked]. `writing_style_guide/index.md:173-181` says near-identical sibling pages, "just a few words swapped out and using the same example", hurt findability and should be written from scratch [checked]. |
| 10 | G | Unexamined | `queries.sgml:1957-1963` vs `ref/select.sgml:1549-1556` near-verbatim LIMIT paragraph; one sentence repeated seven times in `ref/select.sgml` [report]. `docguide.sgml` has no rule on duplication [checked]. |

**Result: 1 lapse, 0 deliberate. The entry carries its own correction (repeat the costliest trap), so keep it as a correction only.**

### 11. Literal prose; warm voice in teaching pages (SKILL.md:54, books-and-video.md:43, SKILL.md:41)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 11 | A | Unexamined | `lifecycle-of-reactive-effects.md:159`, `keeping-components-pure.md:120`, `escape-hatches.md:57` [report]. `CONTRIBUTING.md:19` asks only to match the surrounding tone and style [checked]. Three pages are cited with no count and no template, so nothing shows design. |
| 11 | G | Unexamined | `dml.sgml:260`, `ddl.sgml:81,104,2289`, `docguide.sgml:63` [report]. `docguide.sgml` has no voice rule; its hits for style, plain and tone are all about DocBook stylesheets [checked]. |

**Result: 0 lapses, 0 deliberate. The entry carries its own correction (warm voice in teaching pages), so keep it as a correction only.**

### 12. A page must hold together when walked literally (SKILL.md:66)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 12 | B | Lapse | `tutorial/part-2/recap.md:32` lists the built-in `<Input>` component, but part 2 uses a form and `FormData` (`provider-components.md:248`, `:280`, `:337`) [checked]. `interactive-components.md:120` says `.js`, the file is `.gjs` [report]. |
| 12 | C | Lapse | `faq/troubleshooting.txt:46-52` promises "two common pitfalls" and lists one [checked]. |
| 12 | D | Lapse | `plugins.md:475` names `to_throttled_response`; the code at `:513` defines `to_throttled_json` [checked]. `form_helpers.md:677` [report]. |
| 12 | G | Unexamined | `advanced.sgml:24-27` says the sample data is "not repeated here" but supplies it in `advanced.sql` with a pointer [checked]. That meets the entry's "or is supplied" clause, so the breach is weak. The query and DML chapters give their data inline. `docguide.sgml` is silent. |

**Result: 3 lapses. Keep as "baseline, often broken".**

### 13. One term per concept, updated everywhere (SKILL.md:38, :57, :67)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 13 | A | Lapse | `escape-hatches.md:309` link text "Lifecycle of Reactive Events" points to the page "Lifecycle of Reactive Effects" [checked]. "diner's order" vs "guest's order" (`adding-interactivity.md:242`, `render-and-commit.md:22`) [report]. |
| 13 | B | Lapse | `models/defining-models.md:18` imports `@ember-data/model`; `tutorial/part-2/ember-data.md:98` imports `@warp-drive/legacy/model`; `.hbs` fences beside `.gjs` pages [report]. |
| 13 | E | Lapse | `ch20-05-macros.md:113` says "Listing 20-29" for the macro pattern pieces; the macro is Listing 20-35 (`ch20-05:80`) and 20-29 is the closure example (`ch20-04:55`) [checked]. `gen_range` vs `random_range` [report]. |
| 13 | F | Lapse | `map/foreach` uses `callbackFn` in Syntax (:34-49) and `callback` in the Description (:57-75) [checked]. "resolved" used for fulfilled promises against the page's own definition (`promise/index.md:30-42`) and the "parameters, not arguments" rule at `writing_style_guide/index.md:430`, broken at `promise/try` L26 and `map/foreach` L62 [report, rule checked]. |

**Result: 4 lapses. Keep as "baseline, often broken".**

### 19. State prerequisites and the version the page is true for (SKILL.md:39, teaching.md:8, :14)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 19 | A | Unexamined | Version-dependent syntax with no version stated in `typescript.md:263`, `managing-state.md:744`, `manipulating-the-dom-with-refs.md:366`, `separating-events-from-effects.md:461`; the only version statement is `react-compiler/installation.md:19` [report]. `CONTRIBUTING.md` has no rule on stating versions or prerequisites [checked]. Omission, not a prescribed pattern (reading note 1). |
| 19 | B | Unexamined | `quick-start.md:25` and `orientation.md:28` [report]. `CONTRIBUTING.md` has no rule; its only version line (:11) says old versions are frozen [checked]. Omission (reading note 1). |
| 19 | F | Lapse | `writing_style_guide/index.md:56`: a guide's intro "should inform the reader about ... the prerequisite knowledge the reader is expected to have" [checked]. Only 2 of 37 Guide pages state any (`introduction/index.md:12-14`, `using_classes/index.md:16`) [report]. |

**Result: 1 lapse, 0 deliberate. The entry is baseline only, so mark it "redundant with the skill" (SKILL.md:39; teaching.md:8, :14).**

### 20. Exercises (teaching.md:33, :27)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 20 | B | Unexamined | One challenge prompt (`part-2/provider-components.md:536`) and one "exercise we won't cover" (`quick-start.md:296`); no questions, solutions or recall checks [report]. `CONTRIBUTING.md` has no rule on exercises [checked]. Omission (reading note 1). |
| 20 | E | Unexamined | `ch03-05` summary (three programs to try), `ch08-03` (three exercises, no answers); no solutions anywhere in `src/` [report]. `title-page.md` points to a separate interactive edition for quizzes, but neither `style-guide.md` nor `CONTRIBUTING.md` prescribes omitting them [checked]. |
| 20 | G | Unexamined | `query.sgml:593-599`, the one tutorial exercise, has no expected result [report]. The other tutorial chapters have none; `docguide.sgml` is silent [checked]. |

**Result: 0 lapses, 0 deliberate. The entry is baseline only, so mark it "redundant with the skill" (teaching.md:33).**

### 21. Links and cross-references resolve (SKILL.md:68)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 21 | D | Lapse | `working_with_javascript_in_rails.md:361` links `using_hotwire_in_rails.html`; the file is `using_hotwire_with_rails.md`, and `:28` of the same page spells it correctly [checked]. |
| 21 | E | Lapse | `ch17-06:104` links `ch17-04-streams.html#composing-streams` and `ch17-05:541` links `ch17-03-more-futures.html#working-with-any-number-of-futures`; no such headings exist in `ch17-0*` [checked]. `ch20-04` points to the wrong chapter for pinning [report]. |

**Result: 2 lapses. Keep as "baseline, often broken".**

### 32. Reserved, clearly fake placeholder values (SKILL.md:52)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 32 | A | Unexamined | `@mail.com` in 4 of 47 top-level Learn pages (57 occurrences) while `add-react-to-an-existing-project.md` uses `example.*` [checked]. 9% of pages. `CONTRIBUTING.md` is silent on placeholders [checked]. |
| 32 | D | Unexamined | gmail.com or mail.com in 4 guide files (12 occurrences) against `example.*` in 25 files (185 occurrences) [checked]. Both guidelines files are silent on placeholders [checked]. |

**Result: 0 lapses, 0 deliberate. The entry is baseline only, so mark it "redundant with the skill" (SKILL.md:52).**

### 33. Pasted output from a real run, no stale detail (SKILL.md:53, :64, :70)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 33 | E | Lapse | `ch01-03-hello-cargo.md:126,152,170,181` show the old "Finished dev [unoptimized + debuginfo] target(s) in ... secs" form; `ch02-00:390,:490` print "latest Rust 1.96.0" while `title-page.md:6` says 1.99.1; `appendix-04:38` vs `:52` [checked]. |
| 33 | G | Lapse | `start.sgml:365` prints a 2015-era compiler string and `:371` prints `current_date` 2016-01-07 [checked]: hard-coded environment output that has gone stale. This is the weaker of the two (two lines, one chapter, `docguide.sgml` silent). |

**Result: 2 lapses. Keep as "baseline, often broken".**

### 34. Keep copyable commands in blocks of their own (SKILL.md:43)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 34 | B | Deliberate | Tutorial parts 1 and 2: 14 shell fences on the 8 of 8 pages that have any; all 14 start with a `$` prompt, and 12 of 14 (86%) put the captured output in the same fence (`more-about-components.md:19-22`, `automated-testing.md:33-35`, `orientation.md:26-29`) [checked]. The pages are generated from a separate tutorial repository (`part-1/index.md:1`), so the form comes from the template. Unprompted commands appear only in `quick-start.md`, which is outside that count. |
| 34 | C | Deliberate | `writing-documentation.txt:676-716` requires `.. console::` blocks written with a `$` prompt (:703-706) [checked]. All 16 console blocks in `intro/tutorial01-08` start with `$` (16 of 16); only 1 of 16 (`tutorial02.txt:233-239`) also holds the output [checked]. Reading note 2. |

**Result: 2 deliberate. This becomes a correction candidate. What both do by design: command lines inside the code block carry a prompt marker as the standard form for walk-through material. One of them, in nearly all of its command blocks, also shows the real captured output directly under the command in the same block. The other keeps output separate in most blocks. The evidence shows the practice and its consistency. It does not show how readers copy the text.**

### 35. Known-good state and everything the lesson needs (teaching.md:17, SKILL.md:66)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 35 | C | Unexamined | No tutorial part ends with a repository or tag (only third-party links in `intro/tutorial0*.txt`) [report], but per-step file trees and "you should see" lines exist (`tutorial01.txt:242-255`), and the entry's rule accepts an expected file listing. The style guide is silent. |
| 35 | G | Unexamined | Same finding as entry 12: data supplied in `advanced.sql` with a pointer, so it is weak [checked]. `docguide.sgml` is silent. |

**Result: 0 lapses, 0 deliberate. The entry is baseline only, so mark it "redundant with the skill" (teaching.md:17; SKILL.md:66).**

### 36. Show recovery at the point of failure (teaching.md:18)

| Entry | Source | Class | Evidence |
| - | - | - | - |
| 36 | D | Unexamined | `getting_started.md` has nine "you should see" lines and no "if you see X instead" [report]. `engines.md:806`, `:903` show the error and the fix at the point of failure [report], so it varies by page. The guidelines and `getting_started.md` have no "if you see", "troubleshoot" or "recover" text [checked]. |
| 36 | G | Unexamined | `start.sgml:171-173` and `:47-48` defer to the site administrator [report]; `start.sgml:163-210` quotes four client errors with causes [report]. It varies within one chapter, and `docguide.sgml` is silent. |

**Result: 0 lapses, 0 deliberate. The entry is baseline only, so mark it "redundant with the skill" (teaching.md:18).**

## Summary of results

| Entry | Lapse | Deliberate | Unexamined | Result |
| - | - | - | - | - |
| 1 Cut words that say it is easy | 1 | 0 | 5 | Redundant with the skill (SKILL.md:41) |
| 2 Run every sample | 5 | 0 | 0 | Keep: baseline, often broken |
| 4 Avoid stale content | 4 | 0 | 1 | Keep: baseline, often broken |
| 10 State shared facts once | 1 | 0 | 2 | Correction only (repeat the costliest trap) |
| 11 Literal prose; warm voice | 0 | 0 | 2 | Correction only (warm voice in teaching pages) |
| 12 Walk the page literally | 3 | 0 | 1 | Keep: baseline, often broken |
| 13 One term per concept | 4 | 0 | 0 | Keep: baseline, often broken |
| 19 Prerequisites and version | 1 | 0 | 2 | Redundant with the skill (SKILL.md:39) |
| 20 Exercises | 0 | 0 | 3 | Redundant with the skill (teaching.md:33) |
| 21 Links resolve | 2 | 0 | 0 | Keep: baseline, often broken |
| 32 Reserved placeholders | 0 | 0 | 2 | Redundant with the skill (SKILL.md:52) |
| 33 Real output, no stale detail | 2 | 0 | 0 | Keep: baseline, often broken |
| 34 Commands in blocks of their own | 0 | 2 | 0 | Correction candidate |
| 35 Known-good state | 0 | 0 | 2 | Redundant with the skill (teaching.md:17) |
| 36 Recovery at the point of failure | 0 | 0 | 2 | Redundant with the skill (teaching.md:18) |

Totals across the 47 pairs: 23 lapses, 2 deliberate, 22 unexamined.

## For the writer

These results come from comparing a set of baseline documentation-writing rules with seven large published documentation sets. For each rule the sets were seen breaking, I asked whether the breaking was a mistake, a deliberate house choice, or just uneven practice.

**Keep as written. Real documentation breaks these by accident.** In each case the breakage was an outright error or an inconsistency that plain checking, or the set's own conventions, would have caught.
- Run or compile every sample, and compare the real output with what the surrounding text says it shows.
- Walk each page from its stated starting point and confirm that everything it promises or relies on is actually present.
- Use one term per concept, spelled identically in prose, code and cross-references, and update every occurrence, including sibling pages, when anything is renamed.
- Make every link and cross-reference resolve to the thing it names, and recheck them after any restructuring or renaming.
- Paste output only from a real run of the code shown, and do not freeze environment details that age.
- Do not let content go stale for avoidable reasons: version numbers, support claims and time-relative wording in running prose, and statements that a newer page contradicts.

**Keep the rule but change its emphasis.** The rule was not broken often by accident. The useful finding is a limit on how far it goes.
- Shared facts belong in one place that other pages link to. The exception is the single costliest trap. Repeat that where the reader first meets the feature, in a length that suits the page, and treat each copy as something to recheck when its source changes.
- Prose should stay literal enough to survive translation and non-native readers. In teaching and community pages, a warm personal voice is legitimate: address the reader, pose the problem before the answer, and prefer concrete statements to stacked superlatives. Light humour is acceptable there, and lookup pages stay plain.

**Relax this one, after weighing it.** The rule to keep prompt characters out of command examples and to put output in a separate block is stricter than what established documentation sets do on purpose. Two of them mark command lines with a prompt character inside the code block as their standard form, and one of those mandates it in its style guide for every command block. In its step-by-step lessons, the other also shows the real captured output directly beneath the command in the same block for most commands. The evidence shows the practice and its consistency. It does not show what readers end up copying, so treat this as a candidate change rather than a settled one.

**No change needed. The baseline already covers these.** The departures found were scattered, appeared on some pages and not others, and had no written convention behind them. They were also not frequent enough to count as a pattern. The rules are: avoid words that minimise difficulty or announce that something is obvious; state prerequisites and the version a page is true for; give exercises a checkable outcome, a separate solution and a difficulty marker; use reserved or plainly fake placeholder values; give the learner a known-good state to compare against or return to; and show recovery at the step where failure is common. One caveat applies to the prerequisite-and-version rule and the exercise rule. Many pages simply leave the element out. I did not treat omission as a deliberate choice without a written convention behind it. If very frequent omission should count as design, those two rules need a proper count before they are left alone.
