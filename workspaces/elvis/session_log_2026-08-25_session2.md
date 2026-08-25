# Elvis - Session detail, 2026-08-25 (session 2)

Third session of the day. Elvis raised two new strategic topics unprompted: how to handle very
different early cohorts in the same city, and the recommendation algorithm behind home feed, explore,
and Sunday Deck. Both turned out to be closely linked, cohort segmentation resolved as an input into the
recommendation algorithm rather than its own system, and a related new concept, group dynamics, split
out into its own file partway through.

## What got done

**Community segmentation, `community-segmentation-2026-08-25.md`.** Elvis's framing: a college student
and a 40-year-old professional joining WePop in the same city around the same time would confuse each
other about who the app is for. Resolved: a cohort is (city, age/life-stage bucket), computed
independently per user rather than inherited from an inviter (revised mid-session, first resolved as
inheritance, then corrected). University-affiliated users get pulled into their own overriding cohort at
launch, qualified by any of three signals (self-declared, school email domain, or membership in a
university-affiliated Org profile), one combined cohort per city regardless of specific school. The
mechanism itself was revised once during the recommendation-algorithm discussion: first resolved as a
soft ranking signal, then changed to a hard retrieval-stage filter at launch (same cohort is a must),
softening back to a ranking signal once a city is confirmed dense enough, both changes recorded, not
overwritten, per this repo's own convention. The density-threshold trigger that decides when a city is
dense enough was also revised, from fully automatic to a manual PM-reviewed call at launch, to be
automated later.

**Recommendation algorithm, `recommendation-algorithm-2026-08-25.md`.** Scoped for home feed and
explore. Architecture: rule-based weighted scoring now, no engagement history exists yet to train a
model on, built as a two-stage retrieval-then-ranking pipeline specifically so a learned model can slot
into ranking later without a rebuild. Elvis asked to review the scoring mechanics in detail, delivered as
a worked example with illustrative (not locked) weights. Elvis then added several real extensions in the
same session: keyword matching from an item's title and description text, not just structured tags,
folded into the same tag-overlap signal; a user's interest profile starting from onboarding tags and
growing through inferred keywords as they use the platform; a hidden, internal-only keyword/tag layer
across ideas, events, moments, and users, based on the platform's own learnings, admin-visible for
auditing; and a broad future signal roadmap (likes, dwell time, ratings, attendee-level feedback,
look-alike signals, friends-of-friends) captured for once real usage data exists. Explore was later split
into two distinct views: a map view that is never ranked, viewport-bounded (updates live as the user
pans or zooms) and cohort-filtered only, versus a list view that runs the full scoring algorithm on the
same candidate set, geo-distance-dominant. Elvis also asked whether the launch formula is permanent and
whether users could ever have different weights; resolved to keep one global formula at launch and
document, for a later phase, per-user learned weighting in the direction Netflix, YouTube, and Spotify
are publicly known to use (learned embeddings, not a hand-maintained per-user weight vector), rather than
the lighter alternatives that came up (an explicit user preference toggle, cluster-level shared weights),
which were kept in the doc as considered-but-not-chosen.

**Group dynamics, new concept, `group-dynamics-2026-08-25.md`.** Elvis's own addition: who is already
attending an event matters as much to the experience as the event itself, a real, research-grounded idea
(group recommender systems is an actual academic subfield). Split into three sub-mechanisms once it
outgrew being a single bullet inside the algorithm doc. An avoid-signal, resolved as a soft ranking
penalty when a user consistently rates one specific other person low, amplified substantially when the
user has explicitly blocked that person. Look-alike host affinity, parked, needs real user-base scale to
compute meaningfully. Personality-mix compatibility (an extrovert-heavy group being a poor fit for an
introvert), resolved as a ranking signal only for now, no host-facing tool yet. Surfaced two real gaps
along the way: a general user-blocking feature is assumed but not designed anywhere in this repo, and
attendee-level thumbs-up/down feedback, the actual data source for the avoid-signal, does not exist as a
designed mechanism, flagged as needing its own dedicated scoping pass.

## Files touched this session

- `community-segmentation-2026-08-25.md` (created, revised twice: invite-inheritance corrected,
  mechanism and merge-trigger changed from automatic/soft to manual/hard at launch, university cohort
  added)
- `recommendation-algorithm-2026-08-25.md` (created, revised extensively across the session: illustrative
  scoring walkthrough added, keyword matching and hidden tags added, future signal roadmap added,
  Explore split into map/list views, per-user learned weighting direction documented)
- `group-dynamics-2026-08-25.md` (created)
- No `shared/` edits. Everything stayed in-workspace, correctly.

## Carried forward, open

- Real open items flagged rather than silently assumed: whether cohort match actually reverts to a
  ranking signal once a city softens, versus dropping out of the algorithm entirely; whether the Explore
  map view's cohort restriction ever loosens on the same trigger, explicitly deferred by Elvis; exact
  density threshold, boost decay curves, and per-signal weights all left as post-launch tuning, not
  locked.
- Two real feature gaps surfaced by the group-dynamics discussion, neither designed yet: a general
  user-blocking capability, and attendee-level post-event feedback (thumbs up/down on individual
  attendees).
- Nothing from this session, or either of the two prior sessions, has been promoted into
  `proposed-decisions.md` yet. This gap is now three full sessions deep, all of it sitting in-workspace
  with nothing landed in `shared/`.
- Item 10 (Moments-doc names/budget/legal) still has not actually been sent to Aakash, still only marked
  ready to escalate.

TASK-012 remains Blocked on TASK-010 on the board, unchanged this session.
