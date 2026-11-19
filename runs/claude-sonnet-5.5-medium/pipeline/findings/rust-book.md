Source: The Rust Programming Language, commit 9be0936

> Quotes and descriptions in this file are from [The Rust Programming Language](https://doc.rust-lang.org/book/) ([rust-lang/book](https://github.com/rust-lang/book)), copyright (c) 2010 The Rust Project Developers, licensed under the [MIT License](https://github.com/rust-lang/book/blob/main/LICENSE-MIT) or the [Apache License 2.0](https://github.com/rust-lang/book/blob/main/LICENSE-APACHE). Quotes are short, and used to compare and criticize.

Baseline compared: `developer-docs/SKILL.md` (S), `references/teaching.md` (T), `references/books-and-video.md` (B), `references/reference-and-guides.md` (R), all unchanged. File paths below are relative to the book's `src/` unless noted. Counts come from grep over `src/`.

Intent documents read first: `style-guide.md` (prose, code and link conventions, including how links must read in print) and `CONTRIBUTING.md` (print edition is a snapshot; large revisions only alongside language editions; between them only error fixes; docs ride the same release trains as the software).

---

## 1. Missed principle

**1.1 Failure is a deliberate, labelled teaching step, not a one-off.**
- Evidence: `ch00-00-introduction.md` tells the reader up front: "we'll provide many examples that don't compile along with the error message", and gives a legend of three marker icons: does not compile, panics, compiles but does not do what is wanted. 84 blocks are tagged `does_not_compile` across 51 chapter files. Example arc: `ch04-02` shows the modification attempt (Listing 4-6), the diagnostic, then the fix. Same arc in `ch10-03`, `ch15-04`, `ch16-03`.
- The captured output is real: `listings/ch04-understanding-ownership/listing-04-06/output.txt` is genuine compiler output (`error[E0596]…`) in a complete buildable project beside the source.
- Captions say the state: `ch10-01` Listing 10-5 caption ends "this doesn't compile yet".
- Skill: T:31 limits deliberate errors to "once"; T:43 and S:26 stress pasted code being the correct version and a guaranteed first success. Nothing says to label non-working code in advance or to distinguish kinds of failure.

**1.2 Show the target before building toward it.**
- Evidence: `ch05-03` Listing 5-14 "Using the as-yet-unwritten `can_hold` method"; `ch12-04` Listing 12-15 failing test first; `ch18-03` Listing 18-11 desired behaviour, "won't compile yet because we haven't implemented the `blog` crate"; `ch21-02` Listing 21-12 "Our ideal `ThreadPool` interface", plus the text "writing the client interface first can help guide your design".
- Skill: T:14 opening shows what the whole tutorial builds (a final output). Step-level target-first is absent.

**1.3 A reader-facing guide to a long work: audience and non-audience, reading paths, map, legend.**
- Evidence: `ch00-00-introduction.md` "Who This Book Is For" ("If you're entirely new to programming, you would be better served by a book that specifically provides an introduction"); "How to Use This Book" offers an alternate order ("skip Chapter 2 and go straight to Chapter 3 … then return"); describes each part in a paragraph; says concept chapters and project chapters differ and names which are which; ends "There is no wrong way to read this book".
- Skill: B:10 asks the author to write the profile down as planning; S:12 says assumptions go in the reply "not in the doc". Neither says to publish who it's not for with a redirect, or paths.

**1.4 Alternate concept chapters with integrating project chapters.**
- Evidence: `ch00-00-introduction.md` "Chapter 2, Chapter 12, and Chapter 21 are project chapters; the rest are concept chapters". `ch12-00-an-io-project.md` lists the earlier chapters the project combines (organising code, collections, error handling, traits and lifetimes, tests). Concept chapters use small, throwaway, separately named projects per section (`ch03-01` "generate a new project called _variables_", then _functions_, _branches_, _loops_).
- Skill: T:10 and B:11 prescribe one spine project that grows by accretion. The rhythm of disposable concept examples broken by named integration projects is absent.

**1.5 Teach how to read diagnostics, including distrusting them.**
- Evidence: `ch16-03` "Wow, that error message is very wordy! Here's the important part to focus on"; `ch12-04` "the help text suggests specifying the same lifetime parameter for all the parameters and the output type, which is incorrect!"; `ch15-05` "We also can't take the suggestion from the error text to use `&mut self`"; `ch05-02` includes only chosen lines of captured output (`output.txt:3`, `output.txt:9:10`) to isolate the key lines; `ch09-01` "start from the top and read until you see files you wrote".
- Skill: T:31 says only "teach how to read an error message".

**1.6 Reference entries state caller contracts.**
- Evidence: `ch14-02` "Commonly Used Sections": Panics (when the call terminates instead of returning an error), Errors, Safety (invariants the caller must uphold). `ch09-03` "Contracts for a function, especially when a violation will cause a panic, should be explained in the API documentation". `ch20-01` convention of a SAFETY note at each risky operation and each risky function.
- Skill: R:13–14 list errors and side effects. Preconditions, contract violations that crash rather than return an error, and caller-held invariants are absent.

**1.7 Where something can't be generated, leave the regeneration recipe or sibling list at the spot.**
- Evidence: 43 `manual-regeneration` comments across 21 files give the exact steps to refresh pasted output (e.g. `ch03-05`, run then interrupt). A pinned dependency version carries a comment naming every other file that must change with it (`ch01-01-installation.md:161`, repeated in `ch02`, `ch07-04`, `ch14-03`). `ADMIN_TASKS.md`: "Grep for `manual-regeneration` and follow the instructions".
- Skill: S:50 says generate; S:57 says grep. A recipe or sibling list at the point of duplication is absent.

**1.8 Mark a term where it is defined; don't glue prose onto code font.**
- Evidence: `style-guide.md` "Prefer italics over single quotes when calling out a term" and "Prefer not mixing code and not-code in one word". In prose: "an _associated function_ is a function that's implemented on a type" (`ch02`).
- Skill: S:38 says define at first use; it doesn't say to mark it. B:35 style sheet is generic.

**1.9 Number only listings the prose points back to; make captions state what the listing shows.**
- Evidence: numbered listings are the ones later text names ("fix the code from Listing 4-6"); the others are unnumbered with only a file name (`ch04-02`'s `calculate_length` example). Listing directories split the same way: `ch20-advanced-features` has 39 numbered and 17 unnumbered, `ch04` has 9 and 20.
- Skill: B:26 "Consistent listing numbering lets the prose refer to them" reads as number everything.

**1.10 Keep legacy anchors when a heading is renamed.**
- Evidence: 161 comments across 63 files read "Old headings. Do not remove or links may break", each followed by the old anchor id.
- Skill: R:87 covers page URLs and redirects only.

**1.11 Publish the revision policy.**
- Evidence: `CONTRIBUTING.md` "Expectations": large revisions are timed to language editions; between them "we will only be correcting errors"; non-error requests may wait "months or years"; "Checking for Fixes": a fix may already be on the main branch without yet being in the stable edition.
- Skill: B:37 errata/changelog and R:88 owner/CI. A statement to contributors of cadence, accepted change types and turnaround is absent.

---

## 2. Correction

**2.1 "Check no chapter uses a concept before its introduction" (B:12) is too absolute.**
- Evidence: `ch02` uses `Result`, `match`, `&mut`, associated functions before explanation ("(Chapter 4 will explain references more thoroughly.)"). `ch06-01` "The `<T>` syntax is … a feature we haven't talked about yet … all you need to know is". `ch04-03` "We'll discuss iterators in more detail in Chapter 13. For now, know that…". `ch09-02` "For now, you can read `Box<dyn Error>` to mean 'any kind of error.'" "For now/for now" appears 34 times in 24 files.
- What the book enforces instead: every forward use states how much the reader needs now and where the full treatment is. T:9 allows a one-line black box; the chapter-level rule B:12 contradicts it.

**2.2 "Don't teach by apology… If something is tricky, give the tool" (T:32) is too absolute.**
- Evidence: `ch04-01` "it does take some time to get used to … Keep at it!"; `ch08-02` "New Rustaceans commonly get stuck on strings for a combination of three reasons" (names them); `ch03-01` "Compiler errors can be frustrating, but … they do _not_ mean that you're not a good programmer! Experienced Rustaceans still get compiler errors"; `ch04-02` explains why newcomers struggle with the mutation rule and what it buys.
- The book names the difficulty with a cause and a benefit, then gives the tool. The vague version ("It's a bit tricky at first", `ch06-02`; "Whew!" in `ch02`, `ch04-02`, `ch12-03`, `ch20-05`) is what T:32 rightly targets.

**2.3 "Do not teach prerequisites inline. Link" (T:8) is too absolute.**
- Evidence: `ch04-01` titled sidebar "The Stack and the Heap" ("so here is a brief explanation in preparation"). `ch17-00` "Parallelism and Concurrency" section before the chapter proper. `ch21-01` brief overview of the two network protocols ("will give you the information you need"), with the rest declared out of scope. `ch01-01` sidebar "Command Line Notation". 14 titled sidebars in total.
- These are background the topic's own explanation depends on that the target reader may lack. They're taught in minimum form in a bounded, titled aside with the remainder explicitly out of scope. The book's intro still assumes prior programming knowledge and links out for that.

**2.4 "Remove … alternative approaches… Choices belong in how-to guides" (T:23) is too absolute for learning text.**
- Evidence: `ch07-03` "Our preference in general is to specify absolute paths because…"; `ch08-02` "String::from and to_string do the same thing … a matter of style and readability"; `ch07-05` sidebar "Alternate File Paths" ("older style, still supported"); `ch09-02` sidebar "Alternatives to Using `match`…"; `ch10-02` three forms of the same constraint.
- The motive is that readers meet each form in others' code. The book states a preference and a reason, and keeps the alternatives in bounded asides.

**2.5 "Procedures are numbered" in every mode (S:36) is oversimplified.**
- Evidence: zero numbered-list lines across `ch01-01`, `ch01-02`, `ch01-03`, `ch02`. Those narrative tutorials carry order through headings, one listing per change, and the expected output after each run. Numbered lists appear for plans and rules (`ch10-00` steps, `ch12-04` four-step cycle, `ch21-00` five-step plan, `ch04-01` rules).

**2.6 "Cross-references use generated links, not manual chapter numbers" (B:36) is insufficient when a printed edition exists.**
- Evidence: `style-guide.md` links section: intra-book links must be marked "to be ignored" in print (229 `ignore -->` markers), and link text must "read well" once rewritten as `text at url`. Prose names the chapter and section title around each link ("see the 'Troubleshooting' part of the Installation section", `ch01-02`). Print readers cannot click, so the number and title are the reference.
- The book's own hand-numbered references drift (see 4.3), which supports generating the numbers while still printing them in the prose.

**2.7 (Lower confidence) Analogy rule: "only if you also say where it breaks" (R:57).**
- Evidence: unflagged everyday analogies, each followed at once by the literal mechanism: coin-sorting machine (`ch06-02`), restaurant seating (`ch04-01`), TV in a family room (`ch15-04`), shared microphone (`ch16-03`), river and rubber duck (`ch16-02`), kitchen workers (`ch21-02`).
- Shown: short entry-ramp analogies work when pinned to the exact rule straight after. The cross-language mapping version in T:48 is supported (see section 5). No evidence in the repo on whether unflagged limits caused misconceptions.

---

## 3. House convention (don't generalise)

- Title-case headings, italics for terms and file names, no parentheses after method names in prose, hard wrap at 80 columns (`style-guide.md`).
- The three-icon legend, `{{#rustdoc_include}}`-style snippet anchors, hidden scaffold lines, and `<!-- ignore -->` print markers are mdBook mechanics; the principles behind them are in 1.1, 1.9, 2.6.
- Console transcripts that mix `$` input lines with output in one block, with the notation declared once (`ch01-01`). Works because the audience retypes commands; S:43/T:43 stay the safer default for copy-paste.
- Doc-comment section names (Panics, Errors, Safety), SAFETY comments, `edition = "2024"` and the toolchain-pinning file (`rust-toolchain`: 1.99).
- Per-shell command variants (cmd vs PowerShell) and an "offline" section pre-fetching dependencies (`ch01-01`).
- Docs shipped on the same stable/beta/nightly channels as the software (`CONTRIBUTING.md`).

---

## 4. Where the Rust book falls short of the skill

**4.1 Exercises lack checkable outcomes, solutions, difficulty (T:33).**
- Evidence: `ch03-05` Summary: three one-line programs to "try building"; `ch08-03` three exercises, no answers; grep finds no exercise solutions anywhere in `src/`. `title-page.md` points to a separate interactive edition for quizzes.

**4.2 Hand-pasted output has drifted from the code or the version (S:53, S:64).**
- `ch01-03` shows `Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs`; `ch02` and `ch14-01` show the current `` Finished `dev` profile `` form. `ch01-03` has no regeneration comment.
- `appendix-04-useful-development-tools.md`: code is `let mut x = 42;` (line 38); the pasted warning shows `let mut x = 0;` (line 52).
- `title-page.md` says Rust 1.99.1 and `rust-toolchain` says 1.99, but `ch02` Listing 2-2 output reads "latest Rust 1.96.0" (twice) and `ch09-01` Listing 9-2 shows toolchain 1.85. Those blocks carry `manual-regeneration` comments.

**4.3 Prose, code and cross-references disagree (S:67, S:68, T:41).**
- `ch20-05` says "the pattern pieces in Listing 20-29" for the macro definition; the macro is Listing 20-35 (`listings/ch20-advanced-features/listing-20-35` exists; `listing-20-29` is the `map` example in `ch20-04`).
- `appendix-03` names `gen_range`; `ch02` teaches `random_range` (lines 536, 539).
- `ch17-06` links `ch17-04-streams.html#composing-streams`, which has no such heading; its text recalls using `spawn_task` "in the streams section", but `spawn_task` appears only in `ch17-02` and `ch17-06`. `ch17-05` links `ch17-03-more-futures.html#working-with-any-number-of-futures`, which doesn't exist. `ch20-04` points readers to `ch17-03` for the pinning section, which lives in `ch17-05`.
- These look like leftovers of a revision of the async chapter. They also back B:36's advice to generate numbers and links.

**4.4 Reassurance words in the hardest section (S:41).**
- `ch17-05` line 339: "because they obviously don't have any internal references", inside the pinning discussion the same page calls "a lot to absorb". `ch09-02` line 404 "Of course, using …".

---

## Confirmed (one line each)

- B:45 show the wrong or naive version first: `ch05-02` (loose values, then tuple, then struct), `ch04-03` (index-returning function, then slice), `ch18-03` (traditional pattern, then state-as-types).
- B:46 foreshadow and recall: `ch13-03` "At the time, we said not to worry about the inefficient `clone` calls because we would remove them in the future. Well, that time is now!"
- T:27 spaced reuse of earlier examples: Rectangle (`ch05`, again in `ch11`), the guessing game (`ch02`, `ch09-03`, `ch11-01`), the cons list (`ch15-01`, `-04`, `-05`).
- B:25 code extracted from tested, complete projects: `listings/` has one project per example (`Cargo.toml`, `src/`, `output.txt`); `ADMIN_TASKS.md` regenerates outputs by script and publishes the complete projects as downloadable archives (also B:30).
- R:31 examples that run as tests: `ch14-02` "Running `cargo test` will run the code examples in your documentation as tests!"
- T:26 predict/experiment prompts sparingly: 17 "Try …" prompts in the whole book, plus a handful of explicit predict-first ones (`ch10-03`, `ch17-02`, `ch19-03`).
- T:48 map to what the reader knows and flag differences: `ch05-03` for readers of another systems language ("Rust doesn't have an equivalent to the `->` operator"), `ch04-01` RAII note.

---

## Observed, not counted

Pages that combine explanation, procedure and reference:
- `ch04-01-what-is-ownership.md` runs guided steps (listings), a memory-model explanation (a titled sidebar), and a reference-style "Ownership Rules" list in one page.
- `ch03-02-data-types.md` places lookup tables (Tables 3-1, 3-2) inside narrative.
- `ch11-02-running-tests.md` is a how-to for run options inside a concept chapter.
- `ch14-02-publishing-to-crates-io.md` mixes procedure (publish), explanation (public API design) and a reference checklist ("Commonly Used Sections").

Skill rule it differs from: S:13 ("Choose one mode per page… Mixing modes is the most common structural failure"), S:31 ("Link between modes instead of merging them"), S:69 (check that stray explanation/steps are moved or linked).

Where the book keeps modes apart instead:
- Pure reference lives in appendices (`appendix-01` keywords, `appendix-02` operators and symbols, `appendix-03` derivable traits).
- `ch19-00` says "This chapter is a reference on all things related to patterns" and `ch20-00` "use this chapter as a reference".
- Exhaustive reference is linked out, not rewritten: `ch01-03` ("For more information about Cargo, check out its documentation"), `ch14-01` ("For the full list of configuration options and defaults… see Cargo's documentation"), `ch03-01` (the language reference on constant evaluation).
- Explanation that interrupts the teaching line sits in titled sidebars or `> Note:` blocks (14 sidebars).

I would not count this as a correction. The mixing is bounded and signposted, and exhaustive reference is sent elsewhere, which is what S:31 asks for. The only nuance is that, in a teaching book, the unit the rule governs is the passage, not the page, and the repo has no reader data showing the mixing helps or hurts.

---

## Abstracted

**Missed principles**

1. Treat failure as a teaching step. When a lesson depends on something being rejected, crashing, or silently wrong, show that version on purpose. Tell the reader beforehand that it will not work, and distinguish "rejected before running", "fails while running", and "runs but gives the wrong result". Show the real diagnostic from a real run, then derive the fix from it. Don't limit this to one example per lesson.
2. In build-up sections, show the desired end usage, or a test that fails, before the implementation, so every step has a visible target to move toward.
3. Give long works a reader-facing guide: who it is for, who it is not for and where those readers should go instead, the reading paths for different temperaments (including skipping ahead and coming back), a one-paragraph map of the parts, and a legend for any markers the text uses.
4. Alternate concept sections, which use small disposable examples, with integration projects. Each project says which earlier parts it pulls together.
5. Teach diagnostics as a skill: point at the one line in a long message that matters, show only that line, and say when a tool's own suggested fix is wrong or incomplete and why.
6. For reference entries, document the caller's contract. State when a call terminates rather than returning an error, and list the invariants the caller must uphold, separately from recoverable errors.
7. For any content that cannot be generated, such as pasted output or a value repeated in several files, leave at that spot either the exact steps to regenerate it or the list of other places that must change with it.
8. Mark each term typographically at the point where it is defined, in one consistent style. Never attach ordinary-language endings to code-formatted text.
9. Number only the listings that later text refers back to. Write each caption to say what the listing demonstrates, including that it does not yet work.
10. When a heading is renamed, keep its old anchor in place with a note not to remove it.
11. Publish the revision policy: how often large revisions happen, which kinds of change are accepted between them, and how long a contributor should expect to wait. This matters most when a printed or otherwise frozen edition must stay aligned.

**Corrections**

1. Using a not-yet-taught idea is acceptable. Using it silently is not. Each forward use should say how much the reader needs to know now and where the full treatment comes.
2. Name difficulty honestly. Say that a topic usually takes time, give the specific reason, say that struggling is normal and not a verdict on the reader, and then give the tools. Avoid only the vague apology.
3. Background that the topic's own explanation depends on, that the target reader may lack and that is small, can be taught in place in a bounded, titled aside that says what is left out. Link out for skills the reader is already assumed to have.
4. In learning material, show the two or three alternative forms the reader will meet in other people's work. State which is preferred and why, and keep the alternatives in bounded asides.
5. Numbered steps suit plans and rules. In narrative tutorials, carry the sequence with one change per listing, and show the expected result after each run.
6. Where output may be printed or read offline, references must work without a link. Write the part and its title in the prose, mark links that print should drop, word link text so it still reads when shown as text plus address, and generate the numbers so they cannot drift.
7. Everyday analogies are acceptable as entry ramps when the exact rule follows immediately. The requirement is a precise statement straight after, not necessarily a listed limit (lower confidence).
