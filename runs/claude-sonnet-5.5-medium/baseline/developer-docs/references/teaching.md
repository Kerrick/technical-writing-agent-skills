# Teaching: tutorials, courses, and lessons

Read this when the goal is for the reader to *learn*, not just look something up. The failures here are cognitive overload, steps that don't work, and the curse of knowledge (you forgot what it was like not to know).

## Before drafting

1. Write the **outcome** as an observable thing the learner can do or see at the end ("You'll have a deployed endpoint that returns your name"), not a topic ("Learn about routing").
2. List **prerequisites** as concrete skills and installed tools. Link to where each is learned. Do not teach them inline.
3. Break the outcome into the smallest sequence of **concepts** needed, ordered so each uses only what came before. If a step needs a concept not yet taught, either reorder or give a one-line "for now, treat this as a black box that..." and promise to return to it.
4. Pick a **running project** that is small, real enough to care about, and grows by accretion. A tutorial where the learner ends with something they might keep teaches better than disconnected snippets.

## Structure of a tutorial

- **Opening:** what you'll build (screenshot or output), time estimate, prerequisites, versions.
- **Early win:** the first success within a few minutes, even if crude. Success early buys patience for later difficulty.
- **Steps:** each one action plus its visible result. Tell the learner what they should see so they know they're on track.
- **Checkpoints:** every few steps, a state they can compare against (expected output, a file listing, a link to a repo commit/tag for that step).
- **Recovery:** at the points where people commonly fail, say what the failure looks like and how to fix it, right there. Collect the rest at the end.
- **Close:** recap what was built and learned in a few lines; point to next tutorial, the how-to guides, and reference. Optionally list "going further" exercises.

## Pedagogy rules that change what you write

- **Manage cognitive load.** Working memory holds a few new things at once. Introduce one new concept per step. Remove anything incidental: extra options, alternative approaches, tangents. Choices belong in how-to guides.
- **Worked example, then fade.** Show a complete worked solution, then give a similar task with part removed, then a task with most removed. Moving from reading to doing is how skill transfers; pure reading produces false confidence.
- **Concrete before abstract.** Run the code, see the effect, then name the principle. Then give a second example in a different context so the learner sees what varies and what is invariant.
- **Predict-then-reveal.** Ask "what do you think this prints?" before showing output. Prediction errors are where learning happens. Use sparingly; once or twice per tutorial.
- **Retrieval and spacing.** Reuse earlier concepts in later steps rather than just revisiting them in a summary. Short end-of-section questions that require recall beat re-reading. Space related practice across sections.
- **Common misconceptions.** Identify the two or three wrong mental models learners reliably form (check issue trackers, forum questions, and your own surprise points) and address them directly, saying why the wrong model is tempting.
- **Reduce extraneous load.** Keep code blocks short; highlight or annotate the line that is new in this step; show diffs when extending a file; don't re-paste unchanged code unless full-file context is needed, in which case mark what changed.
- **Name the "why" of each step in a clause,** not a paragraph. The learner who understands the purpose can recover when their environment differs.
- **Normalize errors.** Deliberately trigger and read a common error once so learners recognize it and aren't afraid of it. Teach how to read an error message and a stack trace.
- **Don't teach by apology.** Avoid "this is a bit tricky." If something is tricky, give the tool for handling it.
- **Exercises:** each tests exactly the concept just taught, has a checkable outcome, and comes with a solution that is hidden or placed separately plus a brief note on common wrong answers. Mark difficulty. Avoid trick questions.

## Tutorial gotchas

- Tutorials break silently when dependencies drift. Pin versions, supply a lockfile or starter repo, and state when it was last verified. Run the entire tutorial from a clean directory, using only the instructions, before delivering.
- Don't make learners type large amounts of boilerplate that teaches nothing; supply a starter and focus effort on the new idea.
- "Obvious" steps (opening a terminal, saving the file, restarting the server) are the ones people skip and then get stuck on. State them at first use, not every use.
- Windows/macOS/Linux divergence: give commands for each, in tabs or labeled blocks, or state that the tutorial assumes one and why. Never leave it implicit.
- Consistency between prose and code: variable names, file paths, and port numbers in text must match the code exactly.
- A tutorial that ends without a working result is worse than none. If the learner's last step fails, they remember failure.
- Learners copy-paste. Make the pasted version the correct one; never put output or prompts in the same block as commands.

## Levels and audience

- **Absolute beginner:** define every term, show every step, explain tool use (editor, terminal). Keep sessions short.
- **Experienced in another language/framework:** map to what they know ("this is like X in Y, except..."), skip fundamentals, and call out differences that bite. Analogies must be flagged where they break down.
- **Expert evaluating you:** skip the tutorial; give a quickstart plus architecture explanation and a reference.
- When a tutorial serves mixed audiences, pick the lower level for the main path and let experts skim via clear headings. Do not write for everyone at once.

## Estimating and testing the learning

- Ask a person of the target level to follow it, and watch where they stop, reread, or ask a question. Each stop is a defect in the text. If no person is available, simulate by following literally from a clean environment and noting each assumption you rely on.
- Track time per step. If a step takes far longer than the others, split it.
- Revise using what confused real learners, not what you think is elegant.
