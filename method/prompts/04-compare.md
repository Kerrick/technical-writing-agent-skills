# 4. Compare

The second message to each reading fork, once it has read every page. It writes one findings file per source (two for a source split across forks).

Don't fill it in by hand: `uv run method/scripts/prompt.py compare --source <key> --src ${SRC} --work ${WORK}` prints it filled in, with the per-source values from [sources.toml](../sources.toml). `${does}`, `${shows}`, `${falls}` and `${confirms}` become the right verb for a singular or plural source name. An empty `${FOCUS}` is dropped. A source's `prefix` goes before the first paragraph, and its `first_paragraph_extra` is added to the end of the first paragraph.

```
Don't change the skill you wrote. It's the baseline: a record of what you believed before reading. Its value depends on it staying exactly as you wrote it.

${STYLE_GUIDE}

Then compare everything you read against the skill and write down every difference, sorted into exactly one of these groups:

1. Missed principle: something ${SOURCE} ${does} deliberately and well, which would carry over to other docs, and which the skill doesn't say or implies the opposite of.
2. Correction: something the skill states that ${SOURCE} ${shows} to be wrong, oversimplified, or too absolute.
3. House convention: something specific to ${HOUSE}, that wouldn't carry over. Keep this group short; it's here so convention doesn't get passed off as principle.
4. Where ${SOURCE} ${falls} short: places where the skill's advice is better than what the docs do.

${FOCUS}

Every difference needs evidence: the file and a short quote, or a description of the pattern with two or more places it appears, plus the skill line it differs from (file:line), or "absent". If you can't point to evidence, drop the difference. Don't invent differences to fill the groups. An empty group is a valid result.

Also note anything the skill says that ${SOURCE} clearly ${confirms}, but only one line each, and only where it actually backs up something unusual in the skill.

If any page combines explanation, how-to and reference, describe how in a section "## Observed, not counted" just before "## Abstracted", with evidence and the line of the skill's rule about keeping each page to one kind of documentation it differs from, if the skill has such a rule (file:line). Include where the docs instead keep those apart. If you'd count it as a correction, say so in one sentence; if not, say why. If they don't, write that instead.

${LICENSE}

Finish the file with a section called "## Abstracted". List each missed principle and correction as one general rule, in your own words, with no quote, no mention of ${NAMES}, and no example taken from the source. A writer who has never seen ${SOURCE} must be able to act on it. Keep the evidence above this section; I'll use it to check your claims, and only the Abstracted section goes on to the next step.

To find evidence, search the files (grep) instead of re-reading whole pages.

Write the result to ${OUTPUT}, creating the folder if needed, with "Source: ${SOURCE_LINE}" at the top. Don't write a new skill.
```

`${STYLE_GUIDE}` is either "First read {files}. They state the intent behind the pages you just read." or, when the fork has already read them as part of the pages, "You've already read {files}. Don't re-read them; treat them as the stated intent behind the pages you read."

`${LICENSE}` is "The content is {license}. Quote briefly, and only when the exact wording matters. Otherwise describe the pattern in your own words." For a share-alike license, say so and use "Quote rarely and briefly".

If the fork's summary offers to edit the skill, open with "No, don't fold anything into the skill." and add after the first paragraph: "The summary you just gave is a starting point; every item still needs the evidence described below before it goes in the file."

## Checking a findings file

Before ending each fork, check its file. The fork can still fix a weak claim; once it's ended, nothing can.

- `uv run method/scripts/extract_section.py "## Abstracted" <file> | uv run method/scripts/leak_check.py /dev/stdin` passes. (Run with `--names` for the source's own terms.)
- Two or more evidence claims, checked against the source checkout: at least one principle and one shortfall.
- It has an "Observed, not counted" section, or says why not.
