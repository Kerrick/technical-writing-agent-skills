import json, sys, os, re
from pathlib import Path
P = Path.home()/".claude/projects/-private-tmp-claude-501--Users-kerrick--agents-skills-agent-skills-38943b25-895c-4890-ba81-721fe8c8b685-scratchpad-sonnet-run-work"
sid, listfile = sys.argv[1], sys.argv[2]
expected = [re.sub(r"^\s*(\d+\.\s*)?", "", l).strip() for l in Path(listfile).read_text().splitlines() if l.strip()]
# map tool_use id -> path; then tool_result -> max line number seen
uses = {}; maxline = {}
for line in (P/f"{sid}.jsonl").read_text().splitlines():
    o = json.loads(line)
    c = o.get("message", {}).get("content")
    if not isinstance(c, list): continue
    for b in c:
        if b.get("type") == "tool_use" and b["name"] == "Read":
            uses[b["id"]] = b["input"]["file_path"]
        if b.get("type") == "tool_result" and b.get("tool_use_id") in uses:
            cc = b.get("content"); s = cc if isinstance(cc, str) else "\n".join(x.get("text","") for x in cc if isinstance(x, dict))
            nums = [int(m) for m in re.findall(r"^\s*(\d+)\t", s, re.M)]
            p = uses[b["tool_use_id"]]
            maxline[p] = max(maxline.get(p, 0), max(nums) if nums else 0)
missing = [p for p in expected if p not in maxline]
partial = []
for p in expected:
    if p in maxline and os.path.exists(p):
        n = sum(1 for _ in open(p, errors="ignore"))
        if maxline[p] < n - 1: partial.append((p.split("/sources/")[-1], n, maxline[p]))
print(f"{len(expected)} expected, {len(maxline)} distinct read, missing={len(missing)}, partial={len(partial)}")
for m in missing: print("  MISSING", m)
for p in partial: print("  PARTIAL", p)
