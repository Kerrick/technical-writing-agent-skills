# Lessons: tutorials, books, courses, videos, exercises

Read this when writing a tutorial, quickstart, book chapter, course module, workshop, video or screencast script, or exercises. These rules add to the ones in SKILL.md tagged for tutorials, books, and videos. If the lesson is one of a series, also read [sets-and-sequences.md](sets-and-sequences.md).

## Rules

**Let readers feel the problem before giving them the feature.** Before introducing a feature or abstraction, let the reader meet the problem it solves in what they've built so far. Either have them do the task the laborious way, or point to the duplicated code, hardcoded value, unhelpful output, or bug in their current work, so they feel the cost instead of being told about it. Then present the feature as the fix. A unit may end on a known gap that the next unit fills.

**Let failures recur while each one teaches.** Let learners hit an error on purpose whenever the error introduces the next concept, or whenever the skill being taught is reading a tool's diagnostics or a fail-then-fix workflow. Show the failing attempt and its exact message, and let the message drive the next step. Stop when a failure teaches nothing new.

**Tell learners where difficulty is normal.** Before learners reach them, name the places where people usually get stuck, and say that difficulty there is normal and expected. Tell them which details they can leave partly understood for now.

**Use "we" for shared narrative work.** In narrative, build-along material read in order, write as one knowledgeable person talking to another. Use "we" or "let's" for work you and the reader do together, "you" for what the reader alone does or observes, and imperatives for discrete steps. A vivid comparison or a light joke is fine when it makes an idea stick. Don't flatten the prose into neutral summary.

**Show code changes by file size, with full-code checkpoints.** In a step-by-step build, show the whole file with the changed lines marked while the file is short. Once a whole-file view would bury the change, switch to an anchored excerpt (the file name plus a few surrounding lines) with the changed lines marked. Explain the marking notation the first time it appears. Once a repeated scaffolding pattern is established, you may show only the relevant part and say once what the reader must add. At regular checkpoints, show the complete current code, or link to the tested full version, so readers who have drifted can catch up.

**Tell readers how to check their own work.** At each exercise and checkpoint, tell readers what to try and what they should see. Where a change could overshoot, or is meant to preserve behavior (a refactor), also say what should not happen or not change, and confirm it with unchanged output and passing automated checks.

**Show several solutions when judgment is the goal.** Keep a single path for a reader's first success. In worked solutions where more than one answer is correct, and in material whose goal is design judgment (books, courses, later tutorials, exercises), build two or more working solutions and say openly what each gains or costs.

**End lessons with a short, fixed closing that points forward.** In a sequence of lessons (tutorial parts, chapters, course modules, episodes), end every lesson with the same short closing, in one of two forms:
- one sentence naming what the reader should now be comfortable with, followed by a pointer to the next lesson; or
- a brief recap of the concepts covered, followed by a preview of the next lesson.

A list of skills gained is one form of recap, not the only one. Keep the closing brief, and don't walk back through the page's content.

## Gotchas

- Introducing a feature first and justifying it by assertion, so readers don't see why they need it.
- Including one token error and then only success paths, so learners never practice reading the diagnostics they'll meet.
- Leaving learners to read normal confusion as personal failure.
- Writing a narrative tutorial as uniform second-person imperatives that read like an appliance manual.
- Showing unanchored fragments throughout, or the full file at every step, with no checkpoint for readers who drift.
- Setting exercises and refactoring steps with no way for readers to tell whether they succeeded.
- Presenting one canonical answer where several are right, so readers conclude it is the only one.
- Closing each lesson with a long conclusion that repeats it, or forcing a skills list where one sentence and a pointer onward would serve better.
