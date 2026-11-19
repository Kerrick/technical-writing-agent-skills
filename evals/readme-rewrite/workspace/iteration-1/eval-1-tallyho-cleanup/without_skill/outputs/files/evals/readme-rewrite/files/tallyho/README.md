# tallyho

Count the most common words in text files.

## Install

Requires Python 3.11 or later.

```sh
pip install tallyho
```

## Usage

```sh
tallyho notes.txt
tallyho --limit 5 chapter1.txt chapter2.txt
```

tallyho reads every file you pass it and prints the most common words with their counts, most common first:

```
     2  the
     2  cat
     2  sat
```

| Option        | Default | Description             |
| ------------- | ------- | ----------------------- |
| `--limit N`   | 10      | How many words to show. |

Words are lowercased and made of letters and apostrophes, so `The` and `the` count as the same word and `don't` counts as one word. Words with the same count are listed in the order they first appear in the input.

### From Python

```python
from tallyho import count_words

count_words("b a b c b a", limit=2)  # [("b", 3), ("a", 2)]
```

## Development

Run the tests with `pytest` from the repo root. CI runs them on every push.

To release, bump `version` in `pyproject.toml`, tag the commit, and push the tag. The release workflow handles the rest.

## License

MIT. See [LICENSE](LICENSE).
