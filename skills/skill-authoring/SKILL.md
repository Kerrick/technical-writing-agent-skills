---
name: skill-authoring
description: >-
  Use when creating, editing, reviewing, validating, or testing an Agent Skill
  (a folder with a SKILL.md file): writing one from scratch or from a run of
  corrections, deciding what belongs in it, splitting a long SKILL.md into
  references, fixing a description that triggers too often or not at all,
  bundling a script, writing evals and trigger queries, or measuring whether a
  skill beats having no skill. Use it even when the user says "make this a
  skill", "teach the agent our process", or "why does the agent ignore my
  instructions" without naming SKILL.md. Not for READMEs (use readme-rewrite),
  other documentation pages (use developer-docs), or agent instruction files
  such as AGENTS.md and CLAUDE.md.
license: CC-BY-4.0
metadata:
  author: Kerrick Long
  version: "1.1.0"
---

# Skill authoring

You already know the Agent Skills format. This skill adds what the format guide leaves out: how to decide what a skill holds, how to keep its writing clean, and how to prove it helps. Where a rule here conflicts with advice you would usually follow, follow the rule here.

A skill holds only what its target model doesn't already do. Everything else costs context on every run and buries the rules that matter.

## Choose the task

- **Create a skill:** follow **Workflow** from step 1.
- **Edit a skill:** read the whole skill first, every reference included, then follow **Editing an existing skill**.
- **Review a skill:** read the whole skill, run the validator (step 8), work through the **Pre-handoff checklist** and **Gotchas** as a reviewer, and report each problem with its file and line. Change nothing unless asked.
- **Validate only:** run step 8 and report its output.
- **A description that misfires:** read [references/descriptions.md](references/descriptions.md).
- **Prove a skill helps, or compare two versions:** read [references/evaluating.md](references/evaluating.md).

## Workflow

1. **Name the target.** Write down the model and effort level the skill is for, the job it does, and the skills it sits beside. A skill is a measured difference for one model. On another model it's a guess, so a version made for another model is a variant, kept apart, not a replacement.
2. **Fix a baseline.** Before gathering any rules, record what the target model does without the skill: in a fresh session, with no version of the skill installed, have it do two or three representative tasks, or write down what it knows about the domain. Save the result and never edit it. Every later "does the model already do this?" is answered against this file, not against your sense of what models know. For a skill built rule by rule from outside sources, read [references/measured-build.md](references/measured-build.md) before step 3.
3. **Gather evidence.** Use real material: corrections the user gave an agent, review comments, runbooks, incident fixes, the project's own code and config. Write each candidate rule in this shape:
   - **Rule:** what to do, standalone, so a reader who has never seen the evidence can act on it.
   - **Applies to:** every task, or which kind of task.
   - **Without it:** what an agent does wrong.
   - **Kind:** new to the model; a correction that replaces advice the model follows; or known to the model but often skipped.
4. **Filter against the baseline.** Drop each rule the baseline already states and follows. Keep a rule the baseline states but breaks, as a checklist item. State a correction as the right rule itself, not as "unlike the usual advice". Decide these tests before you judge the rules, and apply them the same way to every rule.
5. **Place each rule.** Rules for every task go in SKILL.md. Rules for one kind of task go in a reference file for that kind, and SKILL.md says when to read it. Each "Without it" becomes a gotcha where it names a mistake an agent would make. Known-but-skipped rules go in a checklist. Add nothing of substance beyond the rules and the backbone they hang on (a short procedure, a checklist). When in doubt, leave it out.
6. **Write the frontmatter.** Read [references/specification.md](references/specification.md) for the field rules and limits. Write the description by **Descriptions** below.
7. **Write the body.** Follow **Rules for every skill**. For the patterns (gotchas, templates, checklists, validation loops), read [references/writing-instructions.md](references/writing-instructions.md). If the skill bundles or runs code, read [references/scripts.md](references/scripts.md).
8. **Validate,** fix every error, and repeat until it passes. Run, from this skill's directory:
   ```bash
   uv run scripts/validate.py path/to/skill-dir
   ```
   It needs [uv](https://docs.astral.sh/uv/), which supplies Python and the pinned `skills-ref` library. It checks the frontmatter: required and allowed fields, name rules, length limits, and that `name` matches the directory. Pass several directories to check them all; add `--json` for machine-readable output. Exit codes: 0 valid, 1 errors, 2 bad arguments. It doesn't read the body, so it can't catch broken links, orphaned references, or a SKILL.md over 500 lines; check those yourself.
9. **Check placement.** For each rule, note the file and line where the skill states it. Every rule should have exactly one place. Read the cited lines to confirm each states its rule. After any edit above a cited line, recheck the citations after it.
10. **Write evals.** Read [references/evaluating.md](references/evaluating.md) for output evals and [references/descriptions.md](references/descriptions.md) for trigger queries.
11. **Report.** Give the file list with line counts, the validator's output, and every judgment call you made, so the user can overturn one at a glance.

## Editing an existing skill

- Snapshot the skill before you change it, outside the skill folder, so you can evaluate the new version against the old one.
- Add a correction the user had to give as a gotcha in SKILL.md, where the agent reads it before it meets the situation.
- Don't append. Fit each change into the structure that's there, and remove what the change makes redundant.
- Keep history out of the body. Why a rule changed belongs in the commit message, and a difference in how an earlier version was made belongs in that version's record. The skill states what to do now.
- When a rule applies to every skill a maintainer owns, put it in the place that holds rules shared by all of them, not in one skill alone. Add a shared rule after the same correction comes up twice, or once where the habit did real harm.
- When an eval shows agents following a rule without the skill, consider removing it.

## Rules for every skill

**Open with what the skill adds.** In a sentence or two, say whom the skill is for, what they already know, and that its rules add to that knowledge rather than restate it. Say that a rule here wins where it conflicts with the reader's usual advice.

**Give a procedure with defaults.** Give numbered steps for the main task. Where several approaches work, name one as the default and give the alternative in a clause, with when to use it.

**Say when to read each reference.** Every reference file is linked from SKILL.md with the condition for reading it: the task, the kind of page, the error. No reference file that nothing points to. Link references from SKILL.md only, one level deep.

**Keep every link inside the installed skill.** A skill is installed as its folder alone. A relative link to anything outside that folder, such as the repository's docs or a vendored copy of another skill, breaks once installed. Copy or adapt what the skill needs into it, or link to a public URL.

**No machine paths or volatile pointers.** Use paths relative to the skill root for the skill's own files, and describe other things by what they are. Don't cite line numbers of files outside the skill; describe a rule by what it says.

**Never direct an agent to write a placeholder to disk.** The skill must never tell an agent to leave a placeholder, a question, or a note to the user in a file, such as `TODO(verify)`, `[TO CONFIRM]`, or `[UNKNOWN]`. Where a rule says to mark or flag something for the user, have the agent leave it out, or raise it in chat, instead. The same holds for you: what you write into the skill and its evals is final. Bring up in chat only what truly needs the user's judgment, where a wrong call would do real harm, and keep it short. For everything else, take the answer the evidence supports that claims the least on the user's behalf, write it as final, and list the call in your report.

**State verified facts plainly.** Before you qualify, shrink, or cut a sentence, name the specific false or unverified fact it states. If you can't name one, it isn't an overclaim, so leave it as written. A statement of what something is for, or what it does, is not an overclaim. Never attach how narrow the proof was ("tested with", "in our testing", "should work").

**State a limit only where it changes what the reader can do.** A platform, a version, a model, a prerequisite, a risk to their data: state it once, as a fact, where the skill keeps its caveats, such as the `compatibility` field.

**Don't narrate the skill's proof.** Proof narration is a sentence in a skill about how far its own testing has got. It either apologizes ("evals not yet run", "untested on other models") or boasts ("passes all its evals", "proven on three projects"). Neither tells the agent using the skill what to do. Keep it in contributor documentation, and state in the skill only the fact it implies, such as the model the skill is for. Have the skill hold agents to the same rule in the pages they write for users.

**Explain the why where the agent must judge.** Give the reason behind a rule the agent will have to apply to cases you didn't foresee. Be prescriptive, with exact commands, where the operation is fragile.

**Credit adapted text.** When a skill adapts someone else's text, set `license` to that text's terms, or terms that honor them, and add a `NOTICE.md` naming the source, its holder, its license, which file came from which page, and every change you made.

## Descriptions

Agents decide whether to load a skill from its description alone. Write it as an instruction: "Use when…". Name the user's intents, not the skill's mechanics, including phrasings that don't name the domain. End with what it is not for, naming the sibling skill to use instead, and have each sibling's description point back. Keep it under 1024 characters. To test or tune one, read [references/descriptions.md](references/descriptions.md).

## Pre-handoff checklist

- [ ] **Delta only.** Every rule passed the baseline test in step 4; nothing restates what the target model already does.
- [ ] **Placed once.** Every rule has exactly one place, and the cited lines state it.
- [ ] **Validator passes,** on the final version of the files.
- [ ] **Size.** SKILL.md under 500 lines and about 5,000 tokens; each reference focused on one kind of task.
- [ ] **Links.** Every link resolves inside the skill folder or is a public URL; every reference is linked from SKILL.md with when to read it.
- [ ] **No placeholders.** No file in the skill or its evals holds a placeholder, a question, or a note to the user, and no instruction tells an agent to write one.
- [ ] **No diluted facts.** Every qualifier names a false or unverified fact; every stated limit changes what the agent can do.
- [ ] **No proof narration.** No sentence in the skill apologizes for, or boasts about, how far its own testing has got.
- [ ] **Scripts run as an agent would run them:** from the skill directory, with the command the skill gives, including `--help`. Delete what the test left behind, such as `__pycache__/`.
- [ ] **Licensing.** Adapted text is credited in `NOTICE.md`, and the `license` field matches.
- [ ] No gotcha below describes the skill.

## Gotchas

- Writing what models already know (what a CSV is, how to write clear prose, "handle errors appropriately"), which dilutes the rules that matter.
- Judging "the model already knows this" from intuition instead of a saved baseline, so rules the model breaks get cut and rules it follows stay in.
- Letting the session that wrote the baseline, or that read the sources, write the skill. It pulls the baseline's structure, or the sources' wording, back in. See [references/measured-build.md](references/measured-build.md).
- Linking to a file in the surrounding repository, which isn't installed with the skill.
- Adding a reference file and never saying when to read it, so the agent never does, or always does.
- Offering a menu of tools with no default, so the agent tries several.
- Carrying a source's instruction to "mark it with TODO" into the skill, which hands the work back to the user.
- Narrating the skill's proof in SKILL.md, apologizing ("evals not yet run", "this may not work") or boasting ("passes all its evals"), which tells the agent nothing it can act on.
- Putting a gotcha in a reference file whose trigger the agent won't recognize until it's too late.
- Testing a skill in a session where an installed copy, or a sibling skill, can load too, so results measure the wrong thing.
- Keeping evals inside the skill folder, where an agent under evaluation can read the assertions, and every install ships them.
- Leaving an unquoted number in `metadata` (`version: 1.0`). The spec requires strings, and the validator accepts the number without a warning. Quote it: `version: "1.0"`.
- Naming the PyPI package as the command: `skills-ref` installs a command named `agentskills`. Prefer `scripts/validate.py`, which also accepts `.` as a path.
