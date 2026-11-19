<!--
Reader: a developer new to webhooks who has been asked to "verify signatures" and wants to know
what that protects against before following the how-to. Read away from the keyboard; no steps.
Describes the scheme implemented by hookshot 3.4.0.
-->

# How webhook signatures work

Your webhook URL is public, so anyone who finds it can POST to it. A signature lets your server tell a delivery the sender actually sent apart from one someone else made up or changed.

## One delivery, start to finish

Say the sender delivers this body to your `/webhooks` route:

```json
{"id": "evt_1042", "type": "invoice.paid"}
```

You and the sender share one value no one else has: the **signing secret**. Before sending, the sender:

1. Takes the current time in Unix seconds, for example `1795065434`.
2. Builds a message from the timestamp, a period, and the exact body bytes: `1795065434.{"id": "evt_1042", "type": "invoice.paid"}`.
3. Computes an HMAC-SHA256 of that message, keyed with the signing secret, and hex-encodes it.
4. Sends the timestamp and digest with the delivery in one header:

   ```text
   Hookshot-Signature: t=1795065434,v1=3807053765348e9ba110d47d08ff4d12d27f733681fce37c29cb4b98d0d1fe74
   ```

When the delivery arrives, `hookshot.verify()` repeats steps 2 and 3 with your copy of the secret and the body it received, then compares its digest with the `v1=` value. If they match, only someone holding the secret could have produced that header for that body at that time.

```text
 sender                                         your Flask app
 ------                                         --------------
 secret + "t.body" --HMAC-SHA256--> digest
                 POST body + Hookshot-Signature: t=…,v1=digest
                 ------------------------------------------------>
                                                secret + "t.body" --HMAC-SHA256--> expected
                                                expected == digest ?  accept : reject
```

## What a match proves, and what it doesn't

An HMAC is not encryption. The body travels as readable JSON, protected in transit only by HTTPS. The signature proves two things: the delivery came from someone with the secret, and nobody changed the body or timestamp along the way. Change one character of the body, and the digest no longer matches.

The signature doesn't prove the delivery is *new*. A captured delivery is still correctly signed when someone resends it an hour later. That is why the timestamp is inside the signed message: an attacker can't change `t=` without breaking the digest, so `verify()` can trust it and reject deliveries more than 300 seconds from your server's clock. That window is the `tolerance` argument. Setting it to `0` turns the age check off and allows replays.

## Why the raw body matters

A common mistake is to verify the parsed event: let Flask decode the JSON, then serialize it again and check that. It looks like the same data, but the signature covers bytes, not meaning. Re-serializing can change spacing, key order, or how characters are escaped:

```text
received:      {"id": "evt_1042", "type": "invoice.paid"}
re-serialized: {"id":"evt_1042","type":"invoice.paid"}
```

The two digests differ, and `verify()` raises `signature mismatch` on a delivery that was genuine. Always verify the bytes exactly as they arrived, then parse them.

## Why the comparison is constant-time

Comparing two strings with `==` stops at the first character that differs, so a wrong guess that shares a longer prefix with the real digest takes slightly longer to reject. With enough requests, an attacker can measure that and recover a valid digest one character at a time. hookshot compares digests with `hmac.compare_digest`, which takes the same time no matter where the strings differ. This is one reason to use the library instead of writing the check yourself.

## Next steps

- [Verify webhook signatures with hookshot](verify-webhook-signatures.md): add the check to a Flask route.
- [Replace a hand-rolled HMAC check with hookshot](replace-hand-rolled-hmac-check.md)
