# Wepop scope matrix - phase and feature tracker

> Owner: Aakash (phase-plan). Others suggest via `suggestions/`. Derived, grounded only in a landed
> decision or a design intake; never invented scope. When this disagrees with `shared/DECISIONS.md`,
> DECISIONS wins. Generated 2026-08-26 after DEC-010 to DEC-025 landed.
> Phase: `1` or `later` (phase 1.5 noted where a decision uses that informal label). Status:
> proposed / decided / designed / in-build / done / deferred. No em-dashes.

## Phase 1

| Feature | Area | Phase | Status | Owner | Linked DEC | Notes |
|---------|------|-------|--------|-------|-----------|-------|
| Invite-first onboarding + waitlist | Onboarding | 1 | designed | Elvis | walkthrough | Non-invited users join a waitlist (email, phone, location, university). |
| Auth: social login + phone always required | Auth | 1 | designed | Elvis/Deepak | DEC-011 | Kakao/Apple/Google; provider-verified phone (Kakao/Korea) may satisfy, else OTP. Password deferred; email magic-link recovery; biometrics for re-login. |
| Age gate + country cascade | Auth | 1 | decided (provisional) | Aakash/Deepak | DEC-012 | Self-declared birthdate locked at signup; store-region cascade; per-country config table. Provisional pending counsel (TASK-013). |
| City-level location at registration | Onboarding | 1 | designed | Elvis | DEC-016 | Required, typed/selected. Device GPS optional/contextual. Distinct from the age-gate country signal. |
| Personality/interest tags (extensible) | Onboarding | 1 | designed | Elvis | DEC-005 | Searchable, user-extendable; feeds matching. |
| Event location map picker | Events | 1 | designed | Elvis/Deepak | DEC-003 | Google-Maps-style search + tap; one interaction detail still open. |
| Events + Ideas core objects | Events/Ideas | 1 | designed | Elvis | walkthrough, DEC-009 | Idea "close to new joiners" toggle built but not exposed; no media upload on ideas. |
| Event schedule / itinerary | Events | 1 | designed | Elvis | DEC-025 | Ordered stops reuse the DEC-003 picker; visibility inherits the event; multi-day depends on Event date-range (Deepak to confirm). |
| Ratings + post-event feedback (3-step) | Social | 1 | designed | Elvis | DEC-014 | Optional/skippable, check-in gated; attendee thumbs internal-only. |
| QR check-in (required) | Events | 1 | decided | Deepak | DEC-014 | Load-bearing for ratings, reputation, recommendations, moments. |
| Moments (content + visibility + video) | Moments | 1 | designed | Elvis | DEC-015 | One per user per event; react/comment/share; most-restrictive-wins; video 720p/H.264/15s/10 items. |
| Live stories (ephemeral) | Moments | 1 | designed | Elvis | DEC-025 | Separate 24h content type; RSVP to post; poster-chosen audience (4 tiers). Media-cap interaction open. |
| Anti-stalking pre-join visibility | Safety | 1 | designed | Elvis/Deepak | DEC-006, DEC-017 | Mutuals + aggregates pre-join; gender aggregate-only; photos only to mutual (bidirectional) follows. |
| DM + user-created group chats | Chat | 1 | decided | Deepak | DEC-013 | Text only, no audio/video. Pulled into phase 1 (superseded DEC-009). Moderation surface. |
| Event/group chat | Chat | 1 | designed | Elvis/Deepak | DEC-009, DEC-013 | Text, photos, replies, reactions. |
| Calendar: busy-time ingestion + add-to-calendar | Calendar | 1 | decided | Deepak | DEC-013 | Read-only free/busy (times only, discard rest); manual per-event write. Full in-app calendar to phase 1.5. |
| Community cohorts (segmentation) | Discovery | 1 | designed | Elvis/Deepak | DEC-019 | (city, life-stage) + university override; hard retrieval filter at launch, manual per-city softening. |
| Recommendation algorithm | Discovery | 1 | designed | Elvis/Deepak | DEC-020 | Two-stage retrieval/ranking; rule-based, ML-ready; Explore map (unranked) vs list (ranked); new-host boost; day-one logging. |
| Group-dynamics signals | Discovery | 1 | designed | Elvis/Deepak | DEC-023 | Avoid signal (needs blocking + attendee feedback, both undesigned); personality-mix ranking signal. |
| Event icebreakers (host question game) | Events | 1 | designed | Elvis | DEC-025 | Up to 3 read-only questions, check-in gated, opt-in. Tag-matching + scavenger later. |
| Tips/guides | Content | 1 | designed | Elvis | DEC-025 | Contextual info icon + static guide; situation/status targeted; copy written later (ux-copy). |
| Waitlist auto-promote + claim window | Events | 1 | designed | Elvis | DEC-024 | Completes existing waitlist mechanic. |
| Org profiles + ownership transfer | Org | 1 | designed | Elvis | walkthrough, DEC-024 | University clubs first; ownership transfer structural for officer turnover. |
| Public org track-record module | Org | 1 | designed | Elvis | DEC-024 | Event count, rating history; cold-start trust signal. |
| Org analytics tier (paid) | Monetization | 1 | decided | Aakash | DEC-018 | Org tier $19.99/mo or $199/yr proceeding; per-event numbers free, rollups/export paid. Financials-owner (governance flag). |
| Payment provisions (gated, not live) | Monetization | 1 | decided | Deepak | DEC-010 | Architected in, toggle-gated; not wired live until phase 1.5. |

## Phase 1.5 (informal, per decisions)

| Feature | Area | Phase | Status | Owner | Linked DEC | Notes |
|---------|------|-------|--------|-------|-----------|-------|
| Payments go-live (ticketing + fee, premium unlocks) | Monetization | later (1.5) | decided | Aakash/Deepak | DEC-010, DEC-018 | Ticketing flagged largest technical scope; needs its own conversation (Stripe Connect, payouts, tax). |
| Individual premium tier | Monetization | later (1.5) | decided (HELD) | Aakash | DEC-018 | $3.99/mo or $36/yr; 30s video, 20 media items, own-content analytics. Ship held pending phase-1 usage data. |
| Full in-app calendar view | Calendar | later (1.5) | decided | Deepak | DEC-013 | Month/list views. |
| Recurring events | Events | later (1.5) | designed | Elvis/Deepak | DEC-021 | Linked Event instances + recurring_group_id; calendar-style semantics; batch generation; snapshot join. |
| Event Series | Events | later (1.5) | designed | Elvis/Deepak | DEC-022 | Master hub; self-curation; multiple series per event. |
| Co-hosts | Events | later (1.5) | decided | Deepak | DEC-022 | Pulled forward from later to ship with Series (revised DEC-024). |
| Free Now (real-time availability + rooms) | Safety/Discovery | later | designed | Elvis/Deepak | DEC-025 | Highest safety flag; rounded location, aggregate-first, reciprocal join; room creation gated on standing; moderation baseline required. |

## Later phase / deferred

| Feature | Area | Phase | Status | Owner | Linked DEC | Notes |
|---------|------|-------|--------|-------|-----------|-------|
| Sunday Deck (swipe discovery) | Discovery | later | deferred | Elvis | DEC-024 | Needs event density; editorial bridge designed ahead (DEC-020). |
| Apply-to-join with host questions | Events | later | deferred | Elvis | DEC-024 | Question builder + approval queue. |
| Annual Wrapped (org + individual) | Social | later | deferred | Elvis | DEC-024 | Retrospective, needs history. |
| P1.2 memories resurfacing | Moments | later | deferred | Elvis | DEC-024 | Per draft P1.2 tag. |
| Private accounts | Social | later | deferred | Elvis | DEC-015 | Slots into most-restrictive-wins when built. |
| Learned per-user recommendation weights | Discovery | later | deferred | Deepak | DEC-020 | Needs real interaction data; two-stage architecture ready for it. |
| Look-alike host affinity | Discovery | later | deferred | Deepak | DEC-023 | Needs scale (cold-start). |
| Aggregate-tag + scavenger icebreakers | Events | later | deferred | Elvis | DEC-025 | Scavenger match-confirm is in-app (locked); rest undesigned. |
| Org analytics phase-1.5 set | Monetization | later (1.5) | decided | Aakash | DEC-018 | Retention, growth, segment performance (min-sample gated), benchmarking, scheduled reports. |
| Ticketing/payments infra | Monetization | later | proposed | Aakash | DEC-010 | Own dedicated conversation; whether phase 1 at all is open. |
| Gamification + virtual goods + avatars/mascot | Feature | later | proposed | Elvis | DEC-025 | One dedicated economy conversation. |
| Supporters marketplace | Monetization | later | proposed | Aakash | DEC-025 | Depends on payments infra. |
| Event music (Spotify integration) | Feature | later | proposed | Elvis/Deepak | DEC-025 | Real external dependency. |
| Ads / promoted listings | Monetization | later | proposed | Aakash | DEC-025 | Deferred; "discuss ads later". |
| Web version | Platform | later | proposed | Deepak | DEC-025 | Platform roadmap item, not a feature design. |
| General user-blocking capability | Safety | later | proposed | Deepak | DEC-023 | Prerequisite for avoid signal; not yet designed. Flag: likely a phase-1 safety baseline, confirm. |
| Attendee-level feedback (thumbs on attendees) | Social | later | proposed | Elvis | DEC-023 | Avoid-signal data source; needs its own scoping pass. |

## Unbacked / needs a decision (flagged, not asserted as scope)

- Whether the general user-blocking feature is actually a phase-1 safety baseline rather than later (DEC-023 assumes it exists). Marked proposed above.
- Whether ticketing/payments is phase 1 at all (DEC-010 sets phasing for provisions; the live build is an open conversation).
