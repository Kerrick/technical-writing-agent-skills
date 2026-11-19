# Style mechanics

Use these when the project has no style guide of its own. If it has one, or a Vale config, follow that instead.

## Formatting

- **UI labels** in bold, matching the interface exactly, including case: Select **Save changes**.
- **Literal text** the reader types or sees (commands, file names, paths, keys, values, error text) in `code`.
- **Placeholders** in `UPPER_SNAKE_CASE` or `<angle-brackets>`, consistently, and say what to replace them with on first use.
- **Keyboard shortcuts**: <kbd>Ctrl</kbd>+<kbd>C</kbd> where supported, otherwise **Ctrl+C**. Give macOS and Windows/Linux variants.
- **Menus**: **File** > **Settings** > **Editor**.
- Don't use code formatting for product names or concepts.

## Links

- Link text says where it goes: "see [rate limits](…)", never "click [here](…)".
- Link a term at its first mention on the page, not every mention.
- Don't hide prerequisites behind links alone. State what's needed, then link how to get it.

## Numbers, dates, units

- Use numerals for numbers you'd measure or type (3 retries, 5 MB, version 2.1).
- Write dates unambiguously: 18 November 2026, or ISO 8601 (2026-11-18) in technical contexts. Never 11/18/26.
- Always give units, with a space: 30 s, 512 MB. Say whether a size is MB or MiB when it matters.

## Global English

Many readers use machine translation or English as a second language.

- Avoid idioms, sports and cultural metaphors, and humor that depends on wordplay.
- Keep *that* in "make sure that ..." and similar; it helps parsing.
- Avoid ambiguous pronouns. "It" with two possible referents is a bug.
- Define abbreviations on first use, except ubiquitous ones (API, URL, HTTP).
- Prefer short, common words: *use* over *utilize*, *start* over *initiate*, *help* over *facilitate*.

## Inclusive language

- *allowlist/denylist* not *whitelist/blacklist*; *primary/replica* or *leader/follower* not *master/slave* (unless it's a literal identifier, in which case put it in code formatting).
- *they* for an unspecified person.
- Avoid words that assume ability or ease: *simply*, *just*, *easy*, *sanity check*, *crazy*, *dummy value* (use *placeholder*).

## Accessibility

- Every meaningful image has alt text that says what it shows and why it's there; decorative images have empty alt text.
- Don't rely on color alone: "the red line" fails for some readers and in print.
- Tables have header rows; don't use tables for layout.
- Heading levels go in order without skipping, so screen-reader navigation works.
- Video has accurate captions and a transcript.

## Words to cut or replace

| Instead of | Write |
| - | - |
| in order to | to |
| utilize | use |
| leverage | use |
| it is possible to | you can |
| please | (omit in instructions) |
| click on | click, or select |
| e.g., i.e., etc. | for example, that is, and so on |
| via | through, by, using |
| should (for behavior) | will, or describe what happens |
