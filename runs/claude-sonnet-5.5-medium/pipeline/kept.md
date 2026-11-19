# Rules to write into the skill

Each rule below has a heading, the rule itself, its kind, where it applies, and what an agent does wrong without it.

### 1. Run every sample and check it against its text
- **Rule:** Run, or at minimum compile or type-check, every code sample and command against the version the page claims, and compare the real output with what the text shows. Check that names, arguments, status codes and sample data agree between the sample, the prose and the output. Small errors a run or a reread would catch (a misspelled name, the wrong status or helper named in prose, a wrong argument) were the typical failures.
- **Kind:** well known, often broken.
- **Applies to:** every page with code
- **Without it:** the agent hands over samples whose syntax, values or output don't match the prose.

### 2. Mixed content within a page
- **Rule:** Judge a page by the reader's job. Each page has one job and one dominant kind of content. Other kinds (a short explanation of what was just built, rationale, internals, advanced depth, a short catalogue) may appear only as short, bounded sections that are labelled, sit off the numbered steps in a consistent position (after the thing they explain), can be skipped without losing the thread, and link to the full treatment. Exhaustive lookup tables, setup and cross-cutting topics go on their own page. Long material of another kind gets its own page.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, how-to, reference, explanation, book
- **Without it:** the agent either splits every aside onto a separate page and fragments the reader's task, or mixes whole reference tables into a guide.

### 3. Avoid content that goes stale; version notes only in set-apart blocks
- **Rule:** Don't let a page go stale for avoidable reasons. Keep version numbers, support and compatibility facts, and time-relative words ("currently", "new", "recently") out of running prose. Hold version and support facts in one structured, ideally generated, place per page. Don't hard-code environment-specific output, and don't keep statements that a newer page contradicts. The exception is a change note that says what changed in which version and what an upgrader must do. It may sit beside the rule it affects as a short, self-contained, set-apart block that can be deleted without touching the surrounding text, always with an explicit version, and removed after a fixed number of releases. When defaults or behaviour change, record the history both beside the setting and in a per-release roll-up.
- **Kind:** well known, often broken.
- **Applies to:** every page; reference and guides most
- **Without it:** the agent writes "as of 3.2, …" and "recently added" into running prose, or bans useful upgrade notes outright.

### 4. Show wrong code as wrong, inside the block
- **Rule:** When you show a wrong or discouraged pattern, mark it as wrong inside the code block itself (a short comment prefix), so a copied snippet still carries the warning. Put the right version next to it, and say in the next sentence why the wrong one fails.
- **Kind:** not commonly known.
- **Applies to:** every page with code: tutorial, how-to, reference, book
- **Without it:** the agent shows the bad version with the caveat only in prose, and readers copy it as correct.

### 5. Help readers choose between overlapping options
- **Rule:** Where features or approaches overlap, say how to choose. Each entry states the condition, or the one difference that matters, that separates it from its nearest alternative, and links to it. Where there are many options, give a decision aid keyed to the reader's circumstances that names the recommended option, ordered from least to most effort or control with when to move up. Say when not to use something and what to use instead. In a page's opening, say what the subject is not and name the neighbour it is most often confused with.
- **Kind:** not commonly known.
- **Applies to:** how-to, reference, explanation
- **Without it:** the agent lists options as equals and leaves the reader to pick wrongly.

### 6. State what a page leaves out and where the rest lives
- **Rule:** Say where an explanation is a simplification, and make sure every skipped edge case lands on an exhaustive page that the simple page links to. Say that a guide covers only the common path and where the rare cases are documented. Say when a table or list is a selection, and point to the complete source. State the environment the page assumes. Put the omission in one sentence where the reader would look, with a link to the exact section.
- **Kind:** not commonly known.
- **Applies to:** every page
- **Without it:** a partial list reads as complete, and skipped cases are silently missing.

### 7. Scope the running example to a build-up sequence
- **Rule:** Declare the example domain near the start of a page. Keep one domain through a sequence that builds on itself (a chapter, a section or a learning path) and evolve the same example across it. Change domain across pages that don't build on each other, or when a concept needs differently shaped data. In that case use a small purpose-built dataset shown inline. Reference examples are self-contained and must not depend on a lesson's data. Don't force one scenario on a whole documentation set.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, guide, reference, book
- **Without it:** the agent bends unrelated pages into one scenario, or writes a reference example that only runs on a lesson's data.

### 8. Reference may carry short advice beside the item
- **Rule:** Keep reference neutral, with no persuasion or vendor claims. Where a wrong choice is costly or non-obvious, put a short, plain recommendation or verdict with its reason right beside the option or rule it qualifies (inline or in a tip), such as "rarely appropriate" or "use X instead". Don't move such a warning to a guide, because the reader who lands from search must see it at the point of error.
- **Kind:** overrides common advice.
- **Applies to:** reference
- **Without it:** the agent strips hazards out of reference and the reader meets the trap with no warning.

### 9. A page must hold together when walked literally
- **Rule:** Walk the page literally from its stated prerequisites in a clean state. Everything it promises or relies on must be present: every promised list or step, every function or method it uses is defined, every file or dataset the lesson needs can be created from the text or is supplied, and the summaries, prose and file names match the code.
- **Kind:** well known, often broken.
- **Applies to:** tutorial, how-to, book
- **Without it:** the page refers to a list that isn't there or data the reader can't create.

### 10. One term per concept, identical everywhere, updated everywhere
- **Rule:** Use one term per concept and spell it identically, parameter names included, across prose, code, output, sibling pages and cross-references. Define a concept once. When you rename or change anything, search the docs and update every occurrence, including related pages (a guide must not lag its reference). Examples must not contradict sibling pages, and output formats must match across pages. Prose that names a listing, function or section must name the right one.
- **Kind:** well known, often broken.
- **Applies to:** every page
- **Without it:** names, values and cross-references drift between prose, code and sibling pages.

### 11. Teach the current approach first; label older forms and name the replacement
- **Rule:** Examples teach habits. Write every example in the currently recommended, non-deprecated, safe style as if it will be copied into production, and order the favoured approach first. Put superseded or older forms after it, short and labelled as superseded, naming what replaces them, so readers recognise them in existing code. Where an older edition of the docs exists, point to it. When you remove documentation for a retired feature, leave a short pointer to the archived version and any migration note.
- **Kind:** not commonly known.
- **Applies to:** every page with examples: tutorial, how-to, reference, book
- **Without it:** the agent leads with an outdated or unsafe pattern that readers copy.

### 12. A learner's path has no choices, but may mention what else exists
- **Rule:** The path the learner follows contains no choices, but you may say what else exists. Show the alternative forms the reader will meet in other people's code or is likely to try, and say why a rejected one falls short. Label each alternative with which to prefer and why, and put it in a bounded aside after the main step so it doesn't derail the path. Keep this to the few the reader will actually meet.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, book
- **Without it:** the agent leaves out alternatives, so a reader who tries the obvious wrong thing or meets a variant gets no explanation.

### 13. Gloss background briefly at first use
- **Rule:** Link out for background the target reader is assumed to have. At first use, give a one- or two-sentence gloss of general terms or language features, with an outside link, set apart where the page's conventions allow so experienced readers can skip it. Where a topic's own explanation depends on small background the reader may lack, teach it in a bounded, titled aside that says what it leaves out. Never teach background at length.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, explanation, book, guide
- **Without it:** the agent either assumes every term is known or detours into a long lesson on prerequisites.

### 14. Give readers a guide to the material
- **Rule:** Tell readers how to use a long work or a documentation set. Say who it is for and who it is not for (and where those readers should go instead). Offer routes through it (including skipping ahead and coming back), and say which parts they may skim or skip and that partial understanding on a first pass is expected. Say in a sentence per kind of page what need it serves, add a feature-by-feature index that lists the guide, task and lookup pages side by side, and end each overview with a jump for people who already know the content.
- **Kind:** not commonly known.
- **Applies to:** book, documentation set, tutorial series
- **Without it:** readers get no map, and can't tell whether to read it, skim it or skip it.

### 15. Let readers check claims themselves
- **Rule:** Show the input data, the operation and the exact result together, so a reader can verify the result by hand. Teach a concrete method for tracing behaviour by hand (substitute values, list events in order) and reuse it across pages. Where a documented default or built-in list can be inspected, give the command that shows the live value on the reader's own system.
- **Kind:** not commonly known.
- **Applies to:** guide, reference, tutorial, explanation
- **Without it:** the reader must take results and defaults on trust.

### 16. Links and cross-references resolve, and track the reader's version
- **Rule:** Every internal link, anchor and named cross-reference (a listing, section or function) must resolve and name the right target, and must be rechecked after any restructuring or renaming. In a documentation set published in several versions, cross-links land on the version the reader is reading, using the alias that tracks the same release. Pin to a specific version only when the sentence is about that release or points to legacy docs.
- **Kind:** well known, often broken.
- **Applies to:** every page in a versioned set
- **Without it:** the agent pins links to a version, leaving readers on the wrong release.

### 17. Scale reference examples to the entry
- **Rule:** A thin entry (only a signature or an option list) may carry no example of its own and should point to the worked example in a guide, saying so. Give an example wherever behaviour is surprising. An entry with many forms or options gets one example per distinct form, not just one or two.
- **Kind:** overrides common advice.
- **Applies to:** reference
- **Without it:** the agent pads thin entries with filler examples and under-exemplifies rich ones.

### 18. Reference errors: contract errors and decision-changing conditions
- **Rule:** In reference, document the errors and conditions that belong to the feature's own contract and change what the reader must do, including cases that look like failures but are not. Don't promise an exhaustive list of every error. Leave out errors caused by caller-supplied code or wrong-typed arguments, and keep step-by-step fixes on a separate troubleshooting page. Put verbatim message text where readers meet it (lessons, guides, troubleshooting), except where users parse a stable format, in which case give it exactly.
- **Kind:** overrides common advice.
- **Applies to:** reference, troubleshooting
- **Without it:** the agent lists every conceivable error with message text, which is unmaintainable and buries the ones that matter.

### 19. Be exact about the contract, not about incidental values
- **Rule:** Say exactly what callers may rely on, including calls that terminate the program rather than return an error and invariants the caller must uphold, listed separately from recoverable errors. Don't commit to exact incidental values you want the freedom to change.
- **Kind:** overrides common advice.
- **Applies to:** reference
- **Without it:** the agent documents incidental behaviour as a promise and omits the invariants a caller must keep.

### 20. Show what a convenience expands to
- **Rule:** When a call or shortcut hides several steps, show the lower-level steps or result it produces next to it, and label the shortcut as doing the same thing, so the reader can check their mental model.
- **Kind:** not commonly known.
- **Applies to:** tutorial, guide, reference
- **Without it:** readers can't see what the shortcut does, so their mental model is wrong.

### 21. State a feature's limits and silent failures
- **Rule:** Where docs present a safeguard, guarantee, filter or check as protecting the reader, state its limits: what it does not catch (a test run may miss cases), which operations bypass it, and what outside mechanism must complement it. Document failures that produce no error (silent no-ops, dropped work, quiet fallbacks) where they occur.
- **Kind:** not commonly known.
- **Applies to:** reference, guide, explanation
- **Without it:** the reader assumes protection that isn't there.

### 22. Mark defined terms; flag narrowed everyday words
- **Rule:** Mark a term typographically at the point you define it, in one consistent style. Where you give an everyday word a narrow technical meaning, say so once and use a different phrase for the broad idea.
- **Kind:** not commonly known.
- **Applies to:** every page; book and tutorial most
- **Without it:** readers can't tell a defined term from an ordinary word.

### 23. Stable heading anchors
- **Rule:** When a page leans on an idea defined elsewhere, link to the specific section that defines it. Give headings stable explicit identifiers, and when you rename a heading, keep the old anchor in place with a note not to remove it.
- **Kind:** not commonly known.
- **Applies to:** every page
- **Without it:** a heading rename silently breaks inbound links.

### 24. Annotate only what isn't obvious
- **Rule:** After a code sample, list only the lines or choices whose purpose isn't obvious, one short point each, and say the rest is self-explanatory. In example code, don't comment what a line plainly does. A very small example may be walked through line by line.
- **Kind:** not commonly known.
- **Applies to:** tutorial, guide, reference, book
- **Without it:** the agent narrates every line.

### 25. Gender-neutral wording for unspecified people
- **Rule:** When writing about hypothetical or unspecified people, avoid gendered pronouns: use singular "they" or reword so no pronoun is needed.
- **Kind:** not commonly known.
- **Applies to:** every page
- **Without it:** the agent defaults to "he" for a hypothetical user or developer.

### 26. Say what each example shows
- **Rule:** Give every example, listing or figure a title or caption that says what it demonstrates, including that it doesn't work yet when that is the point. Never use a bare number or generic label. Number only the listings that later text refers back to.
- **Kind:** not commonly known.
- **Applies to:** book, tutorial, guide, reference
- **Without it:** the agent labels examples "Example 1", and readers can't tell what each is for.

### 27. State shared facts once; repeat only the costliest trap
- **Rule:** Shared facts (setup steps, authentication, shared lists) belong in one place that other pages link to. Don't paste the same instructions, generated method lists or passages into several pages. The one exception is the single costliest trap: repeat it where a reader first meets the feature, in the length that suits the page (a clause in a lesson, a paragraph in a guide, the exact rule in reference), because readers often arrive without passing through the overview. Treat each copy as something to recheck when its source changes.
- **Kind:** overrides common advice.
- **Applies to:** every page; reference and guides most
- **Without it:** the agent either pastes the same setup everywhere and lets the copies drift, or links everything so the trap is missed.

### 28. Keep prose literal; warm voice in teaching pages only
- **Rule:** Keep wording literal enough to survive translation and a non-native reader: avoid idioms, figurative phrasing, culture-bound references, phrasal verbs and jokes that need cultural context. In teaching and community pages a warm, personal voice is legitimate: write as one person to another, pose the problem before the answer, prefer concrete statements to stacked superlatives, and check after any editing pass that these qualities survived. Light humour is acceptable there. Keep lookup pages plain.
- **Kind:** overrides common advice.
- **Applies to:** every page; teaching pages and books for the warm voice
- **Without it:** the agent either writes cold teaching text or sprinkles idioms and jokes that non-native readers trip on.

### 29. Pasted output comes from a real run and must not hard-code stale detail
- **Rule:** Show only output taken from a real run of the exact code and version shown, and make sure the pasted output matches the code. Don't hard-code environment-specific output (paths, versions, timestamps) that goes stale.
- **Kind:** well known, often broken.
- **Applies to:** tutorial, guide, book
- **Without it:** output blocks drift from the code they claim to show.

### 30. Whatever a reader copies must run; set one convention for command blocks
- **Rule:** Pick one convention for command examples, state it, and apply it across the whole set. The safe default is a command-only block with no prompt character and the output in a separate block. Putting a prompt character inside the block, or showing the real captured output directly beneath the command in the same block, is acceptable as a deliberate house convention. It is acceptable only when the rendered page excludes the prompt and the output from what the reader copies (for example non-selectable prompt and output styling, or a copy button that copies the command only), and you have checked that on the rendered page. Where you can't confirm what gets copied, use the safe default.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, how-to, book
- **Without it:** the agent strips prompts from a set whose standard form puts them in the block, or leaves output in a block readers copy whole.

### 31. No placeholders on disk
- **Rule:** Never write a placeholder, a question, or a note to the maintainer into any file. The maintainer asked for the writing so they don't have to do it, so what you write is final. Bring up in chat only what truly needs their judgment, where a wrong call would do real harm, and keep that as short as you can. For everything else, take the answer the evidence supports that claims the least on the maintainer's behalf, write it as final, and list those calls in your report.
- **Kind:** set by the maintainer.
- **Applies to:** every page
- **Without it:** An agent leaves markers like `TODO(verify)` or `[TO CONFIRM]` in the files, handing the work back to the person who asked for it.

### 32. State verified facts plainly
- **Rule:** Most sentences an agent feels the urge to qualify aren't overclaiming anything. Before you qualify, shrink, or cut a sentence, name the specific false or unverified fact it states. If you can't name one, it isn't an overclaim, so leave it as written. A statement of what something is for, or what it does, is not an overclaim. Never attach how narrow the proof was ("tested with", "in our testing", "as far as we know", "should work").
- **Kind:** set by the maintainer.
- **Applies to:** every page
- **Without it:** An agent qualifies, shrinks, or cuts sentences that were true as written, so readers trust the page less than the evidence deserves.

### 33. State a limit only where it changes what the reader can do
- **Rule:** State a limit only when it changes what the reader can do or should expect: a platform, a version, a model, a prerequisite, a risk to their data. State it once, as a fact, where the page keeps its caveats. Work the maintainer hasn't done yet, such as tests or benchmarks not yet run, isn't a limit for the reader. It belongs in contributor documentation.
- **Kind:** set by the maintainer.
- **Applies to:** every page
- **Without it:** An agent apologizes for its own unfinished work in user-facing pages, which tells the reader nothing they can act on.
