# tallyho

Count the most common words in text files.

tallyho is a command-line tool and Python library for people who want to know which words a piece of text uses most: a writer checking a draft for overused words, or a developer taking a first look at a corpus. You give it one or more text files, and it prints the words that appear most often, with their counts, most common first.

You can get the same answer from a shell pipeline such as `tr -cs "A-Za-z'" '\n' < file.txt | tr A-Z a-z | sort | uniq -c | sort -rn | head`. tallyho does those steps in one command, needs only Python rather than a Unix shell, and gives you the counts as a Python list if you call it from code. [`wc`](https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html) counts the total words in a file, but not how often each word appears.

## Example

`story.txt` holds two lines:

```text
The cat sat on the mat.
The dog didn't sit on the cat.
```

```console
$ tallyho --limit 3 story.txt
     4  the
     2  cat
     2  on
```

Each line shows a count, then the word. tallyho lowercases every word before it counts, so "The" and "the" count as one word.

## Compatibility

| Requirement | Version |
| - | - |
| [Python](https://www.python.org/) | 3.11 or later |
| Operating system | Any that runs Python 3.11 |

tallyho has no dependencies outside the Python standard library.

## Installation

From a copy of this repository, install it with [pip](https://pip.pypa.io/):

```console
$ pip install .
```

This puts the `tallyho` command on your `PATH`. To install it as a standalone tool, away from your other Python packages, use [pipx](https://pipx.pypa.io/) instead: `pipx install .`

## Usage

### On the command line

```console
$ tallyho [--limit N] FILE [FILE ...]
```

- `FILE`: one or more text files to read, encoded as UTF-8. Required. tallyho counts the words in all of them together and prints one combined list.
- `--limit N`: how many words to show. Optional. The default is 10.

To see the 25 most common words across two chapters:

```console
$ tallyho --limit 25 chapter1.txt chapter2.txt
```

Run `tallyho --help` to see the options.

### From Python

Call `count_words` with a string. It returns a list of `(word, count)` pairs, most common first:

```python
>>> from tallyho import count_words
>>> count_words("b a b c b a", limit=2)
[('b', 3), ('a', 2)]
```

`limit` is optional and defaults to 10.

## How words are counted

- tallyho lowercases the text, then treats each run of the letters `a` to `z` and apostrophes as one word. "Didn't" is one word.
- Everything else splits words and is not counted, including digits, hyphens, and accented letters. "Well-known" counts as "well" and "known", and "café" counts as "caf".
- When two words have the same count, the one that appears first in the text is listed first.

## Reporting problems

To report a bug or ask for a feature, open an issue in this project's repository. Include the command you ran, what it printed, and, if you can, a short text file that shows the problem.

## Contributing

To run the tests or cut a release, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

tallyho is released under the [MIT License](LICENSE). You can use, copy, change, and share it, including in commercial work, as long as you include the license notice. The license covers tallyho itself, not the text you count with it or the results it prints.
