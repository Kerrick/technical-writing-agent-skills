---
name: adr
description: >-
  Use when writing, reviewing, editing, splitting, replacing, or deleting an
  Architecture Decision Record (ADR), when deciding whether a decision
  deserves one, or when a decision log has drifted from the code. Use it
  whenever the user wants to record why something was built the way it was,
  mentions ADRs, MADR, decision records, or a decision log, or says a recorded
  decision is out of date, even if they never say "ADR". Not for design
  documents, specifications, or other documentation pages (use
  developer-docs), READMEs (use readme-rewrite), or Agent Skills (use
  skill-authoring).
license: CC0-1.0
metadata:
  author: Kerrick Long
  version: "1.2.0"
---

# Architecture Decision Records

You already know what an ADR is and the usual advice for writing one. This skill adds what that advice leaves out or has wrong: a higher bar for what earns a record, what to write when the reasons were never recorded, and how to keep a short log true as the code changes. Where a rule here conflicts with advice you would usually follow, follow the rule here.

A decision log is worth reading only while it is short and true. Most decisions belong in the design document for their subject. A record that is no longer true is deleted, because git keeps it and a stale record is misleading to every reader, agents most of all.

## Choose the task

- **Record a decision,** when asked, or when you make one in your work: follow **Workflow** from step 1.
- **A recorded decision no longer matches the code or the maintainer's ruling:** follow **When a decision changes**.
- **An ADR is long, holds several decisions, or reads like a specification:** read [references/splitting.md](references/splitting.md).
- **A log has grown too long:** apply step 1's test to every record, rank the ones that pass by cost to undo, and keep the top few. Move each of the others into the design document for its subject with [references/splitting.md](references/splitting.md), in an order in which every citation stays true.
- **Review an ADR or a log:** apply step 1's test to each record, then the **Checklist** and **Gotchas**, and report each problem with its file and line. Change nothing unless asked.
- **Several people or agents are changing the repository at once:** read [references/shared-log.md](references/shared-log.md) before you write or number any ADR.

## Workflow

1. **Test the decision.** Name the architecturally significant requirement it resolves, what undoing it would cost, and which other parts of the system depend on it. A requirement is architecturally significant when it shapes the system's structure: much value or risk rides on it, it needs a quality the system doesn't yet have, it depends on something outside the project's control, it reaches across many parts, or the project has not done it before. The cost to undo is on the scale of a layer rewritten, every build remade, or something users already hold broken. A choice that would be tedious to change, but that nothing else in the system rests on, isn't architectural. If you can't name all three, it isn't an ADR, however carefully or by whomever it was decided. Record it in the design document for its subject, say in your reply why it didn't pass, and stop. These never pass:
   - a rule, table, number, or convention people look up while working, which is detailed design;
   - one feature's design, or the choice of a tool or version;
   - a product decision, however firm: what the product does, sells, or collects, and the shape and names of its public API;
   - a rule for contributors, a release policy, a plan, or a task list;
   - a consequence of a decision already recorded, or a statement of scope.

   Records are few: a project's whole log is usually a handful. When several decisions pass, rank them by cost to undo and record the top few. Apply the same test to every existing ADR you touch. One that no longer passes goes to a design document and is deleted ([references/splitting.md](references/splitting.md)).
2. **Follow the log that exists.** Read its index or rules and two of its records. Copy their folder, file naming, heading form, front-matter fields, bullet style, and the way code cites them. Only when the repository has no log, use `docs/decisions/NNNN-title-with-dashes.md` and the template in [references/template.md](references/template.md).
3. **Take the next number** after the highest ever used, deleted records included. Never reuse one. Git history has them: `git log --all --format= --name-only -- <adr dir> | sort -u | tail -1` when numbers are zero-padded. Also search the docs for a "former ADR" with a higher number than any file.
4. **Gather what was recorded:** who decided, when, which options were weighed, and the reasons given at the time. Sources are notes, issues, commit messages, pull requests, and what the user tells you in this conversation. Keep what a record says apart from what you infer.
5. **Write the record** to [references/template.md](references/template.md), or the log's form. It holds one decision in about a page: the problem, the options that were weighed, the one chosen and why, and what it costs.
   - **The title states the decision as one short sentence,** not a topic.
   - **Drivers are the ones the deciders had,** taken from the requirement, not from the chosen option's strengths.
   - **Options are ones that were really weighed,** each able to solve the stated problem, all at one level of abstraction, with the chosen one first. Say in the outcome why each of the others lost. Compare in words. Weighted scores for qualities nobody measured mean nothing.
   - **Record the reasons the deciders had, and no others.** See **When the record is thin**.
   - **Consequences include the bad ones,** for the people who operate and maintain the system as well as those who build it. Leave out what a reader would guess.
   - **In Confidence, keep "it works", which evidence can show, apart from "it is better than the other options", which only a recorded comparison can show.** Name the evidence, and say what is unproven.
   - **In Confirmation, name what enforces the decision:** a test, a build check, a review. If nothing does, say that nothing does.
   - **How it works goes in the design document.** End the outcome with a pointer to it by path. Give a condition for revisiting the decision where one is known.
6. **Check every fact given in the record as proof.** Open each test, path, number, and quotation in it, and correct what the repository or the record doesn't bear out.
7. **Update what points at the log** in the same change: the index, and citations in code and docs. Code cites an ADR by number for why, and a design document by path for how. An ADR never cites a plan.
8. **Work through the Checklist,** then report: the file you wrote, what you inferred and left out, and every judgment call, so the user can overturn one at a glance.

## When the record is thin

Most mistakes in an after-the-fact ADR are inventions that read well.

- **No reason recorded for preferring the chosen option:** say so plainly. The choice may have been close, and the ADR must not imply the chosen option is better.
- **No alternative weighed at the time:** list the one option, and say that none other was weighed. Never invent an option to fill the list. Then look up the real alternatives now, from their documentation and not from memory, and report them under More Information as later research, with today's date. They are for the reader's information. They were never the reason, so don't present them as one, and don't claim the choice is better than them.
- **Drivers nobody recorded:** a driver is a reason too. List the ones in the record, and say no other was recorded. A driver of another ADR isn't a driver of this one unless the record says so, or this record replaces that one.
- **Deciders:** name who made this decision, and say what each decided. Someone who set a constraint didn't choose the mechanism. If the record doesn't say who decided, write that.
- **Confidence the deciders never stated:** write that it wasn't recorded, then give what the evidence shows today.
- **Quotations:** quote a person only from the written record the log's readers can open (a note, an issue, a commit message, a pull request), word for word. This conversation is private. Take the decision and the reasons for it from it, write them in your words, and neither quote it nor tell what was said in it. A paraphrase relayed by another session isn't a quotation.

Never backdate a reason, and never write what you inferred as what was decided.

## When a decision changes

The log stays true to the code. When a change departs from an accepted ADR, either bring the change back in line with it, or record a new decision. Who approves an ADR is the project's to say.

- **Don't edit the decision text of an accepted ADR,** and don't add dated notes or amendments to it. When later work makes that text untrue, write a new ADR with the next number that restates the whole decision as it now stands, so it reads without the old one. Its options and reasons are the ones weighed for the decision as it now stands, not those of the old record. Drivers and consequences of the old record that still hold carry over. Delete the old record in the same change, and rewrite every citation of its number in code, docs, and the index.
- **Dated documents stay as written.** Where research notes, finished plans, and released changelog entries have the old record's number, write "the former ADR N, now ADR M".
- **Context and consequences describe the decision as it was made.** When later work removes a cost, or changes a fact in the context, leave them alone. **Confidence and Confirmation follow the evidence,** so edit those in place when it changes. Typo and link fixes are fine in place too.
- **Status is `proposed` or `accepted`, and nothing else goes in that field.** A rejected proposal is never merged. A superseded or obsolete record is deleted, not marked.
- **Mark an ADR accepted only when the code does what it says.** Land the two together.
- **A hard problem may be decided in stages** (now, next, and in the end) in one ADR, each stage with a reason for it. Revisit it when a stage ends, and write it whole as the decision then stands. This is the one planned rewrite.

## Style

Short sentences and plain words. State facts as they are now ("X is MIT-licensed"), not how the team got there ("X moved to MIT in 0.8.0"). Leave out session names, run IDs, and anything private to the people involved. Read the whole record before you edit it, and edit so it still reads as one piece.

Never write a placeholder, an open question, or a note to the maintainer into an ADR or a design document. What you write is final. Bring up in chat only what truly needs the maintainer's judgment, and for everything else take the answer the evidence supports that claims the least on their behalf, and list those calls in your report. Before you qualify or cut a sentence, name the false or unverified fact it states. If you can't, leave it as written.

## Checklist

- [ ] **It passes the test.** The record states its architecturally significant requirement, other parts of the system rest on it, and undoing it would cost what step 1 describes.
- [ ] **One decision,** in about a page, with no specification, table of rules, or history in it.
- [ ] **Every option was weighed at the time,** or is marked as later research with its date.
- [ ] **Every reason is in the record** it came from. Nothing inferred is written as decided.
- [ ] **A bad consequence is listed,** and one is about operating or maintaining the system.
- [ ] **Confidence says "better"** only with a recorded comparison.
- [ ] **Confirmation lists a real check,** or says there is none. Every test, path, and number cited exists.
- [ ] **The number is new,** above the highest ever used.
- [ ] **Nothing cites a deleted record** as current, and the index matches the folder.
- [ ] No gotcha below describes the record.

## Gotchas

- Writing an ADR for every decision made carefully, so the log grows until nobody reads it. Most belong in a design document.
- Marking a replaced ADR "superseded" and keeping it, so readers and agents follow a dead decision.
- Adding a dated note to an accepted ADR, then another that corrects the first, where one restated record was needed.
- Writing a new ADR that says which sentences of the old one it replaces, and leaving the old one standing.
- Shortening an ADR and losing options or consequences on the way.
- Inventing an option that could never have been chosen, so the list reaches two.
- Presenting alternatives found today as the reasons for a decision made earlier.
- Naming the maintainer as the decider of a mechanism an agent chose within the maintainer's constraint.
- Quoting the user's words from the conversation in a record, or recounting what they said, where everyone who opens the repository reads it.
- Writing "Confidence: high" for a decision whose deciders never said, or claiming proof that no test gives.
- Putting notes in `status`, such as "accepted; its retry rule superseded by ADR 23".
- Taking the next number from the files present, and reusing a deleted record's number.
- Leaving the index, a code comment, or a design document citing a record that is gone.
- Listing only consequences that are pleasant or obvious.
- Ending an ADR with open questions.
