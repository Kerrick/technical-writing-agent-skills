# 7. Check "often broken"

A new fork of the baseline point. It may read the findings files and the source checkouts, so it is not a clean-room context. It decides whether each "baseline, often broken" entry in `merged.md` is a lapse (keep the rule), a deliberate practice (the baseline may be wrong), or neither.

It exists because the reading forks judged group 4, "where the source falls short", themselves. They're forks of the baseline's author, so they tend to side with the baseline. This step makes the call on evidence instead.

```
Don't change technical-writing. It's the baseline: a record of what you believed before reading anything. Its value depends on it staying exactly as you wrote it.

Read ${WORK}/merged.md. In its "Kept" section, every entry whose Kind includes "baseline, often broken" names skill rules that some sources break. Sources are labeled by letter: A react-learn.md, B ember-guides.md, C django-docs.md, D rails-guides-1.md and rails-guides-2.md (one source), E rust-book.md, F mdn-js-guide.md, G postgres-manual.md, all in the same folder. Those files hold the evidence. Each names the source checkout and style guide it compared, and you may open them to check.

For each such entry and each source listed as breaking it, classify the breakage exactly one way:

1. Lapse: what the source does is objectively wrong (code that can't run, a factual error, stale or contradictory text), or the source's own style guide states the same rule the source breaks. Cite the style-guide line, or the error.
2. Deliberate: the source does it by design, and what it does contradicts the skill's rule: it's in the source's templates or style guide, or it appears in the same form on at least 80% of pages of that kind, counted. A template or pattern whose content mostly follows the rule doesn't count. Cite two or more places, and give the count.
3. Unexamined: it appears on some pages and not others, and the source's style guide says nothing either way.

Then classify each entry from its sources' results:
- Two or more lapses: keep as "baseline, often broken".
- Two or more deliberate: it becomes a correction candidate. State, in general terms, what those sources do by design.
- Otherwise: if the entry is also a correction in its own right, keep it as a correction only; if not, mark it "redundant with the skill" and cite the skill line.

Write ${WORK}/often-broken-check.md: a table of entry, source, class and evidence, then for each entry its result. Then end with a section "## For the writer": the results stated in general terms, with no quotes, no source names or technology, and no examples taken from the sources, so it can be given to a writer who has never seen the evidence.
```

## Changes since the first run

The first run's checker used an earlier class 2, without the 80% count or the requirement to contradict the rule. It agreed with a by-hand check on only 9 of 13 entries; all four disagreements were about deliberate versus unexamined, and the checker got them right by doing those two things unasked. Class 2 now requires both.

Check: `uv run method/scripts/extract_section.py "## For the writer" often-broken-check.md > for-the-writer.md`, then `uv run method/scripts/leak_check.py for-the-writer.md` passes.
