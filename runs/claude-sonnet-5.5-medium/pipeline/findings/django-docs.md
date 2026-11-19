Source: Django docs (intro, howto, forms and HTTP threads, FAQ), commit 9e2e5a3

> Quotes and descriptions in this file are from the [Django documentation](https://docs.djangoproject.com/) ([django/django](https://github.com/django/django)), copyright (c) Django Software Foundation and individual contributors, licensed under the [BSD 3-Clause License](https://github.com/django/django/blob/main/LICENSE). Quotes are short, and used to compare and criticize.

# Django docs compared with the baseline `developer-docs` skill

Paths are relative to the docs root (`docs/`) for Django pages and to `work/` for the skill (`developer-docs/SKILL.md:N`, `developer-docs/references/teaching.md:N`, `developer-docs/references/reference-and-guides.md:N`). The skill is unchanged. Django's style guide (`internals/contributing/writing-documentation.txt`, already read, not re-read) is treated as the stated intent and cited by line only. Line numbers were taken with grep.

## How the two threads are split (context for the evidence)

**Forms.**
- *Tutorial* (`intro/tutorial04.txt`): a hand-written HTML `<form>` plus `request.POST` handling. `grep` finds no mention of the forms framework anywhere in `intro/` except a pointer in `intro/whatsnext.txt:50`.
- *Topic guide* (`topics/forms/index.txt`): HTML form basics, why POST, the framework's role, then one complete Form/view/template round trip, then rendering options. Opens with a box (`:7`) naming the reference pages for details. Depth is deferred to `formsets`, `modelforms`, `media` in a toctree.
- *Reference* (`ref/forms/api.txt`, `fields.txt`, `widgets.txt`, `validation.txt`): exhaustive attributes, interactive-shell sessions, per-field fact blocks. `api.txt:7` tells the reader to read the introduction first. Thin pages: `ref/forms/formsets.txt` is one signature plus a pointer to the topic guide; `ref/forms/models.txt` is option lists plus "See ... for example usage".
- *How-to*: none for forms itself. Related how-tos exist (`howto/csrf.txt`, `howto/custom-model-fields.txt` for the form-field hook).

**Request/response.**
- *Tutorial* (`tutorial01-04`): views and `HttpResponse` appear as steps, with links outward.
- *Topic guide* (`topics/http/views.txt`, `urls.txt`, `shortcuts.txt`, `middleware.txt`, `sessions.txt`): `index.txt` is only a toctree. `views.txt` steps through one tiny view line by line, then errors, then async. `shortcuts.txt` is closer to reference (signatures, argument lists) yet lives in the topic tree.
- *Reference* (`ref/request-response.txt`): every attribute and method, `QueryDict`, all response classes.
- *How-to* (`howto/outputting-csv.txt`, `outputting-pdf.txt`): one task each. `ref/request-response.txt` links into the CSV how-to for streaming, and the how-to carries the label that link targets (`outputting-csv.txt:58`).

---

## 1. Missed principle

**M1. Introduce each new tool as the answer to a problem the reader just hit.**
- `intro/tutorial02.txt:323`: "Wait a minute." the default object display "isn't a helpful representation", and the next step adds `__str__`.
- `intro/tutorial03.txt:393`: "Remember, when we wrote the link..." the hardcoded URL, then the fix.
- `intro/tutorial04.txt:175`: the `results` view is "almost exactly the same" as `detail`, "We'll fix this redundancy later", paid off in the generic-views section.
- `intro/tutorial05.txt:138-161`: the reader finds a bug in their own earlier method, sees it fail, then fixes it.
- Skill: absent. Nearest is `teaching.md:25` (concrete before abstract) and `teaching.md:31` (trigger an error), which don't say to motivate the tool by the reader's own visible problem.

**M2. Show the long way first, then the shortcut, named as equivalent.**
- `intro/tutorial03.txt:248` and `:316`: sections titled "A shortcut: render" and "A shortcut: get_object_or_404", each after the manual version.
- `topics/http/shortcuts.txt:79`, `:307`, `:386`: "This example is equivalent to::" followed by the expanded code.
- `intro/tutorial04.txt:228-236` (box "Why the code-shuffle?"): the tutorial deliberately did views "the hard way" and says so. The forms thread does the same one level up (raw HTML form in the tutorial, framework in the topic guide; see context).
- Skill: absent. `teaching.md:24` (worked example, then fade) is about removing scaffolding, not about expanding a shortcut.

**M3. After a sample, annotate only the non-obvious parts, as a short list.**
- `howto/outputting-csv.txt:35` and `outputting-pdf.txt:75`: the code "should be self-explanatory, but a few things deserve a mention:" then one bullet per non-obvious point (header, MIME type, finishing calls).
- `intro/tutorial04.txt:36` ("A quick rundown") and `:108` ("a few things we haven't covered yet").
- `topics/http/views.txt:29`: "step through this code one line at a time".
- Skill: absent. `SKILL.md:37` is about order (example before description) and says nothing about how to annotate afterwards.

**M4. Explain the doc set's own structure to the reader, and add a feature-axis hub next to the type-axis navigation.**
- `index.txt:304-324` ("How the documentation is organized") and `intro/whatsnext.txt:36`: one sentence per kind of page saying what need it serves and who should start where.
- `index.txt:162-170` (Forms bullet) and `:42-49`: one line per feature that puts the topic guide, reference pages and how-to together (e.g. "Custom fields" from `howto/` sits in the same list as model reference). `index.txt:307-308` says the list is thematic while the files are organised by type.
- Skill: `reference-and-guides.md:84` recommends only the journey axis (start, guides, concepts, reference). `reference-and-guides.md:86` covers per-page sibling links. Neither says to publish a map of page kinds or a per-feature hub.

**M5. Say where to get help on every entry page of a series, with separate routes for questions, bugs and security.**
- "Where to get help" box in all eight tutorial parts plus `intro/contributing.txt` (grep count: 9 files, one each). The contributing tutorial uses a different route than the others.
- `faq/help.txt:35`, `:49`, `:55`: three headed routes; for security, a private address and an explicit request not to post publicly (`:59`, `:64`).
- Skill: `teaching.md:18` handles in-place recovery only. `reference-and-guides.md:84` names a "Support" section in navigation and nothing more. No rule on repeating the route per page or splitting it by problem type.

**M6. Next to a claim of protection, state what the safeguard does not catch.**
- `howto/error-reporting.txt:125`: filtering sensitive data "is a hard problem, and it's nearly impossible to guarantee" no leaks, hence who may read the reports.
- `howto/mailers-migration.txt:32`: running tests "may not identify all relevant deprecations", with the reason (test suites swap in a non-functional backend).
- `topics/http/sessions.txt:146` ("No freshness guarantee") and `ref/request-response.txt:1050` (SameSite isn't a replacement for the main protection, only defence in depth).
- Skill: absent. `reference-and-guides.md:64` tells readers how to detect that they're affected, and `SKILL.md:64-66` tells the writer to verify; neither says to state where a check or safeguard is blind.

**M7. Don't copy a third party's steps; cover the seam and link, and say why.**
- `intro/tutorial08.txt:48`: the install steps "are not duplicated in this tutorial, because" the package "may change separately".
- `howto/deployment/wsgi/gunicorn.txt:34`, `modwsgi.txt:17` ("is your source for all the details"), `granian.txt:37`, `asgi/uvicorn.txt:38`, `asgi/hypercorn.txt:35`: each page gives the Django-specific command and defers the rest. `wsgi/uwsgi.txt` has a "seealso" saying its text is limited to the integration.
- Skill: absent. `SKILL.md:50` addresses drift from the author's own code only.

**M8. Keep change notes in self-contained blocks that can be deleted without editing nearby text; keep version numbers out of prose.**
- Pattern: separate "changed/added/deprecated" blocks placed after the thing they annotate, containing only the change. `howto/csp.txt:106`, `ref/forms/widgets.txt:708`, `topics/http/sessions.txt:101`, `ref/request-response.txt:1251` and `:1255`.
- Stated intent: `internals/contributing/writing-documentation.txt:785-788` (the blocks must be "self-contained" because they're removed after two releases) and the instruction to avoid naming a version outside such a block.
- Skill: `reference-and-guides.md:16` asks for added/changed/deprecated/removed info per entry but says nothing about placement or retirement; `SKILL.md:70` only warns against hard-coded versions.

**M9. Order alternatives from least to most effort/control and say when to move on; order extension-point method lists by importance, and say so.**
- `howto/custom-template-tags.txt:396-397`: shortcuts first, then writing from scratch "for those cases when the shortcuts aren't powerful enough"; `:823-826` repeats the escalation.
- `topics/forms/modelforms.txt:617`: widget overrides, then field classes, then "if you want complete control", full declarative fields.
- `howto/custom-model-fields.txt:149` (can an existing field be extended first?) and `:385` (methods listed "in approximately decreasing order of importance, so start from the top").
- Skill: absent. `reference-and-guides.md:22` says alphabetise flat lists, which suits lookup pages only; nothing in the skill covers ordering options by effort or control.

**M10. When a page continues or borrows an earlier example, state the assumed starting state and flag anything the earlier pages didn't have.**
- `howto/custom-management-commands.txt:91`: the field used in the example "does not exist in the tutorial and was added" for this page.
- `intro/reusable-apps.txt:10` ("so that your example project matches the one described below") and `:56` (a file tree of the expected starting state).
- Skill: `SKILL.md:46` only says to reuse one domain; `teaching.md:17` has checkpoints within one tutorial, not for follow-on pages.

**M11. Give evaluators one whole-path tour page that says it is neither tutorial nor reference.**
- `intro/overview.txt:10`: "this isn't intended to be a tutorial or reference". The page walks model, migration, API, admin, URLs, view, template in a single pass with a link out at each stage and ends "This is just the surface".
- Skill: `teaching.md:49` suggests "a quickstart plus architecture explanation" for experts. The four-mode table (`SKILL.md:24-29`) has no tour page.

**M12. Give builders-on-top their own labelled section, with a way to detect capability in code.**
- `howto/mailers-migration.txt:157` ("Reusable library readiness") and `:368` (version/feature detection for libraries supporting several releases).
- `howto/csrf.txt:306` ("CSRF protection in reusable applications").
- Skill: `reference-and-guides.md:64` lists a single upgrade path with no audience split.

**M13. Keep a human voice in teaching and community pages: address the reader, pose the problem before the answer, avoid stacked superlatives.**
- Stated intent: `internals/contributing/writing-documentation.txt:364-430` (the "frictionless" rewrite loses the address to the reader, the problem-posing and the sense that the design was intentional) and `:379-380` (avoid superlatives such as clear, robust, structured).
- Practised: `intro/tutorial03.txt:52-55`, `intro/tutorial05.txt:83` ("they light up your code from the inside"), `faq/general.txt:39` and `:146`; reference pages stay plain (`ref/forms/fields.txt`, `ref/request-response.txt`).
- Skill: `SKILL.md:41-42` cuts filler and marketing and fixes active voice, but never asks to keep the reader addressed or to check that a polishing pass hasn't flattened it. `SKILL.md:54` goes the other way (avoid idioms and jokes); see the note under C1 on scope.

**M14. Use singular "they" for hypothetical people; avoid gendered pronouns.**
- Stated intent: `writing-documentation.txt:435-443`.
- Practised: grep for he/she/his/her across `intro/`, `howto/`, `topics/forms`, `topics/http`, `ref/forms`, `ref/request-response`, `faq/` returns one hit, `faq/general.txt:36`, about a named real person.
- Skill: absent.

---

## 2. Correction

**C1. "A tutorial that stops to explain design has become an explanation" and "no choices" / remove alternatives are too absolute.**
- Short boxed asides outside the numbered path: `intro/tutorial02.txt:91`, `:174`, `:468` and `intro/tutorial03.txt:342` ("Philosophy"), `intro/tutorial04.txt:228` ("Why the code-shuffle?"). All come after the learner has acted, per `writing-documentation.txt:59-63` ("what matters is what the reader does ... explain afterward").
- Named tempting alternatives with the reason not to take them: `intro/tutorial03.txt:190` (template namespacing), `intro/tutorial06.txt:49` (static file namespacing), `intro/tutorial02.txt:74` ("For the minimalists").
- The learner is never asked to choose, and a reader can skip every box.
- Skill: `SKILL.md:26` ("no choices"), `SKILL.md:31` (rule of thumb), `teaching.md:23` ("Remove anything incidental: extra options, alternative approaches, tangents").
- Scope note on the same voice question: the jokes and idioms the skill avoids for translation (`SKILL.md:54`) appear in Django only on FAQ and tutorial pages, not in reference.

**C2. "Neutral voice. No opinions, no 'you should'" is too absolute for reference.**
- Short warnings or recommendations placed at the exact point of error: `ref/forms/api.txt:301` and `:1325` (prefer one accessor over another), `:401` ("Beware not to alter..."), `:666` (one output style preferred, with the accessibility reason); `ref/forms/fields.txt:1389` (avoid the default widget past a size); `ref/request-response.txt:117` (don't test for POST that way), `:1281` (avoid non-dict JSON), `:871`.
- Skill: `reference-and-guides.md:24`.

**C3. "Every entry needs at least one realistic example" is too absolute.**
- Entries that are a signature plus a pointer to a worked example elsewhere: `ref/forms/formsets.txt:18`; `ref/forms/models.txt:218`, `:247`, `:261`.
- Examples are attached where behaviour surprises (`ref/forms/fields.txt` ComboField, MultiValueField, ImageField) and omitted from plain per-field blocks such as `fields.txt:430-448`.
- Skill: `reference-and-guides.md:15`.

**C4. "Describe cross-cutting facts once and link" needs a carve-out for gotchas that bite at the point of use.**
- Same admonition repeated: namespacing in `intro/tutorial03.txt:190`, `intro/tutorial06.txt:49`, `howto/static-files/index.txt:63`; the file-upload encoding fix in both `howto/deployment/wsgi/uwsgi.txt:99` and `modwsgi.txt:84`. Readers land on one server's page, not the overview.
- Cost: copies can drift; the skill's concern (`SKILL.md:50`, `:70` "duplicated tables") is real.
- Skill: `reference-and-guides.md:23` (scoped to API overview facts, but stated without exception).

---

## 3. House convention (do not carry over)

- Cross-reference roles for settings, tags, commands, options (`:setting:`, `:ttag:`, `:cli:`); `versionadded`/`versionchanged` directives; reST heading underline order and 80-column wrap (`writing-documentation.txt:501-557`). Sphinx tooling, though the underlying habit of linking each term to its definition is general.
- A `console` directive that renders Unix and Windows tabs from one `$` block (`writing-documentation.txt:676-679`).
- "How to ..." title prefix on every how-to (`howto/*.txt` titles) versus the skill's verb-first titles (`reference-and-guides.md` how-to bullet); audience habit.
- Project voice and in-jokes (`faq/general.txt:39`, `:146`), the newsroom origin story, pronunciation guide.
- Python/Django terms (project/app, URLconf, namespacing by app directory) and the polls example itself.

---

## 4. Where the Django docs fall short

**S1. Minimising words survive despite the style guide.**
- `howto/windows.txt:89` ("can be installed easily"), `topics/forms/formsets.txt:778` ("can be easily accomplished"), `howto/custom-management-commands.txt:99` ("could be easily modified"), `intro/tutorial06.txt:21`.
- Guide line: `writing-documentation.txt:445`. Skill: `SKILL.md:41`.

**S2. A version baked into prose.**
- `howto/windows.txt:21`: "At the time of writing, Python 3.15 is the latest version." The tutorials avoid this with a substitution (`intro/tutorial01.txt:26`).
- Skill: `SKILL.md:70`.

**S3. Command and its output in one copyable block.**
- `intro/tutorial02.txt:233-239`: the `migrate` command and its result share one `console` block. `intro/tutorial05.txt:205-213` keeps them separate.
- Skill: `SKILL.md:43`.

**S4. No known-good state for a reader who diverges.**
- `grep github.com` over `intro/tutorial0*.txt` finds only third-party links (`tutorial08.txt:26`, `:72`). No part ends with a repository or tag. The only whole-project snapshot is the tree at `intro/reusable-apps.txt:56`. Per-step trees and "you should see" lines exist (e.g. `tutorial01.txt:242-255`).
- Skill: `teaching.md:17` (link to a commit or tag per step).

**S5. A promised list that isn't there.**
- `faq/troubleshooting.txt:46`: "here are two common pitfalls", then one bullet (`:49`).
- Skill: `SKILL.md:66` (walk the page literally and check that nothing promised is missing).

---

## Confirmed by the Django docs (one line each, unusual items only)

- `SKILL.md:46` (one running domain across the set): `howto/custom-management-commands.txt:9-11` and `howto/custom-template-tags.txt` reuse the tutorial's poll app.
- `reference-and-guides.md:78` (index troubleshooting by exact text): `faq/troubleshooting.txt:13` and `faq/admin.txt:5` use the error or symptom verbatim as the heading.
- `SKILL.md:41` (drop minimising words): the style guide asks for the same (`writing-documentation.txt:445`).
- `teaching.md:15` (early win): `intro/tutorial01.txt:141` ends step one with the welcome page.
- `reference-and-guides.md:12` (empty/null case in returns): `ref/forms/fields.txt:436` and a dozen siblings give an "Empty value" line per field.
- `SKILL.md:70` (no hard-coded versions): `intro/tutorial01.txt:26` uses a substitution for the version.

---

## Observed, not counted

Several how-to pages combine explanation, steps and reference.
- `howto/custom-model-fields.txt`: "Background theory" explanation (`:79`), a step sequence, and a method catalogue (`:380-385`).
- `howto/custom-management-commands.txt`: a walkthrough (`:13-160`) followed by the canonical definition of the base class with attributes and methods (`:183`).
- `howto/error-reporting.txt`: steps, then class reference (`:270`, `:322`).
- `howto/custom-template-tags.txt`: steps, an explanatory "quick overview" (`:830`) and a thread-safety discussion (`:1001`).
- `howto/custom-file-storage.txt`: steps, then method reference (`:72`).

Where they are kept apart: forms (topic guide holds all worked examples; `ref/forms/formsets.txt` and `ref/forms/models.txt` hold signatures and point back); the CSV how-to holds the task and the request/response reference links to it by label (`outputting-csv.txt:58`); each tutorial links outward for depth. The style guide states the separation as the rule (`writing-documentation.txt:83-85` reference "isn't the place for general explanation"; `:90-97` how-tos are "result-oriented").

Skill rule that this differs from: `SKILL.md:13` ("Choose one mode per page ... Mixing modes is the most common structural failure"), `SKILL.md:31`, `SKILL.md:69`.

Not counted as a correction: the guide's own intent and the pages that do separate them agree with the skill. The mixed pages are extension-point guides where no other page defines the API, they use headed sections so a reader can skip, and the reference part always follows the steps.

---

## Abstracted

Missed principles, one rule each.

1. Introduce each new tool right after the reader has met the problem it solves: show the awkward result or the duplicated code first, then give the fix, so every new thing arrives with a reason.
2. When a convenience hides several steps, teach the long way first, then show the convenience labelled as doing the same thing, and tell the learner the order is deliberate.
3. After a code sample, list only the lines or choices whose purpose isn't obvious, one short point each, and say the rest needs no comment, instead of narrating everything or burying explanation in code comments.
4. Tell readers how the documentation is organised: say in a sentence per kind of page what need it serves, and add a feature-by-feature index that lists the guide, the task pages and the lookup pages for each feature side by side, alongside any navigation by page type.
5. On every entry page of a multi-part series, say where to get help, and give separate routes for questions, bugs, and security problems, with a private channel and the reason for the last.
6. Next to any statement that a safeguard, filter or check protects the reader, state what it does not catch or guarantee, including blind spots in the test runs and warnings you tell people to rely on.
7. Do not copy another party's setup steps when they change on their own schedule: write only the points where your product meets theirs, link to their instructions, and say that this is why.
8. Keep change-history notes in short, self-contained blocks that can be deleted without touching the surrounding text, keep version numbers out of the main prose, and remove the notes after a fixed number of releases.
9. When there are several ways to do something, present them from least to most effort or control and say when to move to the next; in guides for extension points, order lists of hooks by importance and say so, and keep alphabetical order for pages used to look things up.
10. When a page continues or borrows an example from earlier pages, state the starting state it assumes, show that state if it is complex, and flag every addition that earlier pages did not contain.
11. For readers who are still evaluating, offer one tour page that walks the whole path in a single pass, says openly that it is neither a tutorial nor a reference, and links each stage to its depth.
12. When readers who build on top of your product need different steps from those who only use it, give them their own labelled section, and include a way for their code to detect which capability or version is present.
13. In teaching and community pages, write as one person to another: address the reader, pose the problem before the answer, and prefer concrete statements to piled-up superlatives; after any editing or smoothing pass, check that these qualities survived. Keep lookup pages plain.
14. Use singular "they" for hypothetical people and avoid gendered pronouns.

Corrections, one rule each.

15. A teaching page may carry short, clearly set-off asides outside the numbered path, placed after the reader has acted, that give the reason for a design or name a tempting alternative and why not; the reader is never asked to decide, and skipping every aside must not break the flow.
16. Lookup pages may carry brief warnings and recommendations, stated plainly with the reason, at the exact place a reader would go wrong; keep extended persuasion in guides.
17. Not every lookup entry needs its own example: give one where the behaviour is surprising, and for thin entries that are only a signature or an option list, point to the worked example in the guide and say so.
18. State each cross-cutting fact once and link to it, but a short gotcha that bites at the point of use may be repeated on every page where readers arrive without passing through the overview; keep the copies identical and findable by search so they can be updated together.
