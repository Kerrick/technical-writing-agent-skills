# Template

Read this when the repository has no decision log yet, or when you need to check what a section of a record is for. When the log has records, copy their form instead of this one.

The headings are those of [MADR](https://adr.github.io/madr/) 4.0.0, so MADR tools read the record. The Confidence line and the numbered options are additions.

```markdown
---
status: accepted
date: YYYY-MM-DD
deciders: <who decided, and what each decided>
consulted: <whose views were sought>
informed: <who was told>
---

# <The decision, as a sentence>

## Context and Problem Statement

<The situation and the problem, in a few sentences that end in the question being decided. Facts only.>

## Decision Drivers

* <a quality wanted, a constraint, or a concern, taken from the requirement>

## Considered Options

1. <the chosen option>
2. <another option that was weighed>

## Decision Outcome

Chosen: option 1, because <the reason recorded>. Option 2 lost because <why>. How it works is in <path to the design document>.

Confidence: <what the evidence shows works; whether any recorded comparison says it is better; what is unproven>.

### Consequences

* Good, because <a wanted quality improves>
* Bad, because <the effort, risk, or cost it adds, and for whom>
* Neutral, because <an effect that is neither>

### Confirmation

<The test, build check, or review that fails when the code departs from the decision. Or: nothing automated checks it.>

## Pros and Cons of the Options

### <option 2>

* Good, because <argument>
* Bad, because <argument>

## More Information

<Pointers to design documents and related decisions. When to revisit the decision.>

### Later research (YYYY-MM-DD)

<Alternatives found after the decision. They are for a reader's information; they were never a reason for it.>
```

## Fields and sections

- **`status`:** `proposed` or `accepted`.
- **`date`:** the day the decision was made, or the day it was last restated. A typo or link fix doesn't change it.
- **`deciders`:** required. MADR 4 names this field `decision-makers`, and earlier versions `deciders`. Keep the name the log already uses.
- **`consulted` and `informed`:** include them only when someone was.
- **Decision Drivers, Consequences, and Confirmation** are optional in MADR and required here.
- **Pros and Cons of the Options:** include it only when the reasons an option lost don't fit in a sentence of the outcome.
- **Later research:** include it only when no alternative, or not every alternative listed, was weighed at the time.

Leave out a section that would be empty instead of writing "None".

## Further reading

Olaf Zimmermann's articles describe the practice this template comes from, with a catalogue of the ways records go wrong: [how to create ADRs](https://ozimmer.ch/practices/2023/04/03/ADRCreation.html), [the MADR template explained](https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html), and [a test for architectural significance](https://ozimmer.ch/practices/2020/09/24/ASRTestECSADecisions.html).
