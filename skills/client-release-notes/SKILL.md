---
name: client-release-notes
category: delivery
description: >
  Produces a clean, client-facing "what changed and what got decided since [date or version]" for
  Elvis, drawn from landed decisions, design intakes, merges, and resolved and new open items. The
  shareable changelog the versioned, client-shared repo invites; distinct from weekly-digest (internal
  ops) and status-report (RAG exec). Plain, humanized, no internal merge mechanics or blame; grounded
  only in the record. Client-facing, so drafted for Aakash to review and send. Triggers on "release
  notes", "client changelog", "what changed for the client", "changelog since [date]". Enforces
  BLOCK-not-DENY and no em-dashes.
---

# Skill: client-release-notes (Wepop)

> `[you]` = the caller's workspace name. Client-facing: the PM reviews and sends. Output is chat or a
> dated file; it may also feed `dashboard-update`. It reads the record, it does not change `shared/`.

## Trigger
- "release notes", "client changelog", "what changed for the client", "changelog since [date]",
  "notes for Elvis on what moved".

## Pre-read
1. `shared/DECISIONS.md` (decisions landed in the window).
2. `shared/MERGE-REVIEW.md` (resolved) and the latest design intakes / version notes.
3. `shared/HOTSHEET.md` (resolved and new items), `comms/todos.md` (closed), `shared/PROJECT_TRACKER.md`.

## Steps
### Step 1 - Set the window: since the last release notes, or a given date or version.
### Step 2 - Gather what a client cares about: decisions locked, design updates received, things resolved, and what comes next. Leave out internal churn.
### Step 3 - Write it in plain client-facing prose: warm, specific, no jargon, no owner-blame, no merge/conflict mechanics, no em-dashes. Group as "Decided", "In progress", "Next".
### Step 4 - End "for Aakash to review and send." Optionally save to `comms/attachments/` or hand to `dashboard-update`. Suggest a commit if a file was written.

## Never
- Expose internal conflict, merge, or workspace mechanics, or assign blame.
- Include proposed or unlanded items as if done (only landed decisions and confirmed updates).
- Fabricate a delivery date or number not in the record.
- Em-dash; DENY. Client-facing gate: Aakash sends.
