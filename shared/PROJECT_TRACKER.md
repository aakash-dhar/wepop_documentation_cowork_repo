# PROJECT_TRACKER.md - Wepop single-snapshot status

> Merger-only file. A derived, at-a-glance roll-up of where WEP001 stands, in one screen. Regenerated
> by the **update-tracker** skill from the source-of-truth files; do not hand-author it divergently.
> When any line here disagrees with `shared/DECISIONS.md`, DECISIONS wins and this file is stale until
> refreshed. No em-dashes. Governance values ALLOW / BLOCK / ESCALATE, never DENY.

**As of:** 2026-09-02
**Sources rolled up:** DECISIONS.md, HOTSHEET.md, PROJECT_INDEX.md, MERGE-REVIEW.md,
architecture/phase-plan/ (product overview, scope matrix, compliance register), comms/todos.md

---

## Snapshot

| Field | Value |
|-------|-------|
| Project | WEP001 - Wepop |
| Phase | Phase 1 design deepening (build not started; repo migrating to BetaCraft GitHub) |
| RAG | Green with a watch - a large batch landed 2026-09-02 (DEC-048 to DEC-066: the open-questions call plus Elvis's Moments and org-membership proposals). No hard build blocker; three launch blockers still open: moderation capability, 위치정보법 KCC registration, and the CSAM runbook |
| Last decision | DEC-066 (org-membership model: one account, membership vs following, org-flagged content, detach), 2026-09-02 |
| Decisions landed | DEC-001 to DEC-066 (2026-09-02 batch: DEC-048 to DEC-063 from the aakash intake and DEC-064 to DEC-066 from Elvis's Moments and org-membership proposals) |
| Open conflicts in merge queue | 0 conflicts; 1 item held for client sign-off (the DEC-011 password/recovery amendment) |
| Review-needed direct pushes outstanding | 0 |

---

## Milestones

| Milestone | Target | Status |
|-----------|--------|--------|
| First full design walkthrough | 2026-08-17 | Done (Elvis, Aakash, Deepak) |
| GitHub repo + invite + Cowork setup call | 2026-08-19 | Done (setup call held) |
| Elvis design batch (payments, cohorts, algorithm, features) | 2026-08-25 | Done, landed as DEC-010 to DEC-025 on 2026-08-26 |
| Elvis refinement batch (language, home-location, cohort, Explore gate, paid quota) | 2026-08-27 | Done, landed as DEC-029 to DEC-033 on 2026-08-28 |
| Handoff spec v0.9 intake + phase-1/1.5 review batch | 2026-08-30 | Done, landed as DEC-034 to DEC-047 on 2026-08-31 |
| Governance audit + open-questions call + Moments/org proposals | 2026-09-02 | Done, landed as DEC-048 to DEC-066 on 2026-09-02 |
| BetaCraft GitHub repo migration (Aakash migrates, Elvis re-syncs) | In progress | Open (TASK-044; Elvis frozen until Aakash confirms) |
| Moderation capability (owner, admin queue, guideline, CSAM runbook, gambling blocklist) - launch blocker | Before launch | Open (TASK-034, TASK-039, TASK-042) |
| Legal register L-1 to L-12 to DLG Law (L-3 위치정보법 P0, L-8 into age consult) | Before P0 / launch | Open (TASK-040) |
| Payments/ticketing build scope decision (Korea non-Stripe path in play) | TBD | Open (own conversation, TASK-036) |
| Phase-1 build kickoff | After scope + moderation lock | Not started |

---

## Needs a decision

Open questions (not yet decisions), from the HOTSHEET and the 2026-09-02 merge:

- Three launch-blocking legal/ops gates on the HOTSHEET: moderation capability (admin queue, urgent-report
  alerts, one-page guideline; SLAs deferred until hiring), 위치정보법 KCC registration for the geofenced
  check-in mode (likely de-blocked by DEC-046 self-scan deferral, DLG to confirm), and the CSAM
  preserve-and-report runbook.
- DEC-064 open: the org-paid Moment video length (whether every attendee of a paid-org event gets the 30s
  cap, with a notice, or members-only) remains explicitly undecided; Elvis is reconsidering.
- DEC-063 open: media-retention window (6 vs 12 months before downgrade) left for later; the launch
  free-trial defers its practical effect.
- DEC-060 open (Elvis research): whether an archived idea can be un-archived, and whether commenting on an
  archived idea is allowed (commenting would revive it).
- DEC-048 open: two private-account design sub-items (approval-queue UX, and whether declining a follow
  request notifies the requester); stranger-view and findability were answered by DEC-065.
- DEC-044 open: re-registration cooldown, ban-list retention, minimum account age for org creation and
  member tenure for a suspension-triggered transfer, whether suspension propagation is reviewer-gated.
- DEC-054 open: the Korea map provider (Google vs Naver/Kakao), now Needs Attention on the HOTSHEET, and
  the location-poll sub-mechanics; DEC-057 open: personality-tags single vs multi-select per section.
- Held for client sign-off: the DEC-011 password/recovery amendment (optional password reinstated,
  phone-first recovery), on the Elvis meeting agenda.
- Korea map provider feasibility (whether a non-Korean business can open a Naver/Kakao developer account).
- Commercial-structure proposal channel and the PROJECT_STRATEGY.md rewrite (DEC-018, TASK-037).
- Age/location logic pending counsel (DEC-012, TASK-013); PIPA 만 14세 미만 guardian consent (L-8) folds in.
- How much legacy Wepop code is reused vs rebuilt (DEC-008); the code tree is old salvage, build not started.

ESCALATE (financials owner): freemium/commercial structure (DEC-018); the launch free-trial approach
(DEC-063) and Explore-filters-free (DEC-058), both landed with a financials note; the Moments-doc budget
line, DLG Law counsel, and named contacts; the ticketing/payments build and the Korea non-Stripe path.

---

## Risks (from HOTSHEET Risk Register Snapshot)

| # | Risk | Severity (Likelihood x Impact) | Owner | Status |
|---|------|-------------------------------|-------|--------|
| R1 | Cross-jurisdiction age verification is legally messy; locking the DEC-012 logic before counsel could ship a non-compliant flow | Medium x High | Aakash | ACTIVE (in-flight) |
| R2 | Solo-founder blind spot: Elvis designing alone, calls may go unchallenged | Medium x Medium | Aakash | ACTIVE |
| R3 | OTP/SMS deliverability blocked by geography without an in-region business | Low x Medium | Aakash | ACTIVE |
| R4 | Single-reviewer moderation: one reviewer covering eleven target types across five live UGC surfaces | Medium x High | Elvis | ACTIVE |
| R5 | 위치정보법 registration exposure on the printed-poster check-in geofence | Medium x High | Aakash | ACTIVE |

Note: content moderation is both a Blocking HOTSHEET item and formal risk R4. Informal watch items: a user
who never grants GPS has no path to update a stale home location (DEC-031); the Explore gate's
current-location integrity depends on GPS resisting spoofing (DEC-031/DEC-032).

---

## Open action items

| Item | Owner | Due / Since |
|------|-------|-------------|
| Migrate the repo to BetaCraft GitHub, send Elvis sync steps (Elvis frozen until confirmed) | Aakash | Since 2026-09-02 (TASK-044) |
| Stand up content moderation (admin queue, urgent alerts, guideline) - launch blocker | Aakash/Deepak | Since 2026-08-26 (TASK-034) |
| Write the CSAM preserve-and-report runbook, DLG-reviewed | Elvis (draft), Aakash (review) | Before launch (TASK-039) |
| Add gambling to the moderation blocklist (도박죄, rides on DEC-051) | Elvis (mod), Aakash | Before launch (TASK-042) |
| Route the legal register L-1 to L-12 to DLG (L-3 P0, L-8 into TASK-013) | Aakash | Before P0 (TASK-040) |
| Korean-label review of the taxonomy v2.0 | Korean-label reviewer | Before launch (TASK-043) |
| Build the project-reference comment-sync workflow | Aakash | Since 2026-09-02 (TASK-045) |
| Adopt the I-N invariant registry into CLAUDE.md, re-scope I-12 | Aakash | Open (TASK-041) |
| Resolve the Korea payments path (non-Stripe processors) | Aakash | Since 2026-08-26 (TASK-036) |
| Review every phase-1 feature against the docs and finalize design screens | Elvis | Since 2026-08-26 (todos #14) |
| Pull the repo, set up Cowork, research Korean PASS authentication | Deepak | Since 2026-08-26 (todos #15) |

> Full action-item list lives in `comms/todos.md`; full task tracking in `shared/TASK-BOARD.md` (now
> through TASK-045). This is the headline set. Age/location counsel (TASK-013) remains open and does not
> retire R1 or lift DEC-012's provisional status.

---

## Merge queue

- Open conflicts: none. One item held for client sign-off in `shared/MERGE-REVIEW.md`: the DEC-011
  password/recovery amendment (amends a locked decision, not discussed on the 2026-09-02 call, on the
  Elvis meeting agenda).
- Escalations pending (financials): freemium/commercial structure, the launch free-trial and
  Explore-filters-free financials notes, the Moments-doc budget/legal items, and the ticketing/payments
  build including the Korea non-Stripe path.

---

_Refresh this file with the **update-tracker** skill after a merge run, a design intake, or when a
decision or risk changes._
