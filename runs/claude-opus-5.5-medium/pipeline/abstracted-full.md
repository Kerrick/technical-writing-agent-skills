# Abstracted deltas, checked against their evidence

Seven documentation sources were each compared against a baseline technical-writing skill. They are labeled A to G here. Each source has four sections:

- **Rules:** the rules abstracted from the comparison, checked against the evidence behind them. A rule marked [revised] was rewritten to match that evidence. A rule marked [anonymized] was reworded only to remove material that would identify the source. Unmarked rules are unchanged.
- **Baseline rules broken:** places where the source breaks a rule the skill states. Each is given as the skill line (file:line) and the rule in general terms.
- **Confirmed:** skill lines the source supports.
- **On mixing modes:** what the comparison concluded about pages that combine tutorial, how-to, reference, and explanation, measured against `SKILL.md:44` ("When a page wants to do two jobs, split it and link the halves").

Skill paths are relative to the skill folder.

---

## Source A

### Rules

1. In the middle of an explanation, stop and ask the reader to predict what will happen before you show it. Save prediction for more than the exercises at the end.
2. Give learners a named reasoning procedure they can use to work out behavior themselves. Use it by name again in later lessons and in worked solutions so it becomes habit.
3. When a feature seems like magic, show or assign a tiny working reimplementation of it, written without the library being explained and simplified enough to read in one sitting. [revised]
4. Open each multi-page unit with an overview that previews every topic in a sentence or two plus a small example. End it with two clear exits: work through the unit in order, or skip to the next unit if the material is familiar.
5. Between an exercise and its solution, offer a hint that points to the relevant idea without giving the answer.
6. In worked solutions, show more than one correct answer when there is one, and say what each version gains or costs.
7. In each exercise, tell learners how to check their own work: what to try, and what they should see. Where a fix could overshoot, also say what should not happen. [revised]
8. In working examples, invite the reader to change one specific value or line and watch what changes.
9. When two forms or concepts are easy to mix up, put them side by side in a table that labels which is right, or what distinguishes them.
10. Mark every incorrect or discouraged code sample as wrong inside the code block itself, so someone who copies only the block still sees the warning.
11. Tell learners which details they can leave partly understood for now, and that confusion on a first reading is normal.
12. Use "show the naive attempt, show it fail, explain why, then fix it" as a regular teaching move whenever a misconception is likely, not as a one-time device.
13. Pages in a deliberately ordered learning path may depend on earlier pages. Link back to what they rely on, and serve readers who arrive cold with a separate lookup section rather than by making every lesson self-contained.
14. Lessons that also serve as a later reference should end with a short bulleted recap of the rules covered, written to be scanned on return.
15. A teaching page may combine a walkthrough, explanation, and practice, as long as tangents and deeper material sit in clearly labeled asides that readers can skip.
16. Solutions can sit right after their exercise as long as the reader has to take a deliberate action to see them. Where the solution appears matters less than making the reader try first.
17. In step-by-step builds, show each step as a short snippet with the changed lines marked, and at regular checkpoints show the complete current code so readers who have drifted can catch up.
18. Use warning callouts both for serious risks and for common mistakes that fail silently. Keep each one to a single named failure so readers keep trusting them.

### Baseline rules broken

- `SKILL.md:73`: don't use words that suggest the task is easy.
- `SKILL.md:80`: don't use marketing adjectives.
- `SKILL.md:93`: pin versions in install commands.
- `SKILL.md:52`: verify facts against the source and record the version, so pages don't go stale or contradict each other.
- `SKILL.md:62`: run every example, so snippets don't fail when run or checked.
- `SKILL.md:48`, `references/learning-science.md:57-59`: write objectives as observable, checkable actions, not as knowing or understanding.
- `SKILL.md:102`: give a default path instead of presenting options as equals.
- `references/tutorials.md:39`: next steps point forward in the reading sequence.
- `references/explanation.md:13`: say where an analogy stops holding.

### Confirmed

- `references/books.md:9`
- `SKILL.md:62`, `references/books.md:77`
- `SKILL.md:103`
- `references/explanation.md:14`
- `SKILL.md:25`

### On mixing modes

Not addressed. This comparison has no "observed, not counted" position; it counts mixing as a correction instead (rule 15), on the condition that tangents sit in labeled asides readers can skip.

---

## Source B

### Rules

1. Order material so learners first do a task the laborious way and notice what it costs, then introduce the abstraction that removes that cost. End a unit on a known gap that the next unit fills.
2. When a step involves a judgment call (how much to verify, which level to test at, why order or element choice matters), explain the reasoning briefly at that step, not on a separate page.
3. Give refactoring steps a checkpoint: say in advance that nothing visible should change, and confirm it with the unchanged result and passing automated checks.
4. A running example can carry through a sequenced set of conceptual pages, not just a tutorial, as long as each page restates the starting code it builds on so a reader arriving from search can follow.
5. Use one consistent, visually distinct aside for optional depth: shortcuts, tangents, advanced options. Callouts aren't only for warnings. This keeps the main text on the common path without hiding detail from advanced readers. [revised]
6. When the material relies on features the stated audience may not know, even within a skill they're assumed to have, write a dedicated bridging page that teaches only those features, links out for the rest, and invites readers to return when stuck.
7. Build good practice, such as accessible markup, into ordinary examples, each with one line of reasoning. Attach caveats, such as a security risk, to the example that raises them. Don't save good practice for its own chapter. [revised]
8. Show the older forms of an API that readers will meet in existing code, clearly labeled as legacy, so they can recognize and translate them. Don't teach them as an option.
9. When a new name appears in code, say which package or module it comes from, and tell learners that knowing this is how they search for help and documentation.
10. When a section's readers arrive in different situations or with different goals, give it a landing page that sends each kind of reader to a different starting point. [revised]
11. Right after the first step likely to fail, point readers to where they can get help from people. Early in the documentation, tell them how to report a mistake in it. [revised]
12. Link background concepts only to authoritative, maintained sources. Don't link blog posts or talk slides; leave those to content aggregators. [revised]
13. Set a length budget for a page, roughly a couple of screens, and split by subtopic when a page goes over.
14. In plain-text documentation source, start each sentence on a new line, so a review diff shows only the sentences that changed.
15. One page can serve beginners and experienced readers if it starts with the simplest, most common use, moves steadily to advanced uses, and leaves rare edge cases to the reference.
16. A page about a single feature may combine a motivating worked example, a short explanation and a compact usage summary, provided every feature on the page follows the same internal order.
17. Let learners run into failures as often as each failure introduces the next concept. Stop when a failure teaches nothing new.
18. For short files, showing the whole file with changed lines marked can beat showing a fragment, because readers can bring the whole file back in line. Explain the marking notation once, the first time it appears. Once a diff would bury the change, show an excerpt instead. [revised]
19. Have learners type what's being taught, and hand them everything else (stylesheets, sample data, images) ready-made. Offer a complete reference solution up front as a lifeline for anyone stuck.
20. When commands, directories or tools use a different or older name for a concept than your prose does, state the alias once, prominently, then use one term consistently.
21. When the lesson is that a name is the author's choice, use a deliberately absurd name to make that obvious.
22. In a build-along tutorial, narrate shared work as "we" or "let's", and keep "you" for what the reader alone does or observes.

### Baseline rules broken

- `SKILL.md:60-62`, `SKILL.md:112`: run every example in order, so none has syntax errors or wrong expected output.
- `SKILL.md:111`, `references/api-reference.md:93`: verify every name against the code, so prose doesn't drift from the code it describes.
- `SKILL.md:52`: record the version documented, so sections aren't written against different eras of an API.
- `SKILL.md:62`, `SKILL.md:89`: trim long output with a visible elision, and show changes in context rather than as huge diffs.
- `references/tutorials.md:5`, `references/tutorials.md:46`: a quickstart is short, reaches one visible result, and follows one path.
- `SKILL.md:73`, `SKILL.md:80`: no minimizing words, no marketing adjectives.
- `SKILL.md:74`, `SKILL.md:101`: no boilerplate openings, no closing summaries that restate the page.
- `references/books.md:73`: avoid time-relative claims that age.
- `SKILL.md:104`, `references/style.md:44`: give meaningful images alt text.
- `SKILL.md:76`: use one term per concept.

### Confirmed

- `references/books.md:17`
- `references/explanation.md:14`
- `references/learning-science.md:25`
- `references/learning-science.md:65`
- `references/tutorials.md:48`
- `references/books.md:67`

### On mixing modes

Not addressed. This comparison has no "observed, not counted" position. It counts one pattern as a correction (rule 16): a single-feature page that combines modes in the same fixed internal order for every feature.

---

## Source C

### Rules

1. Write as one knowledgeable person talking to another. Address the reader, use "we" for work you do together, and allow a vivid comparison or a light joke when it makes an idea stick. Don't sand the prose into neutral summary. [revised]
2. Before introducing a feature, let the reader see the problem it solves in what they've built so far: an unhelpful output, duplicated code, a hardcoded value, a bug. Then present the feature as the fix.
3. When a convenience API wraps a common pattern, show the pattern written out first, then the convenience version, and say plainly that they do the same thing. Repeat that equivalence in the reference entry for the convenience API.
4. Wherever a reader is likely to try an alternative that doesn't work, or to doubt that a step is worth it, raise that thought in their words and answer it on the spot. This applies on every page type, including reference entries.
5. At the start of every part of a multi-part tutorial, tell the reader where to go for help if they get stuck. Where there are several places to ask, say which to try first. [revised]
6. When advice holds beyond the product being documented, say so, so readers know it transfers. [revised]
7. When an example is simplified for teaching (incomplete markup, a shortcut you wouldn't use in production, a partial implementation), say so next to it and say what real code should do.
8. Give every concept guide a short note at the top naming its reference pages, and give every reference page a note at the top naming the guide to read first.
9. Use one example domain throughout a feature's guide and its reference pages. Where later pages can build on the beginner tutorial's project, reuse it so readers don't have to learn a new domain.
10. Give readers an explicit map of the documentation: which kinds of page exist, what each is for, and where to start. Tell beginners how much ground the introductory material covers.
11. When a step depends on another project's software, document only how it connects to yours and link to that project's own instructions for the rest. Their steps will change on their schedule, not yours.
12. Keep FAQ answers to a sentence or two, then link to the page that holds the full answer, so the FAQ doesn't become a second copy that drifts.
13. Open a concept guide with the underlying technology or idea the reader already knows, then show what your tool adds on top of it.
14. Give every aside box a descriptive title that says what's inside, such as the question it answers, so readers can choose to skip it. Keep such boxes few. [anonymized]
15. Rationale doesn't always belong on a separate page. When a design choice will puzzle readers at a specific point (in a tutorial, a how-to, or a reference entry), give a few sentences of why right there, in a titled box or a single clearly marked paragraph that can be skipped. Move anything longer to an explanation page.
16. Numbered one-action steps suit procedures and how-tos. Narrative tutorials can instead give each action as its own short paragraph, followed by the code for it and then what it means. Choose by page type, not one rule for every page.
17. Write version-change notes as self-contained blocks: "added in" at the top of the entry, "changed in" at the end of the section. They must be removable without editing the surrounding text. Remove them after a fixed number of releases, and avoid version numbers elsewhere in body text. [revised]

### Baseline rules broken

- `SKILL.md:73`: cut minimizing words such as "easily" and "simply".
- `SKILL.md:91`: use realistic domain names in examples, not placeholder names.
- `references/how-to-guides.md:22-24`: end a how-to with a way to verify the result.
- `references/api-reference.md:104`: a deprecation notice says when the item will be removed.
- `SKILL.md:93`: pin versions in third-party install commands.
- `references/tutorials.md:54`: end each tutorial part with a recap of what the reader can now do.

### Confirmed

- `references/tutorials.md:53`
- `references/tutorials.md:63`
- `references/how-to-guides.md:61`
- `SKILL.md:86`, `SKILL.md:89`
- `references/api-reference.md:3`

### On mixing modes

Pages that combine explanation, task steps, and a reference catalog mostly occur where no separate reference page exists. This makes lookup harder, and the cleanest material keeps the modes apart with pointers in both directions. Not counted as a correction to `SKILL.md:44`, because the mixing is evidence of missing pages, not evidence that mixing works better.

---

## Source D

This source was compared in two parts. Rules 1–21 come from the first part and rules 22–43 from the second. Where a second-part rule repeats a first-part rule, it says so.

### Rules

1. Wherever a call is a layer over something lower-level (a query, markup, a request), show the artifact it produces right after the call, so readers learn both the interface and its effect.
2. Introduce a convenience by first showing the longer code it replaces. The shortcut only means something to someone who has seen what it saves.
3. Verify and document behavior as it appears in the default, fully assembled setup a typical user runs. A component in isolation can behave differently from the same component in its usual surroundings.
4. Document only what the interface promises. For yes/no results, describe the truth condition, not the exact value returned. Keep public-but-internal items out of user docs, because whatever you document becomes a commitment.
5. For every entry, ask what happens with empty, missing, null, zero, or otherwise degenerate input, and write the answer down.
6. When a feature provides a guarantee (validation, hooks, constraints), list exactly which operations bypass it, and flag the bypass each time you show one of those operations.
7. Keep older but still-supported ways of doing something in the docs. Label them as older, say readers will meet them in existing code, and order the material so the current way gets the emphasis, usually by placing the older forms last. [revised]
8. Where two things are easy to confuse (components, methods, options), put the distinction inline at the point of confusion and link each to the other. Don't leave it only on a separate comparison page.
9. When a mistake is common or dangerous, show the wrong form, clearly labeled as wrong, beside the right one.
10. Any elision inside runnable code must itself be valid code, such as a comment, so a trimmed snippet still runs when pasted.
11. Make each example's execution context visible (which shell or interactive session, which environment), most of all when a line runs against production.
12. In reference for a library that loads in pieces, state which module, package, or import provides each item.
13. On a long page whose examples share a setup, define that shared setup once near the top and have every later example refer to it.
14. Give callouts distinct types that tell the reader whether they can skip them: essential context, optional extras and pointers, and warnings about things that break.
15. Where it explains a method's purpose, show a real call site from the library's own code and say which part of the library it comes from, alongside or in place of an invented example. [revised]
16. Use second person in tutorials and task steps. In reference descriptions, prefer impersonal wording that describes the item, not the reader.
17. Use warnings for anything that would break the application, including traps where code looks right but does something else, as well as for data loss, security, and money. Keep them rare so they stay visible. [revised]
18. Keep commands and their output in separate blocks only when the docs platform would copy prompts and output along with the command. If copying strips them, a single transcript block reads better.
19. When a file under construction is still short, showing the whole file with the changed lines highlighted helps readers resync. Switch to anchored excerpts once the file grows.
20. Use realistic domain names by default, but use neutral placeholder names when the example is about pure structure (nesting, inheritance) and no domain fits.
21. Keep entries of the same kind in the same order, but scale the structure to each entry's size. Leave out labels and sections that would be empty.
22. State plainly what the tool or feature does not do, and what falls outside the page's scope, so readers know which responsibilities stay with them.
23. When a command generates files the reader didn't write, show what was generated and explain each relevant part before asking them to change anything.
24. When documenting an option that changes output, show real output and mark exactly which parts the option adds or changes.
25. When a default depends on a version or compatibility setting, give each option's default as a version-by-value table. Also publish, for each version, a single list of every default that changed in it.
26. Document only the behavior you are willing to guarantee. Describe meanings (for example, "returns a true value when …") rather than exact incidental values the implementation could change. (Repeats rule 4.)
27. Explicitly mark interfaces that are reachable but not supported, so readers don't build on them, and keep them out of the public reference. (Repeats rule 4.)
28. Describe behavior as users see it in the standard, fully configured setup, not as the isolated unit behaves on its own. (Repeats rule 3.)
29. Make every example use the currently recommended approach, because readers copy examples. Move superseded approaches out of the main text and leave a one-line pointer to the documentation for the version that used them. (Compare rule 7, which covers older forms that are still supported.)
30. For every reference entry, state what happens on boundary inputs: empty, missing, null, zero, and unnamed values. (Repeats rule 5.)
31. Write links so they keep the reader inside the documentation version they are reading. Never hand-link to the docs for an unreleased version. [revised]
32. In teaching material, show a selected subset of a large API, say explicitly that it is a subset, and link to the complete, authoritative list.
33. Teach readers the command or query that prints the current, complete answer (help output, live lists, introspection), so they don't depend on a static copy that can go stale.
34. Where readers' first instinct produces wrong code, show the wrong version labeled as wrong, then the right version, and say why. (Repeats rule 9.)
35. When the correct value depends on the reader's environment, say so. Name the trade-off it controls, explain why no single default fits everyone, and give a method for measuring and adjusting it. [revised]
36. For each option, state its cost (memory, speed, complexity), whether it is safe for production, and how much the recommendation actually matters.
37. Let readers hit an error on purpose as often as the subject demands. When the workflow being taught is fail-then-fix, or each error motivates the next step, repetition is the lesson, not a detour.
38. Whether to keep commands, prompts, and output in one block depends on your platform. If the copy control strips prompts and output, a single block that shows command and result together is clearer. Otherwise, separate them. (Repeats rule 18.)
39. Use a warning for anything that silently breaks or misleads, including skipped files, overwritten files, and settings unsafe in production, not only for data loss, security, or money. Give each callout type one defined meaning and stick to it. (Overlaps rules 14 and 17.)
40. Address the reader directly in tutorials and how-to steps. In reference descriptions, describe the thing itself without addressing the reader. (Repeats rule 16.)
41. Keep reference entries lean, but for options whose misuse is costly, include why the option exists, its known limits, and its interactions. Leaving these out is not austerity, it's a hazard.
42. Keep a central page for cross-cutting concerns such as security, but also state each feature's own security consequences where that feature is documented. Readers configure features one page at a time.
43. A uniform opening block on every long page, with one sentence of scope followed by a short list of what the reader will learn, is a useful contract, not empty boilerplate. Avoid vague openers, not structured ones. [revised]

### Baseline rules broken

- `SKILL.md:52`, `SKILL.md:62`, `SKILL.md:110-112`: verify every name and output, run every example in order, and state versions consistently.
- `SKILL.md:76`: use one term per concept across the whole documentation set.
- `SKILL.md:73`, `SKILL.md:80`: no ease words, no marketing adjectives.
- `SKILL.md:48`, `references/learning-science.md:57-59`: write objectives as observable actions, not "know about".
- `references/style.md:16`: link text says where the link goes, not its position.
- `SKILL.md:81`, `references/api-reference.md:91-93`: cover material once and link to it, instead of writing it twice and letting the copies drift.
- `SKILL.md:70`: use active voice and a consistent person inside walkthroughs.
- `references/api-reference.md:3`, `references/api-reference.md:85`, `references/api-reference.md:104`: give entries a consistent structure, state every default, and name the replacement in each deprecation note.
- `SKILL.md:52`, `references/books.md:73`: record the version documented, and don't leave dated material in place.
- `SKILL.md:60-62`: run every example, so none depends on undefined code or is invalid.
- `SKILL.md:44`: don't embed large reference dumps in a walkthrough, or unrelated task material in a reference.
- `SKILL.md:77`: give a concrete example before an abstract definition.
- `references/style.md:9`: use one placeholder style consistently.

### Confirmed

- `SKILL.md:103`
- `SKILL.md:82`
- `SKILL.md:102`
- `references/learning-science.md:9`
- `references/explanation.md:14`

### On mixing modes

Both parts saw topic pages that combine explanation, a catalog or reference, and task sections in a fixed order, each mode under its own top-level heading (one reference page reverses the order and puts the reference first). Not counted as a correction to `SKILL.md:44`: the pages show the structure is consistent and readable, not that it serves readers better than split pages, and the places where the separation lapses show the costs the rule exists to prevent.

---

## Source E

### Rules

1. Warn the reader, before they run it, that a code sample is meant to fail or misbehave, and mark such samples consistently so they're recognizable at a glance.
2. When you rename a heading, keep its old anchor so existing links still land.
3. Number code samples and figures, refer to them by number, and when you return to one after a long gap, show it again instead of sending the reader back. Check numbered cross-references whenever samples are added or removed.
4. Next to any sample output, say which parts will differ on the reader's machine or between runs, such as versions, timings, ordering, or paths.
5. Before introducing a feature, have the reader write working code without it, so the problem the feature solves is felt rather than asserted.
6. Name the places where learners usually get stuck, before they reach them, and say that difficulty there is normal and expected.
7. Connect new concepts to their nearest equivalents in tools the audience already knows, and say where the comparison stops holding. [revised]
8. When a teaching example takes a shortcut, such as skipping error handling, using a simplified algorithm, or ignoring edge cases, say so and describe what production code would do instead.
9. At the point where a concept is shown, invite the reader to change the example and predict what will happen before checking it with the real tool.
10. Before implementing something, show the code that will call it, so the reader knows what the implementation must satisfy.
11. When examples depend on a fast-changing external ecosystem, consider a small companion package that wraps exactly what the material needs, to keep examples stable and the focus on concepts. Publish its source.
12. Offer one setup step that fetches everything the whole course or book will need, so readers can work offline afterward.
13. If the same source ships to print and web, write link text that still reads well when converted to plain text with a URL, mark links that only make sense online, and keep internal links relative.
14. For any output that can't be regenerated automatically, leave a note in the source explaining exactly how to reproduce it.
15. Mark each term typographically where it is defined, and never split a single word between code formatting and plain prose.
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

### Baseline rules broken

- `references/books.md:27`, `references/learning-science.md:57-59`: chapter openers state checkable capabilities, not a list of topics.
- `references/books.md:45-55`: give regular, spaced practice with solutions provided.
- `SKILL.md:101`, `references/books.md:35`: chapter summaries list skills gained instead of restating the chapter.
- `SKILL.md:62`, `SKILL.md:111`: paste real, current output that matches the code shown.
- `SKILL.md:52`, `SKILL.md:114`: verify cross-references, so none points at content that changed or was never introduced.
- `SKILL.md:62`: every example the reader follows must work as written.
- `references/books.md:73`: don't tie statements to the date of writing.
- `SKILL.md:73`: no ease words.
- `SKILL.md:91`: no `foo`-style placeholder names in teaching examples.

### Confirmed

- `references/books.md:17`
- `references/explanation.md:14`
- `references/books.md:60`
- `references/books.md:65`
- `references/tutorials.md:48`

### On mixing modes

Chapters read in order weave short rationale, quick-reference recaps, and how-to fragments into a tutorial narrative, while pure reference is kept in separate sections. Counted as a correction to `SKILL.md:44` (rule 25): for learners reading in sequence the woven material supports learning, and lookup is still served elsewhere.

---

## Source F

### Rules

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

### Baseline rules broken

- `SKILL.md:60-62`: run every example, so expected output matches and no snippet has a syntax error.
- `SKILL.md:73`, `SKILL.md:80`: no ease or "obviously" words, no marketing adjectives.
- `SKILL.md:81`: state prerequisites on every page a reader can land on from search.
- `SKILL.md:101`: don't end a page with a conclusion that restates it.
- `SKILL.md:116`: headings say what their section holds, so they outline the page; generic numbered "example" headings don't.

### Confirmed

- `SKILL.md:44`
- `references/api-reference.md:91`
- `references/explanation.md:14`
- `SKILL.md:27`

### On mixing modes

Reference landing pages hold shared explanation and small task examples in fixed, labeled sections. Teaching chapters copy reference tables inline. The first pattern is counted as a correction to `SKILL.md:44` (rule 19), because fixed headings let lookup readers skip the explanation and shared concepts are written once. The second is not, because the copied tables are a second copy to maintain, which supports the rule rather than correcting it.

---

## Source G

### Rules

1. When a reference entry describes an operation with several stages, open with a numbered list of the stages in the order they are evaluated, and link each stage to the section that details it.
2. When a signature or grammar nests, show the complete shape first with named placeholders, then define each placeholder underneath. Don't inline every alternative.
3. In each reference entry, state the operational side effects of using the item: what it blocks or locks, what it costs on large inputs, what other users or processes feel, and the variant that avoids the cost.
4. Readers often arrive with habits from a standard, a specification or a competing product. Give each entry a section saying where this implementation conforms, extends or differs, and add an inline warning wherever those habits lead someone astray.
5. Give all reference entries one small, shared sample domain, separate from the tutorial's scenario, so examples across entries use the same names and can be compared.
6. Match the weight of a reference entry to the item. Put many small items in one table, one row each: signature, a one-line description, and an example paired with its exact result. Variants and aliases share a row.
7. Choose examples that sit on the boundaries where readers would guess wrong, such as negative or zero arguments, missing values and non-ASCII input, and show the exact result.
8. To explain how variants differ, keep the input fixed, change one thing at a time, and show the result of each variant one after another.
9. When a page leaves out something a reader might expect, say so at that point and link to where it is covered.
10. Wherever readers predictably reach for a plausible but wrong form, show it next to the correct one, mark which is wrong, and explain why. This applies on reference and conceptual pages too, not only in tutorials.
11. Collect a feature's known limitations and caveats in a clearly titled section of their own.
12. Keep the section order fixed across entries of the same kind, but leave out sections that have nothing to say rather than filling them with "None".
13. Don't catalog every possible error. Describe the conditions that cause an error at the parameter or step they concern, and document the error format only if readers parse it.
14. Explain a cross-cutting topic fully in one place. In each entry it affects, still state in a line or two the specific requirement or hazard that applies there, and link to the full treatment.
15. End a reference entry with a set of examples covering its common tasks and notable options, each introduced by a short sentence naming the task, rather than a single minimal call.
16. Use warnings for outcomes that are silently wrong as well as for data loss, security and money. Keep lighter callout levels for tips and notes so severity stays meaningful.
17. Abstract placeholder names are fine for demonstrating pure behavior if the data is tiny and every row or value is shown. Use realistic names when the example is a task or the data isn't shown.
18. In teaching material, a one-sentence definition followed immediately by an example works as well as example-first. In lookup material, put the definitions before the examples.

### Baseline rules broken

- `SKILL.md:73`, `references/tutorials.md:48`: no talking-down words, and no dispensable aside before the reader's first success.
- `SKILL.md:62`, `references/tutorials.md:55`: tutorial examples must be reproducible from what the page gives.
- `references/api-reference.md:5`: parameter descriptions add more than the parameter's name.
- `SKILL.md:74`: open with the outcome, not an announcement of what the chapter describes.
- `SKILL.md:91`: don't use abstract names when the data behind them isn't shown.
- `references/tutorials.md:54`: end a tutorial with what the reader can now do, not a generic conclusion.
- `SKILL.md:34`, `SKILL.md:44`: a common task needs a task page, not only a reference entry.
- `SKILL.md:92`: keep statements and their output in separate blocks.

### Confirmed

- `SKILL.md:103`
- `references/explanation.md:13`
- `SKILL.md:102`
- `references/api-reference.md:103`

### On mixing modes

Reference pages contain bounded explanation or recovery-procedure sections, and conceptual chapters embed lookup tables, while the major parts otherwise stay separate. Not a correction to `SKILL.md:44`: each embedded section serves the job of the page it sits on, so no page is doing two jobs.

---

## Audit

No rule was removed. Every abstracted rule had at least some supporting evidence. Revisions narrowed a claim, restored a condition, or replaced a reason the evidence didn't give. The baseline-rules lists leave out falls-short items that no stated skill rule covers. In practice these were navigation defects: a wrong back link, pages with no previous or next link, and two conflicting orderings of the same pages.

**A: 2 revised, 0 removed.**
- Rule 3: the evidence shows reimplementations built without the library being explained, not with "no dependencies".
- Rule 7: the evidence shows manual checks for "what to try and what you should see", not runnable tests. Only one exercise has a negative check, so that part became conditional.

**B: 6 revised, 0 removed.**
- Rule 5: nothing in the evidence shows asides kept apart from warnings. It shows only that most callouts aren't warnings.
- Rule 7: the evidence covers accessibility and one attached security caveat. It doesn't show examples written to production standard in general.
- Rule 10: only some section landing pages route readers by situation, and those are the sections whose readers arrive in different situations. "Each section" overstated it.
- Rule 11: the doc-bug reporting instructions sit on an introductory page, not next to the first step likely to fail.
- Rule 12: the stated reason is to leave such content to aggregators. "Can't keep current" was never given as a reason.
- Rule 18: the evidence says whole-file display "can beat" a fragment. The same comparison shows very long diffs burying the change, a limit the rule had dropped.

**C: 4 revised, 1 anonymized, 0 removed.**
- Rule 1: nothing in the evidence supports "use the exact technical term".
- Rule 5: an ordered escalation path appears in one part only, so giving an order became conditional on there being several channels.
- Rule 6: the evidence shows advice flagged as general. It never shows product-specific advice being flagged.
- Rule 14 (anonymized): the example titles were quoted from the source, so they were replaced with a general description.
- Rule 17: the stated intent is to avoid version numbers in body text, not to ban them outright.

**D: 6 revised, 0 removed.**
- Rule 7: one example puts the older form first and names the recommended one afterward. The real requirement is emphasis on the current way, not a fixed position.
- Rule 15: the call sites come from the library's own code, not from any known codebase.
- Rule 17: one example is an infinite loop, which isn't silent. The defined criterion is "would break the application".
- Rule 31: the stated ban covers hand-linking to the unreleased version, not to every other version.
- Rule 35: the evidence gives trade-offs, reasons, and a measurement method, but not a starting value.
- Rule 43: the opening lists say what the reader will learn. The same comparison shows they often aren't written as actions, so "be able to do" overstated the evidence.

**E: 1 revised, 0 removed.**
- Rule 7: the comparisons often note only that "some" or "significant" differences exist, so "exactly where" overstated the evidence.

**F: 0 revised, 0 removed.** Every rule matched its evidence, conditions included.

**G: 0 revised, 0 removed.** Every rule matched its evidence, conditions included.

**Total: 19 revised, 1 anonymized, 0 removed.**
