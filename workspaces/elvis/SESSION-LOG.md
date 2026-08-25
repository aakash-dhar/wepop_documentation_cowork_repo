# Elvis - Session Log

> Append each session summary here. Most recent at top. This is the audit trail of your work.

---

## 2026-08-25 (session 2) - Community segmentation, recommendation algorithm, and group dynamics scoped
Elvis raised two new strategic topics unprompted: how to handle very different early cohorts sharing a
city (a college student and a 40s professional joining Seoul around the same time), and the
recommendation algorithm behind home feed, explore, and Sunday Deck. Resolved community segmentation
(`community-segmentation-2026-08-25.md`) as cohort = (city, age/life-stage bucket), computed
independently per user, with university-affiliated users pulled into their own overriding cohort at
launch. The mechanism itself was revised mid-session from a soft ranking signal to a hard retrieval
filter at launch (same cohort is a must), softening once a city is manually confirmed dense enough, both
changes recorded not overwritten. Scoped the recommendation algorithm in detail
(`recommendation-algorithm-2026-08-25.md`): rule-based weighted scoring now, architected two-stage
(retrieval then ranking) so a learned model can slot in later, extended with text keyword matching,
evolving user interest profiles, and a hidden internal keyword layer across ideas/events/moments/users.
Explore was split into an unranked, viewport-bounded map view and a fully-ranked list view. Documented a
future per-user learned-weighting direction (Netflix/YouTube/Spotify-style), explicitly deferred, launch
keeps one global formula. A new concept, group dynamics, split out into its own file
(`group-dynamics-2026-08-25.md`): an avoid-signal (soft penalty, amplified by an explicit block),
look-alike host affinity (parked, needs scale), and personality-mix compatibility (ranking signal only),
surfacing two real gaps, a general blocking feature and attendee-level feedback, neither designed yet.
Open: several mechanism transitions flagged rather than assumed (does cohort truly revert to a ranking
signal once a city softens, does the map's cohort restriction loosen too); nothing from this session or
the prior two has been promoted to `proposed-decisions.md`, that gap is now three full sessions deep;
item 10 still hasn't actually been sent to Aakash. No `shared/` edits made.

**Detail:** [session_log_2026-08-25_session2.md](session_log_2026-08-25_session2.md)

---

## 2026-08-25 - Recurring events closed out, new Event Series concept, five-item feature batch scoped
Closed out the recurring-events follow-up (`recurring-events-2026-08-25.md`): separate linked Event
instances sharing a recurring group, Google Calendar-style edit/delete/join semantics, batch-generated
occurrences, both individual and org hosts. Elvis introduced a second, different series concept mid-
session (a thematic hub for heterogeneous events, closer to Idea than to recurring events), fully
scoped in `event-series-2026-08-25.md`: self-curation only, phase 1.5, pulls co-hosts forward from
later-phase, multi-series membership allowed. Caught and fixed a real naming collision between the two
concepts before it caused confusion downstream. Then worked through a twelve-item feature batch Elvis
raised in one message (`feature-backlog-2026-08-25.md`): triaged and sized all twelve, logged seven as
their own future dedicated conversations, fully scoped five (event schedule, live stories, Free Now,
icebreakers, tips/guides), each in its own file. Free Now got the most careful treatment, grounded in
documented failure patterns from comparable real-time-location products, safety-first defaults locked
throughout (rounded location, aggregate-first visibility, reciprocal join, restricted room creation).
Open: several flagged sub-details across the five scoped items still need answers before build; nothing
from this session or the last has been promoted to `proposed-decisions.md`, that gap is now two full
sessions deep; item 10 still hasn't actually been sent to Aakash. No `shared/` edits made.

**Detail:** [session_log_2026-08-25.md](session_log_2026-08-25.md)

---

## 2026-08-19 through 2026-08-24 - Conflict review closed out, freemium model built and priced
Walked all ten items in `conflict-review-2026-08-19.md` to resolution (the six headline
draft-vs-walkthrough conflicts, location at registration, gender/photos pre-join, the ten undiscussed
drafted surfaces) plus one escalation (Moments doc names/budget/legal, routed to Aakash). Built the
full freemium model in `freemium-model-2026-08-19.md`: individual tier at $3.99/mo or $36/yr, org tier
at $19.99/mo or $199/yr, both fully specified and priced, with a real infrastructure cost model
grounded in current Cloudflare R2/AWS pricing behind the org tier's media caps (50 items/attendee/
event), a 12-month retention policy, and a manual safety valve for extreme-usage outliers instead of
defensive pricing. Recommended R2 over S3+CloudFront and self-hosted transcode over Cloudflare Stream,
flagged for Deepak. Open: series pages need recurring events scoped first, not yet started. Neither
workspace file has been promoted to `proposed-decisions.md` yet, and item 10 has not actually been
sent to Aakash yet, only marked ready. No `shared/` edits made, all governance-correct.

**Detail:** [session_log_2026-08-24.md](session_log_2026-08-24.md)

---
