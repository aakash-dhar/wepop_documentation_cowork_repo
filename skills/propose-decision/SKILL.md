---
name: propose-decision
category: ingestion
description: >
  Files a technical or strategic decision as a PROPOSAL into workspaces/[you]/proposed-decisions.md
  for the Wepop repo (shared/DECISIONS.md is merger-owned). Confirms details before writing.
  Triggers on "propose this decision", "log this decision", "record that we decided to X"; also
  auto-triggered by archive-email and process-transcript. Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: propose-decision (Wepop)

> [you] = the caller's workspace name.

## Trigger
- "propose this decision", "log this decision", "record that we decided to [X]", "add this to the decision log"; auto-triggered by archive-email and process-transcript.

## Pre-read
1. `shared/DECISIONS.md` (highest DEC number).
2. `workspaces/[you]/proposed-decisions.md` (higher proposed numbers).
3. Next number = max(both) + 1.

## Steps
### Step 1 - Determine the next DEC number (never reuse).
### Step 2 - Confirm details and wait: Title, Type (Technical / Strategic / Commercial / Operational), Participants, Decision (one sentence), Rationale, Relates to, Evidence.
### Step 3 - Append a `## DEC-NNN (PROPOSED)` block: Date, Type, Participants, Decision, Rationale, Relates to, Evidence, Status: Awaiting merger.
### Step 4 - Note any refinements or conflicts with existing DECs explicitly for the merger.
### Step 5 - Suggest a commit.

## Never
- Write to `shared/DECISIONS.md` directly; reuse or skip a number; propose without confirming; em-dash; DENY.
