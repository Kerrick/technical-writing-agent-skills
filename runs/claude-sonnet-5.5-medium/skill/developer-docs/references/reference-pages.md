# Reference pages

Read this before writing or editing a lookup page: an API, option, command or configuration reference, or a troubleshooting page. Rules in SKILL.md apply as well.

## Keep reference neutral, with advice beside the item

Keep reference free of persuasion and vendor claims. Where a wrong choice is costly or non-obvious, put a short, plain recommendation or verdict with its reason right beside the option or rule it qualifies, inline or in a tip: "rarely appropriate", "use X instead". Do not move such a warning to a guide. A reader who lands from search must see it at the point of error.

## Scale examples to the entry

- A thin entry (only a signature or an option list) may carry no example of its own. Point to the worked example in a guide, and say so.
- Give an example wherever behaviour is surprising.
- An entry with many forms or options gets one example per distinct form, not just one or two.

## Errors: contract errors and decision-changing conditions

Document the errors and conditions that belong to the feature's own contract and change what the reader must do, including cases that look like failures but are not.

- Don't promise an exhaustive list of every error.
- Leave out errors caused by caller-supplied code or wrong-typed arguments.
- Keep step-by-step fixes on a separate troubleshooting page.
- Put verbatim message text where readers meet it (lessons, guides, troubleshooting). The exception is a stable format that users parse: give that exactly.

## Be exact about the contract, not about incidental values

Say exactly what callers may rely on. List calls that terminate the program rather than return an error, and invariants the caller must uphold, separately from recoverable errors. Don't commit to exact incidental values you want the freedom to change.

## Gotchas

- Do not strip hazards out of reference to keep it neutral. The reader meets the trap with no warning.
- Do not pad a thin entry with a filler example, and do not give a rich entry only one or two.
- Do not list every conceivable error with its message text. It can't be maintained and buries the errors that matter.
- Do not document incidental behaviour as a promise, and do not omit the invariants a caller must keep.
