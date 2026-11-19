# 6. Merge

A new fork of the baseline point, which must never open the findings files. It needs the baseline in context, because rule 4 asks whether the baseline already states a rule. Once `merged.md` has been updated by [8. Apply the check](08-apply-check.md), it can be ended: the writer is a different, fresh session.

```
Don't change the skill you wrote. It's the baseline: a record of what you believed before reading anything. Its value depends on it staying exactly as you wrote it.

Read ${WORK}/abstracted-full.md in full, and read nothing else in that folder. It holds what seven famous documentation sources, labeled A–G, showed about your skill, checked against evidence you won't see. For each source it has four sections: "Rules" (things your skill missed, or corrections to things it states), "Baseline rules broken" (rules your skill states that the source itself breaks), "Confirmed" (skill lines the source backs up), and "On mixing modes" (the source's position on the skill's rule about keeping each page to one kind of documentation). You haven't seen the sources, and you don't need to.

Merge the Rules into clusters, applying these fixed rules exactly:

1. Cluster: group rules that state the same idea, even in different words. A rule belongs to one cluster. Where a source cross-references two of its own rules, they still count as one source.
2. Inclusion: keep a cluster only if two or more different sources back it. Count sources by letter. Drop every single-source cluster, however important it seems.
3. Conflicts: where rules in a cluster disagree, write the most specific rule that none of them contradicts. For the skill's rule about keeping each page to one kind of documentation, also weigh every source's "On mixing modes" section, as each is a position on the same question. If no such rule exists, drop the cluster and say why.
4. Delta only: drop a cluster if your skill already states it. Cite the skill line (file:line). A correction is never redundant, since it changes something your skill states.
5. Standalone: write each kept cluster's rule so that a reader who has never seen your skill can act on it. For a correction, state the right rule itself, not "unlike the usual advice…".
6. Keep despite known: a skill rule listed under "Baseline rules broken" by two or more sources goes in "Kept" too, restated standalone, marked "baseline, often broken", with its sources. This overrides rule 4. If a correction in "Kept" changes that same skill rule, state the corrected version once.

"Confirmed" doesn't add rules. Use it only to report, under "Counts", which skill lines two or more sources confirmed.

Write ${WORK}/merged.md with three sections:

- "## Kept": for each cluster, the standalone rule; whether it's a missed principle, a correction, or "baseline, often broken"; for a correction or baseline rule, the skill line (file:line); its sources (letters) and count; where it applies (every page, or which kind: tutorial, how-to, reference, explanation, book, video); in one sentence, what an agent writing without this rule would do wrong; and, where rule 3 applied, one sentence on how the conflict was resolved.
- "## Dropped": each dropped cluster in one line, with its sources and the reason: single source, redundant with the skill (file:line), or unresolvable conflict.
- "## Counts": rules read, clusters formed, kept (for each of the three kinds), dropped for each reason, and the skill lines two or more sources confirmed.

Order "Kept" by source count, most first. Every rule in every "Rules" section must land in exactly one cluster; check that before finishing. Don't write the new skill yet.
```

The "where it applies" and "what an agent would do wrong" fields were added to the prompt just before it was sent; they're what let the writer place each rule and turn it into a gotcha.

Check: every rule landed in exactly one cluster; each kept cluster has two or more sources; every skill citation is a real line.
