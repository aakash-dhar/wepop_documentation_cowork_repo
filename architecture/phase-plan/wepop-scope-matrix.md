# Wepop scope matrix - phase and feature tracker

> Owner: Aakash (phase-plan). Others suggest via `suggestions/`. Derived, grounded only in a landed
> decision or a design intake; never invented scope. When this disagrees with `shared/DECISIONS.md`,
> DECISIONS wins. Generated 2026-08-26 after DEC-010 to DEC-025 landed; updated 2026-08-31 after DEC-026 to DEC-044 landed.
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
| Events + Ideas core objects | Events/Ideas | 1 | designed | Elvis | walkthrough, DEC-009, DEC-040 | Idea toggle now exposed as "Pause new joins" (reversible membership freeze); Ideas gain a lifecycle (90-day auto-archive, delete-if-uninteracted, detach to system-owned, tombstone) per DEC-040, superseding DEC-009's do-not-expose. No media upload on ideas. |
| Event schedule / itinerary | Events | 1 | designed | Elvis | DEC-025, DEC-041 | Ordered stops reuse the DEC-003 picker; visibility inherits the event. Multi-day confirmed (Event supports start/end via scheduled_end, Airbnb-style picker); schedule allowed pre-confirmation; recurring copies itinerary and joins DEC-021's this/following propagation. |
| Ratings + post-event feedback (3-step) | Social | 1 | designed | Elvis | DEC-014, DEC-034 | Optional/skippable. No longer check-in gated (DEC-034): any attendee of a completed event may rate; verified feedback weighted 1.0, unverified 0.4, Bayesian smoothing C=5, public average gated at 3 verified. Attendee thumbs-down removed; single positive-only tap; no bulk-follow. |
| QR check-in (verification badge + weight) | Events | 1 | decided | Deepak | DEC-014, DEC-034 | No longer load-bearing or required (DEC-034): grants a verification badge and a feedback scoring weight (1.0 verified / 0.4 unverified), not access. Printed-poster geofence mode has an open 위치정보법 registration question (HOTSHEET Blocking, R5). |
| Moments (content + visibility + video) | Moments | 1 | designed | Elvis | DEC-015 | One per user per event; react/comment/share; most-restrictive-wins; video 720p/H.264/15s/10 items. |
| Live stories (ephemeral) | Moments | 1 | designed | Elvis | DEC-025 | Separate 24h content type; RSVP to post; poster-chosen audience (4 tiers). Media-cap interaction open. |
| Anti-stalking pre-join visibility | Safety | 1 | designed | Elvis/Deepak | DEC-006, DEC-017 | Mutuals + aggregates pre-join; gender aggregate-only; photos only to mutual (bidirectional) follows. |
| DM + user-created group chats | Chat | 1 | decided | Deepak | DEC-013 | Text only, no audio/video. Pulled into phase 1 (superseded DEC-009). Moderation surface. |
| Event/group chat | Chat | 1 | designed | Elvis/Deepak | DEC-009, DEC-013 | Text, photos, replies, reactions. |
| Calendar: busy-time ingestion + add-to-calendar | Calendar | 1 | decided | Deepak | DEC-013 | Read-only free/busy (times only, discard rest); manual per-event write. Full in-app calendar to phase 1.5. |
| Community cohorts (segmentation) | Discovery | 1 | designed | Elvis/Deepak | DEC-019 | (city, life-stage) + university override; hard retrieval filter at launch, manual per-city softening. |
| Recommendation algorithm | Discovery | 1 | designed | Elvis/Deepak | DEC-020 | Two-stage retrieval/ranking; rule-based, ML-ready; Explore map (unranked) vs list (ranked); new-host boost; day-one logging. |
| Group-dynamics signals | Discovery | 1 | designed | Elvis/Deepak | DEC-023, DEC-036 | Avoid signal is now block-only (DEC-036); the inferred low-rating half is dropped. Positive tap feeds a positive-affinity ranking signal alongside DEC-020 social proximity. Both prerequisites resolved (blocking DEC-037; feedback DEC-036). Personality-mix ranking signal retained. |
| Event icebreakers (host question game) | Events | 1 | designed | Elvis | DEC-025 | Up to 3 read-only questions, check-in gated, opt-in. Tag-matching + scavenger later. |
| Tips/guides | Content | 1 | designed | Elvis | DEC-025 | Contextual info icon + static guide; situation/status targeted; copy written later (ux-copy). |
| Waitlist auto-promote + claim window | Events | 1 | designed | Elvis | DEC-024 | Completes existing waitlist mechanic. |
| Org profiles + ownership transfer | Org | 1 | designed | Elvis | walkthrough, DEC-024 | University clubs first; ownership transfer structural for officer turnover. |
| Public org track-record module | Org | 1 | designed | Elvis | DEC-024 | Event count, rating history; cold-start trust signal. |
| Event cover media | Events | 1 | designed | Elvis | DEC-038 | Separate surface from Moment media: up to 5 items, photos/videos any mix, video 15s free / 30s paid. Open: total-video-duration cap and org-paid video length. |
| Media retention (tiered) | Monetization | 1 | decided | Aakash | DEC-039 | Tiered, active at launch, 6-month boundary; nothing deleted, free-tier demotes to thumbnail+download, paid keeps full-res indefinitely; two advance warnings. Financials-owner. Three refinements open pending Elvis. |
| Change notifications (events + ideas) | Events | 1 | designed | Elvis | DEC-042 | All event/idea changes notify; event changes also post to event chat; batched per save; audience is joined + waitlisted + pending apply-to-join. |
| Completed-event immutability | Events | 1 | designed | Elvis | DEC-043 | Host cannot delete or edit a completed event; deletion admin-only (moderation or PIPA erasure); host detachment is a reviewed request; ratings persist through detach and delete. |
| Host accountability (reputation/enforcement split) | Safety | 1 | designed | Elvis/Deepak | DEC-044 | Reputation deleted with account; enforcement (ban/suspension) survives as 부정이용 fraud-prevention data; hashed ban list (CI key for Korea); suspension propagates to operated orgs; org creation gated on standing. Several parameters open. |
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
| General user-blocking capability | Safety | 1 | designed | Deepak | DEC-023, DEC-037 | Confirmed phase-1 safety baseline, earliest build wave (DEC-037): bidirectional and total across every surface (feed, Explore, comment threads); scope stated to the user at block time; checked at retrieval time. |
| Attendee-level feedback (positive-only tap) | Social | 1 | designed | Elvis | DEC-034, DEC-036 | Thumbs up/down replaced by a single positive-only tap (DEC-034); no negative peer record exists. Feeds the positive-affinity ranking signal (DEC-036). Was the DEC-023 avoid-signal data source; that dependency is now closed in the positive direction only. |

## Unbacked / needs a decision (flagged, not asserted as scope)

- Whether ticketing/payments is phase 1 at all (DEC-010 sets phasing for provisions; the live build is an open conversation).
