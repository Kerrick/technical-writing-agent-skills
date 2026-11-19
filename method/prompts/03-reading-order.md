# 3. Reading order

The first message to each reading fork. A Sonnet sub-agent finds the files in reading order, so the fork's own context holds only the pages, read once.

```
Now, send a Sonnet sub-agent out to ${REPO_PATH} to give you the ${EXTENSION} filenames to read, in the correct order, and nothing more, so you can read them all and have read everything a human would've read by ${READING_PATH}.
```

`${READING_PATH}` names the path a reader actually takes, such as "clicking Learn and going page-by-page on react.dev". `uv run method/scripts/prompt.py reading --source <key> --src ${SRC}` prints each source's filled-in prompt from [sources.toml](../sources.toml), and its list check.

Before the fork starts reading, check the list it gets back: the right folder (not old versions), the expected count, and no sections that were meant to be skipped. Correct the list before anything is read, not after.
