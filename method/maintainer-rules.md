# Maintainer rules

Rules the maintainer sets for every skill in this repository. They usually come from correcting an agent: a habit the model knows better than but keeps, which no comparison with sources would find.

Every run gets them. `method/scripts/build_kept.py` adds them to the writer's `kept.md`, after the rules the method found, with the Kind "set by the maintainer". The writer places them like any other rule, and the placement check confirms each one is in the skill. A skill the method doesn't make gets them by hand.

Add a rule here when you've corrected the same habit more than once, or once where the habit did real harm. Keep each rule in the shape below, so the script can read it. When an eval shows an agent following a rule without being told, consider removing it.

### No placeholders on disk
- **Rule:** Never write a placeholder, a question, or a note to the maintainer into any file. The maintainer asked for the writing so they don't have to do it, so what you write is final. Bring up in chat only what truly needs their judgment, where a wrong call would do real harm, and keep that as short as you can. For everything else, take the answer the evidence supports that claims the least on the maintainer's behalf, write it as final, and list those calls in your report.
- **Applies to:** every page
- **Without it:** An agent leaves markers like `TODO(verify)` or `[TO CONFIRM]` in the files, handing the work back to the person who asked for it.

### State verified facts plainly
- **Rule:** Most sentences an agent feels the urge to qualify aren't overclaiming anything. Before you qualify, shrink, or cut a sentence, name the specific false or unverified fact it states. If you can't name one, it isn't an overclaim, so leave it as written. A statement of what something is for, or what it does, is not an overclaim. Never attach how narrow the proof was ("tested with", "in our testing", "as far as we know", "should work").
- **Applies to:** every page
- **Without it:** An agent qualifies, shrinks, or cuts sentences that were true as written, so readers trust the page less than the evidence deserves.

### State a limit only where it changes what the reader can do
- **Rule:** State a limit only when it changes what the reader can do or should expect: a platform, a version, a model, a prerequisite, a risk to their data. State it once, as a fact, where the page keeps its caveats.
- **Applies to:** every page
- **Without it:** An agent lists limits that change nothing for the reader, or repeats one limit in several places, so the limits that matter are hard to find.

### Don't narrate the project's proof
- **Rule:** Proof narration is a sentence, in a page for users, about how far the project's own testing has got. It either apologizes ("untested", "not yet tried on Windows", "no CI job runs on the oldest version") or boasts ("CI builds and runs every example on every change", a test count, a list of the machines it has run on). Both tell the reader about the maintainer's work, not about what the reader can do. Cut it, or move it to contributor documentation, and keep only the fact it implies for the reader, such as a platform or a minimum version, stated plainly where the page keeps its caveats. A measured result the reader can weigh, such as a benchmark with its numbers, is evidence, not proof narration.
- **Applies to:** every page
- **Without it:** An agent narrates the project's proof in user-facing pages, apologizing for tests not yet run or boasting about what CI does, which tells the reader nothing they can act on.
