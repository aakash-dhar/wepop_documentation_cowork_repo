---
name: update-tracker
category: maintenance
description: >
  Regenerates the single at-a-glance team status roll-up at
  shared/PROJECT_TRACKER.md from the source-of-truth files (DECISIONS, HOTSHEET,
  PROJECT_INDEX, MERGE-REVIEW, the phase-plan scope matrix and product overview,
  and comms/todos.md). A derived snapshot, never hand-authored divergently;
  DECISIONS always wins over any stale line. Merger-owned (Aakash writes shared/
  directly); other callers write a suggestion. Does no git. Triggers on "update
  the tracker", "refresh the tracker", "project tracker", "where does the project
  stand?". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: update-tracker (Wepop)

> `[you]` = the caller's workspace name. `shared/PROJECT_TRACKER.md` is
> merger-owned; only Aakash writes it directly. Others produce a suggestion.
> The tracker is a DERIVED view, like the dashboard but internal and in
> markdown. It never introduces a fact of its own; every line is rolled up from
> a source file, and DECISIONS.md always wins.

## Trigger
- "update the tracker", "refresh the tracker", "project tracker", "refresh
  project status", "where does the project stand?". Suggested at the end of a
  **run-merge** run when the status picture changed.

## Pre-read (the roll-up sources, in order)
1. `shared/DECISIONS.md` - phase, last DEC, anything that overrides a stale line.
2. `shared/PROJECT_INDEX.md` - RAG, phase, team, what-is-being-built.
3. `shared/HOTSHEET.md` - blockers, needs-attention, watching, and the Risk
   Register Snapshot.
4. `shared/MERGE-REVIEW.md` - open conflict count and any escalations.
5. `architecture/phase-plan/wepop-product-overview.md` and the scope matrix -
   milestones and phase line.
6. `comms/todos.md` - open action items (surface the headline set).
7. The current `shared/PROJECT_TRACKER.md` (to diff and to keep the format).

## Steps

### Step 1 - Gather current state
Read every source above. Do not infer anything not present in them. If a source
disagrees with DECISIONS.md, use DECISIONS and note the stale source for a
follow-up (do not silently reconcile it - that is a discrepancy; flag it).

### Step 2 - Regenerate each section
Rebuild the fixed sections of PROJECT_TRACKER.md from the sources: Snapshot
(project, phase, RAG + one-line reason, last DEC, open-conflict count,
review-needed count), Milestones, Needs a decision, Risks (mirror the HOTSHEET
snapshot), Open action items (headline set, pointer to comms/todos.md), Merge
queue. Update the "As of" date to today. Keep it to one screen; the tracker
summarizes, it does not duplicate the full files.

### Step 3 - Write or suggest
If `[you]` is aakash, write the regenerated file to `shared/PROJECT_TRACKER.md`,
preserving the header and format. Otherwise write
`workspaces/[you]/suggestions/suggestion-tracker-YYYY-MM-DD.md` with the proposed
new content for Aakash to land.

### Step 4 - Report and suggest a commit
Report what changed since the last snapshot (RAG move, new DEC, new/retired risk,
milestone flip). Suggest a `[you] refresh PROJECT_TRACKER` commit for GitHub
Desktop. If the client-facing picture changed too, suggest **dashboard-update**.

## Never
- Introduce a status fact not present in a source file; contradict a locked
  decision (DECISIONS wins); silently reconcile a source that disagrees with
  DECISIONS (flag it for the merger).
- Write `shared/PROJECT_TRACKER.md` when not the merger (write a suggestion).
- Run git commit / push; em-dash; DENY.
