I rewrote `README.md` and moved the contributor notes into a new `CONTRIBUTING.md`. I couldn't run any of the commands: this session blocked me from creating a virtual environment, installing the package, or running `tallyho`. The example output in the README comes from reading the code, not from a run. Please run the example and `pytest` once before you publish.

**The new README** has these sections:
1. What tallyho is and how it compares with a shell pipeline and `wc`
2. A worked example with output
3. Compatibility (Python 3.11+)
4. Installation
5. Usage, for both the command line and Python
6. How words are counted
7. Reporting problems
8. Contributing
9. License

The "How words are counted" section comes from the regex in the code. Digits, hyphens and accented letters split words, so "café" counts as "caf". Ties are listed in the order the words first appear. The undated "Update" entries are gone.

**Removed as false:**
- **Python 3.8+:** `pyproject.toml` requires 3.11 or later.
- **The `--top` flag:** it doesn't exist. The flag is `--limit`.
- **"Honestly the most powerful… fast and lightweight":** nothing backs it.
- **"(see ADR 3)":** a reference to an internal record. The README now describes how ties are actually broken.
- **"The latest version is 0.4.0":** a version line goes stale. A version badge would replace it, but I found no package registry page to point one at.

**Moved to `CONTRIBUTING.md`:** how to run the tests and the release steps. I left out two claims I couldn't confirm. There's no CI or workflow file in the repository, so I dropped "CI runs it on every push" and "the workflow handles the rest." I also changed the test command to `pip install -e . pytest` before `pytest`. With the `src/` layout, a bare `pytest` probably can't import the package.

**Decisions you may want to change:**
- **Installation:** the README says to run `pip install .` from a copy of the repository, not `pip install tallyho`. Nothing in the repository shows tallyho is on PyPI, and `pyproject.toml` has no `[build-system]` table or project URLs. If it is on PyPI, switch the line back and add a version badge.
- **Reporting problems:** this section says "open an issue in this project's repository" without a link, because I found no repository URL.
- **No AI disclosure section.** Agents wrote this README, and your other projects use the wrote/wrought/requested section. I couldn't tell how the tallyho code was made. Unless you tell me otherwise, I'd add your standard section with "this README was requested" and leave the code's label to you.

**A bug in the code:** `cli.py` joins the files with `"".join(...)` and adds no separator. If a file doesn't end with a newline, its last word merges with the first word of the next file. Using `"\n".join` would fix it.