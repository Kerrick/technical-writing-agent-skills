Source: Rails guides, Digging Deeper through Contributing, commit f12b615

> Quotes and descriptions in this file are from the [Ruby on Rails Guides](https://guides.rubyonrails.org/) ([rails/rails](https://github.com/rails/rails)), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). "Rails" and "Ruby on Rails" are trademarks of David Heinemeier Hansson. Quotes are short, and used to compare and criticize. Because it quotes and describes that material, this file is licensed under the same license.

Baseline skill: `developer-docs/` (unchanged). Skill citations are `SKILL.md:N`, `references/teaching.md:N`, `references/reference-and-guides.md:N`, `references/books-and-video.md:N`. Guide citations are `file:line` in `guides/source/`. The two style guides (`api_documentation_guidelines.md`, `ruby_on_rails_guides_guidelines.md`) are treated as stated intent and cited as such.

## 1. Missed principles

**M1. A small fixed set of callout types, each defined by what the reader risks by skipping it.**
- Evidence: callout prefixes appear on every page and in volume (security.md 42, testing.md 26, configuring.md 18, engines.md 18, debugging 15). `ruby_on_rails_guides_guidelines.md` ("Notes, Tips and Warnings") defines three levels: context that aids understanding, optional extra, thing that breaks or compromises the app.
- Skill: absent. Nearest is `SKILL.md:44` (warn before the hazard), which covers one level only.

**M2. Every page opens with a short list of what the reader will know or be able to do afterward.**
- Evidence: all 26 pages have it. 24 begin "After reading this guide, you will know" (grep, 24 files); `api_app.md` and `generators.md` use "In this guide you will learn". This includes reference-style pages (configuring.md:8), not only tutorials.
- Skill: partial overlap. `SKILL.md:35` says the first paragraph states purpose and audience; `references/teaching.md:7` asks for an observable outcome, tutorials only. An outcome checklist for every page type is absent.

**M3. Change history indexed two ways: per option and per version.**
- Evidence: configuring.md has a "Starting with version / default value" table under individual options (93 matches) and, separately, 11 "Default Values for Target Version X" roll-ups at the top (configuring.md:61-190). A reader upgrading reads one; a reader checking one setting reads the other.
- Skill: `references/reference-and-guides.md:16` covers per-entry version info only. The per-version rollup is absent.

**M4. When several mechanisms solve the same problem, give a chooser keyed to the reader's situation.**
- Evidence (pattern, 5 places): active_record_multiple_databases.md:38 (table "If you need to... / Use..."); working_with_javascript_in_rails.md:322 ("Choosing Between an Import Map and a JavaScript Bundler"); asset_pipeline.md ("When Should You Use / Bundle ..." sections, three of them); testing.md:1439 ("When to Use System Tests"); plugins.md:102 ("guidance on choosing the right option").
- Skill: absent. `references/reference-and-guides.md:48` handles forks inside one task, not choosing between approaches.

**M5. Declare boundaries early: what the page leaves out, what environment it assumes, and what the documented thing does not do.**
- Evidence: tuning_performance_for_deployment.md:22 (assumes one runtime; "most of this guide doesn't apply" otherwise), :35 and :207 (explicit "beyond the scope"); security.md:1739; working_with_javascript_in_rails.md:256; using_hotwire_with_rails.md:54; active_record_multiple_databases.md:88 plus a "Caveats and Operational Considerations" section stating what the feature does not provide and who owns it.
- Skill: `references/reference-and-guides.md:59` has "Name the scope", for explanation pages only. Non-guarantees and environment assumptions are absent.

**M6. Next to each documented default, tell the reader how to read the live value.**
- Evidence: configuring.md:2569, :2614, :2627, :2640 ("Use ... to observe the configuration. By default, it is defined as:"); api_app.md:452-455 and :490 (commands that list what is included/excluded); generators.md:339 (command to print the load path).
- Skill: `SKILL.md:50` pushes generation from source and says to write only what generation can't; it never asks for a way to inspect the running system. Absent.

**M7. When showing wrong code, label it as wrong inside the code block.**
- Evidence: autoloading_and_reloading_constants.md:26 and :29 (marker comments bracketing the bad snippet); active_record_encryption.md:297/303 (CORRECT / INCORRECT in the block); debugging_rails_applications.md:260/263 (DO / DON'T).
- Skill: `references/teaching.md:43` (make the pasted version the correct one) implies keeping wrong code out of blocks; `references/books-and-video.md:45` says show naive approaches first but not how to mark them.

**M8. Show what a high-level call turns into underneath.**
- Evidence: active_record_composite_primary_keys.md:167, :190, :204, :239, :286 (each call followed by the low-level statement it produces); active_record_multiple_databases.md ("disable_joins" section shows the two statements produced).
- Skill: absent. `references/reference-and-guides.md:15` asks for request/response examples only.

**M9. Document silent failures with the same prominence as errors.**
- Evidence: api_app.md:304 (renders nothing, no error); caching_with_rails.md:1006 (failures return an empty result, never raise); configuring.md:1520 and :3180 (change silently not applied / job silently ignored); i18n.md:1566-1568 (certain keys quietly yield "missing").
- Skill: `references/reference-and-guides.md:13` documents errors that are raised; the case of no error is absent.

**M10. A curated excerpt is labeled as an excerpt and points to the complete list.**
- Evidence: testing.md:373 ("an extract of the assertions"), :412 ("a subset ... For an exhaustive ... list"), :1722; api_app.md:436 ("Some of the included modules") followed by a way to print the full list at :452.
- Skill: `references/reference-and-guides.md:5` asks reference pages to be exhaustive; it says nothing about how a non-reference page may excerpt.

**M11. When a feature is removed, leave a one-line pointer to the archived, versioned docs instead of keeping or deleting the old text.**
- Evidence: asset_pipeline.md:80-83 (previous system, link to a versioned page and a migration note); working_with_javascript_in_rails.md:417-421 (removed library, link to an old version).
- Skill: `references/reference-and-guides.md:39` covers deprecation notices only. The after-removal breadcrumb is absent.

**M12. Illustrative snippets double as style guidance: use the currently recommended idiom, and reorder to put the favored approach first.**
- Evidence: api_documentation_guidelines.md:82 (stated intent: documentation as a model of current practice). Pattern: the same newer parameter-handling call appears in api_app.md (2), engines.md (2), using_hotwire_with_rails.md (1) rather than older forms.
- Skill: `SKILL.md:46`-area ("every example should be one a user could actually need") covers relevance, not currency of idiom. Absent.

**M13. Document the behavior a user gets in the full default setup, not the component in isolation.**
- Evidence: api_documentation_guidelines.md:487 ("document the behavior of the _framework_, not just isolated methods"); caching_with_rails.md section "Caching in Background Jobs and Other Non-Request Contexts" (behavior depends on the surrounding execution context and says how to supply it).
- Skill: absent.

**M14. Every docs change gets a rendered preview for reviewers.**
- Evidence: contributing_to_ruby_on_rails.md:144 ("a preview of the documentation will be deployed for easy review").
- Skill: `references/reference-and-guides.md:88` lists lint, build, link check; a preview is absent. (Single-source; low weight.)

## 2. Corrections

**C1. "No opinions; put recommendations in guides" is too absolute for reference entries.**
- Skill: `references/reference-and-guides.md:24`.
- Evidence: configuring.md (a reference-style page) puts the recommendation beside the option when the choice is risky or non-obvious: :978 ("recommended not to disable ... security measure"), :1914 ("highly recommended that you do not enable this in a production environment"), :277 ("not recommended to adjust this").
- Better statement: neutral by default; a one-sentence recommendation with its reason is right when the wrong choice is costly.

**C2. "Be specific: values, defaults, return values" is too absolute when the value is not part of the promise.**
- Skill: `SKILL.md:40`.
- Evidence: api_documentation_guidelines.md:281 (don't document exact singleton values unless necessary; it avoids contrived code and allows refactors) and :456 (internal-but-public methods are hidden so people don't rely on them).
- Better statement: be exact about the contract; stay deliberately silent or semantic about incidental behavior you don't want to freeze.

**C3. "No prompts in copyable blocks; output in a separate block" confuses the goal with one tactic.**
- Skill: `SKILL.md:43`, `references/teaching.md:43`.
- Evidence: command_line.md (136 prompt-prefixed lines in its code blocks, output directly beneath each command) and ruby_on_rails_guides_guidelines.md:121 ("Prompts are ignored by the copy button"). The transcript form keeps context readable; tooling protects the copy.
- Better statement: what gets copied must be runnable. Separate blocks are the safe default where the site cannot strip prompts.

**C4. "Don't explain what the reader's level already covers" is too absolute for mixed audiences.**
- Skill: `SKILL.md:55`.
- Evidence: one- or two-sentence glosses of general terms in otherwise advanced pages: caching_with_rails.md:116 (hit/miss, set off as an info callout), testing.md:1043, asset_pipeline.md:772, debugging_rails_applications.md:138.
- Better statement: gloss briefly, set apart so experts skip it, rather than omit.

## 3. House conventions (not principles)

- Callout prefix syntax, fence labels and line-highlight syntax (`ruby_on_rails_guides_guidelines.md:153`); a console prompt style and filename comments in examples. Tooling-specific.
- API comment prose avoids "you" (`api_documentation_guidelines.md:148`) while the guides themselves use "you" freely. A per-medium convention.
- RDoc markup for code font, result arrows `# =>`, and the hide-from-docs directive (`api_documentation_guidelines.md:340-461`).
- American spelling, serial comma, title-case headings, 80-column wrap for new text (`api_documentation_guidelines.md:170-176`, `ruby_on_rails_guides_guidelines.md:50, :302`).
- A banner on each source file telling readers not to read it on the code host; translations live in forks (`contributing_to_ruby_on_rails.md:154-164`).

## 4. Where the Rails guides fall short of the skill

**F1. Pages contradict each other or carry stale statements.** Skill: `SKILL.md:50`, `:70`.
- tuning_performance_for_deployment.md:136 says the compiler is on by default "as for 7.2"; configuring.md:658 shows the default changed in 8.1.
- engines.md:1659 and :1708 still describe the old asset system; asset_pipeline.md:80 says it was replaced.
- security.md:1614 refers to a helper that working_with_javascript_in_rails.md:417 says is gone; security.md:1693 ("In 2007"), :1086, :269 keep dated or old-version phrasing.

**F2. A broken internal link.** Skill: `SKILL.md:68`. working_with_javascript_in_rails.md:361 links `using_hotwire_in_rails.html`; the page is `using_hotwire_with_rails.md`.

**F3. Code samples that don't run or don't match their text.** Skill: `SKILL.md:64`, `:66`.
- debugging_rails_applications.md:812 (unclosed output tag) and :330 (output tag on a loop).
- asset_pipeline.md:427 (missing comma in a JSON object).
- plugins.md:475 and :665-674 call a method the page never defines; the page defines a differently named one at :513.

**F4. Filler words the skill bans.** Skill: `SKILL.md:41`. Raw counts of "simply"/"just": security.md 12, engines.md 9, configuring.md 5, plugins.md 5 (some are legitimate "only"; e.g. "Simply pass a file name..." in security.md File Downloads is filler).

**F5. Multi-step builds narrated as prose, not numbered.** Skill: `SKILL.md:36`. engines.md, plugins.md, generators.md contain zero numbered items (grep) while walking long procedures; testing.md has 5. Moderate weight: the prose gives a reason at each step, but resuming mid-way is harder.

## Skill claims the guides confirm (only where unusual)

- `references/teaching.md:31`/`:18` (trigger an error on purpose; show the failure where it occurs): testing.md "Your First Failing Test"; engines.md:806 and :903 show exact error text at the point of failure, then the fix.
- `SKILL.md:58` (one-sentence why beats a rule): autoloading_and_reloading_constants.md:117 and :295 ("Why?" followed by consequence).
- `SKILL.md:39` (state prerequisites, link instead of re-teaching): using_hotwire_with_rails.md:57-59.
- `references/reference-and-guides.md:39` (deprecation names its replacement): configuring.md:1631-1645 deprecations point to the replacement setting.

## Observed, not counted

Several pages combine explanation, how-to and reference. Skill rule they differ from: `SKILL.md:13` (one mode per page) and `SKILL.md:31` (link between modes instead of merging).
- testing.md: a first-test walkthrough (:94), a reference table of assertions (:367), configuration how-to (:2860).
- configuring.md: option reference plus explanation of load hooks and initialization events (sections "Load Hooks", "Initialization Events").
- caching_with_rails.md: concept explanation ("What is Caching?"), procedures, then a per-store reference.
- security.md: attack stories (explanation) alongside countermeasures (how-to).
Where they keep modes apart: setup of the contributor environment is a separate page (contributing_to_ruby_on_rails.md:227 links development_dependencies_install.md); the exhaustive assertion list is delegated outward (testing.md:412); the writing rules for narrative docs and for reference comments are two pages; contributing_to_ruby_on_rails.md:135 names the guides/reference split explicitly.
Verdict: I would not count this as a correction. Each mode sits under its own heading, announced by it and cross-linked, so the failure the skill's rule targets (stray steps or stories in the middle of a lookup) doesn't occur; the rule is better read at section level than page level.

## Abstracted

Missed principles
1. Define a small, fixed set of callout types by what skipping each one costs the reader (understanding, optional depth, breakage), and use them consistently so readers learn to trust the signal.
2. Start every page, whatever its kind, with a brief list of what the reader will know or be able to do afterward, so they can decide in seconds whether to read on.
3. When defaults or behavior change across releases, record the history twice: beside each setting, and as a per-release roll-up, so both "what changed for this setting" and "what changed in this upgrade" are one lookup.
4. Where several approaches solve the same problem, add a decision aid keyed to the reader's circumstances (their need maps to a recommended option), and name the default.
5. State boundaries up front: what the page does not cover, which environment it assumes, and what the documented tool does not do or guarantee, naming who owns the remainder.
6. For every documented default or built-in list, tell the reader how to inspect the live value in their own system, so the page is checkable and doesn't have to be trusted.
7. When showing an incorrect approach, mark it as incorrect inside the code block itself, so a copied snippet still carries the warning.
8. When a convenient call hides what actually happens, show the lower-level result it produces, next to the call.
9. Treat failures that produce no error (silent no-ops, dropped work, quiet fallbacks) as first-class documentation, at least as visible as the failures that raise.
10. If a table or list is a selection, say it is a selection and point to the complete source; don't let a partial list read as complete.
11. When you remove documentation for a retired feature, leave a short pointer to the archived, version-specific documentation and any migration note.
12. Write illustrative snippets in the currently recommended style, and order alternatives so the favored one comes first; examples teach habits.
13. Describe behavior as the user experiences it in a typical full setup, and say when behavior changes because of the surrounding context, rather than describing a component alone.
14. Give reviewers a rendered preview of every documentation change, not just the diff.

Corrections
1. Keep reference neutral by default, but when a wrong choice is costly or non-obvious, put a one-sentence recommendation and its reason right next to the item.
2. Be exact about the contract and deliberately vague about incidental behavior you don't intend to keep stable; over-specifying values invites readers to depend on them.
3. The real requirement for command examples is that what gets copied is runnable. Separate blocks are the safe default; showing prompts and output together is acceptable when the publishing tool strips them on copy.
4. For mixed audiences, don't omit definitions of general terms; give a one- or two-sentence gloss, visually set apart so experienced readers can skip it.
