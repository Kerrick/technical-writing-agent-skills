# 5. Audit

A new fork of the baseline point. It reads every findings file in full, evidence and quotes included, and writes `abstracted-full.md`, the only thing later clean-room steps see. It must be a different context from the merger and the writer.

```
Don't change the skill you wrote. It's the baseline: a record of what you believed before reading anything. Its value depends on it staying exactly as you wrote it.

Read all eight files in ${WORK}/ that compare a documentation source against your skill, in full: react-learn.md, ember-guides.md, django-docs.md, rails-guides-1.md, rails-guides-2.md, rust-book.md, mdn-js-guide.md, postgres-manual.md. Ignore any other file there. Don't open the documentation sources themselves.

Write ${WORK}/abstracted-full.md for a writer who will never see these files or the sources. Label the sources by letter, not name: A react-learn, B ember-guides, C django-docs, D both rails-guides files (one source), E rust-book, F mdn-js-guide, G postgres-manual. For each source, write four sections:

1. "Rules": that file's Abstracted rules, checked against its own evidence above them. Where a rule overstates the evidence, drops a condition the evidence shows, or doesn't follow from it, rewrite it to match and mark it [revised]. Where no evidence supports it, delete it and mark the gap [removed]. Otherwise copy it unchanged.
2. "Baseline rules broken": each item in that file's "falls short" group whose point is that the source breaks a rule your skill states, as one line: the skill line (file:line) and the rule in general terms. Leave out plain factual errors in the source that no skill rule covers.
3. "Confirmed": each confirmation, as the skill line (file:line) it confirms.
4. "On mixing modes": the file's "Observed, not counted" position in one or two general sentences: what pattern it saw, and whether it counts as a correction to the skill's rule about keeping each page to one kind of documentation, and why. Write "not addressed" if the file has none.

Same constraints as the Abstracted sections: no quotes, no names of the source or its technology, no examples taken from the source. Nothing that would let a reader identify which documentation it came from.

End with a "## Audit" section: how many rules you revised and removed, per source, with one line each on why.
```

Check: `uv run method/scripts/leak_check.py abstracted-full.md` passes, and a sample of the [revised] reasons in "## Audit" hold up against the findings files.
