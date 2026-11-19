# Merged findings

Rule IDs: `A-M3` is Source A, Missed principle 3; `A-C1` is Source A, Correction 1. Source C and Source F use their plain numbers (C 15–18 are corrections). Source D's first file is `D1-n` (11–14 are corrections) and its second file is `D2-n` (corrections `D2-c1`–`D2-c4`). Skill lines are file:line as cited in `abstracted-full.md`; baseline files are untouched.

Review applied: a reviewer with the evidence tested the "baseline, often broken" entries. Six stay baseline as written. Two ("state shared facts once", "literal prose") move to Kind "correction", with the reviewer's emphasis. One (command blocks) moves to "correction", marked as a candidate change. Six move to Dropped as already covered by the skill. Each affected entry has a "Review" line.

## Kept

30 entries, ordered by source count, most first. "Members" lists the Rules that landed in the cluster, so the every-rule-once check can be audited.

### 1. Run every sample and check it against its text
- **Rule:** Run, or at minimum compile or type-check, every code sample and command against the version the page claims, and compare the real output with what the text shows. Check that names, arguments, status codes and sample data agree between the sample, the prose and the output. Small errors a run or a reread would catch (a misspelled name, the wrong status or helper named in prose, a wrong argument) were the typical failures.
- **Kind:** baseline, often broken
- **Skill line:** SKILL.md:64 (D also cites SKILL.md:65)
- **Sources:** A, B, D, E, F (5)
- **Applies to:** every page with code
- **Without it:** the agent hands over samples whose syntax, values or output don't match the prose.
- **Review:** keep as written. The breaches were outright errors or inconsistencies that plain checking would have caught.
- **Members:** baseline lists only (no Rules cluster).

### 2. Mixed content within a page
- **Rule:** Judge a page by the reader's job. Each page has one job and one dominant kind of content. Other kinds (a short explanation of what was just built, rationale, internals, advanced depth, a short catalogue) may appear only as short, bounded sections that are labelled, sit off the numbered steps in a consistent position (after the thing they explain), can be skipped without losing the thread, and link to the full treatment. Exhaustive lookup tables, setup and cross-cutting topics go on their own page. Long material of another kind gets its own page.
- **Kind:** correction
- **Skill line:** SKILL.md:13 ("one mode per page"), SKILL.md:31 ("link between modes instead of merging them"), SKILL.md:69; also teaching.md:30
- **Sources:** A, B, C, D, F by rules (5). E's and G's "On mixing modes" positions agree, so all seven were weighed.
- **Applies to:** tutorial, how-to, reference, explanation, book
- **Without it:** the agent either splits every aside onto a separate page and fragments the reader's task, or mixes whole reference tables into a guide.
- **Conflict:** B-C4 (explanation and steps may share a page under headings) and F-7 (one dominant kind, other kinds in fixed-position labelled sections) differ in wording. The seven "On mixing modes" sections all report bounded, labelled mixing with exhaustive lookup kept elsewhere. A, C, D, E and G say this meets the rule's purpose, and B and F say it only rewords the rule. None reports interleaving kinds inside a numbered procedure, and none has reader-outcome data. The merged rule therefore reads the rule at section level, by the reader's job, and keeps exhaustive lookup out.
- **Members:** A-M10, B-C4, C-15, D1-9, F-7.

### 3. Avoid content that goes stale; version notes only in set-apart blocks
- **Rule:** Don't let a page go stale for avoidable reasons. Keep version numbers, support and compatibility facts, and time-relative words ("currently", "new", "recently") out of running prose. Hold version and support facts in one structured, ideally generated, place per page. Don't hard-code environment-specific output, and don't keep statements that a newer page contradicts. The exception is a change note that says what changed in which version and what an upgrader must do. It may sit beside the rule it affects as a short, self-contained, set-apart block that can be deleted without touching the surrounding text, always with an explicit version, and removed after a fixed number of releases. When defaults or behaviour change, record the history both beside the setting and in a per-release roll-up.
- **Kind:** baseline, often broken, with its correction folded in
- **Skill line:** SKILL.md:70 ("hard-coded versions in prose")
- **Sources:** B, C, D, F, G (5). B, C, D, F and G broke the baseline rule. C, D, F and G back the corrected form.
- **Applies to:** every page; reference and guides most
- **Without it:** the agent writes "as of 3.2, …" and "recently added" into running prose, or bans useful upgrade notes outright.
- **Review:** keep as written. The breaches were errors a check would have caught; the set-apart change note below is a limit on the rule, not a breach of it.
- **Conflict:** C-8 and F-12 keep versions out of prose, while G-c5 says a version note in prose is useful when it says what changed and what to do. The merged rule keeps versions out of running prose but allows the set-apart, versioned, deletable note, which satisfies all three. G's warning about version-less time words is kept.
- **Members:** C-8, D2-3, F-12, G-c5.

### 4. Show wrong code as wrong, inside the block
- **Rule:** When you show a wrong or discouraged pattern, mark it as wrong inside the code block itself (a short comment prefix), so a copied snippet still carries the warning. Put the right version next to it, and say in the next sentence why the wrong one fails.
- **Kind:** missed principle
- **Sources:** A, D, F, G (4)
- **Applies to:** every page with code: tutorial, how-to, reference, book
- **Without it:** the agent shows the bad version with the caveat only in prose, and readers copy it as correct.
- **Members:** A-M3, D2-7, F-17, G-M5.

### 5. Help readers choose between overlapping options
- **Rule:** Where features or approaches overlap, say how to choose. Each entry states the condition, or the one difference that matters, that separates it from its nearest alternative, and links to it. Where there are many options, give a decision aid keyed to the reader's circumstances that names the recommended option, ordered from least to most effort or control with when to move up. Say when not to use something and what to use instead. In a page's opening, say what the subject is not and name the neighbour it is most often confused with.
- **Kind:** missed principle
- **Sources:** B, C, D, F (4)
- **Applies to:** how-to, reference, explanation
- **Without it:** the agent lists options as equals and leaves the reader to pick wrongly.
- **Conflict:** C-9 orders options by effort, D2-4 keys them to circumstances, and F-4 uses one separating condition per entry. These fit together as one decision aid, so no source's rule had to be dropped.
- **Members:** B-M3, C-9, D1-6, D1-7, D2-4, F-4.

### 6. State what a page leaves out and where the rest lives
- **Rule:** Say where an explanation is a simplification, and make sure every skipped edge case lands on an exhaustive page that the simple page links to. Say that a guide covers only the common path and where the rare cases are documented. Say when a table or list is a selection, and point to the complete source. State the environment the page assumes. Put the omission in one sentence where the reader would look, with a link to the exact section.
- **Kind:** missed principle (the skill states scope only for explanation pages, at reference-and-guides.md:59, and purpose and audience at SKILL.md:35)
- **Sources:** A, B, D, G (4)
- **Applies to:** every page
- **Without it:** a partial list reads as complete, and skipped cases are silently missing.
- **Members:** A-M4, B-M6, D2-5, D2-10, G-M1.

### 7. Scope the running example to a build-up sequence
- **Rule:** Declare the example domain near the start of a page. Keep one domain through a sequence that builds on itself (a chapter, a section or a learning path) and evolve the same example across it. Change domain across pages that don't build on each other, or when a concept needs differently shaped data. In that case use a small purpose-built dataset shown inline. Reference examples are self-contained and must not depend on a lesson's data. Don't force one scenario on a whole documentation set.
- **Kind:** correction
- **Skill line:** SKILL.md:46 ("Use one running domain across a doc set")
- **Sources:** A, B, D, G (4)
- **Applies to:** tutorial, guide, reference, book
- **Without it:** the agent bends unrelated pages into one scenario, or writes a reference example that only runs on a lesson's data.
- **Conflict:** A says per chapter or section, B per group of pages that build, D per worked sequence, G per learning path. The merged unit is "a sequence of pages that build on each other", the broadest unit none contradicts, and all four reject a single domain across the whole set.
- **Members:** A-C4, B-C1, D1-13, G-c3.

### 8. Reference may carry short advice beside the item
- **Rule:** Keep reference neutral, with no persuasion or vendor claims. Where a wrong choice is costly or non-obvious, put a short, plain recommendation or verdict with its reason right beside the option or rule it qualifies (inline or in a tip), such as "rarely appropriate" or "use X instead". Don't move such a warning to a guide, because the reader who lands from search must see it at the point of error.
- **Kind:** correction
- **Skill line:** reference-and-guides.md:24 ("No opinions, no 'you should'; put recommendations in guides"); SKILL.md:28
- **Sources:** C, D, F, G (4)
- **Applies to:** reference
- **Without it:** the agent strips hazards out of reference and the reader meets the trap with no warning.
- **Conflict:** F's neutrality rule is about vendors, not advice, and C, D and G say the advice needs its reason. The merged rule requires the reason and bans promotion.
- **Members:** C-16, D1-11, D2-c1, F-14, G-c1.

### 9. A page must hold together when walked literally
- **Rule:** Walk the page literally from its stated prerequisites in a clean state. Everything it promises or relies on must be present: every promised list or step, every function or method it uses is defined, every file or dataset the lesson needs can be created from the text or is supplied, and the summaries, prose and file names match the code.
- **Kind:** baseline, often broken
- **Skill line:** SKILL.md:66
- **Sources:** B, C, D, G (4)
- **Applies to:** tutorial, how-to, book
- **Without it:** the page refers to a list that isn't there or data the reader can't create.
- **Review:** keep as written. The breaches were missing or unsupported things that a literal walk-through would have caught.
- **Members:** baseline lists only.

### 10. One term per concept, identical everywhere, updated everywhere
- **Rule:** Use one term per concept and spell it identically, parameter names included, across prose, code, output, sibling pages and cross-references. Define a concept once. When you rename or change anything, search the docs and update every occurrence, including related pages (a guide must not lag its reference). Examples must not contradict sibling pages, and output formats must match across pages. Prose that names a listing, function or section must name the right one.
- **Kind:** baseline, often broken (three skill lines state this rule, so it is one entry)
- **Skill line:** SKILL.md:38, SKILL.md:57, SKILL.md:67 (F also cites reference-and-guides.md:23 and :88)
- **Sources:** A, B, E, F (4)
- **Applies to:** every page
- **Without it:** names, values and cross-references drift between prose, code and sibling pages.
- **Review:** keep as written. The breaches were inconsistencies the set's own conventions would have caught.
- **Members:** baseline lists only.

### 11. Teach the current approach first; label older forms and name the replacement
- **Rule:** Examples teach habits. Write every example in the currently recommended, non-deprecated, safe style as if it will be copied into production, and order the favoured approach first. Put superseded or older forms after it, short and labelled as superseded, naming what replaces them, so readers recognise them in existing code. Where an older edition of the docs exists, point to it. When you remove documentation for a retired feature, leave a short pointer to the archived version and any migration note.
- **Kind:** missed principle
- **Sources:** B, D, F (3)
- **Applies to:** every page with examples: tutorial, how-to, reference, book
- **Without it:** the agent leads with an outdated or unsafe pattern that readers copy.
- **Members:** B-M4, D1-4, D2-11, D2-12, F-18.

### 12. A learner's path has no choices, but may mention what else exists
- **Rule:** The path the learner follows contains no choices, but you may say what else exists. Show the alternative forms the reader will meet in other people's code or is likely to try, and say why a rejected one falls short. Label each alternative with which to prefer and why, and put it in a bounded aside after the main step so it doesn't derail the path. Keep this to the few the reader will actually meet.
- **Kind:** correction
- **Skill line:** SKILL.md:26 ("no choices"); teaching.md:23 ("Remove… alternative approaches… Choices belong in how-to guides")
- **Sources:** A, E, G (3)
- **Applies to:** tutorial, book
- **Without it:** the agent leaves out alternatives, so a reader who tries the obvious wrong thing or meets a variant gets no explanation.
- **Conflict:** A shows a rejected alternative with its reason (and says nothing about leaving others out), E shows two or three forms the reader will meet, and G labels alternatives as long as none derails the path. None contradicts the others, so the merged rule takes the union, bounded by "the reader will meet or try it".
- **Members:** A-C1, E-C4, G-C4.

### 13. Gloss background briefly at first use
- **Rule:** Link out for background the target reader is assumed to have. At first use, give a one- or two-sentence gloss of general terms or language features, with an outside link, set apart where the page's conventions allow so experienced readers can skip it. Where a topic's own explanation depends on small background the reader may lack, teach it in a bounded, titled aside that says what it leaves out. Never teach background at length.
- **Kind:** correction
- **Skill line:** teaching.md:8 ("Do not teach them inline"); SKILL.md:55
- **Sources:** A, D, E (3)
- **Applies to:** tutorial, explanation, book, guide
- **Without it:** the agent either assumes every term is known or detours into a long lesson on prerequisites.
- **Conflict:** A and D give one or two sentences, and E allows a small titled aside. The merged rule uses the gloss as the default and the aside only when the explanation depends on the background.
- **Members:** A-C3, D2-c4, E-C3.

### 14. Give readers a guide to the material
- **Rule:** Tell readers how to use a long work or a documentation set. Say who it is for and who it is not for (and where those readers should go instead). Offer routes through it (including skipping ahead and coming back), and say which parts they may skim or skip and that partial understanding on a first pass is expected. Say in a sentence per kind of page what need it serves, add a feature-by-feature index that lists the guide, task and lookup pages side by side, and end each overview with a jump for people who already know the content.
- **Kind:** missed principle
- **Sources:** A, C, E (3)
- **Applies to:** book, documentation set, tutorial series
- **Without it:** readers get no map, and can't tell whether to read it, skim it or skip it.
- **Members:** A-M5, A-M6, C-4, C-11, E-M3.

### 15. Let readers check claims themselves
- **Rule:** Show the input data, the operation and the exact result together, so a reader can verify the result by hand. Teach a concrete method for tracing behaviour by hand (substitute values, list events in order) and reuse it across pages. Where a documented default or built-in list can be inspected, give the command that shows the live value on the reader's own system.
- **Kind:** missed principle
- **Sources:** A, D, G (3)
- **Applies to:** guide, reference, tutorial, explanation
- **Without it:** the reader must take results and defaults on trust.
- **Members:** A-M8, D2-6, G-M4.

### 16. Links and cross-references resolve, and track the reader's version
- **Rule:** Every internal link, anchor and named cross-reference (a listing, section or function) must resolve and name the right target, and must be rechecked after any restructuring or renaming. In a documentation set published in several versions, cross-links land on the version the reader is reading, using the alias that tracks the same release. Pin to a specific version only when the sentence is about that release or points to legacy docs.
- **Kind:** baseline, often broken, with its correction folded in
- **Skill line:** SKILL.md:68 ("every external link is to a stable, versioned URL where possible")
- **Sources:** B, D, E (3). D and E broke the baseline rule. B and D back the version-tracking link.
- **Applies to:** every page in a versioned set
- **Without it:** the agent pins links to a version, leaving readers on the wrong release.
- **Review:** keep as written. The breaches were links that did not resolve or named the wrong target.
- **Conflict:** the skill says to use versioned URLs, while B-C2 and D1-8 say to track the reader's version. The merged rule defaults to the tracking link and pins only for release-specific sentences. B's evidence doesn't show when pinning is right beyond legacy pointers.
- **Members:** B-C2, D1-8.

### 17. Scale reference examples to the entry
- **Rule:** A thin entry (only a signature or an option list) may carry no example of its own and should point to the worked example in a guide, saying so. Give an example wherever behaviour is surprising. An entry with many forms or options gets one example per distinct form, not just one or two.
- **Kind:** correction
- **Skill line:** reference-and-guides.md:15 ("At least one realistic example")
- **Sources:** C, G (2)
- **Applies to:** reference
- **Without it:** the agent pads thin entries with filler examples and under-exemplifies rich ones.
- **Conflict:** C-17 says not every entry needs an example, and G-M3 says one or two are too few for many-form entries. These conflict only on a fixed count, so the merged rule makes the count follow the entry.
- **Members:** C-17, G-M3.

### 18. Reference errors: contract errors and decision-changing conditions
- **Rule:** In reference, document the errors and conditions that belong to the feature's own contract and change what the reader must do, including cases that look like failures but are not. Don't promise an exhaustive list of every error. Leave out errors caused by caller-supplied code or wrong-typed arguments, and keep step-by-step fixes on a separate troubleshooting page. Put verbatim message text where readers meet it (lessons, guides, troubleshooting), except where users parse a stable format, in which case give it exactly.
- **Kind:** correction
- **Skill line:** reference-and-guides.md:13 ("each error… include the exact message text"), reference-and-guides.md:38 ("List *all* error cases")
- **Sources:** F, G (2)
- **Applies to:** reference, troubleshooting
- **Without it:** the agent lists every conceivable error with message text, which is unmaintainable and buries the ones that matter.
- **Conflict:** F puts fixes on a troubleshooting page, while G documents conditions "at the rule where they arise". A one-line statement of what the reader must do belongs in the entry, and a full fix walkthrough belongs on the troubleshooting page.
- **Members:** F-15, G-c2.

### 19. Be exact about the contract, not about incidental values
- **Rule:** Say exactly what callers may rely on, including calls that terminate the program rather than return an error and invariants the caller must uphold, listed separately from recoverable errors. Don't commit to exact incidental values you want the freedom to change.
- **Kind:** correction
- **Skill line:** SKILL.md:40 ("Numbers, units, defaults, limits… beat adjectives"); reference-and-guides.md:14
- **Sources:** D, E (2)
- **Applies to:** reference
- **Without it:** the agent documents incidental behaviour as a promise and omits the invariants a caller must keep.
- **Members:** D1-14, D2-c2, E-M6.

### 20. Show what a convenience expands to
- **Rule:** When a call or shortcut hides several steps, show the lower-level steps or result it produces next to it, and label the shortcut as doing the same thing, so the reader can check their mental model.
- **Kind:** missed principle
- **Sources:** C, D (2)
- **Applies to:** tutorial, guide, reference
- **Without it:** readers can't see what the shortcut does, so their mental model is wrong.
- **Conflict:** C-2 sequences it (long form first, tell the learner the order is deliberate) and D shows the expansion beside the call. The merged rule keeps what both allow and leaves the long-form-first ordering to the writer.
- **Members:** C-2, D1-3, D2-8.

### 21. State a feature's limits and silent failures
- **Rule:** Where docs present a safeguard, guarantee, filter or check as protecting the reader, state its limits: what it does not catch (a test run may miss cases), which operations bypass it, and what outside mechanism must complement it. Document failures that produce no error (silent no-ops, dropped work, quiet fallbacks) where they occur.
- **Kind:** missed principle
- **Sources:** C, D (2)
- **Applies to:** reference, guide, explanation
- **Without it:** the reader assumes protection that isn't there.
- **Members:** C-6, D1-5, D2-9.

### 22. Mark defined terms; flag narrowed everyday words
- **Rule:** Mark a term typographically at the point you define it, in one consistent style. Where you give an everyday word a narrow technical meaning, say so once and use a different phrase for the broad idea.
- **Kind:** missed principle
- **Sources:** A, E (2)
- **Applies to:** every page; book and tutorial most
- **Without it:** readers can't tell a defined term from an ordinary word.
- **Members:** A-M2, E-M8.

### 23. Stable heading anchors
- **Rule:** When a page leans on an idea defined elsewhere, link to the specific section that defines it. Give headings stable explicit identifiers, and when you rename a heading, keep the old anchor in place with a note not to remove it.
- **Kind:** missed principle
- **Sources:** A, E (2)
- **Applies to:** every page
- **Without it:** a heading rename silently breaks inbound links.
- **Members:** A-M11, E-M10.

### 24. Annotate only what isn't obvious
- **Rule:** After a code sample, list only the lines or choices whose purpose isn't obvious, one short point each, and say the rest is self-explanatory. In example code, don't comment what a line plainly does. A very small example may be walked through line by line.
- **Kind:** missed principle
- **Sources:** C, F (2)
- **Applies to:** tutorial, guide, reference, book
- **Without it:** the agent narrates every line.
- **Members:** C-3, F-21.

### 25. Gender-neutral wording for unspecified people
- **Rule:** When writing about hypothetical or unspecified people, avoid gendered pronouns: use singular "they" or reword so no pronoun is needed.
- **Kind:** missed principle
- **Sources:** C, F (2)
- **Applies to:** every page
- **Without it:** the agent defaults to "he" for a hypothetical user or developer.
- **Members:** C-14, F-10.

### 26. Say what each example shows
- **Rule:** Give every example, listing or figure a title or caption that says what it demonstrates, including that it doesn't work yet when that is the point. Never use a bare number or generic label. Number only the listings that later text refers back to.
- **Kind:** missed principle
- **Sources:** E, F (2)
- **Applies to:** book, tutorial, guide, reference
- **Without it:** the agent labels examples "Example 1", and readers can't tell what each is for.
- **Members:** E-M9, F-16.

### 27. State shared facts once; repeat only the costliest trap
- **Rule:** Shared facts (setup steps, authentication, shared lists) belong in one place that other pages link to. Don't paste the same instructions, generated method lists or passages into several pages. The one exception is the single costliest trap: repeat it where a reader first meets the feature, in the length that suits the page (a clause in a lesson, a paragraph in a guide, the exact rule in reference), because readers often arrive without passing through the overview. Treat each copy as something to recheck when its source changes.
- **Kind:** correction
- **Skill line:** reference-and-guides.md:23 (also SKILL.md:70)
- **Sources:** C, G (2). D, F and G also broke the "state once" rule, but the review found the useful finding is the limit on it, not the breaches.
- **Applies to:** every page; reference and guides most
- **Without it:** the agent either pastes the same setup everywhere and lets the copies drift, or links everything so the trap is missed.
- **Review:** keep the rule, change its emphasis. The "state once" default stands. The emphasis is now the limit: repeat only the single costliest trap, and recheck every copy.
- **Conflict:** "state once and link" (the skill) against C-18 and G-M7 ("repeat the trap at point of use"). The merged rule keeps the default and allows one repeated trap. The repeat stays short, since G also found near-verbatim copies drifting apart.
- **Members:** C-18, G-M7.

### 28. Keep prose literal; warm voice in teaching pages only
- **Rule:** Keep wording literal enough to survive translation and a non-native reader: avoid idioms, figurative phrasing, culture-bound references, phrasal verbs and jokes that need cultural context. In teaching and community pages a warm, personal voice is legitimate: write as one person to another, pose the problem before the answer, prefer concrete statements to stacked superlatives, and check after any editing pass that these qualities survived. Light humour is acceptable there. Keep lookup pages plain.
- **Kind:** correction
- **Skill line:** SKILL.md:54; books-and-video.md:43 (also SKILL.md:41)
- **Sources:** B, C (2). A and G broke the literal-wording rule, but the review found the useful finding is the limit on it, not the breaches. A called its own breach a deliberate voice choice.
- **Applies to:** every page; teaching pages and books for the warm voice
- **Without it:** the agent either writes cold teaching text or sprinkles idioms and jokes that non-native readers trip on.
- **Review:** keep the rule, change its emphasis. Literal prose stays the default. The emphasis is now that a warm, personal voice and light humour are legitimate in teaching and community pages, and lookup pages stay plain.
- **Conflict:** the literal-wording rule against B-C3 (humour is legitimate in teaching) and C-13 (personal voice). B's evidence says nothing about translation, so it can't license idioms. The merged rule puts warmth in address and concreteness, keeps idioms out everywhere, and limits humour to light use in teaching pages.
- **Members:** B-C3, C-13.

### 29. Pasted output comes from a real run and must not hard-code stale detail
- **Rule:** Show only output taken from a real run of the exact code and version shown, and make sure the pasted output matches the code. Don't hard-code environment-specific output (paths, versions, timestamps) that goes stale.
- **Kind:** baseline, often broken
- **Skill line:** SKILL.md:53 (also SKILL.md:64, SKILL.md:70)
- **Sources:** E, G (2)
- **Applies to:** tutorial, guide, book
- **Without it:** output blocks drift from the code they claim to show.
- **Review:** keep as written. The breaches were pasted output that no longer matched the code, or frozen details that age.
- **Members:** baseline lists only.

### 30. Whatever a reader copies must run; set one convention for command blocks
- **Rule:** Pick one convention for command examples, state it, and apply it across the whole set. The safe default is a command-only block with no prompt character and the output in a separate block. Putting a prompt character inside the block, or showing the real captured output directly beneath the command in the same block, is acceptable as a deliberate house convention. It is acceptable only when the rendered page excludes the prompt and the output from what the reader copies (for example non-selectable prompt and output styling, or a copy button that copies the command only), and you have checked that on the rendered page. Where you can't confirm what gets copied, use the safe default.
- **Kind:** correction (a candidate change, not settled)
- **Skill line:** SKILL.md:43 ("no `$` prompts inside copyable blocks, output shown in a separate block")
- **Sources:** B, C (2). B and C broke the baseline rule inconsistently. D's single-source relaxation (D1-12, D2-c3) says the same thing and stays in Dropped.
- **Applies to:** tutorial, how-to, book
- **Without it:** the agent strips prompts from a set whose standard form puts them in the block, or leaves output in a block readers copy whole.
- **Review:** relax the rule. The reviewer found it stricter than what established sets do on purpose. Two of the sets mark command lines with a prompt character inside the block as their standard form, and one of them mandates it in its style guide for every command block. In its step-by-step lessons, the other shows the real captured output directly beneath the command in the same block for most commands. The evidence shows the practice and its consistency, but not what readers end up copying.
- **Conflict:** the skill's intent is that what a reader copies runs. The stated practice is prompt-in-block and output-in-block as a consistent house standard. Neither forbids the other, because the practice is only a problem if the copy action picks up the prompt or the output, and the evidence doesn't show that. The merged rule requires one stated convention and a check that the copy action excludes the extras, and falls back to the skill's original form when that can't be confirmed.
- **Members:** baseline lists only; D1-12 and D2-c3 are the matching Rules and remain in the single-source cluster.

## Dropped

Redundant with the skill (8: 2 clusters from the Rules and 6 baseline entries after review):
- **Show the problem or failure before the remedy** (A-M1, B-M2, C-1, E-M1; A, B, C, E): redundant. The skill already says to trigger and read a common error on purpose (teaching.md:31) and to show wrong or naive approaches first (books-and-video.md:45). E's "not one per lesson" doesn't contradict teaching.md:31, whose "once" is per error.
- **Open with the outcome and close with a recap** (B-M1, D1-1, D2-2; B, D): redundant. The skill states the opening outcome (SKILL.md:35, teaching.md:14), the recap (teaching.md:19) and the book chapter's opening and closing (books-and-video.md:17, :20). The only extra is stating it for every page type and echoing the opener's words.
- **Cut words that say it is easy or obvious** (baseline entry; B, C, D, E, F, G): redundant with SKILL.md:41. The review found the departures scattered, on some pages and not others, with no written convention behind them, and not frequent enough to be a pattern.
- **State prerequisites and the version the page is true for** (baseline entry; A, B, F): redundant with SKILL.md:39 (also teaching.md:8, teaching.md:14). Same finding as above. Caveat: many pages simply leave the element out, and the review did not treat omission as deliberate without a written convention. If very frequent omission should count as design, this rule needs a proper count before it is left alone.
- **Exercises need practice, checkable outcomes, solutions and difficulty** (baseline entry; B, E, G): redundant with teaching.md:33 (also teaching.md:27). Same finding and the same omission caveat as the prerequisites rule.
- **Use reserved, clearly fake placeholder values** (baseline entry; A, D): redundant with SKILL.md:52. Same finding as the first.
- **Give a known-good state and everything the lesson needs** (baseline entry; C, G): redundant with teaching.md:17 (G also cites SKILL.md:66). Same finding as the first.
- **Show recovery at the point of failure** (baseline entry; D, G): redundant with teaching.md:18. Same finding as the first.

Single source (39 clusters):
- Preview multi-step process as a verb-led list (A-M7; A)
- Exercises with planted defects and hints (A-M9; A)
- Prediction prompts: no fixed quota (A-C2; A)
- Accessible samples (B-M5; B)
- Page-length limit and splitting (B-M7; B)
- One sentence per line in the source (B-M8; B)
- Wrong samples as bugs and a one-step edit route (B-M9; B)
- Where-to-get-help routes, including a private security route (C-5; C)
- Link to third parties' setup instead of copying it (C-7; C)
- State the starting state of a continued example (C-10; C)
- Separate section for builders and capability detection (C-12; C)
- Callout types by cost of skipping (D1-2, D2-1; D)
- File path on every file listing (D1-10; D; also stated at books-and-video.md:26)
- Copied code must work; prompts may stay where the tool excludes them (D1-12, D2-c3; D). It relaxes SKILL.md:43 and agrees with the corrected entry 30, but the Rules cluster has one source, so it stays here.
- Describe behaviour in a typical full setup (D2-13; D)
- Rendered preview of every doc change (D2-14; D)
- Show the desired usage or a failing test before the implementation (E-M2; E)
- Alternate concept sections with integration projects (E-M4; E)
- Teach reading diagnostics (E-M5; E)
- Regenerate steps or list of places to change for non-generatable content (E-M7; E)
- Publish a revision policy (E-M11; E)
- Using a not-yet-taught idea is acceptable if not silent (E-C1; E; also stated at teaching.md:9)
- Name difficulty honestly (E-C2; E)
- Numbered steps for plans, one change per listing in narrative tutorials (E-C5; E)
- Print and offline references (E-C6; E)
- Analogies as entry ramps (E-C7; E)
- Page types, templates and following the closest existing page (F-1, F-2; F)
- Hub pages and non-duplicated sibling pages (F-3, F-6; F)
- Previous and next links (F-5; F)
- Heading and list structure (F-8; F)
- No location words such as "above" and "below" (F-9; F)
- Related-links sections (F-11; F)
- Lead paragraph shape (F-13; F)
- Partial snippets labelled partial (F-19; F)
- Logging output as trailing comment (F-20; F)
- Automatic formatter for code layout (F-22; F)
- Departures from conventions in a fixed section (G-M2; G)
- Layered rules as an ordered procedure with worked examples (G-M6; G)
- Match the layout conventions of the tools readers use (G-M8; G)

Unresolvable conflict (0): none. Every conflict above had a rule none of the members contradicted.

## Counts

- **Rules read:** 131 (A 15, B 13, C 18, D 32, E 18, F 22, G 13). The Audit section of the source file says 127 and counts D as 28, but D's second file has 14 missed principles and 4 corrections, so D is 14 + 18 = 32.
- **Clusters formed from the Rules:** 66. Every rule is in exactly one: 81 rules in 25 kept clusters, 7 in 2 redundant clusters, 43 in 39 single-source clusters (81 + 7 + 43 = 131). The review changed no cluster membership.
- **Kept entries:** 30, being the 25 clusters plus 5 entries that came from the "Baseline rules broken" lists alone (entries 1, 9, 10, 29, 30).
  - Missed principles: 13 (entries 4, 5, 6, 11, 14, 15, 20, 21, 22, 23, 24, 25, 26).
  - Corrections: 11 (entries 2, 7, 8, 12, 13, 17, 18, 19, 27, 28, 30). Entries 27 and 28 were "baseline, often broken" before the review and are now corrections. Entry 30 is a candidate change, not settled.
  - Baseline, often broken: 6 (entries 1, 3, 9, 10, 16, 29), all kept as written by the review. Entries 3 and 16 carry a correction from the Rules, stated once.
- **Dropped:** 47 items. Single source 39 clusters. Redundant with the skill 8: the 2 clusters (teaching.md:31 and books-and-video.md:45; SKILL.md:35, teaching.md:14 and :19) and the 6 baseline entries the review found already covered (SKILL.md:41, SKILL.md:39, teaching.md:33, SKILL.md:52, teaching.md:17, teaching.md:18). Unresolvable conflict 0.
- **Changes from the previous version of this file:** kept entries went from 36 to 30. Baseline went from 15 to 6, corrections from 8 to 11, and missed principles stayed at 13. Dropped went from 41 to 47.
- **Skill lines confirmed by two or more sources:**
  - teaching.md:31 (A, B, D)
  - SKILL.md:50 (B, D)
  - SKILL.md:46 (C, F)
  - teaching.md:15 (C, D)
  - books-and-video.md:25 (B, E)
  - reference-and-guides.md:23 (F, G)
  - reference-and-guides.md:29 (F, G)
  - SKILL.md:45 (D, G)
  - SKILL.md:70 (C, F)

  Three of these lines were also broken or corrected elsewhere: SKILL.md:46 (corrected, entry 7), reference-and-guides.md:23 (limited by entry 27) and SKILL.md:70 (kept as written, entry 3). The confirmation holds for the idea, and the entries say what to fix.
- **Baseline breaches by one source only (not kept):** SKILL.md:36, :40, :42, :44, :45, :46, :50, :65; teaching.md:27, :41; reference-and-guides.md:16, :37, :39, :50, :56, :88; books-and-video.md:43 (folded into entry 28 because SKILL.md:54 is the same rule).
