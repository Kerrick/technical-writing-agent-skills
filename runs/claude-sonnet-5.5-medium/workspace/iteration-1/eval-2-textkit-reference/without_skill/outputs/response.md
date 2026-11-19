I wrote the API reference page for textkit 0.9.2. It's a single file, `outputs/textkit-api-reference.md`.

It opens with a summary table. Each function then gets its own short section with signature, parameters, return value, errors and a one-line example. I put `make_slug` last, with a migration snippet to `slugify(..., sep="_")`.

- **Examples:** I traced them by hand against the source, since the sandbox blocked me from running the module. Please run them once before publishing.
- **Link placeholder:** The link to the 0.9 user guide is a `#` placeholder. Swap in the real URL.
- **`shorten` edge case:** When not even the first word fits, it returns the bare placeholder. That can be longer than `width` if `width` is under 3. I documented this rather than hiding it.