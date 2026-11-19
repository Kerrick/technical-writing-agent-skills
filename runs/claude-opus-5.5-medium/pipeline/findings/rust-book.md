Source: The Rust Programming Language, commit 9be0936

> Quotes and descriptions in this file are from [The Rust Programming Language](https://doc.rust-lang.org/book/) ([rust-lang/book](https://github.com/rust-lang/book)), copyright (c) 2010 The Rust Project Developers, licensed under the [MIT License](https://github.com/rust-lang/book/blob/main/LICENSE-MIT) or the [Apache License 2.0](https://github.com/rust-lang/book/blob/main/LICENSE-APACHE). Quotes are short, and used to compare and criticize.

# Differences between the Rust book and the technical-writing skill

Read: all 112 chapter files in `src/` in SUMMARY.md order, plus `style-guide.md` and `CONTRIBUTING.md`. Listings were opened only where a claim depended on them. All `src/` paths are relative to `~/Developer/book/src/`. Skill paths are relative to `~/.agents/skills/technical-writing/`.

## 1. Missed principles

### M1. Mark code that is meant to fail, before the reader runs it
The book warns, in prose and in a visual marker, that a listing won't compile, will panic, or doesn't do what's wanted, so a reader typing along doesn't think they made a mistake. The introduction says so explicitly (`ch00-00-introduction.md:177-191`, the Ferris table). Ninety-eight code fences carry `does_not_compile`, `panics`, or `not_desired_behavior` (grep across `src/`). The prose also flags the listing before it appears: "Note that this code won’t compile just yet" (`ch02-00-guessing-game-tutorial.md:598`). The same pattern occurs at `ch07-05…:16`, `ch12-03…:265`, `ch16-02…:36`, `ch18-03…:55`, and more than a dozen other places.
Skill: absent. tutorials.md:53 allows one deliberate error but says nothing about labeling it.

### M2. Keep old anchors alive when you rename a heading
Sixty-three files carry `<!-- Old headings. Do not remove or links may break. -->` followed by `<a id="…">` tags for headings that were renamed (161 occurrences; for example `ch01-02-hello-world.md:15-16`, `ch04-01-what-is-ownership.md:236-238`).
Skill: absent. SKILL.md:81 and style.md:14-18 cover links but not link durability.

### M3. Number listings, refer to them by number, and re-show a listing instead of sending the reader back
Every substantial listing has a number and a caption, and later prose names it ("Listing 9-13"). When a chapter returns to code from far earlier, it reproduces it. Examples: "Reproduction of the `Config::build` function from Listing 12-23" (`ch13-03-improving-our-io-project.md:16`), and "a function in Listing 4-9, shown again in Listing 10-25" (`ch10-03-lifetime-syntax.md:413-416`).
Caveat: numbered cross-references drift. `ch20-05-macros.md:113` says "Listing 20-29" for the macro that is Listing 20-35 (line 80).
Skill: absent. SKILL.md:86 asks only for the file name.

### M4. Say which parts of shown output will differ for the reader
The book tells readers when their output will legitimately differ. Versions and line order may vary (`ch02-00-guessing-game-tutorial.md:407-409`). Thread interleaving changes between runs (`ch16-01-threads.md:51-54`, `ch16-02-message-passing.md:261-264`). Hash map iteration order is arbitrary (`ch08-03-hash-maps.md:73`).
Skill: absent. SKILL.md:88 and SKILL.md:62 say to show real output but not to flag what varies.

### M5. Show the cost of not having a feature before introducing it
Before a feature appears, the book writes working code without it and makes the pain visible:
- Returning ownership through tuples ("too much ceremony", `ch04-01-what-is-ownership.md:503-515`) leads into references.
- An index that drifts out of sync with its string (`ch04-03-slices.md:75-109`) leads into slices.
- Separate variables, then a tuple, then a struct (`ch05-02-example-structs.md:3-104`).
- Duplicated code, then a function, then generics (`ch10-00-generics.md:31-115`).

Skill: absent. SKILL.md:77 says to show a concrete example first. learning-science.md:65 says to open with the reader's problem. Neither says to build the worse version so the reader feels the cost.

### M6. Tell readers where people usually struggle, and that struggling there is normal
The book flags the hard spots ahead of time:
- Compiler errors "do _not_ mean that you’re not a good programmer" (`ch03-01-variables-and-mutability.md:31-34`).
- Ownership takes time; "Keep at it!" (`ch04-01-what-is-ownership.md:12-15`).
- Strings are a common sticking point, with the reasons why (`ch08-02-strings.md:3-8`).
- Exclusive borrowing is "something that new Rustaceans struggle with" (`ch04-02-references-and-borrowing.md:131-134`).

Skill: absent. learning-science.md:63-65 covers motivation in general, not naming known difficulty in advance.

### M7. Map new ideas onto what the reader already knows from other tools, and say where the mapping breaks
The audience is assumed to know another language (`ch00-00-introduction.md:89-95`). The book keeps tying concepts to those languages:
- Compiling compared with gcc and clang, and with Ruby/Python/JS (`ch01-02-hello-world.md:164-205`).
- C/C++ `->` compared with automatic referencing (`ch05-03-method-syntax.md:95-139`).
- Traits are like interfaces, "although with some differences" (`ch10-02-traits.md:12-13`).
- async in C# and JavaScript, with "significant differences" (`ch17-01-futures-and-syntax.md:21-24`).
- Other languages' names for a hash map (`ch08-03-hash-maps.md:6-8`).

Skill: explanation.md:13 bounds analogies in general. Mapping to the reader's existing toolset is absent.

### M8. When an example cuts a corner for teaching, say so and say what real code would do
- The web server isn't "the best way to build a web server" (`ch21-00-final-project-a-web-server.md:23-31`).
- Production code would handle errors "more gracefully" (`ch21-01-single-threaded.md:162-164`).
- Lowercasing "won’t be 100 percent accurate… If we were writing a real application, we’d want to do a bit more work" (`ch12-05-working-with-environment-variables.md:65-68`).
- A whole section explains why examples call `unwrap` (`ch09-03-to-panic-or-not-to-panic.md:20-36`).

Skill: absent.

### M9. Invite experiments and predictions right where the example is, using the tool as the feedback loop
- "Try adding code to `main` that uses `s` and `x`" (`ch04-01-what-is-ownership.md:473-476`).
- "Make hypotheses… before you compile; then, check" (`ch10-03-lifetime-syntax.md:309-312`).
- "figure out what the output will be _before_ running the code" (`ch17-02-concurrency-with-async.md:173-181`).
- "try to figure out what the code will print before running this code" (`ch19-03-pattern-syntax.md:28-30`).
- "Try adding a `println!` there to see what error message you get" (`ch13-01-closures.md:231-232`).

Skill: learning-science.md:31 and books.md:37-40 put prediction and retrieval at the end of a chapter. Inline, tool-checked experiments are absent.

### M10. Show the calling code you want before building what it calls
- The as-yet-unwritten `can_hold` is used before it's defined (`ch05-03-method-syntax.md:143-156`).
- The desired `blog` usage comes first (`ch18-03-oo-design-patterns.md:54-56`).
- "writing the client interface first can help guide your design" (`ch21-02-multithreaded.md:92-97`).
- An "imagined `timeout`" is used before it's implemented (`ch17-03-more-futures.md:166-175`).

Skill: absent. The tutorials.md:12-13 template shows the end result of a whole tutorial, not the target interface of each step.

### M11. Insulate examples from a fast-moving third-party ecosystem with a small wrapper package
`ch17-01-futures-and-syntax.md:44-59` describes a purpose-built crate that re-exports and sometimes renames the pieces the chapter needs "to keep you focused on the details relevant to this chapter", with its source available for anyone curious.
Skill: absent. SKILL.md:93 only says to pin versions.

### M12. Give one setup step that prefetches everything the material will need
`ch01-01-installation.md:153-179` ("Working Offline with This Book") shows one command sequence that caches every dependency the book uses, plus a flag to use the cache from then on.
Skill: absent. books.md:81 asks for setup in advance only for workshops.

### M13. When one source feeds both print and web, write links that survive the conversion
The style guide says links become "text at *url*" in print, so link text must read well that way. Web-only links are marked to be dropped from print, and internal links are relative so the docs work offline (`~/Developer/book/style-guide.md`, "Links"). The `<!-- ignore -->` markers appear on almost every chapter cross-reference (for example `ch01-02-hello-world.md:12`).
Skill: style.md:16-18 covers link wording for a single medium only.

### M14. Leave a regeneration note beside any output that can't be checked automatically
For output that depends on a browser, user input, or network, the source carries a `manual-regeneration` comment listing the exact steps to reproduce it. There are 21 files with these, for example `ch02-00-guessing-game-tutorial.md:300-304` and `ch21-01-single-threaded.md:176-181`.
Skill: absent. SKILL.md:62 says to run examples but not how to keep untestable output honest later.

### M15. Mark a term typographically where it is defined, and don't split a word between code and prose
The style guide asks for italics on a term at its defining use, and forbids mixing code and non-code in one word (``we `use`d``) (`style-guide.md`, "Prose"). The book applies the italics throughout, for example _associated function_ (`ch02-00-guessing-game-tutorial.md:162`) and _shadowing_ (line 686).
Skill: SKILL.md:76 says define on first use but not how to signal it. style.md:8 covers code formatting only.

## 2. Corrections

### C1. Deliberate errors are a main teaching method, not something to use once
The book makes reading compiler errors a stated learning goal (`ch00-00-introduction.md:177-185`). It shows a failing attempt and its literal error dozens of times (98 marked fences). It even drives a whole implementation from successive errors ("compiler-driven development", `ch21-02-multithreaded.md:99-103`, then the error-by-error build-up at lines 171-304). It also teaches how to read a backtrace (`ch09-01-unrecoverable-errors-with-panic.md:103-163`).
Skill: tutorials.md:53, "Once in a longer tutorial… More than once is a detour." Too absolute when the tool's diagnostics are themselves something the reader must learn to use.

### C2. A long book can use several capstone projects with small examples in between, instead of one running project
The book separates "concept chapters" from "project chapters" (Chapters 2, 12, and 21; `ch00-00-introduction.md:104-108`). Each project consolidates the chapters before it: "This chapter is a recap of the many skills you’ve learned so far" (`ch12-00-an-io-project.md:3-6`). Concept chapters use small, self-contained examples instead: rectangles in Chapter 5, coins in Chapter 6, a restaurant in Chapter 7, a blog post in Chapter 18.
Skill: books.md:16, "Carry one realistic project through the book. Each chapter adds to it and leaves it working." Oversimplified for a long book whose topics don't all fit one domain.

### C3. Concept-first chapters and reference chapters have a place in a learning book
Chapter 3 is an up-front survey of basics that most languages share (`ch03-00-common-programming-concepts.md:3-11`). Chapter 19 calls itself "a reference on all things related to patterns" (`ch19-00-patterns.md:25`). Chapter 20 says "You can use this chapter as a reference" (`ch20-00-advanced-features.md:3-9`). The introduction offers detail-first readers a route that skips the hands-on chapter and returns to it later (`ch00-00-introduction.md:114-120`).
Skill: books.md:10, "one major capability per chapter… not in an up-front theory chapter." Too absolute.

### C4. A broad, shallow preview tutorial can come before systematic teaching
Chapter 2 deliberately touches `let`, `match`, methods, associated functions, external crates, `Result`, shadowing and loops in one project, "at a high level", promising detail later (`ch02-00-guessing-game-tutorial.md:3-8`; `ch00-00-introduction.md:112-115`). It admits that one line "contains a lot of information" (`ch02-00…:84`).
Skill: tutorials.md:48 ("At most one new concept per step") and learning-science.md:13. Too absolute for a whole-task preview whose job is orientation, not mastery.

### C5. Comparing two or more working solutions teaches judgment; "one path" applies only to a first success
- `ch18-03-oo-design-patterns.md` builds the state pattern twice and weighs the trade-offs (lines 43-52, 400-403, 520-527).
- `ch17-03-more-futures.md:121-157` contrasts `sleep` with `yield_now`.
- `ch13-03-improving-our-io-project.md:176-191` compares a loop with an iterator.
- `ch07-04-bringing-paths-into-scope-with-the-use-keyword.md:126-129` presents two idiomatic options as equals.

Skill: tutorials.md:46 ("One path") and tutorials.md:71 (option detours are a failure). SKILL.md:102 ("Don't present every option as equal"). Too absolute once the goal is design judgment rather than a first win.

### C6. Once boilerplate is established, omitting it and saying so beats repeating it
"we won’t include all the `fn main() {` code in the examples, so if you’re following along, make sure to put the following examples inside a `main` function manually" (`ch04-01-what-is-ownership.md:98-102`). The same move happens for the async wrapper (`ch17-02-concurrency-with-async.md:42-44`). The tested files keep the full program; the page shows the relevant slice (the `:here` anchors throughout, for example `ch04-01…:120`).
Skill: SKILL.md:86, "Complete enough to run: include imports, setup…" Too absolute for long-form material where the scaffolding is repeated hundreds of times.

### C7. A transcript with a prompt marker, explained once, can beat separate command and output blocks
The book shows commands and their output in one block, distinguished by a `$` prompt (`>` for PowerShell). It explains the convention once (`ch01-01-installation.md:17-24`) and uses it throughout (for example `ch01-03-hello-cargo.md:150-155`). In print this keeps cause and effect together.
Skill: SKILL.md:92, "Keep commands and their output in separate blocks…" Correct for copy-heavy web docs, too absolute for print-first narrative. The trade-off is that copying from the web version picks up the prompt.

### C8. A collaborative "we" voice suits long-form narrative instruction
The book narrates as author and reader working together: 203 occurrences of "Let’s" and 327 of "we’ll" across `src/`. For example, "Let’s jump into Rust by working through a hands-on project together!" (`ch02-00-guessing-game-tutorial.md:3`).
Skill: SKILL.md:70, "Use second person, present tense". Too absolute: the imperative suits steps, while shared narration suits a book read in order. learning-science.md:47's personalization principle supports either voice.

### C9. One page can serve two audiences when the extra depth is fenced off as a skippable sidebar
The book puts material that only some readers need into titled blockquote sidebars:
- "The Stack and the Heap" (`ch04-01-what-is-ownership.md:22-85`).
- "Where’s the `->` Operator?" for C/C++ readers (`ch05-03-method-syntax.md:95-139`).
- "Integer Overflow" (`ch03-02-data-types.md:96-126`).
- "Ownership of Struct Data" (`ch05-01-defining-structs.md:226-302`).

Skill: SKILL.md:25 ("Don't serve both on one page; write two and link them"), learning-science.md:10 ("Cut… irrelevant asides"), and SKILL.md:79 (callouts only for warnings). Too absolute. Clearly separated optional depth keeps the main line clean without forcing a second page.

## 3. House conventions

- The Ferris icons and the mdBook code-fence flags (`does_not_compile`, `ignore`, `noplayground`) are tooling. The principle behind them is M1. (`ch00-00-introduction.md:187-191`)
- Title Case headings (`style-guide.md`), against SKILL.md:75's sentence case. The skill already defers to a house style guide (SKILL.md:27).
- `{{#rustdoc_include …:anchor}}` listing inclusion and the `<Listing>` component are mdBook mechanics (for example `ch02-00-guessing-game-tutorial.md:76-82`).
- Revisions track language editions and the release trains, with error-only fixes in between to stay in line with the print edition (`CONTRIBUTING.md`, "Checking for Fixes" and "Expectations").
- The community nickname "Rustaceans" (`ch01-01-installation.md:110-111`).

## 4. Where the Rust book falls short

- **Chapter openers list topics, not capabilities.** "In this chapter, we’ll discuss:" (`ch01-00-getting-started.md:4`). "More specifically, we’ll cover:" (`ch13-00-functional-features.md:13`). "Here are the topics we’ll cover" (`ch16-00-concurrency.md:42`). Skill: books.md:27 and learning-science.md:57-59 (checkable objectives).
- **Practice is sparse, never spaced, and has no solutions.** Formal exercise lists appear only at `ch03-05-control-flow.md:383-391` and `ch08-03-hash-maps.md:229-242`. Elsewhere there are scattered "try this" suggestions (`ch12-05…:197`, `ch14-03…:385`, `ch18-03…:367`). No answers exist anywhere: a grep for "solution" finds no exercise answers. Skill: books.md:45-55.
- **Some summaries just restate the chapter.** "We covered a lot in this chapter!" (`ch10-03-lifetime-syntax.md:623-630`) and `ch15-06-reference-cycles.md:303-314` list topics rather than skills. Skill: SKILL.md:101, books.md:35.
- **Hand-pasted output has drifted from the code or the current tools.**
  - The `rustfix` example declares `let mut x = 42;` but its warning shows `let mut x = 0;` (`appendix-04-useful-development-tools.md:38` vs `:52`).
  - Some output uses an older Cargo format ("Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs", `ch01-03-hello-cargo.md:126`) next to the current "Finished `dev` profile" (`ch02-00…:309`).

  Skill: SKILL.md:62, SKILL.md:111.
- **References point at content that has changed or never appeared.**
  - Appendix C cites `gen_range` (`appendix-03-derivable-traits.md:96`), but Chapter 2 now uses `random_range` (`ch02-00…:536`).
  - `ch17-06-futures-tasks-threads.md:19-20` says `spawn_task` was used "in the streams section", but `ch17-04-streams.md` never uses it.
  - `ch17-06…:45` names `spawn_blocking`, which the book never introduces.
  - `ch20-05-macros.md:113` cites the wrong listing number.

  Skill: SKILL.md:52, SKILL.md:114.
- **One example doesn't work as written.** `ch17-05-traits-for-async.md:88-99` matches `Ready(value)` and then uses an undefined `page_title`. It is marked `ignore`, but the reader is meant to follow it. Skill: SKILL.md:62.
- **Statements are tied to the date of writing.** "At the time of this writing" (`appendix-05-editions.md:27`, `ch20-05-macros.md:258`) and "as of this writing" (`ch11-01-writing-tests.md:110`). Skill: books.md:73.
- **Some ease words.** "This function is very easy to write" (`ch06-02-match.md:128`), and "updating… is easy" (`ch01-01-installation.md:115-116`). Skill: SKILL.md:73.
- **`foo` placeholders** in a few teaching examples: `String::from("foo")` (`listings/ch08-common-collections/listing-08-15/src/main.rs:3`) and `r#match("foo", "foobar")` (`appendix-01-keywords.md:122`). Skill: SKILL.md:91.

## Confirmations (one line each, only for unusual skill claims)

- books.md:17 (pull listings from tested code rather than pasting): every chapter includes listings from compiled projects, with anchors (`{{#rustdoc_include …:here}}`, for example `ch04-01…:120`).
- explanation.md:14 (state the wrong model, then correct it): "you might say 12. In fact, Rust’s answer is 24" (`ch08-02-strings.md:275-277`).
- books.md:60 (spiral back with more depth): minigrep is refactored with iterators in `ch13-03-improving-our-io-project.md`, and the guessing game gains a validated `Guess` type in `ch09-03…:137-219`.
- books.md:65 (say who the book isn't for): "If you’re entirely new to programming, you would be better served by…" (`ch00-00-introduction.md:92-95`).
- tutorials.md:48 (say just enough to keep going): "For now, you only need to know two details about iterators" (`ch12-01-accepting-command-line-arguments.md:33-37`).

## Observed, not counted

The book does combine modes on one page. Concept chapters run a tutorial narrative (build, break, fix) and interleave three other kinds of content:
- **Explanation:** the null-reference history and Hoare quote (`ch06-01-defining-an-enum.md:206-232`), why strings can't be indexed (`ch08-02-strings.md:254-343`), and design rationale stated inline ("This is a deliberate decision in Rust’s design", `ch03-03-how-functions-work.md:70-74`).
- **Reference blocks:** the "Modules Cheat Sheet" placed at the top of a teaching section "as a reminder" (`ch07-02-defining-modules-to-control-scope-and-privacy.md:12-51`), lookup tables (`ch03-02-data-types.md:44-89`), and rule recaps ("The Rules of References", `ch04-02-references-and-borrowing.md:255-261`).
- **How-to fragments:** the step-by-step publishing workflow (`ch14-02-publishing-to-crates-io.md:269-421`).

Pure reference is kept in the appendices and the self-declared reference chapters (Chapters 19 and 20).

This differs from SKILL.md:44 ("When a page wants to do two jobs, split it and link the halves"). I would count it as a correction: for material read in order by learners, short rationale and quick-reference recaps woven into the narrative support the learning, while separate pure-reference sections still serve lookup.

## Abstracted

**From missed principles**
1. Warn the reader, before they run it, that a code sample is meant to fail or misbehave, and mark such samples consistently so they're recognizable at a glance.
2. When you rename a heading, keep its old anchor so existing links still land.
3. Number code samples and figures, refer to them by number, and when you return to one after a long gap, show it again instead of sending the reader back. Check numbered cross-references whenever samples are added or removed.
4. Next to any sample output, say which parts will differ on the reader's machine or between runs, such as versions, timings, ordering, or paths.
5. Before introducing a feature, have the reader write working code without it, so the problem the feature solves is felt rather than asserted.
6. Name the places where learners usually get stuck, before they reach them, and say that difficulty there is normal and expected.
7. Connect new concepts to their nearest equivalents in tools the audience already knows, and say exactly where the comparison stops holding.
8. When a teaching example takes a shortcut, such as skipping error handling, using a simplified algorithm, or ignoring edge cases, say so and describe what production code would do instead.
9. At the point where a concept is shown, invite the reader to change the example and predict what will happen before checking it with the real tool.
10. Before implementing something, show the code that will call it, so the reader knows what the implementation must satisfy.
11. When examples depend on a fast-changing external ecosystem, consider a small companion package that wraps exactly what the material needs, to keep examples stable and the focus on concepts. Publish its source.
12. Offer one setup step that fetches everything the whole course or book will need, so readers can work offline afterward.
13. If the same source ships to print and web, write link text that still reads well when converted to plain text with a URL, mark links that only make sense online, and keep internal links relative.
14. For any output that can't be regenerated automatically, leave a note in the source explaining exactly how to reproduce it.
15. Mark each term typographically where it is defined, and never split a single word between code formatting and plain prose.

**From corrections**
16. When learners must learn to read a tool's diagnostics, show failing attempts and their exact messages often, and let those messages drive the next step. One deliberate error is too few.
17. A long book can alternate concept chapters that use small, self-contained examples with project chapters that consolidate everything before them. One project need not run through the whole book.
18. A learning book may include an up-front survey of familiar basics and late chapters meant for reference. Offer an alternative reading order for readers who prefer detail before practice.
19. An early, broad tutorial that touches many concepts lightly can orient readers before systematic teaching, as long as it says detail comes later.
20. Keep a single path for a reader's first success. When the goal is design judgment, build two or more working solutions and compare their trade-offs openly.
21. After repeated scaffolding is established, show only the relevant part of each example and say once what the reader must add. Keep the full, tested version available.
22. In print-first narrative material, showing a command and its output together with a prompt marker, explained once, can be clearer than splitting them. Accept that copying from the web version becomes harder.
23. In narrative instruction read in order, a collaborative "we" voice works. Use imperatives for discrete steps.
24. One page can serve readers with different backgrounds if material only some of them need is set apart in clearly titled sidebars they can skip.
25. In material read in sequence, it is fine to weave short rationale and quick-reference recaps into a narrative. Keep separate pure-reference sections for lookup.
