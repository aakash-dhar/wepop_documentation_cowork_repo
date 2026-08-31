# Wepop product overview - app feature map and phase-1 scope

> Owner: Aakash (phase-plan). Plain-language map of what the app does, derived from the source of
> truth. Design detail is Elvis's (`architecture/elvis/`); technical detail is Deepak's
> (`architecture/technical/`). Regenerated 2026-08-26 after DEC-010 to DEC-025; regenerated
> 2026-08-31 after DEC-026 to DEC-047 landed.
> No em-dashes. Contested points defer to `shared/DECISIONS.md`; the phase/status of each feature is
> tracked in `wepop-scope-matrix.md`.

## One-liner

An invite-first, location-based events and meetup app. Get people together in the real world around
shared activities. A meetup app, not a dating app.

## Core objects

- **Event** - a concrete activity at a place and time, with details, a discussion board, media, and
  chat. Can be a standalone event, one occurrence of a recurring group (DEC-021), or a member of one
  or more Event Series (DEC-022). Supports a multi-day start/end date range via `scheduled_end`,
  exposed as an Airbnb-style calendar picker where a single day and a range are the same
  interaction (DEC-041).
- **Idea** - something a user wants to do without hosting it. Others rally around it (interested /
  polls for time and place) and can spin an event out of it. Ideas have no fixed date. Ideas have a
  defined lifecycle (DEC-040): "Pause new joins" (a reversible membership freeze, visible in phase 1),
  90-day inactivity auto-archive (read-only, links survive), delete only while uninteracted, detach
  to system-owned, and a tombstone.
- **Event Series** - a host-created thematic hub page (not itself joinable) with events attached over
  time; closer to an Idea than to a recurring event; self-curation only (DEC-022). Build phase 1.5.
- **User profile** - the person. Onboarding data (age, home neighborhood, gender, languages,
  personality tags, interests, university), followers, created events/ideas, saved items, moments,
  and a "My feedback" entry (DEC-047).
- **Business / Organization profile** - multi-member account. University clubs first, promotional
  accounts later. Ownership transfers cleanly as officers turn over (DEC-024).

## Screen / feature areas

- **Waitlist** - non-invited users; collects email, phone, location, university. Auto-promote with a
  claim window (DEC-024).
- **Onboarding (invited)** - shows who invited you and to what, then join or log in.
- **Registration and auth (DEC-011, DEC-012, DEC-026, DEC-031).** Social login (Kakao, Apple, Google)
  with a phone number always required; Korean carrier numbers verify identity via PASS (government-
  linked carrier real-name auth, returning identity and age), non-Korean numbers run standard phone
  OTP (DEC-026, DEC-011). Password is deferred; email magic-link is the recovery channel; biometrics
  for day-to-day re-login. Age is a self-declared birthdate locked at signup, with country determined
  by a store-region cascade (no forced GPS prompt) and per-country legal-age thresholds in a config
  table (provisional pending counsel, DEC-012). Home location is required at onboarding, input via
  the DEC-003 map picker at neighborhood-scale granularity and reverse-geocoded to a canonical
  neighborhood ID (the precise tapped point is discarded and never persisted); post-onboarding edits
  are current-location only (DEC-031, refining DEC-016). Personality and interest tags are an
  extensible, searchable list (DEC-005).
- **Language and localization (DEC-027, DEC-029).** Language is a synced profile field, initialized
  by a detection cascade (device language, then store region, then phone number) with a manual
  override that always wins; notifications follow it. WePop-authored strings ship fully bilingual
  (Korean/English); user-generated content renders as authored, no translation pipeline at launch.
- **Ideas** - summary, details, discussion board, and time/location polls. Lifecycle per DEC-040
  (see core objects). No media upload on ideas.
- **Events** - fixed place and time (or a multi-day range, DEC-041) via the Google-style map picker
  (DEC-003); details, discussion, media, chat. Create from an idea without re-prompting. Optional
  structured schedule/itinerary of stops (DEC-025), allowed while the date is still under poll, with
  stops binding to the date on confirmation (DEC-041). Event cover media is its own surface: up to 5
  items, photos/videos any mix, video 15s free / 30s paid (DEC-038). All changes notify (batched per
  save) and post into the event's chat; audience is joined plus waitlisted plus pending applicants
  (DEC-042). A completed event is immutable: the host cannot edit, delete, or leave it; deletion is
  admin-only, detachment is a reviewed request, and ratings persist through both (DEC-043).
  Save-as-draft screen still to be added.
- **Recurring events (DEC-021, build 1.5)** - separate linked Event instances sharing a recurring
  group; Google-Calendar-style "this / this and following" edit, delete, and join; batch-generated;
  join is a snapshot, not a standing subscription; the itinerary copies per occurrence (DEC-041).
- **Explore (DEC-020, DEC-032)** - a map view (unranked, bounded to the visible viewport) and a list
  view (fully ranked); filters and search scoped to a location. Map and search are unrestricted
  worldwide; content detail is country-gated for free users (events outside the current-location
  country render as an aggregate teaser), lifted entirely by individual premium (DEC-032).
- **Home** - a personalized ranked mix of events, ideas, and moments.
- **Discovery and recommendations (DEC-019, DEC-020, DEC-030, DEC-036)** - a two-stage
  retrieval-then-ranking pipeline, rule-based at launch and architected for a learned model later.
  The cohort key is a single binary, university-affiliated or not, computed the same way everywhere;
  location is not part of the cohort formula (DEC-030, revising DEC-019). Cohort match is a hard
  retrieval filter at launch, intended to soften into a ranking signal on one global density call.
  Ranking blends tag/keyword overlap, cohort, recency, distance, popularity, social proximity, a
  new-host fairness boost, positive affinity (events attended by people this user tapped positively
  on, DEC-036), and group-composition fit. The avoid signal runs solely off an explicit block; no
  inferred negative signal exists (DEC-036). Interaction logging runs from day one.
- **Chat (DEC-013)** - event and group chat plus DMs and user-created group chats, all in phase 1,
  text only (no audio or video chat).
- **Calendar (DEC-013)** - phase 1 has read-only device busy-time ingestion (times only) and a manual
  per-event add-to-calendar. The full in-app calendar view is phase 1.5.
- **Moments (DEC-014, DEC-015)** - one post-event post per user per event, with photos, video (720p,
  15 seconds, up to 10 media items in phase 1), and a writeup. React, comment, and share on moments
  visible beyond the owner; visibility inherits the event with a per-moment private override, most
  restrictive wins. Reached through the three-step optional post-event feedback flow, open to anyone
  who joined an event that completed; check-in is not a gate (DEC-034, DEC-045).
- **Post-event feedback and ratings (DEC-014, DEC-034, DEC-045, DEC-047)** - three optional,
  skippable steps: rate the event, rate the host, positive-only peer tap (no thumbs-down, no
  bulk-follow). Stars run 1 to 5; unrated is NULL. Feedback is uniformly anonymous with no
  attribution option; a 7-day edit/withdraw window runs from submission, after which removal goes
  through moderation; the author sees their own feedback only in the "My feedback" profile entry,
  the single surface where the author link ever appears (DEC-047). A host's public star average
  displays at 3 ratings, with event and rating counts shown below that; the internal signal uses
  unweighted Bayesian smoothing toward the global mean (DEC-045).
- **Check-in (DEC-045, DEC-046)** - the host scans the attendee (ticketing standard). An operational
  record only: no badge, no scoring weight, gates nothing; surfaces in analytics. Required on
  ticketed events, a free host toggle on capacity-limited events, absent on open events in phase 1;
  attendee self-scan is deferred as self-service mode. Attendance is recorded on two axes: observed
  attendance where check-in ran (attended / claimed-unconfirmed / no-show / not tracked) and
  self-reported intent on every event (on my way / running late / cannot make it), the primary
  reliability source at launch. Declining in advance is never scored like a silent no-show.
- **Live stories (DEC-025)** - a separate ephemeral 24-hour content type; RSVP (not check-in) to
  post; poster-chosen audience across four tiers defaulting to most restrictive.
- **Free Now (DEC-025)** - real-time availability plus location-pinned rooms; rounded location,
  aggregate-first with identities revealed on reciprocal join, room creation gated on account
  standing, moderation a required baseline.
- **Notifications** - invites, follows, event/idea activity, and change notifications per DEC-042.
- **Profiles** - user and organization, with a public org history / track-record module (DEC-024),
  the post-event rating system (DEC-014), and "My feedback" (DEC-047, slotted into the P1.1
  three-tab restructure).
- **Safety and accountability (DEC-006, DEC-017, DEC-035, DEC-037, DEC-044)** - general user
  blocking is a phase-1 baseline in the earliest build wave: bidirectional and total across every
  surface, scope stated at block time (DEC-037). Host accountability splits reputation (deleted with
  the account) from enforcement (ban/suspension records surviving deletion as disclosed
  fraud-prevention data); hashed ban list checked at signup; suspension propagates to operated orgs;
  org creation gated on standing (DEC-044).
- **Icebreakers and tips/guides (DEC-025)** - a phase-1 host question game (up to 3 read-only
  questions, opt-in) and a contextual info-icon guide targeted by situation, not personality. The
  question game's access gate is open: DEC-025 gated it on check-in, which DEC-045/046 made
  non-universal and non-gating (see Open items).

## Monetization (DEC-010, DEC-018, DEC-032, DEC-033, DEC-039)

Payments are architected into phase 1 as gated, toggle-able provisions and go live at phase 1.5
(ticketing with a platform fee, premium unlocks). The organization analytics tier ($19.99/month or
$199/year) proceeds now, with per-event operational numbers free and aggregate rollups, trends, and
export paid; check-in analytics follow the same split (DEC-046). An individual tier ($3.99/month or
$36/year) is specified but its ship timing is held until phase-1 usage data exists; it lifts the
Explore country gate (DEC-032) and raises the apply-to-join screening-question quota from 3 to 10
(DEC-033). Media retention is a tiered differentiator active at launch: nothing is deleted, free-tier
media demotes past a 6-month boundary to thumbnail plus download with two advance warnings, paid
keeps full resolution indefinitely (DEC-039). Gating follows a three-bucket rule (never gate
marketplace actions, quota-gate personal expression, insight-gate analytics); a paid ranking or
discovery boost is explicitly locked out. Commercial-structure detail lives with the financials
owner.

## Privacy and product principles

- Pre-join, show only mutual friends plus aggregate signals, not the full attendee list (DEC-006).
  Gender is not shown to attendees pre-join in any form; hosts retain an aggregate on the event
  details page and in analytics, never on a per-person row (DEC-035, partially superseding DEC-017).
  Individual attendee photos appear pre-join only between mutual (bidirectional) follows (DEC-017).
- Most-restrictive-visibility-setting always wins (DEC-015), applied across moments and series.
- Feedback anonymity is structural: the author-to-feedback link surfaces to a human only in the
  author's own "My feedback" screen, never to hosts, admin UIs, or exports (DEC-047).
- No in-app AI image or video generation (DEC-007). The only AI the user touches is text
  prompt-to-create for an event or idea.
- Moderation is a launch requirement across rating comments, moment comments, chat, Discussion, and
  Free Now rooms (see HOTSHEET: capability, not SLAs, is the launch bar).
- An A/B experimentation capability is built early (bucketed assignment, measured effect), applied
  to design, usability, and algorithm changes (DEC-028).

## Phase-1 scope boundaries

Phase 1 builds the core objects, invite-first onboarding and waitlist, auth (social login plus phone,
PASS in Korea), neighborhood-level home location, anonymous 1-to-5 ratings via the optional
post-event flow, check-in as a host-side operations tool on ticketed and host-opted capacity events,
moments (with video), event cover media, event/group chat plus DMs and user group chats (text only),
the two lightweight calendar pieces, community cohorts (student-vs-not) and the recommendation
algorithm, general user blocking, host accountability, tiered media retention, change notifications,
and the scoped feature set (schedule, live stories, Free Now, icebreakers, tips/guides). Payment
provisions are built but gated off. Deferred to phase 1.5: payments go-live, the individual premium
tier, the full in-app calendar, recurring events, Event Series, and co-hosts. Later still:
self-service check-in mode, Sunday Deck, apply-to-join, annual Wrapped, private accounts, and the
dedicated payments/gamification/ads/marketplace threads.
Full per-feature phase and status: `wepop-scope-matrix.md`.

## Open items

- Icebreaker question-game access: DEC-025 gated it on check-in; DEC-045/046 made check-in
  non-universal and non-gating. Needs a replacement access rule (or none).
- Whether the cohort hard filter reverts to a ranking signal on the single global density call, and
  who owns that call (DEC-019/DEC-020/DEC-030).
- Check-in open list (DEC-046): what "surfaces in analytics" means concretely; how no-show and
  punctuality data is eventually used and whether any of it is user-visible; visibility of the
  claimed-unconfirmed state; self-reported intent detail, which is designed in Elvis's files but
  documented nowhere in this repo (a documentation task, not a design one).
- Feedback open list (DEC-047): whether an edited rating shows as edited; where aggregates surface
  to the host. Watch item: no-show rating abuse now that weighting is withdrawn (DEC-045, HOTSHEET).
- Free Now open details (account-standing threshold, duration cap, archival, org rooms);
  live-stories vs the org media cap; DEC-038's total-video-duration cap and org-paid video length;
  DEC-039's three retention refinements pending Elvis; the DEC-044 parameter list (cooldown, ban
  retention, tenure minimums, propagation automation, reinstatement).
- 위치정보법: DLG to confirm that deferring self-scan removes the phase-1 trigger (L-3, TASK-040;
  HOTSHEET Blocking until confirmed).
- Age/location logic pending legal counsel (DEC-012, TASK-013). Map picker interaction detail still
  to be finalized. How much legacy code is reused vs rebuilt (DEC-008).
- Commercial-structure proposal channel, the ticketing/payments build conversation (DEC-018,
  DEC-010), and the Korea non-Stripe payments path (HOTSHEET).
- Save-as-draft screen and the profile description field (todos #6, #7).
