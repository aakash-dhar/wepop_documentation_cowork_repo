---
name: alignment-check
category: maintenance
description: >
  Cross-checks any incoming artifact (a design drop, a spec, a transcript, a client email) against
  the source of truth (DECISIONS.md, the scope matrix, the product overview) and produces a
  said-vs-produced divergence report tagged MATCH / CHANGED / ADDED / DOCS-DISAGREE / OPEN, with
  evidence quotes. The repeatable version of the 2026-08-18 walkthrough-vs-drafts review aid.
  Read-only on shared/; writes a report to comms/attachments/ or chat. Flags conflicts, proposes
  nothing. Triggers on "alignment check", "does this match our decisions?", "review this draft
  against the record". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: alignment-check (Wepop)

> `[you]` = the caller's workspace name. Read-only on `shared/`. Output is a report for the PM;
> if it will be shared with Elvis it is client-facing, so it ends "for Aakash to review/send."

## Trigger
- "alignment check", "does this match our decisions?", "check this against our decisions", "review
  this draft against the record", "what diverged?". Good to run after `design-intake` or
  `process-transcript`, and on every revised draft Elvis sends.

## Pre-read
1. `shared/DECISIONS.md` (the locked record that controls).
2. `architecture/phase-plan/wepop-scope-matrix.md` and `wepop-product-overview.md` (phase and scope).
3. `shared/HOTSHEET.md` (open items, risks) and the relevant transcript or prior artifact.
4. The artifact under review (design drop, spec, email, transcript).

## Status tags
`MATCH` reflects a decision or what was said; `CHANGED` a different call than was stated;
`ADDED` present in the artifact but never decided or discussed; `DOCS-DISAGREE` two owned artifacts
contradict each other; `OPEN` a genuinely unresolved item.

## Steps
### Step 1 - Extract every checkable claim from the artifact (feature, number, name, flow, screen).
### Step 2 - Classify each against the record: assign one status tag and quote both sides (the artifact and the decision or source). Never assert alignment without both quotes.
### Step 3 - Rank: DOCS-DISAGREE and CHANGED-vs-a-locked-decision first, then ADDED scope, then OPEN, then MATCH (brief). Lead with a short "top items to confirm".
### Step 4 - Route, do not resolve: a genuine new decision goes to `propose-decision`; a same-topic clash between two owned docs is noted for `run-merge` / MERGE-REVIEW; a scope question goes to `scope-tracker`. This skill records divergences, it does not settle them.
### Step 5 - Deliver the report (chat, or a dated file in `comms/attachments/`). If it is going to Elvis, end "for Aakash to review/send." Suggest a commit if a file was written.

## Never
- Assert a match or a conflict without quoting both the artifact and the source.
- Write `shared/` directly, or propose or land a decision automatically.
- Treat the artifact as authoritative over `shared/DECISIONS.md` (DECISIONS controls).
- Em-dash; DENY.
