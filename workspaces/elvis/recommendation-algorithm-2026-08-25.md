# Recommendation algorithm, scoping (home feed and explore)

> Elvis workspace working file, started and fully scoped 2026-08-25, raised in the same conversation
> as community segmentation and closely tied to it, the cohort signal resolved there is one input here.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Elvis's own framing: the home feed and Sunday Deck need to recommend events, ideas, and moments per
user, well, from a very early stage. The hard constraint underneath this: at launch there is close to
zero engagement history to learn from, so pure collaborative filtering ("users like you also liked X")
is not viable yet. The honest starting point is content-based and rule-driven, not machine-learned.

## Current state at a glance, updated 2026-08-25

This doc has accumulated several rounds of revisions. This section is a consolidated snapshot of where
the design actually stands right now, added at Elvis's request to review the full picture in one place.
Everything here is explained and reasoned through in the sections below, this is the summary, not a
new decision.

**Pipeline, two stages:**
1. Retrieval: time window, exclude RSVPed/dismissed, plus a geographic bound that differs by surface
   (a radius for home feed, the map's live viewport for Explore's map view), plus **same cohort as a
   hard filter at launch** (general age/geo, or the university-affiliated override where it applies).
2. Ranking: only runs for home feed and Explore's list view. Explore's map view is never ranked, it
   shows its full cohort-filtered, viewport-bounded candidate set positioned purely by geography.

**Ranking formula (home feed and Explore list view only):**

`score = w1*tag_and_keyword_overlap + w2*cohort_match + w3*recency + w4*geo_distance + w5*popularity + w6*social_proximity + w7*new_host_boost + w8*group_composition_fit + w9*embedding_similarity`

`w9`, embedding similarity, added 2026-08-26, see the content-embeddings section below. It runs
alongside `w1`, not replacing it, exact tag/keyword overlap stays fast and explainable, embedding
similarity catches semantically related content that shares no exact words.

Cohort match (`w2`) only participates in this formula once a city has been manually confirmed dense
enough that the hard filter above has relaxed. Before that point it isn't a weighted term, it's already
been applied as an exclusion during retrieval. Group composition fit (`w8`) covers both the avoid-signal
and personality-mix compatibility from `group-dynamics-2026-08-25.md`, not yet split into sub-weights.

**Illustrative weights** (placeholders for review, not locked, see the walkthrough below for how these
were used in a worked example): tag/keyword overlap 0.25, cohort match 0.20, recency 0.15, geo distance
0.15, popularity 0.10, social proximity 0.10, new-host boost 0.05. Group composition fit was added to
the formula after that worked example was built and does not yet have an illustrative weight assigned.

**Per-surface weighting:** home feed weights interest and cohort more heavily; Explore's list view
weights geo distance far more heavily, since by the time a user reaches list view they've already
implicitly chosen an area via the map.

**Signals still pending real data, not usable at launch:** likes/interest, dwell time, ratings on hosts
and events, attendee-level thumbs up/down (not yet a designed feature), look-alike collaborative
signals, friends-of-friends. See the future signal roadmap section below.

**Content embeddings and automated tagging, added 2026-08-26:** unlike the signals just listed, this
one is pulled into launch, since it only needs an item's own text, not accumulated user behavior. See
the dedicated section below for the full pipeline.

## Surfaces in scope, RESOLVED 2026-08-25: home feed and explore, now

Home feed is a personalized ranked mix of events, ideas, and moments. Explore splits into two distinct
views with two distinct jobs, resolved in detail below: a map view that is not ranked at all, and a
list view that runs the full scoring algorithm. Sunday Deck stays later-phase, already gated behind real
event density per `conflict-review-2026-08-19.md`, but its editorial-bridge design (below) is captured
now so it is ready whenever that surface gets built. Moments ranking (whether and how moments surface
inside the home feed itself, versus staying on profile and event pages) is explicitly not scoped in
this pass, flagged as its own open question.

## Architecture, RESOLVED 2026-08-25: rule-based scoring now, built ML-ready

A weighted scoring function on real, available-at-launch signals, not a learned model, since there is
no engagement history yet to train one on. Architected as a two-stage pipeline from day one so a
learned ranker can slot in later without a rebuild:

1. **Retrieval:** cheap filters narrow the full catalog to a realistic candidate set per user, time
   window (upcoming events, non-expired ideas), excluding anything already RSVPed to or explicitly
   dismissed. **REVISED 2026-08-25: same cohort is a hard filter here at launch**, not a ranking input,
   see `community-segmentation-2026-08-25.md`'s mechanism revision. A candidate outside a user's cohort
   (general age/geo, or university-affiliated where that override applies) is excluded at this stage
   entirely, it never reaches scoring. Once a city is manually confirmed dense enough, the working
   assumption is this reverts to a ranking signal instead of a retrieval filter, see the open item
   flagged in that doc. The geographic bound differs by surface: home feed uses a radius around the
   user, Explore's map view uses the map's current viewport instead, see below.
2. **Ranking:** the candidate set gets scored by a weighted combination of signals (below) and returned
   in ranked order. This is the stage a future learned model would replace or blend into, once there is
   real logged interaction data to train on.

### Signals available at launch, no behavioral history required

- Tag and keyword overlap (DEC-005 extensible tag list, self-declared, plus keywords extracted from an
  item's title and description text, matched against the user's own interest profile, see below).
- Embedding similarity (added 2026-08-26), a separate signal from tag/keyword overlap, see the content
  embeddings section below.
- Geo distance (DEC-003).
- Social graph proximity, follows and mutuals (DEC-006).
- Invite-chain proximity.
- Recency and urgency, soon-to-happen events rank higher.
- Popularity and fill-rate, a weak social-proof signal, deliberately dampened, see the fairness boost
  below.
- Group composition fit (avoid-signal, personality mix), see `group-dynamics-2026-08-25.md`.

Cohort match is not in this ranking list at launch, since it is currently a retrieval-stage hard filter
(above), not a scored signal. It rejoins this list, weighted rather than absolute, once a city softens.

### New-host fairness, RESOLVED 2026-08-25: deliberate boost for new/low-history content

Pure popularity-driven ranking creates a rich-get-richer loop: whatever got engagement first keeps
getting shown, and a new host's first event struggles to get its first few RSVPs simply because it has
no track record yet to rank on. Confirmed: new or low-history events and hosts get a deliberate,
explicit visibility boost, a counterweight to the popularity signal above, not a replacement for it. The
boost should decay as an item or host accrues real engagement of its own, a standard exploration bonus,
not a permanent advantage. The exact decay curve and boost magnitude are tuning questions for after
launch, not locked here.

## Text keyword matching and evolving user interest profiles, RESOLVED 2026-08-25

Elvis's own addition: yes, matching can and should look at the words in an item's title and
description, not just its structured tags. Concretely, keywords get extracted from an event or idea's
title and description text and matched against a user's own interest profile, feeding the same "tag and
keyword overlap" signal above rather than existing as a separate scoring term.

A user's interest profile starts from what they explicitly declare, the DEC-005 tags picked at
onboarding, and grows over time as the user uses the platform more: the system learns and attaches
additional keywords to that user's profile based on what they actually engage with, the same
cold-start-to-learned progression the rest of this algorithm follows, just applied at the level of an
individual user's profile rather than the whole ranking system. Early on, a user's profile is thin (just
onboarding tags); over time it becomes a richer, partly-inferred picture of their interests.

## Hidden internal keywords and tags, RESOLVED 2026-08-25

Elvis's own addition: alongside what a user or host explicitly enters, the platform should attach
internal-only keywords and tags to ideas, events, moments, and users, based on the system's own
learnings, not shown to the end user. This is a standard, well-established pattern (every major
recommender, Netflix and Spotify included, maintains inferred attributes users never see), and it
applies across all four entity types Elvis named, not just content: a user's own profile can carry
inferred keywords the same way an event or moment can.

**Internal visibility, RESOLVED:** admin-visible internally. The team should have a way to inspect what
the system has inferred about a given piece of content or a given user, for auditing and debugging, even
though this never surfaces in the end-user product. Flagged for the existing legal-consult action item
(`comms/todos.md` #4) that this kind of behavioral inference typically needs general disclosure in a
privacy policy ("we infer interests from usage"), even without exposing the specific inferred tags.

## Content embeddings and automated tagging, RESOLVED 2026-08-26: the actual process

Elvis asked what the actual process is for generating the hidden internal tags and embeddings, since it
cannot be manual. Two distinct mechanisms, worth separating clearly: discrete tags are human-readable
strings; embeddings are dense numeric vectors used for similarity math, not human-readable at all. Most
real recommenders (Netflix, Spotify, Pinterest) use both together, and this is mature, commodity
technology at this point, not something exotic to build.

**Pipeline for content (events, ideas, moments), RESOLVED:**
1. Trigger: on creation, and again on any edit to the title or description.
2. Embedding: the title-plus-description text is passed through a text embedding model, either a hosted
   API or a small self-hosted model, producing a vector stored alongside the item.
3. Tags: the same text is passed through an LLM-based extraction step, resolved over simpler
   keyword/term-frequency extraction, that outputs relevant tags drawn from the existing DEC-005
   vocabulary plus new candidate terms. WePop already has AI-assisted text tooling per DEC-007's
   carve-out (text prompt-to-create), so this is not a new category of AI use for the product, just a
   new application of it.
4. Both get stored. Admin visibility, per the earlier internal-visibility resolution, looks different
   for each: tags are literally readable strings; an embedding is inspected indirectly, an admin tool
   showing "the most similar items to this one" as a sanity check, not the raw vector values.

**Launch timing, RESOLVED:** pulled into launch scope, not deferred with the rest of the future signal
roadmap below. Generating an embedding or extracting tags from an item's own text needs no accumulated
user behavior, so it does not carry the cold-start dependency that collaborative filtering, look-alike
signals, and per-user learned weighting elsewhere in this doc all do. This is a genuinely different
category from "later phase, needs real data."

**Pipeline for users, RESOLVED:** a different shape, since a meaningful user profile does need some
signal to work from. Seeded immediately at onboarding from explicit signals already available (DEC-005
tags, university affiliation, any profile description text), then refined by a periodic batch job, not
computed per request, that recomputes a user's embedding from the embeddings of content they have
positively engaged with, weighted toward recency and engagement strength. This is the concrete consumer
of the day-one interaction-logging pipeline already required elsewhere in this doc: that log is the raw
material, this batch job is what turns it into a usable profile over time.

**Signal relationship, RESOLVED:** embedding similarity runs alongside the existing exact tag/keyword
overlap signal in the formula above (`w9`, separate from `w1`), not replacing it. The exact-match signal
stays fast, cheap, and easy to explain when someone asks why they were shown something; embedding
similarity catches semantically related content the exact-match approach misses entirely, a "sunrise
hike" and a "morning trail run" scoring as related despite sharing no exact words.

**Cost, flagged, not modeled here:** both the embedding call and the LLM-based tag extraction carry a
real, if typically small, per-item cost. Worth a short cost model before committing, the same kind of
exercise already done for the org tier's media infrastructure, not attempted here since it depends on
actual provider pricing and expected item volume.

## Future signal roadmap, once real usage data exists

Elvis listed a broad set of signals that only become usable once there is real behavioral data at
scale, an extension of the feedback-logging requirement above rather than a new architecture. Captured
here so nothing raised gets lost, not designed in detail in this pass:

- Explicit likes/interest, dwell time and time on screen, joins (RSVP and attendance behavior).
- Ratings given to events and hosts (already an existing concept elsewhere in the project).
- Thumbs up/down on attendees during a post-event feedback phase. This is a real, new mechanism, rating
  individual attendees rather than the event or host as a whole, and it does not exist as a designed
  feature anywhere yet. Flagged as needing its own dedicated scoping pass, not assumed here. It is also
  the direct data source for the avoid-signal in `group-dynamics-2026-08-25.md`.
- Collaborative "look-alike" signals, what similar people like, and social graph expansion to friends
  and friends-of-friends beyond DEC-006's direct-mutual signal. Both need real scale to compute
  meaningfully (a form of the cold-start problem in its own right), realistically a post-launch phase,
  not something to attempt on day-one data volumes.

## Editorial bridge, RESOLVED 2026-08-25: for Sunday Deck specifically, not home feed or explore

Concrete shape: a host manager, or Aakash/Elvis directly in the earliest cities, can manually feature or
pin a small number of individually strong events per city, shown prominently in that city's Sunday Deck
stack, as a stopgap while the pool is too thin for the algorithm alone to reliably tell a genuinely
well-put-together event apart from a sparse listing. Scoped to Sunday Deck only, not home feed or
explore, since a scrollable feed tolerates a weak result far better than a full-screen swipe decision
does. This is captured now even though Sunday Deck itself does not build until later, so the design is
ready when it does. Not decided: who operationally owns setting the featured flag day to day, and the
exact condition for turning the bridge off in a given city, plausibly the same density threshold already
used for the cohort-weighting relaxation in `community-segmentation-2026-08-25.md`, but not confirmed
as the same number.

## Explore: map view versus list view, REVISED 2026-08-25

First scoped as one ranked surface, geo-distance-dominant. Elvis revised this into two distinct views
with two distinct jobs, kept here per this repo's own convention for superseded entries.

**Map view, RESOLVED:** not ranked at all. Retrieval is bounded to the map's current viewport (the
visible boundary on screen), not a fixed radius, and updates live as the user pans, zooms, or changes
location, standard "search this area" map behavior. Within that viewport, everything in the user's
cohort shows, unfiltered by relevance and unranked by the scoring algorithm, since a map's job is
showing what exists in a place, not deciding what's most relevant. Position on the map is purely
geographic, not a ranking output.

**List view, RESOLVED:** this is where the scoring algorithm actually runs. When a user switches from
map to list within Explore, the same candidate set already visible on the map (viewport-bounded, same
cohort) gets scored and ordered by the full weighted formula below, geo-distance-dominant the way it
was originally scoped, with the other signals as tie-breakers among similarly-close results.

**Practical effect:** the recommendation algorithm this whole doc describes is not really "how Explore
decides what to show," it is "how Explore's list view orders what the map has already decided is
visible." The map's job (what exists here, in my cohort) and the algorithm's job (what's most relevant
to me, ordered) are cleanly separated, not the same system doing both.

**Deferred, not decided:** whether the map view's "same cohort only" rule loosens once a city is
confirmed dense enough (matching the list view's cohort signal softening), or stays a permanent property
of the map regardless of density. Elvis deferred this explicitly, revisit once the general softening
behavior itself is confirmed.

Home feed reuses the same underlying signal set and scoring function as Explore's list view, weighted
differently, interest and cohort more heavily weighted than distance. One scoring implementation with
different weight configs across home feed and Explore's list view, not separate systems.

## Feedback logging, a baseline requirement regardless of ranking sophistication

RSVPs, check-ins, dismiss and skip actions, shares, and tag clicks should be logged from day one, even
though the rule-based scoring function above does not consume any of it yet. This is what makes a
future learned ranking model possible without months of catch-up once there is enough real interaction
data to train on. Treated as infrastructure, not a feature, should not wait for the ML phase to start.

## Robustness roadmap and day-1 sequencing, RESOLVED 2026-08-26

Elvis asked what else should be considered to build a robust recommendation system, and what belongs on
day 1 versus later. Several real gaps surfaced that were not previously covered in this doc: impression
and position logging (not just action logging), a way to test changes before trusting them, resistance
to gaming the new-host boost and the avoid-signal, deletion handling for inferred profiles, negative
feedback suppression beyond single-item dismissal, output diversity, and a couple of non-functional
concerns (latency once embedding similarity is live, session-stable ordering).

**Day 1, RESOLVED: basic experimentation capability.** Elvis's explicit priority. Concretely, a way to
randomly bucket users into groups per experiment (a control group and one or more test groups), tag
which bucket a given session falls into, and log outcomes by bucket, not a full experimentation
platform, just enough to compare before-and-after on a real metric rather than tuning weights by feel.
This is what makes the "tune weights after launch" plan (Not yet decided, above) an actual measured
process instead of guessing. Needed before the post-launch weight-tuning pass, not after it.

**Deferred, explicit tradeoff acknowledged: impression/position logging and deletion handling.**
Sequenced after experimentation capability, Elvis's own call. Worth restating the tradeoff already
flagged for the record: impression and position data cannot be reconstructed retroactively once
launched without them, so choosing to sequence this after experimentation capability is a deliberate,
informed choice, not an oversight, kept here as the record of that choice.

**Anti-gaming, REVISED 2026-08-26: account integrity, not a separate rate-limiting system.** First
raised as a candidate day-1 build (rate limits and anomaly detection on signal-contributing actions).
Elvis's actual answer addresses the same risk a different way, through account-model integrity rather
than a bolt-on detection system, kept here per this repo's own convention for superseded framing.

**Current resolution:** one personal account per user, enforced initially through phone-number
uniqueness (phone verification is already required per DEC-011), with a move to ID verification planned
eventually for stronger enforcement. A user may create and own multiple business/Organization accounts,
but every Org account is tied to and traceable back to a specific personal user account, not anonymous
or freely creatable. Ratings and reviews are already restricted to checked-in attendees only (DEC-014),
reaffirmed here specifically as an anti-gaming mechanism, not just an authenticity one: it substantially
raises the cost of review-bombing, since it requires physically attending an event, not just creating an
account.

**Residual risk, flagged, not solved here:** phone-number uniqueness is a real deterrent, not an
absolute one (a determined actor can obtain multiple numbers), which is exactly why ID verification is
already the planned eventual hardening step, not treated as sufficient forever. This account-integrity
approach is the primary defense at launch, replacing rather than complementing a separate detection
system, a real and deliberate scope choice, not an oversight.

**Near-term and later items, captured so nothing raised gets lost, not designed in this pass:**
negative-feedback suppression by content type (not just excluding the one dismissed item), a diversity
pass on the final ranked list (avoiding a monotonous feed of near-identical results), a lightweight
"why you're seeing this" explanation label, and formal offline evaluation metrics (the kind that need
real scale to compute meaningfully, bucketed with the rest of the future signal roadmap). Two
non-functional notes worth keeping in mind, not new work: a latency budget once embedding similarity
(a real per-request cost) is live, and keeping a user's feed order stable within a session rather than
visibly reshuffling on every refresh.

## Illustrative scoring walkthrough, added 2026-08-25

Elvis asked to review the scoring mechanics in detail. This section is a concrete example so the
formula is reviewable, not a locked specification. The weight numbers here are illustrative only, real
calibration is a post-launch tuning pass against real usage data, per the open item above.

The ranking stage computes one weighted score per candidate, after retrieval has already narrowed the
full catalog down to a realistic candidate set:

`score = w1*tag_overlap + w2*cohort_match + w3*recency + w4*geo_distance + w5*popularity + w6*social_proximity + w7*new_host_boost`

Each signal is normalized to a 0 to 1 range before weighting, so no single raw unit (kilometers, a fill
count) can dominate just because of its scale.

**Worked example.** Sujin, 22, a self-declared student in Seoul, tags: hiking, coffee, photography.
Cohort: (Seoul, university-affiliated), per the override resolved in
`community-segmentation-2026-08-25.md`. Two candidate events under consideration:

- Event A, "Sunrise hike and coffee," hosted by a student club (also Seoul, university-affiliated),
  3km away, tags hiking and coffee, 18 of 20 spots filled, happening in 2 days, host has run 5 past
  events.
- Event B, "Networking mixer for young professionals," hosted by someone in the general 30s cohort
  (not university-affiliated), 1.5km away, tags networking and professional, 2 of 30 spots filled,
  happening in 5 days, host's first event.

**At launch, before Seoul is manually confirmed dense enough:** Event B never reaches the scoring stage
at all. It fails the retrieval-stage cohort filter (different cohort from Sujin's), so it is excluded
before ranking runs, full stop. Sujin's launch feed only ever considers candidates already inside her
own cohort, Event A among them.

**Once Seoul is confirmed dense enough and cohort softens back into a ranking signal,** both events
would reach scoring, illustrated below:

| Signal | Illustrative weight | Event A | Event B |
|---|---|---|---|
| Tag and keyword overlap | 0.25 | 0.65 (2 of 3 tags shared) | 0.0 (no shared tags) |
| Cohort match | 0.20 | 1.0 (same cohort) | 0.15 (different cohort, not zero, soft weighting not a wall) |
| Recency/urgency | 0.15 | 0.85 (2 days out) | 0.55 (5 days out) |
| Geo distance | 0.15 | 0.55 (3km) | 0.70 (1.5km, closer) |
| Popularity | 0.10 | 0.80 (90 percent full) | 0.10 (barely filled) |
| Social proximity | 0.10 | 0.0 (no mutuals, illustrative) | 0.0 |
| New-host boost | 0.05 | 0.0 (established host) | 0.90 (brand new host) |
| **Weighted total** | | **0.65** | **0.27** |

Event A still ranks well above Event B, correctly, since it is genuinely more relevant to Sujin on tags,
cohort, and urgency, even once both are eligible to be scored at all. The new-host boost gives Event B a
real lift for being a first-time host's event, but it is a nudge, not an override, it cannot pull an
irrelevant result above a relevant one. It is designed to matter in a closer contest, two events
similarly relevant to a given user where one host is established and one is brand new, not to override
actual relevance.

For explore, the same formula runs with `w4` (geo distance) raised substantially so distance dominates,
and the remaining signals act mainly as tie-breakers among similarly-close results, rather than being
able to pull a far-away result above a near one the way tag overlap can inside the home feed.

## Beyond the launch formula, RESOLVED 2026-08-25: one global formula now, learned per-user weights later

Elvis asked whether the launch formula is permanent, and whether different users could ever have
different weights, for example one person caring more about who's going, another caring more about
location. Both real, worth documenting explicitly.

**Confirmed:** the weighted formula in this doc, with one global set of weights applied to every user,
is the launch state only, not the long-term design. It stays a single global formula at launch, no
per-user or per-cluster variation yet.

**Future phase, RESOLVED:** document now, revisit later, per-user learned weighting in the direction
Netflix, YouTube, and Spotify are publicly known to use, learned embeddings that encode an individual's
taste, from which personalized weighting emerges from the model rather than being hand-maintained as an
explicit weight vector per person. This is different from, and more sophisticated than, either of the
lighter-weight alternatives that came up while discussing this (an explicit user-set preference control,
or a small number of shared cluster-level weight profiles); those were surfaced as real options but not
chosen as the direction to pursue, kept here as a record of what was considered.

**Why not now:** a reliable per-user learned weighting needs real individual interaction history per
person to learn from, the same cold-start constraint driving the rest of this doc, just applied at the
individual level instead of the platform level. Not viable against launch-scale data.

**How this would actually work when it's time:** not a rewrite of the scoring approach, an extension of
it. The two-stage retrieval-then-ranking architecture already exists specifically so a learned model can
slot into the ranking stage without a rebuild, see Architecture above. When there's enough logged
interaction data (from the day-one feedback-logging pipeline), the hand-crafted signals in this formula
become input features to that model rather than being replaced outright, and the model learns how much
each signal should matter for a given user from their actual behavior, the practical meaning of
"different weights per user" in a real production system, not a literal per-person spreadsheet of
coefficients.

## Research grounding, well-known concepts this design draws on

Added for reference, not new decisions. What's built here is a hybrid recommender: content-based
filtering now (tags, extracted keywords, distance, recency), architected to blend with collaborative
filtering later ("users like you also liked X") once there's real behavioral data. The launch-time
absence of that data is the formally-named cold-start problem, split into user cold-start (a new person
with no history, mitigated here by onboarding tags and text keywords) and item cold-start (a new event
with no engagement, mitigated by the new-host fairness boost). That boost is itself an instance of the
exploration-exploitation tradeoff, formally studied as multi-armed bandit problems, worth knowing if it
ever needs to become adaptive rather than a fixed decay curve. The group-dynamics work in
`group-dynamics-2026-08-25.md` sits inside an academic subfield called group recommender systems, which
studies how to score an item for a group rather than one person. More generally, this design sits on the
implicit-versus-explicit feedback distinction (RSVPs and dwell time versus ratings and thumbs up/down,
both listed above) and touches fairness-aware ranking, the broader research area behind preventing a
recommender from entrenching popularity bias over time, which is exactly what the new-host boost guards
against at a smaller scale.

Per-user learned weighting (above) is what Netflix and YouTube are publicly known to do through learned
per-user embeddings, and what Spotify is publicly known to use for Discover Weekly, all in the same
matrix-factorization and deep-learning recommender family this design is already headed toward. A
related, more lightweight technique worth knowing by name is the contextual bandit, a family of
algorithms (LinUCB, from a well-cited Yahoo research paper on personalized news recommendation, is the
best-known example) that maintain adjustable per-user weight coefficients updated online as that person
interacts, a middle ground between one global formula and a full deep model, real prior art if a lighter
personalization step ever becomes worth revisiting before the full learned-embeddings version.

## Not yet decided, deliberately parked

- Exact per-signal weights. Not locked without real usage data; expect this to be a tuning pass after
  launch, not a one-time decision now.
- Exact new/low-history boost decay curve and magnitude.
- Whether moments surface inside the home feed at all, or stay on profile and event pages only. Not
  addressed in this pass.
- Whether the Sunday Deck editorial bridge's "turn off" condition reuses the same density threshold as
  community segmentation's cohort-weighting relaxation, or needs its own separate number.
- Whether cohort match actually reverts to a ranking signal once a city softens, or is dropped from the
  algorithm at that point, see the same open item in `community-segmentation-2026-08-25.md`.
- Whether the Explore map view's cohort restriction loosens once a city densifies, or stays permanent
  regardless of density. Explicitly deferred by Elvis.
- Exact embedding model/provider choice, and exact tag-extraction prompt design, are implementation
  detail for Deepak, not specified here. Method is resolved (LLM-based extraction, a stored embedding
  per item), the specific model/vendor is not.
- Cost model for the embedding and tag-extraction calls, flagged but not built in this pass, worth doing
  before committing, similar to the earlier media infrastructure cost model.
- Exact shape of the day-1 experimentation capability (bucketing method, how many concurrent experiments
  it needs to support) is not specified, an implementation detail once Deepak scopes it.
- Timing for the move from phone-number uniqueness to ID verification is not specified, "eventually,"
  not tied to a phase or trigger condition.

## Flags for Deepak, implementation, not decided here

- Retrieval query needs to run before ranking for performance at scale (geo radius, time window, city,
  excluding dismissed/RSVPed), not score the full catalog per request. The cohort hard filter (above)
  belongs in this same retrieval query at launch.
- Interaction-logging pipeline (RSVP, check-in, dismiss/skip, share, tag click) is a day-one
  infrastructure requirement, independent of which ranking approach ships first.
- Needs a per-event or per-host low-history indicator (an engagement count or similar) to drive the
  new-host fairness boost, decaying as real signal accrues.
- Needs a per-event "featured" flag reserved for the Sunday Deck editorial bridge, for whenever that
  surface is built. Who can set it (a host-manager role versus Aakash/Elvis directly) is not decided
  here, an ownership question, not a technical one.
- Explore and home feed should share one scoring function/signal implementation with different weight
  configs, not two separate systems, to avoid drift between them over time.
- Needs a keyword-extraction step for title and description text, and a place to store both a user's
  explicit tags and their evolving, partly-inferred keyword profile, likely the same underlying
  mechanism as the hidden internal keyword layer above, applied to the user entity specifically.
- Hidden/internal keyword and tag storage needs to exist for all four entity types (ideas, events,
  moments, users), plus a lightweight admin view to inspect it, per the internal-visibility resolution
  above.
- See `group-dynamics-2026-08-25.md` for the group-composition signal's own implementation flags,
  including its dependency on a general user-blocking feature that is not designed in this doc.
- Map view needs a live viewport-bounded query (the map's current visible boundary, not a fixed radius),
  re-querying as the user pans, zooms, or changes location. Standard "search this area" map pattern.
  Debounce/throttle behavior for how often this re-queries during continuous map movement is an
  implementation detail, not specified here.
- Map view's candidate set should be retrievable without running the ranking stage at all, since it is
  not scored, only list view invokes the ranking stage on that same candidate set.
- Needs vector-capable storage for embeddings (a vector column/index on the existing database, or a
  dedicated vector store), plus an LLM API integration for the tag-extraction step, both triggered on
  item create/edit.
- Needs a periodic batch job (not real-time) that recomputes each user's embedding from the embeddings
  of content they have positively engaged with, consuming the day-one interaction-logging pipeline.
- Needs a lightweight admin tool to inspect embeddings indirectly (nearest-neighbor lookup, "show items
  most similar to this one") since the raw vector values are not directly readable the way tags are.
- Needs an experimentation/bucketing capability (day-1 priority): assign users to a control or test
  group per experiment, persist that assignment, and tag logged outcomes with the bucket, so a weight or
  algorithm change can be measured, not just deployed on faith.
- Needs a phone-number uniqueness constraint enforced at the account layer (one personal account per
  phone number), and every Organization account needs a traceable owner reference back to a specific
  personal account, not created independently of one. Both are platform/auth-layer requirements that
  happen to double as this algorithm's primary anti-gaming defense, not purely an algorithm concern,
  touches DEC-011 as well as this doc.
