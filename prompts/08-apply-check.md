# 8. Apply the check

Sent to the merge fork from [6. Merge](06-merge.md), after `for-the-writer.md` has been extracted. The merge fork stays clean-room: it reads only the extracted section, never `often-broken-check.md`.

```
A reviewer who can see the evidence checked each "baseline, often broken" entry in merged.md against a stricter test. Read its results in ~/Developer/technical-writing-deltas/for-the-writer.md, and nothing else new in that folder. Apply them to merged.md: move each entry to the Kind, or to "Dropped", exactly as the results state. For each rule the results call open to correction, apply rule 3: write the most specific rule that neither your skill's intent nor the stated practice contradicts, and note how the conflict was resolved. Update "Counts" to match. Don't write the new skill yet.
```

Then build the writer's input:

```
python3 scripts/build_kept.py pipeline/merged.md -o pipeline/kept.md
python3 scripts/leak_check.py pipeline/kept.md
```
