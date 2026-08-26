# PROJECT_TRACKER.md - Wepop single-snapshot status

> Merger-only file. A derived, at-a-glance roll-up of where WEP001 stands, in one screen. Regenerated
> by the **update-tracker** skill from the source-of-truth files; do not hand-author it divergently.
> When any line here disagrees with `shared/DECISIONS.md`, DECISIONS wins and this file is stale until
> refreshed. No em-dashes. Governance values ALLOW / BLOCK / ESCALATE, never DENY.

**As of:** 2026-08-26
**Sources rolled up:** DECISIONS.md, HOTSHEET.md, PROJECT_INDEX.md, MERGE-REVIEW.md,
architecture/phase-plan/ (product overview, scope matrix, compliance register), comms/todos.md

---

## Snapshot

| Field | Value |
|-------|-------|
| Project | WEP001 - Wepop |
| Phase | Phase 1 design deepening (build not started) |
| RAG | Green with a watch - design substantially deeper (DEC-010 to DEC-025 landed); no hard build blocker, but moderation staffing is a launch blocker to resolve |
| Last decision | DEC-025 (new-feature scoping batch), 2026-08-25, landed 2026-08-26 |
| Decisions landed | DEC-001 to DEC-025 (DEC-002/004/009 superseded, DEC-006 extended) |
| Open conflicts in merge queue | 0 |
| Review-needed direct pushes outstanding | 0 |

---

## Milestones

| Milestone | Target | Status |
|-----------|--------|--------|
| First full design walkthrough | 2026-08-17 | Done (Elvis, Aakash, Deepak) |
| GitHub repo + invite + Cowork setup call | 2026-08-19 | Done (setup call held) |
| Elvis design batch (payments, cohorts, algorithm, features) | 2026-08-25 | Done, landed as DEC-010 to DEC-025 on 2026-08-26 |
| Product overview + scope matrix + compliance register refreshed | 2026-08-26 | Done |
| Moderation model + owner (launch blocker) | Before launch | Open |
| Payments/ticketing build scope decision | TBD | Open (own conversation) |
| Phase-1 build kickoff | After scope + moderation lock | Not started |

---

## Needs a decision

Open questions (not yet decisions), from the HOTSHEET:

- Whether the cohort hard filter reverts to a ranking signal once a city softens, and who owns the
  manual per-city density call (DEC-019 / DEC-020). Confirm with Elvis.
- Two undesigned prerequisites for group-dynamics recommendations: a general user-blocking feature
  and an attendee-level feedback mechanism (DEC-023).
- Free Now open details (account-standing threshold, duration cap, archival, org rooms); live-stories
  vs the org media cap; whether the Event model supports a multi-day date range (DEC-025).
- Commercial-structure proposal channel and the PROJECT_STRATEGY.md rewrite (DEC-018).
- Age/location logic pending legal counsel (DEC-012, TASK-013). Map-picker interaction detail.
- How much legacy Wepop code is reused vs rebuilt (DEC-008).

ESCALATE (financials owner): freemium/commercial structure (DEC-018); the Moments-doc ~$100K budget
line, DLG Law counsel, and named contacts (conflict-review item 10); the ticketing/payments build.

---

## Risks (from HOTSHEET Risk Register Snapshot)

| # | Risk | Severity (Likelihood x Impact) | Owner | Status |
|---|------|-------------------------------|-------|--------|
| R1 | Cross-jurisdiction age verification is legally messy; locking the DEC-012 logic (superseded DEC-002) before counsel could ship a non-compliant flow | Medium x High | Aakash | ACTIVE (in-flight) |
| R2 | Solo-founder blind spot: Elvis designing alone, calls may go unchallenged | Medium x Medium | Aakash | ACTIVE |
| R3 | OTP/SMS deliverability blocked by geography without an in-region business (email magic-link now covers recovery per DEC-011) | Low x Medium | Aakash | ACTIVE |

Note: content moderation is tracked as a Blocking item on the HOTSHEET rather than a numbered risk;
promote to R4 via risk-register if a formal risk entry is wanted.

---

## Open action items

| Item | Owner | Due / Since |
|------|-------|-------------|
| Stand up content moderation (owner, SLA, tooling) - launch blocker | Aakash | Since 2026-08-26 (TASK-034) |
| Confirm cohort softening transition + density-call owner with Elvis | Aakash | Since 2026-08-26 (TASK-035) |
| Update the docs with the payments vision + requirements | Elvis | Ongoing, since 2026-08-24 (todos #12) |
| Present community-segmentation options | Aakash | 2026-08-26 (todos #13; now largely resolved by DEC-019) |
| Send the reviewed / consolidated project documentation | Elvis | Since 2026-08-18 (todos #1, TASK-010) |
| Consult counsel on age/location logic | Aakash | Open (todos #4, TASK-013) |

> Full action-item list lives in `comms/todos.md`; full task tracking in `shared/TASK-BOARD.md`
> (now through TASK-037). This is the headline set.

---

## Merge queue

- Open conflicts: none. See `shared/MERGE-REVIEW.md`.
- Escalations pending (financials): freemium/commercial structure and the Moments-doc budget/legal
  items above.

---

_Refresh this file with the **update-tracker** skill after a merge run, a design intake, or when a
decision or risk changes._
