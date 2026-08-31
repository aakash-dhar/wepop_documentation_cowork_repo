# PROJECT_INDEX.md - Wepop grounding document

> Merger-only file. Read this first every session. Everyone else proposes via
> `workspaces/[you]/proposed-project-index.md`. Do not hallucinate capabilities not documented
> here. Where a section is older than the latest snapshot, `shared/DECISIONS.md` controls.

## State snapshot (2026-08-31)

- **Project:** WEP001 - Wepop
- **What it is:** An invite-first, location-based events and meetup app (a meetup app, not a dating
  app) for getting people together in the real world around shared activities. Being rebuilt on top
  of an existing Wepop codebase, salvaged and extended with AI. Focus markets Korea and the US.
- **Phase:** Phase 1 design deepening. First walkthrough 2026-08-17; a large Elvis design batch landed
  2026-08-26 (DEC-010 to DEC-025); a Korea/localization sync landed 2026-08-28 (DEC-026 to DEC-033); the
  handoff-spec-v0.9 intake and the phase-1/1.5 review batch landed 2026-08-31 (DEC-034 to DEC-044); the ratings/check-in
  correction batch landed 2026-08-31 second merge (DEC-045 to DEC-047).
- **RAG:** Green with a watch - design substantially deeper, no hard build blocker, but three launch
  blockers are open on the HOTSHEET: moderation capability (reframed 2026-08-31 as speed-vs-capability),
  위치정보법 KCC registration for the check-in geofence (likely de-blocked by
  DEC-046's self-scan deferral, kept Blocking pending DLG confirmation), and the CSAM preserve-and-report
  runbook.
- **Last decision:** DEC-047 (feedback uniformly anonymous, 7-day edit/withdraw window, "My feedback"
  profile entry), 2026-08-31. The second 2026-08-31 batch (DEC-045 to DEC-047) corrected DEC-034 (badge
  and scoring weight withdrawn; stars 1 to 5; public average gates at 3 ratings), reversed check-in to
  host-scans-attendee as an operations tool with self-service deferred (DEC-046, likely de-blocking L-3
  pending DLG), and settled feedback anonymity (DEC-047). The first batch (DEC-034 to DEC-044) amended DEC-014 (feedback and
  check-in), DEC-017 (gender pre-join), DEC-023 (avoid signal), DEC-015/018 (media caps and retention),
  DEC-025 (event schedule and notifications), and DEC-009 (idea lifecycle), and added host-accountability
  and completed-event-deletion rules.
- **Team:** Aakash (PM/merger/financials), Elvis (client and designer), Deepak (tech lead and developer)

## What is being built

- Core objects: Events (standalone, recurring, or in a Series), Ideas, Event Series (a thematic hub,
  phase 1.5), and Business / Organization profiles (university clubs first, promotional later).
- Phase 1: invite-first onboarding and waitlist (auto-promote), social-login-plus-phone auth (PASS in
  Korea), self-declared age with a country cascade, required neighborhood-level home location via the
  map picker (DEC-031), bilingual i18n (DEC-027/029), events and ideas, event schedule, anonymous
  1-to-5 ratings with a 7-day edit window, check-in as a host-side operations tool on ticketed and
  host-opted capacity events only (DEC-045/046/047), moments with video, event cover media, live
  stories, DMs and group chat (text only), lightweight calendar pieces, community cohorts
  (student-vs-not, DEC-030) and the recommendation algorithm, general user blocking, host
  accountability, tiered media retention, Free Now, icebreakers, tips/guides, A/B experimentation,
  and gated (not live) payment provisions.
- Phase 1.5: payments go-live and the individual premium tier, the full in-app calendar, recurring
  events, Event Series, and co-hosts. Later: self-service check-in mode, Sunday Deck, apply-to-join,
  annual Wrapped, private accounts, and the dedicated payments/gamification/ads/marketplace threads.
- Full feature map: `architecture/phase-plan/wepop-product-overview.md`; per-feature phase and status:
  `architecture/phase-plan/wepop-scope-matrix.md`.

## What has been decided

Source of truth is `shared/DECISIONS.md` (currently DEC-001 to DEC-047). DEC-001 to DEC-009 landed
2026-08-17; DEC-010 to DEC-025 landed 2026-08-26 from the Elvis workspace intake; DEC-026 to DEC-033
landed 2026-08-28 (Korea PASS, localization, A/B testing, cohort simplification, home-location mechanism,
Explore country gate, apply-to-join quota); DEC-034 to DEC-044 landed 2026-08-31; DEC-045 to DEC-047 landed 2026-08-31 (second merge).

Foundational (2026-08-17): DEC-001 central repo + harness; DEC-003 Google-style map picker; DEC-005
extensible tag list; DEC-006 anti-stalking visibility; DEC-007 no in-app AI image/video; DEC-008
salvage the existing code.

Superseded or extended 2026-08-26: DEC-002 age gate (SUPERSEDED by DEC-012, still provisional);
DEC-004 auth (SUPERSEDED by DEC-011); DEC-009 phase-1 scope (SUPERSEDED by DEC-013 for chat/calendar);
DEC-006 (EXTENDED by DEC-017).

Landed 2026-08-26: DEC-010 payments phasing; DEC-011 auth (social login + phone, password deferred);
DEC-012 age/country cascade; DEC-013 chat + calendar into phase 1; DEC-014 ratings + required QR
check-in; DEC-015 moments content/visibility + video; DEC-016 location at registration; DEC-017 gender
aggregate / photos to mutuals; DEC-018 freemium/commercial structure (financials, governance flag);
DEC-019 community cohorts; DEC-020 recommendation algorithm; DEC-021 recurring events; DEC-022 Event
Series + co-hosts; DEC-023 group-dynamics signals; DEC-024 undiscussed-surface triage; DEC-025
new-feature scoping batch.

Landed 2026-08-28: DEC-026 Korea PASS auth; DEC-027 localization/Korean; DEC-028 A/B testing; DEC-029
language-preference storage and i18n scope (refines DEC-027); DEC-030 cohort simplified to student-vs-not,
location removed (revises DEC-019); DEC-031 home-location input mechanism, neighborhood granularity,
mutability (refines DEC-016); DEC-032 Explore gated by country, individual-premium lift (extends DEC-018);
DEC-033 apply-to-join screening-question quota (extends DEC-018).

Landed 2026-08-31: DEC-034 peer feedback positive-only, check-in decoupled (badge plus weight since
withdrawn by DEC-045; amends DEC-014); DEC-035 gender out of attendee pre-join, invariant I-13 (partially supersedes DEC-017); DEC-036
avoid signal block-only plus positive affinity (amends DEC-023); DEC-037 general user blocking as phase-1
baseline; DEC-038 event cover media caps (extends DEC-015/018); DEC-039 tiered 6-month media retention,
active at launch (revises DEC-018); DEC-040 Ideas lifecycle (supersedes DEC-009's idea provision); DEC-041
event schedule multi-day plus propagation (refines DEC-025); DEC-042 change notifications (extends DEC-025);
DEC-043 completed events cannot be deleted or left by host, ratings persist (amends handoff spec §3.2);
DEC-044 host accountability, reputation/enforcement split (extends DEC-024/026).

Landed 2026-08-31 (second merge): DEC-045 badge and scoring weight withdrawn, stars 1 to 5, public average
gates at 3 ratings with unweighted smoothing (supersedes DEC-034 in part, amends DEC-014); DEC-046 check-in
reversed to host-scans-attendee, operations tool only, non-universal, self-service mode deferred, I-12
reverted to visibility-scoped (reverses handoff spec §4.2); DEC-047 feedback uniformly anonymous, 7-day
edit/withdraw window, author link surfaces only in "My feedback" (extends DEC-014/034).

Still open (not decisions): Free Now open details, DEC-038's total-video-duration cap and org-paid video
length, DEC-039's three retention refinements pending Elvis, the DEC-044 open list (re-registration
cooldown, ban-list retention, org-creation account age), age/location pending counsel (TASK-013), the
legal register L-1 to L-12 consult (TASK-040), and the commercial-structure proposal channel (TASK-037).
Resolved since the last snapshot: the group-dynamics prerequisites (DEC-036/037), the cohort softening
mechanism (DEC-030 removed location from the formula), and the Event multi-day date range (DEC-041). See
`shared/HOTSHEET.md`.

## Where everything lives

| Area | Path | Notes |
|------|------|-------|
| Decisions | `shared/DECISIONS.md` | Source of truth |
| Running summary and risks | `shared/HOTSHEET.md` | |
| Single-snapshot status | `shared/PROJECT_TRACKER.md` | One-screen roll-up, regenerated by update-tracker |
| Task board (data) | `shared/TASK-BOARD.md` | Per-task lifecycle: owner, status, started, ended, pushed |
| Task board (internal view) | `team/board.html` | Full five-view board, shown inline; not published |
| Task detail | `team/tasks/TASK-NNN.md` | Per-task overview, linked sources, activity, definition of done (the side panel) |
| Delivery board (alt link) | `docs/board-public.html` | Copy of the full board, kept so older links still resolve |
| Strategy | `shared/PROJECT_STRATEGY.md` | Commercial narrative |
| Merge queue | `shared/MERGE-REVIEW.md` | |
| Product overview | `architecture/phase-plan/wepop-product-overview.md` | App feature map and phase-1 scope |
| Full project reference | `architecture/phase-plan/wepop-project-reference.md` | Complete module-by-module walkthrough, flows, data-model notes, decisions, risks (2026-08-31) |
| Project reference (client page) | `docs/project-reference.html` | BetaCraft-styled module reference with detail drawers and sourced Elvis detail; behind the dashboard login gate; linked from the dashboard header |
| Project reference (pipeline) | `team/project-reference/` | template.html + data.js + build.py; maintained by the project-reference skill; never hand-edit the built HTML |
| Scope matrix | `architecture/phase-plan/wepop-scope-matrix.md` | Per-feature phase, status, owner, linked DEC |
| Emails | `comms/emails/` | `NN_YYYY-MM-DD_kebab-subject.md` |
| Meeting notes | `comms/meeting-notes/` | summary + `_TRANSCRIPT.md` |
| Elvis draft docs (received) | `comms/attachments/2026-08-18_elvis-draft-docs/` | Brief v2 + Moments v0.9, provisional; reviewed version pending; see `_NOTES.md` |
| Walkthrough vs drafts review aid | `comms/attachments/2026-08-18_elvis-draft-docs/` | PM cross-check (md + pdf) |
| Design docs | `architecture/elvis/`, `architecture/technical/` | No code |
| Contracts | `contracts/phase-N/` | Financials owner |
| Delivery board (Pages root) | `docs/index.html` | The full five-view BetaCraft board; served at the GitHub Pages root URL |
| Skills | `skills/` | PM toolkit |
