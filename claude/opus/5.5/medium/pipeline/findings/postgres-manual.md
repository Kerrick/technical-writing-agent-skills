Source: PostgreSQL manual (tutorial, SQL language, func-string, six SQL command reference pages), commit 8303f2e

> Quotes and descriptions in this file are from the [PostgreSQL documentation](https://www.postgresql.org/docs/current/) ([postgres/postgres](https://github.com/postgres/postgres)), portions copyright (c) 1996-2026 PostgreSQL Global Development Group and (c) 1994 The Regents of the University of California, licensed under the [PostgreSQL License](https://www.postgresql.org/about/licence/). Quotes are short, and used to compare and criticize.

# PostgreSQL manual vs. the `technical-writing` skill

The skill being compared is `~/.agents/skills/technical-writing/` as first written. Skill references use `SKILL.md:N` or `references/<file>.md:N`. Manual paths are relative to `doc/src/sgml/`. `docguide.sgml` is read as the stated intent behind the pages.

## How each command is split between chapter and reference page

| Command | Teaching chapter | Reference page |
| - | - | - |
| `SELECT` | `query.sgml` (tutorial), `queries.sgml` | `ref/select.sgml` |
| `INSERT`, `UPDATE`, `DELETE` | `query.sgml` (tutorial), `dml.sgml` | `ref/insert.sgml`, `ref/update.sgml`, `ref/delete.sgml` |
| `CREATE TABLE` | `ddl.sgml` | `ref/create_table.sgml` |
| `CREATE INDEX` | `indices.sgml` | `ref/create_index.sgml` |

**What the chapter includes:**
- Motivation for the feature.
- A running scenario: `weather`, `products`/`orders`, `measurement`.
- The common forms, built up one option at a time.
- Result output shown after the queries.
- Design advice. For example, `ddl.sgml:1311` covers how to choose an `ON DELETE` action.

**What the chapter leaves out:** privileges, command tags, the full option list (storage parameters, `TABLESPACE`, `LIKE` options), and standards compatibility. The chapter often says that it leaves something out (see M9).

**What the reference page includes:**
- The full grammar in a synopsis.
- Every parameter.
- Required privileges.
- Locks taken and blocking behavior.
- Clause-interaction rules.
- Return value or command tag.
- Version-history notes.
- A Compatibility section.
- A gallery of captioned examples that uses its own shared sample tables (`films`, `distributors`).

**What the reference page leaves out:** motivation and design advice, mostly, and output tables, mostly. The `SELECT` examples are the exception: they show results.

**Links in both directions:**
- Chapter to reference page, for the full syntax:
  - `ddl.sgml:264`: "See CREATE TABLE for more details"
  - `ddl.sgml:1942`: "whose reference page contains details beyond those given here"
  - `ddl.sgml:4441`
- Reference page to chapter, for the reasoning:
  - `ref/create_index.sgml:77`: "for more discussion"
  - `ref/select.sgml:381`
  - `ref/create_table.sgml:471`

**Overlap:** important cautions appear in both places, nearly word for word (see C3).

**Imbalance:** `dml.sgml` is thin. Upsert (`ON CONFLICT`), `UPDATE … FROM` and batch updates are taught only on the reference pages (see F7).

## 1. Missed principles

**M1. A reference entry for a multi-part operation opens with the order in which the parts are evaluated, and links each step to its section.**
- Evidence: `ref/select.sgml:91` ("The general processing of SELECT is as follows") is a numbered list, and each step ends with "(See … below.)". The chapter uses the same model at `queries.sgml:103`, which describes the clauses as a "pipeline of successive transformations".
- Skill: absent. `references/api-reference.md` has no overview or evaluation-order element.

**M2. Show the whole syntax first, then name each nested piece and define it below the full shape.**
- Evidence:
  - `ref/select.sgml:50`: "where from_item can be one of:"
  - `ref/insert.sgml:32`, `ref/insert.sgml:37`
  - `ref/create_table.sgml:65`, `73`, `88` and `105`: a chain of "and … is:" definitions
- Skill: absent. `references/api-reference.md` asks only for a single "Usage line" for a CLI command.

**M3. A reference entry states the operational side effects of using it: what it locks or blocks, what it costs at scale, and how to avoid the cost.**
- Evidence:
  - `ref/insert.sgml:81`: tables without unique indexes "will not be blocked by concurrent activity"
  - `ref/create_table.sgml:646` and `1261`: the lock levels taken
  - `ref/create_index.sgml:128`: a normal build "locks out writes (but not reads)"
- Skill: absent. The fields listed at `references/api-reference.md:86` cover behavior, defaults and interactions, but not side effects on other users or on the system.

**M4. Tell readers who arrive with expectations from a standard or a similar system where this implementation departs from it.**
- Evidence:
  - Every reference page ends with a Compatibility section: `ref/insert.sgml:890`, `ref/update.sgml:525`, `ref/delete.sgml:336`, `ref/create_table.sgml:2440`.
  - Porting warnings appear inline: `ref/update.sgml:535` ("Be careful when porting"), `mvcc.sgml:1760` and `mvcc.sgml:1765`.
  - `syntax.sgml:18` tells experienced readers to read the chapter carefully because the rules vary between systems.
- Skill: absent.

**M5. Reference entries share one small sample domain, so their examples read as a set.**
- Evidence: `films`/`distributors` appear in all six reference pages: `ref/select.sgml:1763`, `ref/insert.sgml:691`, `ref/update.sgml:365`, `ref/delete.sgml:259`, `ref/create_table.sgml:2115`, `ref/create_index.sgml:902`. These tables are separate from the scenarios the chapters use.
- Skill: absent. `references/api-reference.md` asks only for consistent values within one request and its response, and `SKILL.md:91` asks for consistency across a running example.

**M6. Match the weight of a reference entry to the size of the item: many small functions go in one table, one row each, with signature, one-line description and an example paired with its exact result. Overloads and aliases share a row.**
- Evidence:
  - `func/func-string.sgml:48` and `561`: the "Example(s)" column header
  - `func/func-string.sgml:172` to `179`: `char_length` and `character_length` in one row
  - `func/func-string.sgml:1499` to `1504`: `to_hex` for `integer` and `bigint` in one row
- Skill: `references/api-reference.md:52` offers a multi-section template for every function or method and has no compact form.

**M7. Choose examples that expose the boundary cases where readers would guess wrong: negative arguments, nulls, multibyte input.**
- Evidence:
  - `func/func-string.sgml:784`: negative `n` for `left`
  - `func/func-string.sgml:1301`: `split_part` with `-2`
  - `func/func-string.sgml:641`: `concat` with a `NULL` argument
  - `func/func-string.sgml:290`: `octet_length` of an accented string, showing that bytes differ from characters
- Skill: differs from `SKILL.md:90` ("the shortest code that shows it"), which says nothing about choosing the revealing case.

**M8. To show how variants differ, keep the input fixed, change one thing at a time, and show every result.**
- Evidence:
  - `queries.sgml:433` to `492`: every join type run on the same two tiny tables
  - `queries.sgml:517`: the same filter put in `ON` and then in `WHERE`, showing different results
  - `advanced.sgml:471` and `500`: the same `sum` computed without and with a window `ORDER BY`
  - `syntax.sgml:2654`, `2689` and `2739`: one function called in positional, named and mixed notation
- Skill: absent. `SKILL.md:90` asks for one concept per example but not for comparisons across variants.

**M9. Say what the page deliberately leaves out, and where the reader can find it.**
- Evidence:
  - `ddl.sgml:1278`: "(not covered in this chapter)"
  - `ddl.sgml:1942`
  - `advanced.sgml:131` and `advanced.sgml:463`
  - `start.sgml:301`
- Skill: absent. `SKILL.md:114` asks only that a page not depend on knowledge it neither gives nor links.

**M10. Wherever readers make a predictable mistake, show the tempting wrong form next to the right one, label which is wrong, and say why. This applies to reference and conceptual pages, not only to tutorials.**
- Evidence:
  - `query.sgml:684`: "-- WRONG"
  - `queries.sgml:583` and `queries.sgml:1881`: "-- wrong"
  - `syntax.sgml:1661`: "-- incorrect"
  - `syntax.sgml:2523`: an "untrustworthy" pattern next to a safe one
  - `ddl.sgml:5011`: "A common mistake"
- Skill: differs from `references/tutorials.md:53`, which allows one deliberate error per tutorial and calls more "a detour", and from `references/explanation.md:14`, which limits refutation to wrong mental models.

**M11. Give known limitations and caveats their own findable section, instead of scattering them.**
- Evidence: `ddl.sgml:4201` (Caveats), `ddl.sgml:4794` (Limitations), `ddl.sgml:5250` (Caveats), `mvcc.sgml:1887` (Caveats).
- Skill: absent. Neither `references/explanation.md` nor `references/how-to-guides.md` asks for one.

## 2. Corrections

**C1. "Identical sections, even when a section is None" is too absolute.**
- Stated intent: `docguide.sgml:488` says sections that do not apply can be omitted. `docguide.sgml:657` says the Outputs section is needed only when the command returns something unusual.
- Practice: `ref/select.sgml` has no Outputs or See Also section. `ref/insert.sgml` and `ref/update.sgml` have no See Also section.
- The fixed part is the order of the sections, not the presence of every one.
- Skill: `references/api-reference.md:3`.

**C2. An exhaustive error table is the wrong default.**
- Stated intent: `docguide.sgml:585`, "Refrain from listing every possible error message", with the reason that it "has little use in practice". Explain unusual output, or the error format if readers parse it.
- Practice: none of the six reference pages has an error list. Error conditions are stated in prose at the parameter they concern, for example `ref/insert.sgml:412` ("If an attempt at inference is unsuccessful, an error is raised").
- Skill: `references/api-reference.md:44`, an Errors table listing each status and code.

**C3. "Cover cross-cutting topics once" is too absolute.**
- The general topic is covered once: privileges in `ddl.sgml` (Privileges), sort order in `queries.sgml`.
- Each reference entry still states the specific requirement or hazard that applies to it:
  - Required privileges at `ref/select.sgml:212`, `ref/insert.sgml:106`, `ref/update.sgml:67`, `ref/delete.sgml:68`.
  - The `LIMIT` without `ORDER BY` warning, nearly word for word, at `queries.sgml:1947` and `ref/select.sgml:1540`.
  - The `INCLUDE` caution at `indices.sgml:1281` and `ref/create_index.sgml:169`.
  - The opclass explanation at `indices.sgml:1405` and `ref/create_index.sgml:743`.
- Skill: `references/api-reference.md:91` to `93` ("Repeating them per entry drifts out of sync"). It is also in tension with `SKILL.md:81`.

**C4. "Show the minimal call first; add a fuller example only when common options need it" undersells the examples section.**
- Reference pages end with a gallery: one example per common task or notable clause, each introduced by a sentence naming the task.
- Evidence: `ref/create_index.sgml:901` to `984`, eleven examples that each begin "To create …"; `ref/create_table.sgml:2115` onward; `ref/insert.sgml:691` onward.
- Readers searching for how to do X with this command land on these examples.
- Skill: `references/api-reference.md:98`.

**C5. Warnings are not only for data loss, security and money.**
- The manual uses caution and warning callouts for results that are silently wrong:
  - `ref/select.sgml:1701`: rows returned out of order under a locking clause
  - `datatype.sgml:2384`: stored literal values that go stale
  - `datatype.sgml:4628`: functions failing on non-ASCII data
  - `mvcc.sgml:1736`: integrity guarantees not extending to replicas
- Lower-severity material gets lighter tiers (note, tip), so the scale stays meaningful.
- Skill: `SKILL.md:79`.

**C6. "Never foo/bar" is too absolute.**
- To show pure semantics, the manual uses tiny abstract tables and prints every row, so the reader can check each result by hand. A domain would only distract.
- Evidence: `queries.sgml:415` to `500` (`t1` and `t2` with `num` and `name`); `queries.sgml:1062` (`test1` with columns `x`, `y`); `queries.sgml:1242` (`items_sold`).
- The failure is abstract names when the data is not shown (see F5).
- Skill: `SKILL.md:91`.

**C7. "Show, then tell" is too absolute.**
- Teaching sections open with one sentence saying what the thing is, then give an example right away: `ddl.sgml:604` (check constraint) and `ddl.sgml:1094` (foreign key).
- Reference pages put Examples after Description, Parameters and Notes, by design (`docguide.sgml:488`), because lookup readers come for definitions first.
- Skill: `SKILL.md:77`.

## 3. House conventions

- **Synopsis notation:** `[ ]`, `{ | }`, `[, ...]` and italic replaceables, in the man-page tradition. Evidence: `ref/select.sgml:35` to `48`, `ref/create_table.sgml:24` to `59`. The general rule is in M2; the notation itself doesn't carry over.
- **Fixed section names and order inherited from Unix man pages,** including the ordering rule for See Also (`docguide.sgml:488`, `docguide.sgml:637` to `643`). Evidence: the section titles of all six reference pages.
- **Compatibility measured against the SQL standard specifically.** Evidence: `ref/insert.sgml:890`, `ref/update.sgml:525`. The general rule is in M4.
- **psql session formatting:** `=>` prompts and `(n rows)` footers in result blocks. Evidence: `queries.sgml:433` to `499`, `start.sgml:362` to `378`.

## 4. Where the manual falls short

**F1. The tutorial uses words that talk down to readers and an aside the manual itself calls dispensable, before the reader's first success.**
- Evidence:
  - `start.sgml:11`: "of course"
  - `start.sgml:247`: "simply type"
  - `start.sgml:118` to `119`: the architecture section ends "(All of this is of course invisible to the user. We only mention it here for completeness.)", ahead of creating the first database
- Skill: `SKILL.md:73`; `references/tutorials.md:48`.

**F2. Tutorial examples depend on data the page never gives.**
- Evidence:
  - `advanced.sgml:25`: the sample data "is not repeated here"
  - The `empsalary` queries at `advanced.sgml:355` and the inheritance results at `advanced.sgml:670` can't be reproduced from the page.
- Skill: `SKILL.md:62`; `references/tutorials.md:55`.

**F3. Some parameter descriptions just restate the parameter's name.**
- Evidence: `ref/create_index.sgml:253` ("The name of a column of the table."), `ref/create_table.sgml:297`, `ref/insert.sgml:363`, `ref/update.sgml:263`.
- Skill: `references/api-reference.md:5`.

**F4. Chapters open by announcing themselves instead of stating the outcome.**
- Evidence: `syntax.sgml:12` ("This chapter describes …"), `mvcc.sgml:11`, `typeconv.sgml:27`.
- Skill: `SKILL.md:74`.

**F5. Abstract names are used without showing the data,** so the reader has nothing to check results against.
- Evidence: `queries.sgml:748` (`foo` and `getfoo`), `queries.sgml:889` (`foo` and `bar` in the `LATERAL` example).
- Skill: `SKILL.md:91`.

**F6. The tutorial ends with a generic conclusion,** not a recap of what the reader can now do.
- Evidence: `advanced.sgml:719`.
- Skill: `references/tutorials.md:54`.

**F7. A common task is taught only on a reference page.**
- `dml.sgml` mentions `ON CONFLICT` only as a link target, at `dml.sgml:388`.
- Upsert is explained only at `ref/insert.sgml:370` to `641` and in that page's examples.
- No chapter or how-to section covers it.
- Skill: `SKILL.md:34` and `SKILL.md:44`.

**F8. Statements and their output share one copyable block.**
- Evidence:
  - `query.sgml:863` to `872`: a `SELECT` and its result table in one program listing
  - `start.sgml:362` to `378`: prompt, input and output together
- Skill: `SKILL.md:92`.

## Confirmations

- `SKILL.md:103`: literal error text with its cause and fix is how the tutorial handles setup failures (`start.sgml:179`, `190`, `210`).
- `references/explanation.md:13`: the manual flags where a simplified model departs from reality (`query.sgml:464` "only a conceptual model", `rowtypes.sgml:291`).
- `SKILL.md:102`: alternatives come with the consequences of choosing each (`ref/update.sgml:429` to `441`, `ref/delete.sgml:267`).
- `references/api-reference.md:103`: version notes say what changed and what older code may rely on (`ref/select.sgml:375`, `ref/select.sgml:1187`, `ref/create_table.sgml:899`).

## Observed, not counted

Some pages contain sections in a second mode:

- **Reference pages with how-to and explanation sections:**
  - `ref/create_index.sgml:599` ("Building Indexes Concurrently") explains the build phases and why a build can fail, then gives the recovery procedure (`ref/create_index.sgml:669`, "The recommended recovery").
  - `ref/update.sgml:480` is a batch-update recipe with its rationale, placed in Examples. `ref/delete.sgml` links to it.
  - `ref/select.sgml:1701` to `1724` is a caution that explains a cause and gives a workaround.
- **Conceptual chapters that embed lookup tables:**
  - the privilege abbreviation table at `ddl.sgml:2597`
  - date input formats at `datatype.sgml:1933`
  - the lock conflict matrix at `mvcc.sgml:1134`

Elsewhere the manual keeps the modes apart. The tutorial (`start`, `query`, `advanced`), the conceptual chapters, the command reference pages and the function tables are separate parts. Reference pages hand the reasoning back to the chapters with links (`ref/create_index.sgml:77`, `ref/select.sgml:381`).

**Why this isn't counted as a correction to `SKILL.md:44`:** each embedded section is bounded and serves the job of the page it sits on. The recovery steps serve someone looking up `CONCURRENTLY`, and the lookup tables serve someone reading about privileges or types. `SKILL.md:44` objects only when a page tries to do two jobs, so these don't contradict it.

## Abstracted

1. When a reference entry describes an operation with several stages, open with a numbered list of the stages in the order they are evaluated, and link each stage to the section that details it.
2. When a signature or grammar nests, show the complete shape first with named placeholders, then define each placeholder underneath. Don't inline every alternative.
3. In each reference entry, state the operational side effects of using the item: what it blocks or locks, what it costs on large inputs, what other users or processes feel, and the variant that avoids the cost.
4. Readers often arrive with habits from a standard, a specification or a competing product. Give each entry a section saying where this implementation conforms, extends or differs, and add an inline warning wherever those habits lead someone astray.
5. Give all reference entries one small, shared sample domain, separate from the tutorial's scenario, so examples across entries use the same names and can be compared.
6. Match the weight of a reference entry to the item. Put many small items in one table, one row each: signature, a one-line description, and an example paired with its exact result. Variants and aliases share a row.
7. Choose examples that sit on the boundaries where readers would guess wrong, such as negative or zero arguments, missing values and non-ASCII input, and show the exact result.
8. To explain how variants differ, keep the input fixed, change one thing at a time, and show the result of each variant one after another.
9. When a page leaves out something a reader might expect, say so at that point and link to where it is covered.
10. Wherever readers predictably reach for a plausible but wrong form, show it next to the correct one, mark which is wrong, and explain why. This applies on reference and conceptual pages too, not only in tutorials.
11. Collect a feature's known limitations and caveats in a clearly titled section of their own.
12. Keep the section order fixed across entries of the same kind, but leave out sections that have nothing to say rather than filling them with "None".
13. Don't catalog every possible error. Describe the conditions that cause an error at the parameter or step they concern, and document the error format only if readers parse it.
14. Explain a cross-cutting topic fully in one place. In each entry it affects, still state in a line or two the specific requirement or hazard that applies there, and link to the full treatment.
15. End a reference entry with a set of examples covering its common tasks and notable options, each introduced by a short sentence naming the task, rather than a single minimal call.
16. Use warnings for outcomes that are silently wrong as well as for data loss, security and money. Keep lighter callout levels for tips and notes so severity stays meaningful.
17. Abstract placeholder names are fine for demonstrating pure behavior if the data is tiny and every row or value is shown. Use realistic names when the example is a task or the data isn't shown.
18. In teaching material, a one-sentence definition followed immediately by an example works as well as example-first. In lookup material, put the definitions before the examples.
