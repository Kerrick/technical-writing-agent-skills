# Verify webhook signatures with hookshot

This guide shows how to check that a webhook request to your Flask app really came from the sender and wasn't altered or replayed. It applies to hookshot 3.4.0.

You'll end up with one Flask route that rejects any delivery that fails verification, plus tests that prove it works.

## Before you start

You need:

- Python 3.10 or later. `hookshot.sign()` uses the `int | None` annotation syntax.
- A Flask app. Any recent Flask 2.x or 3.x works. The `@app.post` shortcut used below needs Flask 2.0 or later.
- The signing secret for your webhook endpoint, from the sender's dashboard.

## Background: what a signature is

If you already hand-roll HMAC checks, skip to [Step 1](#step-1-store-the-secret).

A webhook is an HTTP `POST` that another service sends to a URL you control. Anyone who knows that URL can send requests to it, so you need a way to tell real deliveries from forged ones.

The sender and you share a secret string. For each delivery, the sender computes a signature from the secret and the request, and sends it in a header. You recompute the signature with the same secret. If your result matches the header, only someone holding the secret could have sent the request, and the body wasn't changed in transit.

hookshot checks deliveries signed like this:

- The header is `Hookshot-Signature: t=<unix seconds>,v1=<hex digest>`.
- The digest is HMAC-SHA256 over the timestamp, a literal `.`, and the **raw request body**, keyed with your secret.
- The timestamp is part of the signed data. An attacker can't replay an old, valid delivery with a fresh timestamp, because changing the timestamp breaks the signature.

You don't need to implement any of this yourself. `hookshot.verify()` does the parsing, the age check, and the comparison.

## Step 1: Store the secret

Keep the secret out of your source code. Read it from the environment:

```bash
export HOOKSHOT_SECRET="your-endpoint-secret"
```

## Step 2: Install hookshot

```bash
pip install hookshot==3.4.0
```

Pinning the version keeps your app on the release this guide describes.

## Step 3: Verify in your route

```python
import os

from flask import Flask, abort, request

import hookshot

app = Flask(__name__)
WEBHOOK_SECRET = os.environ["HOOKSHOT_SECRET"]


@app.post("/webhooks/hookshot")
def receive():
    try:
        hookshot.verify(
            request.get_data(),
            request.headers.get("Hookshot-Signature", ""),
            WEBHOOK_SECRET,
        )
    except hookshot.SignatureError:
        abort(400)

    event = request.get_json()
    # Only act on `event` after this point.
    return "", 204
```

What each part does:

- `request.get_data()` returns the body exactly as it arrived, as `bytes`. This is what the sender signed.
- `request.headers.get("Hookshot-Signature", "")` passes an empty string if the header is missing. `verify()` then raises `SignatureError` instead of your route crashing with a `TypeError`.
- `hookshot.verify(raw_body, header, secret)` returns `None` when the signature is valid and raises `hookshot.SignatureError` when it isn't. It never returns `False`, so don't write `if hookshot.verify(...)`. That check would always be false.
- `abort(400)` rejects the request. Parse the JSON only after verification passes.

### Verify the raw body, not parsed JSON

The signature covers the exact bytes the sender transmitted. If you parse the body and serialize it again, whitespace and key order can change, and the signature won't match. Always pass `request.get_data()` to `verify()`.

Don't read the body through `request.form` or `request.get_json()` before verifying. Calling `request.get_data()` first, as in the example, is the safe order.

## Step 4: Test it

`hookshot.sign()` produces a valid header for a body and secret, so you can test without the real sender:

```python
import json
import time

import hookshot
import pytest

from myapp import app

SECRET = "test-secret"  # set HOOKSHOT_SECRET to this value in your test environment
BODY = json.dumps({"type": "ping"}).encode()


@pytest.fixture
def client():
    return app.test_client()


def post(client, header):
    headers = {"Content-Type": "application/json"}
    if header is not None:
        headers["Hookshot-Signature"] = header
    return client.post("/webhooks/hookshot", data=BODY, headers=headers)


def test_valid_signature_is_accepted(client):
    assert post(client, hookshot.sign(BODY, SECRET)).status_code == 204


def test_wrong_secret_is_rejected(client):
    assert post(client, hookshot.sign(BODY, "wrong")).status_code == 400


def test_tampered_body_is_rejected(client):
    header = hookshot.sign(b'{"type": "other"}', SECRET)
    assert post(client, header).status_code == 400


def test_old_delivery_is_rejected(client):
    old = int(time.time()) - 3600
    assert post(client, hookshot.sign(BODY, SECRET, timestamp=old)).status_code == 400


def test_missing_header_is_rejected(client):
    assert post(client, None).status_code == 400
```

Use `sign()` in tests only. Your production code should never need it.

## Tune the replay window

By default, `verify()` rejects deliveries whose timestamp is more than 300 seconds (5 minutes) from your server's clock, in either direction. Change it with `tolerance`:

```python
hookshot.verify(body, header, secret, tolerance=120)
```

Keep your server clock synced (NTP). A clock that drifts past the tolerance makes valid deliveries fail with `timestamp outside tolerance`.

`tolerance=0` turns the age check off entirely, which allows replays. It's not recommended.

## Switch from a hand-rolled HMAC check

If you verify HMACs yourself today, `hookshot.verify()` replaces your check. Compare your code with what the library does, so you don't lose a protection or change behavior unexpectedly:

| Your check does this | `hookshot.verify()` does this |
| --- | --- |
| Reads the signature header | Parses `Hookshot-Signature: t=...,v1=...`. A missing or malformed header raises `SignatureError`. |
| Computes HMAC-SHA256 of the body | Computes HMAC-SHA256 of `"<timestamp>." + body`, so the timestamp is signed too. |
| Compares digests | Uses `hmac.compare_digest`, a constant-time comparison. Don't replace it with `==`. |
| Checks timestamp age (maybe) | Rejects deliveries more than `tolerance` seconds old. Default is 300. |

To migrate:

1. Delete your signature parsing, HMAC, comparison, and timestamp code.
2. Call `hookshot.verify(request.get_data(), header, secret)` in its place.
3. Replace your failure handling with `except hookshot.SignatureError`.
4. Run the tests in [Step 4](#step-4-test-it), including the tampered-body and old-delivery cases.

Things to watch:

- **Headers from older schemes won't verify.** `verify()` only understands the `t=...,v1=...` format. If you currently verify a different format, such as a bare hex digest, `verify()` raises `malformed Hookshot-Signature header` for every request.
- **Only a single `v1` value is read.** The header must carry the `t` and `v1` fields.
- **The error type is one class.** All failures raise `SignatureError`. The message tells you which check failed (`malformed Hookshot-Signature header`, `timestamp outside tolerance`, or `signature mismatch`). Log it, but don't return it to the caller.

## Troubleshooting

| Symptom | Likely cause |
| --- | --- |
| `signature mismatch` on every delivery | Wrong secret, or the body was changed before verification (parsed and re-serialized, or modified by middleware). Verify `request.get_data()`. |
| `signature mismatch` only in production | A proxy or middleware is rewriting the body, or the production secret differs from the one in your tests. |
| `timestamp outside tolerance` | Your server clock is off, or the request was delayed or replayed. |
| `malformed Hookshot-Signature header` | The header is missing, empty, or isn't in the `t=...,v1=...` format. |

## Next steps

- Respond quickly. Return the `204` as soon as the signature checks out, and do slow work in a background job.
- Log rejected requests with the error message, without the secret or full body.
- Treat the secret like a password. Rotate it if it leaks.
