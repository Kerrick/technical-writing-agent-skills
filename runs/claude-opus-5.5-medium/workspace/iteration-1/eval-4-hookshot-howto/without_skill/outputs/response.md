I've written the guide and saved it as `outputs/verify-webhook-signatures-flask.md`.

**What's in it:**
- **A short "what verification protects against" section** for readers new to webhooks. It explains the `t=…,v1=…` header, the HMAC over `"{t}.{body}"`, and why there's a replay window.
- **Three steps:** keep the secret out of your code, verify in the Flask route, and test with `hookshot.sign()`. The test file covers a valid signature, a wrong secret, a changed body, an old delivery and a missing header.
- **An optional section on `tolerance`**, including a warning not to use `tolerance=0` in production.
- **A "Switch from a hand-rolled HMAC check" section** for readers who already do this themselves. It shows the old code next to the new code, and a table of differences that could make deliveries your old code accepted start failing.
- **Troubleshooting** for each `SignatureError` message, and for the errors that show up as a 500 instead of a 400.

**What I found by running hookshot 3.4.0 directly:**
- **A missing header crashes the check.** Flask returns `None` for a missing header, and `verify(..., None, ...)` raises `AttributeError`, not `SignatureError`. So the route defaults the header to `""`, which correctly gives "malformed header."
- **A `bytes` secret or a `str` body also crashes** (`AttributeError` and `TypeError`). The guide calls both out.
- **Formatting is strict.** A space after the comma in the header (`t=…, v1=…`) counts as malformed.
- **Old and future timestamps are both rejected.** The check allows 300 seconds either way.
- **Secret rotation isn't supported.** If a header has several `v1=` values, only the last one is checked, against one secret. The guide suggests trying the new secret and then the old one.

**Things to check before publishing:**
- **The Flask code hasn't been run.** Installing Flask in this environment needed approval, so I couldn't. I checked every hookshot behavior the guide describes by calling the library directly, and the Flask parts only use standard calls (`request.get_data()`, `request.headers.get`, `test_client`). Still, run the test file in CI or on your machine before publishing.
- **I guessed the install command.** I used `pip install hookshot`; swap in your real package name if it's different.
- **Status code:** I return 400 on failure. Change it if your convention is 401.

Because your site is built per release, the guide describes 3.4.0 as it is. It doesn't say "new in", "currently" or anything about other versions.