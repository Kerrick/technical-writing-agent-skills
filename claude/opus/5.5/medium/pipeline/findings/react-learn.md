Source: react.dev Learn, commit 54cd2c40

> Quotes and descriptions in this file are from the [React documentation](https://react.dev/learn) ([reactjs/react.dev](https://github.com/reactjs/react.dev)), by its contributors, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quotes are short, and used to compare and criticize.

# Deltas: react.dev Learn vs. the `technical-writing` skill

Compared: the 51 Learn pages under `src/content/learn/` in Next-button order, plus `CONTRIBUTING.md` ("Technical Writing Tips", "Guidelines for Text", "Guidelines for Code Examples"), against the skill at `~/.agents/skills/technical-writing/` (`SKILL.md` and `references/*.md`). Learn page paths below are relative to `src/content/learn/`. Skill paths are relative to the skill folder.

## 1. Missed principles

### 1.1 Ask the reader to predict, inline, before revealing behavior

The pages often stop mid-explanation and ask the reader to guess the outcome before showing it. These prompts sit in the body text, not in end-of-page exercises.

- `state-as-a-snapshot.md`: "Try to guess what clicking this button will alert", then "Have a guess!" before the timed version.
- `queueing-a-series-of-state-updates.md`: "What do you think `number` will be in the next render?", asked twice.
- `responding-to-events.md`: "Which handlers do you think will fire when you click a button?"

Skill: `references/learning-science.md:31` and `references/books.md:49` put prediction only in end-of-chapter questions and exercises. Inline prediction during exposition is absent.

### 1.2 Give the reader a named reasoning procedure and reuse it across pages

One page introduces a mental technique the reader can apply themselves: substitute the current values into the code and read what happens. Later pages and solutions use it again by name.

- `state-as-a-snapshot.md` introduces "mentally substituting state variables with their values" and calls it "the substitution method".
- `synchronizing-with-effects.md` reuses it ("Let's mentally substitute `roomId`…") to explain Effects.
- The traffic-light solution in `state-as-a-snapshot.md` tells the reader to verify the answer "by applying the substitution method".
- `queueing-a-series-of-state-updates.md` turns the same idea into step-by-step trace tables.

Skill: `references/learning-science.md:53` says to make the model explicit with a diagram or a state trace. It doesn't say to hand the reader a named, repeatable procedure and keep returning to it. Absent.

### 1.3 Rebuild the mechanism in miniature

To show that a feature isn't magic, the pages write a small working version of it with no framework, or have the reader write one.

- `state-a-components-memory.md`: a DeepDive builds a simplified hook store, labeled "This example **doesn't use React**".
- `queueing-a-series-of-state-updates.md`: the challenge "Implement the state queue yourself".
- `extracting-state-logic-into-a-reducer.md`: the challenge "Implement `useReducer` from scratch".
- `referencing-values-with-refs.md`: shows refs written on top of state.
- `reacting-to-input-with-state.md`: the challenge to restructure imperative code "without React".

Skill: `references/explanation.md:11` says to make the machine visible with names and a diagram. A runnable miniature reimplementation is absent.

### 1.4 Chapter overview pages that let readers skim or skip ahead

Each chapter opens with a page that gives every topic in the chapter a short runnable example and a link. It closes by offering two exits: read the chapter page by page, or skip to the next chapter if the topics are familiar.

- `describing-the-ui.md`, `adding-interactivity.md`, and `managing-state.md` all end with "Or, if you're already familiar with these topics, why not read about …?"
- `escape-hatches.md` follows the same overview structure.

Skill: absent. `references/books.md` covers front matter and chapter templates but not a per-chapter skim page that lets experienced readers skip.

### 1.5 Offer a hint between the problem and the solution

Many challenges include a hint, a nudge that is smaller than the answer.

- `your-first-component.md` ("Fix the return statement") warns where the semicolon goes.
- `keeping-components-pure.md` ("Fix a broken clock") reframes the problem: "Rendering is a *calculation*".
- `rendering-lists.md` and `preserving-and-resetting-state.md` add hints that point at the relevant idea without solving the challenge.

Skill: absent. `references/books.md:47-55` lists exercise types and where to put solutions, but has no intermediate hint tier.

### 1.6 Solutions present alternatives and explain the trade-off

Solutions often give more than one correct answer and say when each one is better.

- `conditional-rendering.md` (Drink): an `if` refactor first, then a data-object version that removes the condition entirely.
- `keeping-components-pure.md` (story tray): two fixes, with the caveat that copying only protects the top level.
- `choosing-the-state-structure.md` (multiple selection): an array first, then a `Set`, with the reason being the cost of each lookup.

Skill: absent. The skill describes exercises but not what a good solution contains.

### 1.7 Every exercise says how learners can check their own work

Challenges spell out how to confirm a fix worked.

- `javascript-in-jsx-with-curly-braces.md`: "To check that your fix worked, try changing the value of `imageSize`…"
- `synchronizing-with-effects.md` (focus challenges): "To verify your solution, press…", including a negative check (a checkbox click must *not* focus the input).
- `passing-props-to-a-component.md`: "Verify that your changes work by…"

Skill: `references/tutorials.md:47` asks for checkpoints after tutorial steps. Acceptance criteria inside exercises are absent.

### 1.8 Invite small changes to working examples

Readers are repeatedly told to change one thing in a working example and watch the result.

- `javascript-in-jsx-with-curly-braces.md`: "Try changing the `name`'s value…"
- `render-and-commit.md`: "Try commenting out the `root.render()` call…"
- `thinking-in-react.md`: edit the initial filter value and watch both the input and the table update.

Skill: absent. "Modify" (`references/books.md:52`) appears only as a formal exercise type, not as an inline invitation.

### 1.9 Side-by-side tables for pairs that are easy to confuse

Correct and incorrect forms, or two similar concepts, are set next to each other in a table.

- `responding-to-events.md`: a "passing a function (correct)" vs. "calling a function (incorrect)" table, given twice.
- `updating-arrays-in-state.md`: an "avoid" vs. "prefer" table of array methods.
- `referencing-values-with-refs.md`: refs vs. state.
- `importing-and-exporting-components.md`: default vs. named export and import syntax.

Skill: `references/explanation.md:19` uses comparison tables only for choosing between products or options. Absent for confusable syntax and concepts.

### 1.10 Mark anti-pattern code clearly inside the code itself

Bad examples carry a visible marker in a comment, so a reader who copies only the block still knows it is wrong.

- `you-might-not-need-an-effect.md`: comments that start with "🔴 Avoid" and "✅ Good" throughout.
- `your-first-component.md`: "🔴 Never define a component inside another component!"
- `reusing-logic-with-custom-hooks.md`: lists of names marked 🔴/✅, plus marked code.

Skill: absent. The code rules (`SKILL.md:84-94`) say nothing about flagging wrong examples.

### 1.11 Say what can be left half-understood, and that confusion is expected

The pages tell learners which parts they can skip or understand later.

- `tutorial-tic-tac-toe.md`: "If the code doesn't make sense to you yet … don't worry!"
- `thinking-in-react.md`: "It's okay if the difference still feels fuzzy on the first read."
- `state-a-components-memory.md`: after the internals DeepDive, "You don't have to understand it to use React".

Skill: `references/learning-science.md:61-65` covers motivation but not explicit permission to defer understanding. Absent.

## 2. Corrections

### 2.1 Showing a failure first is a core method, not something to do once

The skill says to teach one error on purpose "once in a longer tutorial. … More than once is a detour." react.dev uses broken-first on almost every page: a naive version that fails, the reason it fails, then the fix.

- `state-a-components-memory.md`: "this **won't work** (you can try it!)"
- `updating-objects-in-state.md`: the dot "stays in the initial position".
- `writing-markup-with-jsx.md`: pasting HTML as-is "will not work".
- `tutorial-tic-tac-toe.md`: walks into the infinite-render error and the missing-key warning on purpose.
- `reacting-to-input-with-state.md`: opens with the imperative version before the declarative one.

Skill: `references/tutorials.md:53`.

### 2.2 Pages in a sequential path can depend on earlier pages

The skill says every page must stand alone for someone arriving from search. CONTRIBUTING:21 requires the opposite for Learn: each article "builds on the knowledge from the previous ones", with no forward references. Pages refer back openly.

- `queueing-a-series-of-state-updates.md`: "as you might recall from the previous section".
- `state-as-a-snapshot.md`: "On the previous page, you saw…"
- `responding-to-events.md`: ends by pointing to "the next page".

Search arrivals are handled with links back to earlier pages, and with a separate Reference section for lookup (CONTRIBUTING:23).

Skill: `SKILL.md:81`.

### 2.3 A short recap is useful on learning pages

The skill says not to end pages with a summary that restates them. Every Learn page ends with a Recap that restates its rules in bullets, for example `keeping-components-pure.md` and `passing-props-to-a-component.md`. CONTRIBUTING:21 says Learn "also serves as a reference manual for React concepts", and the Recap is what a returning reader scans. A recap of rules is a lookup aid, not a restatement of prose.

Skill: `SKILL.md:101`.

### 2.4 One page can mix modes if the extra material is clearly fenced off and optional

The skill says to split pages that mix modes. Learn pages combine a tutorial walkthrough, explanation, and exercises on one page. They keep it manageable by putting tangents in labeled, collapsible asides that readers can skip.

- The "Props vs State" DeepDive in `thinking-in-react.md`.
- The "Why does React care about purity?" DeepDive in `keeping-components-pure.md`.
- The data-fetching alternatives DeepDive in `synchronizing-with-effects.md`.

Skill: `SKILL.md:44`.

### 2.5 Solutions can follow the question if the reader has to choose to reveal them

The skill says to put solutions in an appendix, not right after the question. On react.dev each Solution comes directly after its Challenge and Hint, collapsed until the reader opens it (every page with a `<Challenges>` block). What matters is that the answer takes a deliberate action to see, not where it sits. An appendix is one way to do that in print.

Skill: `references/books.md:55`.

### 2.6 Show partial highlighted snippets for steps, and the full code at checkpoints

The skill says to show a change in context, "Not the whole file every time." The tic-tac-toe tutorial gives each step as a short snippet with the changed lines highlighted. It then repeats the full current file at checkpoints ("At this point your code should look something like this", "Your updated code should look like this", "This is what your code should look like"), so a reader who has fallen behind can catch up. CONTRIBUTING:108 also encourages frequent line highlighting.

Skill: `SKILL.md:89`.

### 2.7 Warnings are worth it for common mistakes that fail silently, not only for data loss, security, and money

Pitfall callouts flag frequent beginner errors that are easy to miss.

- `your-first-component.md`: capitalized component names, and the missing parentheses after `return`.
- `conditional-rendering.md`: "Don't put numbers on the left side of `&&`".
- `rendering-lists.md`: a block-body arrow function needs an explicit return.

Each callout names one specific failure, so the callouts stay credible.

Skill: `SKILL.md:79`.

## 3. House conventions

- Every example is a live, editable sandbox with a "Fork" option. CONTRIBUTING:31-33 adds a rule to describe the result in prose so the lesson still works offline. That rule repeats the skill's existing line (`SKILL.md:88`). The sandbox itself doesn't carry over to other docs.
- Framework concept names are capitalized ("Hooks", "Effects", "Transitions"; CONTRIBUTING:54). This is a house style choice. Absent from the skill.
- JavaScript code style: named `function` declarations at top level, `const` over `let`, semicolons, Prettier defaults (CONTRIBUTING:41-53). Language-specific.
- A shared pool of sample data appears across many pages, drawing on real scientists, sculptures, and places (for example `describing-the-ui.md`, `state-a-components-memory.md`, `rendering-lists.md`). This is an editorial choice, not a teaching principle.

## 4. Where react.dev falls short

- **Words that suggest the task is easy.**
  - `tutorial-tic-tac-toe.md`: "Now you just need to copy-paste a few times".
  - `build-a-react-app-from-scratch.md`: "Starting from scratch is an easy way to get started".
  - `add-react-to-an-existing-project.md`: "Of course, you don't actually want to clear…"

  Skill: `SKILL.md:73`.
- **Marketing adjectives.**
  - `build-a-react-app-from-scratch.md`: a "seamless development experience".
  - `add-react-to-an-existing-project.md`: "all the wonderful packages".
  - `scaling-up-with-reducer-and-context.md`: "a powerful way to scale your app".

  Skill: `SKILL.md:80`.
- **Install commands not pinned to a version.**
  - `creating-a-react-app.md`: `npx create-next-app@latest`, `npx create-react-router@latest`.
  - `react-compiler/installation.md`: `babel-plugin-react-compiler@latest`, `eslint-plugin-react-hooks@latest`.

  Skill: `SKILL.md:93`.
- **Stale or contradictory facts between pages.**
  - `editor-setup.md` recommends `eslint-config-react-app`, the Create React App preset, while `installation.md` says Create React App "has been deprecated".
  - `typescript.md` lists Remix (linked to 1.19.2 docs) and Gatsby as the frameworks, while `creating-a-react-app.md` recommends Next.js, React Router, and Expo.
  - `render-and-commit.md` links to the legacy reactjs.org Performance page.

  Skill: `SKILL.md:52` (verify against the source, record the version).
- **Snippets that would fail if run or checked.**
  - `thinking-in-react.md` labels a block `json`, but its keys are unquoted, so it isn't valid JSON.
  - `updating-arrays-in-state.md` explains the Immer version with a snippet that calls `updateMyTodos`, a name that isn't in the example (the example uses `updateMyList`).
  - In `choosing-the-state-structure.md`, the first flattened `places.js` has entry `39` with `id: 40`.

  Skill: `SKILL.md:62`.
- **Learning objectives that can't be checked.** Several "You will learn" items are about knowing or why, not about doing.
  - `your-first-component.md`: "What a component is".
  - `state-a-components-memory.md`: "Why state is called local".
  - `describing-the-ui.md`: "Why understanding your UI as trees is useful".

  Skill: `SKILL.md:48`, `references/learning-science.md:57-59`.
- **Options listed with no default.**
  - `build-a-react-app-from-scratch.md` presents Vite, Parcel, and Rsbuild as equals.
  - Its data-fetching section lists three REST libraries and two GraphQL libraries without a recommendation.
  - Staying neutral across the ecosystem may be deliberate, but it leaves a new reader to choose alone.

  Skill: `SKILL.md:102`.
- **"Next steps" that point backward in the reading order.** `installation.md` and `setup.md` both end with "Head to the Quick Start guide", but in the Next order a reader reaches them after the Quick Start.

  Skill: `references/tutorials.md:39` (point to the next item in sequence).
- **Analogies left open-ended.** `render-and-commit.md` (React as a waiter, components as cooks) and `referencing-values-with-refs.md` (a "secret pocket") never say where the analogy stops holding. The CSS-inheritance analogy in `passing-data-deeply-with-context.md` does state its limit, so the site can do this when it chooses to.

  Skill: `references/explanation.md:13`.

## Confirmations

- `references/books.md:9` (find backward edges in the concept order) is matched by CONTRIBUTING:21's rule that a reader never has to "look ahead" for a definition.
- `SKILL.md:62` and `references/books.md:77` (run it yourself; watch someone from the target audience use it) are matched by CONTRIBUTING:25-27, "Try to follow your own instructions", with bonus points for watching someone else.
- `SKILL.md:103` (quote error messages exactly) is matched by literal error and warning blocks, for example in `tutorial-tic-tac-toe.md` and `rendering-lists.md`.
- `references/explanation.md:14` (address the misconception directly) is matched by the OOP-instances DeepDive in `conditional-rendering.md` and "Objects are not really nested" in `updating-objects-in-state.md`.
- `SKILL.md:25` (separate pages for novices and experts) is matched by CONTRIBUTING:21-23: Learn leaves corner cases out on purpose, and Reference is exhaustive.

## Abstracted

### From missed principles

1. In the middle of an explanation, stop and ask the reader to predict what will happen before you show it. Save prediction for more than the exercises at the end.
2. Give learners a named reasoning procedure they can use to work out behavior themselves. Use it by name again in later lessons and in worked solutions so it becomes habit.
3. When a feature seems like magic, show or assign a tiny working reimplementation of it with no dependencies, simplified enough to read in one sitting.
4. Open each multi-page unit with an overview that previews every topic in a sentence or two plus a small example. End it with two clear exits: work through the unit in order, or skip to the next unit if the material is familiar.
5. Between an exercise and its solution, offer a hint that points to the relevant idea without giving the answer.
6. In worked solutions, show more than one correct answer when there is one, and say what each version gains or costs.
7. Give every exercise a test the learner can run to know they succeeded, including a check that something that should not happen didn't.
8. In working examples, invite the reader to change one specific value or line and watch what changes.
9. When two forms or concepts are easy to mix up, put them side by side in a table that labels which is right, or what distinguishes them.
10. Mark every incorrect or discouraged code sample as wrong inside the code block itself, so someone who copies only the block still sees the warning.
11. Tell learners which details they can leave partly understood for now, and that confusion on a first reading is normal.

### From corrections

12. Use "show the naive attempt, show it fail, explain why, then fix it" as a regular teaching move whenever a misconception is likely, not as a one-time device.
13. Pages in a deliberately ordered learning path may depend on earlier pages. Link back to what they rely on, and serve readers who arrive cold with a separate lookup section rather than by making every lesson self-contained.
14. Lessons that also serve as a later reference should end with a short bulleted recap of the rules covered, written to be scanned on return.
15. A teaching page may combine a walkthrough, explanation, and practice, as long as tangents and deeper material sit in clearly labeled asides that readers can skip.
16. Solutions can sit right after their exercise as long as the reader has to take a deliberate action to see them. Where the solution appears matters less than making the reader try first.
17. In step-by-step builds, show each step as a short snippet with the changed lines marked, and at regular checkpoints show the complete current code so readers who have drifted can catch up.
18. Use warning callouts both for serious risks and for common mistakes that fail silently. Keep each one to a single named failure so readers keep trusting them.
