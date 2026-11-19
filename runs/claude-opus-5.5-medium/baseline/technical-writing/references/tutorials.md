# Tutorials and quickstarts

A tutorial gives a learner a first success, and the confidence that comes with it. It is not where they learn everything about the subject. The author owns the outcome: if a reader follows every step and it fails, the tutorial failed.

A **quickstart** is the shortest tutorial, from nothing to one visible working result. Aim for under five minutes of reader time. A **tutorial** proper builds something small but real across several steps and introduces the core concepts along the way.

## Template

```markdown
# Build <concrete thing> with <tool>

<One or two sentences: what you'll have at the end, ideally with a
screenshot or the final output.>

## Before you begin

- <Tool> <exact version> or later (`<command to check the version>`)
- <Prior knowledge, stated as skills: "You can run commands in a terminal">
- About <N> minutes

## <Subgoal 1, phrased as its purpose: "Create the project">

1. <Action.> <What you see.>
2. ...

<Checkpoint: what should work now, and how to confirm it.>

## <Subgoal 2>

...

## What you learned

- <Skill, not feature: "Define a route that renders a template">
- ...

## Next steps

- <The next tutorial in sequence>
- <The how-to guides they'll want first>
- <The explanation page for the concept they just used without fully understanding>
```

## Rules

- **One path.** Make every choice for the learner: one OS default, one package manager, one database. Each choice offered is a place to get lost. Use tabs for platform variants only when there's no way around them.
- **Visible progress every step or two.** Each subgoal ends with a checkpoint the reader can see: output, a page in the browser, a passing test. A long run of steps with nothing to check means an error in step 3 surfaces in step 11.
- **At most one new concept per step.** Name it when it appears, say just enough to keep going, and link to the explanation page. Learners don't need the full model to take the next step, and stopping to explain everything breaks the flow of doing.
- **Label subgoals.** Group steps under headings that name their purpose ("Connect to the database"), not their mechanics ("Edit config/database.yml"). Subgoal labels are how learners later recall the shape of the procedure.
- **A running example that grows.** One small, realistic project carried through the whole tutorial beats a fresh toy per section. Learners spend their attention on the new concept, not on re-reading a new domain.
- **Make them type.** Show code they write into their own files; avoid "download the finished project" until the end.
- **Anticipate failure.** After a step that commonly fails, say what failure looks like and how to recover: "If you see `EADDRINUSE`, another process is using port 3000. Stop it, or run with `PORT=3001`."
- **Teach one error on purpose.** Once in a longer tutorial, it can help to let the reader hit a common error, read it, and fix it. They'll recognize it later. More than once is a detour.
- **Recap skills, not features.** "What you learned" lists what the reader can now do.
- **Test from scratch.** Follow the tutorial on a clean environment with the stated versions. Do this again whenever a dependency changes.

## Worked examples and fading

In a multi-part tutorial or course, move responsibility to the learner gradually:

1. **Worked example**: you do the whole thing and explain each step.
2. **Completion problem**: you do most of it and the learner fills a gap ("Now add the `destroy` action the same way").
3. **Independent problem**: the learner does a similar task with only the goal stated.

Skipping straight to step 3 overloads novices. Staying at step 1 forever bores them and they don't learn to do it alone.

## Common failures

- Prerequisites that silently assume a tool, account, or credential.
- Steps that work only because of state left over from the author's machine.
- Detours into options, configuration matrices, or history. Those belong on how-to and explanation pages.
- A finale that is the first time anything visibly works.
