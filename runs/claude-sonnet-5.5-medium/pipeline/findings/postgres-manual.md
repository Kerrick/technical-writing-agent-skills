Source: PostgreSQL manual (tutorial, SQL language, func-string, six SQL command reference pages), commit 8303f2e

> Quotes and descriptions in this file are from the [PostgreSQL documentation](https://www.postgresql.org/docs/current/) ([postgres/postgres](https://github.com/postgres/postgres)), portions copyright (c) 1996-2026 PostgreSQL Global Development Group and (c) 1994 The Regents of the University of California, licensed under the [PostgreSQL License](https://www.postgresql.org/about/licence/). Quotes are short, and used to compare and criticize.

Skill compared: `developer-docs/SKILL.md`, `references/reference-and-guides.md`, `references/teaching.md`, `references/books-and-video.md` (written before reading; unchanged).
Source paths are relative to `doc/src/sgml/`; `ref/` pages are `select`, `insert`, `update`, `delete`, `create_table`, `create_index`.
Skill citations use short names: SKILL = `developer-docs/SKILL.md`, REF = `developer-docs/references/reference-and-guides.md`, TEACH = `developer-docs/references/teaching.md`.

## 1. Missed principle

**M1. Lessons omit whole features on purpose, say so at the spot, and name where the rest lives.**
- Evidence, scope statements: `query.sgml:12-13` ("in no way a complete tutorial"); `advanced.sgml:131` ("We will not go beyond this simple example") and `advanced.sgml:462-464` (window-frame options: "this tutorial does not cover them", followed by a link); `indices.sgml:132-134` (concurrent index builds: one sentence, then a deep link to a named subsection of the reference page).
- Evidence, reader routing: `ddl.sgml:164-167` (readers eager to load data "can skip ahead"); `syntax.sgml:17-22` (experienced readers are told to read the chapter closely because several rules differ from what they expect).
- How each command is split (this is the evidence for the omission pattern):
  - SELECT. `query.sgml`/`queries.sgml` teach clause by clause on small tables. They contain none of TABLESAMPLE, WITH TIES, FETCH FIRST, SKIP LOCKED or FOR UPDATE (0 matches in `query`, `queries`, `dml`). Row locking is taught in a different chapter (`mvcc.sgml:1295-1404`), and the reference page carries the locking clause (`ref/select.sgml:1568-1733`), the sampling clause and the full grammar (`:35-82`).
  - INSERT / UPDATE / DELETE. `dml.sgml` gives each command a short section. It has no UPDATE ... FROM, no DELETE ... USING, no WHERE CURRENT OF and no OVERRIDING; ON CONFLICT appears only as a link (`dml.sgml:388`). The reference pages hold: upsert and conflict-target inference (`ref/insert.sgml:370-641`), the identity-override clause (`:218-256`), join-style update (`ref/update.sgml:301-317`), partition row movement (`:320-357`), join-style delete (`ref/delete.sgml:256-274`), and a batching recipe (`ref/update.sgml:480-518`).
  - CREATE TABLE. `ddl.sgml` is organised by feature (defaults, identity, generated columns, each constraint kind, partitioning, inheritance), not by command syntax. The reference page adds persistence modes, typed tables, the full list of LIKE options and all storage parameters (`ref/create_table.sgml:1578-2084`); `ddl.sgml` has none of fillfactor, COMPRESSION, ON COMMIT or UNLOGGED.
  - CREATE INDEX. `indices.sgml` teaches types, multicolumn, ordering, partial, covering and operator classes. The reference page adds how a concurrent build works and fails (`ref/create_index.sgml:598-710`), per-method storage parameters (`:385-596`) and parallel-build tuning (`:798-868`).
  - What the reference leaves out: motivation and design guidance. `ddl.sgml:1310-1328` explains how to choose between delete actions; `ref/create_table.sgml:1297-1374` defines each in a sentence or two with no advice on choosing.
  - Links: chapters link the command name to its reference page at first mention (`dml.sgml:36,144,246`; `queries.sgml:27`; `indices.sgml:157`). Reference pages deep-link back to the teaching section for the same topic (`ref/select.sgml:829,1107-1109,1600`; `ref/create_table.sgml:471`; `ref/create_index.sgml:77,747`; `ref/update.sgml:488-491`). The links go to named sections, not to a book or chapter top.
- Skill line: absent. Nearest are TEACH:23 ("Remove anything incidental ... tangents"; says nothing about marking what was removed), REF:59 ("Name the scope", explanations only) and SKILL:35 (first paragraph says what the page is for).

**M2. Record where behaviour departs from conventions the reader brings from elsewhere.**
- Evidence: a "Compatibility" section in all six reference pages (`ref/select.sgml:1988`, `insert.sgml:886`, `update.sgml:521`, `delete.sgml:332`, `create_table.sgml:2436`, `create_index.sgml:991`). It also carries portability warnings: `ref/update.sgml:532-536` ("That is not how PostgreSQL interprets FROM. Be careful when porting"); `ref/insert.sgml:899-900` points to the more standard alternative; `ref/select.sgml:2074-2076` says which form the standard disallows.
- Skill line: absent. A search of the skill for compat/standard/port finds only "port numbers" (TEACH:41). Nearest are REF:16 (version info) and REF:63-64 (migration guides), which cover change over time, not departure from outside conventions.

**M3. Reference examples are a catalogue: one per distinct form or option, each introduced by a plain goal sentence, each runnable alone.**
- Evidence: `ref/insert.sgml` has 17 code listings, all inside Examples (`:688-883`); `ref/update.sgml` has 12, all inside Examples (`:360-519`). Lead-ins state the goal: `insert.sgml:691` ("Insert a single row into table films:"), `:721` ("To insert a row consisting entirely of default values:"), `:862` ("Insert a new distributor or return and lock the existing row"). Order runs from the plain form (`:694`) to the subtle option (`:866`). `ref/delete.sgml` has 5 examples (`:283-314`) in the same style.
- Skill line: REF:15 ("At least one realistic example ... a second shows the most important option"). Too few for a command with many forms.

**M4. Examples show the input data, the statement and the exact result together, so the reader can check by hand.**
- Evidence: `queries.sgml:414-431` prints both input tables, then nine statements each followed by its result; `array.sgml:155-161` shows the table contents after the inserts; `ddl.sgml:3146-3187` is a whole session transcript with the expected denials.
- Skill line: SKILL:43 covers only the output block ("output shown in a separate block"); SKILL:64 checks that output matches. Showing the input is absent.

**M5. Show the tempting wrong form beside the right one, mark it in the code, and say why it fails.**
- Evidence: `query.sgml:684` (code marked WRONG, reason at `:687-692`, fix at `:697-700`); `syntax.sgml:1661` (marked incorrect, reason at `:1663-1665`); `queries.sgml:583` and `:1881` (marked wrong). Two of the four are in reference-style chapters, not lessons.
- Skill line: partial overlap only in TEACH:28 (misconceptions) and TEACH:31 (trigger a common error once); both are scoped to tutorials. Absent for reference and guide material.

**M6. Behaviour decided by layered rules is written as an ordered procedure with explicit tie-break order, then worked examples that name the deciding step.**
- Evidence: `typeconv.sgml:221-352` (operator resolution as numbered steps and substeps; "Some examples follow" at `:355`, `:759`, `:1126`); examples cite step ids: `:508` ("tells it to assume ..."), `:535` and `:538` (which step fired and which did not, for the custom-operator case). `syntax.sgml:993-1108` does the same job for precedence with a table that gives associativity.
- Skill line: absent. SKILL:36 numbers steps for a user's task, not for a rule the system applies.

**M7. Single-source the machinery, but repeat the costliest trap wherever the reader first meets the feature, sized to the page.**
- Evidence, trap repeated: unordered results are warned about at three sizes: `query.sgml:388-390` (one sentence in a lesson), `queries.sgml:1811-1817` (a paragraph, then a second paragraph on LIMIT at `:1943-1964`), `ref/select.sgml:181-185` (one clause in the processing list; LIMIT at `:1537-1557`). WHERE versus HAVING is stated at `query.sgml:784-800`, `queries.sgml:1161-1173` and `ref/select.sgml:884-891`.
- Evidence, machinery single-sourced: see confirmations for REF:23.
- Skill line: REF:23 ("once ... not repeated per endpoint") and SKILL:70 ("duplicated tables") say nothing about hazards. See also G4-8: two of these repeats are near-verbatim copies, which the skill's advice would avoid.

**M8. Match the layout conventions of the tools readers already use, not only the doc set's own.**
- Evidence: `docguide.sgml:475-483` states the aim as consistency among reference pages "but also with reference pages provided by the operating system and other packages". The six pages use the man-page section vocabulary (`refmeta`, `manvolnum` 7 at e.g. `ref/select.sgml:20-24`).
- Skill line: REF:21-22 asks for sameness inside one doc set and for mirroring the product's own structure only.

## 2. Correction

**C1. Reference voice is not strictly neutral; short advice with a reason sits beside the rule it qualifies.**
- Evidence (five of six pages): `ref/update.sgml:315` ("referencing other tables only within sub-selects is safer, though often harder to read and slower"); `ref/select.sgml:1136` ("it is recommended that you always either write AS or double-quote"); `ref/insert.sgml:630` (a tip: "It is often preferable to use unique index inference"); `ref/create_index.sgml:169` ("It's wise to be conservative about adding non-key columns"); `ref/create_table.sgml:599` ("you should choose a modulus equal to the number of partitions"). The stated intent for the Notes section is "anything that doesn't fit elsewhere", with bugs, security and compatibility named (`docguide.sgml:593-601`).
- Skill line: REF:24 ("No opinions, no 'you should'; put recommendations in guides and link them").

**C2. A reference should not promise every error with exact text.**
- Evidence: `docguide.sgml:585` ("Refrain from listing every possible error message. This is a lot of work and has little use in practice") with the exception of formats users can parse. The three DML reference pages contain no message transcripts (0 matches for `ERROR:` in `insert`, `update`, `delete`); they name conditions in prose where the rule is stated (`insert.sgml:412,615,675`; `update.sgml:324,338`) and state non-errors (`update.sgml:285`, `delete.sgml:240`: zero rows "not considered an error"). Verbatim messages sit where the reader meets them: `start.sgml:163-210` (four client errors with cause), `ddl.sgml` (6 transcripts), `typeconv.sgml` (4), `array.sgml` (2).
- Skill line: REF:13 ("Include the exact message text") and REF:38 ("List *all* error cases").

**C3. "One running domain across a doc set" holds inside a learning path, not across the whole set.**
- Evidence: tutorial and chapters do continue one domain (`query.sgml:117-123` weather/cities; `advanced.sgml:83-85` refers back; `dml.sgml:39` "consider the products table from ddl"). But `queries.sgml` switches to purpose-built tiny tables where the data has to be visible (`t1`/`t2` at `:414-430`, `test1` at `:1062`, `items_sold` at `:1242`), and the reference pages use their own self-contained domain (films/distributors at `ref/insert.sgml:694`, `ref/select.sgml:1767`).
- Skill line: SKILL:46 ("Use one running domain across a doc set").

**C4. A tutorial may show alternatives when readers will meet all of them in real code; the rule is to label which to prefer, not to hide the others.**
- Evidence: `query.sgml:228-243` shows three INSERT forms and says explicit columns is better style; `query.sgml:544-553` shows the older join form beside the newer one, says they give identical results and why the explicit one reads better; `query.sgml:303-309` footnotes that `SELECT *` is poor style in production code.
- Skill line: SKILL:26 (tutorial tone "no choices") and TEACH:23 ("Remove ... alternative approaches ... Choices belong in how-to guides").

**C5. Version mentions in prose are not the rot risk; unanchored time words are.**
- Evidence: dated notes set apart in callouts say what changed and what to do: `syntax.sgml:1131-1145` (precedence changed before 9.5; "no behavioral change, or perhaps 'no such operator' failures ... resolved by adding parentheses"), `typeconv.sgml:1252-1258`, `ref/select.sgml:375-377`, `:1185-1190`. The rot lives in sentences like the "Currently" ones (see G4-5).
- Skill line: SKILL:70 ("hard-coded versions in prose").

## 3. House convention

- Compatibility sections framed around the SQL standard and other database products; "extension" labels (`ref/select.sgml:2195-2211`). The principle is M2; the standard itself is domain-specific.
- Synopsis notation with `[ ]`, `{ | }` and `...` (`ref/select.sgml:35-82`), and the Name/Synopsis/Description/Parameters/Outputs section names (`docguide.sgml:486-664`), which suit a command language and man pages.
- Interactive-client transcripts (`mydb=>` prompts, backslash commands, `\i basics.sql`) and shipped tutorial scripts (`start.sgml:154-170`, `query.sgml:27-54`).
- DocBook markup: `refentry`/`refsect1`, `xref` ids, `indexterm`, and `.sgml` files that are actually XML (`docguide.sgml:438-443`).

## 4. Where the PostgreSQL manual falls short

**G4-1. Lessons use data the reader cannot create from the text.** `advanced.sgml:25-26` says the sample data is in a script and "is not repeated here"; the window-function examples then query `empsalary` (`:354-372`) with no way to build it in-page. Skill: SKILL:66 (no step missing), TEACH:17.

**G4-2. Recovery is delegated.** `start.sgml:171-173` ("Contact your site administrator or check the installation instructions") and `:47-48` after showing the failure text. Skill: TEACH:18 (say how to fix it, right there).

**G4-3. Hard-coded environment output goes stale.** `start.sgml:365` prints a compiler string for an old distribution and `:371` prints `2016-01-07` as the current date. Skill: SKILL:53, SKILL:70.

**G4-4. Jokes and filler a non-native reader trips on.** `dml.sgml:260` ("Caveat programmer."), `query.sgml:147-149` ("you choose"), `ddl.sgml:81,104,2289` (aptly/fittingly named; "Of course, ... heavily contrived"), `docguide.sgml:63` ("for your online reading pleasure"). A filler-word pattern (of course, obviously, simply, trivial, easy, easily) matches 26 times across `start`, `query`, `advanced`, `ddl`, `dml` (17 in `ddl`); some matches are neutral. Skill: SKILL:41, SKILL:54.

**G4-5. "Currently" with no version.** 24 matches of currently/Currently in the six reference pages (`select` 9, `create_index` 6, `create_table` 5). The sentence "Currently, FOR NO KEY UPDATE ... cannot be specified with" is repeated seven times in `ref/select.sgml` (`:866,909,1100,1233,1285,1333,1377`). Skill: REF:16 and REF:39 (version or date), SKILL:70.

**G4-6. Parameter entries that restate the name.** `ref/create_index.sgml:253` ("The name of a column of the table."), `:378` ("The constraint expression for a partial index."), `ref/create_table.sgml:297` ("The name of a column to be created in the new table."). Skill: REF:37.

**G4-7. The one tutorial exercise has no checkable outcome.** `query.sgml:593-599`: "Try to find out what those do." No expected result, no solution. Skill: TEACH:33.

**G4-8. Near-verbatim paragraph copied between chapter and reference.** The LIMIT paragraph ending "will give inconsistent results unless you enforce a predictable result ordering" is nearly identical at `queries.sgml:1957-1963` and `ref/select.sgml:1549-1556`. Copies drift; M7 says to repeat the trap, but rewritten per page. Skill: SKILL:70 ("duplicated"), REF:23.

## Confirmed by the manual (one line each)

- REF:21 "Sameness is the feature": all six pages share one order, Description, Parameters, (Outputs), (Notes), Examples, Compatibility, (See Also); `docguide.sgml:488` adds "sections that do not apply can be omitted".
- REF:23 "once ... and link": the RETURNING list syntax is defined by pointing to the SELECT output list (`ref/insert.sgml:97`, `update.sgml:62`, `delete.sgml:63`), WITH is delegated to the chapter and SELECT page in all three (`insert.sgml:160`, `update.sgml:86`, `delete.sgml:86`), and `ref/delete.sgml:310-313` reuses UPDATE's batching recipe by linking to its paragraph (`update.sgml:480`).
- REF:29 "generate where possible": `docguide.sgml:498` says the Name section "is generated automatically".
- SKILL:45 exact error strings in the text: `start.sgml:163,179,190,210` quote four client errors verbatim.

## Observed, not counted

Several pages combine explanation, how-to and reference.
- Inside reference pages: `ref/select.sgml:91-208` opens Description with an ordered account of how the command is processed (explanation); `ref/create_index.sgml:598-710` puts a multi-paragraph account of how concurrent builds work, how they fail and how to recover (explanation plus how-to) inside the Parameters section; `ref/update.sgml:480-518` and `ref/delete.sgml:309-329` put a batching recipe (how-to) in Examples; `ref/insert.sgml:370-641` carries a concept subsection on conflict targets.
- Inside chapters: `ddl.sgml:2314-2822` is a full privilege catalogue and two lookup tables (reference) in the middle of a teaching chapter; `datatype.sgml` opens with a table of all types.
- Where the docs keep modes apart: three book parts (tutorial `start`/`query`/`advanced`, which hold no option catalogues; SQL-language chapters; command reference pages). `func/func-string.sgml:36-536` and `:549-1614` are pure lookup tables of signature, description and example, with the one explanatory subsection placed after them under its own heading (`:1635-1842`). In the reference pages each mode sits in its own labelled section in a fixed position (Description, Parameters, Notes, Examples), so a reader can skip it by heading.
- Skill rule differed from: SKILL:13 ("Mixing modes is the most common structural failure"), SKILL:31 ("a reference that tells a story has become an explanation ... Link between modes instead of merging them"), SKILL:69, and REF:5 ("no narrative").
- Counted as a correction? No. The manual does not refute the skill's concern, that a reader cannot tell what they are reading; labelled, fixed-position sections meet it. The word "page" in those rules is stricter than the practice, but I would only reword it, not correct it.

## Abstracted

**Missed principles**

1. When a lesson or guide leaves a feature out on purpose, say so in one sentence at that spot and link to the exact section holding the rest. Teaching material may skip whole features, but never silently. Also tell experienced readers which sections to read closely because their habits will mislead them, and tell newcomers what they may skip.
2. Give every documented unit a fixed place that records where its behaviour departs from conventions readers bring from standards or neighbouring tools, and warn explicitly where a habit from elsewhere will quietly do something different.
3. Build reference examples as a catalogue: one per distinct form or option, each introduced by a plain sentence stating its goal, each runnable on its own, ordered from the plain case to the subtle one. One or two examples per entry is too few when an entry has many forms.
4. In examples, show the starting data, the statement and the exact result together, so the reader can verify the result by hand without guessing at inputs.
5. Show the tempting wrong form next to the right one, mark it plainly in the code, and say in the next sentence why it fails. Do this in reference and guide material too, not only in lessons.
6. When an outcome is decided by layered rules, write the rules as an ordered procedure with the tie-break order explicit, then give worked examples that name the step that decided each result.
7. Keep shared machinery in one place and link to it, but repeat the costliest trap wherever a reader first meets the feature, in a length suited to that page: a clause in a lesson, a paragraph in a guide, an exact rule in reference. Rewrite it for each page instead of pasting the same text.
8. Match the layout conventions of the tools your readers already use, not only the conventions of your own doc set, so lookup habits transfer.

**Corrections**

1. Reference voice should be neutral by default, but a short piece of advice with its reason belongs beside the rule it qualifies, in a labelled notes or tip area. Sending the reader to a separate guide for every "prefer this" costs more than it saves.
2. Do not promise an exhaustive error list with exact message text in reference. Document the conditions that change what the reader must do or that will surprise them, including cases that look like failures but are not, at the rule where they arise and with the stable code. Put verbatim message text where readers meet it, in lessons and troubleshooting.
3. Keep one running example domain within a learning path. When a concept needs specific data, use a small purpose-built dataset shown inline. Make reference examples self-contained so they do not depend on the lesson's data.
4. A lesson may show alternatives when readers will meet all of them in real code, as long as each is labelled with which to prefer and why and none derails the main path. "No choices" applies to the path the learner follows, not to what they are told exists.
5. Mentioning versions in prose is acceptable and useful when the note says what changed and what an upgrader should do, set apart beside the rule it affects. The real rot risk is time-relative wording such as "currently" or "new" with no version attached; avoid that.
