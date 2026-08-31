# Proposed HOTSHEET changes from elvis - for merger review

> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Pending

One entry. The five filed 2026-08-30 all landed; this one updates a Blocking entry that the check-in
direction reversal may have de-blocked.

## Proposed Hotsheet Entry
**Date:** 2026-09-01
**Proposed by:** Elvis
**Source:** `workspaces/elvis/ratings-checkin-2026-08-31.md`; updates the existing Blocking entry
"위치정보법 registration for geofenced check-in (blocking before P0)" and risk R5
**Type:** Blocking
**Summary:** The 위치정보법 blocker may no longer gate P0, because the check-in direction reversed and the
mode that triggers it is deferred with attendee self-scan.
**Key Points:**
- The exposure attaches specifically to the **printed-poster** check-in mode, whose static token needs a
  location radius to resist forgery. Printed posters exist to support **attendee self-scan**.
- Phase 1 check-in reversed on 2026-08-31 to **host-scans-attendee** (ticketing standard), and attendee
  self-scan moved to a deferred **self-service mode**. The poster and its geofence defer with it.
- If that holds, L-3 stops being a gate before P0 and becomes a later-phase legal question.
- **Do not close the item, and do not drop it from the DLG consult (TASK-040).** Re-scope it to a question
  rather than a blocker. The exposure returns intact the day self-service mode is built, and the answer is
  cheaper to have in hand before that work starts than during it.
- Risk R5 should be re-rated on the same basis: same exposure, materially lower near-term likelihood, since
  nothing in phase 1 now collects the location data that triggers it.
- Also worth noting on the same entry: anti-forgery simplifies under the reversal. The 60-second rotating QR
  existed because a host-displayed code could be screenshotted and forwarded; once a host scans a person
  standing in front of them, the host's own eyes are the strongest control available, so a static
  per-attendee credential suffices.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| Check-in reverses to host-scans-attendee; attendee self-scan deferred to self-service mode | Elvis | 2026-08-31 |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Confirm with DLG that deferring attendee self-scan removes the 위치정보법 trigger from phase 1, rather than assuming it | Aakash | Before P0 |
| Re-scope the HOTSHEET Blocking entry and re-rate R5 once DLG confirms | Aakash (merger) | On confirmation |
| Keep L-3 in the TASK-040 consult regardless, scoped as a question for when self-service is built | Aakash | With TASK-040 |

---

## Landed

- **2026-08-31: all five entries filed 2026-08-30 landed** into `shared/HOTSHEET.md` by the merger: the
  content-moderation blocker reframed around capability rather than response time, 위치정보법 registration
  added as Blocking, the CSAM preserve-and-report runbook added as Blocking, the QR check-in Watching entry
  rewritten around no-show rating abuse, and the DEC-023 prerequisites entry moved to Resolved. Companion
  risks R4 (single-reviewer moderation) and R5 (위치정보법 exposure) both landed on the risk register.
- 2026-08-26: the Korea/Stripe payments item was consolidated with Aakash's Korea-payments item and landed
  as a single Needs Attention entry.
