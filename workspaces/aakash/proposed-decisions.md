# Proposed decisions from aakash - for merger review

> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Pending

### DEC-010: Payments architecture - build gated, enable in Phase 1.5
**Date:** 2026-08-24
**Participants:** Aakash, Elvis
**Status:** PENDING

**Decision:** Payments (event ticketing with a 10 percent platform fee on ticket sales, plus a gated
premium-feature unlock tier) are architected into the Phase 1 codebase from the start as toggle-able
provisions, but are not wired live until the end of Phase 1 ("Phase 1.5"). Wepop uses Programination's
existing Stripe account rather than a new dedicated account. Elvis includes the payments vision and
requirements in the design docs now so the structure is built for it from day one, even though the
live build is deferred.
**Reasoning:** Getting the core Phase 1 structure (the demo-ready product) done first keeps the
investor-facing milestone on track, while still baking payments into the architecture so enabling it
later is a toggle, not a rebuild. AI-assisted build makes the payments piece fast to complete once the
structure is solid.
**Impact:** Phase 1 build includes payment provisions (gated, not live). Payments (ticketing plus fee,
premium unlocks) become a Phase 1.5 milestone. Elvis updates the docs to reflect payments
requirements. No new Stripe account needed; Programination's existing account covers Wepop.

## Landed

- 2026-08-17: DEC-001 to DEC-009 landed into `shared/DECISIONS.md` from the 2026-08-17 Wepop
  progress walkthrough. Nothing pending.
