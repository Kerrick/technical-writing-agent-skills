# 2. Baseline

The second message, in the same session as [1. Recall](01-recall.md). The session writes the baseline skill: a record of what the model believes about the field, in Agent Skills form. It usually writes into the agent's installed skills folder; move it to `${RUN}/baseline/technical-writing/` before step 9.

"The agent-skills skill" must be the pinned copy in `${AGENT_SKILLS}`, installed as a skill before step 1 (for example, symlinked into the agent's skills folder), because the baseline is shaped by its exact text. In the first run it was installed at `~/.agents/skills/agent-skills`.

```
Now read the entirety of the agent-skills skill and all its references, then write a skill for it. Do not use any other tools or read any other files.
```

**The fork point is the end of this turn.** Every later step that says "fork the baseline point" forks this session here, before anything else is sent. Don't send anything else to this session.
