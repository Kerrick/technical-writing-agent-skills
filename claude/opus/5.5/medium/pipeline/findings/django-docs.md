Source: Django docs (intro, howto, forms and HTTP threads, FAQ), commit 9e2e5a3

> Quotes and descriptions in this file are from the [Django documentation](https://docs.djangoproject.com/) ([django/django](https://github.com/django/django)), copyright (c) Django Software Foundation and individual contributors, licensed under the [BSD 3-Clause License](https://github.com/django/django/blob/main/LICENSE). Quotes are short, and used to compare and criticize.

# Django docs vs. the technical-writing skill

Skill paths are relative to `technical-writing/`. Django paths are relative to `docs/`. "Style guide" means `internals/contributing/writing-documentation.txt`, which I treat as the stated intent behind the pages.

## How the two feature threads are split

**Forms.**
- The tutorial (`intro/tutorial04.txt:14-195`) builds a voting form in raw HTML, reads `request.POST` by hand, and never introduces the forms framework. It links out to the request/response reference.
- The topic guide (`topics/forms/index.txt`) starts from HTML forms and GET vs. POST (`:21-88`) before reaching the `Form` class. It builds one small form end to end (form, view, template: `:187-379`), then a fuller `ContactForm` (`:424`). An "About this document" box at the top (`:7-12`) sends readers to three reference pages.
- The reference pages (`ref/forms/api.txt`, `fields.txt`, `validation.txt`) reuse the same `ContactForm` and tell readers to read the topic guide first (`api.txt:7-11`). The smaller reference pages open the same way: `ref/forms/index.txt:5`, `models.txt:11`, `formsets.txt:5`.
- The formset and model-form topic guides carry most of their own reference (`topics/forms/formsets.txt:518-964` uses attribute and method directives). The formset reference page is only a function signature that points back (`ref/forms/formsets.txt:14-18`).
- No how-to page covers forms.

**HTTP.**
- The tutorial introduces URLconfs, views, `Http404` and redirects (`tutorial01`, `tutorial03`, `tutorial04`). It links to `topics/http/urls` and `ref/request-response` for depth.
- `topics/http/urls.txt` explains the request-matching algorithm (`:29-66`) and reuses the tutorial's polls app for namespaces (`:705-707`).
- `topics/http/shortcuts.txt` lives in topics but is pure reference: signature, required and optional arguments, example, equivalent long form.
- `topics/http/generic-views.txt` is a one-line pointer to the reference (`:5`).
- `ref/request-response.txt` is reference with REPL examples.
- How-tos (`outputting-csv`, `outputting-pdf`, `csrf`, `error-reporting`) use these objects to reach a specific result.
- The FAQ answers in a line and links to one of the above.

## 1. Missed principles

**M1. Write in a human voice, not a frictionless one.**
- Evidence: the style guide's Voice section asks for one person addressing another, lively and figurative language, and "some friction". The pages follow it:
  - `intro/tutorial03.txt:52-55` "You will be pleased to know…"
  - `intro/tutorial05.txt:654` "**It doesn't matter**. Let them grow."
  - `intro/whatsnext.txt:22-23` jokes about a document on how to read the document about documentation.
  - `faq/usage.txt:20` "chunky bacon".
  - `intro/overview.txt:145` "it's not just scaffolding -- it's the whole house".
- Tutorials use a collaborative "we/let's" for shared work: `tutorial01.txt:5`, `tutorial03.txt:148`.
- Skill: absent as a positive rule. `SKILL.md:70` ("Use second person") and `references/style.md:30` ("Avoid idioms… humor") point the other way.

**M2. Introduce each feature as the fix for a visible problem in the reader's current code.**
- `tutorial02.txt:323`: the unhelpful `Question object (1)` output motivates `__str__`.
- `tutorial03.txt:169`: "There's a problem here, though: the page's design is hardcoded in the view" motivates templates.
- `tutorial03.txt:393-404`: hardcoded URLs motivate `{% url %}`.
- `tutorial04.txt:200-202`: redundant views motivate generic views.
- `tutorial05.txt:135-159`: a real bug, confirmed in the shell, motivates tests.
- Style guide: "Explain the nature of the problem we're solving."
- Skill: absent. `references/tutorials.md:48` covers concept pacing but not motivation.

**M3. Teach the long form first, then the shortcut, and state that they're equivalent.**
- `tutorial03.txt:225-277`: loader plus `HttpResponse`, then `render()`.
- `tutorial03.txt:285-340`: try/except `Http404`, then `get_object_or_404`.
- `tutorial04.txt:228-236`: function views "the hard way", then generic views ("You should know basic math before you start using a calculator").
- Reference repeats the pairing: `topics/http/shortcuts.txt:79, 307, 386` ("This example is equivalent to") and `ref/forms/validation.txt:248-252`.
- Skill: absent. `references/tutorials.md:46` ("One path") doesn't address it.

**M4. Answer the reader's likely objection or wrong move at the point where they'd make it, on every page type.**
- Reference:
  - `ref/forms/fields.txt:184` "You may be thinking, why not just pass a dictionary…", then shows why that fails.
  - `ref/request-response.txt:115-119`: don't use `if request.POST` to detect the method.
  - `ref/forms/api.txt:67`: an empty dict still makes a bound form.
  - `ref/forms/models.txt:54-57`: typos in `Meta` raise no error.
- Tutorials:
  - `tutorial04.txt:228` "Why the code-shuffle?"
  - `tutorial05.txt:38` "So why create tests, and why now?"
  - `intro/contributing.txt:320` "But this testing thing looks kinda hard..."
- Skill: `references/explanation.md:14` confines misconception-refuting to explanation pages, and `references/api-reference.md:3` ("Be austere") implies reference shouldn't do it.

**M5. Tell stuck learners where to get help at the top of every tutorial part.**
- A "Where to get help" box appears once in each of `tutorial01`–`tutorial08`.
- `tutorial08.txt:58-74` adds an ordered escalation path: package docs, issue tracker, forum, chat.
- Skill: absent.

**M6. Mark which advice is general practice and which is specific to the product.**
- `tutorial04.txt:49-50` and `:139-140`: "This tip isn't specific to Django; it's good web development practice in general."
- `ref/request-response.txt:898` "There's nothing Django-specific about the `Content-Disposition` header".
- `howto/custom-model-fields.txt:54` "nothing Django-specific about it".
- Skill: absent.

**M7. Say when an example cuts a corner, and what real code should do instead.**
- `tutorial03.txt:218-219`: templates use incomplete HTML "To make the tutorial shorter"; use complete documents in real projects.
- `tutorial07.txt:378-381`: overriding the template is for teaching; "In an actual project" you'd use an attribute.
- `topics/http/sessions.txt:522-526`: the logout example is "not … a full `logout()` implementation".
- Skill: absent. `SKILL.md:86` only asks that examples be runnable.

**M8. Pair every concept guide with its reference pages in both directions, at the top of each.**
- Guide to reference: `topics/forms/index.txt:7-12`.
- Reference to guide:
  - `ref/forms/api.txt:7-11` ("You should read the introduction… first")
  - `ref/forms/index.txt:5`, `ref/forms/models.txt:11`, `ref/forms/formsets.txt:5`
  - `howto/writing-migrations.txt:5-7`
- Skill: `SKILL.md:81` asks each page to link its prerequisites. Nothing makes the guide/reference pairing a structural element, and the reference templates in `references/api-reference.md` have no pointer to a guide.

**M9. Use one example domain across a feature's guide and reference pages, and reuse the beginner tutorial's project in later pages.**
- `ContactForm` is the same form in `topics/forms/index.txt:424`, throughout `ref/forms/api.txt`, and in `ref/forms/validation.txt:293`.
- The tutorial's polls app returns in:
  - `howto/custom-management-commands.txt:9-11` ("from the tutorial")
  - `howto/custom-template-tags.txt:705-706`
  - `topics/http/urls.txt:705-707`
- A single how-to also keeps one example throughout: `howto/custom-model-fields.txt:32-33`.
- Skill: `references/tutorials.md:50` and `references/books.md:14` limit running examples to one tutorial or book.

**M10. Tell readers how the docs are organized and which kind of page to use for what.**
- `index.txt:304-323` and `intro/whatsnext.txt:36-82` describe the four page types to the reader.
- `whatsnext.txt:7-8` sets expectations about how much the reader has covered: "about 5% of the overall documentation".
- Skill: absent. The skill's mode split (`SKILL.md:31-44`) is for the writer only.

**M11. For another project's software, give only the integration step and send readers to that project's docs for the rest.**
- `tutorial08.txt:45-49`: the steps "are not duplicated… because as a third-party package, it may change separately".
- `howto/deployment/wsgi/granian.txt:37` and `asgi/hypercorn.txt:35-36`: "For more advanced usage, please read the … documentation".
- `howto/deployment/wsgi/uwsgi.txt:10-14`: seealso pointing to uWSGI's own tutorial.
- Skill: absent.

**M12. Keep FAQ answers short and route them to the canonical page.**
- `faq/models.txt:48` "Yes. See …".
- `faq/admin.txt:45-46`: a one-line pointer.
- `faq/install.txt:8-12`: "How do I get started?" is a list of links.
- Skill: absent. No reference file covers FAQ pages.

**M13. Start a concept guide from the underlying thing the reader already knows, then show what the framework adds.**
- `topics/forms/index.txt:21-88` covers HTML forms and GET vs. POST before the `Form` class.
- `howto/custom-model-fields.txt:79-142` has a "Background theory" section on column types before any code.
- Style guide: "Providing background context helps a newcomer connect the topic to things that they already know."
- Skill: `references/learning-science.md:21` and `:45` (concrete-before-abstract, pre-training) don't cover it.

**M14. Give non-warning asides a descriptive title so readers can decide whether to read them.**
- `tutorial01.txt:174` "Projects vs. apps"
- `tutorial01.txt:303` "Page not found?"
- `tutorial05.txt:230` "Different error?"
- `intro/reusable-apps.txt:34` "Package? App?"
- Style guide: titled admonitions instead of bare notes, used sparingly.
- Skill: `SKILL.md:79` treats callouts only as warnings.

## 2. Corrections

**C1. Short rationale belongs where the reader meets a surprising design, set off so it can be skipped.**
- Tutorials put "Philosophy" boxes mid-flow: `tutorial02.txt:91, 174, 468` and `tutorial03.txt:342` (why `get_object_or_404` exists rather than catching exceptions higher up).
- Reference explains an odd API in place:
  - `ref/forms/api.txt:164` ("The need for the `as_data()` method is due to backwards compatibility")
  - `howto/custom-template-tags.txt:913-916` ("It's low-level because that's fastest")
- Skill lines this corrects:
  - `references/tutorials.md:71` lists history among detours.
  - `references/tutorials.md:48` says to link rationale away.
  - `references/api-reference.md:3` says reference is austere.
  - `references/how-to-guides.md:42` allows only "one clause of why".
- These are too absolute. A titled, skippable box of a few sentences keeps the flow and answers "why is it like this?" at the moment it's asked.

**C2. "One action per numbered step" fits procedures, not narrative tutorials.**
- The beginner tutorial gives instructions in prose paragraphs, each followed by a captioned code block and an explanation: `tutorial03.txt:174-201`, `tutorial05.txt:173-198`.
- Numbered lists are kept for procedures and short how-tos: `intro/reusable-apps.txt:124-293`, `howto/delete-app.txt:10-29`, `howto/custom-file-storage.txt:11-45`.
- Skill: `SKILL.md:71` states the rule for every page.

**C3. Version notes should be self-contained, placed predictably, and removed after a set time. Version numbers shouldn't appear in body text.**
- Style guide: annotations are kept "for two releases", must be removable "without having to reflow, reindent, or edit the surrounding text", and version references elsewhere are to be avoided.
- Pages follow this:
  - `ref/forms/fields.txt:730` (`versionadded` at the top of the entry)
  - `ref/forms/widgets.txt:708`, `topics/http/shortcuts.txt:132`, `topics/http/sessions.txt:101` (`versionchanged` at the end of a section)
  - `tutorial02.txt:380-381`: a source comment marks text for future removal.
- Skill: `references/api-reference.md:103` ("Version every entry that changed: 'Since 2.3.0'") implies permanent, inline version labels.

## 3. House conventions

- **Semantic cross-reference markup on every mention.** Example: `:setting:\`INSTALLED_APPS\`` is linked repeatedly in `tutorial02.txt:33-81`. The style guide asks for "the more semantic markup… the better". The tooling makes this cheap and it serves lookup, but it conflicts with `references/style.md:17` (link the first mention only). It depends on Sphinx.
- **`.. console::` blocks** render Unix and Windows tabs from one Unix-style example (style guide). Examples are written as `pycon` REPL transcripts (`ref/forms/fields.txt`, `ref/forms/api.txt`).
- **Fixed term list and spelling:** URLconf, email, "an SQL", "-ize" spellings (style guide "Commonly used terms").
- **Build-time substitutions:** `|version|` and `|today|` in expected output (`tutorial01.txt:128-129`, `intro/install.txt:80`).

## 4. Where the Django docs fall short

- **Banned words still appear.** The style guide bans "easily", "simply", "merely" and "straightforward", yet they appear more than 20 times in the pages read. Examples:
  - `howto/windows.txt:89` "Django can be installed easily"
  - `topics/forms/formsets.txt:778` "can be easily accomplished"
  - `tutorial02.txt:281` "simply typing"
  - `howto/initial-data.txt:27` "most straightforward way"

  Skill `SKILL.md:73` agrees with the style guide; the pages don't follow it.
- **Placeholder names in examples:**
  - `topics/http/shortcuts.txt:74, 88, 159`
  - `topics/http/urls.txt:486`
  - `ref/forms/api.txt:478-480`
  - `topics/http/sessions.txt:631-637`
  - `howto/outputting-csv.txt:30`

  Skill `SKILL.md:91`.
- **How-tos without a check that the result worked:**
  - `howto/csp.txt` ends without showing how to confirm the header is sent.
  - `howto/custom-file-storage.txt` ends at a code fragment.
  - `howto/legacy-databases.txt:80-86` ends with a vague "Test and tweak".

  Skill `references/how-to-guides.md:22-24`.
- **Incomplete deprecation notice.** `ref/request-response.txt:1255-1257` deprecates `safe` with no removal version. `howto/mailers-migration.txt:52-54` shows the docs can give one. Skill `references/api-reference.md:104`.
- **Unpinned third-party installs:** `tutorial08.txt:38`, `howto/outputting-pdf.txt:29`, `howto/deployment/wsgi/gunicorn.txt:13`. Skill `SKILL.md:93`. Caveat: the docs are versioned with each release, so the risk is lower than for undated docs.
- **No recap at the end of tutorial parts.** They end with a pointer to the next part (`tutorial03.txt:470`, `tutorial06.txt:131`) and no summary of what the reader can now do. Skill `references/tutorials.md:54`.

## Confirmed

- Deliberate error: `tutorial05.txt:135-228` (bug, failing test, fix) and `contributing.txt:338-351` back `references/tutorials.md:53`.
- Fading to independent practice: `tutorial05.txt:624-645` ("Ideas for more tests") backs `references/tutorials.md:63`.
- Literal error text as heading: `faq/troubleshooting.txt:13` backs `references/how-to-guides.md` (troubleshooting).
- Change shown in context with elision: `tutorial03.txt:167` ("Leave the rest of the views… unchanged") plus filename captions back `SKILL.md:86` and the code rule on showing changes in context.
- Identical entry structure: every field in `ref/forms/fields.txt` lists the same items, and every widget in `ref/forms/widgets.txt` likewise. This backs `references/api-reference.md:3`.

## Observed, not counted

Several pages combine explanation, how-to and reference:

- `topics/http/sessions.txt`, titled "How to use sessions", combines:
  - setup steps (`:14-29`)
  - explanation of backend trade-offs and security (`:61-165`, `:741-760`)
  - a method-by-method API reference for the session object (`:177-404`)
  - a settings list (`:721-739`)
- `howto/custom-management-commands.txt` is a how-to (`:7-158`) followed by the full `BaseCommand` class reference (`:180-401`).
- `howto/error-reporting.txt` embeds class references for `SafeExceptionReporterFilter` (`:270-306`) and `ExceptionReporter` (`:322-364`).
- `topics/http/middleware.txt` combines the "onion" explanation (`:135-151`), how to write middleware (`:19-100`), and hook reference (`:159-244`).
- `topics/forms/formsets.txt` documents attributes and methods as reference entries inside the guide (`:518-964`), while its reference page is only a signature.
- `ref/forms/validation.txt` is a reference page whose second half is worked examples (`:213-424`).

Where the docs keep the kinds apart: the core forms thread (topic guide `topics/forms/index.txt` against `ref/forms/api.txt` and `ref/forms/fields.txt`, with pointers both ways), `topics/http/generic-views.txt` (a bare pointer rather than a copy), and `topics/http/shortcuts.txt` against the tutorial's narrative introduction of the same functions.

These differ from `SKILL.md:44`. I don't count them as a correction. The combined pages are mostly places where no separate reference page exists, so the reference lands in a guide or how-to. That cuts against the style guide's own "Link to reference material rather than repeat it", and it makes lookup harder (session methods are under "How to"). The thread where the kinds are kept apart is the cleanest one read. The mixing is evidence of missing pages, not of mixing working better.

## Abstracted

**Missed principles**

1. Write as one knowledgeable person talking to another. Address the reader, use "we" for work you do together, allow a vivid comparison or a light joke when it makes an idea stick, and use the exact technical term. Don't sand the prose into neutral summary.
2. Before introducing a feature, let the reader see the problem it solves in what they've built so far: an unhelpful output, duplicated code, a hardcoded value, a bug. Then present the feature as the fix.
3. When a convenience API wraps a common pattern, show the pattern written out first, then the convenience version, and say plainly that they do the same thing. Repeat that equivalence in the reference entry for the convenience API.
4. Wherever a reader is likely to try an alternative that doesn't work, or to doubt that a step is worth it, raise that thought in their words and answer it on the spot. This applies on every page type, including reference entries.
5. At the start of every part of a multi-part tutorial, tell the reader where to go for help if they get stuck, and give an order to try those places in.
6. When advice holds beyond the product being documented, say so. When it's specific to the product, let that be clear too.
7. When an example is simplified for teaching (incomplete markup, a shortcut you wouldn't use in production, a partial implementation), say so next to it and say what real code should do.
8. Give every concept guide a short note at the top naming its reference pages, and give every reference page a note at the top naming the guide to read first.
9. Use one example domain throughout a feature's guide and its reference pages. Where later pages can build on the beginner tutorial's project, reuse it so readers don't have to learn a new domain.
10. Give readers an explicit map of the documentation: which kinds of page exist, what each is for, and where to start. Tell beginners how much ground the introductory material covers.
11. When a step depends on another project's software, document only how it connects to yours and link to that project's own instructions for the rest. Their steps will change on their schedule, not yours.
12. Keep FAQ answers to a sentence or two, then link to the page that holds the full answer, so the FAQ doesn't become a second copy that drifts.
13. Open a concept guide with the underlying technology or idea the reader already knows, then show what your tool adds on top of it.
14. Give every aside box a descriptive title that says what's inside ("Different error?", "Projects vs. apps"), so readers can choose to skip it. Keep such boxes few.

**Corrections**

15. Rationale doesn't always belong on a separate page. When a design choice will puzzle readers at a specific point (in a tutorial, a how-to, or a reference entry), give a few sentences of why right there, in a titled box or a single clearly marked paragraph that can be skipped. Move anything longer to an explanation page.
16. Numbered one-action steps suit procedures and how-tos. Narrative tutorials can instead give each action as its own short paragraph, followed by the code for it and then what it means. Choose by page type, not one rule for every page.
17. Write version-change notes as self-contained blocks: "added in" at the top of the entry, "changed in" at the end of the section. They must be removable without editing the surrounding text. Remove them after a fixed number of releases, and don't mention version numbers in body text at all.
