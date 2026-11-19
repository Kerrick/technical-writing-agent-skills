# Things I keep telling the agent about ferry migrations

Collected from about six weeks of sessions on the ferry app. Some of these I've said many times.

- Migrations live in `db/ferry/`, not `db/migrate/`. It keeps creating `db/migrate/` and then wondering why nothing runs. (corrected 4 times)
- Always run `bin/ferry migrate --plan` first and read the plan before running `bin/ferry migrate --apply`. Never go straight to `--apply`. (corrected 3 times)
- Backfills on big tables (orders, events, line_items) need `--batch 5000`. The default batch is 50,000 rows and it locks the table long enough to time out checkout. We had an incident from this in March.
- Renaming a column takes two deploys: first add the new column and write to both, then in a later deploy switch reads and drop the old one. A one-step rename breaks the old app servers during the rollout. (corrected twice)
- Every migration needs a `down` step, or `irreversible!` at the top with a one-line reason. `bin/ferry lint` fails any migration that has neither.
- Staging gets refreshed from a production snapshot every night at 02:00 UTC. Don't run destructive migrations on staging between 01:30 and 02:30 UTC, the refresh will collide with it.
- Write clear commit messages.
- Always test your code before you push.
- Give migrations descriptive names.
- Make sure you understand SQL before writing a migration.
- Priya suggested: when it isn't sure a migration is reversible, it could leave a `# TODO: check reversibility` comment in the file for us to look at later.
- Deploys themselves are covered by our ferry-deploy skill, so this one shouldn't try to do those.
