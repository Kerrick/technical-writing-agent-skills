# Reference, how-to guides, explanations, and release docs

## API reference (HTTP, library, CLI, config)

Reference is consulted, not read. Optimize for lookup: predictable structure, exhaustive facts, no narrative.

### What every entry needs

- **Name and one-line purpose** (what it does, not "a function that...").
- **Signature or request shape,** copied or generated from source.
- **Parameters/fields:** name, type, required or optional, default, allowed values or range, units, and the *effect* (not just "the timeout"; say "milliseconds before the connection is aborted; 0 disables").
- **Returns / response:** type and shape, including empty and null cases, pagination, and ordering guarantees.
- **Errors:** each error, status code, or exception, with the *cause* and the *fix*. Include the exact message text.
- **Side effects and guarantees:** idempotency, atomicity, rate limits, thread safety, permissions or scopes required, cost.
- **At least one realistic example** with request and response (or call and result). For HTTP, show curl plus one SDK. Examples show the common case; a second shows the most important option.
- **Version info:** added in, changed in, deprecated in, removed in, with link to replacement.
- **Related:** the guide that shows it in use, and sibling entries easily confused with it.

### Structure rules

- Same template for every entry of the same kind. Sameness is the feature; readers learn where to look.
- Organize to mirror the product (the module, resource, or command tree), alphabetize flat lists, and provide a search-friendly index.
- Describe authentication, base URLs, pagination, errors, rate limits, versioning, and idempotency **once** in a shared overview page and link to it, not repeated per endpoint.
- Neutral voice. No opinions, no "you should"; put recommendations in guides and link them.
- Document the default behavior and what happens with omitted optional fields; people rely on defaults you didn't mention.

### Generate where possible

- Source of truth first: OpenAPI/JSON Schema, type definitions, docstrings, `--help`, CLI man pages. Generate tables from them in CI so docs can't drift; add human prose in overrides.
- For hand-written docs, include a checklist or script that compares documented names to those in code.
- Example code in reference should be extracted from tests or compiled in CI when the toolchain allows.

### Reference gotchas

- Undocumented parameters people discover become de facto API. Either document them as unstable or state that undocumented means unsupported.
- Types in docs must match wire format, not internal types (a 64-bit integer returned as a string, timestamps as ISO 8601 UTC, enums as exact strings, case sensitivity).
- Don't describe a parameter by repeating its name ("`user_id`: the user ID"). Say what it identifies, where to get one, and the format.
- List *all* error cases, including 429, 5xx behavior, and what's safe to retry.
- Deprecations need a date or version, a replacement, and a migration path; "deprecated" alone is useless.

## How-to guides

A how-to answers "How do I X?" for someone who already knows the basics.

- **Title is the task:** "Rotate an API key," "Run migrations in CI." Start with a verb. Write what the reader would search.
- **Start with the goal and prerequisites,** then numbered steps, then verification ("You should see...").
- **Assume competence;** link instead of re-teaching. Don't lecture on why.
- **Handle real-world forks** with short conditionals ("If you use Postgres, also run...") rather than separate pages, unless the paths diverge substantially.
- **Cover the unhappy path** briefly: the common errors for this task and fixes.
- **One task per guide.** If two tasks always occur together, put them in sequence under one title; if they have independent uses, split.
- End with what to read next, and rollback or cleanup when the task changes state.

## Explanations (concepts, architecture, design rationale)

- Answer "why" and "how does it fit together." Provide context, history, tradeoffs, and alternatives considered. Opinions are allowed here when reasoned.
- Use diagrams for structure and flow; every diagram needs surrounding text that states its point, plus alt text. Prefer text-based diagram source (Mermaid, PlantUML) so it's diffable.
- Define the mental model with an analogy only if you also say where it breaks.
- Link out to reference for details and guides for action. Don't turn it into a list of steps or parameters.
- Name the scope: what this page covers and what it doesn't.

## Migration and upgrade guides

- Start with who needs to act and by when (versions affected, end-of-support date).
- Order: summary of breaking changes with severity; step-by-step upgrade path in the order to do it; before/after code for every breaking change; how to detect you're affected (grep patterns, deprecation warnings, a codemod or CLI check); how to roll back.
- Give the reason for each break in a sentence, since people accept pain they understand.
- Mention intermediate versions if skipping is unsupported.

## Changelogs and release notes

- Audience is the upgrader. Group by Added, Changed, Deprecated, Removed, Fixed, Security. Breaking changes first and visibly marked.
- Each entry says what changed *for the user* ("`fetch` now retries on 503"), not the implementation ("refactored RetryManager"). Link to the issue/PR and docs.
- Date and version every release; follow semantic versioning, and say what that promises for this project.
- Don't dump commit logs; curate.

## Error message and troubleshooting docs

- Index by the **exact text or code** users see, so pasting an error finds the page.
- Each entry: symptom, cause(s) in order of likelihood, how to confirm, fix, and when to escalate. Include how to collect logs and version info for a bug report.
- Better, fix the message itself: it should state what happened, why, and what to do. Suggest message rewrites to the user when you find unhelpful ones in the code.
- Troubleshooting is not a place to keep workarounds forever; link to the issue and delete the entry when the bug is fixed.

## Information architecture across a doc set

- Top-level navigation by the reader's journey: Get started → Guides → Concepts → Reference → Changelog/Support. Don't organize by your org chart or repo layout.
- Provide a single, short quickstart that reaches the first success in minutes; it's the highest-leverage page.
- Every page: say what it is for, link up to its parent and across to the neighboring modes.
- Keep URLs stable; add redirects when moving pages; version docs alongside the software if multiple versions are supported and show a version selector.
- Treat docs as code: in the repo, reviewed in PRs, linted (Vale or a prose linter, markdown lint, link checker), built in CI, and updated in the same PR as the behavior change. Define an owner for each page.
- Maintain a glossary and a style guide (voice, terminology, capitalization of product names, code formatting conventions, how to write UI paths such as **Settings > Billing**). If one exists, follow it over anything here.
- Measure: search queries with no results, pages with high exit rates, repeated support questions, and feedback widgets all point to the next doc to write.
