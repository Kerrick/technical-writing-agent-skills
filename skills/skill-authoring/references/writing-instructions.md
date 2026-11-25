# Writing instructions

Read this when drafting or substantially revising a skill's body. Adapted from the Agent Skills best practices; [NOTICE.md](../NOTICE.md) has the credit and the changes.

## Ground it in real expertise

A skill generated from general knowledge alone comes out vague ("handle errors appropriately", "follow best practices"). Feed project-specific material into the writing:

- **A finished task.** Do a real task with an agent, then extract the reusable pattern: the steps that worked, the corrections you made, the input and output formats, and the facts you had to supply.
- **Project artifacts:** runbooks, style guides, API specifications, schemas, config files, review comments, issue threads, patches and fixes in version control, and failure cases with their resolutions. Your team's incident reports are better than a generic best-practices article, because they hold your schemas and failure modes.

Then run the draft on real tasks and feed back every result, not only the failures. Read the execution traces, not only the outputs. An agent that wastes steps usually had instructions that were too vague, instructions that didn't apply to the task (it followed them anyway), or options with no default.

## Spend context on what the agent lacks

The body shares the context window with everything else. For each line, ask whether the agent would get the task wrong without it. If not, cut it. Skip what a PDF is or how HTTP works; say which library to use and what to fall back to.

- **Scope a coherent unit,** like a well-chosen function. Too narrow, and agents load several skills for one task, which may conflict. Too broad, and agents have trouble loading the skill at the right times.
- **Aim for moderate detail.** Concise steps with a working example work better than exhaustive coverage. With instructions that don't apply to the task, the agent goes down unproductive paths. Leave most edge cases to the agent's judgment.
- **Move detail to references,** and say when to read each one: "Read `references/api-errors.md` if the API returns a non-200 status" is better than "see references/ for details".

## Calibrate control

- **Give freedom where approaches vary.** Say what to look for and why, and let the agent choose how. An agent that understands the purpose makes better calls in cases you didn't foresee.
- **Be prescriptive where the operation is fragile,** consistency matters, or the order is fixed: give the exact command, and say not to change it.
- **Give a default, not a menu.** Name one tool or approach, and the alternative in a clause with its condition ("For scanned PDFs, use OCR instead").
- **Teach the approach, not one answer.** Steps that work for any instance of the task are better than the specific answer to one instance. Specific details still belong: templates, hard constraints, tool-specific commands.

Most skills mix these; calibrate each part on its own.

## Patterns

Use the ones that fit.

**Gotchas.** Often worth the most: concrete facts that contradict reasonable assumptions, each a correction to a mistake the agent will make. "The `users` table uses soft deletes; add `WHERE deleted_at IS NULL`" is a gotcha. "Be careful with the database" isn't. Keep gotchas in `SKILL.md`, where the agent reads them before it meets the situation. When you correct an agent, add the correction here.

**Templates for output.** When output must follow a format, give a template; agents match concrete structures more reliably than prose descriptions. Keep short ones inline, and put long or situational ones in `assets/` with a pointer.

**Checklists.** For multi-step work with dependencies or gates, with a checklist to tick through, the agent doesn't skip steps.

**Validation loops.** Do the work, run a validator (a script, a reference checklist, a self-check), fix what fails, and repeat until it passes. Only then move on.

**Plan, validate, execute.** For batch or destructive operations, have the agent write a plan in a structured file, validate it against the source of truth with a script, and only then execute it. With error messages that say what's wrong and what's available ("Field 'signature_date' not found; available: customer_name, signature_date_signed"), the agent can fix the plan itself.

**Bundled scripts.** When traces show the agent writing the same helper on every run (a parser, a chart builder, a validator), write and test it once, and bundle it. See [scripts.md](scripts.md).
