# HOTSHEET.md - Wepop running summary

> Merger-only file. Everyone else proposes via `workspaces/[you]/proposed-hotsheet.md`.
> Newest at top. Priority order: Blocking, Needs Attention, Watching, Resolved. Resolved items
> move to Resolved, they are never deleted. No em-dashes. Use a lowercase x for Likelihood x Impact.

---

## Current state (as of 2026-08-31)

Project WEP001 - Wepop. First full design walkthrough 2026-08-17 (DEC-001 to DEC-009). On 2026-08-26 a
three-session batch of Elvis design work landed as DEC-010 to DEC-025 (16 decisions), superseding DEC-002
(age mechanism), DEC-004 (auth), and DEC-009 (chat/calendar scope), and extending DEC-006. Phase 1 scope
grew materially (DM and group chat, video moments, ratings with required QR check-in, city-level location,
community cohorts, the recommendation algorithm). The main new risk is moderation load. No hard build
blockers, but moderation staffing must be resolved before launch. On 2026-08-31 (second merge) DEC-045
to DEC-047 landed: DEC-034's badge and scoring weight withdrawn, check-in reversed to host-scans-attendee
as an operations tool with self-service deferred, and feedback confirmed uniformly anonymous with a 7-day
edit window. The reversal likely de-blocks the 위치정보법 entry, pending DLG confirmation.

### Blocking

- **Content moderation capability (launch blocker), reframed 2026-08-31.** The blocker splits into two
  halves. Response-time SLAs (handoff spec §12.5: urgent under 4h waking hours, standard 24h weekday /
  48h weekend, appeals 72h) are DEFERRED by Elvis until employees are hired, and the numbers are recorded
  for reuse, not committed; independent appeal review is structurally impossible with one reviewer, and
  "waking hours" is undefined for a Korea-first launch. Moderation CAPABILITY cannot be deferred: at launch
  the app ships anonymous host-rating comments (DEC-014), public Moment comments (DEC-015), DM and
  user-created group chat (DEC-013), Free Now rooms (DEC-025), and Discussion on every event and idea (five
  live UGC surfaces, eleven reportable target types). Without a place for reports to land and someone able
  to act, there is no removal path at all. Three pre-launch artifacts, none of which exist yet and none of
  which are SLA commitments: a basic internal admin queue, urgent-report push alerts to whoever is on call,
  and a one-page written moderation guideline. Statutory duties do not wait for hiring: 정보통신망법 takedown
  and 임시조치 (legal register L-5, L-11) and 불법촬영물 under 전기통신사업법 (L-12) attach from the day the
  service has users. Rota is one reviewer (Elvis) plus "Reviewer B (to be hired)". Load reducers already
  designed in: one generic report model feeding a single queue, idempotent repeat reports, auto-hide on a
  double condition (5+ distinct reporters AND 10 percent of distinct viewers), and a brigade_suspected
  flag. Day-one metrics (reports per 1,000 Moments, median time-to-decision, backlog depth, appeal overturn
  rate) become the hiring trigger. Tracked as TASK-034; companion risk R4. Does not clear until the three
  artifacts exist. Since 2026-08-26, reframed 2026-08-31. Source: handoff spec v0.9 §12; Elvis intake.
- **위치정보법 registration for check-in (updated 2026-08-31 on DEC-046: likely no longer gates P0; kept
  Blocking until DLG confirms).** The exposure attaches to the printed-poster check-in mode, whose static
  token needs a location radius to resist forgery, and printed posters exist to support attendee self-scan.
  DEC-046 reverses phase-1 check-in to host-scans-attendee and defers attendee self-scan to a later
  self-service mode, so the poster and its geofence defer with it; if that holds, L-3 stops being a gate
  before P0 and becomes a later-phase legal question. Not closed and not dropped from the DLG consult
  (TASK-040): confirm with DLG that deferring self-scan removes the 위치정보법 trigger from phase 1 rather
  than assuming it, then re-scope this entry to a question and re-rate R5 on the same basis (same exposure,
  materially lower near-term likelihood, since nothing in phase 1 then collects the triggering location
  data). The exposure returns intact the day self-service mode is built, and the answer is cheaper in hand
  before that work starts. Anti-forgery also simplifies under the reversal: once a host scans a person
  standing in front of them, a static per-attendee credential suffices and the 60-second rotating QR is no
  longer needed. Stakes remain lowered by check-in gating nothing (DEC-045/046). Distinct from TASK-013
  (age/location logic). Companion risk R5. Since 2026-08-31, updated 2026-08-31. Source: handoff spec v0.9
  §4.2, §16 L-3; `workspaces/elvis/ratings-checkin-2026-08-31.md`.
- **CSAM preserve-and-report runbook required before launch.** If child sexual abuse material appears it
  must not be deleted (deleting destroys evidence); the required handling is preserve, restrict access, and
  report to the authorities. A written one-page procedure any reviewer can follow unaided is a pre-launch
  requirement, not a post-launch improvement, and with the rota at one person plus a to-be-hired second
  reviewer it is what makes the procedure transferable. Ties to 불법촬영물 under 전기통신사업법 (L-12), whose
  thresholds are a growth trigger while the runbook is needed at launch regardless. Interacts with the
  moderation entry: the urgent lane auto-hides this class on report, so the runbook governs what happens
  after auto-hide. Never previously reached the HOTSHEET despite being a hard pre-launch legal gate. Since
  2026-08-31. Source: handoff spec v0.9 §12.5, §16 L-12.

### Needs Attention

- **Korea map provider (Google vs Naver/Kakao) is now a decision, not a distant concern.** The zoom-determines-precision picker (DEC-054) depends on the provider's POI and reverse-geocode quality at each zoom tier, so the provider choice now affects a phase-1 feature. Open question whether a non-Korean business can even open a Naver or Kakao developer account, which constrains the choice; Elvis researched a dual Google/Naver design (per-session provider lock, reusing the current-location signal), but the decision is unmade. Elevated from the Watching "Korean map coverage" item below. Owner Aakash with Deepak on feasibility. Since 2026-09-02. Source: `workspaces/elvis/event-location-map-picker-2026-08-27.md`; 2026-09-02 call.

- **Korea payments need a non-Stripe path (org tier is live now, so not distant).** Stripe's actual support for Korea-based merchant payouts, KRW, and Korean local methods (KakaoPay, Naver Pay, bank transfer/virtual account) is unconfirmed, and Korean consumers strongly prefer local methods over cards. DEC-010 assumed Programination's Stripe account and DEC-018's org tier is proceeding now. Evaluate Korea-specific processors (Toss Payments, NHN KCP, PortOne/Iamport). App-store IAP also in play (15 to 30 percent; virtual-goods vs physical-experience distinction; web-payment workaround). Financials owner (Aakash); raises the urgency of the DEC-010 payments conversation (TASK-036). Since 2026-08-26. Source: 2026-08-26 team sync; elvis proposal (`internationalization-korea-2026-08-26.md`).

- **Cohort/algorithm mechanism transitions unconfirmed.** Whether the cohort hard retrieval filter
  reverts to a weighted ranking signal once a city is manually confirmed dense enough (DEC-019/DEC-020),
  who owns the manual per-city density call (presumed Aakash), and whether the Explore map view's cohort
  restriction also loosens. Confirm with Elvis. Since 2026-08-26. Source: Elvis workspace intake.
- **Commercial/legal items to the financials owner (Aakash).** Freemium/commercial structure (DEC-018)
  needs a proposal-channel decision (no proposed-project-strategy channel exists) before the
  PROJECT_STRATEGY.md rewrite. Moments-doc escalation (conflict-review item 10): named contacts (confirm
  "Ratnadeep Deshmane" vs Deepak; the ops/legal contact is being refilled, previously-named person removed
  2026-08-31), a ~$100K budget line, DLG Law as counsel, KPI
  targets. Ticketing/payments (flagged largest technical scope) needs its own conversation, including
  whether it is phase 1. Since 2026-08-26. Source: Elvis workspace intake.
- **Repo and Cowork harness setup.** Elvis's GitHub ID (`programinator-elvis`) received 2026-08-18.
  Elvis's project documentation now processed into the record via the 2026-08-26 intake (DEC-010 to
  DEC-025). A reviewed/consolidated design doc from Elvis is still expected. Since 2026-08-17. Source:
  2026-08-17 walkthrough. Action items tracked in `comms/todos.md`.

### Watching

- **Korean map coverage is a known future concern; Google Maps acceptable for now.** South Korea restricts map-data export, so local providers have richer data and Google has historically been thinner in Korea; Google is reportedly expanding Korean coverage. Use Google (DEC-003) for now. Elevated to Needs Attention 2026-09-02 because the zoom-precision picker (DEC-054) now depends on provider POI quality. Since 2026-08-26. Source: 2026-08-26 team sync.

- **No-show rating abuse, now unmitigated by weighting (rewritten again 2026-08-31 on DEC-045).** DEC-045
  withdraws DEC-034's badge and 1.0/0.4 scoring weight, so eligibility is simply joined plus event
  completed: a user who RSVP'd and never attended can rate an event and its host and is indistinguishable
  from a real attendee. This is an accepted cost under DEC-045, not an oversight. The protections are now
  the 3-rating public display gate (one person cannot establish a public number alone), Bayesian smoothing
  toward the global mean with C = 5 (absorbs a single outlier), and host reporting of a rating from someone
  who was not there, which makes abuse a moderation rather than a scoring problem. The motive is judged
  thin at a free casual meetup. The `attendance` table stays first-class and transactional, so reinstating
  weighting later is a config change plus a runnable backfill; that is the lever if abuse appears. Watch
  after the first events. Since 2026-08-26, rewritten 2026-08-31 twice (was: QR check-in load-bearing;
  then: 0.4 weight as the designed mitigation). Source: DEC-045.
- **New real-time features carry open safety/scope details before build (DEC-025).** Free Now: exact
  account-standing threshold for room creation, duration cap, room auto-archival, org-created rooms;
  location rounding needs a concrete method; reciprocal-join enforced server-side. Live stories: whether
  they count against the org 50-item media cap (likely a separate allowance). Event schedule depends on a
  multi-day Event date range; Deepak to confirm. Since 2026-08-26. Source: Elvis workspace intake.
- Age verification across jurisdictions is legally messy; the DEC-012 logic (which superseded DEC-002's
  mechanism) is provisional and should not be finalized before legal counsel. Since 2026-08-17. Source:
  2026-08-17 walkthrough. (Risk R1.)
- Solo-founder blind spot: Elvis is designing Wepop alone and asked for structured pushback. Since
  2026-08-17. Source: 2026-08-17 walkthrough. (Risk R2.)
- OTP/SMS deliverability can be blocked by geography without an in-region registered business;
  relevant on expansion beyond US/Korea. Since 2026-08-17. Source: 2026-08-17 walkthrough. (Risk R3.)

### Resolved

- **Two undesigned prerequisites for group-dynamics recommendations (DEC-023).** Resolved 2026-08-31 by
  DEC-036 and DEC-037. General user blocking is now fully designed as a phase-1 safety baseline
  (bidirectional, total across every surface, scope stated at block time; DEC-037). The attendee-feedback
  prerequisite is resolved by removing the need for it: thumbs-down is dropped, the avoid signal becomes
  block-only, and the positive tap is redirected into a positive affinity ranking signal alongside
  DEC-020's social-proximity weight (DEC-036). Also clears the scope-matrix "Unbacked / needs a decision"
  entry for general blocking. Was Needs Attention since 2026-08-26.
- **Location at registration (open question O1).** Resolved by DEC-016 (2026-08-24): city-level location
  required at onboarding (typed/selected, not GPS), device GPS optional and contextual. Was Needs
  Attention since 2026-08-17.

---

## Risk Register Snapshot

| # | Risk | Severity (Likelihood x Impact) | Owner | Mitigation | Status |
|---|------|-------------------------------|-------|------------|--------|
| R1 | Cross-jurisdiction age verification is legally messy (US 18, Korea 19, Germany 16; passive vs active location, travel jurisdiction); locking the age/location logic before counsel could ship a non-compliant flow. | Medium x High | Aakash | Consult a lawyer before locking the DEC-012 logic (superseded DEC-002 mechanism); keep the country-tied approach provisional until then. | ACTIVE (in-flight) |
| R2 | Solo-founder blind spot: Elvis designing alone, product/design calls may go unchallenged. | Medium x Medium | Aakash | Aakash and Deepak give structured critique on design and docs once shared; capture as proposals/suggestions. | ACTIVE |
| R3 | OTP/SMS (Twilio/WhatsApp) deliverability blocked by geography without an in-region registered business; breaks phone verification on expansion beyond US/Korea. | Low x Medium | Aakash | Email magic-link recovery now covers reset (DEC-011, which superseded the DEC-004 password fallback); check regional messaging-provider requirements before a new market. | ACTIVE |
| R4 | Single-reviewer moderation. Rota is one person (Elvis) until employees are hired, covering eleven reportable target types across five live UGC surfaces. Three failure modes: no coverage for sleep/travel/illness so an urgent report sits until one person wakes; appeals cannot be independent with one reviewer; and growth outpacing hiring rather than launch day itself. | Medium x High | Elvis | Ship the designed load reducers (one generic report model and single queue, idempotent repeat reports, auto-hide on 5+ distinct reporters AND 10 percent of distinct viewers, brigade_suspected flag); track the four day-one metrics as the hiring trigger. Auto-hide is doing heavy lifting under a single reviewer, so its thresholds must not be loosened without revisiting this risk. Companion to the moderation Blocking entry. | ACTIVE |
| R5 | 위치정보법 registration exposure. The printed-poster check-in geofence constrains scans to a location radius, which is location-data collection and may require 위치기반서비스사업 신고 to the KCC before it can ship in Korea. Shipping without an answer risks operating an unregistered location-based service; waiting with no fallback risks blocking P0. | Medium x High | Aakash | Route to DLG Law before the geofence ships (companion Blocking entry, before P0). Default to the fallback if registration proves burdensome: drop the radius and rely on the time window plus live-display mode. Near-term likelihood expected to drop on DEC-046 (phase 1 no longer collects the triggering location data; the poster geofence defers with self-service mode); re-rate once DLG confirms. | ACTIVE |
