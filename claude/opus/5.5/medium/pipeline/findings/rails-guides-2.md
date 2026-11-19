Source: Rails guides, Digging Deeper through Contributing, commit f12b615

> Quotes and descriptions in this file are from the [Ruby on Rails Guides](https://guides.rubyonrails.org/) ([rails/rails](https://github.com/rails/rails)), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). "Rails" and "Ruby on Rails" are trademarks of David Heinemeier Hansson. Quotes are short, and used to compare and criticize. Because it quotes and describes that material, this file is licensed under the same license.

# Rails guides vs. the technical-writing skill

This compares the 26 guides in Digging Deeper, Going to Production, Advanced Active Record, Extending Rails, and Contributing against the `technical-writing` skill as it was first written. Guide paths are relative to `guides/source/`. Skill paths are relative to the skill folder. Quotes are kept short. Most evidence describes a pattern instead of quoting it.

## 1. Missed principles

**M1. Say what the tool does not do.** Several guides list what falls outside the feature or outside the guide's scope, so readers know which jobs are still theirs.
- `active_record_multiple_databases.md:88`: a NOTE lists what the framework won't provision or manage: servers, users, replication, load balancing, distributed transactions.
- `autoloading_and_reloading_constants.md:50`: lists what the loaders don't manage.
- `asset_pipeline.md:61`: the pipeline core "**DOES NOT** do any transpiling or bundling."
- `tuning_performance_for_deployment.md:15`: names the components the guide won't cover.
- Skill: absent.

**M2. Walk through generated files before changing them.** When a command generates code the reader didn't write, the guides show the generated file or tree and explain each part before asking for any edit.
- `testing.md:121`: a line-by-line walk through the generated test stub.
- `plugins.md:134`: the generated tree, then what each directory is for.
- `engines.md:146-215`: the directory structure, then a section per generated file.
- Skill: absent. `tutorials.md` covers steps the reader types, not output the reader receives.

**M3. Mark which lines of real output a setting adds.** When the guides document a logging option, they show actual log output and highlight the lines that option is responsible for.
- `debugging_rails_applications.md:360`, `:413`, `:440` (three options, same pattern).
- Skill: absent. `SKILL.md:89` uses highlighting only for code changes, and `SKILL.md:62` says only to paste real output.

**M4. When defaults depend on a compatibility level, document the history two ways.** The configuration reference gives each option's default as a table of "starting with version → value." It also gives a per-version index listing every default that changed in that version, so an upgrader can see the whole delta at once.
- `configuring.md:61-191`: the per-version index.
- `configuring.md:208`, `:510`, `:654`: the per-option tables, among many others.
- Skill: `references/api-reference.md:103` covers versioning one entry at a time ("Since 2.3.0"). It has no per-release index of changed defaults and doesn't consider defaults that depend on a compatibility setting.

**M5. Document the contract, not the incidental value.** The API guidelines say to describe what a predicate means (true or false in the language's sense) rather than the exact object it returns, so the docs don't promise more than the code guarantees.
- `api_documentation_guidelines.md:274`, `:281`: "do not document singletons unless absolutely necessary."
- Skill: absent. `references/api-reference.md:80-87` asks for exact defaults and types, with no counterweight about over-promising.

**M6. Mark what is not public API.** Methods that must be technically reachable but aren't supported are explicitly excluded from the reference, and that exclusion is tied to the project's deprecation promise.
- `api_documentation_guidelines.md:435-467`.
- Skill: absent.

**M7. Document behavior as users experience it in the default full setup.** The guidelines tell writers to describe what a method returns once the whole default stack is in play, not what the unit does in isolation.
- `api_documentation_guidelines.md:483`, `:487`.
- Skill: absent.

**M8. Examples model the current way; superseded approaches get a one-line pointer to old docs.** The guidelines require examples to use the currently recommended idioms and allow reordering sections to favor them. The guides then point to archived versioned docs for old approaches instead of documenting them inline.
- `api_documentation_guidelines.md:82`: the instruction.
- `asset_pipeline.md:80-84` and `working_with_javascript_in_rails.md:417-421`: the pattern.
- Skill: `SKILL.md:102` says to give a default path, but nothing says examples are copied and must model current practice, or how to handle superseded approaches.

**M9. Document boundary inputs.** The guidelines say to cover what happens with empty, nil, or anonymous inputs.
- `api_documentation_guidelines.md:94`.
- Skill: absent. `references/api-reference.md:82-87` lists default, units, range, and interactions, but not edge-case behavior.

**M10. Keep links inside the version the reader is in.** Reference links are written so they resolve within the docs version being read. Guide links to the reference are rewritten per release, and hand-linking to the bleeding-edge reference is forbidden.
- `api_documentation_guidelines.md:33`.
- `ruby_on_rails_guides_guidelines.md:257-300`.
- Skill: absent. `references/style.md:14-18` covers link text only.

**M11. In learning docs, show a curated subset of a large API, say it's a subset, and point to the complete list.**
- `testing.md:373`, `:412`, `:1722`: "an extract", "a subset … For an exhaustive … list."
- `debugging_rails_applications.md:477`: "a brief overview … Consult …"
- `api_app.md:436`: "Some of the included modules."
- Skill: absent. `SKILL.md:81` says only to link instead of repeating.

**M12. Teach readers to ask the system for the authoritative answer.** The guides repeatedly give the command that prints the current, complete list (help output, the middleware stack, a module list), instead of relying only on a static list that can drift.
- `generators.md:113`.
- `rails_on_rack.md:170`.
- `api_app.md:452`.
- `command_line.md:75-115`.
- Skill: absent. The skill tells the writer to read `--help` (`SKILL.md:52`), not to teach the reader to.

**M13. Pair the tempting wrong version with the right one.** Where readers' instinct produces bad code, the guides show the bad code labeled as such, then the fix.
- `i18n.md:283`, `:310`.
- `caching_with_rails.md:195`.
- `debugging_rails_applications.md:260-264`.
- `autoloading_and_reloading_constants.md:26`.
- Skill: absent from the code rules (`SKILL.md:84-94`). `references/explanation.md:14` covers wrong mental models, not wrong code.

**M14. When the right value depends on the reader's environment, say so and teach how to find it.** The tuning guide states the trade-off axes (throughput and latency), explains why no single default fits everyone, and gives a measurement method. The multiple-databases guide does the same for its delay setting.
- `tuning_performance_for_deployment.md:44-53`, `:164`.
- `active_record_multiple_databases.md:658-660`.
- Skill: absent. `SKILL.md:102` pushes toward a single default path.

**M15. State each option's cost, whether it suits production, and how much the advice matters.**
- `debugging_rails_applications.md:364-366`, `:423-425`, `:447-449`: the memory cost in production, repeated for each option.
- `debugging_rails_applications.md:273`: "These are micro-optimizations."
- `active_record_composite_primary_keys.md:40-42`: a complexity and speed cost.
- `active_record_multiple_databases.md:1082`: a list of trade-offs.
- Skill: absent.

## 2. Corrections

**C1. "Teach one error on purpose … More than once is a detour" is too absolute.** When the subject is a fail-then-fix loop, repeating the error is the lesson. Testing does this several times. When each error motivates the next step, errors can drive a whole tutorial; the engines guide uses two such errors in sequence.
- `testing.md:194`, `:293-332`, `:1137`.
- `engines.md:806`, `:903`.
- Skill: `references/tutorials.md:53`.

**C2. "Keep commands and their output in separate blocks" depends on tooling.** When the copy button strips prompts and annotations, one block with a prompted command and its output reads better and copies cleanly. The guides do this throughout.
- `ruby_on_rails_guides_guidelines.md:97`, `:121`: the copy button ignores filename comments and prompts.
- `testing.md:214-235`: a typical combined block.
- Skill: `SKILL.md:92`.

**C3. "Reserve warnings for data loss, security, and money" is too narrow.** The style guide defines a warning as anything to avoid that would break the application. The guides use warnings for silent misbehavior: files that are skipped, files that overwrite each other, and settings unsafe for production memory. These earn a warning without fitting the skill's three categories.
- `ruby_on_rails_guides_guidelines.md:223`.
- `asset_pipeline.md:100`, `:104`, `:725`.
- `debugging_rails_applications.md:364`.
- Skill: `SKILL.md:79`.

**C4. "Use second person" is too absolute for reference text.** The API guidelines ask writers to avoid addressing the reader in reference comments. Those comments describe the thing, while task guides address the reader.
- `api_documentation_guidelines.md:148`.
- Skill: `SKILL.md:70`, which applies the rule to every draft. `references/api-reference.md:89` is consistent with the guidelines but never reconciles the two.

**C5. "Be austere" is too absolute for consequential settings.** Reference entries for options with non-obvious costs explain why the option exists, what it can't catch, and how it interacts with performance. Leaving that out would make the entry dangerous rather than lean.
- `configuring.md:1555`: the history behind a serializer default.
- `configuring.md:1590`: a query-plan cost.
- `configuring.md:2102-2114`: "best effort," with the limits listed.
- Skill: `references/api-reference.md:3`. `references/api-reference.md:86` allows interactions but not rationale or limits.

**C6. "Cover cross-cutting topics once" fails for security consequences.** There is a central security guide, but each feature guide also states the security implications at the point of use. A reader configuring that feature wouldn't otherwise see them.
- `using_hotwire_with_rails.md:394-410`, `:553`.
- `generators.md:646`.
- `debugging_rails_applications.md:862-863`.
- `active_record_encryption.md:628-634`.
- Skill: `references/api-reference.md:91-93`.

**C7. "Open with the answer, not 'In this guide …'" is too absolute.** Every guide in scope opens with the same block: a sentence of scope, then a list of what the reader will learn. The style guide requires it. A uniform, scannable scope-and-outcomes block works as a contract for long guides. The skill's objection to boilerplate applies to vague openers, not to this.
- `ruby_on_rails_guides_guidelines.md:27-32`.
- "After reading this guide" appears in 31 source files, including all 26 here.
- Skill: `SKILL.md:74`.

## 3. House conventions

- **Code-comment notation:** RDoc markup (`+x+` vs `<tt>`), results written as aligned `# =>`, and SQL output without the arrow. See `api_documentation_guidelines.md:206-269` and `:327-361`. This is specific to Ruby and RDoc.
- **Title-case headings:** `ruby_on_rails_guides_guidelines.md:50-57`. The skill's sentence case (`SKILL.md:75`) is just as valid. Neither is a principle.
- **Callout prefixes:** `NOTE:`, `TIP:`, and `WARNING:` paragraphs. See `ruby_on_rails_guides_guidelines.md:182-230`.
- **Language rules:** American spelling, the Oxford comma, "an SQL," and component names spelled as products ("Active Record") rather than modules. See `api_documentation_guidelines.md:96-178`.
- **Generated test app:** a dummy host application for testing plugins and engines. See `plugins.md:166`, `engines.md:442-454`.

## 4. Where the Rails guides fall short

**F1. Outcome lists use "know," not observable actions.** Examples: "Rails testing terminology." (`testing.md:10`), "What caching is." (`caching_with_rails.md:11`), "What is an engine." (`engines.md:12`). The skill's rule is stronger: `SKILL.md:48`.

**F2. Words the skill bans appear.** "makes it easy" (`testing.md:26`), "a powerful part" (`command_line.md:20`), "even more powerful" (`caching_with_rails.md:778-779`), "Simply pass" (`security.md:723`). Skill: `SKILL.md:73`, `SKILL.md:80`.

**F3. Passive voice and mixed person inside walkthroughs.** Examples: "it is asserted" (`testing.md:197`), "an assertion should be added" (`testing.md:1124`). The same guide shifts between "we" (`testing.md:487`) and "you." Skill: `SKILL.md:70`.

**F4. Reference entries are inconsistent.** Some option entries give no default, for example `configuring.md:716` and `:1090`. Opening verbs vary between "Lets you," "Is a flag," and "Accepts." One deprecation note names the removal version but no replacement (`configuring.md:1528`). Skill: `references/api-reference.md:3`, `:85`, `:104`.

**F5. Version drift and dated material.**
- The tuning guide describes YJIT's default as of an older release (`tuning_performance_for_deployment.md:136`), while the configuration reference shows that default changed later (`configuring.md:658`).
- The security guide cites decade-old browser versions, statistics, and framework versions (`security.md:27`, `:269`, `:1053`, `:1323`).
- Skill: `SKILL.md:52` (record the version you documented), `references/books.md:73`.

**F6. Examples that couldn't have been run.**
- The plugin guide tests a method the guide never defines, and a model it never generates (`plugins.md:475`, `:665-674`, `:690`).
- An import-map example is invalid JSON because of a missing comma (`asset_pipeline.md:427`).
- An ERB example has an unclosed tag (`debugging_rails_applications.md:812`).
- A system-test walkthrough gives the wrong request path (`testing.md:1683`).
- A cross-guide link points to a file that doesn't exist (`working_with_javascript_in_rails.md:361`).
- Skill: `SKILL.md:60-62`.

**F7. Modes mix on one page.** The testing walkthrough embeds full assertion reference tables and a pasted help dump (`testing.md:378-410`, `:549-589`). The configuration reference contains reverse-proxy setup and robots.txt advice that aren't configuration (`configuring.md:4433`, `:4921`). Skill: `SKILL.md:44`.

**F8. Definitions come before any example.** Some guides open with an abstract definition and no concrete case: `caching_with_rails.md:18-32` and `engines.md:21-45`. Skill: `SKILL.md:77`.

**F9. Placeholder styles vary.** `YOUR_GITHUB_HANDLE` (`plugins.md:741`), `<your username>` (`contributing_to_ruby_on_rails.md:820`), `<timestamp>` (`engines.md:480`). Skill: `references/style.md:9`.

## Confirmations

- Document error messages by their literal text (`SKILL.md:103`): `active_record_multiple_databases.md:743`, `configuring.md:4835`.
- Teach names and roles before the process (`references/learning-science.md:9`): `active_record_multiple_databases.md:21` puts a terminology table before any setup.
- Refute the wrong mental model directly (`references/explanation.md:14`): `autoloading_and_reloading_constants.md:263` states the misconception about reloading, then shows the case where it fails.

## Observed, not counted

Many of these guides are organized around a topic rather than around a mode. Explanation, how-to, and reference share one page. Where this is done deliberately, the parts follow a consistent order: explanation, then how-to, then reference. Each part gets its own top-level section heading, so the switch from one mode to the next happens at a heading and not partway through a section.

- `rails_on_rack.md`: explains what Rack is and how middleware works (`:16`), then shows how to change the stack (`:212`), then ends with a reference entry for each built-in middleware (`:291`).
- `caching_with_rails.md`: explains what caching is (`:18`), then covers setup and each caching technique, then gives a uniform subsection for each cache store (`:818`).
- `active_record_multiple_databases.md`: opens with a terminology table, a table matching needs to setups (`:34`), and the limitations, all before the first setup step (`:77`).
- `configuring.md`: inverts the order. The reference comes first, with option entries from `:193`. Explanation and how-to sections follow at the end of the page: how connection settings combine (`:4096`), and load hooks with a table of available hooks (`:4510`, `:4592`).
- `security.md`: alternates within each topic. Each attack is explained, then followed by its own countermeasures subsection (`:464`, `:970`, `:1164`, `:1194`).
- When reference material appears inside a teaching section, it's presented as a table that is labeled as a subset and links to the complete reference. See `testing.md:367-415` and the evidence for M11.

This differs from `SKILL.md:44`, which says to split a page that tries to do two jobs and link the halves. I don't count it as a correction. The guides show that topic pages combining the modes, in a fixed order with each mode under its own heading, are common and readable, but they don't show those pages serving readers better than split pages would. The places where the separation lapses (F7: a pasted help dump inside a walkthrough, and unrelated how-to sections inside the configuration reference) show the costs that the skill's rule is meant to prevent.

## Abstracted

1. State plainly what the tool or feature does not do, and what falls outside the page's scope, so readers know which responsibilities stay with them.
2. When a command generates files the reader didn't write, show what was generated and explain each relevant part before asking them to change anything.
3. When documenting an option that changes output, show real output and mark exactly which parts the option adds or changes.
4. When a default depends on a version or compatibility setting, give each option's default as a version-by-value table. Also publish, for each version, a single list of every default that changed in it.
5. Document only the behavior you are willing to guarantee. Describe meanings (for example, "returns a true value when …") rather than exact incidental values the implementation could change.
6. Explicitly mark interfaces that are reachable but not supported, so readers don't build on them, and keep them out of the public reference.
7. Describe behavior as users see it in the standard, fully configured setup, not as the isolated unit behaves on its own.
8. Make every example use the currently recommended approach, because readers copy examples. Move superseded approaches out of the main text and leave a one-line pointer to the documentation for the version that used them.
9. For every reference entry, state what happens on boundary inputs: empty, missing, null, zero, and unnamed values.
10. Write links so they keep the reader inside the documentation version they are reading. Never hard-link to docs for a different or unreleased version.
11. In teaching material, show a selected subset of a large API, say explicitly that it is a subset, and link to the complete, authoritative list.
12. Teach readers the command or query that prints the current, complete answer (help output, live lists, introspection), so they don't depend on a static copy that can go stale.
13. Where readers' first instinct produces wrong code, show the wrong version labeled as wrong, then the right version, and say why.
14. When the correct value depends on the reader's environment, say so. Name the trade-off it controls, give a starting value, and give a method for measuring and adjusting it.
15. For each option, state its cost (memory, speed, complexity), whether it is safe for production, and how much the recommendation actually matters.
16. Let readers hit an error on purpose as often as the subject demands. When the workflow being taught is fail-then-fix, or each error motivates the next step, repetition is the lesson, not a detour.
17. Whether to keep commands, prompts, and output in one block depends on your platform. If the copy control strips prompts and output, a single block that shows command and result together is clearer. Otherwise, separate them.
18. Use a warning for anything that silently breaks or misleads, including skipped files, overwritten files, and settings unsafe in production, not only for data loss, security, or money. Give each callout type one defined meaning and stick to it.
19. Address the reader directly in tutorials and how-to steps. In reference descriptions, describe the thing itself without addressing the reader.
20. Keep reference entries lean, but for options whose misuse is costly, include why the option exists, its known limits, and its interactions. Leaving these out is not austerity, it's a hazard.
21. Keep a central page for cross-cutting concerns such as security, but also state each feature's own security consequences where that feature is documented. Readers configure features one page at a time.
22. A uniform opening block on every long page, with one sentence of scope followed by a short list of what the reader will be able to do, is a useful contract, not empty boilerplate. Avoid vague openers, not structured ones.
