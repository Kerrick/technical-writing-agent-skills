# Explanation

Explanation answers *why* and builds the reader's mental model: how the parts relate, why the design is the way it is, what was traded away, and how it compares to alternatives. It's read away from the keyboard. It has no steps.

Titles are topics or questions: "How caching works," "Why jobs run at least once," "Choosing between webhooks and polling."

## Rules

- **Build one model per page.** Decide the picture the reader should hold in their head at the end, and make everything on the page serve it.
- **Anchor abstractions in a concrete case.** Walk one specific request, record, or job through the system before generalizing.
- **Make the machine visible.** Name the parts, say what each holds and what moves between them. A diagram of the actual mechanism (boxes for components, arrows for data or control) earns its place here more than anywhere else in docs.
- **Give the reasons.** Design decisions, constraints, history when it explains the present, and what the alternatives cost. Explanation is allowed opinions, stated as such.
- **Bound analogies.** Say where an analogy stops holding ("Unlike a real queue, ..."), or readers will carry it past the edge.
- **Refute misconceptions directly.** When readers commonly hold a wrong model, state it, show a case where it predicts the wrong thing, then give the right model. Just presenting the right model often leaves the wrong one intact.
- **Link to the doing.** End with the tutorials and how-tos where the reader applies the model, and the reference entries for the parts named.

## Comparison pages

When explaining a choice between options, compare on the dimensions that decide it (a table works), say which you'd pick for which situation, and be honest about where your own product loses.
