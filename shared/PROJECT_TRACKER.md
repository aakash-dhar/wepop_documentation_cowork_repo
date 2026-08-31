# PROJECT_TRACKER.md - Wepop single-snapshot status

> Merger-only file. A derived, at-a-glance roll-up of where WEP001 stands, in one screen. Regenerated
> by the **update-tracker** skill from the source-of-truth files; do not hand-author it divergently.
> When any line here disagrees with `shared/DECISIONS.md`, DECISIONS wins and this file is stale until
> refreshed. No em-dashes. Governance values ALLOW / BLOCK / ESCALATE, never DENY.

**As of:** 2026-08-31
**Sources rolled up:** DECISIONS.md, HOTSHEET.md, PROJECT_INDEX.md, MERGE-REVIEW.md,
architecture/phase-plan/ (product overview, scope matrix, compliance register), comms/todos.md

---

## Snapshot

| Field | Value |
|-------|-------|
| Project | WEP001 - Wepop |
| Phase | Phase 1 design deepening (build not started) |
| RAG | Green with a watch - design deepened again (DEC-034 to DEC-044 landed 2026-08-31 from the handoff-spec v0.9 intake and the phase-1/1.5 review batch); no hard build blocker, but three launch blockers are open: moderation capability, 위치정보법 KCC registration, and the CSAM runbook |
| Last decision | DEC-044 (host accountability: reputation/enforcement split, ban list, org loophole), 2026-08-30, landed 2026-08-31 |
| Decisions landed | DEC-001 to DEC-044 (DEC-002/004/009 superseded; DEC-006 extended; DEC-016/018/019/027 refined 2026-08-28; DEC-014/015/017/023/025 amended 2026-08-31) |
| Open conflicts in merge queue | 0 |
| Review-needed direct pushes outstanding | 0 |

---

## Milestones

| Milestone | Target | Status |
|-----------|--------|--------|
| First full design walkthrough | 2026-08-17 | Done (Elvis, Aakash, Deepak) |
| GitHub repo + invite + Cowork setup call | 2026-08-19 | Done (setup call held) |
| Elvis design batch (payments, cohorts, algorithm, features) | 2026-08-25 | Done, landed as DEC-010 to DEC-025 on 2026-08-26 |
| Elvis refinement batch (language, home-location, cohort, Explore gate, paid quota) | 2026-08-27 | Done, landed as DEC-029 to DEC-033 on 2026-08-28 |
| Handoff spec v0.9 intake + phase-1/1.5 review batch (feedback, blocking, media, retention, ideas, schedule, accountability) | 2026-08-30 | Done, landed as DEC-034 to DEC-044 on 2026-08-31 |
| Moderation capability (owner, admin queue, guideline, CSAM runbook) - launch blocker | Before launch | Open (TASK-034, TASK-039) |
| Legal register L-1 to L-12 to DLG Law (L-3 위치정보법 P0, L-8 into age consult) | Before P0 / launch | Open (TASK-040) |
| Payments/ticketing build scope decision (Korea non-Stripe path in play) | TBD | Open (own conversation, TASK-036) |
| Phase-1 build kickoff | After scope + moderation lock | Not started |

---

## Needs a decision

Open questions (not yet decisions), from the HOTSHEET and the 2026-08-31 merge:

- Three launch-blocking legal/ops gates on the HOTSHEET: moderation capability (admin queue, urgent-report
  alerts, one-page guideline; SLAs deferred until hiring), 위치정보법 KCC registration for the geofenced
  check-in mode (DLG before the geofence ships, clean radius-drop fallback exists), and the CSAM
  preserve-and-report runbook (DLG-reviewed, written before launch).
- DEC-038 open: a total-video-duration cap per Moment (recommended 150s free / 300s paid, not confirmed)
  and the org-paid Moment video length.
- DEC-039 open: three retention refinements pending Elvis (restore-from-cold Wrapped path, a general
  retrospective-surface capability, a 1080px mid-tier for free full-screen), and per-uploader vs per-room
  retention scope.
- DEC-044 open: re-registration cooldown period, ban-list retention period, minimum account age for org
  creation and member tenure for a suspension-triggered transfer, and whether suspension propagation is
  automatic or reviewer-gated.
- Free Now open details (account-standing threshold, duration cap, archival, org rooms); live-stories vs
  the org media cap.
- Explore country-gate open UI details (DEC-032) and the cohort softening trigger (DEC-030 made the
  density call a single global one; the trigger itself is still open).
- Apply-to-join itself (phase-1.5 placement and design) still unmerged; DEC-033's quota rides along.
- Commercial-structure proposal channel and the PROJECT_STRATEGY.md rewrite (DEC-018, TASK-037).
- Age/location logic pending counsel (DEC-012, TASK-013); the operational todo was deprioritized
  2026-08-31 but the consult and risk R1 stand. PIPA 만 14세 미만 guardian consent (L-8) folds in.
- How much legacy Wepop code is reused vs rebuilt (DEC-008).

ESCALATE (financials owner): freemium/commercial structure (DEC-018); the Moments-doc ~$100K budget line,
DLG Law counsel, and named contacts (conflict-review item 10, ops/legal contact being refilled); the
ticketing/payments build and the Korea non-Stripe path. DEC-039 tiered retention was reviewed and landed
by the financials owner on 2026-08-31 (favorable to the DEC-018 cost model; re-check before ship).

---

## Risks (from HOTSHEET Risk Register Snapshot)

| # | Risk | Severity (Likelihood x Impact) | Owner | Status |
|---|------|-------------------------------|-------|--------|
| R1 | Cross-jurisdiction age verification is legally messy; locking the DEC-012 logic before counsel could ship a non-compliant flow | Medium x High | Aakash | ACTIVE (in-flight) |
| R2 | Solo-founder blind spot: Elvis designing alone, calls may go unchallenged | Medium x Medium | Aakash | ACTIVE |
| R3 | OTP/SMS deliverability blocked by geography without an in-region business (email magic-link now covers recovery per DEC-011) | Low x Medium | Aakash | ACTIVE |
| R4 | Single-reviewer moderation: one reviewer covering eleven target types across five live UGC surfaces; no coverage for sleep/travel/illness, appeals cannot be independent, growth may outpace hiring | Medium x High | Elvis | ACTIVE |
| R5 | 위치정보법 registration exposure: the printed-poster check-in geofence may require 위치기반서비스사업 신고 before shipping in Korea | Medium x High | Aakash | ACTIVE |

Note: content moderation is now both a Blocking HOTSHEET item and formal risk R4. Two design-level watch
items remain informal: a user who never grants GPS has no path to update a stale home location (DEC-031),
and the Explore gate's current-location integrity depends on GPS resisting spoofing (DEC-031/DEC-032).

---

## Open action items

| Item | Owner | Due / Since |
|------|-------|-------------|
| Stand up content moderation (admin queue, urgent alerts, guideline) - launch blocker | Aakash/Deepak | Since 2026-08-26 (TASK-034) |
| Write the CSAM preserve-and-report runbook, DLG-reviewed | Elvis (draft), Aakash (review) | Before launch (TASK-039) |
| Route the legal register L-1 to L-12 to DLG (L-3 P0, L-8 into TASK-013) | Aakash | Before P0 (TASK-040) |
| Adopt the I-N invariant registry into CLAUDE.md, re-scope I-12, fix stale phone-OTP line | Aakash | Open (TASK-041) |
| Confirm cohort softening transition with Elvis (density call now global per DEC-030) | Aakash | Since 2026-08-26 (TASK-035) |
| Resolve the Korea payments path (non-Stripe processors) | Aakash | Since 2026-08-26 (TASK-036) |
| Update the docs with the payments vision + requirements | Elvis | Ongoing, since 2026-08-24 (todos #12) |
| Review every phase-1 feature against the docs and finalize design screens | Elvis | Since 2026-08-26 (todos #14) |
| Pull the repo, set up Cowork, research Korean PASS authentication | Deepak | Since 2026-08-26 (todos #15) |

> Age/location counsel (todos #4, TASK-013) was deprioritized 2026-08-31 as not an immediate blocker; it
> is not a completed consult and does not retire R1 or lift DEC-012's provisional status. Full
> action-item list lives in `comms/todos.md`; full task tracking in `shared/TASK-BOARD.md` (now through
> TASK-041). This is the headline set.

---

## Merge queue

- Open conflicts: none. See `shared/MERGE-REVIEW.md`.
- Escalations pending (financials): freemium/commercial structure, the Moments-doc budget/legal items,
  and the ticketing/payments build (including the Korea non-Stripe path). The DEC-039 tiered-retention
  commercial item was reviewed and landed by the financials owner on 2026-08-31.

---

_Refresh this file with the **update-tracker** skill after a merge run, a design intake, or when a
decision or risk changes._
