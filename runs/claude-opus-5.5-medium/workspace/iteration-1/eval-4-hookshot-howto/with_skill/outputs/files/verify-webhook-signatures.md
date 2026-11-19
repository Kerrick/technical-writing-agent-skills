# Verify webhook signatures with hookshot

This guide adds a Flask endpoint that accepts a webhook delivery only when its signature checks out, and rejects forged, altered, and replayed deliveries. It covers hookshot 3.4.0.

If you already check signatures with your own `hmac` code, follow the same steps, then read [Switching from a hand-rolled HMAC check](#switching-from-a-hand-rolled-hmac-check) to see what to delete and what changes.

## Before you begin

You need:

- Python 3.10 or later. hookshot 3.4.0 fails to import on earlier versions.
- A Flask app. To set one up, follow [Flask's installation guide](https://flask.palletsprojects.com/en/stable/installation/).
- The **signing secret** for your endpoint. This is the shared secret the webhook sender issued to you. The sender signs every delivery with it, and you use it to check each signature. hookshot calls this parameter `secret`.

Terms used on this page:

- A **delivery** is one HTTP request the sender makes to your endpoint.
- An **event** is the JSON payload inside a delivery.
- The **signature header** is the `Hookshot-Signature` request header that comes with each delivery.

## How hookshot checks a delivery

Signing a delivery works like this. The sender takes the current Unix time and the exact bytes of the request body, joins them as `<timestamp>.<body>`, and computes an HMAC-SHA256 of the result with the signing secret. Then it sends the timestamp and the hex digest in the signature header:

```text
Hookshot-Signature: t=1795065333,v1=b91eb71ca2e9dd432f17baf4c624f8d4d54bfa047a61c2c0167b272c027cd29b
```

`hookshot.verify(raw_body, header, secret)` repeats that computation on your side and compares the results. It returns `None` when the delivery is valid. Otherwise it raises `hookshot.SignatureError` with one of these messages:

| Message | What happened |
|---|---|
| `malformed Hookshot-Signature header` | The header is empty, or is missing `t=` or `v1=`, or `t` is not an integer. |
| `timestamp outside tolerance` | The timestamp is more than `tolerance` seconds (default `300`) before or after your server's clock. This rejects a captured delivery that someone replays later. |
| `signature mismatch` | The body, the timestamp, or the secret differs from what the sender signed. |

The timestamp check compares against your server's clock, so keep that clock synchronized (for example, with NTP). If it drifts by more than five minutes, valid deliveries get rejected.

## Step 1: Install hookshot

Install hookshot into the same environment as your Flask app:

```sh
python -m pip install hookshot
```

`verify` and `SignatureError` both come from the `hookshot` module. Search for `hookshot.verify` when you need its reference entry.

## Step 2: Make the signing secret available to your app

Keep the signing secret out of source control. This guide reads it from the `HOOKSHOT_SECRET` environment variable. Set it in your shell for local development, and in your host's secret store for production:

```sh
export HOOKSHOT_SECRET='paste-your-signing-secret-here'
```

## Step 3: Add the webhook endpoint

The following `app.py` receives billing events at `/webhooks/billing`. It checks each delivery before it parses or acts on the event:

```python
# app.py
import json
import os

import hookshot
from flask import Flask, abort, request

app = Flask(__name__)


@app.post("/webhooks/billing")
def receive_billing_webhook():
    # The exact bytes received. Read them before touching request.form or request.files.
    raw_body = request.get_data()
    # "" rather than None when the header is missing; verify() needs a string.
    signature = request.headers.get("Hookshot-Signature", "")

    try:
        hookshot.verify(raw_body, signature, os.environ["HOOKSHOT_SECRET"])
    except hookshot.SignatureError as error:
        app.logger.warning("Rejected webhook delivery: %s", error)
        abort(400)

    # Parse the same bytes that were verified.
    event = json.loads(raw_body)
    app.logger.info("Received %s for %s", event["event"], event["invoice_id"])
    # Handle the verified event here.
    return "", 204
```

What each part does:

- `request.get_data()` returns the body exactly as it arrived. The signature covers those bytes, so verify those bytes and nothing else. [Getting the raw body right](#getting-the-raw-body-right) shows the forms that look equivalent but aren't.
- `request.headers.get("Hookshot-Signature", "")` passes an empty string when the header is missing, so `verify` raises `SignatureError` (`malformed Hookshot-Signature header`) and the endpoint returns 400. With `None`, `verify` crashes with `AttributeError` and Flask returns a 500.
- The `except` block catches only `hookshot.SignatureError`. Other errors, such as a missing `HOOKSHOT_SECRET` variable, still surface as server errors you'll notice.
- `json.loads(raw_body)` parses the verified bytes directly. It doesn't depend on the delivery's `Content-Type`, the way `request.get_json()` does.
- The endpoint returns `204 No Content` once the delivery passes, and `400 Bad Request` when it fails.

> **Why log the reason but not return it?**
> The log message tells you which check failed (header, age, or signature), which is what you need when debugging a misconfigured secret or a drifting clock. The response body says nothing, so someone probing your endpoint with forged deliveries doesn't learn which check stopped them.

> **Warning: don't act on the event before `verify` returns.**
> Anything your code does with the body before verification, such as logging event contents, writing to a database, or enqueueing a job, also happens for forged deliveries.

## Step 4: Test the endpoint with signed deliveries

`hookshot.sign(raw_body, secret, timestamp=None)` returns a signature header value, the same way a real sender builds one. Use it in tests to produce valid deliveries, and deliberately broken ones, without the sender.

Save this as `test_webhooks.py` next to `app.py`:

```python
# test_webhooks.py
import json
import time

import hookshot
import pytest

from app import app

SECRET = "test-signing-secret"
BODY = json.dumps({"event": "invoice.paid", "invoice_id": "inv_1042"}).encode()


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("HOOKSHOT_SECRET", SECRET)
    return app.test_client()


def deliver(client, body, signature=None):
    headers = {"Content-Type": "application/json"}
    if signature is not None:
        headers["Hookshot-Signature"] = signature
    return client.post("/webhooks/billing", data=body, headers=headers)


def test_accepts_signed_delivery(client):
    response = deliver(client, BODY, hookshot.sign(BODY, SECRET))
    assert response.status_code == 204


def test_rejects_wrong_secret(client):
    response = deliver(client, BODY, hookshot.sign(BODY, "some-other-secret"))
    assert response.status_code == 400


def test_rejects_altered_body(client):
    signature = hookshot.sign(BODY, SECRET)
    altered = BODY.replace(b"inv_1042", b"inv_9999")
    response = deliver(client, altered, signature)
    assert response.status_code == 400


def test_rejects_replayed_delivery(client):
    ten_minutes_ago = int(time.time()) - 600
    response = deliver(client, BODY, hookshot.sign(BODY, SECRET, timestamp=ten_minutes_ago))
    assert response.status_code == 400


def test_rejects_missing_signature(client):
    response = deliver(client, BODY)
    assert response.status_code == 400
```

Install pytest if you don't have it, then run the tests:

```sh
python -m pip install pytest
python -m pytest test_webhooks.py
```

Each test covers one way a delivery can fail: the wrong secret, an altered body, a delivery older than the five-minute tolerance, and a missing header. `test_accepts_signed_delivery` confirms that a correct delivery still gets through.

## Getting the raw body right

Most failed verifications come from passing `verify` something other than the bytes that arrived. Flask offers several ways to read a request body, and only one is right here:

| Expression | Result with `verify` |
|---|---|
| `request.get_data()` | **Right.** The exact bytes received. |
| `json.dumps(request.get_json()).encode()` | **Wrong.** Raises `SignatureError: signature mismatch` on valid deliveries. |
| `request.get_data(as_text=True)` | **Wrong.** Returns a `str`, so `verify` raises `TypeError` and Flask returns a 500. |
| `request.data` | **Wrong for form-encoded deliveries.** It's empty when the body is form data, so the signature never matches. |

The re-serialized JSON form is the one people reach for most, because the parsed event looks identical:

```python
# Wrong: verifies a re-serialized copy, not the bytes the sender signed.
event = request.get_json()
hookshot.verify(json.dumps(event).encode(), signature, os.environ["HOOKSHOT_SECRET"])
```

```python
# Right: verify the raw bytes, then parse them.
raw_body = request.get_data()
hookshot.verify(raw_body, signature, os.environ["HOOKSHOT_SECRET"])
event = json.loads(raw_body)
```

The wrong form fails because `json.dumps` writes its own whitespace, key separators, and character escapes. For example, a sender's body of `{"event": "invoice.paid",  "invoice_id": "inv_1042"}`, with two spaces after the comma, comes back from `json.dumps` with one space. That changes a single byte, and the HMAC no longer matches. Some senders' JSON happens to round-trip unchanged, so this bug can pass your tests and then fail in production.

## Switching from a hand-rolled HMAC check

If your endpoint already verifies `Hookshot-Signature` with `hmac` and `hashlib`, it probably looks something like this:

```python
# Wrong: a typical hand-rolled check, shown so you can recognize it. Don't copy it.
raw_body = request.get_data()
parts = dict(p.split("=", 1) for p in request.headers["Hookshot-Signature"].split(","))
signed_payload = parts["t"].encode() + b"." + raw_body
expected = hmac.new(os.environ["HOOKSHOT_SECRET"].encode(), signed_payload, hashlib.sha256).hexdigest()
if parts["v1"] != expected:
    abort(400)
```

This code has three flaws:

- **`!=` leaks timing.** A string comparison stops at the first differing character, so how long it takes reveals how much of a forged signature is right. hookshot compares with `hmac.compare_digest`, which takes the same time either way.
- **It never checks the timestamp.** Anyone who captures one valid delivery can replay it to your endpoint forever. hookshot rejects deliveries more than `tolerance` seconds from your clock.
- **Bad headers crash it.** A missing header, a header without `v1=`, or a part with no `=` raises `KeyError` or `ValueError`, and Flask returns a 500. hookshot raises `SignatureError` for all of these.

Here is how each part of the hand-rolled check maps to hookshot:

| Hand-rolled step | With hookshot |
|---|---|
| Split the header into `t` and `v1` | Done inside `verify`. A malformed header raises `SignatureError`. |
| HMAC-SHA256 over `t` + `.` + body | Done inside `verify`. Same computation. |
| Compare with `==` or `!=` | Done inside `verify` with `hmac.compare_digest`. |
| (no age check) | Done inside `verify`. Default `tolerance=300` seconds. |
| `abort(400)` on mismatch | Catch `hookshot.SignatureError` and `abort(400)`. |

To switch, replace the whole block with the `try`/`except` from [Step 3](#step-3-add-the-webhook-endpoint):

```python
raw_body = request.get_data()
signature = request.headers.get("Hookshot-Signature", "")
try:
    hookshot.verify(raw_body, signature, os.environ["HOOKSHOT_SECRET"])
except hookshot.SignatureError as error:
    app.logger.warning("Rejected webhook delivery: %s", error)
    abort(400)
```

Then remove the `hmac` and `hashlib` imports if nothing else uses them.

> **Warning: don't set `tolerance=0` to match your old behavior.**
> `tolerance=0` turns off the age check entirely, so replayed deliveries pass verification again. If valid deliveries fail with `timestamp outside tolerance` after you switch, fix your server's clock rather than disabling the check. If deliveries really do arrive late, pass a larger value, such as `tolerance=600`.

## Accepting two secrets during a rotation

> **Optional: how do I rotate the signing secret without dropping deliveries?**
> `verify` checks against one secret per call. While the sender switches to a new secret, some deliveries arrive signed with the old one. To accept both until the switch is done, try each secret in turn:
>
> ```python
> def verify_with_any_secret(raw_body, signature, secrets):
>     """Raise SignatureError unless the delivery is signed with one of `secrets`."""
>     error = hookshot.SignatureError("no signing secrets configured")
>     for secret in secrets:
>         try:
>             hookshot.verify(raw_body, signature, secret)
>         except hookshot.SignatureError as exc:
>             error = exc
>         else:
>             return
>     raise error
> ```
>
> Call it from the endpoint with the new secret first, for example `verify_with_any_secret(raw_body, signature, [os.environ["HOOKSHOT_SECRET"], os.environ["HOOKSHOT_PREVIOUS_SECRET"]])`. Once deliveries signed with the old secret stop arriving, remove it and go back to plain `hookshot.verify`.

## What hookshot doesn't do

hookshot verifies one delivery's signature and age. These stay your responsibility:

- **Duplicate deliveries.** A delivery replayed within the tolerance window passes verification, and senders often retry deliveries they think failed. If handling the same event twice would cause harm, such as charging a customer twice, record an identifier from each event you've handled and skip repeats.
- **Reading the header.** `verify` needs the header value as a string. It doesn't read Flask requests itself, and passing `None` for a missing header raises `AttributeError`, not `SignatureError`.
- **Storing secrets.** hookshot takes the secret as an argument. Where you keep it is up to you.
- **Checking the event's contents.** A valid signature proves the sender produced the body. It doesn't prove that the body has the fields your code expects.
- **More than one secret per call.** See [Accepting two secrets during a rotation](#accepting-two-secrets-during-a-rotation).
