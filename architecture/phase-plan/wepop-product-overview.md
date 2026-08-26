# Wepop product overview - app feature map and phase-1 scope

> Owner: Aakash (phase-plan). Plain-language map of what the app does, derived from the source of
> truth. Design detail is Elvis's (`architecture/elvis/`); technical detail is Deepak's
> (`architecture/technical/`). Regenerated 2026-08-26 after DEC-010 to DEC-025 landed.
> No em-dashes. Contested points defer to `shared/DECISIONS.md`; the phase/status of each feature is
> tracked in `wepop-scope-matrix.md`.

## One-liner

An invite-first, location-based events and meetup app. Get people together in the real world around
shared activities. A meetup app, not a dating app.

## Core objects

- **Event** - a concrete activity at a place and time, with details, a discussion board, media, and
  chat. Can be a standalone event, one occurrence of a recurring group (DEC-021), or a member of one
  or more Event Series (DEC-022).
- **Idea** - something a user wants to do without hosting it. Others rally around it (interested /
  polls for time and place) and can spin an event out of it. Ideas have no fixed date.
- **Event Series** - a host-created thematic hub page (not itself joinable) with events attached over
  time; closer to an Idea than to a recurring event; self-curation only (DEC-022). Build phase 1.5.
- **User profile** - the person. Onboarding data (age, city, gender, languages, personality tags,
  interests, university), followers, created events/ideas, saved items, and moments.
- **Business / Organization profile** - multi-member account. University clubs first, promotional
  accounts later. Ownership transfers cleanly as officers turn over (DEC-024).

## Screen / feature areas

- **Waitlist** - non-invited users; collects email, phone, location, university. Auto-promote with a
  claim window (DEC-024).
- **Onboarding (invited)** - shows who invited you and to what, then join or log in.
- **Registration and auth (DEC-011, DEC-012, DEC-016).** Social login (Kakao, Apple, Google) with a
  phone number always required; a provider-verified phone (Kakao, Korea in practice) can satisfy
  verification, otherwise phone OTP runs. Password is deferred to a later phase; email magic-link is
  the recovery channel; biometrics for day-to-day re-login. Age is a self-declared birthdate locked
  at signup, with country determined by a store-region cascade (no forced GPS prompt) and per-country
  legal-age thresholds in a config table (provisional pending counsel). A general city-level location
  is required at onboarding (typed or selected); device GPS stays optional and contextual. Personality
  and interest tags are an extensible, searchable list (DEC-005).
- **Ideas** - summary, details, discussion board, and time/location polls. "Close to new joiners"
  toggle is built but not exposed (DEC-009). No media upload on ideas.
- **Events** - fixed place and time via the Google-style map picker (DEC-003); details, discussion,
  media, chat. Create from an idea without re-prompting. Optional structured schedule/itinerary of
  stops (DEC-025). Save-as-draft screen still to be added.
- **Recurring events (DEC-021, build 1.5)** - separate linked Event instances sharing a recurring
  group; Google-Calendar-style "this / this and following" edit, delete, and join; batch-generated;
  join is a snapshot, not a standing subscription.
- **Explore (DEC-020)** - a map view (unranked, bounded to the visible viewport) and a list view
  (fully ranked by the recommendation algorithm); filters and search scoped to a location.
- **Home** - a personalized ranked mix of events, ideas, and moments.
- **Discovery and recommendations (DEC-019, DEC-020, DEC-023)** - a two-stage retrieval-then-ranking
  pipeline, rule-based at launch and architected for a learned model later. Community cohorts
  (city plus age/life-stage, with a university-affiliated override) act as a hard retrieval filter at
  launch, softening per city as density grows. Ranking blends tag/keyword overlap, cohort, recency,
  distance, popularity, social proximity, a new-host fairness boost, and group-composition fit.
  Interaction logging runs from day one.
- **Chat (DEC-013)** - event and group chat plus DMs and user-created group chats, all in phase 1,
  text only (no audio or video chat).
- **Calendar (DEC-013)** - phase 1 has read-only device busy-time ingestion (times only) and a manual
  per-event add-to-calendar. The full in-app calendar view is phase 1.5.
- **Moments (DEC-014, DEC-015)** - one post-event post per user per event, with photos, video (720p,
  15 seconds, up to 10 media items in phase 1), and a writeup. React, comment, and share on moments
  visible beyond the owner; visibility inherits the event with a per-moment private override, most
  restrictive wins. Reached through a three-step, optional, check-in-gated post-event feedback flow
  (rate the event, rate the people, add moments).
- **Live stories (DEC-025)** - a separate ephemeral 24-hour content type; RSVP (not check-in) to post;
  poster-chosen audience across four tiers defaulting to most restrictive.
- **Free Now (DEC-025)** - real-time availability plus location-pinned rooms; rounded location,
  aggregate-first with identities revealed on reciprocal join, room creation gated on account
  standing, moderation a required baseline.
- **Notifications** - invites, follows, event/idea activity.
- **Profiles** - user and organization, with a public org history / track-record module (DEC-024) and
  the post-event rating system (DEC-014).
- **Icebreakers and tips/guides (DEC-025)** - a phase-1 host question game (check-in gated) and a
  contextual info-icon guide targeted by situation, not personality.

## Monetization (DEC-010, DEC-018)

Payments are architected into phase 1 as gated, toggle-able provisions and go live at phase 1.5
(ticketing with a platform fee, premium unlocks). The organization analytics tier ($19.99/month or
$199/year) proceeds now, with per-event operational numbers free and aggregate rollups, trends, and
export paid. An individual tier ($3.99/month or $36/year) is specified but its ship timing is held
until phase-1 usage data exists. Gating follows a three-bucket rule (never gate marketplace actions,
quota-gate personal expression, insight-gate analytics); a paid ranking or discovery boost is
explicitly locked out. Commercial-structure detail lives with the financials owner.

## Privacy and product principles

- Pre-join, show only mutual friends plus aggregate signals, not the full attendee list (DEC-006).
  Gender is an aggregate ratio only; individual attendee photos appear pre-join only between mutual
  (bidirectional) follows (DEC-017).
- Most-restrictive-visibility-setting always wins (DEC-015), applied across moments and series.
- No in-app AI image or video generation (DEC-007). The only AI the user touches is text
  prompt-to-create for an event or idea.
- Moderation is a launch requirement across rating comments, moment comments, chat, and Free Now
  rooms (see HOTSHEET).

## Phase-1 scope boundaries

Phase 1 builds the core objects, invite-first onboarding and waitlist, auth, ratings with required QR
check-in, moments (with video), event/group chat plus DMs and user group chats (text only), the two
lightweight calendar pieces, community cohorts and the recommendation algorithm, and the scoped
feature set (schedule, live stories, Free Now, icebreakers, tips/guides). Payment provisions are built
but gated off. Deferred to phase 1.5: payments go-live, the individual premium tier, the full in-app
calendar, recurring events, Event Series, and co-hosts. Later still: Sunday Deck, apply-to-join,
annual Wrapped, private accounts, and the dedicated payments/gamification/ads/marketplace threads.
Full per-feature phase and status: `wepop-scope-matrix.md`.

## Open items

- Whether the cohort hard filter reverts to a ranking signal once a city softens, and who owns the
  manual per-city density call (DEC-019/DEC-020).
- Two prerequisites for group-dynamics recommendations are undesigned: a general user-blocking
  feature and an attendee-level feedback mechanism (DEC-023).
- Free Now open details (account-standing threshold, duration cap, archival, org rooms); live-stories
  vs the org media cap; whether the Event model supports a multi-day date range (schedule depends).
- Age/location logic pending legal counsel (DEC-012, TASK-013). Map picker interaction detail still
  to be finalized. How much legacy code is reused vs rebuilt (DEC-008).
- Commercial-structure proposal channel and the ticketing/payments build conversation (DEC-018,
  DEC-010).
