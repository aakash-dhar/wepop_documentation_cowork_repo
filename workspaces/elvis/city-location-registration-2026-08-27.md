# Home location at registration, 2026-08-27

> Elvis workspace working file. Item #4 of the phase-1/1.5 review list (`wepop-scope-matrix.md`), given
> the same detailed flow-review treatment items #1 (onboarding) and #2 (auth) got. Location at registration
> was already decided at a policy level (DEC-016, from conflict-review item 7, "a general city-level
> location") and slotted as step 4 of the assembled onboarding sequence
> (`onboarding-flow-2026-08-26.md`), but the actual input mechanism, exact granularity, mutability, its
> relationship to DEC-019's cohort formula, and (added later this session) a monetization angle on Explore
> had never been specified. This file resolves those, confirmed live with Elvis 2026-08-27, revises
> DEC-016's granularity from city down to neighborhood, and surfaces two real proposals: a DEC-019 revision
> and a new DEC-018 monetization feature that needs Aakash's explicit sign-off, not just routine merger, see
> the flag in that section.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

DEC-016 says registration requires "a general city-level location that is typed or selected from a
list/search (not a device permission grant)." That settled the policy question (required, no forced GPS)
but left the actual mechanism, precise granularity, mutability, and the relationship to DEC-019's cohort
formula undecided. Those gaps mattered enough to work through before this can be handed to Deepak as a
build spec, and working through them surfaced a real problem with "city" itself as the stored granularity,
plus a genuine monetization idea from Elvis worth documenting carefully given its governance implications.

## Onboarding input, RESOLVED 2026-08-27 (confirmed by Elvis): unrestricted map picker, one-time

At onboarding only, the user sees a map with a search bar, the same search-plus-tap interaction DEC-003
already built for picking an event location, and taps anywhere in the world, then confirms. This is a real
design-system reuse, not a new component, and it's genuinely unrestricted at this step: the user can pick
any location on Earth as their home. This unrestricted picker is a one-time onboarding privilege, see
Mutability below for why later edits work differently.

## Granularity, RESOLVED 2026-08-27 (confirmed by Elvis): neighborhood-scale, down from city-scale

DEC-003's picker was built to capture a precise place ("let's meet at this park"). DEC-016 requires only a
general location, not an exact one, for the same anti-stalking reasons already landed in DEC-006/DEC-017.
The first pass at this (reverse-geocode the tapped point to a city, discard the exact coordinate) was
directionally right but too coarse: Elvis's own catch is that a city-wide bucket can span many kilometers,
which starves DEC-020's existing `geo_distance` ranking signal (`w4` in the scoring formula, already
computing real distances like "3km away" in its worked examples) of any real precision.

**Target granularity, RESOLVED:** neighborhood-scale, roughly dong-level in Korea or a
neighborhood/postal-code-sized area elsewhere (comparable to a US zip code), not a full administrative city
and not gu/borough-scale either. Small enough to give `geo_distance` real accuracy, large enough that it
doesn't reveal where someone actually lives.

**Mechanism, RESOLVED:** the moment the user confirms a point on the map picker (at onboarding, or during a
current-location update per Mutability below), the app reverse-geocodes it to this neighborhood-level area
(a canonical ID, that area's centroid coordinate, and its country, see the Explore gate below for why
country is captured here too) and stores only that. The exact coordinate is used for the one-time
reverse-geocode lookup and then discarded, never persisted or transmitted beyond that lookup. The stored
centroid becomes the anchor point DEC-020's retrieval radius and `geo_distance` ranking measure from,
resolving a gap recommendation-algorithm-2026-08-25.md never actually specified.

**Cross-market consistency, flagged for Deepak, not resolved here:** neighborhood-level geocoding tiers
aren't globally consistent. Seoul has a clean gu/dong hierarchy; many US cities have no official
administrative neighborhood tier at all, and geocoders fall back to an informal neighborhood name, a
postal/zip code, or nothing between city and exact address. Needs a defined fallback chain (neighborhood,
then postal code, then city) rather than assuming every market resolves cleanly to the same tier.

**Canonical identity, implementation detail:** whatever the reverse-geocode resolves to needs a stable
canonical ID underneath (not just a display string), same requirement DEC-019's cohort matching already
implied for city, applies one level down at the neighborhood tier, plus a canonical country code alongside
it.

## Mutability, REVISED 2026-08-27 (confirmed by Elvis, replaces this file's earlier resolution): after
onboarding, updates are restricted to "set to current location," no free re-picking

The unrestricted map-tap picker is onboarding-only. Once set, the home location can only be updated by
granting device location permission and selecting "use my current location," a live GPS read that becomes
the new stored value (still reverse-geocoded down to neighborhood-plus-country, still discarding the
precise coordinate, exactly as at onboarding). The free-form map picker does not reopen for a profile edit.

**Why this matters beyond mutability itself:** this closes a real loophole in the Explore country-gate
below. Without this restriction, a free user could defeat that gate by simply re-opening an unrestricted
picker and dropping a pin in whatever country they want to preview. Restricting edits to GPS-confirmed
location means a user can only ever "become" a country by actually being there, not by claiming to be.
Worth being upfront about the residual gap this doesn't close: a user can still misrepresent their country
once, at onboarding itself, since that step stays unrestricted. Same category of risk DEC-012's
self-declared age/country already accepts, not a new one.

**No-GPS fallback, RESOLVED 2026-08-27 (Elvis's explicit call, against my recommendation): hard
requirement, no fallback.** A user who never grants device location permission has no path to update their
home location after onboarding, not for a genuine relocation, not for a correction, nothing, self-serve or
support-assisted. I'd flagged this as a real risk, comparable to a user getting permanently stuck with a
stale value, and recommended a support-ticket fallback matching DEC-012's pattern for its own locked value.
Elvis's call was to keep it a hard requirement with no exception. Recording the risk plainly rather than
softening it: this is a real, if probably rare, class of user (anyone who relocates and never grants
location permission) who will have no way to fix a stale home location, ever, under this design.

**Integrity caveat, flagged for Deepak, not resolved here:** "current location only" as an anti-gaming
mechanism only works as well as GPS itself resists spoofing. Mock-location tooling exists on both major
platforms (more easily on Android via developer options, but not exclusively). This doesn't mean the
mechanism is worthless, it raises the bar well above a free-form picker, but it shouldn't be assumed
airtight either.

## Home feed / Explore anchor, RESOLVED 2026-08-27 (confirmed by Elvis, simplified from an earlier
three-tier version now that browsing-city is retired below): live GPS if granted, else the stored default

Two tiers, not three: (1) live current location, if the user has granted device GPS permission; (2) the
stored home-location default, if GPS was never granted or is denied. This is the contextual GPS trigger
DEC-016 already anticipated (it names Explore's map as an example value point), not a new exception to the
no-forced-GPS decision, home feed and Explore are simply two more such value points.

Home feed gets an explicit manual refresh action, re-pulling live GPS on demand rather than only reading it
once per screen load. Whether Explore needs an equivalent manual refresh, distinct from the map's own live
viewport panning, is not yet decided, see below.

**Persistence, recommended by me, not yet independently confirmed:** a live GPS read used to anchor home
feed or Explore should stay ephemeral, used to compute that request and discarded, never written to the
stored home-location field. Only the current-location-update flow above should ever change the stored
value. Keeping these separate (a coarse persisted default, a precise ephemeral live read) avoids GPS
permission quietly becoming a persisted precise-location log, in tension with the anti-stalking stance
already landed (DEC-006, DEC-017).

**Fetch behavior:** on-demand per screen load and on manual refresh, not continuous background tracking.
No meaningful ranking benefit to continuous tracking within one session, real battery cost, and more
invasive than DEC-016's contextual-permission framing describes.

## Explore content gate by country, PROPOSED 2026-08-27 (Elvis's monetization idea, flagged for Aakash's
explicit financials-owner sign-off, not just routine merger, see the DEC-018 tension below)

**The idea:** Explore's map and search stay fully open for everyone, panning and searching anywhere in the
world is never restricted, matching the earlier call that gating the map interaction itself reads as
broken, not as a paywall. What's gated is content detail: for a free user, events in a different country
than their current-location country (the same signal resolved above, live GPS if granted, else the stored
default) render as an aggregate teaser only, a clustered count with no pin-level or listing detail, tap-to-
upgrade. Events within the same country as current location render in full. Individual-tier premium lifts
this gate entirely, full detail everywhere. Elvis's stated use case: a user planning a trip abroad wants to
browse what's happening at the destination before they arrive.

**Reuses an existing pattern rather than inventing one.** This is the same "aggregate visible, individual
detail gated" language DEC-006 and DEC-017 already use for the pre-join attendee view (gender as a ratio,
photos gated to mutual follows). Using it here keeps the monetization gate visually and conceptually
consistent with a pattern users already learn elsewhere in the app, rather than a new dark-pattern-shaped
wall.

**A genuinely coherent side effect, confirmed as intended rather than left ambiguous:** because the gate
compares content country against *current-location* country (not a fixed home value), a free user who is
actually standing in another country, GPS-confirmed, sees that country's content in full, no paywall,
since it's no longer a preview, they're there. The gate only bites while previewing a country you are not
currently in. One real consequence worth being explicit about: a free user traveling with GPS on would
correspondingly lose full-detail access to their own home country's content for the duration, since it's no
longer their current-location country. Turning GPS off while traveling would fall back to the stored home
default, restoring full access to home content (and re-gating the country they're actually standing in).
This is an emergent, not special-cased, consequence of a single simple rule, flagged so it reads as
intended rather than something Deepak "fixes" unexpectedly later.

**Must not be conflated with DEC-012's country signal, same discipline DEC-016 item 7 already established
for city versus DEC-012's country.** This is a third, distinct country-shaped value: dynamic (moves with
current location), used purely for this content gate, with no legal or age-threshold meaning. DEC-012's
country is self-declared, locked forever, and exists purely for the age gate. Naming and data modeling
should keep these unmistakably separate fields, not two things called "country" on the same user record.

**Governance flag, real tension worth surfacing rather than quietly filing:** DEC-018 (Aakash's territory
as financials-owner) explicitly states "paid ranking/discovery boost is explicitly locked out," reasoning
that a paid discovery advantage would cut against the fairness/anti-stalking moat. My own read is that this
proposal is different in kind from what that rule was protecting against: DEC-018's concern reads as
same-market competitive fairness, a paid user should not get better placement or visibility of the *same*
local events free users and hosts are competing over. This gate does not touch ranking, placement, or
visibility within a user's own market at all, it only concerns access to an entirely different, non-
competing market (a country the user does not live in). That said, "discovery boost" is close enough to
this proposal's surface description that I don't think it's my call to wave through, this needs Aakash's
explicit read against DEC-018's own rule before it becomes a filed proposed decision, not just Elvis and me
agreeing it's probably fine.

## Cohort formula, REVISION PROPOSED 2026-08-27 (confirmed by Elvis, changes an ACTIVE decision): drop
location from the cohort key, cohort becomes student-vs-not only

Unchanged from this file's earlier resolution. DEC-019 currently defines cohort as `(city, age/life-stage
bucket)`, with university-affiliated users pulled into their own `(city, university-affiliated)` cohort.
Elvis's read: phase-1 cohort is doing its real work on the student/not-student axis, not the geographic
axis. Cohort becomes a single binary value, university-affiliated or not, computed the same way everywhere.
Location is removed from the cohort formula entirely; geographic relevance for home feed and Explore was
already radius/viewport-based, not a city hard-match, so this doesn't remove a filter, it just stops
conflating cohort with geography. Filed to `proposed-decisions.md`, revising DEC-019, awaiting Aakash's
merger.

## Not yet decided, deliberately parked

- Whether Explore gets its own manual refresh distinct from the home feed's, or relies on the map's live
  viewport panning plus whatever anchor the ranked list view inherits.
- Whether changing the home-location field (via a current-location update) should show any confirmation
  ("this will update your feed, ranking, and Explore gate") or apply silently.
- Exact UI for the aggregate-teaser markers on Explore's map at country scale, cluster count copy, what
  happens when the map is zoomed out to a world view with many countries partially teased at once.
- Whether Explore's ranked list view (not just the map) needs the same teaser treatment for out-of-country
  results, or excludes them entirely from that view.

## Flags for Deepak, implementation, not decided here

- Home-location capture (onboarding, unrestricted; current-location update, GPS-only) both reverse-geocode
  to a canonical neighborhood ID, centroid, and country code, discarding the precise coordinate immediately
  after that lookup, never persisted.
- Needs a defined geocoding fallback chain (neighborhood tier, then postal code, then city) for markets
  without a clean neighborhood/sublocality tier.
- Canonical neighborhood ID needs a bilingual/per-market display layer, same requirement DEC-019's
  exact-match cohort key already implied for city.
- The stored country field for the Explore gate must be a distinct field from DEC-012's locked legal
  country, different purpose, different mutability, different name, should not share a column or a
  conflated concept in the data model.
- Current-location updates require a live GPS read; there is deliberately no fallback path for a user who
  never grants permission, confirmed by Elvis, flagged as a real support-load and user-stuck risk worth
  monitoring post-launch even though it's the agreed design.
- Server-side enforcement is the real gate for the Explore country teaser, the client map must never be the
  authority, since a modified client could otherwise request full detail directly. Every Explore query
  needs the requester's tier and current-location country compared against each candidate event's country
  at query time, not resolved once and cached.
- Live GPS reads (for anchor resolution or current-location updates) should not be persisted beyond serving
  the single request, including in analytics/logging pipelines, worth an explicit note in the
  data-retention spec, not just the capture spec.
- DEC-020's retrieval stage needs its radius/viewport anchor point updated from an unspecified user-location
  value to the new neighborhood centroid explicitly, worth a one-line addition to
  `recommendation-algorithm-2026-08-25.md` so the two docs don't drift.
- Home feed's manual refresh needs a loading/error state for the GPS read itself (permission revoked mid-
  session, timeout), falling back to the stored default rather than failing the whole feed load.
- Mock-location/GPS-spoofing resistance for the current-location-update flow is a real, only partially
  closeable gap, worth a light fraud-review note even if not a phase-1 build item.

## Retired this session: the standalone "browsing city" override

An earlier pass at this file proposed a separate, manually-set "browsing city" concept distinct from the
home location, kept at city-scale, for previewing another city ahead of a trip. That's superseded by the
two mechanisms above: Explore's map already pans and searches anywhere in the world with no restriction,
which covers domestic trip planning for free, and the country-level content gate covers the international
case directly, as a real (proposed) monetization feature rather than a free manual toggle. Keeping both
would have meant two overlapping ways to look at somewhere else. The corresponding `proposed-decisions.md`
entry is being revised to drop this point rather than left filed alongside the mechanism that replaces it.
