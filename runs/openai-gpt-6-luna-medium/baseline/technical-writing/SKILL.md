---
name: technical-writing
description: Use when creating, restructuring, reviewing, or improving programming books, developer documentation, API references, tutorials, video scripts, learning materials, README content, or technical guides. Apply when the work must teach a technical concept or help a reader successfully use software, even if the user asks only for an outline, lesson, examples, or editorial review.
---

# Technical Writing

Create technical material that helps a defined reader accomplish a real task or build a durable mental model. Treat correctness, usability, and learning as one job: a clear explanation built on a false claim is harmful, and correct facts arranged around the author's interests can still leave readers stuck.

## Workflow

1. **Identify the reader and outcome.** Determine what the reader knows, what they need to do or understand, the context in which they will use the material, and what success looks like. Use the user's description and available project context; make a reasonable assumption when a detail is nonessential. Ask a concise question only when an unresolved choice would materially change the content.
2. **Choose the form and scope.** Match the structure to the job: a quickstart gets to a working result; a conceptual guide builds a model; a task guide supports a specific job; a tutorial teaches by doing; API reference documents exact behavior; a book or series sequences skills over time. Separate forms when one page cannot serve their different reader needs.
3. **Ground the content.** For software-specific claims, inspect the source of truth available for the task: implementation, schemas, tests, examples, official documentation, or user-provided material. Check names, defaults, versions, prerequisites, outputs, errors, limits, and side effects. Prefer the most authoritative and current source. Mark unresolved claims or assumptions; do not invent behavior, benchmarks, guarantees, citations, or examples and present them as verified.
4. **Design the learning path.** Order material from prerequisites and motivation through a useful result, explanation, practice, and next steps. Introduce one major concept at a time; connect each new idea to what the learner already knows. Make prerequisites explicit. For long-form material, define outcomes per chapter or lesson and ensure each one prepares for the next.
5. **Draft for action and understanding.** Lead with the reader's goal. Use concrete examples, direct language, meaningful headings, and steps in the order they are performed. Explain why a step matters where that prevents confusion. Define unfamiliar terms at first use. Prefer a small complete example over a broad but ungrounded survey.
6. **Check every instructional path.** Mentally or mechanically follow the procedure from a clean starting point. For code, verify syntax and dependencies when tools or user instructions authorize checking; distinguish tested code from illustrative pseudocode. Confirm that commands, file names, expected output, and transitions agree. Include recovery guidance for likely failure points.
7. **Revise and validate.** Review for technical accuracy, reader fit, completeness, sequence, accessibility, consistency, and unnecessary repetition. Remove content that does not advance the reader's task or understanding. For substantial work, review the artifact as a newcomer would: Can they locate the right section, follow it, recognize success, and continue?
8. **Report the result plainly.** Summarize what was created or changed, identify important assumptions or unverified details, and state what was checked. Do not claim execution or verification that did not happen.

## Choose the structure by reader job

- **Quickstart:** state prerequisites and estimated starting state; give the shortest safe path to a visible success; show expected output; link or point to the next useful guide. Avoid turning it into a complete reference.
- **Conceptual guide:** state the question or model; explain key terms and relationships; use an example or diagram when it makes the model easier to grasp; explain limits and common misconceptions.
- **Task guide / how-to:** name the goal; list prerequisites; give ordered, actionable steps; show checkpoints and likely recovery paths; finish with the result and relevant follow-up.
- **Tutorial:** keep the learner actively doing meaningful work. Introduce concepts at the moment they are needed, explain decisions, and pause for prediction or practice. Avoid unexplained copy-paste sequences and incidental complexity.
- **API reference:** document each public operation consistently: purpose, signature, parameters and types, defaults, return value, errors, side effects, version or availability constraints, and a minimal example. Derive details from the implementation or authoritative schema. Do not replace exact reference facts with promotional prose.
- **Book or course:** build a progression, not a pile of topics. State audience, prerequisites, and outcomes. Give each unit a focused purpose, teach concepts before relying on them, revisit ideas in new contexts, and include exercises with clear objectives. Keep examples coherent across units where that helps transfer.
- **Tutorial video / screencast script:** optimize for spoken comprehension and visible action. Separate narration from on-screen actions, code, and editor notes. Keep steps observable, avoid narration that merely reads the screen, and allow time for viewers to inspect results. Describe cuts or prerequisites when the recording skips setup.

## Teaching and learning

- Make learning outcomes observable: what should a reader be able to explain, build, diagnose, or choose afterward?
- Activate useful prior knowledge, but do not assume familiarity with unstated tools or conventions.
- Move from a worked example to a partially guided task and then independent practice when the material warrants it. Explain the reasoning behind important choices, not just the sequence of keystrokes.
- Use examples that reveal the concept and remain small enough to inspect. Show expected behavior and, when useful, a plausible incorrect result and how to diagnose it.
- Place definitions near first use. Keep terminology stable; distinguish similar concepts explicitly when their difference affects decisions.
- Use exercises to practice the stated outcome. Provide success criteria, hints or solutions when appropriate to the audience and format.
- Manage cognitive load: introduce complexity in steps, make prerequisites visible, avoid unrelated setup, and use diagrams or tables only when they clarify relationships or comparisons.
- Support transfer by explaining when a pattern applies, where it stops applying, and how the learner can adapt it.

## Technical accuracy and examples

- Treat code samples, commands, API signatures, and outputs as executable claims. Check them against the relevant version and environment when possible.
- State language, runtime, package, service, and operating-system assumptions when they affect results. Include setup only when needed for the promised path.
- Keep examples internally consistent: identifiers, paths, types, response shapes, and expected output must match across prose and code.
- Prefer complete, minimal examples. If a snippet omits context, label the omission and show where it belongs. Never imply that placeholder or pseudocode is directly runnable.
- Explain destructive, costly, irreversible, security-sensitive, or externally visible steps before the reader reaches them. Show safe defaults and a way to inspect the outcome.
- Document errors and edge cases that change what a reader should do. Avoid exhaustive lists that do not support the intended task.
- Distinguish stable concepts from version-specific behavior. Date or version-scope information that can change, and verify it when appropriate.

## API reference checklist

For every documented endpoint, function, class, command, or configuration option, check the applicable items:

- Exact name, location, signature, and availability/version
- Purpose and intended use
- Required and optional parameters, types, constraints, defaults, and examples
- Return value or response shape, including meaningful fields
- Errors, status codes, exceptions, and validation behavior
- Side effects, state changes, retries, idempotency, and relevant limits
- Authentication, permissions, security, or privacy implications
- A minimal example that matches the documented contract

Do not fill gaps by guessing. Call out unknowns for the owner or resolve them from a source of truth.

## Editing and review

When improving existing material, preserve correct information and the author's intended audience while fixing the highest-impact reader problems first. Check whether the content belongs in this artifact, whether headings match what readers will scan for, whether steps can be followed in order, and whether examples demonstrate the stated point. Keep established terminology and style unless they are inconsistent or obstruct understanding. Do not rewrite merely to impose a preferred voice.

For review feedback, prioritize issues that block task completion or teach incorrect behavior. Cite the location, describe the reader impact, and suggest a concrete correction. Separate confirmed defects from questions or stylistic preferences.

## Final quality check

Before delivery, confirm:

- The intended reader and outcome are apparent.
- The structure fits the reader's job and the content fulfills its promise.
- Prerequisites and assumptions are stated where needed.
- Instructions are complete, ordered, and have a recognizable success condition.
- Technical claims and examples are grounded or clearly marked as unverified.
- Terms, names, versions, and examples are consistent.
- Headings and formatting support scanning and accessibility.
- The material contains enough explanation to support understanding without burying the task in unrelated detail.
- Any checks reported to the user were actually performed.
