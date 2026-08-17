---
name: spec-sync
category: maintenance
description: >
  Keeps the Wepop product overview (architecture/phase-plan/wepop-product-overview.md) and the
  PROJECT_INDEX "what is being built" section in sync with the source of truth: DECISIONS.md plus
  the latest design intake and scope matrix. Regenerates the overview so it never drifts; DECISIONS
  always wins over the overview. Triggers on "spec sync", "refresh the product overview", "sync the
  spec", or after decisions land or a design drop is processed. Enforces BLOCK-not-DENY and no em-dashes.
---

# Skill: spec-sync (Wepop)

> [you] = the caller's workspace name. `architecture/phase-plan/` is Aakash-owned; `shared/` is merger-only.

## Trigger
- "spec sync", "refresh the product overview", "sync the spec"; auto after propose-decision lands, design-intake, or scope-tracker changes.

## Pre-read
1. `shared/DECISIONS.md` (SOURCE OF TRUTH); `architecture/phase-plan/wepop-product-overview.md`.
2. The latest design-intake catalog; `architecture/phase-plan/wepop-scope-matrix.md`; `shared/PROJECT_INDEX.md`.

## Steps
### Step 1 - Reconcile each feature area of the overview against the latest landed decisions, the design catalog, and the scope matrix.
### Step 2 - Resolve drift: where the overview contradicts a DEC, the DEC wins and the overview is corrected. Where a design adds something not backed by a decision, list it under "Open items" rather than encoding it as decided.
### Step 3 - Write the refreshed overview (if the caller owns `architecture/phase-plan/`; otherwise a `suggestions/suggestion-overview-*.md`). Keep contested points pointing to DECISIONS.md.
### Step 4 - Align PROJECT_INDEX "what is being built" / "what has been decided": if the caller is the merger (Aakash), update `shared/PROJECT_INDEX.md`; otherwise file a `proposed-project-index.md`. Report and suggest a commit.

## Never
- Treat the overview as authority over `shared/DECISIONS.md`; encode undecided design as decided (flag it open); write `shared/` directly when not the merger; write `architecture/phase-plan/` when not the owner; em-dash; DENY.
