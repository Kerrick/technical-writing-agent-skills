# Tutorials, how-tos, books and documentation sets

Read this before writing or editing a tutorial, how-to, course, video script, book or whole documentation set. Rules in SKILL.md apply as well.

## Checklist for these pages

- [ ] Walked the page literally from its stated prerequisites in a clean state. Everything it promises or relies on is present: every promised list or step; every function or method it uses is defined; every file or dataset the lesson needs can be created from the text or is supplied; summaries, prose and file names match the code.
- [ ] One command-block convention, stated and applied across the set (below).

## Command blocks

Pick one convention for command examples, state it, and apply it across the whole set. Whatever a reader copies must run.

- Safe default: a command-only block with no prompt character, and the output in a separate block.
- A prompt character inside the block, or real captured output directly beneath the command in the same block, is acceptable as a deliberate house convention. It is acceptable only when the rendered page excludes the prompt and the output from what the reader copies (non-selectable prompt and output styling, or a copy button that copies the command only), and you have checked that on the rendered page.
- Where you can't confirm what gets copied, use the safe default.

## A learner's path has no choices, but may mention what else exists

The path the learner follows contains no choices. You may say what else exists: show the alternative forms the reader will meet in other people's code or is likely to try, and say why a rejected one falls short. Label each alternative with which to prefer and why, and put it in a bounded aside after the main step so it doesn't derail the path. Keep this to the few the reader will actually meet.

## Give readers a guide to the material (books, documentation sets, tutorial series)

Tell readers how to use a long work or a documentation set:

- Say who it is for and who it is not for, and where those readers should go instead.
- Offer routes through it, including skipping ahead and coming back. Say which parts they may skim or skip, and that partial understanding on a first pass is expected.
- Say in a sentence per kind of page what need it serves.
- Add a feature-by-feature index that lists the guide, task and lookup pages side by side.
- End each overview with a jump for people who already know the content.

## Gotchas

- A page that refers to a list that isn't there, or to data the reader can't create, fails the literal walk-through. Do the walk.
- Do not strip prompts from a set whose standard form puts them in the block, and do not leave output in a block readers copy whole.
- Do not leave out alternatives. A reader who tries the obvious wrong thing, or meets a variant, gets no explanation.
- A long work with no map leaves readers unable to tell whether to read, skim or skip it.
