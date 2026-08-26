# Elvis workspace intake and decision inventory, 2026-08-26

> Prepared by Aakash (merger) as an intake of Elvis's workspace working files, which accumulated across
> three sessions (2026-08-19 through 2026-08-25) and had not yet been promoted to proposals or pulled
> into `shared/`. This is the said-vs-record analysis plus the full list of decisions to be proposed.
> Read-only on `shared/`. Nothing here is landed; the formatted proposals live in
> `workspaces/aakash/proposed-decisions.md` and `proposed-hotsheet.md`, pending the merge.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Why this exists

Elvis did the design work in his own workspace (correct) but, by his own session-log note, never
promoted any of it to `proposed-decisions.md`, so none of it reached `shared/`. That gap is three
sessions deep. This intake extracts the RESOLVED items into decision proposals, carries the OPEN
flags to the HOTSHEET and todos, and routes the governance gaps to Aakash. Elvis's open flags are NOT
converted into decisions.

## Source files reviewed

| File | Date | Substance |
|------|------|-----------|
| `conflict-review-2026-08-19.md` | 08-19..08-24 | 10 walkthrough-vs-draft conflicts resolved, plus items 11/12 |
| `freemium-model-2026-08-19.md` | 08-19..08-24 | Two-tier pricing, gating principle, analytics, media caps, cost model |
| `community-segmentation-2026-08-25.md` | 08-25 | Cohort model (city + life-stage, university override) |
| `recommendation-algorithm-2026-08-25.md` | 08-25 | Two-stage retrieval/ranking, ML-ready, explore split |
| `group-dynamics-2026-08-25.md` | 08-25 | Avoid signal, look-alike affinity, personality-mix |
| `recurring-events-2026-08-25.md` | 08-25 | Linked Event instances, calendar-style semantics |
| `event-series-2026-08-25.md` | 08-25 | Thematic master hub, co-hosts pulled forward |
| `feature-backlog-2026-08-25.md` | 08-25 | 12-item batch triaged and sized |
| `event-schedule / live-stories / free-now / icebreakers / tips-guides -2026-08-25.md` | 08-25 | 5 features fully scoped |

## Alignment against locked decisions (DEC-001 to DEC-009)

No accidental contradictions. Three locked decisions are DELIBERATELY superseded by newer resolutions,
and one is refined. These are intentional supersessions for Aakash to approve, not conflicts to route to
MERGE-REVIEW. Everything else is additive.

| Locked | Relationship | New entry |
|--------|-------------|-----------|
| DEC-002 (age gate, provisional) | Mechanism changed (no forced early GPS prompt; store-region cascade); country-tied principle kept; stays provisional pending TASK-013 | DEC-012 |
| DEC-004 (OTP required, optional password) | SUPERSEDED (provider-verified phone can satisfy verification; password deferred; email recovery) | DEC-011 |
| DEC-006 (anti-stalking visibility) | Extended, not superseded (gender aggregate-only; photos pre-join only to mutual follows) | DEC-017 |
| DEC-009 (phase-1 scope) | SUPERSEDED for chat/calendar only (DM+group chat into phase 1; calendar split); close-toggle and no-media-on-ideas carry forward | DEC-013 |
| DEC-003, DEC-005, DEC-007, DEC-008 | Reused/consistent, no change | n/a |

## Decision inventory (proposed DEC-010 to DEC-025)

Each maps to a formatted entry in `workspaces/aakash/proposed-decisions.md`. Source file cited per entry
there. Confidence is High unless noted.

1. DEC-010 Payments and monetization phasing (08-24 call). Architect gated in phase 1, enable phase 1.5.
2. DEC-011 Auth model. SUPERSEDES DEC-004. Social login + phone always required; provider-verified phone
   (Kakao/Korea only) can satisfy verification, else OTP; password deferred; email magic-link recovery;
   biometrics for re-login.
3. DEC-012 Age gate + country determination. SUPERSEDES DEC-002 (still provisional, TASK-013). Self-declared
   birthdate locked at signup; per-country config table; country via cascade (store region, then
   already-granted device location, then phone country code); no forced GPS prompt; no ID check phase 1.
4. DEC-013 Phase-1 chat and calendar scope. SUPERSEDES DEC-009 (chat/calendar only). DM + user-created
   group chats into phase 1 (text only). Calendar split: phase 1 read-only busy-time ingestion + manual
   per-event add-to-calendar; full in-app calendar to phase 1.5.
5. DEC-014 Post-event feedback (ratings and reviews). Three-step optional/skippable flow (rate event,
   rate people, add moments), check-in gated. Attendee thumbs are an internal-only signal. QR check-in
   becomes REQUIRED for phase 1. Moderation becomes a launch blocker.
6. DEC-015 Moments content and visibility. One post per user per event; react/comment/share on moments
   visible beyond owner; visibility inherits event with a per-moment private override; most-restrictive
   -wins principle; private accounts deferred; video in (720p H.264, 15s flat, 10 media items free).
7. DEC-016 Location at registration (resolves open question O1). City-level location required at
   onboarding (typed/selected, not GPS); device GPS optional and contextual with in-app nudges; kept
   distinct from the age-gate country signal.
8. DEC-017 Pre-join gender and photo visibility. EXTENDS DEC-006. Gender aggregate ratio only; photos not
   shown in the pre-join attendee list except between mutual (bidirectional) follows.
9. DEC-018 Freemium / commercial structure. GOVERNANCE FLAG (financials + no proposal channel for
   PROJECT_STRATEGY). Two tiers (individual $3.99/mo or $36/yr, HELD to post-phase-1; org $19.99/mo or
   $199/yr, proceeding); three-bucket gating principle; no paid ranking boost (locked); org analytics
   free/paid split; per-attendee media caps; 12-month retention; manual tail safety valve.
10. DEC-019 Community segmentation (cohorts). Cohort = (city, age/life-stage bucket); university override;
    hard retrieval filter at launch, softens to a ranking signal on manual per-city density review;
    computed per user independently (no inviter inheritance).
11. DEC-020 Recommendation algorithm architecture. Two-stage retrieval then ranking; rule-based weighted
    scoring at launch, ML-ready; home feed + Explore (map unranked/viewport-bounded, list ranked);
    new-host fairness boost; text keyword matching + evolving interest profiles; hidden internal keyword
    layer (admin-visible); day-one feedback logging; one global formula now, learned per-user weights later.
12. DEC-021 Recurring events (build phase 1.5). Separate linked Event instances + recurring_group_id;
    Google-Calendar-style this/following semantics; batch generation; join = snapshot not subscription;
    series pages fall out as an instance-embedded list; both individual and org hosts.
13. DEC-022 Event Series (build phase 1.5). Master hub page (not joinable); closer to Idea; self-curation
    only; co-hosts PULLED FORWARD to ship alongside (revises item 9); most-restrictive-wins for private
    events; multiple series per event; both host types.
14. DEC-023 Group dynamics as recommendation factors. Avoid signal (soft penalty, amplified by explicit
    block); look-alike host affinity (parked, needs scale); personality-mix compatibility (ranking signal
    only). Depends on an undesigned general blocking feature and attendee-level feedback (both flagged).
15. DEC-024 Undiscussed-surfaces phase triage (item 9). Phase 1: waitlist auto-promote + claim window,
    org ownership transfer, public org track-record module. Later: apply-to-join, Sunday Deck, annual
    Wrapped, P1.2 memories resurfacing. Co-hosts pulled forward (see DEC-022).
16. DEC-025 New-feature scoping batch. Event schedule (phase 1), live stories (phase 1, safety-flagged),
    Free Now (phase 1, highest safety), icebreakers (phase 1 host-question game; rest later),
    tips/guides (phase 1 mechanism, copy later). Seven items grouped to dedicated future threads
    (ticketing/payments, gamification/economy, ads/promotion, supporters marketplace, event music,
    web version).

## Open flags routed to HOTSHEET / todos (NOT decisions)

- Moderation staffing and SLA (OQ-9) is now a launch blocker: three text surfaces (host-rating comments,
  moment comments, DM/group chat) plus Free Now rooms. Needs a named owner before launch.
- Low QR check-in rate is a product risk (no scans means no ratings and no recommendation signal).
- Whether the cohort hard filter reverts to a ranking signal once a city softens (assumed, unconfirmed).
- Who owns the manual per-city density review (presumed PM/Aakash, unconfirmed).
- Free Now: exact account-standing threshold, duration cap, room auto-archival, org-created rooms.
- Live stories vs the org 50-item media cap (likely separate allowance, unconfirmed).
- General user-blocking feature and attendee-level feedback mechanism: real prerequisites, undesigned.
- Event model multi-day date-range support (event schedule depends on it), Deepak to confirm.
- Ratings "0 star = unrated vs a real value" small open item.

## Governance items routed to Aakash

- ESCALATION (conflict-review item 10): Moments doc names (Ratnadeep Deshmane, confirm vs Deepak; Joy
  Jeong ops/legal), a ~$100K budget line, DLG Law as counsel, KPI targets. Commercial/legal, financials
  owner. Not a DEC.
- Freemium (DEC-018) sits in commercial-structure territory. `PROJECT_STRATEGY.md` is merger-owned but
  `CLAUDE.md` section 6 defines no `proposed-project-strategy.md` channel. Decide the channel (or accept
  pricing via the decision log as financials owner) before this content flows to `shared/`.
- Ticketing/payments is flagged by Elvis as likely the single largest piece of technical scope in the
  project. DEC-010 sets the phasing; the detailed build decision (and whether it is phase 1 at all)
  needs its own dedicated conversation.
- Phase 1.5 is currently an informal label, not a `CONVENTIONS.md` integer phase. If it becomes a real
  contract phase with its own SOW and folder, that is Aakash's phase-plan/financials call.

## After the merge (derived-doc refresh, not yet done)

Once these proposals land in `shared/`, run in order: `scope-tracker` (populate the phase/feature matrix
with all new features and phase placements), `spec-sync` (regenerate the product overview), `task-board`
(add build tasks for Deepak and design follow-ups), `update-tracker` (roll-up), and reflect the
moderation launch blocker on the HOTSHEET. `compliance-watch` should also pick up the age/country
cascade, behavioral-inference disclosure, and Free Now location handling.
