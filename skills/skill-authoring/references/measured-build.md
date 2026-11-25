# A measured build

Read this before building a skill rule by rule from outside sources, such as documentation sets, style guides, or codebases, when you need to show that each rule is new to the target model and that the skill carries no source's wording. This file was written for this skill; it isn't adapted from the Agent Skills documentation.

In a measured build, you compare what the model already believes (the baseline) with what the sources show, keep only the difference, and have it written up by a session that has seen neither.

## Three kinds of context

Assign each step to one, on purpose, because what a context has seen shapes what it writes:

- **A fork of the baseline point:** a copy of the session that just wrote the baseline, forked before anything else is sent to it. It holds the baseline as its beliefs, so it's the best judge of what the baseline already says.
- **A fresh session:** knows only its prompt and the files it's told to read.
- **A script:** no judgment. Use one for anything mechanical: extracting sections, stripping fields, checking names, checking citations.

## Steps

1. **Baseline.** In a new session on the target model and effort level, with no version of the skill installed, ask the model to recall everything it knows about the field without tools, and to say what it would actually do by default, step by step, in a dozen realistic situations the skill will cover. Then, in the same session, have it read the Agent Skills format guidance and write a skill from memory. That skill is the baseline; the end of that turn is the fork point. Send nothing else to that session, and never edit the baseline. The default behaviors are the skill's user research: each one the sources contradict is a habit the skill needs a rule against. For a library old enough to be in the model's training data, include situations that touch APIs changed since then; the outdated calls and names it reaches for become corrections.
2. **Budget context.** Check how full the fork point's context already is. Each reading fork needs room for its pages and then the comparison, so keep each source's scope well under what's left, and split a large source across forks.
3. **List before reading.** Have a cheaper sub-agent list each source's files in reading order. Check the list (the right folder and version, the expected count, no sections meant to be skipped) before the fork reads anything.
4. **Read and compare,** one fork of the baseline point per source. After reading, the fork sorts every difference from the baseline into one group: a principle the baseline missed; a correction to something it states; a house convention that wouldn't carry over; or a place where the baseline's advice is better than the source's practice. Each needs evidence: a file and a short quote, or a pattern seen in two or more places, plus the baseline line it differs from. An empty group is a valid result. The fork ends its file with the rules restated in general terms: no quotes, no names of the source or its technology, no examples taken from it.
5. **Check each findings file before ending its fork,** while the fork can still fix a weak claim: run the leak check on its general rules, and verify two of its claims against the source yourself.
6. **Audit** in a new fork: check every general rule against its evidence, revise or remove what the evidence doesn't support, and relabel the sources by letter. Its output is the only thing the sessions in later clean-room steps read.
7. **Merge** in another fork, under rules fixed before anyone reads the findings. First decide how the sources relate, because what counts as support depends on it:
   - **Corroborate,** when the sources are independent takes on the same craft, such as several documentation sets: a rule needs two or more of them. Drop single-source rules, however good. Where sources differ, write the most specific rule none of them contradicts.
   - **Compose,** when the sources are layers of one stack, such as a framework and the library under it: a rule needs the one source for the layer it's about. Give the merge fork each letter's layer, described without naming it. Where sources differ, follow the source for a layer on that layer's interface, and the source for a higher layer where that layer is meant to change how a lower one is used. Under the corroborate rule, a layered skill loses every rule only one layer states.
   - A build can mix both, such as several applications on one framework: corroborate across the applications, compose over the framework.
   - Drop a rule the baseline already states, citing the line. A correction is never redundant.
   - Keep a baseline rule that two or more sources break, as known but often skipped.
   - Record for each kept rule its kind, what it applies to, and what an agent does wrong without it.
8. **Re-decide the shortfalls** in a separate fork that can see the evidence. A reader forked from the baseline's author tends to side with the baseline, so "the source falls short here" needs an evidence test. Classify each breakage as a lapse (objectively wrong, or against the source's style guide), deliberate (in the source's templates or style guide, or on at least 80% of pages of that kind, counted, and contradicting the rule), or unexamined. A source that doesn't forbid something hasn't endorsed it.
9. **Build the writer's input by script:** keep each rule's text, kind, scope, and "without it"; strip sources, baseline citations, and process notes; append the maintainer's standing rules. Run the leak check on the result.
10. **Arrange for the agent.** A skill is read at the moment an agent is about to act, so arrange it around the decisions the agent faces and the habits it must override, not in the sources' order. Write each rule as a card, then:
    - shuffle the cards, twice, with `uv run scripts/shuffle.py shuffle CARDS OUT MAP`, so no later step inherits the sources' order;
    - give each shuffled copy to a separate fresh session, which first designs the files and sections from the baseline's default behaviors and the corrections alone, writing them down before it opens the cards, then places every card, ordering each section by stakes and by how often the habit behind it shows up;
    - put both sorts on shared ids with `shuffle.py common`, and reconcile them in a third fresh session into one outline. Where the sorts agree, the structure holds; where they differ is a judgment call that session makes, with its reasons written down.
11. **Write** in a fresh session that has never seen the baseline skill, the sources, or the findings. Its inputs are the format guidance, the outline, the cards, and the baseline's default behaviors, which show it the habits to write against; never the baseline skill itself, whose structure and wording it would pull in. Neither the baseline nor any version of the skill may be installed while it runs. It places every card where the outline has it, then writes a placement table: each card's id and the file:line that states it.
12. **Check:** the validator, the leak check on the finished skill, and the placement check; read a sample of cited lines to confirm each states its rule; confirm from the writer's transcript that it read only what it was allowed to. Then have a fresh session audit the skill against the cards, card by card, for anything missing, weakened, or contradicted, and send its findings back to the writer.

## The checks

**Leak check.** A short script that searches files, case-insensitively and by whole word, for a list of source names and technology names, and prints `file:line: word` for each hit, exiting 1 on any. With whole-word matching, "trust" doesn't match "rust". Run it on every file a clean-room step reads and on the finished skill, and add each source's terms to the list.

**Placement check.** A script that reads the rule numbers from the rule file and the rows of the placement table, and fails unless every rule has exactly one row, and every cited file:line exists and isn't blank. It proves the line exists, not that it states the rule, so read some yourself.

**Source checks.** The leak check catches names, not wording. Two bundled scripts compare the finished skill with the sources themselves:

- `uv run scripts/overlap.py --source SRC FILES` reports every line that shares a run of eight or more words with the source, and exits 1 on any.
- `uv run scripts/structure.py --source SRC FILES` matches each paragraph to its most similar source paragraph and fails a file that follows a source page's order, or holds several sentences close to the source's. A failure is a list of lines to read, not a verdict: text that shares the sources' ideas will match some sentences by topic. Before trusting its thresholds on a new source, run it on a known close copy, which should fail, and on unrelated writing by the same author, which should pass, and adjust `--para` and `--sentence` until it separates them.

Run them whenever the skill's license depends on carrying none of the sources' expression. An open license doesn't mean no conditions: copied text from a CC BY source needs credit, from a share-alike source makes the skill share-alike, and from an MIT, BSD, or similar source carries its notice. A skill dedicated to the public domain with no notice is right only if the checks find nothing.

## Keeping it repeatable

- **Keep ad-hoc judgment out.** A check done by hand outside a fixed prompt can't be repeated for the next model. Make every check a prompt or a script.
- **Write prompts with slots** for paths and per-source values, and fill them by script. No machine paths, and no baseline line numbers in a prompt: describe a baseline rule by what it says.
- **Prompts state the method as it now stands.** Record how a past build differed in that build's record, not in the prompt.
- **Never edit a build's records:** the baseline, the findings, the intermediate files. Later builds are compared against them.
- **Never compact a session whose job needs exact wording,** such as a reading fork. If it runs out of room, rewind to before the reading, narrow the scope, and fork again.
- **One build per model and effort level.** A skill built for one model is a variant for any other, and replaces the current skill only if its eval results are better on the current skill's target model.

## Licensing

Files that quote a source carry that source's license and an opening notice naming the source, its holder, and the license. Quote briefly, and only when the exact wording matters. A share-alike license applies to each file that quotes it, not to the rest of the repository. Everything from the anonymized audit onward, the skill included, holds no source wording.
