Source: react.dev Learn, commit 46a54e05

> Quotes and descriptions in this file are from the [React documentation](https://react.dev/learn) ([reactjs/react.dev](https://github.com/reactjs/react.dev)), by its contributors, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quotes are short, and used to compare and criticize.

# Comparison of react.dev Learn against the baseline `developer-docs` skill

Paths: react.dev files are under `src/content/learn/` (shortened below) unless marked `CONTRIBUTING.md`. Skill files are under `work/developer-docs/` (`SKILL.md`, `references/teaching.md`, `references/reference-and-guides.md`, `references/books-and-video.md`). The skill was not edited. Quotes are short and only where the wording matters.

CONTRIBUTING.md frames the intent: Learn is a step-by-step path in which "the reader can start with the first article and work their way to the last ... without ever having to 'look ahead' for a definition" and which "also serves as a reference manual for React concepts" (CONTRIBUTING.md:21). Corner cases skipped in Learn belong in the exhaustive API reference (CONTRIBUTING.md:23). Different sections intentionally differ in style (CONTRIBUTING.md:17).

## 1. Missed principle

**M1. Open a concept with a failure the reader can reproduce, then name the cause.**
- Pattern: `state-a-components-memory.md:22` "However, this **won't work** (you can try it!)" before `useState` is introduced; `tutorial-tic-tac-toe.md:390` "Oh no! The squares are all in a single line"; `tutorial-tic-tac-toe.md:560` "Oh no! You lost the numbered squares"; `synchronizing-with-effects.md:94` "You might be tempted to try to call `play()` ... but that isn't correct".
- Skill: `SKILL.md:37` says to give "a minimal working example before the abstract description"; the failure-first idea appears only for books (`books-and-video.md:45`) and as a one-off error to normalize (`teaching.md:31`). Not stated for tutorials or concept pages.

**M2. Mark a term of art that shares a spelling with an ordinary word, and say so once.**
- `synchronizing-with-effects.md:35`: capitalized "Effect" is the React-specific meaning; the broad idea is called "side effect". Style rule at `CONTRIBUTING.md:50` (capitalize concept names).
- Skill: `SKILL.md:38` (one term per concept, define at first use) does not cover separating a specialised sense from the everyday sense of the same word. `books-and-video.md:35` mentions capitalization only as a style-sheet item.

**M3. Label wrong or discouraged code inside the code block.**
- Pattern, 32 marker occurrences across 8 files: `you-might-not-need-an-effect.md:42` "// 🔴 Avoid: redundant state and unnecessary Effect"; `your-first-component.md:185` "// 🔴 Never define a component inside another component!"; `synchronizing-with-effects.md:610` "// 🚩 This wont fix the bug!!!".
- Skill: `SKILL.md:43` and `teaching.md:43` make blocks safe to paste but say nothing about marking bad examples in-block. Absent.

**M4. Name simplifications as simplifications; record omitted corner cases where the exhaustive page lives.**
- `synchronizing-with-effects.md:210` "This example is very simplified and incomplete"; `state-a-components-memory.md:543` "// How useState works inside React (simplified)"; `extracting-state-logic-into-a-reducer.md:456` "similar to what React does"; the duty to move skipped edge cases to the reference is `CONTRIBUTING.md:23`.
- Skill: absent (no mention of flagging simplifications; `SKILL.md:35` only orders edge cases after the common case).

**M5. Say which parts can be skimmed, and that partial understanding is expected.**
- `tutorial-tic-tac-toe.md:1526` "Don't worry too much about the `calculateWinner` function; it's not specific to React"; `tutorial-tic-tac-toe.md:197`; `thinking-in-react.md:247` "It's okay if the difference still feels fuzzy on the first read"; `state-a-components-memory.md:727` "You don't have to understand it to use React".
- Skill: `teaching.md:23` says to remove incidental material; `teaching.md:32` forbids apology. Neither covers keeping needed-but-incidental material and labelling it skippable. This is scope reassurance, not apology, so it does not conflict with `teaching.md:32`.

**M6. Offer parallel routes for different learning preferences, with a jump for readers who already know the material.**
- `tutorial-tic-tac-toe.md:13` (learn-by-doing route vs "learning each concept step by step"); `index.md:7` (a quick tour of "80%" of concepts); every chapter overview ends with a page-by-page route and "if you're already familiar ... read about" the next chapter: `describing-the-ui.md:560-562`, `adding-interactivity.md:798-800`, `managing-state.md:1013-1015`. Motive: `CONTRIBUTING.md:19` "cater to different learning styles".
- Skill: `teaching.md:49-50` covers experts skimming via headings and picking the lower level. No parallel routes, no skip-ahead pointer at the end of overviews.

**M7. Preview a multi-step process as a short verb-led list, then walk each step in that order.**
- `reacting-to-input-with-state.md:146-147` (five bold verbs before "Step 1..."); `importing-and-exporting-components.md:61-62` (Make / Export / Import); `extracting-state-logic-into-a-reducer.md:186-187` (Move / Write / Use); `state-a-components-memory.md:161-162`.
- Skill: `SKILL.md:36` covers numbered one-action steps; previewing the whole shape first is absent.

**M8. Give the reader a mechanical way to trace behaviour in their head, and reuse it.**
- `state-as-a-snapshot.md:206`, `:244`, `:417` ("the substitution method"); `synchronizing-with-effects.md:889` reuses it ("Let's mentally substitute"); `lifecycle-of-reactive-effects.md:165` retells one scenario from two viewpoints; the tables of queued steps in `queueing-a-series-of-state-updates.md`.
- Skill: absent (nothing about teaching a tracing method; `teaching.md:25` covers worked examples only).

**M9. Write some exercises as nearly-working code with a seeded defect, with hints about where such defects hide.**
- Titles: `state-a-components-memory.md:1328` "Fix a crash"; `preserving-and-resetting-state.md:1989` "Fix misplaced state in the list"; `synchronizing-with-effects.md:1465` "Fix fetching inside an Effect". Hints: `lifecycle-of-reactive-effects.md:1128` "If you see a linter rule being suppressed, remove the suppression! That's where the mistakes usually are."; `separating-events-from-effects.md:989`.
- Skill: `teaching.md:33` describes exercises with checkable outcomes and wrong-answer notes, with nothing on diagnosis-style exercises or diagnostic hints.

**M10. Keep the main path linear by fencing optional depth in clearly labelled, skippable blocks.**
- 41 collapsible deep-dive blocks across 28 pages, e.g. `state-a-components-memory.md:525` (how the mechanism works inside), `keeping-components-pure.md:148`, `updating-objects-in-state.md` (why mutation is discouraged). The main text stays usable without them.
- Skill: `teaching.md:23` says to remove tangents and extra options; `books-and-video.md:21` allows sidebars "sparingly". Implies the opposite for tutorial-type pages.

**M11. Link to the exact section that defines a concept, and keep heading anchors stable.**
- `synchronizing-with-effects.md:889` links `/learn/state-as-a-snapshot#rendering-takes-a-snapshot-in-time`; `removing-effect-dependencies.md:112` links `/learn/lifecycle-of-reactive-effects#effects-react-to-reactive-values`; every heading carries an explicit identifier (`{/*...*/}`), so retitling does not move anchors.
- Skill: `SKILL.md:68` only requires that links and anchors resolve; section-level linking and pinned anchors are absent.

## 2. Correction

**C1. "No choices / remove alternatives" in tutorials is too absolute.**
- `tutorial-tic-tac-toe.md:1159-1177`: names the call-it-immediately attempt, shows it fails, and describes a longer alternative ("You could fix this by creating a function like `handleFirstSquareClick`") before choosing the shorter one.
- Skill: `SKILL.md:26` ("no choices"), `teaching.md:23` ("alternative approaches" removed).

**C2. Prediction prompts have no fixed quota.**
- `state-as-a-snapshot.md:177`, `:213`, `:262` (three prompts on one page), plus `adding-interactivity.md:268` and `synchronizing-with-effects.md:863`.
- Skill: `teaching.md:26` "once or twice per tutorial".

**C3. A short point-of-need gloss of prerequisite knowledge helps; "do not teach inline" is too strict.**
- `tutorial-tic-tac-toe.md:1137` (closures, in a note), `:1193` (a one-sentence explanation of the arrow syntax), `:1868` (how to read the spread syntax), all with an outside link and while the page claims "does not assume any existing React knowledge" about the framework only.
- Skill: `teaching.md:8` "Link to where each is learned. Do not teach them inline."

**C4. One running domain for an entire doc set is too coarse; one per chapter, evolving across consecutive pages, is what the docs do.**
- Scientist profiles: `your-first-component.md:66` onward through the chapter; sculpture gallery: `state-a-components-memory.md:62`; a chat room that evolves over five consecutive pages: `lifecycle-of-reactive-effects.md:36`, `separating-events-from-effects.md:37`.
- Skill: `SKILL.md:46` "Use one running domain across a doc set."

## 3. House convention (not carried over)

- Live, editable code sandboxes with hidden files, "Fork" and "Try changing ..." prompts (51 prompts across 28 pages): relies on the platform. The portable part is covered by M1/M8.
- A fixed vocabulary of page components (intro, learning-goals, recap, challenges, deep-dive, pitfall, note, link-out). The portable parts are in M5, M9, M10.
- Capitalizing framework concept names and Prettier-style code rules (`CONTRIBUTING.md:33-50`: JSX over `createElement`, `const`/`let`, named function declarations). Local style guide; the skill already says to follow one if it exists (`reference-and-guides.md:89`).
- The strict "never look ahead for a definition" ordering (`CONTRIBUTING.md:21`) comes from Learn being one linear course; the skill's weaker form (`SKILL.md:67`, `books-and-video.md:12`) is enough for most doc sets.
- Emoji markers (🔴, ✅, 🚩) as the in-block labels: the emoji are local, the labelling idea is M3.

## 4. Where react.dev falls short

**F1. Non-descriptive link text.** `setup.md:20` "Learn how to install it [here]"; `typescript.md:422` "the full list can be found [here]"; `you-might-not-need-an-effect.md:344` "[see here] for how to deal with that". Skill: `SKILL.md:45`.

**F2. Images without alt text.** `thinking-in-react.md:30` and `:52` (`<img src=... />`, no `alt`), while the page's diagrams elsewhere do have it. Skill: `SKILL.md:45`, `reference-and-guides.md:56`.

**F3. Names and wording drift between pages.** `escape-hatches.md:309` link text "Lifecycle of Reactive Events" points at a page titled "Lifecycle of Reactive Effects"; the same sentence reads "delivering the diner's order" in `adding-interactivity.md:242` and "the guest's order" in `render-and-commit.md:22`. Skill: `SKILL.md:38`, `:57`.

**F4. Version-specific syntax with no version stated.** Context used directly as a provider (`typescript.md:263`, `managing-state.md:744`), `ref` as a plain prop (`manipulating-the-dom-with-refs.md:366`), `useEffectEvent` imported from the main package (`separating-events-from-effects.md:461`). The only version statement in the Learn pages I searched is `react-compiler/installation.md:19`. Skill: `SKILL.md:39`.

**F5. Sample data inconsistency.** `choosing-the-state-structure.md:1066-1067` gives the entry keyed `39` the `id: 40`, and `:1071-1072` gives entry `40` the same id. Skill: `SKILL.md:64` (every sample checked against the claim).

**F6. Real-looking placeholder domains.** `preserving-and-resetting-state.md:1048` and `you-might-not-need-an-effect.md:1333` use `@mail.com` addresses (a live domain). Skill: `SKILL.md:52`. Low severity.

**F7. Figurative phrasing in explanatory prose.** `lifecycle-of-reactive-effects.md:159` "Disaster averted!"; `keeping-components-pure.md:120` "planes would fall out of the sky"; `escape-hatches.md:57` "a secret pocket". Skill: `SKILL.md:54`, `books-and-video.md:43`. This is a deliberate voice choice; I list it as a shortfall only for non-native readers, and I have no evidence of its cost beyond the skill's rationale.

## Confirmed by react.dev (backs up something unusual in the skill)

- "Walk it literally, as a fresh machine would" (`SKILL.md:66`) matches `CONTRIBUTING.md:27` ("try to forget everything you know ... follow the instructions you wrote, a single step at time").
- Normalizing errors by showing one (`teaching.md:31`): `tutorial-tic-tac-toe.md:363-365` shows the "Adjacent JSX elements" error; `rendering-lists.md:88-94` shows the missing-key warning.
- Name the tempting wrong mental model (`teaching.md:28`): `lifecycle-of-reactive-effects.md:75` "Intuitively, you might think that React would start synchronizing when your component mounts".
- Highlight the new lines and re-show the full file at checkpoints (`teaching.md:17`, `:29`): highlight markers in code fences (`CONTRIBUTING.md:104`) plus repeated full listings such as `tutorial-tic-tac-toe.md:1872`.

## Observed, not counted

Pages that combine explanation, procedure and definition:
- `tutorial-tic-tac-toe.md:1337` "Why immutability is important": an explanation section inside a tutorial, directly after the reader used `slice()` (`:1131`).
- `thinking-in-react.md:238`: a deep-dive defining two concepts inside a five-step procedure.
- `state-a-components-memory.md:161-162` (two-step recipe) next to `:525` (how the mechanism works inside) next to a recap list that acts as a reference summary.

Where the docs keep the kinds apart:
- Exhaustive facts are linked out: 76 links to `/reference/` across 27 Learn pages, e.g. `synchronizing-with-effects.md:400` "See the `useEffect` reference for details"; the contract is at `CONTRIBUTING.md:23`.
- `react-compiler/index.md` splits task pages (install, incremental adoption, debugging) from the option and directive reference (`:22-28`).
- Setup pages (`installation.md`, `creating-a-react-app.md`) are separate from the concept pages.

Skill rule: `SKILL.md:13` ("Mixing modes is the most common structural failure"), `:31` ("a tutorial that stops to explain design has become an explanation"), `:69`.

I do not count this as a correction. Each page serves one reader job (learn this idea), the explanation is attached to something the reader just did or is fenced as skippable (M10), and option lists and edge cases are linked out, so the rule survives if "mode" is judged by the reader's job rather than by the kind of sentence.

## Abstracted

Missed principles
1. When a lesson exists to prevent a specific mistake, let the reader reproduce the mistake first, then name the cause and the fix.
2. When you give an everyday word a narrow technical meaning, mark it visibly, say once that you are doing so, and use a different phrase for the broad idea.
3. Mark wrong or discouraged code inside the code block itself with a short comment prefix, because people copy blocks without reading the text around them.
4. Say plainly where an explanation is a simplification, and make sure every edge case you skipped lands on an exhaustive page that the simple page links to.
5. Tell readers which parts they may skim, and say that partial understanding on a first pass is expected; this is scope guidance, not apology.
6. Offer more than one route through the same material for different learning preferences, say at each entry point whom it suits, and end each overview with a jump for people who already know the content.
7. Before walking through a multi-step process, preview it as a short list whose items begin with verbs, then present the steps in that same order.
8. Teach a concrete method for tracing behaviour by hand (substitute values, list events in order, or tell one scenario from two vantage points) and reuse it across pages so readers can check claims themselves.
9. Include exercises built from nearly-working code with a planted defect, and give hints that say where such defects tend to hide.
10. Keep the main path linear by putting optional depth (internals, rationale, history) in clearly labelled blocks that can be skipped without losing the thread.
11. When a page leans on an idea defined elsewhere, link to the specific section that defines it, and give headings stable identifiers so renaming a heading does not break those links.

Corrections
1. In teaching material, show one rejected alternative when it is what readers will naturally try first; state why it falls short, then move on. Leave out alternatives readers would not think of.
2. Do not cap prediction prompts at a fixed number; use them as often as the topic is counterintuitive, and expect several on a page about surprising behaviour.
3. When a lesson needs background knowledge, give a one- or two-sentence explanation at the point of first use, with an outside link, rather than only a prerequisite list; do not teach the background at length.
4. Use one running example domain per chapter or section, and evolve that same example across consecutive pages; change the domain when the subject changes, rather than holding a single domain across the whole set.
