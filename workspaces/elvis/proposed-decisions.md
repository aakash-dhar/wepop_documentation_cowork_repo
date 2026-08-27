# Proposed decisions from elvis, 2026-08-26 - for merger review

## DEC-NNN (PROPOSED)
**Date:** 2026-08-26
**Proposed by:** Elvis
**Source:** `workspaces/elvis/internationalization-korea-2026-08-26.md`, refining DEC-027 (landed
2026-08-26 from the live team sync)
**Topic:** Language preference storage, detection cascade, and scope
**Type:** Technical
**Decision:** The language setting is a profile field, not a device-only setting, so it syncs across a
user's devices. Its initial value comes from a fallback cascade at first launch: device language setting
first, then app/Play Store region if that signal is unavailable or ambiguous, then phone number as a
last resort, mirroring the shape of DEC-012's own age/country cascade. A manual override in profile
settings always takes precedence over the cascade. Notifications (push, SMS, email) follow this same
profile field rather than the device/OS locale independently. Scope is split explicitly in two: every
WePop-authored string (chrome, system messages, transactional text) ships fully bilingual, selected by
this field; user-generated content (event titles/descriptions, moment captions, chat) renders exactly as
authored with no translation pipeline at launch, on-demand translation deferred to a later phase per the
existing UGC deferral already in DEC-027's source doc.
**Reasoning:** DEC-027 only specified device-detection-plus-manual-switch; it did not specify storage
model, initial-detection fallback order, or whether notifications follow the same setting. A profile
field avoids a real "I lost my language setting" complaint on a new device or reinstall, and reusing the
DEC-012 cascade shape keeps the codebase consistent rather than inventing a second pattern. Splitting
WePop-copy from UGC scope prevents the i18n coverage requirement from silently expanding to content
translation, which was deliberately deferred.
**Impact:** Adds a profile-level language field and a first-launch cascade to the auth/onboarding flow
alongside DEC-012's existing cascade logic. Notification pipeline (push/SMS/email) needs to read this
field rather than infer language independently. Does not change DEC-027's core detect-plus-switch design,
refines its implementation. Still open, not resolved by this proposal: fallback behavior for a
WePop-authored string with no Korean translation yet at ship time (English fallback vs blocking launch on
full coverage), and whether the profile field re-reads device signals after initial set or is captured
once like DEC-012's age value. Both flagged in the source doc for a future pass.
**Relates to / Supersedes:** Refines DEC-027. Reuses the cascade pattern from DEC-012. Does not supersede
either.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-27
**Proposed by:** Elvis
**Source:** `workspaces/elvis/city-location-registration-2026-08-27.md`, revising DEC-019
**Topic:** Cohort formula simplified to student-vs-not, city removed as a cohort dimension
**Type:** Product
**Decision:** DEC-019's cohort key changes from `(city, age/life-stage bucket)` to a single binary value,
university-affiliated or not, computed the same way everywhere rather than per-location. Location is
removed from the cohort formula entirely. Geographic event relevance is unaffected by this change and was
never actually a city hard-match to begin with, DEC-020's retrieval stage already uses a distance radius
(home feed) or the live map viewport (Explore), not a city filter; this proposal just confirms that
mechanism was never part of what DEC-019's cohort was solving for, and gives it a precise anchor point (see
the DEC-016 refinement proposal below).
**Reasoning:** Elvis's direct call, made while reviewing the home-location-at-registration flow: in
practice phase-1 cohort is doing its real work on the student/not-student split, not the geographic one.
DEC-019's own cold-start reasoning (a college student and a 40-something joining the same city) was
protecting against the age/life-stage collision specifically; location riding along in the same key was
never the load-bearing part of that protection.
**Impact:** DEC-019's per-city manual density review (the mechanism that softens cohort from a hard filter
into a ranking signal once a city is confirmed dense enough) loses its per-location dimension along with
location leaving the formula; that review becomes a single global call instead of a city-by-city PM
decision. Simpler to own, at the cost of the ability to soften the filter in one dense city ahead of
others. The retrieval-filter mechanism itself, the university three-signal check (self-declared, school
email domain, org membership), and DEC-020's existing radius/viewport-based geographic relevance are all
unaffected in mechanism, though the latter gains a real anchor point for the first time via the DEC-016
refinement below. Deepak flag: if any per-city density-review interface work has started against the old
per-city shape, hold it pending this merger.
**Relates to / Supersedes:** Revises DEC-019. Interacts with DEC-020 (recommendation architecture, whose
`geo_distance` anchor point this affects) and the new DEC-016 refinement proposal below (where the location
value itself is captured).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-27
**Proposed by:** Elvis
**Source:** `workspaces/elvis/city-location-registration-2026-08-27.md`, refining DEC-016
**Topic:** Home-location input mechanism, neighborhood-level granularity, and mutability
**Type:** Design + Technical
**Decision:** Four changes to DEC-016, which only set policy (required, city-level, no forced GPS) and left
mechanism open. (1) Input reuses the DEC-003 event-location map picker (search plus tap), not a
typed/autocomplete city-name field; unrestricted (anywhere in the world) at onboarding only. (2)
Granularity is revised down from city to neighborhood-scale (roughly dong-level in Korea, or a
neighborhood/postal-code-sized area elsewhere, comparable to a US zip code); city-level proved too coarse
to give DEC-020's `geo_distance` ranking signal real accuracy. The confirmed map point is immediately
reverse-geocoded to a canonical neighborhood ID, that area's centroid, and its country code, and the
precise tapped coordinate is discarded, never persisted, consistent with the anti-stalking stance in
DEC-006/DEC-017; a fallback chain (neighborhood, then postal code, then city) covers markets without a
clean neighborhood geocoding tier. (3) After onboarding, the home location can only be updated by granting
device location permission and selecting current location, a live GPS read that becomes the new stored
value through the same reverse-geocode-and-discard flow; the unrestricted map picker does not reopen for a
later edit. There is deliberately no fallback for a user who never grants location permission, Elvis's
explicit call against my recommendation of a support-ticket path matching DEC-012's pattern; that user has
no way to ever update their home location. (4) The stored home location is only the *default* anchor for
home feed and Explore: when device GPS permission is granted, live current location is used instead, pulled
on-demand per screen load (not continuous background tracking) and never persisted, with a manual refresh
action on the home feed to explicitly re-pull it.
**Reasoning:** Reusing DEC-003's picker avoids building a second location-selection UI. City-level
granularity was revised to neighborhood after Elvis caught that a city-wide bucket would starve
`geo_distance` ranking of real precision. Restricting post-onboarding edits to a GPS-confirmed current-
location read (rather than reopening the free picker) is deliberate anti-gaming design, not just a
mutability choice, it closes the loophole where a user could otherwise defeat the country-based Explore
gate (separate proposal below) by simply dropping a pin wherever they want free access to. Preferring live
GPS over the stored default when granted exercises the contextual-permission path DEC-016 already built (it
names Explore's map as one example value point); keeping the GPS read ephemeral rather than persisted keeps
this consistent with why the stored default itself was deliberately kept coarse in the first place.
**Impact:** Location input needs a canonical neighborhood-level ID, centroid, and country code underneath
the display string, which becomes the anchor point for DEC-020's retrieval radius and `geo_distance`
ranking, a gap that doc never actually specified before this. A geocoding fallback chain is needed for
markets without a clean neighborhood tier. Every home-feed or Explore retrieval call now needs request-time
anchor resolution (live GPS if granted, else stored default) rather than a single cached value, plus a
fallback path for GPS read failures so a feed load never hard-fails on a location error. Note: an earlier
version of this proposal included a separate "browsing city" override; that's retired in favor of the
country-gate proposal below, which covers the same underlying need (previewing somewhere else) without a
redundant second mechanism.
**Not yet decided, flagged for a follow-up pass, not resolved by this proposal:** whether Explore needs its
own manual refresh distinct from the home feed's, and whether a user who granted GPS should still be able
to opt back into the coarser stored default rather than always getting live location.
**Relates to / Supersedes:** Refines DEC-016. Reuses DEC-003. Interacts with the DEC-019 cohort-formula
revision above (the neighborhood value captured here anchors DEC-020's geographic ranking directly) and the
Explore country-gate proposal below (this entry's mutability restriction is load-bearing for that
proposal's integrity).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED, NEEDS AAKASH'S EXPLICIT REVIEW, NOT ROUTINE MERGER)
**Date:** 2026-08-27
**Proposed by:** Elvis
**Source:** `workspaces/elvis/city-location-registration-2026-08-27.md`, extends DEC-018's commercial
structure
**Topic:** Explore content gated by country, individual-premium perk for trip planning
**Type:** Product / Commercial (financials-owner territory per DEC-018's own governance note)
**Decision:** Explore's map and search stay fully unrestricted for everyone, no gating on panning or
searching to anywhere in the world. What's gated is content detail: for a free user, events in a country
other than their current-location country (live GPS if granted, else the stored home-location default,
same signal defined in the DEC-016 refinement above) render as an aggregate teaser only, a clustered count
with no pin-level or listing detail. Events in the same country as current location render in full.
Individual-tier premium (DEC-018) lifts this gate entirely. Stated use case: browsing another country's
events before a trip there.
**Reasoning:** Reuses the existing "aggregate visible, individual detail gated" pattern from DEC-006/DEC-017
rather than inventing a new mechanic. Gating content detail rather than the map interaction itself avoids
the map reading as broken. Country-level, not a distance radius, both matches the actual use case (trip
planning) and avoids per-market boundary-data inconsistency. The gate compares against *current* location,
not a fixed home value, so a user physically present in another country (GPS-confirmed) sees it in full,
they're not previewing, they're there; the flip side, a traveling free user correspondingly loses full
access to home-country content for the duration unless they disable GPS, is a deliberate, examined
consequence of that single rule, not a bug to special-case around.
**Impact:** Requires a distinct, separate country field from DEC-012's locked legal-compliance country
(different purpose, different mutability, must not be conflated in the data model). Server-side enforcement
is the actual gate, the client map is never the authority. Depends on the DEC-016 refinement's mutability
restriction (current-location-only post-onboarding edits) to prevent a free user from trivially defeating
the gate by re-picking a foreign home location.
**Governance flag, not resolved by this proposal:** DEC-018 explicitly states "paid ranking/discovery boost
is explicitly locked out," reasoning that it would cut against the fairness/anti-stalking moat. My own read
is that this proposal differs in kind, DEC-018's concern appears to be same-market competitive fairness
(paid users outranking free users on the same local events), while this gate never touches ranking or
visibility within a user's own market, only access to a non-competing market they don't live in. That
reading is not authoritative. This needs Aakash's explicit sign-off against DEC-018's own rule before it's
treated as a normal awaiting-merger proposal, flagged here rather than silently assumed compatible.
**Relates to / Supersedes:** Extends DEC-018. Interacts with the DEC-016 refinement above (shares the
current-location signal and depends on its mutability restriction) and is explicitly distinct from DEC-012
(must not share a country field or concept).
**Status:** Awaiting Aakash's explicit review (DEC-018 tension), not routine merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-27
**Proposed by:** Elvis
**Source:** `workspaces/elvis/paid-tier-features-2026-08-27.md`, extends DEC-018
**Topic:** Apply-to-join screening questions, quota by tier
**Type:** Product / Commercial
**Decision:** A host using apply-to-join can write up to 3 screening questions for free; individual-tier
premium raises that to 10.
**Reasoning:** Directly matches the shape DEC-018 already established for Moments (10 free / 20
individual-paid / 50 org-paid media items), a quota that scales with tier rather than a feature blocked
outright for free users. A full free-tier block was considered and rejected: apply-to-join questions are
how a host screens who gets into their event, and blocking that outright for free hosts would edge toward
gating a marketplace-adjacent capability (screening/curation), which DEC-018's own three-bucket rule says
not to do. A small free quota keeps the capability available to everyone; more questions for a host who
wants finer screening is a difference of degree, in the "quota-gate" bucket DEC-018 already permits.
**Impact:** Needs a tier-check on question count at event creation/edit for apply-to-join hosts. Exact
numbers (3, 10) are a starting point, not data-backed, same caveat DEC-018's own media caps carried at
first ("priced against realistic usage"), worth revisiting once real usage exists. Apply-to-join itself is
still an unmerged proposal (phase-1.5 placement, from the 2026-08-26 session), this quota rides along with
that feature's own merger rather than needing separate build sequencing.
**Relates to / Supersedes:** Extends DEC-018. Depends on apply-to-join's own (still unmerged) phase-1.5
placement and design.
**Status:** Awaiting merger
