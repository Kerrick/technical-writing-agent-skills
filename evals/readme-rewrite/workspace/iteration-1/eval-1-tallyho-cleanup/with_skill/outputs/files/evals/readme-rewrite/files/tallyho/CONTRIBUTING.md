# Contributing to tallyho

## Running the tests

The tests use [pytest](https://docs.pytest.org/) and live in `tests/`. Install tallyho in editable mode with pytest in a virtual environment, then run pytest from the repository root:

```console
$ pip install -e . pytest
$ pytest
```

## Releasing a new version

1. Bump `version` in `pyproject.toml`.
2. Tag the commit with the new version.
3. Push the tag.
