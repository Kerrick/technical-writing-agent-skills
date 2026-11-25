# Descriptions and triggering

Read this when writing trigger queries, or when a skill loads when it shouldn't or doesn't load when it should. Adapted from the Agent Skills guide to optimizing descriptions; [NOTICE.md](../NOTICE.md) has the credit and the changes.

## How triggering works

At startup the agent sees only each skill's `name` and `description`, and loads a skill's body when a task matches. Agents usually consult a skill only for work they can't easily do alone: for a one-step request ("read this PDF"), an agent may not load a matching skill at all. Descriptions matter most for specialized work.

## Writing one

- **Imperative:** "Use when…", not "This skill does…".
- **The user's intent, not the mechanism.** The agent matches against what the user asked for.
- **Pushy about scope.** List the contexts where it applies, including requests that never name the domain: "even if they don't say 'CSV'".
- **A boundary with each sibling.** Say what it's not for and which skill to use instead, and make the sibling say the same back. Without that, agents can't tell the two skills apart for the same requests.
- **Concise:** a few sentences to a short paragraph, under the 1024-character limit.

## Trigger queries

Write about 16–20 realistic queries, half that should load the skill and half that shouldn't, as a JSON array:

```json
[
  { "query": "I've got a spreadsheet in ~/data/q4_results.xlsx with revenue in col C, can you add a margin column and flag anything under 10%?", "should_trigger": true },
  { "query": "whats the quickest way to convert this json file to yaml", "should_trigger": false }
]
```

Make them realistic: file paths, personal context ("my manager asked…"), real names and values, casual wording, abbreviations, the odd typo.

**Should load the skill:** vary the phrasing (formal, casual), the explicitness (naming the domain, or only describing the need), the detail (terse, or full of backstory), and the complexity (one step, or the skill's task buried in a longer chain). The most useful are the ones where the connection isn't obvious from the words.

**Shouldn't load it:** near-misses, which share keywords or concepts but need something else. "Write a fibonacci function" is no test at all. Include requests meant for each sibling skill, and requests in the skill's vocabulary for a neighboring task.

## Running them

Trigger tests need the opposite setup from output evals: the skill installed and discoverable, with the agent's skill tool enabled, and the sibling skills installed too, so each near-miss shows whether the agent picks the right skill. Run every query in a separate fresh session.

A query loaded the skill if the agent read the skill's `SKILL.md`. In Claude Code, run `claude -p "<query>" --output-format stream-json --verbose` and look for a `tool_use` block named `Skill` whose `input.skill` is the skill's name. Stop a run early once the outcome is clear.

Run each query three times and compute its trigger rate. A should-trigger query passes above 0.5; a shouldn't-trigger query passes below it. Script the loop: 20 queries at three runs each is 60 sessions.

In Claude Code, `--tools` and `--allowedTools` are each followed by several values, so pass the query on stdin, or right after `-p`; placed after them, it's read as one of their values and the session starts with no prompt.

A query sent as a session's first message shows whether the agent loads the skill at the start of work. An agent that skips a skill usually does it mid-task: it finishes the work it was asked for, then commits, pushes, or releases without loading the skill that covers that step. For a skill about such a step, add queries that arrive as the second or third message of a session already busy with other work, and count those separately.

## Tuning

1. **Split** the queries once, at random: about 60% train, 40% validation, each with a proportional mix of positives and negatives. Keep the split fixed across iterations.
2. **Evaluate** the current description on both sets.
3. **Revise from train failures only;** keep validation results out of the revision.
   - Missed triggers: the description is too narrow. Broaden the scope or the contexts.
   - False triggers: it's too broad. Say what the skill isn't for, and sharpen the boundary with neighbors.
   - Don't paste keywords from failed queries. Name the category they belong to.
   - After several stalled rounds, try a structurally different description, not another tweak.
   - Recheck the 1024-character limit; descriptions grow while tuning.
4. **Repeat** until the train set passes or improvement stops; about five rounds is usually enough. If nothing improves, suspect the queries: too easy, too hard, or mislabeled.
5. **Pick** the iteration with the best validation pass rate, which may not be the last.

Then put the chosen description in the frontmatter, validate, and check it on 5–10 fresh queries that were never part of tuning.
