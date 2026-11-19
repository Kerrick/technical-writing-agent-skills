# API, CLI, and configuration reference

Reference is for lookup. The reader knows what they're looking for and wants it to be correct, complete, and in the same place as last time. Be austere and consistent: every entry of a kind has the same sections in the same order, even when a section is "None."

Generate the skeleton from the source of truth when one exists (OpenAPI, type signatures, docstrings, `--help`, a config schema), then write the descriptions by hand. Generated descriptions that restate the name ("`name`: the name") are worse than nothing because they look finished.

## Templates

### HTTP endpoint

````markdown
## Create an invoice

`POST /v2/invoices`

Creates a draft invoice for a customer. The invoice isn't sent until you
[finalize it](#finalize-an-invoice).

### Request body

| Field | Type | Required | Description |
| - | - | - | - |
| `customer_id` | string | Yes | ID of the customer to bill. |
| `currency` | string | No | Three-letter ISO 4217 code, lowercase. Defaults to the customer's currency. |
| `due_days` | integer | No | Days after finalization the invoice is due. 1–365. Defaults to `30`. |

### Example request

```bash
curl https://api.example.com/v2/invoices \
  -H "Authorization: Bearer $EXAMPLE_API_KEY" \
  -d customer_id=cus_8Hq2 \
  -d due_days=14
```

### Response

`201 Created` with the [invoice object](#the-invoice-object).

```json
{ "id": "inv_31Kd", "status": "draft", "customer_id": "cus_8Hq2", "due_days": 14 }
```

### Errors

| Status | Code | When | Fix |
| - | - | - | - |
| 404 | `customer_not_found` | `customer_id` doesn't exist in this account. | Check the ID, and that you're using the right account's key. |
| 422 | `invalid_due_days` | `due_days` is outside 1–365. | |
````

### Function or method

```markdown
## `Client#retry(attempts:, backoff: :exponential)`

Re-runs the last failed request up to `attempts` times.

**Parameters**
- `attempts` (Integer, required): maximum retries, 1–10.
- `backoff` (Symbol): `:exponential` (default) or `:linear`.

**Returns** the successful `Response`.

**Raises** `RetryExhausted` after the final attempt fails; its `#cause` is the last error.

**Example** ...

**Since** 2.3.0
```

### CLI command

Usage line, one-sentence description, arguments, options (each with type, default, and environment-variable equivalent if any), exit codes, and examples covering the common case first. Make it agree with `--help`.

### Configuration option

Key, type, default, allowed values, where it can be set (file, env var, flag) and which wins, whether it needs a restart, and an example.

## Writing each description

A good parameter or field description answers what a reader can't get from its name and type:

- What it does, and its effect on the result.
- Default, units, range, format, and allowed values.
- Interactions: "Ignored when `mode` is `async`."
- When you'd set it, if that's not obvious.

Start method and endpoint descriptions with a verb ("Creates," "Returns"). Follow the ecosystem's docstring convention where one exists: PEP 257 for Python, YARD or RDoc for Ruby, JSDoc or TSDoc for JavaScript, rustdoc for Rust, godoc for Go (which starts with the identifier's name).

## Cover cross-cutting topics once

Write one page each for authentication, errors and error format, pagination, rate limits, versioning, idempotency, and webhooks, and link to them from every entry they affect. Repeating them per entry drifts out of sync.

## Examples in reference

- Use realistic IDs and values in the API's real format, and make them consistent between request and response.
- Show the minimal call first; add a fuller example only when common options need it.
- Offer every SDK language the product supports, or none; a page with two of five languages looks broken.

## Change over time

- **Version** every entry that changed: "Since 2.3.0," "Changed in 3.0: now returns `nil` instead of raising."
- **Deprecation**: say what is deprecated, since when, what replaces it, and when it will be removed. Keep the entry until removal.
- **Changelog** entries describe the effect on users, not the commit. List breaking changes first, each with a migration step.
