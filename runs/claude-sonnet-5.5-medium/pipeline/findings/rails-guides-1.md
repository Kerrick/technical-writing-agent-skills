Source: Rails guides, Start Here through Other Components, commit f12b615

> Quotes and descriptions in this file are from the [Ruby on Rails Guides](https://guides.rubyonrails.org/) ([rails/rails](https://github.com/rails/rails)), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). "Rails" and "Ruby on Rails" are trademarks of David Heinemeier Hansson. Quotes are short, and used to compare and criticize. Because it quotes and describes that material, this file is licensed under the same license.

# Differences between the baseline skill and the Rails guides

Skill files (unchanged baseline): `developer-docs/SKILL.md` (S), `references/teaching.md` (T), `references/reference-and-guides.md` (R), `references/books-and-video.md` (B), all under `scratchpad/sonnet-run/work/`.
Guide files are cited by name and line, under `sources/rails/guides/source/`. Style guides: `ruby_on_rails_guides_guidelines.md` (G), `api_documentation_guidelines.md` (A).

## 1. Missed principles

**1.1 Every page opens by saying what the reader will know afterwards.**
- Evidence: all 22 pages read open with an "After reading this guide, you will know" list (grep: 22 of 22 files). G:29-32 requires a prologue saying what the guide is about and what the reader will learn. The list is used on reference-like pages (active_support_core_extensions.md:11-16), not only on the tutorial.
- Skill: S:35 asks only for what the page is for and who it's for. The outcome rule (T:7) is scoped to tutorials. No outcome list for other page types: absent.

**1.2 Asides are graded by consequence, with each label meaning one thing.**
- Evidence: G:198-230 defines three levels: needed to understand the subject (NOTE), optional extra or pointer (TIP), things that break or compromise the app (WARNING). The pattern is heavy and consistent: 155 callout lines across just 8 of the pages (layouts_and_rendering 14, active_storage_overview 24, association_basics 27, active_record_querying 28, getting_started 16, active_record_callbacks 15, active_record_validations 20, active_job_basics 11).
- Skill: S:44 covers only warnings before hazards. Grading other asides by importance: absent.

**1.3 Next to a call that is shorthand, show what it produces or expands into.**
- Evidence: active_record_querying.md repeats "The SQL equivalent of the above is:" after nearly every finder (e.g. :223, :244, :270); the grep for this pattern found 31 hits in that file. form_helpers.md shows the generated markup after each helper (:64, :115, :157). routing.md:138-146 puts the generated routes in a table directly under the one-line declaration.
- Skill: S:37 ("Show, then name") wants a minimal working example; S:43 wants output in a separate block. Pairing each convenience call with its lower-level result: absent.

**1.4 The docs model the current preferred approach; superseded approaches are demoted, labeled, and sent last.**
- Evidence: A:82 says docs should communicate the current way and reorder sections to favor it. In practice: active_record_validations.md:367-374 names the older form and says the newer one is recommended; form_helpers.md:1338-1341 puts the two superseded helpers in the last section, one paragraph, "discouraged"; active_record_querying.md:2672 and :2763 say to prefer the higher-level method; action_controller_overview.md:969 calls one technique the recommended one.
- Skill: S:35 says common case first; R:39 covers deprecations (date, replacement) only. Ordering and example choice as a way to teach the preferred approach: absent.

**1.5 For each guarantee, say where it does not hold and what complements it.**
- Evidence: active_record_validations.md:158-186 lists every operation that skips validation; :131-143 lists the ones that trigger it; :886 warns that the check creates no database-level constraint and says what to add. active_record_callbacks.md:609-653 lists what triggers callbacks and :745-770 what skips them, with a warning at :798. active_record_migrations.md:1649-1677 (referential integrity) explains the model-level check cannot be the only layer.
- Skill: R:14 names "side effects and guarantees" generally. Enumerating bypass paths and the complementary mechanism: absent.

**1.6 Where two features overlap, give a decision section with criteria.**
- Evidence: association_basics.md:1441 "Choosing an Association" (two sub-sections, each with when-to-use bullet lists, :1537-1566); action_view_helpers.md:897-906 NOTE on how two helpers differ; active_record_querying.md:1008-1016 "The key difference between ..." for two similar finders.
- Skill: R:17 only says to link easily-confused siblings. A "when to choose which" section: absent.

**1.7 The opening says what the thing is not, and names the neighbor it gets confused with.**
- Evidence: active_record_basics.md:28-32 (NOTE: difference from the neighboring layer); action_mailer_basics.md:21-23 and action_mailbox_basics.md:21-23 (each says the other handles the opposite direction); active_model_basics.md:34-37.
- Skill: R:59 does this only for explanation pages ("Name the scope"). Not in S's page-opening advice (S:35): absent.

**1.8 Links inside a versioned doc set follow the version the reader is on; pin only where the sentence is about a specific release.**
- Evidence: A:33-39 prefers links relative to the current docs because absolute ones "take the reader outside their current documentation version"; G:262-300 describes rewriting unpinned links to the doc set being built, and pinning only in release notes.
- Skill: S:68 asks for a "stable, versioned URL"; R:87 asks for a version selector. Neither says cross-links should follow the reader's version: absent.

**1.9 Mark advanced or optional sections as such, inside the page.**
- Evidence: action_view_overview.md:566-568 says the next two sections are more advanced "included here for completeness"; association_basics.md:1568 has an "Advanced Associations" heading that separates the rarer material from the main set.
- Skill: T:47-50 handles audience levels by heading clarity only; marking depth within a page: absent.

**1.10 Every code listing that belongs in a file names the file on its first line.**
- Evidence: G:84-108 requires it. getting_started.md repeats it for every block that is file content (e.g. :293, :382, :920, :1055, :1172); it lets the learner place each snippet without prose.
- Skill: B:26 asks for it in books only. S:43 and T:41 are silent about it for tutorials and guides: absent.

## 2. Corrections

**2.1 R:24 "Neutral voice. No opinions, no 'you should'" is too absolute for reference-style material.**
- Evidence: in layouts_and_rendering.md, a page that catalogs every render option, the odd options carry usage verdicts in place: :301 "There's rarely a good reason to do this in practice"; :353 a warning that a practical use is unlikely; :482 "seldom any good reason". active_record_callbacks.md:155 puts "Refrain from using ..." next to the registration reference. action_controller_overview.md:1196 states large session data "is discouraged".
- Skill line: R:24.

**2.2 S:43 "no `$` prompts inside copyable blocks ... output shown in a separate block" is stronger than the purpose requires.**
- Evidence: getting_started.md:86-89 shows a prompt line and its output in one fenced block; G:112-121 and G:97 state prompts and filename comments are skipped by the page's copy button, so the block stays copy-safe while showing input and output together.
- Skill line: S:43. The goal (a copy that works) holds; the mechanism depends on whether the page tooling excludes prompts and output.

**2.3 S:46 "Use one running domain across a doc set" is oversimplified.**
- Evidence: each guide declares its own example domain and uses it on that page: active_record_querying.md:53-56 ("Code examples throughout this guide will refer to one or more of the following models"), people in validations, products in the tutorial (getting_started.md:66). Within one page the domain even changes when the concept needs another shape: association_basics.md:424 (Supplier/Account), :962 (Physician/Patient), :1175 (Assembly/Part), :1697 (Employee).
- Skill line: S:46. Consistency within one tutorial thread holds up (getting_started.md keeps one shop throughout); across separate pages it was not applied.

**2.4 S:40 "Be specific ... defaults, limits ... beat adjectives" omits that some exact values should deliberately not be promised.**
- Evidence: A:274-284 says to document the semantics of flags and predicates, not exact singleton values, because it keeps refactors open; A:315-316 "careful not to commit to any particular value". A:456-467 does the same for internal methods.
- Skill line: S:40 (and R:35 on exact wire types). Not a contradiction of being precise about the contract; it is a missing limit on what to pin down.

## 3. House conventions (not carried over)

- Callout keywords, line-highlight syntax, copy-button behavior: G:182-196, G:147-167.
- Title-case headings: G:50-57.
- Ruby/RDoc markup, `# =>` result notation, fixed-width via plus signs vs `<tt>`: A:206-215, A:350-352.
- Spelling and style: American English, Oxford comma, "an SQL": A:134-177.
- Component names written with a space; "application" not "service": A:98-116.
- API comments avoid "you" (A:148-158) while the guides address the reader as "you" throughout; this is a split between two audiences, so S:42 is unaffected.
- Internal methods hidden from published API docs with a directive: A:441-467.
- 80-column wrap only for new text: G:304-305.

## 4. Where the Rails guides fall short of the skill

**4.1 Hard-coded versions drift between pages.**
- Evidence: install_ruby_on_rails.md:109 shows "Rails 8.1.0" and :91 "ruby 4.0.6", while getting_started.md:75-76 requires Ruby 3.4 and Rails 8.2.0 and :196 prints a server banner from "ruby 3.3.5-p100". "Rails 8.2.0" appears at :88, :91, :193, :360.
- Skill: S:70 and S:64-65 (check versions, no hard-coded versions in prose).

**4.2 Small errors that running or re-reading the text would catch.**
- Evidence: action_controller_overview.md:1066 and :1073 use a misspelled receiver in the cookie examples; layouts_and_rendering.md:192-193 names status "303 Unprocessable Content" while the code uses the 422 symbol; form_helpers.md:677 names one helper in prose while the example uses another (`time_zone_select`); action_view_helpers.md:452 calls the link-stripping helper in the example for the tag-stripping helper; association_basics.md:1494 passes `supplier_id` where the association name is meant.
- Skill: S:64-65.

**4.3 The same instructions are pasted several times.**
- Evidence: action_mailbox_basics.md:84-100, :180-196, :254-270 repeat the same relay-password setup for three mail servers; association_basics.md:710-765 and :1241-1299 repeat a nearly identical list of generated methods.
- Skill: R:23 (state shared steps once and link).

**4.4 The tutorial gives expected results but almost no recovery paths.**
- Evidence: getting_started.md has nine "you'll/you should see" statements (e.g. :83, :256, :404, :3148) but no "if you see X instead"; the only recovery hint is :341 about rolling back a migration (grep for "if you see", "didn't work", "troubleshoot": none).
- Skill: T:18.

**4.5 Real mail-provider addresses in examples.**
- Evidence: action_view_helpers.md:338, action_mailer_basics.md:258 and :326, active_model_basics.md:1393 use gmail.com addresses, though other pages use reserved example domains (getting_started.md:1629).
- Skill: S:52.

**4.6 Reader-facing "easy" claims and future tense.**
- Evidence: getting_started.md:171 "Let's start easy", :1878 "makes it easy to upload files", :1943 "Rails makes it easy to translate". A:58-68 requires present tense, yet the guides regularly write "This will generate the following SQL" (active_record_querying.md:623, form_helpers.md:64).
- Skill: S:41, S:42.

## Confirmations (one line each)

- S:38 one term per concept: A:98-116 fixes proper names and says "application", not "service".
- S:50 keep docs next to source: A:18 and A:416-433 generate API docs from comments in source, with the generated code shown beside dynamic definitions.
- S:58 explain the why: layouts_and_rendering.md:192-197 gives the reason for the status code rather than a bare rule.
- S:45 descriptive links: G:234-255 extends the same rule to in-page links.
- T:15 early win: getting_started.md:206-214 gets a working page in the first minutes and calls it a smoke test.

## Observed, not counted

Several pages combine explanation, how-to and reference:
- active_record_validations.md mixes why-use-it explanation (:42-77), a catalog of every validator with option tables (:396-780), and a how-to for showing errors in views (:1904-1956), all under headings that say which is which.
- getting_started.md is a tutorial with explanation embedded in the steps: a philosophy section (:34-61), a strong-parameters explanation inside the create step (:1295-1304), a design discussion on concerns (:2450-2511), then pointers to the fuller guide (e.g. :1872).
- action_controller_overview.md and layouts_and_rendering.md mix reference tables with decision advice (see 2.1).

Where the docs keep them apart: install steps are a separate page from the tutorial (install_ruby_on_rails.md); exhaustive method reference lives in a separate generated API reference that nearly every method name links to; configuration, testing and security each have their own guides that these pages point to (e.g. action_mailer_basics.md:1015, form_helpers.md:43); a follow-on tutorial is a separate page (getting_started.md:3211).
Skill rules it differs from: S:13 ("Choose one mode per page ... Mixing modes is the most common structural failure"), S:31, S:69; for tutorials also T:23.
Not counted as a correction: this is one document set, the mixing is bounded by headings and callouts that tell the reader which kind of text they are in, and heavy reference and cross-cutting topics are moved to other pages. I have no evidence on reader outcomes, so I cannot say the mixing helps or hurts; the evidence supports only that sections can change kind under clear labels.

## Abstracted

Missed principles
1. Begin every page, whatever its type, with a short statement of what the reader will know or be able to do after reading it.
2. Use a small fixed set of labels for asides and give each one a single, stable meaning based on consequence: needed to understand, optional extra, and harmful if ignored.
3. When a call is shorthand for something lower-level, show next to it what it produces or expands into, so the reader can check their mental model.
4. Let your examples and ordering teach the currently preferred approach. Put superseded approaches later, label them as such, and name what replaces them.
5. For any guarantee a feature gives, list the operations that trigger it, the ones that silently skip it, and any mechanism outside the feature that has to complement it.
6. Where two features overlap, include a section on choosing between them that states the criteria; at minimum state the one difference that matters.
7. In the opening of a page, say what the subject is not and name the nearest neighbor it is likely to be confused with.
8. In a documentation set that has several versions, make cross-links land on the same version the reader is currently reading; pin to a specific version only when the sentence is about that release.
9. Mark advanced or optional sections as such, inside the page, so readers who don't need them know they can skip them.
10. Start every code listing that represents a file with the file's path, so the reader never has to guess where it goes.

Corrections
11. A reference page may carry a short verdict next to an option that is rarely appropriate, and should when readers would otherwise pick it by default; keep the verdict brief and put the reasoning in a linked page.
12. The rule is that whatever the reader copies must work. If your publishing tool strips prompts and output from copy, you may show input and output together; if you can't rely on that, keep them in separate blocks.
13. Keep one example domain within a single page or worked sequence, and announce it at the top; across separate pages, or when a concept needs a different shape of data, choose the domain that shows the concept best.
14. Be exact about the contract and deliberate about what you leave unpromised: don't state incidental exact values that you want the freedom to change; say what behavior callers may rely on.
