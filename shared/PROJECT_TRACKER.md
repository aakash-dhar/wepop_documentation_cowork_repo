# PROJECT_TRACKER.md - Wepop single-snapshot status

> Merger-only file. A derived, at-a-glance roll-up of where WEP001 stands, in one screen. Regenerated
> by the **update-tracker** skill from the source-of-truth files; do not hand-author it divergently.
> When any line here disagrees with `shared/DECISIONS.md`, DECISIONS wins and this file is stale until
> refreshed. No em-dashes. Governance values ALLOW / BLOCK / ESCALATE, never DENY.

**As of:** 2026-08-28
**Sources rolled up:** DECISIONS.md, HOTSHEET.md, PROJECT_INDEX.md, MERGE-REVIEW.md,
architecture/phase-plan/ (product overview, scope matrix, compliance register), comms/todos.md

---

## Snapshot

| Field | Value |
|-------|-------|
| Project | WEP001 - Wepop |
| Phase | Phase 1 design deepening (build not started) |
| RAG | Green with a watch - design deepened again (DEC-029 to DEC-033 landed 2026-08-28); no hard build blocker, but moderation staffing is a launch blocker to resolve |
| Last decision | DEC-033 (apply-to-join screening question quota), 2026-08-27, landed 2026-08-28 |
| Decisions landed | DEC-001 to DEC-033 (DEC-002/004/009 superseded; DEC-006 extended; DEC-016/018/019/027 refined 2026-08-28) |
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
| Elvis refinement batch (language storage, home-location mechanism, cohort, Explore gate, paid quota) | 2026-08-27 | Done, landed as DEC-029 to DEC-033 on 2026-08-28 |
| Moderation model + owner (launch blocker), now needs Korean-language coverage too | Before launch | Open |
| Payments/ticketing build scope decision (Korea non-Stripe path in play) | TBD | Open (own conversation) |
| Phase-1 build kickoff | After scope + moderation lock | Not started |

---

## Needs a decision

Open questions (not yet decisions), from the HOTSHEET and the 2026-08-28 merge:

- Whether the cohort hard filter reverts to a ranking signal once density allows (DEC-019 / DEC-020).
  Note: DEC-030 removed city from the cohort formula, so the per-city density call is now a single
  global call rather than a per-city PM decision; the softening trigger itself is still open.
- Two undesigned prerequisites for group-dynamics recommendations: a general user-blocking feature
  and an attendee-level feedback mechanism (DEC-023).
- Explore country-gate open UI details (DEC-032): the aggregate-teaser markers at country scale and
  world-zoom, whether Explore needs its own manual refresh distinct from the home feed's, and whether
  Explore's ranked list view gets the same out-of-country teaser treatment or excludes those results.
- Apply-to-join itself (phase-1.5 placement and design) is still unmerged; DEC-033's screening-question
  quota rides along with that feature's own eventual merger.
- Free Now open details (account-standing threshold, duration cap, archival, org rooms); live-stories
  vs the org media cap; whether the Event model supports a multi-day date range (DEC-025).
- Commercial-structure proposal channel and the PROJECT_STRATEGY.md rewrite (DEC-018).
- Age/location logic pending legal counsel (DEC-012, TASK-013), now including Korea's carrier-based
  PASS verification (DEC-026) and the redacted-ID fallback flow.
- How much legacy Wepop code is reused vs rebuilt (DEC-008).

ESCALATE (financials owner): freemium/commercial structure (DEC-018); the Moments-doc ~$100K budget
line, DLG Law counsel, and named contacts (conflict-review item 10); the ticketing/payments build and
the Korea non-Stripe payment path. The DEC-032 Explore country gate and DEC-033 apply-to-join quota
were reviewed and signed off by the financials owner on 2026-08-28.

---

## Risks (from HOTSHEET Risk Register Snapshot)

| # | Risk | Severity (Likelihood x Impact) | Owner | Status |
|---|------|-------------------------------|-------|--------|
| R1 | Cross-jurisdiction age verification is legally messy; locking the DEC-012 logic (superseded DEC-002) before counsel could ship a non-compliant flow | Medium x High | Aakash | ACTIVE (in-flight) |
| R2 | Solo-founder blind spot: Elvis designing alone, calls may go unchallenged | Medium x Medium | Aakash | ACTIVE |
| R3 | OTP/SMS deliverability blocked by geography without an in-region business (email magic-link now covers recovery per DEC-011) | Low x Medium | Aakash | ACTIVE |

Note: content moderation is tracked as a Blocking item on the HOTSHEET rather than a numbered risk;
promote to R4 via risk-register if a formal risk entry is wanted. Two design-level watch items surfaced
by the 2026-08-28 merge are not yet formal risks: a user who never grants GPS has no path to update a
stale home location (DEC-031, Elvis's explicit no-fallback call), and the Explore gate's
current-location integrity depends on GPS resisting mock-location spoofing (DEC-031/DEC-032).

---

## Open action items

| Item | Owner | Due / Since |
|------|-------|-------------|
| Stand up content moderation (owner, SLA, tooling), now including Korean-language coverage - launch blocker | Aakash | Since 2026-08-26 (TASK-034) |
| Confirm cohort softening transition with Elvis (density call now global per DEC-030) | Aakash | Since 2026-08-26 (TASK-035) |
| Resolve the Korea payments path (non-Stripe processors) | Aakash | Since 2026-08-26 (TASK-036) |
| Update the docs with the payments vision + requirements | Elvis | Ongoing, since 2026-08-24 (todos #12) |
| Review every phase-1 feature against the docs and finalize design screens | Elvis | Since 2026-08-26 (todos #14) |
| Pull the repo, set up Cowork, research Korean PASS authentication | Deepak | Since 2026-08-26 (todos #15) |
| Consult counsel on age/location logic | Aakash | Open (todos #4, TASK-013) |

> Full action-item list lives in `comms/todos.md`; full task tracking in `shared/TASK-BOARD.md`
> (now through TASK-038). This is the headline set.

---

## Merge queue

- Open conflicts: none. See `shared/MERGE-REVIEW.md`.
- Escalations pending (financials): freemium/commercial structure, the Moments-doc budget/legal items,
  and the ticketing/payments build (including the Korea non-Stripe path). The DEC-032 and DEC-033
  commercial items were signed off and landed on 2026-08-28.

---

_Refresh this file with the **update-tracker** skill after a merge run, a design intake, or when a
decision or risk changes._
