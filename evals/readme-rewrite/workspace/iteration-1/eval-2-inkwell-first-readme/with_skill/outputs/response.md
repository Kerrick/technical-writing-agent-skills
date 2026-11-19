I wrote `README.md` at `evals/readme-rewrite/files/inkwell/README.md`. I based it only on the code. I ran both examples in it through `uv` against the real package and pasted the actual output.

**One decision for you before you publish:** the README has no AI disclosure section, because nothing here shows who wrote inkwell's code. If an agent built it with little review from you, I'd add your usual "How this was made" section. It would say the code, the docs, and this README were requested, and link the declare-ai level "total". This README was written by an agent, so the section belongs there in any case. Tell me which labels fit the code and I'll add it.

**Where the code and the package metadata disagree:**
- **"Self-contained":** `pyproject.toml` says "tidy, self-contained HTML," but `render()` only wraps markdown-it-py's output in a bare page. There's no CSS, no `<meta charset>`, and images stay links to their files. The README says "a complete HTML page" and lists these gaps under Compatibility. You may want to change the PyPI description to match.
- **Unescaped input:** `render()` doesn't escape `title`, and raw HTML in the Markdown goes straight into the page. Passing `title="A & <B>"` puts that text into `<title>` as written. The README warns readers not to pass untrusted text without sanitizing it.
- **No GitHub extensions:** markdown-it-py's default CommonMark mode is in use, so tables, `~~strikethrough~~` and bare URLs come out as plain text. The README says so.
- **PDF export:** `export_pdf()` is listed in `__all__`, but it raises `NotImplementedError`. The README says PDF export isn't available yet.

**Calls I made that you can overturn:**
- **No screenshot:** `docs/demo.png` is a text placeholder, not an image, so I didn't embed it.
- **Absolute links:** all links are full URLs so they work on PyPI. They assume the repo is `github.com/example/inkwell` (from `pyproject.toml`) and that the default branch is `main`. I couldn't check either one. If `example` is a stand-in, the issues, license and badge links will break.
- **Badges:** I used PyPI version, Python version and license badges. They show real values only once `inkwell-md` is on PyPI. There's no CI badge because the project has no CI config and no tests.
- **No Contributing or Documentation section:** the project has no CONTRIBUTING file and no docs to point to. The Reporting problems section links to the issue tracker.
- **License wording:** the License section says Apache 2.0 allows commercial and closed-source use, and that it doesn't cover pages people make with inkwell. That's standard Apache 2.0. Your `LICENSE` file has its full text cut out, so I couldn't check it against your copy.

I couldn't check whether the external links resolve, because this session had no web access.