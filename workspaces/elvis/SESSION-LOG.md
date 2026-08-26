# Elvis - Session Log

> Append each session summary here. Most recent at top. This is the audit trail of your work.

---

## 2026-08-26 - Embeddings/tagging pipeline, robustness roadmap, internationalization, and Korea-user
detection resolved; first proposal filed to the merger
Second start-session of the visible stretch (first re-verified Aakash's large DEC-010 through DEC-025
merge against the actual repo state rather than assuming the earlier briefing still held, catching one
real stale-doc discrepancy in CLAUDE.md section 8, flagged rather than fixed unilaterally). Elvis then
worked through four linked topics. Resolved how embeddings and hidden internal tags actually get
generated, since Elvis correctly identified this cannot be manual
(`recommendation-algorithm-2026-08-25.md`): a create/edit-triggered pipeline (embedding model call plus
LLM-based tag extraction) for content, pulled into launch scope since it needs no behavioral history,
versus a periodic batch job refining user-side embeddings from engagement data, deferred until real usage
exists. Scoped a day-1-versus-later robustness roadmap: basic experimentation/bucketing capability
resolved for day 1, impression/position logging and deletion handling explicitly deferred by Elvis
despite the retroactive-data-loss tradeoff already being explained, and anti-gaming reframed away from a
rate-limiting system toward account integrity (one personal account per phone number, ID verification
later, Org accounts always traceable to a specific user, reviews already gated to checked-in attendees).
Then scoped internationalization and Korea-specific concerns in a new file
(`internationalization-korea-2026-08-26.md`), grounded in real research rather than assumption: full i18n
architecture from day one with on-demand UGC translation explicitly deferred, a bilingual tag vocabulary,
a flexible full-name field for Korean naming order, and on the Korea side a genuine gap found in DEC-010's
Stripe-only payments plan (escalated to `proposed-hotsheet.md`, the first proposal filed to the merger in
over three sessions), Bumble's actual Korea ID-verification flow strengthening the already-provisional
DEC-012 age gate, a resolved plan to adopt Korea's carrier-based PASS verification, and three concrete
PIPA points tied directly to the embedding/tag layer. Closed with a Korea-user-detection design that
reframed "is this user in Korea" into four independent signals rather than one new detection mechanism:
timezone and language read from the device with a settings-level manual override on each (Elvis
confirmed both), PASS eligibility checked directly against the phone number's own carrier country code
rather than DEC-012's blended value, payment options driven by the org's own billing setup, and a
redacted-ID fallback path for Korea-based users without a Korean number.
Open: `proposed-decisions.md` still has nothing filed despite several launch-scoped resolutions this
session (embeddings/tagging pipeline, day-1 experimentation capability, PASS adoption plan) that read as
real decisions, not just workspace notes, this gap is now four-plus sessions deep even though the hotsheet
channel was used for the first time. Item 10 still has not actually been sent to Aakash. No `shared/`
edits made.

**Detail:** [session_log_2026-08-26.md](session_log_2026-08-26.md)

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
