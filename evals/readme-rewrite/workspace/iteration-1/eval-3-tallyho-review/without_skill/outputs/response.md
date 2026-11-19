I checked the README against the code in `src/`, `pyproject.toml` and the tests. I haven't changed anything.

## Wrong: these contradict the code

1. **The usage example fails.** `README.md:11` shows `tallyho --top 5 notes.txt`, but the CLI has no `--top` flag. It's `--limit` (`cli.py:10`), so argparse rejects the command. The update note on line 15 ("Added the --top flag") is wrong for the same reason.
2. **Wrong Python version.** Line 7 says "needs Python 3.8+", but `pyproject.toml:5` says `requires-python = ">=3.11"`. Anyone on 3.8–3.10 will be told by pip that it can't install.
3. **The tie-breaking note points nowhere.** "The counter decides how to break ties (see ADR 3)": there's no ADR in the repo. Tied words actually come out in the order they first appear, which is how `Counter.most_common` works. The README should just say that.

## Can't confirm from the repo

4. **CI and release.** "CI runs it on every push" and "the workflow handles the rest" both assume a CI workflow, but there's no `.github/` or other CI config here. It may live elsewhere, but as written it can't be checked.
5. **"Run `pytest` from the repo root" won't work on a fresh clone.** The package uses a `src/` layout, so the tests can't import `tallyho` until it's installed. The steps need a `pip install -e .` (or similar) first.

## Structure and content

6. **Marketing language instead of a description.** "honestly the most powerful way to count words — it's fast and lightweight" is hype with nothing behind it. `pyproject.toml` already has the plain version: "Count the most common words in text files."
7. **Changelog entries in the README.** The "Update 2026-03-02" and "Update 2026-05-19" sections belong in a CHANGELOG or release notes. "The latest version is 0.4.0" will go stale with the next release.
8. **Odd order and mixed readers.** Maintainer content (release steps) sits between user content, and the dated updates are scattered. A clearer order is: what it is → install → usage → contributing/tests → release.
9. **Missing things a user needs:**
   - What the output looks like (right-aligned count, two spaces, then the word).
   - That `--limit` defaults to 10.
   - That it accepts several files.
   - That it lowercases text and only counts `[a-z']`. Digits and accented or non-Latin letters are silently dropped, which is a big caveat for a word counter.
   - That `count_words` can be imported as a library.
   - The license (MIT).
10. **Formatting.** The install command is plain prose, not in a code block, so it's hard to copy.

## Outside the README

- **Multi-file bug:** `cli.py:12` joins file contents with `""`. If one file doesn't end in a newline, its last word merges with the first word of the next file. If the README documents multi-file use, this should be fixed (join with `"\n"`) or the README will be describing buggy behaviour.
- **License text:** `LICENSE` isn't the real MIT text. It's a one-sentence paraphrase without the warranty disclaimer, so calling it "MIT" is shaky.

I can do the rewrite next if you'd like. Items 1–3 are the most urgent because they're actually wrong.