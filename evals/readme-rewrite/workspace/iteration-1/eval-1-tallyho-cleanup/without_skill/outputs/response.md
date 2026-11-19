I rewrote `README.md` around what a user needs: what tallyho does, how to install it, how to use it, then development notes and the license. The dated "Update" sections are gone, and what they said is now part of the normal sections.

When I compared the old README with the code, three things in it were wrong, so I fixed them:

- **Wrong flag name:** the README said `--top`, but the CLI's flag is `--limit` (default 10). Anyone copying the old example would have gotten an error.
- **Wrong Python version:** the README said Python 3.8+, but `pyproject.toml` requires 3.11 or later.
- **Missing tie-breaking info:** the README pointed to "ADR 3" for how ties are broken, but there's no such file in the repo. I replaced the reference with the actual behavior: words with the same count are listed in the order they first appear.

Other changes:
- I cut the "most powerful way to count words" line and replaced it with the one-line description from `pyproject.toml`.
- I cut the "latest version is 0.4.0" note, since it will go out of date and `pyproject.toml` or PyPI already has the version.
- I added an example of the output, made by running `count_words` on a sample sentence.
- I added a short options table, explained what counts as a word, and added an example of calling it from Python (the same case as the test).
- I added a License section.

I kept the testing and release steps but moved them under "Development". There's no CI config or release workflow file in this directory, so please check that those instructions still match your setup.