# DECISIONS.md - Wepop decision log (SOURCE OF TRUTH)

> Merger-only file. Everyone else proposes via `workspaces/[you]/proposed-decisions.md`.
> This file is the single source of truth. When any document conflicts with it, defer to the
> latest DECISIONS.md entry.

## Conventions

- Each decision has a unique ID `DEC-NNN` (zero-padded, never reused).
- Status is one of `ACTIVE` / `SUPERSEDED` / `PENDING`.
- Superseded decisions are never deleted. They are marked SUPERSEDED with a pointer to the replacement.
- If a decision is ever modified, add a change-history note to that entry.
- No em-dashes. Governance values are ALLOW / BLOCK / ESCALATE, never DENY.

## Entry format

```markdown
### DEC-NNN: {{Title}}
**Date:** YYYY-MM-DD
**Participants:** {{who}}
**Status:** ACTIVE

**Decision:** {{one clear statement}}
**Reasoning:** {{why this over alternatives}}
**Impact:** {{what changes as a result}}
```

---

## Decisions

### DEC-001: Central GitHub repo as source of truth plus Cowork PM harness
**Date:** 2026-08-17
**Participants:** Aakash, Elvis
**Status:** ACTIVE

**Decision:** Wepop coordination runs off one central GitHub repo as the single source of truth, with a Cowork PM harness on top. Elvis shares his GitHub ID, Aakash creates the repo, sends the invite, and runs a short setup call.
**Reasoning:** Removes back-and-forth document sharing and gives both sides a common, versioned source of truth.
**Impact:** Elvis pushes design and doc updates to the repo; Aakash pulls and maintains the PM record and status there.

### DEC-002: Age gating tied to country legal age
**Date:** 2026-08-17
**Participants:** Aakash, Elvis, Deepak
**Status:** SUPERSEDED (by DEC-012, 2026-08-26)

**Change history:** 2026-08-26 - superseded by DEC-012. The country-tied-legal-age principle is carried forward; the mechanism (triggering location permission early) is replaced by a self-declared birthdate plus a store-region country cascade with no forced GPS prompt. DEC-012 remains provisional pending legal counsel (TASK-013).

**Decision:** Age eligibility is tied to the user's country legal age. If the entered age is under a threshold (around 19), the app triggers location permission early, checks the country's legal age, and blocks under-age users with a message that names the country.
**Reasoning:** Legal age differs by country (US 18, Korea 19, Germany 16). Checking against the country avoids letting through under-age users while keeping the block early rather than after a long flow. Focus markets are Korea and the US.
**Impact:** Registration gains an early conditional location and age check. Provisional: the exact logic (passive vs active location capture, travel-jurisdiction handling) is pending legal counsel before implementation is locked. See the risk register in HOTSHEET.md (R1).

### DEC-003: Event location picker uses Google-Maps-style select
**Date:** 2026-08-17
**Participants:** Aakash, Elvis, Deepak
**Status:** ACTIVE

**Decision:** The map picker uses a Google-Maps-style model (search plus tap a place, showing the place name) rather than the Uber-style fixed center-pin, with zoom, a free-text address field, and an optional per-event note for the exact unit. Profile location captures only the general city.
**Reasoning:** Events need a human-readable named place, not raw latitude and longitude. The center-pin model suits precise pickup points (Uber) but reads poorly for "let's meet at this park". Profiles do not need a home's exact coordinates.
**Impact:** One map interaction pattern across the app for places; text-address plus note covers exact-unit cases. One picker interaction detail is still to be finalized by Elvis and Deepak.

### DEC-004: Auth - OTP required, optional password, biometrics if feasible
**Date:** 2026-08-17
**Participants:** Aakash, Elvis
**Status:** SUPERSEDED (by DEC-011, 2026-08-26)

**Change history:** 2026-08-26 - superseded by DEC-011. Phone verification for every account is carried forward; provider-supplied verified phone (Kakao/Korea only) may now satisfy verification, the optional password is deferred to a later phase, and email magic-link becomes the recovery channel.

**Decision:** Phone OTP verification is required to verify every user. An optional password is also offered, and biometric login is added if feasible.
**Reasoning:** OTP alone cannot cover a lost or blocked phone or a reset. A password is a fallback where SMS/OTP is regionally blocked (for example when the sending business is not registered in that region) and enables password reset.
**Impact:** Signup always verifies the phone via OTP; users may additionally set a password; biometric login is a nice-to-have.

### DEC-005: Replace MBTI with an extensible tag list
**Date:** 2026-08-17
**Participants:** Aakash, Elvis
**Status:** ACTIVE

**Decision:** The personality field is an extensible list of tags (MBTI values included as tags) rather than an MBTI selector. Show the top 10-20 common tags, make them searchable, and let users add their own.
**Reasoning:** A growing tag database is richer for the recommendation and event-matching algorithm than a fixed MBTI type.
**Impact:** Onboarding shows a searchable, user-extendable tag picker feeding matching.

### DEC-006: Anti-stalking visibility model
**Date:** 2026-08-17
**Participants:** Aakash, Elvis, Deepak
**Status:** ACTIVE

**Decision:** Before a user joins an event or idea, show only mutual friends' attendance plus aggregate signals (people near your age, area, and interests), not the full attendee list. Lock fuller info until the user joins or marks interested. Show mutuals' profile pictures only.
**Reasoning:** Keeps Wepop a meetup app rather than a stalking or dating app, reduces liability, and pushes users toward the activity rather than judging attendees by looks.
**Impact:** Event and idea detail views gate the attendee list and richer info behind joining; only mutuals' pictures appear pre-join. Whether to show gender and photos at all is still open and not settled by this decision.

### DEC-007: No in-app AI image or video generation for now
**Date:** 2026-08-17
**Participants:** Aakash, Elvis, Deepak
**Status:** ACTIVE

**Decision:** The app does not generate AI images or video for users. The only AI the user interacts with is text prompt-to-create for an idea or event.
**Reasoning:** Current AI images read as low-quality and off-brand for a real-world meetup app, and skipping generation saves on token cost.
**Impact:** Users upload their own photos; no in-app image or video generation is built for this phase.

### DEC-008: Salvage and build on the existing Wepop code
**Date:** 2026-08-17
**Participants:** Aakash, Elvis, Deepak
**Status:** ACTIVE

**Decision:** Reuse and salvage the existing Wepop codebase and build on top of it with AI rather than rebuilding from scratch.
**Reasoning:** Reduces the timeline and gets features sorted faster.
**Impact:** Design decisions should account for what the legacy code already supports. How much is reused vs rebuilt is still being assessed.

### DEC-009: Phase-1 scope boundaries
**Date:** 2026-08-17
**Participants:** Aakash, Elvis
**Status:** SUPERSEDED (by DEC-013, 2026-08-26)

**Change history:** 2026-08-26 - superseded by DEC-013 for chat and calendar only. The idea "close to new joiners" toggle (built, not exposed) and no-media-on-ideas provisions are carried forward unchanged; DM and user-created group chats move into phase 1 and the calendar is split (phase 1 busy-time ingestion plus manual add-to-calendar; full in-app calendar to phase 1.5).

**Decision:** For phase 1: build the idea "close to new joiners" toggle but do not expose it; defer the calendar view and device calendar (Google / iCal) integration to a later phase; ship event and group chat first, with DM and user-created group chats later if they cannot be done one-shot with AI, and no audio or video chat (text only); no media upload on ideas (photos go in the discussion board).
**Reasoning:** A new app needs more joiners not fewer, so a "close" toggle is premature to expose. The deferred items are lower priority than core flows and reduce phase-1 build scope.
**Impact:** Sets a clear phase-1 line for design and build.

### DEC-010: Payments and monetization phasing
**Date:** 2026-08-24
**Participants:** Aakash, Elvis
**Status:** ACTIVE

**Decision:** Payments (event ticketing with a platform fee, and a gated premium-feature tier) are architected into the Phase 1 codebase as toggle-able, gated provisions but not wired live until the end of Phase 1 ("Phase 1.5"). Wepop uses Programination's existing Stripe account rather than a new one.
**Reasoning:** Getting the core Phase 1 structure to a demo-ready state for investors takes the primary seat; baking payment provisions in from the start makes enabling them later a toggle rather than a rebuild, and AI-assisted build makes the payments piece fast to complete once the structure is solid.
**Impact:** Phase 1 build carries payment provisions (gated, not live). Payments become a Phase 1.5 milestone. Elvis reflects the payments vision in the docs now. No new Stripe account needed. The detailed ticketing build (and whether it is phase 1 at all) is a separate dedicated conversation (see DEC-018). Relates to DEC-009, DEC-018.

### DEC-011: Auth model - social login plus phone, password deferred
**Date:** 2026-08-19
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Social login (Kakao, Apple, Google) may create or sign in an account, but a phone number is always required. If the provider supplies a verified phone (Kakao only, under a business-reviewed scope, Korea-only in practice) that satisfies verification; otherwise the app runs its own phone OTP. Password is deferred to a later phase, with email magic-link or emailed code as the recovery channel and biometrics for day-to-day re-login.
**Reasoning:** A password is a fallback channel, not a security upgrade, and phone OTP is stronger; an optional post-signup password has very low adoption so it would not exist for the user who needs it; email is already collected from every account, so an email link covers 100 percent of accounts with no added onboarding step; the Kakao skip narrows rather than removes OTP (the full flow still ships for every provider).
**Impact:** Every account still has a verified phone. CLAUDE.md section 8 invariant changes from "Phone OTP verifies every user; optional password and biometrics are additive" to phone-verified accounts with OTP as default and provider-supplied verification as the exception. Revisit trigger: add a password when support data shows a real recovery gap or on entering a market where SMS is genuinely blocked. Supersedes DEC-004. Source: `workspaces/elvis/conflict-review-2026-08-19.md` item 2.

### DEC-012: Age gate and country determination mechanism
**Date:** 2026-08-19
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE (provisional, pending legal counsel per TASK-013)

**Decision:** Age is a self-declared birthdate typed once and locked at signup (correctable only via support, ToS ban if falsified), with no ID verification in phase 1. Country is determined once at registration via a fallback cascade (app store region first, then device location only if already granted, then phone number country code) and set permanently, never re-checked as the user travels. Per-country age thresholds live in a config table, not hardcoded in a screen.
**Reasoning:** Matches the industry norm (self-declared birthdate against a per-country minimum-age table, no forced GPS prompt, which is the most-declined onboarding step); the invite-first model is a real structural mitigation the comparison apps lack; a config table turns a legal answer from counsel into a config change rather than a design revision.
**Impact:** Registration gains no forced early location prompt. Supersedes DEC-002; the country-tied-age principle is preserved but its "trigger location permission early" mechanism is replaced. Stays provisional until TASK-013 closes with counsel. Signal-conflict handling (store region vs phone code) and the store-region APIs (StoreKit, Play Billing) are flagged to TASK-013 and Deepak. Source: `workspaces/elvis/conflict-review-2026-08-19.md` item 3.

### DEC-013: Phase-1 chat and calendar scope
**Date:** 2026-08-19
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** DM and user-created group chats are pulled fully into phase 1 (text only, no audio or video chat). The calendar is split: phase 1 gets read-only device busy-time ingestion (start/end times only, everything else discarded) plus a manual per-event "add to my calendar" write; the full in-app calendar view (month/list) is deferred to phase 1.5.
**Reasoning:** Chat is core to the product experience, not primarily a build-difficulty call; the two phase-1 calendar pieces improve recommendations and convenience without an in-app calendar UI; contextual (not forced) calendar-read permission is consistent with the location stance in DEC-016.
**Impact:** Largest scope addition of the conflict-review set. Live messaging is infrastructure (delivery, presence, push) and adds a third moderation surface. Supersedes DEC-009 for chat and calendar only; DEC-009's "close to new joiners" toggle and no-media-on-ideas provisions carry forward unchanged. Source: `workspaces/elvis/conflict-review-2026-08-19.md` item 6.

### DEC-014: Post-event feedback (ratings and reviews)
**Date:** 2026-08-19
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** After an event, checked-in attendees see a three-step feedback flow, every field optional and every step skippable: (1) rate the event 0-5 stars plus optional anonymous text with an everyone/host-only visibility toggle defaulting to everyone, (2) rate the host 0-5 plus a comment and give other attendees a thumbs up/down, all anonymous, (3) add moments. Attendee thumbs are an internal recommendation signal only, never shown to anyone.
**Reasoning:** Resolves the draft conflict (Phase 1 Brief ships ratings, Moments spec v0.9 bans them) in favor of ratings, while keeping attendee peer-rating inside the DEC-006 reasoning by never surfacing it. Steps 1 and 2 feed host reputation and the recommendation engine.
**Impact:** QR check-in becomes REQUIRED for phase 1 (it gates feedback, ratings, and recommendations, not only moments). Moderation becomes a launch blocker (anonymous public-by-default text needs day-one removal). Low check-in rate becomes a product risk. Moments spec loses its ratings ban; Phase 1 Brief rating/Reviews screens are reworked to this flow. Small open item: whether 0 is a real star value or means unrated. Relates to DEC-006, DEC-015. Source: `workspaces/elvis/conflict-review-2026-08-19.md` item 1.

### DEC-015: Moments content and visibility model
**Date:** 2026-08-19
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** A moment is one post per user per event (never a paid lever). Moments visible beyond the owner support reactions, comments, and share (all in for phase 1). A moment inherits the visibility of its event by default; the owner can override an individual moment to private; the most-restrictive setting always wins. Private accounts are deferred. Video is in phase 1 at 720p H.264, roughly 3 Mbps, a flat 15-second cap and a flat 10-media-item cap for everyone (server-side transcode of every upload required).
**Reasoning:** Resolves the draft conflict (comments and video in vs out) toward an Instagram-like model for shared moments while preserving the memory-keeping tone for private ones; the most-restrictive-wins rule is adopted as a general principle so it scales as more visibility settings are added; flat caps because the individual premium unlock is deferred (DEC-018).
**Impact:** Public moment comments are a second moderation surface (on top of anonymous host-rating comments). Video cost (transcode, storage, bandwidth) enters phase 1 scope, overriding the Moments spec deferral. Recommend consolidating the scattered visibility rules into one visibility-model spec. The 10-item cap is where the individual premium tier's 20-item allowance attaches later. Relates to DEC-006, DEC-007, DEC-014, DEC-018. Source: `workspaces/elvis/conflict-review-2026-08-19.md` items 4 and 5.

### DEC-016: Location at registration
**Date:** 2026-08-24
**Participants:** Aakash, Elvis
**Status:** ACTIVE

**Decision:** Registration requires a general city-level location that is typed or selected from a list/search (not a device permission grant). Device GPS permission stays optional and is requested contextually (never at registration), with a plain explanation that recommendations are only city-level accurate without it and an in-app nudge re-surfaced whenever the user hits a value point that benefits from precise location.
**Reasoning:** Satisfies the "required" half of the original push without reopening DEC-012's no-forced-GPS-prompt decision, since nothing OS-level is requested; the contextual nudge respects OS re-prompt limits (deep-link to Settings once the OS will not re-trigger its dialog).
**Impact:** Resolves open question O1 (was on the HOTSHEET Needs Attention). City-level location (for discovery) is kept deliberately distinct from the age-gate country signal (for legal compliance); the two are not merged, and the city field is not added to DEC-012's country cascade. Relates to DEC-012, DEC-003. Source: `workspaces/elvis/conflict-review-2026-08-19.md` item 7.

### DEC-017: Pre-join visibility of gender and photos
**Date:** 2026-08-24
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** In an event's pre-join attendee view, gender is shown only as an aggregate ratio (for example "roughly 60% women, 40% men") with no individual attribution, and individual attendee photos are not shown except between two people who mutually follow each other (both directions); a one-way follow never unlocks this.
**Reasoning:** Extends DEC-006 to two data types weighed on their own after it was written; the protected risk is a stranger learning that a specific person will be at a specific place and time by browsing an event page, so a one-way follow must not unlock it (a trivial surveillance vector), while a mutual follow is reciprocal by construction.
**Impact:** Deepak must check follow-state bidirectionally when rendering a pre-join attendee list, not just whether the browser follows the attendee. Governs the pre-join attendee list specifically, not general profile-photo visibility (accounts are public in phase 1 per DEC-015). Extends DEC-006. Source: `workspaces/elvis/conflict-review-2026-08-19.md` item 8.

### DEC-018: Freemium model and commercial structure
**Date:** 2026-08-24
**Participants:** Elvis (design), Aakash (financials owner)
**Status:** ACTIVE

**Decision:** Two premium tiers on separate timelines: an individual tier at $3.99/month or $36/year (30s video, 20 media items per moment, own-content engagement analytics) whose ship timing is HELD until phase-1 usage data exists, and an organization tier at $19.99/month or $199/year (per-organization billing, 7-day trial) proceeding now, split so per-event operational numbers stay free and aggregate rollups/trends/export are paid. Gating follows a three-bucket rule (never gate marketplace actions, quota-gate personal expression, insight-gate analytics). Paid ranking/discovery boost is explicitly locked out. Attendee media caps are 10 free / 20 individual-paid / 50 at org-paid events (most-generous-wins). Media retention is 12 months. Price against realistic usage with a manual safety valve for extreme-usage orgs.
**Reasoning:** Willingness to pay differs by roughly an order of magnitude between a casual individual host and an org that needs data to justify budget; a paid boost would cut against the fairness/anti-stalking moat; retention (not the sticker price) is the real cost lever, grounded in a Cloudflare R2/AWS cost model.
**Impact:** Establishes Wepop's commercial structure (PROJECT_STRATEGY.md "Commercial structure" was marked to-fill). Infra recommendation flagged to Deepak (R2 over S3+CloudFront, self-hosted 720p transcode over Cloudflare Stream). Grandfathering left open. GOVERNANCE: financials-owner (Aakash) territory and CLAUDE.md section 6 defines no proposed-project-strategy channel; the corresponding PROJECT_STRATEGY.md commercial-structure rewrite is deferred until that channel is defined. Relates to DEC-010, DEC-015. Source: `workspaces/elvis/freemium-model-2026-08-19.md`.

### DEC-019: Community segmentation (cohorts)
**Date:** 2026-08-25
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Change history:** 2026-08-26 - refined (2026-08-26 team sync): content from users you follow is exempt from the launch cohort hard retrieval filter and is instead surfaced/ranked via social proximity, rather than excluded for being in a different cohort. Deepak: the retrieval query unions the cohort set with content from followed users.

**Decision:** Users are grouped into cohorts defined as (city, age/life-stage bucket), computed independently per user from their own profile (no inheritance from an inviter). University-affiliated users (verified by any of self-declared student status, school email domain, or membership in a university-flagged Org profile) are pulled into their own (city, university-affiliated) cohort at launch, one per city regardless of school. At launch cohort match is a hard retrieval filter (a candidate outside the cohort is excluded before ranking), relaxing per city via a manual PM-reviewed density call, at which point cohort is intended to soften back into a weighted ranking signal.
**Reasoning:** Solves the cold-start cohort problem (a college student and a 40-something joining the same city should not be pooled with no structure) without separate servers or data partitioning; one unified data platform underneath, restricted only by what a retrieval query returns; mirrors Facebook's per-network cold start and merge.
**Impact:** No new data-model entity by itself; becomes a signal/filter on the recommendation layer (DEC-020). Deepak flags: cohort computed from profile signals, university check first; hard filter in the retrieval query at launch; per-market school-domain lists and an Org "university-affiliated" flag; a lightweight manual per-city review process. Open (HOTSHEET): whether cohort softens to a ranking signal, and who owns the density call. Relates to DEC-020, DEC-005, DEC-006. Source: `workspaces/elvis/community-segmentation-2026-08-25.md`.

### DEC-020: Recommendation algorithm architecture
**Date:** 2026-08-25
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Change history:** 2026-08-26 - clarified (2026-08-26 team sync): a followed user's events bypass the DEC-019 cohort filter and are pulled into the candidate set via the social-proximity signal (w6), so a connection surfaces out-of-cohort content instead of hiding it.

**Decision:** Home feed and Explore run a two-stage pipeline (cheap retrieval then weighted ranking), rule-based at launch (no learned model, since there is no engagement history) but architected so a learned ranker can slot into the ranking stage later. Explore splits into an unranked, viewport-bounded map view and a fully-ranked list view. Ranking uses a normalized weighted sum over launch-available signals (tag/keyword overlap, cohort, recency, geo, popularity, social proximity, new-host boost, group-composition fit) with a deliberate new-host fairness boost. Keyword extraction from titles/descriptions and an evolving per-user interest profile feed the tag signal. A hidden internal keyword layer (admin-visible) spans ideas/events/moments/users. Interaction logging ships day one. One global weight formula at launch, learned per-user weights a later phase.
**Reasoning:** Pure collaborative filtering is not viable at launch (cold start), so the honest starting point is content-based and rule-driven; the two-stage split and day-one logging make a later ML upgrade an extension rather than a rebuild; the new-host boost counters a rich-get-richer popularity loop.
**Impact:** Defines how discovery works. Cohort (DEC-019) is a retrieval hard filter at launch, becoming ranking weight w2 once a city softens. Behavioral inference typically needs general privacy-policy disclosure (flag to todos #4 / legal). Deepak flags: retrieval-before-ranking, logging pipeline, low-history indicator, featured flag for Sunday Deck, shared scoring function across surfaces, keyword-extraction step, internal-keyword storage + admin view, live viewport query. Relates to DEC-019, DEC-023, DEC-005, DEC-003, DEC-006. Source: `workspaces/elvis/recommendation-algorithm-2026-08-25.md`.

### DEC-021: Recurring events (build target phase 1.5)
**Date:** 2026-08-25
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** A recurring event is modeled as separate, fully linked Event instances sharing a recurring-group ID (not one multi-date Event object). Edit, delete, and join/interest use a uniform Google-Calendar-style "this occurrence / this and following" choice ("following" relative to the edited occurrence). Occurrences are batch-generated from a host-set pattern plus an end date or count (re-run to extend). Joining "this and all future" is a snapshot of occurrences that exist at that moment, not a standing subscription (members are notified and opt in when a group is extended). Both individual and org hosts can create them. "Series pages" fall out as an instance-embedded list of the other occurrences, with no master hub page.
**Reasoning:** Separate instances keep every per-event decision already made (ratings, QR check-in, media caps, DEC-006 pre-join, org track record) working unchanged and fit DEC-008 (salvage) better than teaching every screen that an Event can mean several things; batch generation covers the real case (a semester-long club meetup) without an iCalendar-style rule engine; the snapshot join respects ongoing consent.
**Impact:** Build targeted for phase 1.5. Deepak flags: a nullable recurring_group_id plus occurrence ordering; a batch-generation tool; an extend-notification hook; one shared "this/following" UI pattern across delete/edit/join; recurring-group membership is distinct from Event Series membership (separate keys). Relates to DEC-022, DEC-008. Source: `workspaces/elvis/recurring-events-2026-08-25.md`.

### DEC-022: Event Series (build target phase 1.5)
**Date:** 2026-08-25
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** An Event Series is a host-created master hub page (cover, title, description, tags) that is not itself joinable but can be liked/shared/discussed, to which the host attaches events over time. It is closer to an Idea than to a recurring event (a hub with attached events, but with a locked add-permission). Curation is self-only (only the host or approved co-hosts attach their own events); an event may belong to multiple series; a private event attached to a public series follows most-restrictive-wins. Approved co-hosts are pulled forward to ship alongside Series.
**Reasoning:** Groups events that share a theme rather than a repeating template (a touring act, a multi-venue weekend); self-curation avoids a separate cross-host consent system and keeps the private-event visibility rule simple; co-hosts is a real prerequisite permission for "who can add events to a series."
**Impact:** Build targeted for phase 1.5, bundled with recurring events and co-hosts. Revises DEC-024 (co-hosts is no longer purely later-phase). Deepak flags: Series membership is a many-to-many join table (distinct from recurring_group_id); per-viewer render-time visibility checks; distinct UI badges for recurring-group vs series membership. Detaching (assumed to only remove the link) to be confirmed. Relates to DEC-021, DEC-024. Source: `workspaces/elvis/event-series-2026-08-25.md`.

### DEC-023: Group dynamics as recommendation factors
**Date:** 2026-08-25
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Who else is attending feeds the recommender via three sub-mechanisms: an avoid signal (if a user consistently rates another user low, events that person attends are down-weighted, not excluded; an explicit block down-weights substantially more but is still not a hard exclusion), look-alike host affinity (parked, needs real scale), and group personality-mix compatibility (a ranking signal only at launch, no host-facing surface). All are ranking inputs, not a separate system.
**Reasoning:** A great event can be a poor experience because of who else is there, so scoring only an event's own attributes misses this (the group-recommender-systems subfield); soft penalties respect that a rating pattern is a signal, not a certainty.
**Impact:** Depends on two features that do not yet exist and are not designed here: a general user-blocking capability and an attendee-level (thumbs up/down) post-event feedback mechanism. Both are real prerequisites, flagged to the HOTSHEET for their own scoping passes, not assumed into existence. Deepak flags: per-user-pair rating/block history checked at ranking time; cached aggregate personality-tag composition per event. Relates to DEC-020, DEC-014, DEC-005. Source: `workspaces/elvis/group-dynamics-2026-08-25.md`.

### DEC-024: Phase triage of undiscussed drafted surfaces
**Date:** 2026-08-24
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Of the drafted surfaces never discussed at the walkthrough, phase 1 gets waitlist auto-promote with a claim window, org ownership transfer, and a public-facing org history/track-record module; later phases get apply-to-join with host questions, Sunday Deck (needs event density), annual (not semester) Wrapped, and P1.2 memories resurfacing. QR check-in was already confirmed required (DEC-014); co-hosts, originally deferred here, are pulled forward to ship with Event Series (DEC-022).
**Reasoning:** The phase-1 items complete mechanics that already exist as core scope (waitlist) or are structurally required for the target market (club officer turnover makes org ownership transfer non-optional); the later items depend on history or density a new account will not have.
**Impact:** Sets phase placement for these surfaces on the scope matrix. Co-host placement is revised by DEC-022. Source: `workspaces/elvis/conflict-review-2026-08-19.md` item 9.

### DEC-025: New-feature scoping batch (12-item intake)
**Date:** 2026-08-25
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** From the 12-item batch, five are scoped for phase 1: event schedule/itinerary (ordered stops reusing the DEC-003 map picker, visibility inherits the event); live stories (a separate ephemeral 24-hour content type, RSVP not check-in to post, poster-chosen audience from four tiers defaulting to most restrictive); Free Now (real-time availability plus location-pinned rooms, rounded location, aggregate-first with identities on reciprocal join, room creation gated on account standing, moderation a required baseline); event icebreakers (phase 1 = a host-authored up-to-3-question read-only game, check-in gated; tag-matching and scavenger game later); tips/guides (contextual info icon plus a static guide, targeted by situation/status not personality, copy written later). The remaining seven (ticketing/fees, gamification/virtual goods, supporters marketplace, event music, ads/promoted listings, mascot/avatars, web version) are grouped into dedicated future threads, not designed now.
**Reasoning:** Contained features are worth locking now; the two higher-risk real-time features (live stories, Free Now) get priority precisely because of their safety profile, grounded in documented failure patterns of comparable location/real-time products; the deferred seven are each their own product pillar.
**Impact:** Populates the scope matrix with phase placements and owners. Open flags (Free Now account-standing threshold/duration/archival/org rooms, live-stories vs the org media cap, event-model multi-day date-range support) go to the HOTSHEET and to Deepak. Relates to DEC-003, DEC-006, DEC-010, DEC-018. Source: `workspaces/elvis/feature-backlog-2026-08-25.md` and the five per-feature files.

### DEC-026: Korea PASS authentication (Korea-specific verification)
**Date:** 2026-08-26
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** For Korean carrier phone numbers, identity is verified via PASS (the common Korean carrier real-name authentication, government-linked, which returns success/fail plus identity and age); non-Korean numbers continue on the standard phone OTP path (Twilio-style) per DEC-011. A freelancer may be engaged for the Korea-specific integration.
**Reasoning:** Korean carrier numbers are government-linked, so PASS is the common, expected verification method in Korea and returns verified age/identity that a self-declared birthdate does not; it also tends to be cheaper than SMS OTP in-region. Detecting a Korean number and routing to PASS keeps one global flow with a Korea branch.
**Impact:** Adds a Korea-market verification branch to auth. Extends DEC-011 (a provider that can satisfy verification, Korea-only). Refines DEC-012 for Korea: Korean users get verified age via PASS rather than self-declared birthdate, strengthening the age gate for that market (PIPA and CI/DI data-handling implications; see the compliance register). Non-Korea markets unchanged. Deepak to research PASS. Directional per Elvis ("we'll probably adopt that"); confirm before build. Source: 2026-08-26 team sync; `workspaces/elvis/internationalization-korea-2026-08-26.md`.

### DEC-027: Localization and Korean language
**Date:** 2026-08-26
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** The app detects the device language on launch and serves the Korean-language version to Korean-language devices, with the user able to switch language manually.
**Reasoning:** Korea is a focus launch market; a Korean-language experience is expected there, and device-language detection with a manual override is the standard localization pattern.
**Impact:** Adds internationalization (i18n) as phase-1 scope: string externalization, a Korean locale, and a language switcher. Flag for Deepak on the i18n framework and for Elvis on Korean copy. Source: 2026-08-26 team sync; `workspaces/elvis/internationalization-korea-2026-08-26.md`.

### DEC-028: A/B testing and experimentation framework
**Date:** 2026-08-26
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Build an A/B experimentation capability early: assign users to buckets (group A vs group B), ship a change to one group, and measure the effect, applied to design, usability, and algorithm changes. Exact phase is set by build difficulty, targeted as early as feasible.
**Reasoning:** As a startup the post-launch goal is to learn fast what works; embedding experimentation early (rather than retrofitting it) lets design, usability, and recommendation changes be measured against a control instead of guessed.
**Impact:** Adds an experimentation/bucketing layer and event instrumentation, complementing the day-one interaction logging in DEC-020. Phase-1 candidate, unconfirmed pending a build-difficulty assessment (Deepak); tracked as proposed on the scope matrix until phase is confirmed. Source: 2026-08-26 team sync.
