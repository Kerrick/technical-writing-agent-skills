# Books, courses, and workshops

Long-form material is a sequence of tutorials and explanations with a reference appendix, designed backward from what the reader can do at the end.

## Plan backward

1. **List end capabilities.** What the reader can do after the last page, as observable actions. Five to fifteen for a book.
2. **Decide the evidence.** For each capability, the exercise or project that would show the reader has it.
3. **Map dependencies.** Sketch which concepts each capability needs and which concepts need which. The order of chapters falls out of this graph; a concept used before it's introduced shows up as a backward edge.
4. **Assign one major capability per chapter** (or module, or workshop session). Introduce supporting concepts where they're first needed, not in an up-front theory chapter.
5. **Outline to the heading level**, with one-line outcomes, and agree it with the user before drafting.
6. **Draft one sample chapter from the middle** before the rest. It tests the voice, depth, and running example under realistic load; chapter 1 is atypical.

## Running project

- Carry one realistic project through the book. Each chapter adds to it and leaves it working.
- Keep the code in a repository with a tag or directory per chapter, and run the code in CI so every listing in the book is known to work. Pull listings from the tested code rather than pasting them.
- Pick a domain the audience understands without explanation, so attention goes to the technique.

## Chapter template

```markdown
# <Chapter title: the capability or the problem it solves>

<Opening: a concrete problem in the running project that this chapter solves.>

<Objectives: "By the end of this chapter, you'll be able to ...">

## <Section>
<Show a working example → explain what it does and why → reader practices>

...

## Summary
<Capabilities gained, in a few lines. Name the concepts so readers can look them up.>

## Exercises
1. <Recall or predict: "What does this print, and why?">
2. <Apply: the same technique on a new case>
3. <Extend: a harder variation with less guidance>

## Further reading
```

## Exercises

Practice that makes readers retrieve and use what they learned does more for retention than re-reading. Good exercise types, roughly from easiest:

- **Predict**: show code, ask what it outputs before running it.
- **Parsons problem**: give the correct lines of a solution, shuffled; the reader orders them. Good for novices: it practices structure without the blank-page problem.
- **Find the bug**: a short listing with one realistic mistake.
- **Modify**: change working code to do something slightly different.
- **Make**: write something new from a goal statement.

Revisit earlier concepts in later chapters' exercises, mixed in with new ones, so practice is spaced and interleaved rather than all blocked at the chapter where the concept appeared. Put solutions in an appendix or the repository, not right after the question.

## Pacing

- Alternate showing, explaining, and doing. A long stretch of any one loses readers.
- Spiral: introduce a concept simply, use it, and return to it later with more depth, rather than covering it exhaustively the first time.
- Watch the density of new terms per page. When a section introduces several, split it or move some earlier.

## Front matter

- **Who this is for, and who it isn't for.** Readers self-select better than you can guess.
- **What you need to know first**, as skills.
- **How to read it**: in order, or which chapters can be skipped.
- **Conventions**: what monospace, bold, callouts, and placeholders mean; how to get the code.
- **Versions** covered.

## Aging well

Isolate version-specific details (install steps, UI walkthroughs, screenshots) in a few places so updates touch little. Avoid dated cultural references and "new" or "recently."

## Review

Use two kinds of technical reviewer: someone from the target audience who reads in order and notes where they got stuck, and an expert who checks correctness. The first finds more of the problems that matter.

## Workshops and live courses

- Send setup instructions in advance and test them on every listed platform. Have a fallback such as a hosted environment, because setup failures eat the first hour.
- Keep each stretch of instruction short, around 10–15 minutes, before learners do something.
- Use visible checkpoints (a sticky note, a reaction, a chat message) so you know who is stuck without asking "any questions?"
- Live-code rather than showing slides of code: learners see the pace, the mistakes, and the recovery. Type slowly, narrate, and use a large font.
