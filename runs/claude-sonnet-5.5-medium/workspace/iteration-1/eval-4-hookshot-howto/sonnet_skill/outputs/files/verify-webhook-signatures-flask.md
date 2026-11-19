---
title: Verify webhook signatures with hookshot
description: Reject forged, tampered and replayed webhook deliveries in a Flask view.
---

# Verify webhook signatures with hookshot

This guide shows how to check the signature on every webhook delivery your Flask app receives, using `hookshot.verify`. When you finish, your view answers `200` to genuine deliveries and `400` to anything forged, altered, malformed or too old.

This guide covers Flask and the common path: one shared secret and the default replay window. It is not a guide to receiving webhooks in general (routing, retries, queuing). Other frameworks use the same `hookshot.verify` call; only the way you read the raw body and the headers changes. For every argument and edge case, run `help(hookshot.verify)`.

## Prerequisites

- A Flask app and `hookshot` installed in the same environment.
- The signing secret for the endpoint, as a string. Keep it out of source control. The examples read it from the `HOOKSHOT_SECRET` environment variable.

## How signing works

A **webhook** is an HTTP request that a service (the sender) makes to your app when something happens. Anyone who knows your URL can send you the same kind of request, so you need proof that a delivery came from the sender and was not changed on the way.

hookshot senders provide that proof with an **HMAC**: a hash computed from the message and a secret that only the sender and you know ([HMAC on Wikipedia](https://en.wikipedia.org/wiki/HMAC)). Each delivery carries this header:

```text
Hookshot-Signature: t=<unix seconds>,v1=<hex digest>
```

The digest is HMAC-SHA256 over the timestamp, a dot, and the raw body bytes. `hookshot.verify` recomputes the digest with your secret, compares it with `v1` and checks that `t` is recent.

If you already compute HMACs by hand, see [Replace a hand-rolled check](#replace-a-hand-rolled-check) for what `verify` does for you.

## Verify a delivery in a Flask view {#verify-in-flask}

**Listing: a Flask view that rejects deliveries with an invalid signature**

```python
import os

from flask import Flask, abort, request

import hookshot

app = Flask(__name__)
SECRET = os.environ["HOOKSHOT_SECRET"]


@app.post("/webhooks/hookshot")
def receive():
    signature = request.headers.get("Hookshot-Signature", "")
    if not signature.isascii():
        abort(400)
    try:
        hookshot.verify(request.get_data(), signature, SECRET)
    except hookshot.SignatureError:
        abort(400)

    event = request.get_json()
    return {"received": event["type"]}, 200
```

Points that are not obvious:

- `request.get_data()` returns the body exactly as received, as `bytes`. The signature covers those bytes, so verify before you parse. Flask still lets you call `request.get_json()` afterwards.
- `request.headers.get("Hookshot-Signature", "")` uses an empty default. A missing header then raises `SignatureError`. Without the default, `verify` receives `None` and raises `AttributeError`, which Flask turns into a `500`.
- The `isascii()` check rejects headers with non-ASCII characters before `verify` sees them. `verify` raises `TypeError` for such a value instead of `SignatureError`.
- Return `400` for every failure and send no detail to the caller. The `SignatureError` message says which check failed; log it on your side if you need it.

The rest of the view is self-explanatory.

### Do not parse the body first

Wrong:

```python
# WRONG: the signature will not match, because the body was re-serialized
event = request.get_json()
hookshot.verify(json.dumps(event).encode(), signature, SECRET)
```

Right: pass `request.get_data()`, as in the listing above.

Re-serializing changes whitespace, key order or number formatting, so the bytes differ from what the sender signed and `verify` raises `SignatureError("signature mismatch")` on genuine deliveries.

## Test the view

`hookshot.sign` produces a header value for a body and secret, so you can test without the sender. It is meant for tests.

**Listing: tests for a valid, a tampered and an unsigned delivery**

```python
import json

import hookshot

SECRET = "test-secret"
BODY = json.dumps({"type": "order.created"}).encode()


def post(client, body, signature=None):
    headers = {"Content-Type": "application/json"}
    if signature is not None:
        headers["Hookshot-Signature"] = signature
    return client.post("/webhooks/hookshot", data=body, headers=headers)


def test_valid_delivery(client):
    response = post(client, BODY, hookshot.sign(BODY, SECRET))
    assert response.status_code == 200


def test_tampered_body(client):
    response = post(client, BODY + b" ", hookshot.sign(BODY, SECRET))
    assert response.status_code == 400


def test_missing_header(client):
    assert post(client, BODY).status_code == 400
```

Set `HOOKSHOT_SECRET=test-secret` before the app module is imported, so the view and the tests share a secret. `client` is the usual Flask test client fixture (`app.test_client()`).

To test an old delivery, sign with an explicit timestamp: `hookshot.sign(BODY, SECRET, timestamp=1_700_000_000)`. `verify` raises `SignatureError("timestamp outside tolerance")`, so the view answers `400`.

## Replace a hand-rolled check

Most hand-rolled checks look like this. `hookshot.verify` does the same work and closes the gaps marked in the comments.

**Listing: a typical hand-rolled check, with its gaps marked**

```python
import hashlib
import hmac

def is_valid(raw_body, signature, secret):
    expected = hmac.new(secret.encode(), raw_body, hashlib.sha256).hexdigest()
    # WRONG: == leaks timing information; use hmac.compare_digest
    return expected == signature
    # WRONG: no timestamp, so a captured delivery can be replayed forever
```

**Listing: what `hookshot.verify` does, written out (same behaviour)**

```python
import hashlib
import hmac
import time

def verify(raw_body, header, secret, tolerance=300):
    parts = dict(p.split("=", 1) for p in header.split(","))
    timestamp, sig = int(parts["t"]), parts["v1"]
    if tolerance and abs(time.time() - timestamp) > tolerance:
        raise SignatureError("timestamp outside tolerance")
    expected = hmac.new(secret.encode(), f"{timestamp}.".encode() + raw_body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, sig):
        raise SignatureError("signature mismatch")
```

This is a simplified view: the real function also raises `SignatureError("malformed Hookshot-Signature header")` when the header cannot be parsed.

To switch:

1. Delete your parsing and comparison code and call `hookshot.verify(request.get_data(), header, SECRET)`.
2. Catch `hookshot.SignatureError` instead of testing a boolean.
3. Remove any handling of the timestamp. `verify` signs `"<timestamp>.<body>"`, not the body alone, so a check that signs only the body fails on hookshot deliveries.

## Limits of this check

A passing `verify` shows that someone with your secret signed this body, recently. It does not show more:

- **Replays inside the window.** The default `tolerance` is 300 seconds. A captured delivery is accepted again until it is older than that. If handling an event twice is harmful, also store the event identifier from the payload and ignore repeats. `verify` does not do this.
- **Disabled age check.** `tolerance=0` turns the age check off entirely, and old captured deliveries then pass. Use it only for fixtures.
- **Clock drift.** The age check compares the timestamp with your server clock in both directions, so a badly wrong clock rejects genuine deliveries.
- **Secret exposure.** Anyone with the secret can sign valid deliveries. Keep it in the environment or a secrets manager and never in the repository.
- **Transport.** The signature does not hide the body. Serve the endpoint over HTTPS.

## Troubleshooting

| What you see | Cause | Fix |
| --- | --- | --- |
| `SignatureError: signature mismatch` on every genuine delivery | The body was parsed and re-serialized, or the secret differs from the sender's | Pass `request.get_data()`; check `HOOKSHOT_SECRET` |
| `SignatureError: timestamp outside tolerance` | Replayed or delayed delivery, or the server clock is wrong | Check the server clock; do not widen `tolerance` to hide a clock problem |
| `SignatureError: malformed Hookshot-Signature header` | Header missing, or not in `t=<seconds>,v1=<digest>` form | Check that no proxy between the sender and your app removes or rewrites the header |
| `500` with `AttributeError` | `None` was passed as the header | Use `request.headers.get("Hookshot-Signature", "")` |
| `500` with `TypeError` | Header contains non-ASCII characters | Add the `isascii()` check from the listing |
