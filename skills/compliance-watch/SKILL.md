---
name: compliance-watch
category: maintenance
description: >
  Maintains a legal, privacy, and compliance register for Wepop and flags any decision or design
  that touches it: age gating (DEC-002, R1), OTP/SMS deliverability by region (R3), PIPA and personal
  data, photos of identifiable people, minors, moderation, and DLG Law open items. Lives at
  architecture/phase-plan/wepop-compliance-register.md (Aakash-owned; others suggest). Grounded in a
  decision, a design, or a law reference, never invented; rising exposure routes a proposed risk.
  Triggers on "compliance watch", "compliance check", "does this touch legal/privacy?", "update the
  compliance register", "what legal items are open?". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: compliance-watch (Wepop)

> `[you]` = the caller's workspace name. The register lives under `architecture/phase-plan/`
> (Aakash-owned); other callers suggest. This skill surfaces and tracks exposure. It is not legal
> advice: unresolved legal questions route to counsel (DLG Law) and are marked pending-counsel.

## Trigger
- "compliance watch", "compliance check", "does this touch legal or privacy?", "update the
  compliance register", "what legal items are open?". Good to run after a decision lands or a design
  is intaken.

## Register format
`| Item | Area | Requirement | Linked DEC / LC | Status | Owner |`
- Area: age / privacy / consent / deliverability / minors / moderation / data-retention.
- Status: `open` / `mitigated` / `pending-counsel` / `closed`.

## Pre-read
1. `shared/DECISIONS.md` and `shared/HOTSHEET.md` (risk register R1-R3).
2. The compliance register (if it exists) and `comms/todos.md` legal items.
3. The Moments spec LC-1..LC-8 and OQ-7 / OQ-8 when a Moments artifact is in play; the artifact under review.

## Steps
### Step 1 - Identify the change or query and map it to a compliance area.
### Step 2 - Ground it in a decision, a design, or a law reference. Flag anything not backed as an `assumption`, do not assert it as settled.
### Step 3 - Update the register: if the caller owns `architecture/phase-plan/`, write it; otherwise write a `suggestions/suggestion-compliance-*.md`.
### Step 4 - If exposure rises (a new or worsened legal risk), route a proposed risk via `risk-register` (proposal, merger lands it). Mark items needing counsel `pending-counsel` and name the owner (Aakash / DLG Law).
### Step 5 - Report the open and pending-counsel items; suggest a commit.

## Never
- Give settled legal advice; anything unresolved is `pending-counsel`, routed to counsel.
- Assert a compliance status without a decision, design, or law reference (mark it an assumption).
- Write `shared/` directly (risks go via `risk-register`); write `architecture/phase-plan/` when not the owner.
- Em-dash; DENY.
