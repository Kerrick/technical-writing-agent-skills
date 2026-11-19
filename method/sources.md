# Sources

Seven documentation sets, chosen to differ in kind: framework guides with tutorials (A, B, D), a strict tutorial/topic/how-to/reference split (C), a book (E), reference and guides by many writers (F), and deep reference for a language with no framework (G). Keep the sources, scopes and commits fixed when repeating the method for another model, so the only thing that changes is the model.

Everything a prompt needs (repository, commit, paths, reading prompt, style guide, license and the rest) is in [`sources.toml`](sources.toml). `method/scripts/fetch_sources.py` clones from it and `method/scripts/prompt.py` fills prompts from it. This file explains the choices.

| Letter | Source | Repository | Findings file |
| - | - | - | - |
| A | React Learn | `reactjs/react.dev` | `react-learn.md` |
| B | Ember Guides | `ember-learn/guides-source` | `ember-guides.md` |
| C | Django docs | `django/django` | `django-docs.md` |
| D | Rails Guides | `rails/rails` | `rails-guides-1.md`, `rails-guides-2.md` |
| E | The Rust Programming Language | `rust-lang/book` | `rust-book.md` |
| F | MDN JavaScript Guide and reference | `mdn/content` | `mdn-js-guide.md` |
| G | PostgreSQL manual | `postgres/postgres` | `postgres-manual.md` |

Letters are the anonymous labels used from the audit onward.

## Budget

A reading fork needs room for its pages and then for the comparison. In the first run, with a 1M-token window, about 1.2–1.5 MB of source fit: React Learn (1.45 MB) did, while Rails (about 1.9 MB) and the first PostgreSQL attempt crashed. The scopes in `sources.toml` are sized for that window. On a smaller one, measure the fork point's context use and narrow or split scopes to fit, and record the change in your run's README.

Never compact a reading fork: the comparison needs exact wording for evidence. If one runs out of room, rewind to the reading-order message, narrow the scope, and fork again.

## Why each scope is what it is

- **A, React Learn:** the whole Learn section, in Next-button order. About 1.45 MB.
- **B, Ember Guides:** only `guides/release/`. The repo also has 95 folders of older versions, which the file list must not include. Pages that the table of contents never links to (62 in the first run) aren't read, because a reader clicking through never reaches them.
- **C, Django docs:** a fixed sample. Django has no single reading path beyond its tutorial, and its docs (4.9 MB without release notes) are about four forks' worth. The sample keeps the tutorial and how-tos whole, and follows two features (forms, and request handling) from their topic guides into their reference pages, which is what Django has that the other sources don't: a strict split of one feature across kinds of page. The first run's fork asked for this scope after its file list came back at 6.5 MB; `sources.toml` puts it in the reading prompt directly.
- **D, Rails Guides:** two forks, split by `documents.yaml` section, skipping Release Notes, Policies and work-in-progress guides. All of it (3.2 MB) is too big for one fork; the first run's single attempt crashed at guide 36. The second half reads both Rails documentation style guides as part of its Contributing section.
- **E, The Rust book:** every chapter. Its listings (about 0.30 MB of code and compiler output under `listings/`) aren't read in full; the fork opens one only when a finding depends on it.
- **F, MDN:** the JavaScript Guide, then the Promise and Map reference pages and their page templates. The reference pages are what MDN is best known for, and the Guide alone wouldn't show them; the HTML and CSS guides were left out because they'd repeat the JavaScript Guide's style, writers and mode.
- **G, PostgreSQL manual:** the tutorial and the SQL Language chapters, one sample of the function reference tables (`func/func-string.sgml`), the documentation style guide, and six SQL command reference pages, each paired with a chapter that teaches the same command. The first run's first attempt read all of Parts I and II and crashed in the function tables (`func/`, 1.2 MB of near-identical tables).
