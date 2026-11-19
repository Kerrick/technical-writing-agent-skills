# Often-broken check

This checks every Kept entry in `merged.md` whose Kind includes "baseline, often broken": #1, 2, 3, 4, 5, 12, 13, 23, 24, 25, 50, 51, and 52. For each source listed as breaking the entry, the breakage is classified as one of:

- **Lapse:** what the source does is objectively wrong, or its own style guide states the rule it breaks.
- **Deliberate:** it's in the source's templates or style guide, or it has the same form on nearly every page of that kind.
- **Unexamined:** it appears on some pages and not others, and the style guide says nothing either way.

Checkouts are under `~/Developer/`: `react.dev`, `guides-source` (Ember), `django`, `rails`, `book` (Rust), `content` (MDN), `postgres`. Delta file sections are cited as, for example, `ember-guides.md` F1. Counts of pages were taken with `grep` over each checkout at the commit named in its delta file.

## Classifications

| Entry | Source | Class | Evidence |
| - | - | - | - |
| #1 Ease words | A | Unexamined | Three pages (`react-learn.md` §4). `react.dev/CONTRIBUTING.md` has no rule on wording. |
| #1 | B | Unexamined | Two "Simply" uses (`ember-guides.md` F6). The style guide (`guides-source/CONTRIBUTING.md:49-140`) asks for a "friendly tone" but doesn't mention these words. |
| #1 | C | Lapse | `django/docs/internals/contributing/writing-documentation.txt:445-449` bans "easily", "simply", "just", "merely", and "straightforward". The pages still use them more than 20 times (`django-docs.md` §4). |
| #1 | D | Unexamined | "easily" in about ten of 23 guides (`rails-guides-1.md` 4.3, `rails-guides-2.md` F2). Neither `ruby_on_rails_guides_guidelines.md` nor `api_documentation_guidelines.md` bans them; `:47` says only "Write simple, declarative sentences." |
| #1 | E | Unexamined | Two uses (`rust-book.md` §4). `book/style-guide.md` and `book/CONTRIBUTING.md` say nothing about wording. |
| #1 | F | Unexamined | Seven uses across six pages (`mdn-js-guide.md` F5). The MDN writing guidelines don't ban the words; the style guide uses "of course" and "Obviously" itself (`writing_style_guide/index.md:127, 186`). |
| #1 | G | Unexamined | Two tutorial uses (`postgres-manual.md` F1). `docguide.sgml`'s Style Guide (`:468` on) covers only reference-page layout, and uses "simply" itself (`:183`). |
| #2 Run every example | A | Lapse | A `json` block that isn't valid JSON, a call to `updateMyTodos` when the example defines `updateMyList` (`updating-arrays-in-state.md:680` vs `:768`), and an entry whose `id` doesn't match its key (`react-learn.md` §4). `CONTRIBUTING.md` also says "Try to follow your own instructions." |
| #2 | B | Lapse | The test sets `colorValue = 'red'` but asserts "Pretty Color: orange" (`testing/testing-components.md:188` vs `:193`). There are also syntax errors and missing braces (`ember-guides.md` F1). |
| #2 | D | Lapse | A test for a method that's never defined, invalid JSON, and an unclosed ERB tag (`rails-guides-2.md` F6). Also a wrong status code and a version contradiction (`rails-guides-1.md` 4.1). |
| #2 | E | Lapse | The code declares `let mut x = 42;` but the warning output shows `= 0` (`appendix-04-useful-development-tools.md:38` vs `:52`). Cargo output from an old release, and one example that uses an undefined variable (`rust-book.md` §4). |
| #2 | F | Lapse | `"Success"` vs `"Success!"`, a duplicate `const` that is a syntax error (`mdn-js-guide.md` F4). `writing_guidelines/code_style_guide/index.md:24`: "Run and test every code example before you submit it." |
| #2 | G | Deliberate | The tutorial keeps its sample data in shipped files and points to them instead of printing the data: `query.sgml:29-35` (`src/tutorial/`), `advanced.sgml:20-26` ("not repeated here"), and `xtypes.sgml:23` and `xfunc.sgml:70` for later chapters. The data for the cited queries exists in `postgres/src/tutorial/advanced.source:18-38`. |
| #3 One job per page | D | Deliberate | Component guides put explanation, catalog, how-to, and reference on one page, in a fixed order with one mode per top-level heading: `association_basics.md:18, 141, 1441, 2562`, `routing.md:18, 100, 1384`, `rails_on_rack.md:16, 212, 291`, `caching_with_rails.md:18, 818` (`rails-guides-1.md` and `rails-guides-2.md`, "Observed, not counted"). The cited tables are labeled as an extract and link to the full list (`testing.md:373-377`). The unlabeled help dump (`testing.md:549`) and the deployment and search-engine sections in the configuration reference (`configuring.md:4433, 4921`) depart from that design. |
| #3 | G | Unexamined | Upsert and `UPDATE … FROM` are taught only on reference pages because `dml.sgml` is thin (`postgres-manual.md` F7, "Imbalance"). Other commands get a teaching chapter (the split table at the top of `postgres-manual.md`). `docguide.sgml` says nothing about it. |
| #4 End with what the reader can do | B | Unexamined | Restating "## Summary" sections on 5 of 188 pages (`ember-guides.md` F7). The style guide says nothing about endings. |
| #4 | C | Deliberate | Every part of the tutorial ends with the same one-sentence handoff, "When you're comfortable with …, read part N … to learn …", and nothing else: `intro/tutorial01.txt` through `tutorial07.txt` (last lines of each). `tutorial08.txt` ends the series the same way. |
| #4 | E | Deliberate | 21 of 22 chapters end with a "## Summary" that recaps the concepts covered and previews the next chapter: for example `ch04-03-slices.md`, `ch06-03-if-let.md`, `ch10-03-lifetime-syntax.md`, `ch11-03-test-organization.md`, and `ch12-06-writing-to-stderr-instead-of-stdout.md`. |
| #4 | F | Unexamined | 2 of 38 guide pages have a "Conclusion" or "Summary" heading; one restates the page and the other lists what the reader now has (`mdn-js-guide.md` F7). The guidelines say nothing about endings. |
| #4 | G | Unexamined | One instance: the tutorial's last section, "Conclusion" (`advanced.sgml:719`). `docguide.sgml` says nothing about it. |
| #5 Realistic names | C | Unexamined | `foo`/`bar`/`MyModel`-style names appear in 68 of 240 files under `intro`, `topics`, `ref`, and `howto`. Other pages use realistic domains, such as the polls tutorial. `writing-documentation.txt` has no rule on example names. |
| #5 | E | Unexamined | Two `foo` examples (`rust-book.md` §4) in a book that otherwise uses a domain for each project. The style guide says nothing about names. |
| #5 | G | Unexamined | `foo`/`bar` with no data shown at `queries.sgml:748` and `:889`. The same chapter and the tutorial use `weather`, `products`, and tables with their data shown (`postgres-manual.md`, split table). `docguide.sgml` says nothing. |
| #12 Marketing adjectives | A | Unexamined | Three pages (`react-learn.md` §4). `CONTRIBUTING.md` says nothing about it. |
| #12 | B | Unexamined | Two uses (`ember-guides.md` F6). The style guide says nothing about it. |
| #12 | D | Unexamined | "seamless", "very powerful", and "robust" on a handful of guides (`rails-guides-1.md` 4.3, `rails-guides-2.md` F2). Neither Rails guideline file mentions them. |
| #12 | F | Unexamined | "powerful" on four pages (`mdn-js-guide.md` F5). The style guide has no rule, and uses "more powerful" as a sample sentence itself (`writing_style_guide/index.md:387`). |
| #13 Verify facts, record version | A | Lapse | Contradictory facts: one page recommends the preset of a tool that another page says is deprecated, and the framework lists don't match. There's also a link to a legacy site (`react-learn.md` §4). |
| #13 | B | Lapse | Prose names files and methods that the code doesn't use, and sections are written against two eras of the API (`ember-guides.md` F2, F3). |
| #13 | D | Lapse | A link labeled "303 Unprocessable Content" points to the 303 page, when the status meant is 422 (`layouts_and_rendering.md:192`). The guides show `Rails 8.1.0` as expected output, but also require 8.2.0 or newer (`rails-guides-1.md` 4.1). A stale default is described (`rails-guides-2.md` F5). |
| #13 | E | Lapse | Cross-references point to a renamed function, a section that never uses the named item, and the wrong listing number (`rust-book.md` §4). |
| #23 One term per concept | B | Unexamined | Test-type names keep varying after the alias is given, and "container tests" is never defined (`ember-guides.md` F10). The style guide fixes only its own three terms (Guides, guide, section). |
| #23 | D | Unexamined | `:unprocessable_entity` in two guides and `:unprocessable_content` in two others (`rails-guides-1.md` 4.2). Both work: Rails converts one to the other (`actionpack/lib/action_dispatch/http/response.rb:48-55`). `api_documentation_guidelines.md:98` requires consistency only for component names. |
| #24 Checkable objectives | A | Unexamined | 43 of 47 Learn pages have a "You will learn" block. About 72 of roughly 100 items start "How to…"; the "What/Why/When" items cited are the minority. `CONTRIBUTING.md` says nothing about it. |
| #24 | D | Unexamined | The prologue is a template (`ruby_on_rails_guides_guidelines.md:29-31`, "what they will learn"; 45 of 77 files use "you will know:"). But 133 of about 175 items start "How", and the "What…"-style items cited are the minority. The guideline doesn't specify how the items are phrased. |
| #24 | E | Deliberate | Nearly every chapter opener lists topics: "In this chapter, we'll discuss:" (`ch01-00-getting-started.md:4`), `ch06-00-enums.md:3`, `ch08-00-common-collections.md:10`, `ch13-00-functional-features.md:13`, `ch15-00-smart-pointers.md:29`, `ch16-00-concurrency.md:42`. |
| #25 Claims that age | B | Lapse | Class fields are called "still in development" and "not yet been fully finalized", and the glossary says "some even have ES6 support". All three are false today (`ember-guides.md` F8). |
| #25 | D | Lapse | The guides give an old YJIT default that the configuration reference shows has changed, and cite browser and framework versions from a decade ago (`rails-guides-2.md` F5). |
| #25 | E | Unexamined | Four "at/as of the time of this writing" claims. The three checked are still true at this commit (`appendix-05-editions.md:27`, `ch20-05-macros.md:258`, `ch11-01-writing-tests.md:110`). The style guide says nothing about it. |
| #50 Open with the outcome | B | Unexamined | 11 of 188 pages open with "In this section/guide, we/you will…" (`ember-guides.md` F7). The style guide says nothing about it. |
| #50 | G | Unexamined | 18 of 68 chapters open with "This chapter describes/discusses…" (`postgres-manual.md` F4). `docguide.sgml` says nothing about chapter openings. |
| #51 Pin versions | A | Deliberate | Every install command in Learn is unpinned or uses `@latest`: `creating-a-react-app.md:32, 44, 54`, `build-a-react-app-from-scratch.md:37`, `react-compiler/installation.md:26, 32, 38, 190`, `add-react-to-an-existing-project.md:53`. |
| #51 | C | Deliberate | Nearly every third-party install is an unpinned `python -m pip install <name>`: the ASGI and WSGI deployment how-tos (uvicorn, daphne, hypercorn, gunicorn, uwsgi), `howto/outputting-pdf.txt:29`, and `intro/tutorial08.txt:38`. A minimum version appears only where one is required. The docs are versioned with each release (`django-docs.md` §4 caveat). |
| #52 Complete deprecation notes | C | Unexamined | `ref/request-response.txt:1255-1257` and `ref/paginator.txt:54-57` give no removal version or replacement. The settings deprecations at `ref/settings.txt:1414-1505` give both. The style guide describes the version directives (`writing-documentation.txt:737-813`) but not what a deprecation note must contain. |
| #52 | D | Unexamined | `configuring.md:1528` names a removal version but no replacement. `:1631` and `:1950` name a replacement but no removal version. Neither Rails guideline file says what a deprecation note must contain. |

## Results

### #1. Don't call a task easy: redundant with the skill

One lapse (C) and six unexamined. That's fewer than two lapses or two deliberate, and the entry is baseline only. The rule is already `SKILL.md:73` (also `references/style.md:40`).

### #2. Run every example as written: keep as "baseline, often broken"

Five lapses (A, B, D, E, F). G is deliberate: it keeps sample data in files that ship with the material, and points to them from the page. That doesn't change the result. The deliberate pattern also isn't the failure the rule targets, as long as the page says where the data is.

### #3. One primary job per page: keep as a correction only

D is deliberate and G is unexamined. That's fewer than two of either kind. The entry is also a correction in its own right, so it stays a correction, without the "baseline, often broken" label. D's deliberate design (several modes on one page, one mode per top-level heading, in a fixed order) is already what the corrected rule allows.

### #4. End with what the reader can now do: correction candidate

Two deliberate (C, E). Both sources end every lesson in a sequence with a fixed, brief closing instead of a skills list. One uses a single sentence that names what the reader should now be comfortable with and hands off to the next part. The other uses a short section that recaps the concepts covered and previews what comes next. Neither ends with a list of skills, and both apply their closing to every lesson in the sequence.

### #5. Realistic names for real use: keep as a correction only

Three unexamined (C, E, G). The breakages are scattered, so "often broken" isn't supported. The entry is also a correction, so it stays as one.

### #12. No marketing adjectives: redundant with the skill

Four unexamined. The rule is already `SKILL.md:80`.

### #13. Verify every fact against its source: keep as "baseline, often broken"

Four lapses (A, B, D, E).

### #23. One term per concept: keep as a correction only

Two unexamined (B, D). In D, both names work, so it isn't an error. The entry is also a correction, so it stays as one.

### #24. Write objectives as checkable actions: redundant with the skill

E is deliberate, and A and D are unexamined. In A and D, the opening block is a fixed template, but most items in it already name actions; the uncheckable items are the minority. The rule is already `SKILL.md:48` (also `references/learning-science.md:57-59`, `references/books.md:27`).

### #25. Avoid claims that age: keep as "baseline, often broken"

Two lapses (B, D). E's dated claims are still true, so they're unexamined.

### #50. Open with the outcome, not an announcement: redundant with the skill

Two unexamined (B, G). The rule is already `SKILL.md:74`.

### #51. Pin versions in install commands: correction candidate

Two deliberate (A, C). Both sources consistently install the newest release, unpinned or with an explicit latest tag, in every install command. In one, the docs are versioned with each release. In the other, the docs track the current release. Either way, the reader installs what the page describes. They add a version constraint only where a minimum is actually required.

### #52. Complete deprecation notes: redundant with the skill

Two unexamined (C, D). Each source writes complete notes on some pages and incomplete ones on others. The rule is already `references/api-reference.md:104`.

### Summary

| Result | Entries |
| - | - |
| Keep as "baseline, often broken" | #2, #13, #25 |
| Correction candidate | #4, #51 |
| Keep as a correction only | #3, #5, #23 |
| Redundant with the skill | #1 (`SKILL.md:73`), #12 (`SKILL.md:80`), #24 (`SKILL.md:48`), #50 (`SKILL.md:74`), #52 (`references/api-reference.md:104`) |

## For the writer

**Rules that well-run documentation breaks by mistake.** Each of these is broken in several mature documentation sets, and each time it's an error, not a design choice. Check these hardest in every draft:

- Run every example in order from the page's starting state, and make the shown output match what the code produces.
- Check every name, version, cross-reference, and factual claim against its source, and keep facts consistent across pages.
- Don't make statements that depend on when they were written. They become false later, and readers can't tell when.

**Rules that mature documentation breaks on purpose.** Treat these as open to correction:

- **Lesson endings.** In a sequence of lessons, a fixed, brief closing on every lesson works. It can be one sentence naming what the reader should now be comfortable with and pointing to the next lesson, or a short recap of the concepts covered followed by a preview of the next one. A list of skills is one way to end, not the only way. What matters is that the closing is short, the same on every lesson, and points forward.
- **Version pinning.** When the documentation is versioned with each release, or always describes the current release, installing the newest release without a pin is a sound choice: the reader gets the version the page was written for. Add a version constraint where a minimum version is actually required.

**Rules that hold as written.** These were broken only here and there, with nothing in the sources to defend the breakage. Keep them as they are:

- Don't call a task easy or obvious.
- Don't use promotional adjectives.
- State objectives as actions the reader can perform and check.
- Open with the outcome or the answer, not an announcement of what the page will do.
- In a deprecation note, give what is deprecated, since when, its replacement, and when it will be removed.

**Correction rules whose baseline turned out not to be broken in practice.** The corrected versions of these three still stand. The breakages were scattered, so they don't justify warning that the rule is often broken:

- One primary job per page, with other material only in short, labeled sections.
- Realistic names for real use, and neutral names only for pure mechanism.
- One term per concept, with any second name declared once.

**A note on sample data.** Keeping a tutorial's setup data in a separate file that ships with the material, and telling the reader on the page where it is, doesn't break the rule to run every example. The page still has to say where the data is, and the data has to produce the output shown.
