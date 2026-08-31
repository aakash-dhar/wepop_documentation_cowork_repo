# Proposed HOTSHEET changes from elvis - for merger review

> Newest at top. Priority order Blocking, Needs Attention, Watching, Resolved. No em-dashes.
> Governance values ALLOW / BLOCK / ESCALATE.

## Pending

<<<<<<< HEAD
**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Build the internal admin moderation queue plus urgent-report push alerts (feeds TASK-034). Not an SLA commitment, this is the removal path itself | Deepak | Before launch |
| Write the one-page moderation guideline | Elvis | Before launch |
| Confirm with DLG whether 정보통신망법 / 임시조치 takedown windows impose an external response deadline that a single-reviewer setup can actually meet, since statutory windows do not defer with internal targets | Aakash | Before launch |
| Remove "Joy Jeong ops/legal" from the conflict-review item 10 name-confirmation list; that position is being refilled | Aakash | Next merge |
| Revisit response-time SLAs and independent appeal review once a second reviewer exists | Elvis | On hiring |

---

## Proposed Hotsheet Entry
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx` §4.2, §16 item L-3
**Type:** Blocking
**Summary:** The printed-poster check-in mode collects location data and may require
위치기반서비스사업 신고 to the KCC under 위치정보법, which the handoff marks BLOCKING before P0.
**LIKELY DE-BLOCKED 2026-08-31, needs DLG confirmation rather than assumption.** Elvis reversed the
check-in direction the same week: phase 1 now has the host scan the attendee (ticketing-standard), and
attendee self-scan moves to a later self-service mode. The printed poster exists to support attendee
self-scan, so the poster and its location radius defer with it. If that holds, L-3 stops being a gate before
P0 and becomes a later-phase legal question. File it to DLG as a scoped question rather than dropping it,
since the exposure returns intact whenever self-service mode is built.
**Key Points:**
- Check-in has three host-side modes. The printed-poster mode uses a static event-scoped token, so its
  only anti-forgery controls are a server-side time window and a **location radius**. That radius is
  location-data collection, which is what triggers the question.
- Korea's 위치정보법 (Location Information Act) may require registering as a location-based service
  provider (위치기반서비스사업 신고) with the KCC before shipping it. This must be answered by DLG Law
  before the geofence ships.
- **There is a clean fallback if registration proves burdensome**, and it is worth stating up front so
  this does not become a hard stop: drop the radius constraint entirely and rely on the time window plus
  the live-display mode (a QR regenerated every 60 seconds from a short-TTL signed token, where a
  forwarded screenshot dies within a minute). Live display is already the default mode, so the fallback
  costs the printed-poster path some anti-forgery strength rather than costing the feature.
- The stakes are also lower than they look, because of the pending DEC-014 amendment: once Moment and
  feedback eligibility decouple from check-in, a forged check-in unlocks a badge and nothing else.
- Distinct from TASK-013, which scopes the age/location *logic* consult. This is a separate regulatory
  registration question about collecting location data at all.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| None yet. Legal answer required before the geofence ships. | | |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Route L-3 (위치정보법 registration for geofenced check-in) to DLG Law | Aakash | Before P0 |
| If registration is burdensome, drop the radius and ship printed-poster with time-window plus live-display only | Elvis + Deepak | On legal answer |

---

## Proposed Hotsheet Entry
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx` §12.5, §16 item L-12
**Type:** Blocking
**Summary:** A written CSAM preservation-and-report runbook, reviewed by DLG, is required before launch
and does not exist; the default engineering instinct (delete it) is the legally wrong action.
**Key Points:**
- If child sexual abuse material appears it must not simply be deleted. The required handling is
  preserve, restrict access, and report to the authorities. **Deleting destroys evidence.**
- This is a pre-launch requirement, not a post-launch process improvement, and it is specifically a
  *written page* a reviewer can follow without calling Elvis at the moment it happens. With the rota
  currently at one person plus Reviewer B (to be hired), the runbook is what makes the procedure
  transferable to whoever is hired, rather than knowledge living in one head.
- Ties to 불법촬영물 obligations under 전기통신사업법 (L-12), whose user and revenue thresholds are a
  growth trigger rather than a launch trigger; the runbook itself is needed at launch regardless.
- Interacts with the moderation entry above: the urgent lane already auto-hides this content class on
  report, so the runbook governs what happens after auto-hide, not whether it is caught.
- Never reached the HOTSHEET or the risk register despite being a hard pre-launch legal gate.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| None yet. | | |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Write the CSAM preservation-and-report runbook as a one-page procedure any reviewer can follow unaided | Elvis | Before launch |
| Have DLG Law review the runbook | Aakash | Before launch |

---

## Proposed Hotsheet Entry
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** Pending DEC-014 amendment in `workspaces/elvis/proposed-decisions.md` (filed 2026-08-29)
**Type:** Watching
**Summary:** The "QR check-in is load-bearing, low check-in rate is a product risk" entry is being
reversed by a pending proposal and should be rewritten rather than left standing as-is.
**Key Points:**
- The current entry states that check-in gates ratings, host reputation, and the recommendation signal
  (DEC-014), that no scans means no ratings and no recommendation signal, and that no fallback path is
  being built. That was accurate when written on 2026-08-26.
- The pending DEC-014 amendment decouples check-in from both Moment authorship and feedback eligibility.
  A user who joined an event that completed can do both regardless of whether they checked in. Check-in
  now grants a visible verification badge and a scoring weight (1.0 verified, 0.4 unverified), not access.
- **Net effect: the risk drops substantially but does not disappear, and it changes shape.** A low
  check-in rate no longer means no ratings and no recommendation signal; it means a weaker-confidence
  signal and fewer badges. The remaining risk is different and worth watching in its place: with
  eligibility decoupled, a user who RSVP'd and never attended can now rate an event and its host, which
  DEC-014's hard gate had been quietly preventing. The 0.4 weight is the designed mitigation and the
  lever to pull if abuse appears, which is why it is specified as read-time config rather than a
  materialized value.
- Should only be rewritten if and when the DEC-014 amendment actually merges. Filed now so the entry is
  not left contradicting a landed decision at the moment it lands.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| None. Contingent on the pending DEC-014 amendment merging. | | |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| On merging the DEC-014 amendment, rewrite this Watching entry to track no-show rating abuse instead of signal starvation | Aakash (merger) | On merge |

---

## Proposed Hotsheet Entry
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** Pending DEC-023 amendment and general-blocking proposal in
`workspaces/elvis/proposed-decisions.md` (filed 2026-08-29)
**Type:** Resolved
**Summary:** Both undesigned prerequisites for group-dynamics recommendations (DEC-023) are now designed
and filed, so this Needs Attention entry closes on merger.
**Key Points:**
- The entry named two prerequisites: a general user-blocking capability (assumed by DEC-023 to exist,
  never designed) and an attendee-level thumbs up/down post-event feedback mechanism (the avoid-signal
  data source, which did not exist).
- **Blocking is now fully designed** and proposed as a phase-1 safety baseline in the earliest build
  wave: bidirectional and total across every surface including feed, Explore, and comment threads, with
  the scope of the block stated to the user at the moment they block. This also resolves the scope
  matrix's own flagged question ("likely a phase-1 safety baseline, confirm") and the corresponding entry
  in its "Unbacked / needs a decision" section.
- **The attendee-feedback prerequisite is resolved by removing the need for it rather than by building
  it.** Thumbs-down is being removed entirely, so the avoid signal has no negative data source and never
  will. Per Elvis, the avoid signal becomes block-only, and running it on absence of a positive signal was
  explicitly considered and rejected, on the principle that it matters more to focus on what to recommend
  than on what not to recommend.
- The positive tap that replaces thumbs-down is redirected into a positive affinity ranking signal
  alongside DEC-020's social-proximity weight, so DEC-023 gains a usable attendee-level input rather than
  simply losing one.
- Closes on merger of the two pending proposals, not before.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| Avoid signal becomes block-only; absence-of-positive explicitly rejected | Elvis | 2026-08-29 |
| General user blocking confirmed phase-1 baseline, earliest build wave | Elvis | 2026-08-29 |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Move this entry to Resolved once both pending proposals merge | Aakash (merger) | On merge |
| Update the scope matrix row for general user blocking from later/proposed to phase 1, and clear its "Unbacked / needs a decision" entry | Aakash | On merge |
=======
_Queue is empty. Nothing pending._
>>>>>>> 9232f52265c666b151966dbeb0d86f0f40b141b6

---

## Landed

- 2026-08-31: Five HOTSHEET changes landed into `shared/HOTSHEET.md` by the merger. The moderation
  Blocking entry was rewritten around the speed-vs-capability split (SLAs deferred, three pre-launch
  artifacts, statutory duties do not wait). Two new Blocking entries added: 위치정보법 KCC registration
  for the geofenced check-in mode, and the CSAM preserve-and-report runbook. The QR check-in Watching
  entry was rewritten to track no-show rating abuse (on DEC-034). The group-dynamics-prerequisites Needs
  Attention entry moved to Resolved (on DEC-036 and DEC-037). "Joy Jeong ops/legal" removed from the
  conflict-review item 10 name list (position being refilled). Companion risks R4 and R5 landed.
  Source: `handoff-spec-v0.9-intake-2026-08-29.md`.

- 2026-08-26: The Korea/Stripe payments item was consolidated with Aakash's Korea-payments item and
  landed into `shared/HOTSHEET.md` as a single Needs Attention entry by the merger. Source:
  `workspaces/elvis/internationalization-korea-2026-08-26.md`.
