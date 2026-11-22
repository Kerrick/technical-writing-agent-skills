# One log, many hands

Read this when more than one person or agent is changing the repository at once, before you write or number any ADR.

Two agents that each take "the next number" collide, and two that each record the same decision leave the log with both. One of them keeps the log.

- **The keeper** decides which reported decisions deserve an ADR, drafts those, and numbers them in the order they land. If nobody has been named keeper, ask who is before writing a record.
- **Everyone else writes no ADRs.** Report to the keeper each decision your work needs, with its options and evidence, and each line of an existing ADR that your change makes untrue.
- **For a technical decision, the review may follow the change.** A departure that is accepted gets its ADR after the fact. One that is rejected is reverted or fixed.
- **The keeper writes that ADR within the hour of the push it follows.** A log left untrue across a pause in the work is a broken build of its own kind.
- **A decision the project reserves for its owner waits for the owner.** So does a departure from one.
- **One decision found in two records keeps the lower number.** Fold what the other adds into it and delete the other.
