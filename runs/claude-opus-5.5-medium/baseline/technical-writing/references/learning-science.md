# Learning science, applied

Read this when designing anything a reader is meant to *learn* from rather than look up: multi-page tutorials, books, courses, video series. Each principle is followed by what to do about it.

## Working memory is small

Learners can hold only a few new things in mind at once. Load comes from three places:

- **Intrinsic**: the material's own complexity. Reduce it by sequencing: teach prerequisites first, and introduce parts before the whole (pre-training on names and roles of components before showing them interact).
- **Extraneous**: load from presentation. Cut it ruthlessly: decoration, split attention (code on one page, its explanation on another), the same words on screen and in narration, irrelevant asides.
- **Germane**: effort spent building the mental model. That's the effort to protect.

What to do: one new concept per step; define terms before they're needed; keep code and its explanation adjacent.

## Worked examples beat problem-solving, until they don't

Novices learn faster from studying worked examples than from solving equivalent problems. As expertise grows, the effect reverses: worked detail becomes redundant and slows experts down (the expertise reversal effect).

What to do: start with worked examples, fade them into completion problems, then independent ones (see [tutorials](tutorials.md#worked-examples-and-fading)). Write separate pages for novices and experts rather than one page for both.

## Concrete before abstract

Learners grasp a general rule more easily after a specific case. But a rule learned only from one concrete case may not transfer.

What to do: show a specific example, then name the general pattern, then show a second, different example of the same pattern.

## Retrieval, spacing, interleaving

Recalling information strengthens memory more than re-reading it. Practice spread over time beats the same practice massed together. Mixing problem types makes learners choose the technique, which they must do in real work.

What to do: end chapters and episodes with questions that require recall or prediction. Revisit earlier concepts in later exercises. Mix problem types in review sets. These feel harder to learners than re-reading; that difficulty is the point.

## Words and pictures together

People learn better from words with relevant pictures than from words alone, provided the picture shows the mechanism and isn't decoration. The main principles from multimedia learning research (Mayer):

| Principle | Do |
| - | - |
| Coherence | Cut interesting but irrelevant material. |
| Signaling | Highlight the structure and the thing being discussed. |
| Redundancy | Don't add on-screen text that repeats the narration. |
| Spatial contiguity | Put labels and explanations next to what they describe. |
| Temporal contiguity | Narrate an action while it happens, not before or after. |
| Segmenting | Break lessons into learner-paced chunks. |
| Pre-training | Teach component names and roles before the process. |
| Modality | For animations and screencasts, explain in narration, not on-screen text. |
| Personalization | Write conversationally, in second person. |

## Mental models and misconceptions

Novices don't lack facts so much as a working model of how the thing behaves (for code, the notional machine: what the computer does when each line runs). Experts have models so automatic they forget them, which is why they skip steps.

What to do: make the model explicit, with a diagram or a trace of state step by step. Find the common misconceptions for the topic (from support questions, forum posts, and issues) and refute them directly, as in [explanation](explanation.md).

## Objectives you can check

An objective is useful when you can tell whether a learner met it. "Understand closures" can't be checked; "predict the output of code that captures a loop variable in a closure" can.

What to do: write objectives with observable verbs (predict, write, debug, choose, compare). Test at the level you taught: if the objective is "debug," the exercises must involve debugging, not recall.

## Motivation

Learners persist when they see why the material matters to them and feel capable of it.

What to do: open with the problem the reader has, not the feature you have. Give an early, real success. Make difficulty climb steadily, without cliffs.
