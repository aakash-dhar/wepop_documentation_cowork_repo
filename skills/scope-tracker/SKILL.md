---
name: scope-tracker
category: maintenance
description: >
  Maintains the Wepop phase and feature matrix so the phase-1 line (per DEC-009) and deferred work
  stay visible. Tracks each feature by phase, status, owner, and linked decision, grounded only in
  a decision or a design (never invented scope). Lives at architecture/phase-plan/wepop-scope-matrix.md
  (Aakash-owned; others suggest). Triggers on "scope tracker", "update the scope matrix", "what's in
  phase 1?", "is this in scope?", "reclassify [feature]". Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: scope-tracker (Wepop)

> [you] = the caller's workspace name. `architecture/phase-plan/` is Aakash-owned; other callers suggest.

## Trigger
- "scope tracker", "update the scope matrix", "what's in phase 1 / a later phase?", "is this in scope?", "reclassify [feature]", "mark [feature] built / deferred".

## Matrix format
`| Feature | Area | Phase | Status | Owner | Linked DEC | Notes |`
- Phase: `1` or `later`. Status: `proposed` / `decided` / `designed` / `in-build` / `done` / `deferred`.

## Pre-read
1. `shared/DECISIONS.md` (phase and scope are grounded here); `architecture/phase-plan/wepop-product-overview.md`.
2. The existing scope matrix; `shared/HOTSHEET.md`.

## Steps
### Step 1 - Identify the change: add a feature, reclassify a phase, update a status/owner, or just show the matrix.
### Step 2 - Ground every phase and status in a decision (cite the DEC) or a design intake. Flag any feature whose phase or status is not backed by a decision as `proposed` and note it, rather than asserting scope.
### Step 3 - Show mode: list phase-1 vs later, and anything `proposed` (unbacked) needing a decision.
### Step 4 - Write mode: if the caller owns `architecture/phase-plan/`, write the matrix back; otherwise write a `suggestions/suggestion-scope-*.md` for Aakash. Queue an update-index refresh if the phase picture changed. Report and suggest a commit.

## Never
- Assert a feature's phase or status without a backing decision or design (mark it proposed and flag it); write `architecture/phase-plan/` when not the owner (suggest instead); contradict a locked decision (defer to DECISIONS.md); write `shared/` directly; em-dash; DENY.
