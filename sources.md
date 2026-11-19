# Sources

Seven documentation sets, chosen to differ in kind: framework guides with tutorials (A, B, D), a strict tutorial/topic/how-to/reference split (C), a book (E), reference and guides by many writers (F), and deep reference for a language with no framework (G). Keep the sources, scopes and commits fixed when repeating the method for another model, so the only thing that changes is the model.

| Letter | Source | Repository | Commit | Findings file |
| - | - | - | - | - |
| A | React Learn | `reactjs/react.dev` | `54cd2c40` | `react-learn.md` |
| B | Ember Guides | `ember-learn/guides-source` | `919777db2` | `ember-guides.md` |
| C | Django docs | `django/django` | `9e2e5a3` | `django-docs.md` |
| D | Rails Guides | `rails/rails` | `f12b615` | `rails-guides-1.md`, `rails-guides-2.md` |
| E | The Rust Programming Language | `rust-lang/book` | `9be0936` | `rust-book.md` |
| F | MDN JavaScript Guide and reference | `mdn/content` | `54ef250b` | `mdn-js-guide.md` |
| G | PostgreSQL manual | `postgres/postgres` | `8303f2e` | `postgres-manual.md` |

Letters are the anonymous labels used from the audit onward. Clone each repository into `~/Developer/` and check out the commit.

## Budget

One fork holds about 1.2–1.5 MB of source text. React Learn (1.45 MB) fit with room to compare. Rails (about 1.9 MB) and the first PostgreSQL attempt both hit the context limit and crashed. Measure a scope before a fork reads it, and split or narrow it if it's over about 1.2 MB. Never compact a reading fork: the comparison needs exact wording for evidence. Rewind to the reading-order message instead, narrow the scope, and fork again.

## Per source

### A: React Learn

- **Reading path:** "clicking Learn and going page-by-page on react.dev". The Learn section in Next-button order, 51 pages, about 1.45 MB.
- **Style guide:** `CONTRIBUTING.md`, sections "Technical Writing Tips", "Guidelines for Text" and "Guidelines for Code Examples".
- **House:** React, react.dev's interactive sandboxes, or its audience.
- **Names to exclude from Abstracted:** React, react.dev.
- **License:** CC BY 4.0 (`LICENSE-DOCS.md`).

### B: Ember Guides

- **Reading path:** "clicking Getting Started and going page-by-page on guides.emberjs.com/release". Only `guides/release/`, in `pages.yml` order: 127 pages, about 0.96 MB. The repo has 95 other folders for older versions; the list must not include them. Skip redirect stubs (about 57 bytes each). It found 62 files the table of contents never links to, and correctly didn't read them.
- **Style guide:** `CONTRIBUTING.md`, sections "Style Guide" and "Writing". Mostly formatting, so expect more findings inferred from the pages than stated intent.
- **House:** Ember, its tooling or its tutorial app, or the guides' audience.
- **Names to exclude:** Ember, the Ember Guides.
- **License:** MIT.

### C: Django docs

The reading-order prompt as sent (it says `.md`, though Django's docs are `.txt`; the sub-agent found them anyway):

```
Now, send a Sonnet sub-agent out to ~/Developer/django/docs/ to give you the .md filenames to read, in the correct order, and nothing more, so you can read them all and have read everything a human would've read by clicking Documentation and going page-by-page on docs.djangoproject.com.
```

The sub-agent returned 681 files, about 6.5 MB, and the fork asked how to proceed. Django has no single reading path beyond the tutorial, and its docs (4.9 MB without release notes) are about four forks' worth. The fork read a fixed sample instead, given as its answer:

```
None of these. Read about 1.1 MB, in this order, in full:

1. index.txt
2. All of intro/ (the tutorial and the overview), in the order the tutorial's "next" links follow
3. All of howto/, in the order of howto/index.txt
4. topics/forms/ and ref/forms/, in the order of their index files: one feature followed from its topic guide into its reference pages
5. topics/http/ and ref/request-response.txt: a second feature followed the same way
6. All of faq/
7. internals/contributing/writing-documentation.txt last: it's Django's own documentation style guide

Skip releases/, the rest of topics/ and ref/, misc/ and the rest of internals/.
```

- **Style guide:** `docs/internals/contributing/writing-documentation.txt`, read as part of the pages.
- **Focus:** "Pay particular attention to how one feature is split across the tutorial, topic guide, how-to and reference pages: what each kind of page includes, leaves out, and links to."
- **House:** Django, Python or reStructuredText and Sphinx, or the docs' audience.
- **Names to exclude:** Django, Python, the Django docs.
- **License:** BSD 3-clause (`LICENSE`).

### D: Rails Guides

Too big for one fork (3.2 MB, 2.4 MB without release notes). The first attempt crashed at guide 36. Split into two forks by `guides/source/documents.yaml` section, skipping Release Notes, Policies and work-in-progress guides. Both halves are one source.

- **D1 reading path:** "going page-by-page through the Start Here, Models, Routing and Controllers, Views, and Other Components sections of the Rails Guides index (the order in documents.yaml), skipping work-in-progress guides". 23 guides, about 1.22 MB.
- **D2 reading path:** the same, for "Digging Deeper, Going to Production, Advanced Active Record, Extending Rails, and Contributing". 26 guides, about 1.15 MB. D2 reads both style guides as part of Contributing.
- **Style guides:** the "Guidelines" section of `guides/source/ruby_on_rails_guides_guidelines.md` (skip "HTML Guides" and "EPUB Guides", which cover the build), and all of `guides/source/api_documentation_guidelines.md`.
- **House:** Rails, Ruby or RDoc, or the guides' audience.
- **Names to exclude:** Rails, Ruby, the Rails guides.
- **License:** CC BY-SA 4.0. Share-alike: quote rarely.
- **D2 extra:** "I'm not asking you to make it follow Rails conventions; I'm asking what the Rails guides know that it doesn't."

### E: The Rust Programming Language

- **Reading path:** "going page-by-page on doc.rust-lang.org/book", with `~/Developer/book/src/` as the folder. The fork read all 112 files, from the title page through Appendix G. About 1.22 MB.
- **Listings:** the chapters pull in about 0.30 MB of code and compiler output (669 files under `listings/`) at build time. Don't read them all. Prefix the comparison with: "Don't read all the listings. Where a difference you're about to record depends on what a listing or its output.txt actually shows, open that one listing (or grep across ~/Developer/book/listings/) to check, and cite it. Otherwise work from the prose."
- **Style guide:** `style-guide.md` and `CONTRIBUTING.md`.
- **Focus:** "The book is long-form, which the skill covers in references/books.md and references/learning-science.md. Pay particular attention to how it differs from those files."
- **House:** Rust, its tooling (Cargo, rustc, mdBook), or the book's audience.
- **Names to exclude:** Rust, Cargo, the Rust book.
- **License:** MIT and Apache-2.0, dual-licensed.

### F: MDN JavaScript Guide and reference

- **Reading path:** "going page-by-page on developer.mozilla.org/en-US/docs/Web/JavaScript/Guide", from `files/en-us/web/javascript/guide/`. 38 pages in sidebar order. Then, before comparing:

  ```
  Before comparing, read two more parts of MDN in full, so you've seen its reference pages as well as its Guide:

  1. Every page under ~/Developer/content/files/en-us/web/javascript/reference/global_objects/promise/, starting with index.md, then the constructor, static methods, and instance methods in the order index.md lists them.
  2. The same for ~/Developer/content/files/en-us/web/javascript/reference/global_objects/map/.
  3. These templates from ~/Developer/content/files/en-us/mdn/writing_guidelines/page_structures/page_types/: javascript_class_page_template, javascript_constructor_page_template, javascript_static_method_page_template, javascript_instance_method_page_template (each is index.md in that folder).

  Read them in full; then wait for my next message.
  ```

- **Style guide:** in `files/en-us/mdn/writing_guidelines/`: `index.md`, `what_we_write/index.md`, `writing_style_guide/index.md`, `code_style_guide/index.md`, `code_style_guide/javascript/index.md`, `page_structures/code_examples/index.md`, `page_structures/page_types/index.md`. Skip the rest, which is mostly templates for reference pages.
- **Focus:** "MDN is written by many contributors under one style guide. Note where that shows: what the style guide succeeds in keeping consistent, and what it doesn't. Compare how the Guide and the reference pages handle the same concepts, and what each kind of page leaves to the other."
- **House:** MDN, JavaScript or the web platform, MDN's macros and live samples, or its audience.
- **Names to exclude:** MDN, JavaScript, the web platform.
- **License:** CC BY-SA 2.5. Share-alike: quote rarely.

### G: PostgreSQL manual

The first attempt (all of Part I and Part II) crashed in the function reference tables (`func/`, 1.2 MB). The second used a fixed scope in `doc/src/sgml/`, about 1.1 MB:

```
Now, send a Sonnet sub-agent out to ~/Developer/postgres/doc/src/sgml/ to give you the .sgml filenames to read, in the correct order, and nothing more, so you can read everything a human would've read by going page-by-page on postgresql.org/docs/current through these parts only: the tutorial (start, query, advanced), then the SQL Language chapters syntax, ddl, dml, queries, datatype (with the files it includes: json, array, rowtypes, rangetypes, in the order it includes them), typeconv, indices and mvcc. Then add exactly one function section, func/func-string.sgml, as a sample of the reference tables, and docguide.sgml last; it's the documentation style guide. Skip the rest of func/, textsearch and perform.
```

Then, with room left, before comparing:

```
Don't fold anything into the skill; I'll explain why in my next message. First read these SQL command reference pages in full, in this order, from ~/Developer/postgres/doc/src/sgml/ref/: select.sgml, insert.sgml, update.sgml, delete.sgml, create_table.sgml, create_index.sgml. Each covers a command a chapter you've read already taught, so notice how the reference page and the chapter divide the work. Then wait for my next message.
```

- **Style guide:** `docguide.sgml`, read as part of the pages.
- **Focus:** "Pay particular attention to how each command is split between its chapter and its reference page: what each includes, leaves out, and links to."
- **House:** PostgreSQL, SQL or psql, DocBook/SGML, or the manual's audience.
- **Names to exclude:** PostgreSQL, SQL, psql.
- **License:** the PostgreSQL License, permissive and BSD-style (`COPYRIGHT`).
