# Proposed tasks from elvis - for merger review

> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Pending

<<<<<<< HEAD
## Proposed Task
**Date:** 2026-08-30
**Proposed by:** Elvis
**Task:** Route the handoff spec's legal register (L-1 to L-12) to DLG Law as a single consult, with L-3
treated as a P0 blocker and L-8 folded into the existing TASK-013 age/location consult
**Suggested owner:** Aakash
**Why / context:** The handoff spec carries a twelve-item legal register that has never been routed
anywhere. Two items are genuinely new rather than restatements of known issues. **L-3** (위치정보법:
the printed-poster check-in geofence is location-data collection and may require 위치기반서비스사업 신고
to the KCC) is marked BLOCKING before P0 by the handoff itself and is distinct from TASK-013, which
scopes the age/location logic rather than the question of collecting location data at all. **L-8** (PIPA
만 14세 미만 guardian consent) is a genuinely new angle on the age gate: TASK-013 and DEC-012 have been
framed around adult-age thresholds (US 18, Korea 19, Germany 16), and the under-14 guardian-consent
requirement applies regardless of the target audience being university students, so it is the same
consult rather than a separate one. The remaining items (L-1 peer affinity records as personal data, L-2
gender collection purpose limitation, L-4 EXIF/GPS stripping as a release gate, L-5 and L-11 정보통신망법
takedown and 임시조치 procedure, L-6 and L-7 subscription and in-app payment provisions, L-9 FSC
선불전자지급수단 for the deferred points economy, L-10 data retention and deletion) are lower priority
individually but cheaper to answer in one consult than piecemeal. Source: handoff spec §16; companion
HOTSHEET entry for L-3 filed 2026-08-30.
**Priority:** High

## Proposed Task
**Date:** 2026-08-30
**Proposed by:** Elvis
**Task:** Adopt the handoff spec's I-N invariant numbering into `CLAUDE.md` as a maintained registry,
with I-12 re-scoped to distinguish participant rating from host rating
**Suggested owner:** Aakash
**Why / context:** The handoff spec cites invariants by ID (I-6 through I-20) and marks several as
"Existing", but no such registry exists in this repo. `CLAUDE.md` section 8 carries key invariants as an
unnumbered bullet list, so the IDs currently refer to nothing a reader here can look up, and future
documents citing I-9 or I-11 cannot be checked against anything. Adopting the scheme makes the citations
resolvable. **One correction is required before adoption, not after:** I-12 as drafted reads "no mechanic
may create a persistent peer rating of an individual that is visible to anyone," which forbids host
ratings on its face and therefore contradicts DEC-014. Elvis confirmed 2026-08-29 that host rating and
attendee rating are separate concepts and host rating is permitted; replacement wording carrying that
distinction explicitly is drafted in `handoff-spec-v0.9-intake-2026-08-29.md` item A. Adopting the
numbering without that fix would land a contradiction into the invariant registry. **A correction to that correction, 2026-08-31**
(`ratings-checkin-2026-08-31.md`): the 2026-08-29 replacement wording also widened the invariant from the
handoff's "visible to anyone" to "whether visible or internal". That widening was a drafting error, not a
decision, and it contradicts DEC-014 a second way, since DEC-014 explicitly permits an internal-only
attendee signal ("attendee thumbs are an internal recommendation signal only, never shown to anyone").
Adopt the **visibility-scoped** version: I-12 prohibits a persistent peer rating of a participant that is
visible to anyone; internal signals are permitted, and making one visible or using it to gate event access
is a separate decision requiring its own review; host rating is out of scope and permitted. Note also that
`CLAUDE.md` section 8 has a known stale line flagged 2026-08-26 (the phone-OTP invariant predating
DEC-011), worth correcting in the same pass. Source: handoff spec §13; intake review item A and Part 5.
**Priority:** Medium
=======
_Queue is empty. Nothing pending._
>>>>>>> 9232f52265c666b151966dbeb0d86f0f40b141b6

## Landed

- 2026-08-31: Three tasks landed onto `shared/TASK-BOARD.md` by the merger via task-board, each with a
  `team/tasks/` detail file. TASK-039 (CSAM preserve-and-report runbook; owner Elvis draft, Aakash DLG
  review), TASK-040 (route the handoff legal register L-1..L-12 to DLG as one consult, L-3 P0, L-8 into
  TASK-013; owner Aakash), TASK-041 (adopt the I-N invariant registry into CLAUDE.md, re-scope I-12, fix
  the stale phone-OTP line; owner Aakash). Source: `handoff-spec-v0.9-intake-2026-08-29.md`.

- 2026-08-18: Landed as TASK-016 (event location map picker) into shared/TASK-BOARD.md, owner Deepak.
