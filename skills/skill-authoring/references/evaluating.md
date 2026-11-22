# Evaluating a skill

Read this when writing output evals, running them, or deciding whether one version of a skill beats another. Adapted from the Agent Skills guide to evaluating skills, with rules for keeping runs isolated and comparable; [NOTICE.md](../NOTICE.md) gives the credit and the changes.

An eval answers one question: does the agent do the task better with this skill than without it, or than with the previous version? Without a comparison, a pass rate means nothing.

## Where evals live

Keep a skill's evals outside its folder, in a sibling such as `evals/<skill-name>/`:

```
evals/<skill-name>/
├── evals.json          # output evals
├── eval_queries.json   # trigger queries (see descriptions.md)
└── files/              # input files the prompts name
```

Inside the skill folder, an agent under evaluation can open the assertions, and every install ships them. If the repository already keeps evals inside each skill, follow it, and keep the agent under test away from them.

Keep the evals fixed once results exist. Changing a prompt, an input file, or an assertion makes earlier results incomparable. Add a new eval rather than editing an old one, and change the set in its own commit.

## Test cases

```json
{
  "skill_name": "csv-analyzer",
  "evals": [
    {
      "id": 1,
      "prompt": "I have monthly sales in evals/csv-analyzer/files/sales_2025.csv. Can you find the top 3 months by revenue and make a bar chart?",
      "expected_output": "A bar chart of the top 3 months by revenue, with labeled axes and values.",
      "files": ["evals/csv-analyzer/files/sales_2025.csv"],
      "assertions": [
        "[Label every axis] Both axes of the chart are labeled",
        "[Rank by the column the user named] The chart shows exactly the 3 months with the highest revenue"
      ]
    }
  ]
}
```

- **Start with three or four.** Expand after you've seen results.
- **Realistic prompts:** file paths, names, personal context, varied formality ("hey can you clean up this csv" beside a precise spec).
- **At least one edge case:** malformed input, an unusual request, or a case where the skill is ambiguous.
- **Build inputs that exercise the rules.** A fixture with a planted flaw (a wrong flag in a README, a name that doesn't match its folder) shows whether the agent catches it.
- **No placeholders** in prompts, fixtures, or assertions. They're final files too.

## Assertions

Each assertion names, in brackets, the rule it tests, then states one observable fact about the output. Name the rule so you can aggregate results by rule, and find rules that never make a difference.

- Good: "The output file is valid JSON", "Both axes are labeled", "At least 3 recommendations". Checkable and specific.
- Weak: "The output is good" (vague), "Uses exactly the phrase 'Total Revenue: $X'" (brittle).
- A rule's "Without it" usually gives the assertion: test for the absence of that mistake.
- Leave taste (style, whether it "feels right") to human review.

Draft assertions from the rules, then revise them after the first run shows what outputs look like.

## Isolating each run

Every run must measure one skill, or none, and nothing else.

- **A fresh session per run,** with no history from writing the skill or from other runs. Sub-agents work if each starts fresh.
- **Give the skill by path in the prompt** ("Read and follow the skill at `<path>/SKILL.md`"), and disable the agent's skill tool, so no installed skill can join the run. In Claude Code: `--disallowedTools Skill`.
- **Three setups per eval:** the new skill; the baseline, or the previous version; and no skill, with the same prompt minus the path. Before editing a skill, snapshot it outside its folder, and point the previous-version setup at the snapshot.
- **Its own copy of every input file,** since agents edit files.
- **Record tokens and duration** when each run finishes. Harnesses often report them only once: in Claude Code, a sub-agent's completion notification carries `total_tokens` and `duration_ms`, and a headless JSON result carries `usage`.

## Workspace

Put results outside the skill folder, one directory per pass:

```
<workspace>/iteration-1/
├── eval-top-months-chart/
│   ├── with_skill/      outputs/  timing.json  grading.json
│   ├── old_skill/       outputs/  timing.json  grading.json
│   └── without_skill/   outputs/  timing.json  grading.json
└── benchmark.json
```

`timing.json` holds `{"total_tokens": 84852, "duration_ms": 23332}`.

## Grading

- **One fresh grader per eval,** shown every setup's output labeled X, Y, Z, without knowing which is which, plus the assertions. For each assertion it records PASS or FAIL with quoted evidence, in each output's `grading.json`, and then compares the outputs blind on holistic quality.
- **No benefit of the doubt.** A section titled "Summary" holding one vague sentence fails "includes a summary".
- **Scripts for mechanical checks** (valid JSON, row counts, a file exists, a command exits 0). They're more reliable than a model and reusable.
- **Grade the assertions too:** note any that always pass, always fail, or can't be checked from the output, and fix them next iteration.

```json
{
  "assertion_results": [
    { "text": "Both axes are labeled", "passed": false, "evidence": "Y-axis reads 'Revenue ($)'; X-axis has no label" }
  ],
  "summary": { "passed": 3, "failed": 1, "total": 4, "pass_rate": 0.75 }
}
```

## Aggregating

Write `benchmark.json` per iteration: for each setup, the mean and standard deviation of pass rate, seconds, and tokens, plus the delta between setups. Break pass rates down by rule, and by each rule's kind (new, correction, known but skipped), to see which kind of rule the skill earns its keep on. A skill that adds 13 seconds for 50 points of pass rate is worth it; one that doubles tokens for 2 points may not be.

Run each setup three times before trusting a difference. Standard deviation means nothing with one run.

## Reading the results

- **Passes in every setup:** the model already does it. Drop the assertion, and consider dropping the rule.
- **Fails in every setup:** the assertion or the eval is broken, or the task is too hard. Fix it first.
- **Passes only with the skill:** the skill's value. Find which instruction made the difference.
- **Inconsistent across runs:** the eval is flaky, or the instruction is ambiguous. Tighten it with an example or a sharper rule.
- **A time or token outlier:** read that run's transcript for the wasted steps.

Then review outputs yourself, or with the user, and record specific feedback per eval in `feedback.json` ("the months are in alphabetical order", not "looks bad"; empty means fine).

## Iterating

Give the failed assertions, the feedback, the transcripts, and the current `SKILL.md` to a model, and ask for changes that:

- generalize, rather than patch the one test case;
- keep the skill lean: remove instructions that cause wasted work, and try removing rules when pass rates plateau;
- explain the why behind each rule;
- bundle any helper every run rewrote.

Apply them, rerun every eval into `iteration-<N+1>/`, grade, review, repeat. Stop when feedback is empty or iterations stop improving. A new version replaces the current one only if it beats it, on the current one's target model.

## Real tasks

Real work counts as an eval. For each, keep the target repository's commit, the request word for word, the session ID, tokens and time, whether the skill loaded without being named, every correction given, and any hand fixes in a separate commit. Then the task can be rerun later with a newer version, the baseline, or no skill.

## Headless runs in Claude Code

With Claude Code's command line (v2.1.311):

- **Start** a session with a known ID: `claude -p --model <model> --effort <level> --session-id <uuid> --output-format json "<prompt>" < /dev/null`.
- **Continue** it: `claude -p --resume <uuid> … "<next prompt>"`.
- **Fork** it: `claude -p --resume <uuid> --fork-session … "<prompt>"`. The fork gets everything the session had and its own ID, and leaves the original unchanged.
- **Measure context** from the session's transcript, not the JSON result: add `input_tokens`, `cache_read_input_tokens`, and `cache_creation_input_tokens` in the last assistant message's `usage` in `~/.claude/projects/<cwd>/<session>.jsonl`. The result's `usage` is summed over the session's calls.
- **Limit** a session with `--allowedTools`, keep it to the run's folders with `--add-dir`, and start it from the run's working folder.
- **For every eval run,** add `--disallowedTools Skill` and give the skill by path in the prompt.
