# HOTSHEET.md - Wepop running summary

> Merger-only file. Everyone else proposes via `workspaces/[you]/proposed-hotsheet.md`.
> Newest at top. Priority order: Blocking, Needs Attention, Watching, Resolved. Resolved items
> move to Resolved, they are never deleted. No em-dashes. Use a lowercase x for Likelihood x Impact.

---

## Current state (as of 2026-08-26)

Project WEP001 - Wepop. First full design walkthrough 2026-08-17 (DEC-001 to DEC-009). On 2026-08-26 a
three-session batch of Elvis design work landed as DEC-010 to DEC-025 (16 decisions), superseding DEC-002
(age mechanism), DEC-004 (auth), and DEC-009 (chat/calendar scope), and extending DEC-006. Phase 1 scope
grew materially (DM and group chat, video moments, ratings with required QR check-in, city-level location,
community cohorts, the recommendation algorithm). The main new risk is moderation load. No hard build
blockers, but moderation staffing must be resolved before launch.

### Blocking

- **Content moderation staffing and SLA (launch blocker).** Four surfaces need day-one moderation:
  anonymous public-by-default host-rating comments (DEC-014), public moment comments (DEC-015), DM and
  user-created group chat (DEC-013), and Free Now location-tied rooms (DEC-025). Answers the long-open
  Moments spec OQ-9. Needs a named owner before launch. Since 2026-08-26. Source: Elvis workspace intake.

### Needs Attention

- **Korea payments need a non-Stripe path (org tier is live now, so not distant).** Stripe's actual support for Korea-based merchant payouts, KRW, and Korean local methods (KakaoPay, Naver Pay, bank transfer/virtual account) is unconfirmed, and Korean consumers strongly prefer local methods over cards. DEC-010 assumed Programination's Stripe account and DEC-018's org tier is proceeding now. Evaluate Korea-specific processors (Toss Payments, NHN KCP, PortOne/Iamport). App-store IAP also in play (15 to 30 percent; virtual-goods vs physical-experience distinction; web-payment workaround). Financials owner (Aakash); raises the urgency of the DEC-010 payments conversation (TASK-036). Since 2026-08-26. Source: 2026-08-26 team sync; elvis proposal (`internationalization-korea-2026-08-26.md`).

- **Cohort/algorithm mechanism transitions unconfirmed.** Whether the cohort hard retrieval filter
  reverts to a weighted ranking signal once a city is manually confirmed dense enough (DEC-019/DEC-020),
  who owns the manual per-city density call (presumed Aakash), and whether the Explore map view's cohort
  restriction also loosens. Confirm with Elvis. Since 2026-08-26. Source: Elvis workspace intake.
- **Two undesigned prerequisites for group-dynamics recommendations (DEC-023).** A general user-blocking
  capability (assumed to exist, never designed) and an attendee-level thumbs up/down post-event feedback
  mechanism (the avoid-signal data source, does not exist yet). Each needs its own scoping pass. Since
  2026-08-26. Source: Elvis workspace intake.
- **Commercial/legal items to the financials owner (Aakash).** Freemium/commercial structure (DEC-018)
  needs a proposal-channel decision (no proposed-project-strategy channel exists) before the
  PROJECT_STRATEGY.md rewrite. Moments-doc escalation (conflict-review item 10): named contacts (confirm
  "Ratnadeep Deshmane" vs Deepak; Joy Jeong ops/legal), a ~$100K budget line, DLG Law as counsel, KPI
  targets. Ticketing/payments (flagged largest technical scope) needs its own conversation, including
  whether it is phase 1. Since 2026-08-26. Source: Elvis workspace intake.
- **Repo and Cowork harness setup.** Elvis's GitHub ID (`programinator-elvis`) received 2026-08-18.
  Elvis's project documentation now processed into the record via the 2026-08-26 intake (DEC-010 to
  DEC-025). A reviewed/consolidated design doc from Elvis is still expected. Since 2026-08-17. Source:
  2026-08-17 walkthrough. Action items tracked in `comms/todos.md`.

### Watching

- **Korean map coverage is a known future concern; Google Maps acceptable for now.** South Korea restricts map-data export, so local providers have richer data and Google has historically been thinner in Korea; Google is reportedly expanding Korean coverage. Use Google (DEC-003) for now; revisit only if it becomes a real issue. Since 2026-08-26. Source: 2026-08-26 team sync.

- **QR check-in is now load-bearing; a low check-in rate is a product risk, not only ops.** Check-in gates
  ratings, host reputation, and the recommendation signal (DEC-014). No scans means no ratings and no
  recommendation signal. No fallback path is being built now. Watch after the first events. Since
  2026-08-26. Source: Elvis workspace intake.
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
