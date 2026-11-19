# Abstracted findings from seven documentation sources

Sources are labelled A to G. Source D is one source made of two files, so its rules are listed per file. Skill citations are file:line against the baseline skill files: SKILL.md, teaching.md, reference-and-guides.md, books-and-video.md. Each rule is marked [revised] where it was rewritten to match its evidence. No rule was marked [removed], and the Audit explains why.

---

## Source A

### 1. Rules

Missed principles

1. When a lesson exists to prevent a specific mistake, let the reader reproduce the mistake first, then name the cause and the fix.
2. When you give an everyday word a narrow technical meaning, mark it visibly, say once that you are doing so, and use a different phrase for the broad idea.
3. Mark wrong or discouraged code inside the code block itself with a short comment prefix. [revised]
4. Say plainly where an explanation is a simplification, and make sure every edge case you skipped lands on an exhaustive page that the simple page links to.
5. Tell readers which parts they may skim, and say that partial understanding on a first pass is expected; this is scope guidance, not apology.
6. Offer more than one route through the same material for different learning preferences, say at each entry point whom it suits, and end each overview with a jump for people who already know the content.
7. Before walking through a multi-step process, preview it as a short list whose items begin with verbs, then present the steps in that same order.
8. Teach a concrete method for tracing behaviour by hand (substitute values, list events in order, or tell one scenario from two vantage points) and reuse it across pages so readers can check claims themselves.
9. Include exercises built from nearly-working code with a planted defect, and give hints that say where such defects tend to hide.
10. Keep the main path linear by putting optional depth (internals, rationale) in clearly labelled blocks that can be skipped without losing the thread. [revised]
11. When a page leans on an idea defined elsewhere, link to the specific section that defines it, and give headings stable identifiers so renaming a heading does not break those links.

Corrections

1. In teaching material, a rejected alternative that readers will naturally try may be shown, with the reason it falls short; one passage also described a longer working alternative before choosing the shorter one. The evidence does not show that other alternatives should be left out. [revised]
2. Prediction prompts need no fixed quota: one page about surprising behaviour carried three, and other pages carried one. [revised]
3. A one- or two-sentence gloss of background knowledge at the point of first use, with an outside link, is supported alongside a plain link-out. The evidence covers only brief glosses of general-language features, not longer teaching of background. [revised]
4. Use one running example domain per chapter or section, and evolve that same example across consecutive pages; change the domain when the subject changes, rather than holding a single domain across the whole set.

### 2. Baseline rules broken

- SKILL.md:45 — link text must describe its target, not be a bare pointer word.
- SKILL.md:45; reference-and-guides.md:56 — images need text alternatives.
- SKILL.md:38; SKILL.md:57 — one term per concept, and a change of name or wording must be carried to every place that uses it.
- SKILL.md:39 — state the version a page is true for, especially where syntax is version-specific.
- SKILL.md:64 — samples must be checked against what the text claims, including sample data being internally consistent.
- SKILL.md:52 — placeholder values must come from reserved, clearly fake ranges, not live ones (low severity).
- SKILL.md:54; books-and-video.md:43 — avoid figurative phrasing in explanatory prose, for non-native readers (a deliberate voice choice; cost beyond the skill's rationale is not evidenced).

### 3. Confirmed

- SKILL.md:66 — walk the page literally from a clean state.
- teaching.md:31 — show a common error on purpose so readers recognise it.
- teaching.md:28 — name the tempting wrong mental model.
- teaching.md:17; teaching.md:29 — highlight the new lines and re-show the full file at checkpoints.

### 4. On mixing modes

Pages combined explanation, procedure and definition, while exhaustive facts, setup and option catalogues were linked out or placed on separate pages. It is not a correction to the one-kind-per-page rule: each page served one reader job, the explanation was tied to what the reader had just done or fenced as skippable, and the rule survives if the mode is judged by the reader's job rather than by the kind of sentence.

---

## Source B

### 1. Rules

Missed principles

1. Open each lesson with the list of concepts it teaches, and close each part of the series with a recap that reuses those same items in the same words, so each idea is named twice and the reader can check it against what they did. [revised]
2. When you introduce a feature, first show the situation without it (repetition, near-duplicates, or a pain the reader can see), then show the feature resolving it, so the reader knows what problem it solves before learning how it is written.
3. Where a feature has a likely misuse or a close alternative, say when to use it, when not to, and what to use instead. When several options work, name the one you recommend and say whether the others are equivalent. Answer doubts readers bring from outside your docs under a heading phrased as the reader's own question. [revised]
4. After the current approach, give older or deprecated forms a short, clearly labelled place, enough to recognise them in existing code. Where an older edition of the docs exists, point to it. [revised]
5. Make each sample itself follow accessibility practice, and add a one-clause reason when the choice is not obvious. [revised]
6. State that a guide covers the common path only and say where the rare cases are documented. Start each page and each section with the simplest, most common case, then advance, instead of appending edge cases.
7. Set a page-length limit and split pages that exceed it. A stated limit alone does not hold: pages well over it persisted. [revised]
8. Put each sentence of the prose source on its own line. The evidence is a stated convention applied unevenly, with no reason or measured effect given. [revised]
9. Declare that wrong samples and typos are documentation bugs, and put a one-step route from every page to the editable source. [revised]

Corrections

1. Scope a running example to a group of pages that build on each other. Pages that don't build on each other may each use their own small scenario. Don't force a single scenario on an entire set.
2. When docs are published once per release, link to the alias that tracks the same release for current-release material; the only pinned links found were stale or arbitrary, while deliberate pointers to older editions exist for legacy content. The evidence does not show when pinning is right. [revised]
3. A warm, lightly humorous voice is a legitimate deliberate choice in teaching material; in the source it was absent from reference-like pages. The evidence says nothing about translation. [revised]
4. Explanation and task steps may share a page if headings mark the shift and the order runs from simplest to most advanced. A lesson may include a short explanation of what it just built, if it links to the full treatment. Keep exhaustive lookup tables out of such pages.

### 2. Baseline rules broken

- SKILL.md:64 — samples must be run or checked; the source had mismatched syntax and mismatched values.
- SKILL.md:66; SKILL.md:67; SKILL.md:70 — prose, summaries and file names must match the code they describe.
- SKILL.md:64; SKILL.md:67 — one release should not mix two vintages of the same interface across samples and output.
- SKILL.md:44 — warn before the hazard, not after it.
- SKILL.md:41 — drop filler and reassurance words.
- SKILL.md:39; teaching.md:14 — state prerequisites and versions.
- SKILL.md:43 — keep commands, prompts and output out of one copyable block (the source was inconsistent).
- SKILL.md:70 — avoid content that goes stale for avoidable reasons; the source documents someone else's changing interface step by step with screenshots.
- teaching.md:27; teaching.md:33 — give the learner practice: recall checks and exercises with solutions.
- reference-and-guides.md:50 — one task per page and split by task; several pages ran far over the source's own length limit.

### 3. Confirmed

- SKILL.md:50 — generate reference from source.
- SKILL.md:53; books-and-video.md:25 — use real output and tested code.
- SKILL.md:52; SKILL.md:43 — use obviously fake placeholders.
- teaching.md:31 — trigger and read an error on purpose.
- teaching.md:38 — supply bulky assets instead of making learners type them.

### 4. On mixing modes

Explanation, task steps and short catalogues shared pages, with headings marking each shift, an order from simplest to most advanced, and brief explanation placed next to what was just built with a link to the full treatment. It counts as a correction to the wording of the one-kind-per-page rule only, and the claim that this does no harm is inferred from how consistently it is done, not measured; mixing exhaustive reference into guides was not seen and is not a correction.

---

## Source C

### 1. Rules

Missed principles

1. Where the tutorial allows, introduce a tool right after the reader has met the problem it solves: show the awkward result or the duplicated code first, then give the fix, so the new thing arrives with a reason. [revised]
2. When a convenience hides several steps, teach the long way first, then show the convenience labelled as doing the same thing, and tell the learner the order is deliberate.
3. After a code sample, list only the lines or choices whose purpose isn't obvious, one short point each, and say the rest is self-explanatory, instead of narrating everything. A very small example may instead be walked through line by line. [revised]
4. Tell readers how the documentation is organised: say in a sentence per kind of page what need it serves, and add a feature-by-feature index that lists the guide, the task pages and the lookup pages for each feature side by side, alongside any navigation by page type.
5. On each part of a multi-part series, say where to get help. Give separate routes for questions, bugs and security problems on a help page, with a private channel and a request not to post publicly for the security route. [revised]
6. Where the docs present a safeguard, filter or check as protecting the reader, state what it does not catch or guarantee, including that a test run may miss cases. [revised]
7. Do not copy another party's setup steps when they change on their own schedule: write only the points where your product meets theirs, link to their instructions, and say that this is why.
8. Keep change-history notes in short, self-contained blocks that can be deleted without touching the surrounding text, keep version numbers out of the main prose, and remove the notes after a fixed number of releases.
9. When there are several ways to do something, present them from least to most effort or control and say when to move to the next; in guides for extension points, order lists of hooks by importance and say so. [revised]
10. When a page continues or borrows an example from earlier pages, state the starting state it assumes, show that state if it is complex, and flag every addition that earlier pages did not contain.
11. For readers who are still evaluating, offer one tour page that walks the whole path in a single pass, says openly that it is neither a tutorial nor a reference, and links each stage to its depth.
12. When readers who build on top of your product need different steps from those who only use it, give them their own labelled section, and include a way for their code to detect which capability or version is present.
13. In teaching and community pages, write as one person to another: address the reader, pose the problem before the answer, and prefer concrete statements to piled-up superlatives; after any editing or smoothing pass, check that these qualities survived. Keep lookup pages plain.
14. Use singular they for hypothetical people and avoid gendered pronouns.

Corrections

15. A teaching page may carry short, clearly set-off asides outside the numbered path, placed after the reader has acted, that give the reason for a design or name a tempting alternative and why not; the reader is never asked to decide, and skipping every aside must not break the flow.
16. Lookup pages may carry brief warnings and recommendations, stated plainly with the reason, at the exact place a reader would go wrong. [revised]
17. Not every lookup entry needs its own example: give one where the behaviour is surprising, and for thin entries that are only a signature or an option list, point to the worked example in the guide and say so.
18. State each cross-cutting fact once and link to it, but a short gotcha that bites at the point of use may be repeated on every page where readers arrive without passing through the overview; the copies can drift apart. [revised]

### 2. Baseline rules broken

- SKILL.md:41 — drop words that minimise difficulty or effort.
- SKILL.md:70 — keep versions out of running prose; one page fixed a version in a sentence.
- SKILL.md:43 — keep a command and its output out of one copyable block (the source was inconsistent).
- teaching.md:17 — give the learner a known-good state to compare against or return to, such as a commit or tag per step.
- SKILL.md:66 — nothing a page promises may be missing; a promised list was absent.

### 3. Confirmed

- SKILL.md:46 — reuse one running domain across related pages.
- reference-and-guides.md:77 — index troubleshooting by the exact text a reader sees.
- SKILL.md:41 — drop minimising words (the source's own style guide asks for the same).
- teaching.md:15 — give an early win.
- reference-and-guides.md:12 — state the empty or null return case.
- SKILL.md:70 — keep versions out of prose, using a substitution.

### 4. On mixing modes

Several task pages combined background explanation, steps and a catalogue of methods under headed sections, in places where no other page defines the interface; elsewhere worked examples and lookup sat on separate pages that link to each other. It is not a correction: the source's stated intent and its separated pages agree with the rule, and the mixed pages are bounded by headings with the lookup part always after the steps.

---

## Source D (two files, one source)

### 1. Rules

First file

Missed principles

1. Begin every page, whatever its type, with a short statement of what the reader will know or be able to do after reading it.
2. Use a small fixed set of labels for asides and give each one a single, stable meaning based on consequence: needed to understand, optional extra, and harmful if ignored.
3. When a call is shorthand for something lower-level, show next to it what it produces or expands into, so the reader can check their mental model.
4. Let your examples and ordering teach the currently preferred approach. Put superseded approaches later, label them as such, and name what replaces them.
5. Where a feature gives a guarantee that some operations bypass, list the operations that trigger it, the ones that silently skip it, and any mechanism outside the feature that has to complement it. [revised]
6. Where two features overlap, include a section on choosing between them that states the criteria; at minimum state the one difference that matters.
7. In the opening of a page, say what the subject is not and name the nearest neighbour it is likely to be confused with.
8. In a documentation set that has several versions, make cross-links land on the same version the reader is currently reading; pin to a specific version only when the sentence is about that release.
9. Mark advanced or optional sections as such, inside the page, so readers who don't need them know they can skip them.
10. Start every code listing that represents a file with the file's path, so the reader never has to guess where it goes.

Corrections

11. A reference page may carry a short verdict next to an option that is rarely appropriate. [revised]
12. The requirement is that whatever the reader copies must work. Where the publishing tool excludes prompts from copying, prompts may stay in the block; where it cannot be relied on, keep commands in blocks of their own. The evidence does not show how output shown under a command is treated. [revised]
13. Declare near the start of a page the example domain it uses. Keep one domain through a worked sequence. Across separate pages, or when a concept needs a different shape of data even within one page, change the domain. [revised]
14. Be exact about the contract; do not commit to exact incidental values you want the freedom to change, and say what behaviour callers may rely on. [revised]

Second file

Missed principles

1. Define a small, fixed set of callout types by what skipping each one costs the reader (understanding, optional depth, breakage), and use them consistently so readers learn to trust the signal.
2. Start every page, whatever its kind, with a brief list of what the reader will know or be able to do afterward. [revised]
3. When defaults or behaviour change across releases, record the history twice: beside each setting, and as a per-release roll-up, so both what changed for this setting and what changed in this upgrade are one lookup.
4. Where several approaches solve the same problem, add a decision aid keyed to the reader's circumstances, so their need maps to a recommended option. [revised]
5. State boundaries explicitly: what the page leaves out, which environment it assumes, and what the documented tool does not do or guarantee, naming who owns the remainder. [revised]
6. Where a documented default or built-in list can be inspected, give the command that shows the live value in the reader's own system. [revised]
7. When showing an incorrect approach, mark it as incorrect inside the code block itself, so a copied snippet still carries the warning.
8. When a convenient call hides what actually happens, show the lower-level result it produces, next to the call.
9. Document failures that produce no error (silent no-ops, dropped work, quiet fallbacks) explicitly where they occur. [revised]
10. If a table or list is a selection, say it is a selection and point to the complete source; don't let a partial list read as complete.
11. When you remove documentation for a retired feature, leave a short pointer to the archived, version-specific documentation and any migration note.
12. Write illustrative snippets in the currently recommended style, and order alternatives so the favoured one comes first; examples teach habits.
13. Describe behaviour as the user experiences it in a typical full setup, and say when behaviour changes because of the surrounding context, rather than describing a component alone.
14. Give reviewers a rendered preview of every documentation change, not just the diff.

Corrections

1. Keep reference neutral by default, but when a wrong choice is costly or non-obvious, put a one-sentence recommendation and its reason right next to the item.
2. Be exact about the contract; do not commit to exact incidental values you want the freedom to change, and say what behaviour callers may rely on. [revised]
3. The real requirement for command examples is that what gets copied is runnable. Separate blocks are the safe default; showing prompts and output together is acceptable when the publishing tool excludes prompts from copying. The evidence does not show whether output is excluded. [revised]
4. For mixed audiences, don't omit definitions of general terms; give a one- or two-sentence gloss, set apart from the main text where the page's conventions allow so experienced readers can skip it. [revised]

### 2. Baseline rules broken

- SKILL.md:70; SKILL.md:64; SKILL.md:65 — keep versions out of prose and check them; versions stated in different places disagreed.
- SKILL.md:64; SKILL.md:65 — samples and commands must be checked; small errors that a run or a re-read would catch (misspelled names, wrong status or helper named in prose, wrong argument).
- reference-and-guides.md:23 — state shared steps and cross-cutting facts once and link; the same setup instructions and the same generated-method lists were pasted several times.
- teaching.md:18 — show recovery where a step commonly fails; the tutorial gave expected results but almost no recovery paths.
- SKILL.md:52 — placeholder values must be reserved, clearly fake ones, not live provider addresses.
- SKILL.md:41; SKILL.md:42 — drop claims of ease, and use present tense.
- SKILL.md:50; SKILL.md:70 — docs must not contradict each other or keep statements that a newer page says are stale.
- SKILL.md:68 — internal links must resolve; one pointed to a page name that does not exist.
- SKILL.md:64; SKILL.md:66 — samples must run and match their text; unclosed output tags, a missing separator, and a method used but never defined.
- SKILL.md:41 — drop filler words.
- SKILL.md:36 — long procedures should be numbered, one action per step; several guides narrated them as prose.

### 3. Confirmed

- SKILL.md:38 — one term per concept.
- SKILL.md:50 — generate reference from comments in source.
- SKILL.md:58 — give the why in a sentence rather than a bare rule.
- SKILL.md:45 — descriptive link text, extended to in-page links.
- teaching.md:15 — an early win within the first minutes.
- teaching.md:31; teaching.md:18 — show the failure and its exact text where it occurs, then the fix.
- SKILL.md:39 — state prerequisites and link rather than re-teach.
- reference-and-guides.md:39 — a deprecation names its replacement.

### 4. On mixing modes

Both files saw pages that combine explanation, procedure and lookup under headings that name the kind of text, while exhaustive lookup, setup and cross-cutting topics were moved to other pages. Neither counts it as a correction: labelled sections meet the rule's purpose, the evidence supports only that sections may change kind under clear labels (the rule is better read at section level than page level), and there is no data on reader outcomes.

---

## Source E

### 1. Rules

Missed principles

1. Treat failure as a teaching step. When a lesson depends on something being rejected, crashing, or silently wrong, show that version on purpose. Tell the reader beforehand that it will not work, and distinguish rejected before running, fails while running, and runs but gives the wrong result. Show the real diagnostic from a real run, then derive the fix from it. Don't limit this to one example per lesson.
2. In build-up sections, show the desired end usage, or a test that fails, before the implementation, so the build-up has a visible target to move toward. [revised]
3. Give long works a reader-facing guide: who it is for, who it is not for and where those readers should go instead, reading paths (including skipping ahead and coming back), a short paragraph per part describing it, and a legend for any markers the text uses. [revised]
4. Alternate concept sections, which use small disposable examples, with integration projects. A project can open by listing the earlier parts it combines. [revised]
5. Teach diagnostics as a skill: point at the part of a long message that matters, show only the relevant lines when output is long, and say when a tool's own suggested fix is wrong or incomplete and why. [revised]
6. For reference entries, document the caller's contract. State when a call terminates rather than returning an error, and list the invariants the caller must uphold, separately from recoverable errors.
7. For any content that cannot be generated, such as pasted output or a value repeated in several files, leave at that spot either the exact steps to regenerate it or the list of other places that must change with it.
8. Mark a term typographically at the point where it is defined, in one consistent style. Prefer not to attach ordinary-language endings to code-formatted text. [revised]
9. Number only the listings that later text refers back to. A caption can say what the listing shows, including that it does not yet work. [revised]
10. When a heading is renamed, keep its old anchor in place with a note not to remove it.
11. Publish the revision policy: when large revisions happen, which kinds of change are accepted between them, and how long a contributor should expect to wait. In the evidence this is tied to a printed snapshot and to the described product's own edition cycle. [revised]

Corrections

1. Using a not-yet-taught idea is acceptable. Using it silently is not. Each forward use should say how much the reader needs to know now and where the full treatment comes.
2. Name difficulty honestly. Say that a topic usually takes time, give the specific reason, say that struggling is normal and not a verdict on the reader, and then give the tools. Avoid only the vague apology.
3. Background that the topic's own explanation depends on, that the target reader may lack and that is small, can be taught in place in a bounded, titled aside that says what is left out. Link out for skills the reader is already assumed to have.
4. In learning material, show the two or three alternative forms the reader will meet in other people's work. State which is preferred and why, and keep the alternatives in bounded asides.
5. Numbered steps suit plans and rules. In narrative tutorials, carry the sequence with one change per listing, and show the expected result after each run.
6. Where output may be printed or read offline, references must work without a link. Write the part and its title in the prose, mark links that print should drop, word link text so it still reads when shown as text plus address, and generate the numbers so they cannot drift.
7. Everyday analogies appear as entry ramps, each followed at once by the literal rule. The evidence does not show whether leaving their limits unstated causes misconceptions (lower confidence). [revised]

### 2. Baseline rules broken

- teaching.md:33 — exercises need checkable outcomes, solutions and difficulty; the source had none.
- SKILL.md:53; SKILL.md:64 — pasted output must match the code and the version it claims; several blocks had drifted.
- SKILL.md:67; SKILL.md:68; teaching.md:41 — prose, code and cross-references must agree; several named the wrong listing, function or section, and some links had no target.
- SKILL.md:41 — drop reassurance words, especially in the hardest section.

### 3. Confirmed

- books-and-video.md:45 — show the wrong or naive version first.
- books-and-video.md:46 — foreshadow and recall.
- teaching.md:27 — reuse earlier examples for spaced practice.
- books-and-video.md:25; books-and-video.md:30 — extract code from tested, complete projects.
- reference-and-guides.md:31 — reference examples that run as tests.
- teaching.md:26 — predict or experiment prompts used sparingly.
- teaching.md:48 — map to what the reader already knows and flag the differences.

### 4. On mixing modes

One chapter combined guided steps, a background explanation and a lookup list, while pure lookup sat in appendices, exhaustive reference was linked out, and explanation that interrupts the teaching line sat in titled asides. It is not a correction: the mixing is bounded and signposted and exhaustive reference goes elsewhere, which is what the rule asks; at most, in a long teaching work the unit the rule governs is the passage rather than the page, and there is no reader data either way.

---

## Source F

### 1. Rules

Page structure and navigation

1. Before you write a page, find the closest existing page of the same kind and follow its structure. Related pages share structure beyond what any template requires. [revised]
2. Give every page a declared type. Keep a template with required sections in a fixed order for each reference type, and define the navigation type (a short summary that opens a list of links) and the short definition entry too, with a size limit that triggers converting an overgrown entry to a fuller conceptual page. Long-form guides in the evidence lacked a template and were the less consistent half. [revised]
3. A hub page lists every child with the same summary sentence the child opens with, and the two are kept in sync. Put explanation shared by many children on the hub and link to it instead of repeating it. [revised]
4. When entries look alike, each one states the condition that separates it from its nearest alternative and links to it. The hub summarizes the contrast in one line per entry.
5. For pages meant to be read in order, put previous and next links at the top and bottom of every page in the sequence, including the later pages.
6. Do not give sibling pages near-identical text and examples. Write substance each page owns, so a search tool and a reader can tell them apart. Do not publish stubs.
7. A page may hold more than one kind of content when each kind sits in its own labelled section in a fixed position, as reference entries do; long material of another kind goes on its own page. Interleaving kinds inside a procedure was not seen. [revised]

Headings, lists, links and wording

8. Never leave a lone subsection, never put a heading directly under a heading with no text between, and split the page if you need a fourth level. Open every list with a sentence of context. Make titles specific, single-purpose, parallel at each level, free of the parent's words and free of a leading article. [revised]
9. Do not refer to location with words like above, below, here or right. Name the target by its title or by what it contains, because layout differs by device, by assistive tool and by translation.
10. Use neutral wording about people: avoid gendered pronouns when gender is irrelevant (prefer rewriting so no pronoun is needed), avoid loaded terms and violent idioms.
11. A related-links section is a list of terms, not sentences. Link text equals the target's title. Put your own docs before outside ones and reference before guides, and give each outside link its source and year. Prefer links you can maintain, avoid link shorteners and self-promotion, and disclose any relationship to a target. [revised]
12. Keep version and support information out of running prose. Hold it in one structured place per page, ideally generated from a data source, so it is corrected once.
13. A lead is one or two short sentences saying what the thing is and what it depends on, then links outward. A one-clause lead is too short and a long one equally wrong; a key caveat can go in the second sentence. [revised]
14. Reference entries may carry guidance on which sibling to use and on hazards, stated directly; the neutrality the source enforces concerns vendors, not advice. [revised]
15. List the errors a feature raises under its own contract. Leave out errors caused by caller-supplied code or wrong-type arguments. Put fixes on a separate troubleshooting page. [revised]

Examples and code

16. Give every example a title that says what it demonstrates (never a bare number or generic label), a sentence before it saying what it does and why, and an explanation after it of the result. Split long examples into pieces with prose between them.
17. When you show a discouraged pattern, mark it visibly as wrong next to the right version. [revised]
18. Write every example as code that will be copied into production. Model current, safe, non-deprecated practice. Depend on as little outside the subject as you can, and name which parts belong to which component when you combine several. If an example is not production-grade, say so both in a code comment and in the prose.
19. A snippet may be partial if it is labelled partial and its omissions are written as comments, so the code stays valid when copied. [revised]
20. Show the output of logging calls as a trailing comment on the line that produces it. The evidence says nothing about command-line sessions. [revised]
21. In example code, comments should not restate what a line plainly does, and a well-named call needs no comment. [revised]
22. Let an automatic formatter settle code layout, and use the style guide only for the rules a formatter cannot enforce.

### 2. Baseline rules broken

- SKILL.md:46 — use meaningful domain names in examples rather than placeholder names (reference examples demonstrating a mechanism make this partly defensible).
- SKILL.md:38; SKILL.md:67 — one term per concept, including parameter names inside one page.
- SKILL.md:64; SKILL.md:67 — examples must not contradict sibling pages, and output formats must match across pages.
- SKILL.md:40 — be specific; one precise page used loose, inconsistent wording about the same behaviour.
- SKILL.md:70 — keep time-bound claims out of prose.
- SKILL.md:39; teaching.md:8 — state prerequisites; the source's own guide requires them and almost no guide page did.
- SKILL.md:41 — drop filler that tells the reader the answer was obvious.
- SKILL.md:38; reference-and-guides.md:23 — define a concept once; one concept was defined twice in different words.
- SKILL.md:57; reference-and-guides.md:88 — keep docs in step when a related page changes; the guide lagged the reference.

### 3. Confirmed

- SKILL.md:46 — prefer meaningful names over placeholder names.
- SKILL.md:64; SKILL.md:72 — run and test every example, and do not claim tested what was not.
- SKILL.md:70 — keep supported versions out of prose.
- SKILL.md:54 — tie wording choices to translation.
- reference-and-guides.md:23 — move description shared by many pages to the parent and link to it.
- reference-and-guides.md:29 — populate status and compatibility information from data, not by hand.
- SKILL.md:37 — a runnable example near the top for readers who will not read the whole page.

### 4. On mixing modes

Reference entries held lookup, explanation and recipes in labelled sections in a fixed order, and some guide pages carried lookup tables, while long-form teaching, exhaustive detail and navigation sat on separate pages. It counts as a narrow correction: the rule should read one dominant kind of content per page, with other kinds confined to labelled sections in a fixed place, because a reader who lands on one entry from search needs the caveat there; the rule's purpose survives, since no interleaving inside a procedure was seen.

---

## Source G

### 1. Rules

Missed principles

1. When a lesson leaves a feature out on purpose, it can say so in one sentence where the reader would look and link to the exact section holding the rest; the evidence shows this for some omissions while others pass without mention. Tell experienced readers which sections to read closely because their habits will mislead them, and tell readers which sections they can skip. [revised]
2. Where a reference entry's behaviour departs from conventions readers bring from standards or neighbouring tools, record it in a fixed section of the entry, and warn explicitly where a habit from elsewhere will quietly do something different. All entries of that kind that were read had the section. [revised]
3. Build reference examples as a catalogue: one per distinct form or option, each introduced by a plain sentence stating its goal, each runnable on its own, ordered from the plain case to the subtle one. One or two examples per entry is too few when an entry has many forms.
4. In examples, show the input data, the operation applied and the exact result together, so the reader can verify the result by hand without guessing at inputs.
5. Show the tempting wrong form next to the right one, mark it plainly in the code, and say in the next sentence why it fails. Do this in reference and guide material too, not only in lessons.
6. When an outcome is decided by layered rules, write the rules as an ordered procedure with the tie-break order explicit, then give worked examples that name the step that decided each result.
7. Keep shared machinery in one place and link to it, but repeat the costliest trap wherever a reader first meets the feature, in a length suited to that page: a clause in a lesson, a paragraph in a guide, an exact rule in reference. Near-verbatim copies also occurred and can drift apart. [revised]
8. Match the layout conventions of the tools your readers already use, not only the conventions of your own doc set, so lookup habits transfer.

Corrections

1. Reference voice should be neutral by default, but a short piece of advice with its reason sits beside the rule it qualifies, inline or in a tip. [revised]
2. Do not promise an exhaustive error list with exact message text in reference. Document the conditions that change what the reader must do or that will surprise them, including cases that look like failures but are not, at the rule where they arise; where a format users parse is stable, give it. Put verbatim message text where readers meet it, in lessons and guide chapters. [revised]
3. Keep one running example domain within a learning path. When a concept needs specific data, use a small purpose-built dataset shown inline. Make reference examples self-contained so they do not depend on the lesson's data.
4. A lesson may show alternatives, each labelled with which to prefer and why, as long as none derails the main path. The no-choices rule applies to the path the learner follows, not to what they are told exists. [revised]
5. Mentioning versions in prose is acceptable and useful when the note says what changed and what an upgrader should do, set apart beside the rule it affects. Time-relative wording with no version attached was common and leaves the reader unable to tell whether the statement still holds; avoid it. [revised]

### 2. Baseline rules broken

- SKILL.md:66; teaching.md:17 — a lesson must not depend on data the reader cannot create from the text.
- teaching.md:18 — say how to recover at the point of failure; recovery was delegated elsewhere.
- SKILL.md:53; SKILL.md:70 — do not hard-code environment output that goes stale.
- SKILL.md:41; SKILL.md:54 — drop jokes, idioms and filler that a non-native reader trips on.
- reference-and-guides.md:16; reference-and-guides.md:39; SKILL.md:70 — attach a version or date to any time-relative statement.
- reference-and-guides.md:37 — a parameter entry must say what the parameter is, not restate its name.
- teaching.md:33 — exercises need a checkable outcome.
- SKILL.md:70; reference-and-guides.md:23 — avoid duplicated text; one passage was copied near-verbatim between a chapter and a reference page.

### 3. Confirmed

- reference-and-guides.md:21 — one template for entries of the same kind, with inapplicable sections omitted.
- reference-and-guides.md:23 — define shared material once and link to it.
- reference-and-guides.md:29 — generate where possible.
- SKILL.md:45 — put exact error strings in the text so they can be found.

### 4. On mixing modes

Reference entries held a processing explanation and recipes inside labelled, fixed-position sections, and a lesson chapter held a lookup catalogue, while pure lookup tables were kept separate and explanation was placed after them under its own heading. It is not a correction: labelled, fixed-position sections meet the rule's concern that a reader can tell what kind of text they are reading, and the word page in the rule is at most stricter than practice, which calls for rewording rather than correction.

---

## Audit

Counts are rules, counted as listed in each file. A rule that lost or gained an unsupported clause is counted as revised, not removed. No rule was removed in any source, because every rule had at least part of its claim in the evidence; what failed was scope, a causal clause, or a stated reason.

Total: 127 rules checked (A 15, B 13, C 18, D 28, E 18, F 22, G 13); 62 revised (A 5, B 9, C 7, D 13, E 8, F 13, G 7); 0 removed.

### A: 5 revised, 0 removed (of 15)
- Missed 3: dropped a causal claim about reader behaviour that the evidence (marker use in many files) does not show.
- Missed 10: dropped history from the optional-depth list; the evidence shows internals and rationale only.
- Correction 1: the evidence is one passage showing a failed attempt and a longer alternative; the leave-out-the-rest sentence had no support.
- Correction 2: the claim tying prompt count to how counterintuitive the topic is went beyond one page with three prompts and others with one.
- Correction 3: the evidence is brief glosses only; the do-not-teach-at-length prohibition was not shown.

### B: 9 revised, 0 removed (of 13)
- Missed 1: recaps exist per part, not once at the end of the series.
- Missed 3: not every feature gets this treatment, and the question-and-answer form was only headings phrased as questions; also removed a source-derived example.
- Missed 4: the evidence supports recognition of older forms, and a pointer to older docs on one page only.
- Missed 5: the evidence is accessibility only; the other domain and the copying rationale were not shown.
- Missed 7: the source breaks its own limit on several pages, so a stated limit alone is not shown to work; the many-short-pages preference had no evidence.
- Missed 8: the evidence is a stated convention applied unevenly; the stated rationale was not in it.
- Missed 9: the evidence shows an edit route on each page and no report button.
- Correction 2: only stale or arbitrary pinned links were found, and pointers to older editions exist deliberately, so pin-only-in-archives was not shown.
- Correction 3: the translation condition had no evidence in either direction.

### C: 7 revised, 0 removed (of 18)
- Missed 1: four tutorial instances do not show that every new thing arrives with a reason.
- Missed 3: one page walks a small example line by line, and the avoid-explaining-in-comments clause had no evidence.
- Missed 5: the help box appears on each part, while the separate routes live on a help page; no reason for the private route was given.
- Missed 6: four instances do not support any statement, and warnings people rely on were not shown.
- Missed 9: the alphabetical-for-lookup clause had no evidence in this source.
- Correction 16: the keep-persuasion-in-guides clause had no evidence.
- Correction 18: the evidence names a drift cost; the identical-and-searchable clause was not shown.

### D: 13 revised, 0 removed (of 28; first file 5 of 14, second file 8 of 14)
- First 5: three features show it, not any guarantee.
- First 11: the default-pick condition and the linked-reasoning clause had no evidence.
- First 12: only prompts, not output, are shown as excluded from copying.
- First 13: the evidence shows a domain announced on one page and domains changing within a page, contradicting keep one per page.
- First 14: the evidence is about not committing to exact incidental values, not being vague.
- Second 2: the decide-in-seconds claim about readers had no evidence.
- Second 4: the name-the-default clause had no evidence.
- Second 5: some boundary statements sit mid-page, so up front was not shown.
- Second 6: several defaults, not every one, carry an inspection command.
- Second 9: the evidence shows these failures documented, not that they are as visible as errors.
- Second corrections 2: same as first 14.
- Second corrections 3: same as first 12.
- Second corrections 4: only one of four glosses was shown set apart.

### E: 8 revised, 0 removed (of 18)
- Missed 2: the evidence is a target for a section, not for every step.
- Missed 3: the evidence is a paragraph per part, not one paragraph; the temperament framing was not shown.
- Missed 4: only one project chapter was shown listing earlier parts.
- Missed 5: the evidence trims to chosen lines and points at the important part, not a single line.
- Missed 8: the source's guidance says prefer, not never.
- Missed 9: one caption was shown, not every caption.
- Missed 11: the evidence ties timing to editions, not a frequency, and the matters-most claim was inference.
- Correction 7: no evidence on whether unstated limits cause misconceptions.

### F: 13 revised, 0 removed (of 22)
- 1: the evidence is copy the structure; phrasing habits and the stated-reason clause were not shown.
- 2: the source's own long-form guides have no template, so every type has a template was contradicted.
- 3: the evidence says keep in sync, not a single source.
- 7: the evidence shows labelled fixed-position sections, so the dominant-kind and only wording went beyond it.
- 8: only lists are said to need a lead-in sentence.
- 11: the order-within-a-group clause had no evidence.
- 13: the must-state-the-caveat claim rests on one page; the guideline asks for what it is and what it depends on.
- 14: the neutrality enforced is about vendors, and keep-longer-advice-in-a-guide had no evidence.
- 15: the fixes-on-another-page claim is supported, the causes-on-the-entry claim is not.
- 17: say-why and the cannot-be-mistaken guarantee had no evidence.
- 19: the require-completeness-only-where-run clause had no evidence.
- 20: the second sentence concerns command sessions, which the evidence does not cover.
- 21: the evidence is negative only, and not never.

### G: 7 revised, 0 removed (of 13)
- Missed 1: some omissions pass without mention, and the evidence says skip-ahead, not newcomers.
- Missed 2: the evidence is one kind of entry, not every documented unit.
- Missed 7: the evidence includes near-verbatim copies; rewrite-not-paste was not shown to help.
- Correction 1: the cost claim had no evidence, and not every piece of advice sits in a labelled area.
- Correction 2: troubleshooting and a stable code were not in the evidence.
- Correction 4: the readers-will-meet-them motive was not in this source's evidence.
- Correction 5: the new-word example and the real-rot claim were inference; the evidence is the frequency of unanchored time words.

### Other notes
- Source D's two files are counted together; the first-file and second-file lines above show the split.
- Wording in several unrevised rules was changed only to avoid identifying the source (examples, quoted words, technology terms); the meaning did not change and these edits are not counted.
- Source B's item about breaking its own style guide on outside links was left out of section 2: its point is a breach of that source's own guide, and no skill rule covers outside links.
- Two skill citations in the comparison files did not match the skill's line numbers by my count of the files as I wrote them. I used books-and-video.md:25 for tested code, where one file cited :26, and reference-and-guides.md:77 for indexing troubleshooting by exact text, where one file cited :78. I used teaching.md:38 for the item that had no line cited.
