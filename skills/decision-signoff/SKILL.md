---
name: decision-signoff
category: delivery
description: >
  When a decision needs the client's explicit yes, packages it as a one-page sign-off brief (the
  question, the options, a recommendation, the impact and reversibility), tracks the sign-off in
  workspaces/[you]/decision-signoffs.md, and on approval hands to propose-decision and the merge.
  Closes the loop that Elvis being both client and approver implies. Client-facing brief drafted for
  Aakash to send. Triggers on "decision signoff", "get Elvis to sign off on [X]", "prepare a
  sign-off", "client approval for [decision]". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: decision-signoff (Wepop)

> `[you]` = the caller's workspace name. Elvis is the client and the client-side approver. This skill
> records the ask and the answer; it never files a decision to `shared/DECISIONS.md` before sign-off
> is recorded, and never writes `shared/` directly (it routes through `propose-decision` + `run-merge`).

## Trigger
- "decision signoff", "get Elvis to sign off on [X]", "prepare a sign-off", "client approval for
  [decision]", "does Elvis need to approve this?".

## Pre-read
1. `shared/DECISIONS.md` (related or superseded decisions) and the topic or source.
2. `architecture/phase-plan/wepop-scope-matrix.md` and `shared/HOTSHEET.md` (impact, risks).
3. `workspaces/[you]/decision-signoffs.md` (the running sign-off tracker).

## Steps
### Step 1 - Frame the decision needing sign-off as one clear question.
### Step 2 - Lay out the options, a recommendation, the impact (what changes), and reversibility. Keep it to one page a client can act on.
### Step 3 - Produce the client one-pager, for Aakash to send. Record the item in `workspaces/[you]/decision-signoffs.md` as `Pending` with the date and owner.
### Step 4 - On "Elvis approved": route to `propose-decision` (next DEC-NNN) then `run-merge` to land it; mark the tracker `Approved (date)`. On "rejected" or "changed": record the outcome and reframe.

## Never
- File or land a decision to `shared/DECISIONS.md` before the sign-off is recorded, or write `shared/` directly (go via `propose-decision` + `run-merge`).
- Present a proposed decision to the client as already approved.
- Bundle several decisions into one sign-off so the answer is ambiguous (one question per sign-off).
- Em-dash; DENY. Client-facing gate: Aakash sends.
