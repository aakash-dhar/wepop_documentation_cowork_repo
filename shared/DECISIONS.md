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

**Change history:** 2026-08-31 - amended (DEC-045): the star scale is 1 to 5, not 0 to 5, and an unrated field is NULL rather than 0. Eligibility for the flow is joined plus event completed (DEC-034 as corrected by DEC-045), no longer checked-in.

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

**Change history:** 2026-08-28 - refined (DEC-031): input reuses the DEC-003 map picker at neighborhood-scale granularity (not a typed city field), reverse-geocoded to a canonical neighborhood ID with the precise tapped point discarded and never persisted; post-onboarding edits are current-location (GPS) only; the stored value is a default anchor, with live GPS preferred when granted and never persisted.

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

**Change history:** 2026-08-28 - extended (DEC-032, DEC-033): an Explore cross-country content-detail gate was added as an individual-premium lift (reviewed by the financials owner and cleared against the paid ranking/discovery-boost lockout as differing in kind, since it never touches ranking within a user's own market); apply-to-join screening-question quota set at 3 free / 10 individual-paid.

**Decision:** Two premium tiers on separate timelines: an individual tier at $3.99/month or $36/year (30s video, 20 media items per moment, own-content engagement analytics) whose ship timing is HELD until phase-1 usage data exists, and an organization tier at $19.99/month or $199/year (per-organization billing, 7-day trial) proceeding now, split so per-event operational numbers stay free and aggregate rollups/trends/export are paid. Gating follows a three-bucket rule (never gate marketplace actions, quota-gate personal expression, insight-gate analytics). Paid ranking/discovery boost is explicitly locked out. Attendee media caps are 10 free / 20 individual-paid / 50 at org-paid events (most-generous-wins). Media retention is 12 months. Price against realistic usage with a manual safety valve for extreme-usage orgs.
**Reasoning:** Willingness to pay differs by roughly an order of magnitude between a casual individual host and an org that needs data to justify budget; a paid boost would cut against the fairness/anti-stalking moat; retention (not the sticker price) is the real cost lever, grounded in a Cloudflare R2/AWS cost model.
**Impact:** Establishes Wepop's commercial structure (PROJECT_STRATEGY.md "Commercial structure" was marked to-fill). Infra recommendation flagged to Deepak (R2 over S3+CloudFront, self-hosted 720p transcode over Cloudflare Stream). Grandfathering left open. GOVERNANCE: financials-owner (Aakash) territory and CLAUDE.md section 6 defines no proposed-project-strategy channel; the corresponding PROJECT_STRATEGY.md commercial-structure rewrite is deferred until that channel is defined. Relates to DEC-010, DEC-015. Source: `workspaces/elvis/freemium-model-2026-08-19.md`.

### DEC-019: Community segmentation (cohorts)
**Date:** 2026-08-25
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Change history:** 2026-08-26 - refined (2026-08-26 team sync): content from users you follow is exempt from the launch cohort hard retrieval filter and is instead surfaced/ranked via social proximity, rather than excluded for being in a different cohort. Deepak: the retrieval query unions the cohort set with content from followed users.

**Change history:** 2026-08-28 - revised (DEC-030): cohort key simplified from `(city, age/life-stage bucket)` to a single binary value (university-affiliated or not); location removed from the cohort formula; the per-city manual density review becomes one global call. Deepak: hold any per-city density-review interface work built against the old per-city shape.

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

**Change history:** 2026-08-28 - refined (DEC-029): language is a synced profile field with a first-launch detection cascade (device language, then app/store region, then phone number) and a manual override that always wins; notifications (push, SMS, email) follow this field; WePop-authored strings ship fully bilingual while user-generated content renders as authored (on-demand translation deferred).

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

### DEC-029: Language preference storage, detection cascade, and i18n scope split
**Date:** 2026-08-26
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Language is a synced profile field, not a device-only setting. Its initial value comes from a first-launch fallback cascade (device language setting, then app/Play Store region if that is unavailable or ambiguous, then phone number as a last resort), mirroring DEC-012's age/country cascade shape; a manual override in profile settings always wins. Notifications (push, SMS, email) read this same profile field rather than the device/OS locale independently. Scope is split explicitly: every WePop-authored string ships fully bilingual selected by this field, while user-generated content (event titles/descriptions, moment captions, chat) renders as authored with no translation pipeline at launch (on-demand UGC translation deferred to a later phase).
**Reasoning:** DEC-027 set device-detection-plus-manual-switch but did not set the storage model, the initial-detection order, or notification behavior. A synced profile field avoids a lost-language-setting complaint on a new device or reinstall, and reusing the DEC-012 cascade keeps one pattern rather than inventing a second. Splitting WePop-copy from UGC scope stops the i18n requirement from silently expanding into content translation, which was deliberately deferred.
**Impact:** Adds a profile-level language field and a first-launch cascade to auth/onboarding alongside DEC-012's cascade; the notification pipeline reads the field rather than inferring locale independently. Refines DEC-027 (does not change its core detect-plus-switch design). Relates to DEC-027, DEC-012. Source: `workspaces/elvis/internationalization-korea-2026-08-26.md`.
**Change history:** 2026-09-02 - the two items previously flagged "Open, not resolved here" were stale; both are resolved in the source file. Full bilingual coverage is committed at launch, so there is no missing-string fallback to decide, and the language field is a one-time read at account setup, not re-checked as device signals change, matching DEC-012. Reconciled by the merger. Source: `workspaces/elvis/internationalization-korea-2026-08-26.md`.

### DEC-030: Cohort formula simplified to student-vs-not (location removed)
**Date:** 2026-08-27
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** DEC-019's cohort key changes from `(city, age/life-stage bucket)` to a single binary value, university-affiliated or not, computed the same way everywhere rather than per-location. Location is removed from the cohort formula entirely. DEC-020's retrieval-stage geographic relevance (a distance radius for the home feed, the live map viewport for Explore) is unaffected and was never a city hard-match to begin with.
**Reasoning:** Elvis's design call while reviewing the home-location-at-registration flow: in practice the phase-1 cohort does its real work on the student/not-student split, not the geographic one. DEC-019's cold-start reasoning (a college student and a 40-something joining the same city should not be pooled with no structure) was protecting against the age/life-stage collision specifically; location riding along in the same key was never the load-bearing part.
**Impact:** DEC-019's per-city manual density review loses its per-location dimension along with location leaving the formula; that review becomes a single global call instead of a city-by-city PM decision. Simpler to own, at the cost of the ability to soften the filter in one dense city ahead of others. The retrieval-filter mechanism, the university three-signal check (self-declared, school email domain, Org membership), and DEC-020's radius/viewport geographic relevance are all unchanged in mechanism. Deepak hold: if any per-city density-review interface work has started against the old per-city shape, hold it pending this change. Revises DEC-019; interacts with DEC-020 and DEC-031. Source: `workspaces/elvis/city-location-registration-2026-08-27.md`.

### DEC-031: Home-location input mechanism, neighborhood granularity, and mutability
**Date:** 2026-08-27
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Four changes to DEC-016, which set policy only (required, city-level, no forced GPS). (1) Input reuses the DEC-003 event-location map picker (search plus tap), not a typed/autocomplete city field, unrestricted (anywhere in the world) at onboarding only. (2) Granularity is revised down from city to neighborhood-scale (roughly dong-level in Korea, a neighborhood/postal-code-sized area elsewhere, comparable to a US zip code); the confirmed map point is reverse-geocoded to a canonical neighborhood ID, that area's centroid, and its country code, and the precise tapped coordinate is discarded and never persisted (consistent with DEC-006/DEC-017 anti-stalking), with a fallback chain (neighborhood, then postal code, then city) for markets without a clean neighborhood tier. (3) After onboarding, home location can only be updated by granting device location permission and selecting current location (a live GPS read that becomes the new stored value through the same reverse-geocode-and-discard flow); the unrestricted picker does not reopen for a later edit. There is deliberately no fallback for a user who never grants location permission (Elvis's explicit call against a support-ticket path); that user has no way to update their home location. (4) The stored home location is only the default anchor for home feed and Explore: when device GPS permission is granted, live current location is used instead, pulled on-demand per screen load (not continuous background tracking) and never persisted, with a manual refresh action on the home feed.
**Reasoning:** Reusing DEC-003's picker avoids building a second location-selection UI. City-level granularity was revised to neighborhood after Elvis caught that a city-wide bucket would starve DEC-020's `geo_distance` ranking of real precision. Restricting post-onboarding edits to a GPS-confirmed current-location read (rather than reopening the free picker) is deliberate anti-gaming design: it closes the loophole where a user could otherwise defeat the country-based Explore gate (DEC-032) by dropping a pin wherever they want free access. Preferring live GPS over the stored default when granted exercises DEC-016's contextual-permission path; keeping the GPS read ephemeral keeps this consistent with why the stored default was deliberately kept coarse.
**Impact:** Location input needs a canonical neighborhood-level ID, centroid, and country code underneath the display string, which becomes the anchor for DEC-020's retrieval radius and `geo_distance` ranking (a gap DEC-020 did not specify before). A geocoding fallback chain is needed for markets without a clean neighborhood tier. Every home-feed or Explore retrieval call now needs request-time anchor resolution (live GPS if granted, else stored default) plus a fallback for GPS read failures so a feed load never hard-fails on a location error. Open, not resolved here: whether Explore needs its own manual refresh distinct from the home feed's, and whether a GPS-granted user can opt back into the coarser stored default. Refines DEC-016; reuses DEC-003; interacts with DEC-030 and DEC-032. Source: `workspaces/elvis/city-location-registration-2026-08-27.md`.

### DEC-032: Explore content gated by country, individual-premium lift
**Date:** 2026-08-27
**Participants:** Elvis (design), Aakash (financials owner)
**Status:** ACTIVE

**Decision:** Explore's map and search stay fully unrestricted for everyone (no gating on panning or searching anywhere in the world). What is gated is content detail: for a free user, events in a country other than their current-location country (live GPS if granted, else the stored home-location default per DEC-031) render as an aggregate teaser only (a clustered count with no pin-level or listing detail); events in the same country as current location render in full. Individual-tier premium (DEC-018) lifts this gate entirely. Stated use case: browsing another country's events before a trip there.
**Reasoning:** Reuses the "aggregate visible, individual detail gated" pattern from DEC-006/DEC-017 rather than inventing a new mechanic. Gating content detail rather than the map interaction itself avoids the map reading as broken. Country-level (not a distance radius) matches the trip-planning use case and avoids per-market boundary-data inconsistency. The gate compares against current location, so a GPS-confirmed user physically present in another country sees it in full; the flip side (a traveling free user loses full access to home-country content unless they disable GPS) is a deliberate, examined consequence of that single rule. Governance: DEC-018 explicitly locks out paid ranking/discovery boost; this gate was reviewed against that rule and cleared by the financials owner (Aakash) as differing in kind, since it never touches ranking or visibility within a user's own market, only access to a non-competing market they do not live in.
**Impact:** Requires a distinct country field separate from DEC-012's locked legal-compliance country (different purpose, different mutability, must not be conflated in the data model). Server-side enforcement is the actual gate; the client map is never the authority. Depends on DEC-031's mutability restriction (current-location-only post-onboarding edits) to prevent a free user from defeating the gate by re-picking a foreign home location. Extends DEC-018; distinct from DEC-012; interacts with DEC-031. Source: `workspaces/elvis/city-location-registration-2026-08-27.md`.

### DEC-033: Apply-to-join screening question quota by tier
**Date:** 2026-08-27
**Participants:** Elvis (design), Aakash (financials owner)
**Status:** ACTIVE

**Decision:** A host using apply-to-join can write up to 3 screening questions for free; individual-tier premium (DEC-018) raises that to 10.
**Reasoning:** Matches the tier-scaling shape DEC-018 set for Moments (10 free / 20 individual-paid / 50 org-paid media items), a quota that scales with tier rather than a feature blocked outright for free users. A full free-tier block was considered and rejected: apply-to-join questions are how a host screens who gets into their event, and blocking that outright for free hosts edges toward gating a marketplace-adjacent capability (screening/curation), which DEC-018's own three-bucket rule prohibits. A small free quota keeps the capability available to everyone; more questions for finer screening is a difference of degree, in the quota-gate bucket DEC-018 already permits.
**Reasoning cont.:** Exact numbers (3, 10) are a starting point, not data-backed, the same caveat DEC-018's own media caps carried at first.
**Impact:** Needs a tier-check on question count at event creation/edit for apply-to-join hosts. Depends on apply-to-join itself, which DEC-024 placed in a later phase and whose phase-1.5 placement and design proposal is still unmerged; this quota rides along with that feature's own merger rather than needing separate build sequencing. Extends DEC-018; depends on the (still unmerged) apply-to-join placement. Source: `workspaces/elvis/paid-tier-features-2026-08-27.md`.

### DEC-034: Peer feedback positive-only, no bulk-follow, check-in decoupled to a badge plus a scoring weight
**Date:** 2026-08-29
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Change history:** 2026-08-31 - partially superseded (DEC-045): the verification badge and the 1.0/0.4 scoring weight are withdrawn in full, the public-average display gate becomes 3 ratings (not 3 verified) with unweighted Bayesian smoothing, and stars run 1 to 5 with unrated stored as NULL. The merge and Elvis's same-day revision crossed (merged 15:02, revised 18:52); nobody's error. The positive-only peer tap, the bulk-follow removal, and the decoupling of check-in from feedback and Moment eligibility stand.

**Decision:** DEC-014's 0-5 star ratings on events and hosts are retained exactly as merged, including the optional anonymous text and its everyone/host-only visibility toggle, and their feed into host reputation. Three amendments. (1) Attendee-to-attendee thumbs up/down is replaced by a single positive-only tap; no negative peer record is created anywhere, and no negative peer table exists in the schema. (2) The "follow all" affordance is removed; individual follow taps only, nothing pre-selected. (3) Check-in is no longer a gate on feedback or on Moment authorship. A user who joined an event that completed may do both. Check-in instead grants a visible verification badge (on Moments per the existing 참석 인증 badge, and now also on feedback) and an invisible scoring weight: verified feedback is weighted 1.0, unverified feedback (joined and completed but never checked in, or self-attested and unresolved at the 7-day auto-close) is weighted 0.4. A host or org public star average does not display until at least 3 verified ratings exist, showing event count and rating count only below that threshold. The internal recommendation signal reads the same weighted rows through a Bayesian smoothing toward the global mean, R = (C·m + Σwᵢrᵢ) / (C + Σwᵢ) with C = 5.
**Reasoning:** Bulk-follow destroys follow as a recommendation signal, which DEC-020 weights as social proximity (w6); a one-tap bulk action makes that weight meaningless. Removing thumbs-down reflects Elvis's stated principle that the product should focus on what to recommend rather than what not to recommend. Decoupling check-in removes it as a single point of failure for the entire evergreen content layer: a host who forgets to run check-in should cost their attendees a badge, not their memories. The weights exist because decoupling reintroduces a real integrity risk that DEC-014's hard gate was quietly handling, namely that a user who RSVP'd and never attended can now rate. At 0.4 it takes two and a half unverified ratings to outweigh one verified one: unverified feedback genuinely counts, which it must since launch check-in rates will be low, but a cluster of no-shows cannot move a host's score against the people who turned up. The minimum-verified display gate has direct precedent in DEC-018's min-sample gating for org analytics. The smoothing constant protects DEC-020's deliberate new-host fairness boost, which a single early 2-star rating would otherwise undo immediately.
**Impact:** Supersedes DEC-014's attendee thumbs up/down provision and its "QR check-in becomes REQUIRED" impact clause. QR check-in remains phase-1 scope but is no longer load-bearing for feedback, ratings, or recommendations; the scope-matrix row's "Load-bearing for ratings, reputation, recommendations, moments" note needs correcting. DEC-023's avoid signal loses its data source as a direct consequence, handled in DEC-036. Deepak flags: store `method` and `verified_at` on the feedback row, mirroring the attendance schema; compute the weight at read time from a config table rather than baking 0.4 into a materialized aggregate, so retuning is a config change rather than a backfill. A verification badge on anonymous feedback discloses attendance status and not identity, so it coexists with DEC-014's anonymity option. The weights (1.0 / 0.4), the display threshold (3), and the smoothing constant (C = 5) are starting points and not data-backed; revisit once real usage exists.
**Relates to / Supersedes:** Amends DEC-014. Interacts with DEC-020 (social-proximity weight and new-host boost) and DEC-018 (min-sample precedent). Forces DEC-036. Source: `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` items A and B.

### DEC-035: Gender removed from the attendee-facing pre-join aggregate; host aggregate retained
**Date:** 2026-08-29
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Gender is not shown to attendees pre-join in any form, including the aggregate ratio DEC-017 established. Hosts continue to see an aggregate on the event details page and in analytics. Gender never appears on a per-person row in any accept/decline or selection UI. DEC-017's separate provision on individual attendee photos is untouched: photos remain visible pre-join only between two users who mutually follow each other in both directions, and a one-way follow never unlocks them.
**Reasoning:** An aggregate ratio on a small event is re-identifiable in practice, which DEC-017's original reasoning did not weigh. The per-row prohibition addresses a different and sharper problem: the same data that informs planning becomes a selection mechanism when it sits inside an accept/decline UI at the moment a yes/no is made about a specific person, and it recreates on the supply side exactly the sorting DEC-006 and DEC-017 exist to prevent on the demand side, with the added harm of silent rejection with no feedback and no recourse. Hosts with a genuine balance requirement declare it at creation and it is enforced at join eligibility, so nobody applies and is quietly rejected.
**Impact:** Partially supersedes DEC-017 (the gender-aggregate provision only; the photo provision stands). Extends DEC-006. Introduces a new invariant I-13: gender is never displayed on a per-person row in any accept/decline or selection UI. Deepak flag: the pre-join aggregate composition payload drops its gender field for attendee-facing requests but retains it for host-facing ones, so this is a per-audience response shape rather than a stored-data change. Gender remains optional at signup and purpose-limited to host aggregate planning, a stated-purpose requirement under PIPA already flagged as legal register L-2.
**Relates to / Supersedes:** Partially supersedes DEC-017. Extends DEC-006. Source: `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item C.

### DEC-036: Avoid signal becomes block-only; positive affinity added as the constructive half
**Date:** 2026-08-29
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** DEC-023's avoid signal runs solely off an explicit block. The soft, inferred half ("if a user consistently rates another user low, down-weight events that person attends") is dropped rather than deferred, since the thumbs-down mechanism it depended on is being removed. Running it instead on the absence of a positive signal was considered and explicitly rejected. In its place, the positive peer tap feeds a positive affinity ranking signal: events attended by people this user has tapped "또 만나고 싶어요" on are boosted, sitting alongside DEC-020's existing social-proximity weight.
**Reasoning:** Elvis's stated principle, recorded because it is general: it matters more to focus on what to recommend than on what not to recommend. Absence-of-positive is also technically fragile as a proxy, since most attendee pairs at most events will never exchange an optional low-uptake tap, so absence is overwhelmingly noise rather than signal. Recording the rejection matters because absence-of-positive is the obvious repair a future reader will propose; it was examined and declined, not overlooked. Flipping the polarity means DEC-023 does not lose its attendee-level data source, it gains a usable one.
**Impact:** Amends DEC-023. Closes DEC-023's flagged dependency on an undesigned attendee-level feedback mechanism, in the positive direction only. Its other flagged dependency, a general user-blocking capability, is closed by DEC-037. Look-alike host affinity stays parked as DEC-023 already had it. Deepak flags: no per-user-pair negative rating history is needed or stored; block state and positive-tap history are the only per-pair reads at ranking time.
**Relates to / Supersedes:** Amends DEC-023. Consequence of DEC-034. Interacts with DEC-020. Source: `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item F.

### DEC-037: General user blocking confirmed as a phase-1 safety baseline
**Date:** 2026-08-29
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** General user blocking is phase-1 scope, in the earliest build wave. A block is bidirectional and total: the blocked user's events, ideas, Moments, comments, and profile are mutually invisible across every surface, including home feed, Explore, and comment threads. The scope of the block is stated to the user at the moment they block, rather than left to be discovered.
**Reasoning:** The scope matrix already flagged this as "likely a phase-1 safety baseline, confirm," and DEC-023 depends on it existing. Bidirectionality is the same reasoning DEC-017 used for mutual follows: a one-directional block leaves the blocking user visible to the person they blocked, which inverts the protection. Stating the scope at block time is required because a user who believes a block is broader than it is will make safety decisions on a false premise.
**Impact:** Moves the scope-matrix row "General user-blocking capability" from later/proposed to phase 1, and resolves the corresponding entry in the matrix's "Unbacked / needs a decision" section. Closes one of DEC-023's two flagged prerequisites. Deepak flags: block state is checked at retrieval time on every content-bearing surface rather than filtered at render, and block is a hard exclusion here even though DEC-023 treats it as a heavy ranking penalty for the avoid signal; those are two different consumers of the same state and both are intended.
**Relates to / Supersedes:** Resolves a scope-matrix open question. Prerequisite for DEC-023 (via DEC-036). Source: `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item G.

### DEC-038: Event cover media caps, a surface distinct from Moment media
**Date:** 2026-08-29
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** DEC-015's and DEC-018's Moment media caps stand unchanged (10 items free / 20 individual-paid / 50 at org-paid events, most-generous-wins, video 15s free and 30s paid, 720p H.264). Event cover media is a separate surface with its own caps: up to 5 items total, photos and videos in any mix, with video capped at 15s for free accounts and 30s for paid accounts of either type, individual or organization.
**Reasoning:** The 15s-free / 30s-paid split matches the split DEC-018 already established for Moment video, so one rule governs both surfaces rather than two. A 5-item cover is a cover, not a gallery; the Moment composer remains the place volume belongs, which keeps the single-uploader and single-moderation-queue architecture intact.
**Impact:** Adds a scope-matrix row for event cover media, which has no home today. Deepak flag: the per-clip technical ceiling of 50MB is compatible with these caps (30s at 720p and roughly 3 Mbps is about 11MB) and functions as an abuse and corruption guard rather than a product limit; client-side compression before upload is mandatory rather than an optimization.
**Open, not decided here:** whether to add a total-video-duration cap per Moment (the handoff spec recommends one; suggested starting values 150s free / 300s paid, examined but not confirmed by Elvis), and the org-paid Moment video length, which DEC-018 never set (recommendation is 30s for most-generous-wins consistency, not decided). A proposed app-wide cut to 5-10s free / 20s paid clip caps was reviewed on cost grounds and rejected; 15s stays the floor.
**Relates to / Supersedes:** Extends DEC-015 and DEC-018 rather than superseding either. Source: `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item E.

### DEC-039: Media retention becomes a tiered paid differentiator, active at launch
**Date:** 2026-08-29
**Participants:** Elvis (design), Aakash (financials owner)
**Status:** ACTIVE

**Decision:** DEC-018's flat "media retention is 12 months" becomes a tiered policy that is active at launch rather than deferred. Nothing is ever deleted. Past the retention boundary, free-tier media moves to cheaper storage and the user sees a thumbnail plus a download of the original; paid accounts, individual and organization, keep full-resolution access indefinitely. Two advance warnings (T-14 days and T-3 days) precede any tier change, each carrying a bulk-download affordance; silent degradation is not acceptable. Thumbnails persist indefinitely at roughly 400px longest edge so no conversation develops holes. The preservation path is device download and explicitly not copy-to-Moment. `storage_tier` and `expires_at` ship on the media row with a scheduled job. The retention threshold is 6 months, between the handoff spec's 90 days and DEC-018's 12 months: it covers the semester a memory was made in plus the break after it, and roughly halves the steady-state storage assumption behind DEC-018's pricing. Retrospective surfaces (annual Wrapped, and P1.2 memories resurfacing) restore their selected items from cold storage and serve them at full quality.
**Reasoning:** Elvis's stated goal is that retention create real value for paid individual and paid org accounts, which DEC-018's flat everyone-archives model does not and the tiered model does. Turning it on at launch rather than shipping unlimited retention and revisiting later avoids setting an expectation that is expensive to walk back and avoids unbounded storage growth against a price that was never modeled for it.
**Impact:** Revises DEC-018's retention provision. Financials (Aakash): this moves the cost math favorably, since DEC-018's $6.15 realistic and $24.60 extreme monthly org figures assumed 12 months of full-resolution media held online for everyone; under this policy free-tier media leaves hot storage at the boundary while paid-tier media stays hot indefinitely, so net effect depends on the paid/free mix within an org. The bounded shape DEC-018 priced against is preserved; worth a re-check of the DEC-018 org cost model before ship. Deepak flag: cold-storage retrieval has real latency and needs a designed loading state.
**Open, not decided here:** three implementation refinements recommended but not yet confirmed by Elvis (build the Wrapped full-quality path as restore-from-cold rather than exemption-from-demotion; build it once as a general "retrospective surface requests full quality" capability so P1.2 memories resurfacing reuses it; introduce a mid-resolution ~1080px tier as what free users see full-screen past the boundary rather than the ~400px thumbnail). Also open: whether retention scope is per-uploader or per-room (handoff open item O-3); nothing at launch depends on it.
**Relates to / Supersedes:** Revises DEC-018. Interacts with DEC-024 (Wrapped, memories resurfacing). Source: `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item D.

### DEC-040: Ideas lifecycle: pause new joins, auto-archive on inactivity, deletion, detachment, tombstone
**Date:** 2026-08-30
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Ideas gain a defined lifecycle, which they did not previously have (the handoff spec's §3 status machine covers Events only). Five parts. (1) DEC-009's "close to new joiners" toggle is confirmed as a membership freeze, not a shutdown: the existing group keeps full access and only new joins stop. It is reversible, is renamed "Pause new joins" (state "New joins paused", outsider-facing "This idea isn't taking new people right now"), and ships visible and usable in phase 1, superseding DEC-009's "do not expose" provision. (2) An idea with no activity for 90 days is archived automatically by the system: visible, read-only, with links and spawned-event backlinks surviving. Activity means another user's Interested tap, a Discussion comment, or a spawned event; views do not count. There is no reason string on an idea archive, correcting handoff spec §10, because reasons belong to Events (cancellation, where §3.2 already requires a written non-empty reason). (3) A creator may delete an idea outright only while no one else has interacted with it, using that same interaction test; the motivating case is created-by-mistake, so this path is friction-free and needs no review routing. (4) Once interaction exists the idea cannot be deleted, but the creator may detach themselves; a detached idea becomes system-owned in phase 1, actionable only by admins. (5) An idea removed by moderation leaves its inspired events standing where those events are themselves fine, with the backlink replaced by an "Idea removed" tombstone. Spawning an event never archives or closes an idea.
**Reasoning:** Elvis's framing is that an Idea is closer to a subreddit than to a post: it gathers conversation around a topic and has a life of its own beyond its creator. The two-mechanic split (pause vs archive) is grounded in the 2026-08-17 walkthrough, where the toggle's purpose was protective of an active conversation rather than an ending of it. "Pause" was chosen over "Close" and "Lock" because reversibility is the semantic that separates it from archive; "Lock" was rejected as misleading. 90 days rather than the events' 60 because ideas are slower-burning by design. Views are excluded from the interaction test deliberately, so a single passive viewer cannot permanently block a creator from deleting their own mistyped draft. Detached ideas become system-owned rather than transferring ownership, because handing an idea to a user who never asked for it is worse than having no owner.
**Impact:** Gives Ideas their first defined lifecycle and closes a real accumulation gap. Deepak flags: one tombstone mechanism should serve both the deleted-event anchor on Moments (§3.5) and the deleted-idea backlink; ideas need `archived_at` plus a last-activity timestamp and an inert scheduled sweep, shipped now so retuning the threshold is a config change; the interaction test is one shared predicate used by both delete-eligibility and archive-activity; a system-owned idea needs a real ownerless state, not a null creator every read path defends against. Records the deliberate distinction from an Event Series (DEC-022): both are hubs with events attached over time; the difference is permission, a Series has a locked add-permission while an Idea is open to anyone inspired.
**Open, not decided here:** whether an archived idea can be un-archived; whether a detached idea can regain an owner; whether archived ideas surface in Explore or only by direct link; whether interested users are notified when an idea is paused or archived; a host-initiated early archive is deliberately not included, cheap to add later.
**Relates to / Supersedes:** Supersedes DEC-009's surviving "do not expose" idea provision, closing phase-1/1.5 review item #7. Corrects handoff spec §10. Relates to DEC-022 and the §3.5 tombstone pattern. Source: `workspaces/elvis/ideas-lifecycle-2026-08-30.md`.

### DEC-041: Event schedule: multi-day confirmed, schedule allowed pre-confirmation, recurring propagation
**Date:** 2026-08-30
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Three resolutions completing the event schedule design. (1) The multi-day dependency flagged 2026-08-25 is closed: the Event model does support a start and end date that differ. The handoff spec ships `scheduled_end` on the Event row as "ship now" and states multi-day events are covered, and Elvis confirms the creation flow exposes it as an Airbnb-style calendar picker where a single day and a range are the same interaction. (2) A host may build a schedule on an event whose date or time is still unresolved (`planning` status, under poll); stops carry their times and bind to the date on confirmation. (3) Recurring events copy the full itinerary at batch generation with dates shifted per occurrence, a host may edit a single occurrence's itinerary, and the schedule participates in DEC-021's "this occurrence / this and following" choice rather than being copied once and left as independent rows.
**Reasoning:** On (1), nothing in DEC-001 through DEC-009 had established that an Event could span calendar days, so the 2026-08-25 design's multi-day branch was resting on an unverified assumption; two independent confirmations now close it. On (2), sketching the shape of a day is what a host does while rallying people; blocking the itinerary until a date poll resolves would make Plan Mode feel half-built for no protective benefit. On (3), copy-at-generation and propagate-on-edit look like one feature and are two, which is why it is stated explicitly.
**Impact:** Clears the scope-matrix note "multi-day depends on Event date-range (Deepak to confirm)" on the event schedule row. Deepak flags: the schedule must be part of the same this/following propagation path DEC-021 already requires for edit, delete, and join. Recommended and not yet confirmed by Elvis: store an explicit date on every stop including single-day events and derive the display rather than the storage, because §3.4 permits a host to extend a Live event at any time and an extension crossing midnight retroactively turns a single-day event into a two-day one; one column removes the class of bug. Elvis's calendar-picker design has not landed yet and this should be revisited against it.
**Relates to / Supersedes:** Refines DEC-025's event schedule provision. Depends on DEC-021 (recurring) and DEC-003 (map picker), both unchanged. Source: `workspaces/elvis/event-schedule-2026-08-25.md` (2026-08-30 update).

### DEC-042: Change notifications on events and ideas: what notifies, where it lands, who receives it
**Date:** 2026-08-30
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** All changes to an event or an idea generate a notification. Event changes additionally post into the event's chat. Notifications batch per save, so one save produces one notification regardless of how many fields changed. The audience for an event change is three groups: joined attendees, waitlisted users (DEC-024), and users with a pending apply-to-join application (DEC-033). Followers and passive viewers are not notified. Idea changes notify their interested users; whether they also post into the idea's Discussion is deferred to a later phase. Completed events are not editable at all, so no change notifications arise after completion; admin-initiated removal of a completed event still notifies (see DEC-043).
**Reasoning:** The failure mode is concrete: someone who read an itinerary yesterday and is standing at the old meeting point is not refreshing the event page, so a silent change strands them. This satisfies I-14 (consequential actions are never silent) and rides on existing machinery, since §11 already establishes that poll resolution posts an announcement and §7.2's chat is announcement-only by default until T-24h. Per-save batching answers §7.3's warning that notification volume is a launch-level risk. The three-way audience matters because an attendees-only rule would miss the waitlisted user, who can be auto-promoted into an event whose date moved while they were waiting.
**Impact:** Establishes a general rule spanning events, ideas, and every sub-object including schedule stops, rather than leaving each feature to invent its own notification behavior. Deepak flags: notifications batch at the save boundary, not per field; the audience query for an event change unions three membership sets; a completed event must reject detail edits server-side. Interacts with §7.3's notification-grouping requirement.
**Open, not decided here:** whether pausing or archiving an idea counts as a change for notification purposes; both state transitions were designed 2026-08-30 but neither was named explicitly in this rule.
**Relates to / Supersedes:** Extends DEC-025 (event schedule); interacts with DEC-024 (waitlist auto-promote) and DEC-033 (apply-to-join). No supersession. Source: `workspaces/elvis/event-schedule-2026-08-25.md` (2026-08-30 update) and `workspaces/elvis/ideas-lifecycle-2026-08-30.md`.

### DEC-043: Completed events cannot be deleted or left by their host; detachment is a reviewed request
**Date:** 2026-08-30
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** A host may not delete an event once it has completed. After completion, deletion is admin-only and arises from exactly two sources: moderation removal (an event found inappropriate after it ran) and a legal erasure request under PIPA. A host who wants to be unlinked from a completed event may request detachment, which is reviewed by an admin rather than taking effect immediately. Detail edits on a completed event are likewise prohibited. All three restrictions are enforced server-side, not by hiding the affordance. Ratings persist through both detachment and deletion: a detached host keeps the event's ratings on their record, and ratings survive even when the completed event carrying them is itself deleted.
**Reasoning:** Raised by Elvis asking why anyone would want to delete an event after it is over. Following that through found a real hole: handoff spec §3.2 permits `any -> deleted` for "host or admin" without distinguishing them, so a host could delete a completed event and with it that event's ratings, letting a host with a poor rating clean their record. That directly undermines DEC-014's host reputation and DEC-024's public org track-record module, which exists specifically as a cold-start trust signal; a trust signal its subject can selectively delete is not a trust signal. The same principle is already settled elsewhere (an idea creator cannot delete once others have engaged, DEC-040; §12.6 routes host takedown of a Moment to review). Detachment is stricter for events than for ideas because an event host carries ratings, attendance, and a public track record; self-serve detachment would reopen the laundering hole. Routing detachment through review lets an admin distinguish a legitimate request from an attempt to escape a rating history, reusing the §12.6 pattern.
**Impact:** Amends handoff spec §3.2's deletion transition, which must now split by actor: host-initiated deletion permitted only before completion, admin-only after. Detachment on a completed event becomes a request object entering the existing admin/moderation review queue, new scope with no current home on the scope matrix. Deepak flags: enforce the completion boundary server-side for deletion, detachment, and detail edits alike; a host's rating aggregate must not be computed by joining live event rows, since that makes event deletion silently destroy the ratings; ratings carry their own denormalized host reference and survive their source event, reusing the §3.5 pattern (denormalized `event_name`, `event_date`, `org_name` copied at creation). The §3.5 Moment tombstone behavior is unchanged and applies when an admin removes a completed event.
**Relates to / Supersedes:** Amends handoff spec §3.2. Protects DEC-014 (host reputation) and DEC-024 (public org track-record module). Consistent with DEC-040 and §12.6. Three further accountability loopholes (statutory erasure, account deletion and re-registration, disposable org accounts) are resolved in DEC-044. Source: `workspaces/elvis/event-schedule-2026-08-25.md` (2026-08-30 update).

### DEC-044: Host accountability: reputation and enforcement split, ban list, and closing the org loophole
**Date:** 2026-08-30
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Reputation and enforcement are separated as distinct objects with distinct retention. Reputation (host ratings, public track record) is personal data about the host and is deleted with the account. Enforcement (ban and suspension records) is fraud-prevention data and survives account deletion, retained under a disclosed 부정이용 방지 privacy-policy item. This follows Danggeun's model; their 0-1,000 Karrot Score is explicitly not adopted, and DEC-014's 0-5 star ratings stand. Re-registration after account deletion is allowed, subject to a cooldown and a ban-list check at signup. The ban list stores a hashed identifier (phone hash plus device and environment signals) rather than a readable roster, with CI (연계정보) from DEC-026's PASS flow as the strong key for Korean users. On organizations: enforcement propagates, so suspending an individual suspends the orgs they operate; admins can see every org a user operates; org creation is gated on standing (no active suspensions plus a minimum account age) rather than on a rating; and a suspended admin may transfer their admin role to another org member, subject to three qualifications (the target has standing, the target was a member before the suspension with a minimum tenure, and a suspension-triggered transfer is admin-reviewed rather than self-serve). A suspended individual loses org access entirely, not merely the admin title. A cap on org accounts per user and public display of a person's connected profiles were both considered and rejected.
**Reasoning:** The conflict between accountability and PIPA dissolves once reputation and enforcement stop being one object. PIPA Art. 36(1)'s deletion right carries only a narrow proviso (where another law specifies the data as a collection target), which does not reach "we want to keep it for accountability", so retained ratings are not defensible against an erasure request while a disclosed, purpose-limited abuse record is the route Korean platforms actually use. Danggeun demonstrates the pattern in this exact market: 매너온도 dies with the account while suspensions carry over. On the org loophole, the problem was never that multiple orgs exist but that no consequence flowed along the org-to-user traceability the recommendation work already requires; making enforcement propagate closes most of it with no new data model. Standing rather than rating as the creation gate avoids blocking brand-new university club officers, the launch market. The admin transfer exists because a 40-member club should not die for one officer's misconduct, and its three qualifications stop a bad actor planting an accomplice and keeping de facto control. Public profile linking was rejected because it fights DEC-006 and DEC-017 directly and creates a real deanonymization surface.
**Impact:** Establishes the accountability model spanning users, hosts, and orgs. Deepak flags: the ban list is a hashed lookup at signup, not a stored roster; suspension propagation walks the existing traceability link; suspension-triggered admin transfer is a distinct path from DEC-024's routine ownership transfer; a suspended user is removed from org access entirely; the deletion path must distinguish account deletion (ratings deleted) from event deletion (ratings survive, per DEC-043). Legal escalation for DLG via the proposed legal-register consult: whether a disclosed 부정이용 retention item supports a ban list surviving an erasure request and what period is defensible; whether hashing changes the analysis; CI handling obligations if CI becomes the ban-list key. Interacts with legal register L-1 and L-10.
**Open, not decided here:** the re-registration cooldown period (Danggeun uses 7 days); the ban-list retention period; minimum account age for org creation and minimum member tenure for a suspension-triggered transfer; whether suspension propagation is automatic or a per-org reviewer decision; whether an org suspended by propagation is restored automatically on a valid transfer or needs separate reinstatement.
**Relates to / Supersedes:** Extends DEC-024 (org ownership transfer, public track record) and DEC-026 (PASS/CI). Consistent with DEC-014 and with DEC-006/DEC-017. Source: `workspaces/elvis/host-accountability-2026-08-30.md`.

### DEC-045: Check-in badge and scoring weight withdrawn; stars 1 to 5; public average gates at 3 ratings
**Date:** 2026-08-31
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** DEC-034's verification badge and feedback scoring weight are withdrawn in full. Check-in awards no 참석 인증 badge, carries no scoring weight, and gates nothing; it produces an operational record surfaced in analytics only. Anyone who joined an event through the app may give feedback and post a Moment once the event completes; that is the whole eligibility rule. Two protections replace the weighting, neither depending on check-in: a public star average displays once a host has 3 ratings (not 3 verified ratings), showing event count and rating count only below that; and the internal recommendation signal applies Bayesian smoothing toward the global mean, now unweighted, R = (C·m + Σrᵢ) / (C + n) with C = 5. Separately, stars run 1 to 5, not 0 to 5, and an unrated field is NULL rather than 0.
**Reasoning:** DEC-034 landed 2026-08-31 at 15:02 from the proposal as it stood when the merger reviewed it; work later the same day (items #9 and #10 of the phase-1/1.5 review) revised that proposal twice and then withdrew its central mechanism, committed at 18:52 after the merge. Nobody's error; this entry brings the decision log back into agreement with the working file. Three findings undid the weighting. (1) Check-in ceased to be universal (DEC-046): it runs only on ticketed events and on capacity-limited events whose host enables it, so at an open event nobody can be verified and every rating would weight 0.4 permanently, leaving a host who runs only open events with no public star average ever, including an org whose track record is a cold-start trust signal under DEC-024. (2) A three-state fix (verified / unverified / axis-not-applicable) solved that but introduced a perverse incentive: a host who turned check-in on would have some ratings discounted to 0.4 while a host with no check-in had all ratings at full weight, so the host who did more to verify attendance reached the display gate later. (3) The machinery was nearly inert at launch anyway, since ticketing is not live until phase 1.5 (DEC-010) and the individual paid tier is HELD (DEC-018), so it would have served org-tier capacity events and almost nothing else. On the star scale: a 0-star rating is not expressible in a star widget (tapping the first star yields 1, and not tapping is indistinguishable from skipping), DEC-014 makes every field skippable so a distinct sentinel for "did not answer" is required, and a 0 entering the average would count in the denominator and drag the numerator, penalising every host whose attendees skipped feedback.
**Accepted cost:** a user who joined and never attended is now indistinguishable from a real attendee when rating. Judged acceptable because the motive is thin at a free casual meetup, the 3-rating gate stops one person establishing a public number alone, smoothing absorbs a single outlier, and a host can report a rating from someone who was not there, making it a moderation rather than a scoring problem.
**Impact:** Supersedes DEC-034's badge and weighting provisions and its "0 to 5 stars" reading of DEC-014 (DEC-014 carries a matching change-history note). DEC-034's other provisions stand unchanged (positive-only peer tap, no bulk-follow, check-in decoupled from eligibility). Two `wepop-scope-matrix.md` rows need correcting, both currently describing the withdrawn model: the "Ratings + post-event feedback" row (verified 1.0 / unverified 0.4, gate at 3 verified) and the "QR check-in (verification badge + weight)" row, titled for a badge that is not shipping. Deepak flags: no weight column, no badge surfaces, aggregates recomputed from rows rather than accumulated, and `attendance(event_id, user_id, method, verified_at, approved_by)` stays a first-class transactional table so that reinstating weighting later is a config change plus a runnable backfill rather than a rebuild, which is the condition making this a deferral rather than a deletion.
**Relates to / Supersedes:** Supersedes DEC-034 in part; amends DEC-014's star scale. Prerequisite for DEC-046. Interacts with DEC-018 (min-sample precedent) and DEC-020 (new-host boost, which the smoothing protects). Source: `workspaces/elvis/ratings-checkin-2026-08-31.md`.

### DEC-046: Check-in reverses to host-scans-attendee, an operations tool on a defined subset of events; self-service mode deferred
**Date:** 2026-08-31
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Phase 1 follows the ticketing industry standard: the host scans the attendee, reversing handoff spec §4.2, where the host displays a rotating QR that attendees scan. Check-in produces an operational record only: it is recorded and surfaces in analytics, awards no badge, carries no scoring weight, and gates nothing. The 참석 인증 badge is removed and does not ship. Check-in is not universal: required on ticketed events; a host choice on capacity-limited events via a "Check-In Required" toggle shown when capacity is set, available to every host, free and paid; and not available in phase 1 on open events with neither ticketing nor capacity. What is paid is the analytics built on check-in data, not the ability to record it, inside DEC-018's existing split of per-event operational numbers free and aggregate rollups paid. Attendees scanning a displayed QR or typing a numeric code becomes self-service mode, deferred to a later phase, possibly paid. Attendance data is retained deliberately for later use: no-show and punctuality behaviour is tracked from launch, nothing acts on it in phase 1. Attendance is recorded as two independent axes, not one enum. Observed attendance exists only where check-in ran, with four states: attended (host-scanned or self-attested and host-approved), claimed-unconfirmed (self-attested, host never acted before §4.3's 7-day auto-close), no-show (joined, then nothing), and not tracked (the event ran no check-in, a property of the event rather than the person); neither "not tracked" nor "claimed, unconfirmed" may collapse into no-show. Self-reported intent exists on every event including those with no check-in: as the event approaches the attendee receives a notification, an in-app pop-up, and a button on the event detail page offering on my way / running late / cannot make it. Because check-in coverage in phase 1 is narrow while self-report reaches every event, self-report is the primary reliability source at launch and check-in the secondary one. The host check-in timestamp is recorded but is not an arrival time, since a host who batch-scans twenty minutes in makes everyone look late. Design rule attached to the data, holding from day one: declining in advance must not be scored like a silent no-show; the two states stay distinct in the data now or the choice is gone.
**Reasoning:** Staff scanning the attendee is universal in ticketing; the stated operational reason is throughput, the structural reason is enforcement: a gate must be able to deny entry, and denial only works if the venue controls the decision, since an attendee who scans their own phone has already walked in. WePop is committed to paid ticketing (DEC-010, TASK-036), so building the direction that supports enforcement now avoids inverting the whole attendance surface later. Check-in is not universal because a host of an open event may not want the hassle and should not have to. Reducing check-in to an operational record follows: once it is optional and rare, a badge and a scoring weight hanging off it created more problems than they solved (DEC-045), and check-in becomes honestly what it now is, the door at a ticketed event and a headcount at a capacity event. Self-service is deferred because it serves the low-stakes case that no longer needs it. Two problems were being conflated and are now separated: rating integrity (mitigation withdrawn as an accepted cost, DEC-045) and attendee reliability (a behavioural problem, significant in the event space, which the retained attendance data is for).
**Impact:** Corrects the scope-matrix row "QR check-in (required)" on two counts, since check-in is neither required of all events nor load-bearing. Dissolves a governance escalation that was about to be filed: paid-gating check-in brushed against DEC-018's "never gate marketplace actions" rule and I-16, because the attendee could never earn a badge purely because their host did not pay; with no badge there is no degradation and nothing to escalate. Likely de-blocks L-3: the 위치정보법 exposure attaches to the printed-poster mode, whose static token needs a location radius to resist forgery, and printed posters exist to support attendee self-scan; with self-scan deferred, the poster and its geofence defer with it and L-3 becomes a later-phase legal question rather than a gate before P0. Confirm with DLG rather than assuming (TASK-040; HOTSHEET entry kept Blocking until confirmed). Anti-forgery simplifies: once a host scans a person standing in front of them the host's own eyes are the strongest available control, so a static per-attendee credential suffices and the 60-second rotating QR is no longer needed; the handoff's rejection of SafeTix-class rotating attendee credentials still holds. The co-host `run_checkin` permission flag (§8.1) becomes more useful. Deepak flags: `attendance.method` stays an open discriminator (phase 1 adds a host-scan method, deferred self-service adds another later), nothing hard-codes the assumption that the attendee initiates, and an event carries a boolean for whether check-in runs. Naming correction preserved: the deferred mode is self-service, not offline, since it needs every attendee's device online; the genuinely offline-capable path is the ticketing one (host's device caches the roster before doors). Corrects the I-12 drafting error rather than requiring a carve-out: the 2026-08-29 replacement wording widened §13's "visible to anyone" to "whether visible or internal", which was not asked for and contradicts DEC-014's internal-only attendee signal. Reverted to the visibility scope, keeping the host carve-out: I-12 prohibits a persistent peer rating of a participant that is visible to anyone; internal signals are permitted, and making one visible or using it to gate event access is a separate decision requiring its own review. Retained no-show data then needs no exception. For the DLG register: a reliability score is personal data of the same character as L-1's peer affinity records and belongs in the same consult (TASK-040).
**Open, not decided here:** what "surfaces in analytics" means concretely (which surface, per-event or rollup); how and when no-show and punctuality data is eventually used, and whether any of it is surfaced to users; whether the claimed-but-unconfirmed state is visible to the attendee or the host is nudged to resolve the queue before auto-close; self-reported intent detail (individual host notification vs roster view, whether "running late" carries an estimate, attachment to a DEC-025 schedule stop). Documentation gap: self-reported intent exists in Elvis's design files but is defined nowhere in this repo; the work is documenting it, not designing it. Future direction, noted not designed: self-check-in on open events tied to a rewards mechanic (deferred gamification thread, DEC-025); geo-located arrival time, which would need its own privacy pass against DEC-016, DEC-012, and 위치정보법.
**Relates to / Supersedes:** Reverses handoff spec §4.2; reverts the 2026-08-29 I-12 wording to visibility-scoped (TASK-041). Depends on DEC-045. Relates to DEC-010 and TASK-036 (ticketing), DEC-024 (capacity and waitlist). Source: `workspaces/elvis/ratings-checkin-2026-08-31.md`.

### DEC-047: Feedback uniformly anonymous; 7-day edit and withdraw window; author-visible only in the profile
**Date:** 2026-08-31
**Participants:** Elvis (design), Aakash (merger)
**Status:** ACTIVE

**Decision:** Post-event feedback is uniformly anonymous, with no option for a user to attach their name. A user may edit or withdraw their own feedback for 7 days after submitting it, measured from submission rather than from the event; after that, removal goes through moderation. A user can see all feedback they have given via a menu entry in their profile ("My feedback / 내가 남긴 후기") listing what they wrote, which event it was for, and whether the 7-day window is still open, with edit and withdraw living there.
**Reasoning:** Optional attribution would destroy anonymity for the people who used it: if most attendees sign and a few do not, the few are identifiable as the ones with something to hide, which on a ten-person event is close to naming them. It would also create pressure, since a host asking who said what puts everyone in a position where declining reads as hostile. Structurally, anonymity is doing the work that Airbnb needs double-blind simultaneous publication to do; WePop needs none of that machinery because a host cannot identify a rater, and optional attribution trades that away for nothing. The signed channel already exists and is the follow button, which DEC-014 deliberately places on the feedback screen separated from the rating controls. On the window: 7 days from submission rather than from the event, because Airbnb's edit window works only by being tied to a review period that closes, and §5.2 says WePop's feedback window never closes, so the same pattern would mean editable forever. Not indefinite, because ratings feed host reputation and the recommendation engine, so a rating that can change forever means the aggregate never stabilises and opens a coercion vector where a host pressures someone months later to revise a score. 7 days also matches the self-attest auto-resolve window in §4.3, giving the product one "we wait a week" period rather than two competing ones.
**Impact:** Deepak flags, one easy to build wrong first: weighted aggregates must be recomputed from rows rather than accumulated as a running sum, since an incremental aggregate is silently corrupted by the first edit or withdrawal. The "My feedback" screen is the only place the author-to-feedback link ever surfaces to a human: private to that user, never to a host, never in an admin UI that could leak it, never in an export; anonymity is doing structural work here and this linkage is the single point at which it could be undone. The screen slots into the profile three-tab restructure already scheduled in the handoff's P1.1 wave rather than being added separately.
**Open, not decided here:** whether an edited rating shows as edited to viewers or changes silently within the window; where feedback aggregates surface to the host and in what form.
**Relates to / Supersedes:** Extends DEC-014 and DEC-034 as corrected by DEC-045. Source: `workspaces/elvis/ratings-checkin-2026-08-31.md`.
