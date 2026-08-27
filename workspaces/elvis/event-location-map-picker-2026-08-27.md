# Event location map picker, 2026-08-27

> Elvis workspace working file. Item #6 of the phase-1/1.5 review list (`wepop-scope-matrix.md`). The
> original 2026-08-17 walkthrough flagged "O2 - Map picker: one interaction detail Elvis and Deepak still
> need to finalize" and it was never actually written down anywhere beyond that line, carried forward
> unresolved on the task board and tracker ever since. Rather than guess at a lost detail, this file
> captures the full picker design Elvis described fresh today: three surfaces sharing one component, a
> zoom-determines-precision mechanic that extends DEC-003, a newly-scoped location poll, and a real, current
> finding on the map-provider question that changes a HOTSHEET "watching" item into something worth an
> actual decision.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

DEC-003 established the interaction model (Google-Maps-style search-plus-tap, not Uber's fixed center-pin)
but the specific open detail from the original walkthrough was never recorded anywhere beyond a single
unexplained line. Working through the picker's actual use cases today surfaced enough real design questions
to make this moot, rather than continuing to carry an undefined flag forward.

## Three surfaces, one component, RESOLVED 2026-08-27 (confirmed by Elvis)

The same map-plus-search component serves three distinct surfaces, not three separate pickers:

1. **Event/idea location capture**, at creation. Full-screen map, search bar, current-location recenter
   icon. Search for a place, or pan/zoom and tap directly.
2. **Location polls**, a newly-scoped use of the same component (previously only named in passing, on
   TASK-016, never designed). A creator adds multiple location options, each captured through the identical
   picker-plus-optional-comment flow described below, and attendees vote among them.
3. **Explore's browse map**, already extensively specified in `recommendation-algorithm-2026-08-25.md` and
   this session's location work, a live-viewport query, not a point-selection flow. Same underlying
   map/search/geocoding plumbing, different mode: browsing content rather than picking a point to save.

Worth naming explicitly for Deepak: one core map component with (at least) two modes, a picker mode
(search, pan, zoom, tap-to-select, current-location recenter) and a browse mode (search, pan, zoom, live
content overlay), rather than building or maintaining three separate map integrations.

## Zoom determines precision, RESOLVED 2026-08-27 (confirmed by Elvis, extends DEC-003): no minimum floor

Panning and zooming before tapping determines the scale of what gets captured. Zoomed in, a tap resolves to
a specific store, building, or address. Zoomed out, a tap resolves to a broader area, a whole neighborhood.
This extends DEC-003, which described capturing "a place" (implicitly always a specific one); this makes
the captured precision a real range, user-controlled by how far they've zoomed, not a fixed grain.

**Whether Events need a minimum precision floor, RESOLVED against my own initial recommendation.** I'd
flagged a real concern: an Event (unlike a looser Idea) has real attendees who need to physically find it,
and QR check-in (DEC-014, required) depends on there being an actual place. I recommended requiring Events
to zoom in past some threshold; Elvis's correction is right and changes the picture: an event's top-level
location is not necessarily its meeting point. A host can supply the actual findable spot through the
optional per-location comment (below), or through the event-schedule feature's own ordered stops
(`event-schedule-2026-08-25.md`, which already reuses this exact map-picker component per-stop). A
neighborhood-wide event, a bar crawl, an "explore this area together" idea, genuinely doesn't have one
single point, and shouldn't be forced to invent one. No precision floor for either Ideas or Events, same
range for both.

## Mechanism, technical detail

Reuses the reverse-geocode-and-store-canonical-value approach already built for home location
(`city-location-registration-2026-08-27.md`), generalized across whatever precision tier the zoom level
implies: a canonical ID, a centroid or boundary reference, a display name, at the resolved tier (POI/address,
neighborhood, or whatever granularity the zoom level and the underlying map data actually support).

**Zoom-to-precision thresholds, starting technical proposal, not yet confirmed:** roughly, POI/building-level
at high zoom (comparable to street-level map zoom), neighborhood/locality-level at low zoom (comparable to
district-level map zoom), with a smooth range in between depending on what tier the map provider's own
reverse-geocoding actually returns at a given zoom. Exact thresholds depend on the map-provider decision
below, flagged as tunable, not locked here.

**Current-location recenter icon, RESOLVED:** a live, on-demand GPS read to recenter the map, the same
contextual-permission and ephemeral-not-persisted pattern already established for home feed and Explore.
Recentering the map is not itself a location capture, only the subsequent tap or search selection is.

## Optional per-location comment, RESOLVED (reconfirms and extends DEC-003)

DEC-003 already includes "an optional per-event note for the exact unit." This applies uniformly to every
location capture through this component, an event/idea's main location, each event-schedule stop (already
established), and each location-poll option (new). One consistent mechanism, not a special case per surface.

## Location poll, newly scoped 2026-08-27

Previously named only in passing (TASK-016: "needed for event / idea create and location polls"), never
actually designed until now.

**Resolution, RESOLVED 2026-08-27 (confirmed by Elvis):** the host manually confirms the final location
after voting, rather than the top-voted option auto-adopting. Voting surfaces group preference; the host
isn't required to follow it. Keeps a human in the loop on a decision QR check-in and attendee
safety/findability depend on, rather than letting a vote count alone silently become the real-world meeting
point.

**Not yet decided, deliberately parked, flagged for a follow-up pass:**
- Where poll creation lives in the event/idea creation flow (a toggle instead of a single location, most
  likely, not confirmed).
- Minimum and maximum number of location options a poll can have.
- Whether a vote is changeable before the poll closes, and what closes it (host action, a deadline, or
  both).
- Whether attendees see who voted for what, or votes are anonymous, consistent with the anonymity pattern
  already used elsewhere (DEC-014's rating comments, DEC-017's gender aggregates) but not yet decided here
  specifically.

## Map provider, RESEARCHED 2026-08-27, flagged for Deepak and Aakash: the existing "watch" call is worth
revisiting now, not because the facts changed, but because this session gave it a concrete mechanic to break

HOTSHEET.md already carries this as a "Watching" item from the 2026-08-26 team sync: "Korean map coverage
is a known future concern; Google Maps acceptable for now... revisit only if it becomes a real issue."
That was reasonable as an abstract concern. The zoom-precision mechanic designed today depends directly on
good building/POI-level data at the zoomed-in end, which makes this concrete rather than abstract, in one
of WePop's two named focus markets.

**Current state, researched 2026-08-27:** South Korea conditionally approved Google's request to export its
restricted high-precision map data on February 27, 2026, ending a 19-year dispute (five conditions attached:
domestic-server processing, obscured sensitive-site imagery, excluded contour data, a security "red button"
mechanism, a dedicated Google map-affairs officer in Korea). That approval has since stalled: as of the most
recent reporting, the two sides remain divided on implementation details (compliance plans, data-update
procedures, revocation mechanisms), with no follow-up meetings and no resolution timeline. Google Maps in
Korea today has no turn-by-turn navigation, and current sources describe its business/POI data as thin and
stale relative to domestic options; Naver Map holds a dominant position (roughly 73% market share by one
count, or about 31 million monthly users against Google's 12 million by another) and offers real English
support, undercutting the assumption that the domestic alternative is unusable for a non-Korean-reading
team.

**Recommendation, not a decision:** worth an actual call now rather than continuing to wait on a stalled,
timeline-less regulatory negotiation. Realistic paths: accept degraded precision for Korean users at the
picker's zoomed-in tier and stay Google-everywhere, or build a Korea-specific branch onto Naver Map or Kakao
Map's API for that one market. I don't have visibility into integration cost, API terms, or documentation
quality for either Korean provider, that's real scoping work for Deepak, not something to guess at here.
Flagging this as ready to move from "Watching" to an actual HOTSHEET decision item, not editing
`shared/HOTSHEET.md` directly per this workspace's governance rule.

**Sources (2026-08-27 research):**
- [Korea clears exporting map data for Google, ends 19-year dispute — The Korea Herald](https://www.koreaherald.com/article/10684189)
- [Google map export stalls 2 months after Korea's conditional approval — The Korea Herald](https://www.koreaherald.com/article/10720446)
- [Google Maps in Korea 2026: Why It Fails & What to Use Instead — krsnap](https://www.krsnap.com/2026/04/google-maps-korea-not-working-naver-map-english-2026.html)

## Dual Google/Naver feasibility, RESEARCHED 2026-08-27, in response to Elvis's follow-up

Elvis asked directly whether running both providers is realistic: is it possible, would provider selection
default to Korea based on location, and is the geo-data comparable enough to store in one table.

**Feasible, established pattern, not exotic.** Several apps serving both Korea and international markets
already switch map SDKs by region. The real cost is integration and consistency, not novelty.

**Scope, REVISED 2026-08-27 (Elvis's clarification): locked per map session, no live cross-border
swapping, no wrapper layer for now.** My first pass over-engineered this, framing it around a live
viewport-based swap as the user pans. Elvis's actual model is simpler and removes that entire problem:
Naver renders exclusively for a Korea-determined user, Google exclusively otherwise, decided once when a
map screen opens and held fixed for that session regardless of how far the user pans, including across the
Korea border in either direction. A Korea-determined user who pans to New York still sees it through Naver
(whatever coverage that has); a non-Korea user who pans into Seoul still sees it through Google, accepted as
"usable, not equivalent" for what's expected to be a rare case (most users create events in their own
country). No visual/interaction wrapper between the two SDKs is being built for early phases either,
accepted as a real but low-priority inconsistency for now, worth revisiting only if it becomes an actual
complaint. Both calls remove most of what I'd flagged as hard: no mid-session hot-swap to build, no
normalization layer to build yet.

**Determining Korea vs elsewhere, RESOLVED 2026-08-27: reuses the existing signal, no new detection
mechanism.** Elvis asked how best to determine this, and the right answer is to apply a principle he
already established: `internationalization-korea-2026-08-26.md` explicitly resolved against building any
general "is this user in Korea" flag, reasoning that "the framing of 'detect whether the user is in Korea'
is the wrong problem shape" and that a dedicated detector would cut against DEC-012/DEC-016's no-forced-GPS,
no-continuous-recheck stance. That file gave each feature needing a Korea signal its own natural one
(timezone from device OS, language from device locale, PASS eligibility from the phone's own carrier code)
rather than one shared mechanism. This session already built the right natural signal for map-provider
selection specifically, for an unrelated reason: the Explore country gate's current-location country (live
GPS if granted, else the stored home-location default, from `city-location-registration-2026-08-27.md`).
When a map screen opens, resolve that same signal once, Naver if it's Korea, Google otherwise, hold it for
the session. No new signal, no new privacy surface. This also gets the traveling case right without extra
logic: a Korea-based user actually standing in the US gets Google for that session (correct, they're
placing a pin where they are), not Naver just because Korea is their permanent home; a stored-country-only
rule would get that backwards.

**Operational cost, still real, unaffected by the simplification:** two SDK integrations, doubled across
iOS and Android (closer to four integration surfaces than two), two billing relationships, two credential
sets, two providers' terms of service and data-handling obligations, the last worth a light PIPA flag given
Naver would be a Korean data processor handling user location data, not fully resolved here.

**Data compatibility, better than expected on coordinates, not on place records.** Naver's Maps API v3
supports WGS84 latitude/longitude directly as input and output, the same system Google uses, even though
Naver's engine runs its own projection internally. Raw coordinates don't need manual conversion to share a
table. Place records don't carry over as cleanly: Google Place IDs and Naver's own POI identifiers are
different namespaces from two different companies, and Korean addresses have their own structure (a
jibun-versus-road-name convention) that won't map one-to-one onto how Google formats an international
address. Confirms the direction already implied by this file's canonical-ID approach: store a
provider-agnostic canonical ID, centroid, and display name as the primary record, with each provider's own
place ID and raw address kept as secondary reference fields, not the primary key.

**Real unresolved question, not answerable by more searching:** whether a non-Korean-registered business can
actually sign up for Naver Cloud Platform's or Kakao's Maps API at all. Neither's public documentation
states eligibility either way. NCP's listed support line is a Korea-domestic number, a soft signal it's
Korea-oriented, not proof of a hard restriction. This needs someone to actually attempt account creation or
contact developer support directly, not further desk research, and is worth resolving before scoping the
rest of this (the wrapper layer, the cross-border handling) any further.

**Sources (dual-provider research, 2026-08-27):**
- [Naver Cloud Platform Maps overview](https://guide.ncloud-docs.com/docs/en/maps-overview)
- [NAVER Maps API v3, projections and coordinate systems](https://navermaps.github.io/maps.js.en/docs/tutorial-Projection.html)
- [Kakao Developers FAQ](https://developers.kakao.com/docs/latest/en/getting-started/faq)

## Precedent for dual-provider (Google + Naver) architecture, RESEARCHED 2026-08-27, flagged for Deepak

Elvis asked which real companies handle a Korea/international map split like this and how. Full account of
what a thorough search actually turned up, so this reads as researched fact plus an honest gap, not a
confident claim I can't back up.

**Confirmed, concrete: the underlying pattern is real and working, at the tooling level.**
[`react-maps-loader`](https://github.com/hyejin85/react-maps-loader), an open-source project by a Korean
developer, is a monorepo that wraps both Google Maps and Naver Maps as separate React components
(`react-maps-loader-google` and `react-maps-loader-naver`), explicitly built so either provider can be used
from the same codebase. This is real, verifiable confirmation that Google and Naver can coexist cleanly in
one codebase, a practitioner actually built infrastructure for exactly that combination. It does not include
region-based auto-switching logic itself, that's left to whatever app consumes it, consistent with this
file's own recommendation to keep provider selection as app-level logic on top of two independent SDK
integrations.

**The well-documented analogous precedent is China, not Korea, and the severity is meaningfully different.**
International apps operating in China are commonly known to swap in Baidu Maps or Amap/Gaode instead of
Google Maps for their China operations, Airbnb is the most commonly cited example. That precedent is real
and confirms "swap map backend by region" is an established pattern in principle. It's a harder problem than
Korea's, though: Google Maps is effectively blocked in China by the Great Firewall, not merely degraded, so
those companies had no functional choice. Korea's situation is weaker in severity, Google Maps works, it's
missing turn-by-turn navigation and has thin POI data, which is a real but lesser problem. The China
precedent supports the pattern's soundness, it doesn't prove any company has solved Korea's specific,
lower-severity version of it.

**Honest gap, despite searching several channels:** no named company or public engineering write-up
describing "we use Google globally and switch to Naver or Kakao specifically for Korea, here's why and how"
turned up, not in engineering blogs, conference talks, package docs, or developer forum threads. The one
Korea-focused map-API comparison piece found (a Medium post recommending Kakao for Korea-only services) was
written from a Korea-only service's perspective, not a global app's Korea branch, so it doesn't actually
address this question either. Read as: most global apps operating in Korea have apparently accepted Google's
degraded experience there rather than building a second map integration, at least without publishing about
it, not as evidence the approach is unsound. Worth Deepak's own review before treating this as settled either
way.

**Sources (precedent research, 2026-08-27):**
- [react-maps-loader (GitHub)](https://github.com/hyejin85/react-maps-loader)
- [Can Alibaba and Baidu convince Chinese travelers to ditch Google Maps? — KrASIA](https://kr-asia.com/can-alibaba-and-baidu-convince-chinese-travelers-to-ditch-google-maps)
- [The best map API for Korean services — Medium](https://medium.com/@codeisneverodd/the-best-map-api-for-korean-services-62fa0fb5c78d)
