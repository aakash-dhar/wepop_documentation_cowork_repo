# Session detail, 2026-08-27

> Continuing the phase-1/1.5 review list started 2026-08-26 (item #1 onboarding, item #2 auth). This
> session covered item #3 (age gate, research only, still provisional), item #4 (city/home location, fully
> reworked across several rounds), confirmed item #5 (personality tags) already done, item #6 (event
> location map picker), plus an unplanned but substantial detour into paid-tier feature design triggered
> while reviewing item #4.

## Item #3, age gate: research filed to TASK-013, no decision change

`age-gate-country-cascade-2026-08-27.md`. DEC-012 stays ACTIVE and provisional, unchanged. Flagged two
things for counsel: DEC-012's own reasoning conflates age-of-majority with GDPR digital-consent age under
"Germany 16," and Apple's Declared Age Range API (expanded Feb 2026) offers a platform-native alternative
to the self-built store-region/GPS/phone-code cascade, worth putting to counsel as real questions rather
than assumed either way. Recommended defaulting to the stricter of the two legal concepts where a country's
figures diverge, pending counsel.

## Item #4, home location: extensively reworked, `city-location-registration-2026-08-27.md`

Started as a straightforward mechanism spec, ended up revised several times as real implications surfaced:

- Input reuses the DEC-003 map picker (search plus tap), unrestricted at onboarding only.
- Granularity revised down from city to neighborhood-scale (Elvis's catch: city-level was too coarse for
  DEC-020's `geo_distance` ranking signal).
- Mutability revised twice: first to "editable, full picker reopens," then to "current-location-only,
  GPS-confirmed" once the anti-gaming tie-in to the Explore country gate became clear. No fallback for a
  user who never grants location permission, Elvis's explicit call against my recommendation.
- Home feed / Explore anchor: live GPS if granted, else the stored default, with a manual refresh on home
  feed. Ephemeral GPS reads, never persisted.
- Cohort formula (DEC-019) revised: dropped location entirely, cohort becomes student-vs-not only. Caught
  and corrected my own oversimplification along the way (geographic relevance was already radius-based in
  DEC-020, never a city hard-match, so nothing new needed replacing there).
- A "browsing city" concept was proposed, then retired once the country-gate below made it redundant.
- Explore content gate by country, individual-premium perk (Elvis's idea, refined from an earlier, riskier
  "lock everyone to live GPS, pay to unlock" version he clarified he didn't actually mean). Reuses the
  DEC-006/DEC-017 aggregate-teaser pattern. Flagged, not filed as routine: DEC-018 explicitly locks out
  "paid discovery boost," and this needs Aakash's explicit read against that rule before merger, not just
  Elvis and me agreeing it's probably fine.

Two proposed decisions filed (DEC-019 revision, DEC-016 refinement), one flagged for Aakash specifically
(the country-gate, extends DEC-018).

## Item #5, personality tags: confirmed already resolved, no new work

Already covered via `personality-tags-catalog-2026-08-27.md` and `categories-taxonomy-2026-08-27.md`,
both done earlier the same day before this session's location work began.

## Detour: paid-tier feature design, `paid-tier-features-2026-08-27.md`

Triggered while discussing the country-gate's monetization angle. Elvis restated DEC-018's own three-bucket
rule in his own words (never gate core functionality); resolved apply-to-join screening questions at 3
free / 10 paid, filed as a proposed decision. Two low-effort next-candidate slots noted, not decided
(live-stories' already-open media-cap question, icebreakers' flat 3-question cap). Explore filter ideas
(multi-category combination, host-quality threshold, date-range picker) were floated as premium candidates,
then corrected by Elvis: these are core discovery functionality, not power-user extras, reclassified as
free for everyone. Saved filter presets parked entirely, not built now. "See who viewed your profile"
raised and explicitly shelved given the anti-stalking design stance, may revisit later.

## Item #6, event location map picker, `event-location-map-picker-2026-08-27.md`

Closed out a walkthrough flag that had carried unresolved since 2026-08-17 with no actual detail ever
recorded ("O2 - Map picker: one interaction detail Elvis and Deepak still need to finalize"). Elvis
described the real design fresh: one map component in two modes (picker, browse) serving three surfaces
(event/idea location, location polls, Explore); zoom level at tap time determines captured precision, no
minimum floor after Elvis corrected my initial instinct (an event's top-level location isn't necessarily
its meeting point, the per-location comment or event-schedule stops cover that); location polls newly
scoped (host manually confirms the winner, several mechanics still open).

Map-provider research escalated the existing HOTSHEET "watching" item: Korea's Feb 2026 conditional
approval of Google's map-data export has stalled with no timeline, and current Google Maps Korea data is
genuinely thin. Recommended moving this from watch to an actual decision. Follow-up research into dual
Google/Naver architecture: feasible, and Elvis's own simplification (locked per session, no live
cross-border swap, no visual wrapper for now) removed most of the real engineering difficulty. Korea
determination reuses the existing current-location-country signal rather than a new detector, consistent
with a principle Elvis had already established in `internationalization-korea-2026-08-26.md`. Precedent
research: honestly reported a claim I'd made without verifying it (that several companies already do this),
corrected it, then found real supporting evidence on a second pass (`react-maps-loader`, an open-source
project actually wrapping both Google and Naver Maps in one codebase) plus the well-documented but
higher-severity China/Baidu analogy, while being upfront that no named company doing Korea's specific
version was found despite checking several channels.

## Open at session close

- None of today's proposed decisions (DEC-019 revision, DEC-016 refinement, the Explore country-gate
  extending DEC-018, the apply-to-join quota extending DEC-018) have been merged yet.
- The Explore country-gate specifically needs Aakash's explicit sign-off against DEC-018's "no paid
  discovery boost" rule before it's even a normal awaiting-merger item, not routine.
- Whether a non-Korean-registered business can open a Naver Cloud Platform or Kakao developer account at
  all is unresolved and not answerable by further research, needs an actual signup attempt.
- Location poll mechanics (min/max options, vote changeability, anonymity, where it lives in the creation
  flow) not decided.
- Whether Explore needs its own manual location refresh distinct from home feed's, and whether a user who
  granted GPS can opt back into the coarser stored default, both parked.
- Items #7 onward of the phase-1/1.5 review list not yet reached.
- No `shared/` edits made this session, all writes stayed in `workspaces/elvis/`.
