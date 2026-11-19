Source: Rails guides, Start Here through Other Components, commit f12b615

> Quotes and descriptions in this file are from the [Ruby on Rails Guides](https://guides.rubyonrails.org/) ([rails/rails](https://github.com/rails/rails)), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). "Rails" and "Ruby on Rails" are trademarks of David Heinemeier Hansson. Quotes are short, and used to compare and criticize. Because it quotes and describes that material, this file is licensed under the same license.

# Rails guides vs. the technical-writing skill (baseline)

This compares the skill as first written against two things: 23 Rails guides (Start Here, Models, Routing and Controllers, Views, Other Components) and the two Rails style documents (the "Guidelines" section of `ruby_on_rails_guides_guidelines.md`, and `api_documentation_guidelines.md`).

Guide paths are relative to `~/Developer/rails/guides/source/`. Skill paths are relative to `~/.agents/skills/technical-writing/`. Quotes are kept short and used only where the exact wording matters.

## 1. Missed principles

### 1.1 Show what the abstraction produces next to each call

The Querying and Basics guides follow almost every high-level call with the SQL it runs: about 32 times in `active_record_querying.md` and 6 times in `active_record_basics.md`. The view-helper and form guides do the same with the HTML each helper emits (`form_helpers.md:64`, `form_helpers.md:157`, `action_view_helpers.md:262`, `action_view_helpers.md:598`). The reader sees what the abstraction does as well as how to call it. This also answers the reader's next question, "is this efficient?", without a separate explanation page.

Skill: `SKILL.md:88` says to show "the output or the visible result". It doesn't mention showing the lower-level artifact a call generates. Otherwise absent.

### 1.2 Show a feature's value by contrast with doing it by hand

`association_basics.md:41` and `:90` pair "Without Associations" and "Using Associations" sections, with the manual code first. `active_record_querying.md:715` and `:800` introduce `pluck` and `pick` by showing the longer code they replace. `getting_started.md:842` writes out every CRUD route by hand, then replaces them all with `resources`. The pattern is to show the tedious version first, so the shortcut means something.

Skill: closest is `SKILL.md:77` ("Show, then tell") and `references/learning-science.md:65` ("open with the problem the reader has"). Neither says to show the manual alternative as code. Absent.

### 1.3 Document the behavior the user gets in the default full configuration

`api_documentation_guidelines.md:476-489` gives an example: a helper returns one path in isolation and a different one once the asset pipeline is in place. The rule is to document "the behavior that the user experiences when using the full default Rails stack."

Skill: `SKILL.md:52` sends the writer to source code, schemas, and `--help` for ground truth. That implies reading a unit's code is enough, and it doesn't warn that the integrated default setup can change what a reader observes.

### 1.4 Document the promise, not the implementation

`api_documentation_guidelines.md:274-316` says to document predicates and flags by their truth semantics, not by the exact object returned, so the implementation stays free to change. `api_documentation_guidelines.md:438-467` keeps public-but-internal methods out of user docs ("users should not rely on it"), because anything documented becomes a compatibility promise.

Skill: `references/api-reference.md:82-87` lists what each description should contain, but never separates contract from incidental behavior or says to leave out what isn't promised. Absent.

### 1.5 Explore and document edge cases

`api_documentation_guidelines.md:94`: "Explore and document edge cases", with nil arguments, empty collections, and anonymous modules as examples. The guides follow this:
- `action_view_overview.md:521`: rendering an empty collection returns nil.
- `active_support_core_extensions.md:109`: a WARNING that 0 and 0.0 are not blank.
- `active_record_querying.md:1598`: a NOT condition silently drops rows whose nullable column is null.

Skill: `references/api-reference.md:82-87` covers defaults, ranges, and interactions, but not empty, nil, or degenerate inputs. Absent.

### 1.6 For any safeguard, list exactly which operations bypass it

`active_record_validations.md:158` lists every method that skips validations. `active_record_callbacks.md:609` and `:745` list which methods trigger callbacks and which skip them. `active_record_basics.md` bolds "without callbacks or validations" each time it shows a bulk method. Readers learn where the guarantee ends, which is where the bugs are.

Skill: absent.

### 1.7 Keep legacy forms documented, placed last and labeled as older

Readers meet old idioms in existing code, so the guides keep them but mark them as superseded:
- `form_helpers.md:1341`: a closing section on the older form helpers, "now discouraged", which readers may still find in some codebases.
- `active_record_validations.md:367`: shows the older validation-helper notation after the modern form.
- `action_controller_overview.md:969`: names the recommended parameter API after explaining the older pair.

`api_documentation_guidelines.md:82` adds the ordering rule: reorder sections to emphasize the favored approach.

Skill: `SKILL.md:102` gives a default path and mentions alternatives. `references/api-reference.md:104` keeps deprecated entries until removal. Neither covers older-but-still-supported forms that readers will meet in real code. `references/tutorials.md:46` ("One path") points the other way for tutorials only, which is fine. For topic and reference pages this is absent.

### 1.8 Disambiguate lookalikes where the confusion happens

Inline, right where readers would mix things up:
- Component level, at the top of the page: `active_record_basics.md:28` (Active Record vs. Active Model), `action_mailer_basics.md:21-23` and `action_mailbox_basics.md:21-23` (sending vs. receiving mail, each linking the other).
- Method level: `association_basics.md:393` ("Do not confuse" two similar predicates), `active_record_querying.md:1008` (the "key difference" between two find-or-create methods, including atomicity), `action_view_helpers.md:897` (capture vs. content_for).

Skill: `references/explanation.md:17-19` covers separate comparison pages for choosing between options. It doesn't say to put the distinction inline at the point of confusion. Absent.

### 1.9 Show the wrong form beside the right one when misuse is likely

- `active_record_querying.md:1420-1431`: an injectable string condition next to the placeholder version.
- `action_view_overview.md:126`: an ERB snippet labeled "WRONG" to show that printing methods don't render.
- Both style docs teach almost every rule as a BAD/GOOD pair (`api_documentation_guidelines.md:50`, `:61`, `:73`, `:85`, `:109`, `:137`, `:151`).

Skill: absent. It gives only positive examples.

### 1.10 Code elisions must stay valid code

`ruby_on_rails_guides_guidelines.md:134-135`: if an example is executable, comment out the ellipsis. `getting_started.md` uses a commented-out `# ...` or `<%# ... %>` 25 times, so trimmed snippets still parse when pasted.

Skill: `SKILL.md:62` mentions a visible `...` only for trimmed output. Absent for code.

### 1.11 Make the execution context visible in the prompt

Console examples use a prompt that names the application and environment, `app(env)>`. It's defined in `ruby_on_rails_guides_guidelines.md:123` and used throughout `getting_started.md` (`:368` in development, `:3169` in production) and `active_record_querying.md`. A reader can tell at a glance whether a line runs in the shell or the console, and against which environment. That matters most for the production line.

Skill: `SKILL.md:92` treats prompts only as something to strip from copied text. Absent.

### 1.12 In reference for a modular library, say where each item comes from

`active_support_core_extensions.md:43` says every entry ends with a note naming the file that defines it, so readers can load just that piece. It does this 138 times.

Skill: `references/api-reference.md:52-70` (method template) has no "provided by" or "import from" slot. Absent.

### 1.13 Declare a long page's shared example schema once, at the top

`active_record_querying.md:53-117` defines the bookstore models (plus a diagram) once, and says every later snippet refers to them. Snippets can then stay short without redefining context. `getting_started.md` does the same for a tutorial with its single `store` app.

Skill: `references/tutorials.md:50` covers a running example for tutorials. It says nothing about a shared fixture for long reference or topic pages. Absent outside tutorials.

### 1.14 Type callouts by whether reading them is necessary

`ruby_on_rails_guides_guidelines.md:198-230` defines three callouts. NOTE helps understanding, TIP is optional extra (often a pointer elsewhere), and WARNING covers things that break the app or compromise security. Readers can skip TIPs safely and know they can't skip the others.

Skill: `SKILL.md:79` treats callouts as one kind and only limits warnings. Absent.

### 1.15 Show real uses of an API, attributed to their source

`active_support_core_extensions.md:1446`, `:1470`, `:1500`, `:1834`, `:3935` show how the framework itself calls a utility method, and say which component it comes from. This shows why the method exists, not just its signature.

Skill: `SKILL.md:90-91` asks for minimal invented examples with realistic names. Absent.

## 2. Corrections

### 2.1 Second person everywhere is too absolute

`api_documentation_guidelines.md:148`: "Prefer wordings that avoid 'you's", with a rewrite that drops the reader from a reference sentence. In the guides, reference-style option lists are also written impersonally. For example, the option list at `active_record_validations.md:1114-1122` describes what each option does, not what "you" do.

Skill: `SKILL.md:70` says "Use second person" with no exception for reference.

### 2.2 Warnings are for more than data loss, security, and money

`ruby_on_rails_guides_guidelines.md:223` defines WARNING as things to avoid "that could break the application", as well as security. The guides use it for silent correctness traps:
- `action_controller_overview.md:188` and `:271`: render and redirect don't return.
- `active_record_validations.md:952`: mutual association validation loops forever.

Skill: `SKILL.md:79` reserves warnings for data loss, security, and money, which would demote these.

### 2.3 Separating commands from output depends on the tooling

The guides keep `$` commands and their output in one block (`getting_started.md:87-88`, `routing.md:1413-1436`). The copy button strips prompts and filename comments (`ruby_on_rails_guides_guidelines.md:97`, `:121`), so readers get a readable transcript and a clean copy.

Skill: `SKILL.md:92` requires separate blocks unconditionally.

### 2.4 Showing the whole file with highlights is sometimes right

`getting_started.md` repeats the whole, still-short controller at each step and highlights the changed lines (`:1264` `#15-27`, `:1341` `#24-35`, `:1470`, `:1526`). The reader can resync to the full file state after each change. It switches to excerpts with `# ...` once files grow (`:1846`, `:1918`). `ruby_on_rails_guides_guidelines.md:147-150` gives the highlighting syntax for exactly this.

Skill: `SKILL.md:89` says "Not the whole file every time".

### 2.5 Placeholder names fit structural examples

For examples about inheritance and namespacing, `active_support_core_extensions.md` uses `X::Y::Z` (`:631`, `:656`, `:681`) and `class A` / `B < A` (`:881`). No domain applies there, and domain names would add noise.

Skill: `SKILL.md:91` says "never `foo`/`bar`".

### 2.6 Scale entry structure to the entry's size

`api_documentation_guidelines.md:186`: short docs don't need an "Examples" label; larger ones may use a labeled section. Entries in `active_support_core_extensions.md` share a shape (description, example, "Defined in" note) but leave out sections that don't apply.

Skill: `references/api-reference.md:3` says every entry should have the same sections "even when a section is 'None.'"

## 3. House conventions

- **Headings:** title case for headings (`ruby_on_rails_guides_guidelines.md:50`), where the skill uses sentence case (`SKILL.md:75`).
- **Spelling and grammar:** American spelling, the Oxford comma, and "an SQL" (`api_documentation_guidelines.md:134-177`).
- **RDoc markup:** `+x+` vs `<tt>`, `==== Examples`, `:nodoc:`, hyphens in description lists, and aligned `# =>` result comments (`api_documentation_guidelines.md:186-411`).
- **Naming:** component names spelled with spaces ("Active Record") vs. module names (`api_documentation_guidelines.md:98`), and "application", not "service" (`:106`).
- **Formatting:** 80-column wrapping and `NOTE:`/`TIP:`/`WARNING:` paragraph prefixes (`ruby_on_rails_guides_guidelines.md:188`, `:304`).
- **Prompts:** the `$` and `app(env)>` prompt strings themselves (`ruby_on_rails_guides_guidelines.md:112`, `:123`). The principle behind them is in 1.11.

## 4. Where the Rails guides fall short

### 4.1 Factual and code errors that running and verifying would catch

- `layouts_and_rendering.md:192-193` labels the form-error status "303 Unprocessable Content" and links the 303 page. The status meant is 422.
- `action_controller_overview.md:1066` and `:1073` misspell the cookies object.
- `association_basics.md:1494` passes an `_id` name to a helper that appends `_id` itself.
- `install_ruby_on_rails.md:109` shows `Rails 8.1.0` as expected output, while `getting_started.md:76` requires 8.2.0 or newer.

Skill: `SKILL.md:52`, `SKILL.md:62`, and `SKILL.md:110-112` (verify every name and output, run every example in order, state versions).

### 4.2 Inconsistent terms for one thing across guides

The form-error status symbol is `:unprocessable_entity` in `getting_started.md` (7 times) and `action_mailer_basics.md` (2), but `:unprocessable_content` in `action_controller_overview.md` (2) and `layouts_and_rendering.md` (5).

Skill: `SKILL.md:76` (one term per concept).

### 4.3 Ease words and marketing adjectives

"easily" appears in at least ten of the guides (for example `active_record_basics.md:327`, `active_record_validations.md:301`). There's also "simply" (`action_controller_overview.md:272`), "Just specify" (`active_record_migrations.md:1350`), "seamless" (`active_record_basics.md:381`), "very powerful" (`active_record_basics.md:105`, `routing.md:661`), and "robust test suite" (`getting_started.md:2749`).

Skill: `SKILL.md:73` and `SKILL.md:80`.

### 4.4 Prologue objectives that can't be checked

Many "you will know" lists name knowing-about, not doing: `active_record_basics.md:10-11`, `active_model_basics.md:13`, `action_view_overview.md:8`, `action_text_overview.md:11`. The guidelines only ask the prologue to say what the reader "will learn" (`ruby_on_rails_guides_guidelines.md:29-31`).

Skill: `SKILL.md:48` and `references/learning-science.md:57-59` (observable outcomes).

### 4.5 The guides break their own descriptive-link rule

`ruby_on_rails_guides_guidelines.md:246-255` marks a bare "below" link as BAD. It still appears at `active_record_validations.md:837` and `form_helpers.md:76`.

Skill: `references/style.md:16`.

### 4.6 The same material covered twice, drifting

- The query guide documents the same method twice: `active_record_querying.md:1956` and again under `:3218`.
- Association callbacks are written up in both `active_record_callbacks.md:961` and `association_basics.md:3209`, with different examples for the same feature.

Skill: `SKILL.md:81` and `references/api-reference.md:91-93` (cover once, link from elsewhere).

## Confirmations (only where the skill says something unusual)

- **Literal error text:** `SKILL.md:103` is confirmed by `active_record_basics.md:371` and `active_record_migrations.md:1371`, which quote error output verbatim.
- **No hedging:** `SKILL.md:82` is confirmed by `api_documentation_guidelines.md:47-56` (BAD/GOOD: drop "may" for a plain declarative).
- **Default path:** `SKILL.md:102` is confirmed by `api_documentation_guidelines.md:82` (teach the current idiom; reorder to favor it).

## Observed, not counted

### One page per component, combining explanation, how-to, and reference

Each component guide puts all three modes on a single page. They're ordered from why, to what exists, to how, and ending with lookup. Only `h2` headings separate them, with no label saying which mode a section is.

- `association_basics.md`:
  - Explanation: it opens with why associations exist, contrasting code with and without them (`:18`).
  - Catalog: each association type follows, with its generated methods (`:141`).
  - Explanation again: a section on choosing between types (`:1441`).
  - Practical caveats: "Tips, Tricks, and Warnings" (`:2100`).
  - Reference: an options-and-scopes section at the end (`:2562`).
- `active_record_validations.md`:
  - Explanation: an overview of why to validate at the model and what alternatives exist (`:19`).
  - Reference: a catalog of built-in validators, then option lists (`:345`, `:1109`).
  - How-to: custom validators (`:1466`) and displaying errors in views (`:1904`).
- `routing.md`:
  - Explanation: the router's purpose (`:18`).
  - Catalog: the resourceful and non-resourceful features (`:100`, `:658`).
  - How-to: inspecting routes (`:1384`), testing them (`:1492`), and splitting the routes file (`:1536`).

Skill: `SKILL.md:44` says pages that mix modes are bad, and that a page doing two jobs should be split and the halves linked.

I didn't count this as a correction because the guides only show that this structure exists and is consistent. They don't show that readers are better served than they would be by split pages.

## Abstracted

### Missed principles

1. Wherever a call is a layer over something lower-level (a query, markup, a request), show the artifact it produces right after the call, so readers learn both the interface and its effect.
2. Introduce a convenience by first showing the longer code it replaces. The shortcut only means something to someone who has seen what it saves.
3. Verify and document behavior as it appears in the default, fully assembled setup a typical user runs. A component in isolation can behave differently from the same component in its usual surroundings.
4. Document only what the interface promises. For yes/no results, describe the truth condition, not the exact value returned. Keep public-but-internal items out of user docs, because whatever you document becomes a commitment.
5. For every entry, ask what happens with empty, missing, null, zero, or otherwise degenerate input, and write the answer down.
6. When a feature provides a guarantee (validation, hooks, constraints), list exactly which operations bypass it, and flag the bypass each time you show one of those operations.
7. Keep older but still-supported ways of doing something in the docs. Place them after the current way, label them as older, and say readers will meet them in existing code.
8. Where two things are easy to confuse (components, methods, options), put the distinction inline at the point of confusion and link each to the other. Don't leave it only on a separate comparison page.
9. When a mistake is common or dangerous, show the wrong form, clearly labeled as wrong, beside the right one.
10. Any elision inside runnable code must itself be valid code, such as a comment, so a trimmed snippet still runs when pasted.
11. Make each example's execution context visible (which shell or interactive session, which environment), most of all when a line runs against production.
12. In reference for a library that loads in pieces, state which module, package, or import provides each item.
13. On a long page whose examples share a setup, define that shared setup once near the top and have every later example refer to it.
14. Give callouts distinct types that tell the reader whether they can skip them: essential context, optional extras and pointers, and warnings about things that break.
15. Where it explains a method's purpose, show a real call site from a known codebase and say where it comes from, alongside or in place of an invented example.

### Corrections

1. Use second person in tutorials and task steps. In reference descriptions, prefer impersonal wording that describes the item, not the reader.
2. Use warnings for anything that silently breaks correctness (traps where code looks right but does something else), as well as for data loss, security, and money. Keep them rare so they stay visible.
3. Keep commands and their output in separate blocks only when the docs platform would copy prompts and output along with the command. If copying strips them, a single transcript block reads better.
4. When a file under construction is still short, showing the whole file with the changed lines highlighted helps readers resync. Switch to anchored excerpts once the file grows.
5. Use realistic domain names by default, but use neutral placeholder names when the example is about pure structure (nesting, inheritance) and no domain fits.
6. Keep entries of the same kind in the same order, but scale the structure to each entry's size. Leave out labels and sections that would be empty.
