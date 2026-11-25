# AI-provenance disclosure

Put it in the README's last section, after License, under a heading such as "How this was made". Say the facts a reader needs to weigh the code: who wrote what, and who reviewed it, or what checks the project uses in place of review.

Use the maintainer's existing wording and any existing disclosure in their other projects. Never assume they've written, reviewed, or read anything they haven't said they have. Ask in chat only if you have no evidence at all, once, with your proposed answer. Otherwise, use the category with the smallest claim: work an agent made, with no record of review, is requested. Write the disclosure as final, and say in your report which categories you inferred.

## In Kerrick Long's projects

Or wherever the maintainer has no house pattern and approves it. The section is two paragraphs.

The first is this exact text, as an ordinary paragraph in the maintainer's voice, not a blockquote:

```markdown
I use three words for how code and prose comes to exist. Code or prose I wrote, I typed by hand, with nothing generated. Code or prose I wrought, an AI agent generated while I iterated with it, and I reviewed every change before committing it, so I take responsibility for every diff. Code or prose I requested, an agent built with little or no review from me, in the style of a "dark factory."
```

The second says, in a few sentences:

1. Which parts are wrote, wrought, or requested. Name parts, not files: "its code, tests, and documentation, this README included". Give one blanket label only when it's true.
2. What the project uses in place of review, for anything requested: the tests, checks, and gates the project requires.
3. The project's [declare-ai](https://declare-ai.org/1.0.0/assess.html) level, as a link whose text is `declare-ai.org`, pointing at that level's page, at the end of the paragraph.

For example, from a project an agent built in full:

```markdown
All of `machines` (its code, tests, cluster configuration, skills and documentation, this README included) was requested. Agents built it from my goals and decisions, with little review of the diffs. In place of review, the project's rules require every line of Ruby to be covered by tests meant to stand up to mutation testing, tests that never touch the network, a check of each change before its push, and the full test and lint run on the build machines before each release. I use `machines` for my agents' work in my projects. [declare-ai.org](https://declare-ai.org/1.0.0/total.html).
```

## The declare-ai level

Work it out with the [assessment](https://declare-ai.org/1.0.0/assess.html), then link the level's page:

| Level | When | Link |
| - | - | - |
| None | No generative AI was used | `https://declare-ai.org/1.0.0/none.html` |
| Non-creative | AI did only mechanical work, such as fixing typos | `https://declare-ai.org/1.0.0/non-creative.html` |
| Creative | AI contributed creatively, and a person contributed to the work too | `https://declare-ai.org/1.0.0/creative.html` |
| Total | AI produced the entire work | `https://declare-ai.org/1.0.0/total.html` |

A person's goals and decisions alone don't count as a creative contribution. A project is total if an agent produced every part.

## Rules

- Don't apologize. Don't boast.
- Don't argue for the maintainer's contribution. State the categories and the checks, and stop.
- Keep it to those two paragraphs. Link to a longer policy if there is one.
