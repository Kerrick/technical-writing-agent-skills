# Rules to write into the skill

Each rule below has a heading, the rule itself, its kind, where it applies, and what an agent does wrong without it.


### 1. Run every example as written
- **Rule:** Run every command and code sample in page order, starting from the state the page declares. Check that each one runs without syntax errors, produces the output the page shows, and needs no code the page never gives. Setup data may live in a separate file that ships with the material, as long as the page says where it is and that data produces the output shown. Repeat the run on a clean environment whenever a dependency changes.
- **Kind:** well known, often broken.
- **Applies to:** every page with code
- **Without it:** An agent publishes snippets that fail, or that show output the code doesn't produce, because they were never run.


### 2. End lessons with a short, fixed closing that points forward
- **Rule:** In a sequence of lessons (tutorial parts, chapters, course modules, episodes), end every lesson with the same short closing, and make it point forward. Use one of two forms:
  - one sentence naming what the reader should now be comfortable with, followed by a pointer to the next lesson; or
  - a brief recap of the concepts covered, followed by a preview of the next lesson.

  A list of skills the reader gained is one form of recap, not the only one. Keep the closing brief. Don't walk back through the page's content. Outside a sequence, don't end a page with a conclusion that restates it.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, book, course, video; the no-restating rule applies to every page
- **Without it:** An agent either closes each lesson with a long conclusion that repeats it, or forces a skills list onto lessons where one sentence and a pointer onward would serve better.

### 3. One primary job per page; other kinds of material only in short, labeled sections
- **Rule:** Give each page one primary job: teaching by doing, getting a task done, supporting lookup, or explaining why. A page may carry a short piece of another kind of material when that piece serves the page's primary job. It must sit in a clearly labeled section or a skippable aside, in the same position on every page of that kind. Examples:
  - brief rationale and a quick recap woven into a lesson that is read in order;
  - a labeled section of shared concepts on a reference landing page, kept apart from the member listing;
  - a motivating example, a short explanation, and a compact usage summary on a single-feature page, in the same order for every feature.

  When the other material is large, or readers need it on its own, give it a page of its own and link both ways. Don't paste reference catalogs or copies of reference tables into a walkthrough. Don't let a task exist only inside a reference entry: give every common task its own task page.
- **Kind:** overrides common advice.
- **Applies to:** every page
- **Without it:** An agent either moves every sentence of rationale to a separate page, leaving lessons choppy and sending readers back and forth, or pastes whole reference tables into tutorials.

### 4. Show the wrong form beside the right one
- **Rule:** Wherever readers predictably reach for a plausible but wrong form, show it next to the correct one. Label which is wrong and explain why it fails. Do this on every page type, including reference and conceptual pages, as often as real traps occur, and especially when the wrong form runs without error but gives a wrong result. Showing the naive attempt, its failure, why it fails, and then the fix is a regular teaching move, not a one-time device.
- **Kind:** not commonly known.
- **Applies to:** every page
- **Without it:** An agent shows only correct code, so readers who already hold the wrong form never learn why it's wrong.


### 5. Show the longhand before the shortcut, and say how equivalent they are
- **Rule:** Introduce a convenience API, or a construct that seems like magic, by first showing the longer code it stands for, built from parts the reader already knows. A tiny reimplementation also works, if it is readable in one sitting and written without the library being explained. Then show the short form and say plainly whether the two are exactly equivalent, approximately equivalent, or only illustrative, and list where the equivalence breaks. Mark illustrative implementations as not for real use. Repeat the equivalence in the reference entry for the convenience API.
- **Kind:** not commonly known.
- **Applies to:** tutorial, explanation, reference, book
- **Without it:** An agent presents the shortcut as opaque magic, so readers can't reason about what it does or what it saves.


### 6. Give the docs a map and each section a landing page
- **Rule:** Give the documentation an explicit map: which kinds of page exist, what each is for, where beginners start, and how much ground the introductory material covers. Give each section or multi-page unit a landing page: a short summary of the area, then a structured list of its child pages with one line on what each covers. A unit overview can preview each topic in a sentence or two with a small example, and end with two exits: "work through this in order" and "skip to the next unit if this is familiar." Where a section's readers arrive in different situations or with different goals, send each kind of reader to a different starting point.
- **Kind:** not commonly known.
- **Applies to:** navigation and landing pages, books, courses
- **Without it:** An agent writes content pages with no entry points, so readers can't tell where to start, what's there, or what they can skip.


### 7. Warn about silent and breaking failures too
- **Rule:** Use a warning callout for data loss, security, and money. Also use one for anything that breaks the application or silently gives a wrong result: code that looks right but does something else, mistakes that fail silently, skipped or overwritten files, settings unsafe in production, hangs, crashes, and code that isn't meant to be copied. Each warning names one failure. Give each callout type one fixed meaning, use lighter types (note, tip) for everything else, and keep warnings rare enough that readers still notice them.
- **Kind:** overrides common advice.
- **Applies to:** every page
- **Without it:** An agent leaves silent wrong-result traps unflagged because they don't involve data loss, security, or money.


### 8. Show code changes by file size, with full-code checkpoints
- **Rule:** In a step-by-step build, show the whole file with the changed lines marked while the file is short. Once a whole-file view would bury the change, switch to an anchored excerpt (the file name plus a few surrounding lines) with the changed lines marked. Explain the marking notation the first time it appears. Once a repeated scaffolding pattern is established, you may show only the relevant part and say once what the reader must add. At regular checkpoints, show the complete current code, or link to the tested full version, so readers who have drifted can catch up.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, book, video
- **Without it:** An agent shows unanchored fragments throughout (or the full file at every step), and readers who drift have no way to get back in sync.

### 9. Connect new concepts to what readers already know
- **Rule:** When readers bring knowledge or habits from another tool, standard, specification, or competing product, connect each new concept to its nearest counterpart there. Say where the two conform and where they differ, and put an inline warning wherever the old habit leads readers astray. Open a concept guide with the underlying technology or idea the reader already knows, then show what your tool adds on top of it.
- **Kind:** not commonly known.
- **Applies to:** explanation, reference, tutorial, book
- **Without it:** An agent explains everything from scratch, losing the transfer readers could get and leaving their wrong habits unflagged.


### 10. Verify every fact against its source, and keep facts consistent
- **Rule:** Take every name, type, default, error, output, and version from a source you have checked: code, schema, `--help`, tests, or changelog. Make prose agree with the code it describes, check every cross-reference against the content it points to, record which version you documented, and keep facts and version statements consistent across pages. Mark anything you couldn't verify.
- **Kind:** well known, often broken.
- **Applies to:** every page
- **Without it:** An agent writes plausible names and outputs from memory, and sections drift apart, written against different versions of the API.


### 11. Realistic names for real use; neutral names only for pure mechanism
- **Rule:** Use realistic domain names (`invoice`, `customer_id`) when an example models real use, shows a task, or works on data the reader can't see. Use neutral placeholder names only when all three hold: the example demonstrates pure structure or mechanism (nesting, inheritance, how an operator behaves), no domain fits, and the data is tiny and fully shown. Keep the chosen names consistent across a running example.
- **Kind:** overrides common advice.
- **Applies to:** every page with code
- **Without it:** An agent either uses `foo`/`bar` in task examples, or forces an invented business domain onto a pure mechanism demo and hides the mechanism.

### 12. Let readers feel the problem before giving them the feature
- **Rule:** Before introducing a feature or abstraction, let the reader meet the problem it solves in what they've built so far. Either have them do the task the laborious way, or point to the duplicated code, hardcoded value, unhelpful output, or bug in their current work, so they feel the cost instead of being told about it. Then present the feature as the fix. A unit may end on a known gap that the next unit fills.
- **Kind:** not commonly known.
- **Applies to:** tutorial, book, video
- **Without it:** An agent introduces features first and justifies them by assertion, so readers don't see why they need them.


### 13. Settle easily confused pairs where the confusion happens
- **Rule:** Where two forms, components, methods, options, or terms are easy to confuse, put the distinction at the point of confusion. This includes terms readers commonly use as if they meant the same thing. A side-by-side table that labels which is which, or what distinguishes them, works well. Say that the loose usage exists, show a case where the difference matters, and link each item to the other. Don't leave the distinction only on a separate comparison page.
- **Kind:** not commonly known.
- **Applies to:** every page
- **Without it:** An agent documents each item in isolation, and readers keep mixing them up.


### 14. Put optional depth in titled, consistent asides
- **Rule:** Put optional depth (shortcuts, tangents, advanced options) in one consistent, visually distinct kind of aside, separate from warnings. Give each aside a descriptive title saying what's inside, such as the question it answers, so readers can choose to skip it. Give each callout type a fixed meaning that tells readers whether they can skip it: essential context, optional extra, or warning. Keep asides few.
- **Kind:** not commonly known.
- **Applies to:** every page
- **Without it:** An agent either clutters the main path with optional detail or cuts it, and readers can't tell what is safe to skip.


### 15. Use "we" for shared narrative work
- **Rule:** In narrative, build-along material read in order, write as one knowledgeable person talking to another. Use "we" or "let's" for work you and the reader do together, "you" for what the reader alone does or observes, and imperatives for discrete steps. A vivid comparison or a light joke is fine when it makes an idea stick. Don't flatten the prose into neutral summary.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, book, video
- **Without it:** An agent writes every narrative tutorial as uniform second-person imperatives that read like an appliance manual.


### 16. One shared sample domain per set of examples
- **Rule:** Give each body of related examples one shared sample domain:
  - On a long page whose examples share a setup, define that setup once near the top and have every later example refer to it.
  - Across a set of reference entries, use one small shared sample domain, so names match and examples can be compared.
  - Across a feature's guide and its reference pages, keep the same domain.
- **Kind:** not commonly known.
- **Applies to:** reference, how-to, explanation
- **Without it:** An agent invents new data for every example, so readers have to learn a new domain each time and can't compare entries.

### 17. Document boundary behavior
- **Rule:** In every reference entry, state what happens on boundary and degenerate input: empty, missing, null, zero, negative, unnamed, non-ASCII, input that is already complete, and cases where nothing qualifies. Also state whether results arrive at once or later. State plainly any effect a reader might expect that does not happen. Choose examples on those boundaries, where readers would guess wrong, and show the exact result.
- **Kind:** not commonly known.
- **Applies to:** reference
- **Without it:** An agent documents only the happy path, and readers find the edge behavior in production.


### 18. Let failures recur while each one teaches
- **Rule:** Let learners hit an error on purpose whenever the error introduces the next concept, or whenever the skill being taught is reading a tool's diagnostics or a fail-then-fix workflow. Show the failing attempt and its exact message, and let the message drive the next step. Stop when a failure teaches nothing new.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, book, video
- **Without it:** An agent includes one token error and then only success paths, so learners never practice reading the diagnostics they'll meet.


### 19. Write every example as if it will be copied into production
- **Rule:** Assume every example will be pasted into production. Use the currently recommended approach, with current safe and accessible practice built into ordinary examples, and give a line of reasoning where a practice isn't obvious. Attach each caveat, such as a security risk, to the example that raises it. Never use a deprecated or risky construct just to save space. Move superseded approaches out of the main text, leaving a one-line pointer to the documentation for the version that used them.
- **Kind:** not commonly known.
- **Applies to:** every page with code
- **Without it:** An agent writes the shortest code that demonstrates the point, and readers copy its insecure or outdated shortcuts.


### 20. Keep one maintained copy of anything that changes
- **Rule:** Keep one maintained copy of anything that changes, and point to it instead of copying it:
  - For a step that depends on another project's software, document only how it connects to yours and link to that project's own instructions.
  - Keep FAQ answers to a sentence or two, with a link to the page that holds the full answer.
  - When teaching a subset of a large API, say it's a subset and link the complete list.
  - Teach the command or introspection that prints the current, complete answer.
  - Keep support, compatibility, and availability data in one structured source, rather than hand-writing version numbers into prose.
- **Kind:** not commonly known.
- **Applies to:** every page
- **Without it:** An agent copies third-party steps, full answers, and version tables into many pages, and the copies drift out of date.


### 21. Avoid claims that age
- **Rule:** Don't make statements that depend on when they were written ("new", "recently", "currently", "as of this writing"). They become false later, and readers can't tell when. Keep version-specific details in a few places so updates touch little, and remove dated material when it expires.
- **Kind:** well known, often broken.
- **Applies to:** every page, especially books
- **Without it:** An agent writes "the new X API", which becomes false and confusing a release later.


### 22. One term per concept, with any unavoidable second name declared once
- **Rule:** Use one term per concept, define it on first use, and never vary it for elegance. When a second name is unavoidable, declare the equivalence once, prominently, near the start, saying which term is exact and why. Two cases:
  - When commands, directories, or tools use a different or older name, keep your one term in prose.
  - When a precise term has a more natural synonym, both may appear on the page once the synonym is declared.
- **Kind:** overrides common advice.
- **Applies to:** every page
- **Without it:** An agent uses undeclared synonyms that read as different things, or hides that the tools use another name, so readers can't connect the prose to what they see.

### 23. Ask for predictions at the point of the concept
- **Rule:** At the point where a concept is shown, not only in end-of-chapter exercises, stop and ask the reader what will happen before you show it. Or invite them to change one specific value or line and predict the result, then check it with the real tool.
- **Kind:** not commonly known.
- **Applies to:** tutorial, explanation, book, video
- **Without it:** An agent saves all retrieval and prediction for end-of-chapter exercises, so readers pass through examples without engaging with them.


### 24. Show several solutions when judgment is the goal
- **Rule:** Keep a single path for a reader's first success. In worked solutions where more than one answer is correct, and in material whose goal is design judgment, build two or more working solutions and say openly what each gains or costs.
- **Kind:** not commonly known.
- **Applies to:** book, course, later tutorials, exercises
- **Without it:** An agent presents one canonical answer, and readers conclude that it is the only right one.


### 25. Tell readers how to check their own work
- **Rule:** At each exercise and checkpoint, tell readers how to check their own work: what to try and what they should see. Where a change could overshoot, or is meant to preserve behavior (a refactor), also say what should not happen or not change, and confirm it with unchanged output and passing automated checks.
- **Kind:** not commonly known.
- **Applies to:** tutorial, book, exercises
- **Without it:** An agent sets exercises and refactoring steps with no way for readers to tell whether they succeeded.


### 26. Mark wrong and failing samples inside the block
- **Rule:** Mark every sample that is incorrect, discouraged, or meant to fail inside the code block itself, for example with a `# Wrong:` comment, and use the same marking every time. Warn before the reader runs a sample that is meant to fail. Someone who copies or runs only the block should still see the warning.
- **Kind:** not commonly known.
- **Applies to:** every page with code
- **Without it:** An agent labels wrong code only in surrounding prose, and readers who copy the block take the wrong version.


### 27. Tell learners where difficulty is normal
- **Rule:** Before learners reach them, name the places where people usually get stuck, and say that difficulty there is normal and expected. Tell them which details they can leave partly understood for now.
- **Kind:** not commonly known.
- **Applies to:** tutorial, book, video
- **Without it:** An agent leaves learners to read normal confusion as personal failure, and some give up.


### 28. Sequenced pages may build on earlier ones
- **Rule:** Pages in a deliberately ordered learning path may depend on earlier pages, including a running example carried across sequenced conceptual pages. Each such page links back to what it relies on and restates the starting code it builds on, so a reader arriving from search can follow. Serve readers who want to look something up with separate lookup sections, rather than making every lesson self-contained.
- **Kind:** overrides common advice.
- **Applies to:** tutorial series, book, course, sequenced conceptual pages
- **Without it:** An agent makes every lesson fully self-contained, repeating setup and context until the sequence becomes bloated.

### 29. One page can serve beginners and experts
- **Rule:** One page can serve beginners and experienced readers if it starts with the simplest, most common use, moves steadily to advanced uses, sets material only some readers need apart in clearly titled sidebars they can skip, and leaves rare edge cases to the reference.
- **Kind:** overrides common advice.
- **Applies to:** every page, especially feature guides
- **Without it:** An agent splits every topic into separate novice and expert pages, which multiplies pages and splits up the material that readers move through as they progress.


### 30. Give reasoning where the reader will wonder
- **Rule:** When a step involves a judgment call (how much to verify, which level to test at, why an order or a choice of element matters), or a design choice that will puzzle readers at that point, give the reasoning right there. Keep it to a few sentences, in a titled box or a single clearly marked paragraph that can be skipped. This holds in tutorials, how-tos, and reference entries. Move anything longer to an explanation page.
- **Kind:** overrides common advice.
- **Applies to:** tutorial, how-to, reference
- **Without it:** An agent cuts the why to one clause or a link, so readers make the judgment call blind at exactly the moment they need the reasoning.


### 31. Bridge gaps in assumed knowledge
- **Rule:** When the material relies on things some readers may not know (features within a skill they're assumed to have, or basics only some readers have), add a dedicated bridging section or chapter. It covers only those things, links out for the rest, says who can skip it, and invites readers to return when stuck. A book may also mark its late chapters as reference, and offer an alternative reading order for readers who want detail before practice.
- **Kind:** not commonly known.
- **Applies to:** book, course, tutorial series
- **Without it:** An agent either assumes the prerequisite features and loses part of the audience, or scatters remedial asides through every chapter.


### 32. Show legacy forms for recognition
- **Rule:** Show the older forms of an API that readers will meet in existing code, labeled as older or legacy, so readers can recognize and translate them. Keep the emphasis on the current way, usually by placing older forms last, and don't present them as an equal option.
- **Kind:** not commonly known.
- **Applies to:** reference, tutorial, book
- **Without it:** An agent shows only the current form, and readers can't make sense of the older code they'll inherit.


### 33. Say where each name comes from
- **Rule:** When a new name appears in code, say which package, module, or import provides it. In reference for a library that loads in pieces, state for each item which module provides it. Tell learners that this is what to search for when they need help or documentation.
- **Kind:** not commonly known.
- **Applies to:** tutorial, reference, book
- **Without it:** An agent uses names without saying where they come from, so readers can't find their documentation or import them.


### 34. Say where to get help
- **Rule:** Tell readers where to get help from people at the start of each part of a multi-part tutorial, and right after the first step likely to fail. Where there are several channels, say which to try first. Early in the documentation, say how to report a mistake in it.
- **Kind:** not commonly known.
- **Applies to:** tutorial, documentation set
- **Without it:** An agent leaves stuck readers with nowhere to turn and gives doc bugs no route to the maintainers.

### 35. Flag teaching shortcuts
- **Rule:** When a teaching example takes a shortcut (skipped error handling, a simplified algorithm, ignored edge cases, incomplete markup, a partial implementation), say so next to it and say what production code would do instead.
- **Kind:** not commonly known.
- **Applies to:** tutorial, explanation, book, video
- **Without it:** An agent simplifies examples silently, and readers ship the simplification.


### 36. Cross-cutting topics: full treatment once, local consequences everywhere
- **Rule:** Explain each cross-cutting topic (security, authentication, errors, pagination, and so on) fully on one page. In every entry or feature page it affects, still state in a line or two the specific requirement, consequence, or hazard that applies there, with a link to the full treatment.
- **Kind:** overrides common advice.
- **Applies to:** reference, how-to
- **Without it:** An agent leaves only a bare link, and readers who configure one feature at a time miss that feature's security or other consequences.


### 37. Elisions in code must be valid code
- **Rule:** When you omit part of a code sample, mark the gap with something the language accepts, usually a comment, and say what belongs there, so a pasted snippet still parses and runs.
- **Kind:** not commonly known.
- **Applies to:** every page with code
- **Without it:** An agent writes a bare `...` inside code, and pasted snippets fail with syntax errors.


### 38. Show commands and output the way readers will copy them
- **Rule:** Decide how to show commands and output by how readers will copy them. Put them in separate blocks when the docs platform's copy action would pick up prompts and output along with the command. When the copy action strips them, or the material is print-first narrative, one transcript block showing command and result together is clearer. Explain the prompt marker once.
- **Kind:** overrides common advice.
- **Applies to:** every page with commands
- **Without it:** An agent always splits commands from their output, even where a single transcript would read better and copy cleanly.


### 39. Scale reference entries to their item
- **Rule:** Keep the section order fixed across reference entries of the same kind, but scale each entry to its item. Leave out sections and labels that would be empty instead of filling them with "None". Put many small items in one table, one row each: signature, a one-line description, and an example paired with its exact result. Variants and aliases share a row.
- **Kind:** overrides common advice.
- **Applies to:** reference
- **Without it:** An agent gives every tiny function a full template full of "None" sections, burying the content.


### 40. Say what isn't covered or done
- **Rule:** State plainly what the tool or feature does not do, and which responsibilities stay with the reader. When a page leaves out something a reader might expect, say so at that point and link to where it's covered.
- **Kind:** not commonly known.
- **Applies to:** every page
- **Without it:** An agent describes only what the tool does, and readers assume it handles things it doesn't.


### 41. Change one thing at a time to show variants
- **Rule:** To show what an option or variant changes, keep the input fixed, change one thing at a time, and show the real output for each, one after another. Mark exactly which parts of the output the option adds or changes.
- **Kind:** not commonly known.
- **Applies to:** reference, explanation
- **Without it:** An agent shows each option on different input, so readers can't see what the option itself does.


### 42. State operational cost
- **Rule:** For each reference entry or option, state its operational cost: memory, speed, cost on large inputs, what it blocks or locks, and what other users or processes feel. Say whether it is safe for production, how much the choice actually matters, and which variant avoids the cost.
- **Kind:** not commonly known.
- **Applies to:** reference
- **Without it:** An agent documents only function, and readers discover locking or memory costs in production.


### 43. Collect known limits
- **Rule:** For features and options whose misuse is costly, document why they exist, their known limitations and caveats, and their interactions. Collect these in a clearly titled section of the feature's or entry's documentation.
- **Kind:** not commonly known.
- **Applies to:** reference, explanation
- **Without it:** An agent trims entries to an austere minimum and leaves out exactly the limits that make misuse expensive.

### 44. Refer to other parts by stable label, never by position
- **Rule:** Refer to other parts of a document by a stable label: a number for code samples and figures, a section name, or what an example shows. Never refer by position, such as "above" or "below". When returning to a sample after a long gap, show it again instead of sending the reader back. Recheck numbered references whenever samples are added or removed.
- **Kind:** not commonly known.
- **Applies to:** every page
- **Without it:** An agent writes "as shown above", which breaks with layout changes, screen readers, translation, and reflowed pages.

### 45. Definitions first in lookup material
- **Rule:** In reference and other lookup material, put the definition before the examples, and make it complete on its own: the description fully defines the behavior, and the examples only illustrate it. In teaching material, give a concrete example before the abstraction it illustrates, or a one-sentence definition followed immediately by an example. Both work.
- **Kind:** overrides common advice.
- **Applies to:** reference (definition first); tutorial, explanation, book (either order)
- **Without it:** An agent leads every reference entry with an example and leaves some rules stated only in the examples.


### 46. Frame every example, and give reference a set of task examples
- **Rule:** Introduce every example with a heading or a sentence naming the task or behavior it demonstrates and what to watch for, and follow it with an explanation of the result. End a reference entry with a set of such examples covering its common tasks and notable options, not a single minimal call.
- **Kind:** overrides common advice.
- **Applies to:** every page with examples; the example set applies to reference
- **Without it:** An agent drops in unlabeled examples and gives reference entries one minimal call, so readers can't find the usage they need.

### 47. Pin versions unless the docs track the current release
- **Rule:** When the documentation is versioned with each release, or always describes the current release, install the newest release without a pin: the reader gets the version the page was written for. Add a version constraint, such as a minimum, wherever a minimum version is actually required. When the documentation is written against one version and not updated with each release, pin the version the page was written and tested against.
- **Kind:** overrides common advice.
- **Applies to:** every page with install steps
- **Without it:** An agent either pins every install, so versioned or current-release docs install outdated packages, or leaves unversioned docs unpinned, so they break when a dependency releases a new major version.
