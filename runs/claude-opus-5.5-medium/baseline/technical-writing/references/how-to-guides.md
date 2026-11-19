# How-to guides and troubleshooting

A how-to guide gets a competent reader from a goal to a result. They already know the basics; they came with a job to do. Respect their time: no teaching, no backstory.

## Template

```markdown
# <Verb phrase naming the goal: "Rotate an API key without downtime">

<One sentence on when you'd do this, if the title doesn't make it obvious.>

## Before you begin

- <Required access, versions, or prior setup, linked>

## Steps

1. <Action.> <Expected result, when it's not obvious.>
2. If <condition>, <action>. Otherwise, <action>.
3. ...

## Verify

<How to confirm it worked: a command and its expected output.>

## Undo

<For anything destructive or risky: how to roll back.>

## Related

- <Reference entries for anything used above>
- <Explanation page for the why>
```

## Rules

- **Title is the goal in the reader's words.** Readers scan a sidebar or search results for their task. "Configure SSO with Okta" beats "SAML integration."
- **Assume competence, not context.** Skip how to open a terminal; don't skip which credentials the command needs.
- **Real-world variation is welcome.** Unlike a tutorial, a how-to may branch, because readers arrive with different setups. Use conditional steps or short tabs, and keep the common path first.
- **Start where the reader is.** It's fine to begin mid-flow ("With your cluster running, ...") as long as the prerequisites say what that means.
- **Link out instead of explaining.** One clause of why is fine; a paragraph belongs on an explanation page.
- **Include verification and rollback.** A reader can't tell success from silent failure without a check, and anything touching production needs a way back.
- **One goal per guide.** If the steps fork into two different results, write two guides.

## Troubleshooting pages

Organize by symptom, because that's what the reader has.

```markdown
## `Error: connection refused (os error 111)` when running `app migrate`

**Cause:** The database isn't reachable at the host in `DATABASE_URL`.

**Fix:**

1. Check the database is running: `pg_isready -h localhost`
2. ...
```

- Use the literal error text as the heading so it matches what readers paste into search.
- Give the cause in one sentence, then the fix as steps.
- When one symptom has several causes, list them most likely first, each with how to tell it apart.
