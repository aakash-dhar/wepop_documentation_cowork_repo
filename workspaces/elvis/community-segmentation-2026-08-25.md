# Community segmentation strategy, 2026-08-25

> Elvis workspace working file. Raised 2026-08-25, alongside the recommendation-algorithm discussion
> it turned out to be closely tied to. Fully resolved same day via a four-question round.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Elvis's own framing: a city's very first users can be extremely different people. A college student
joining in Seoul and a man in his 40s joining around the same time would confuse each other about who
the app is for if surfaced together with no structure. Rather than ignoring one cohort in favor of the
other, keep them apart early on and combine as the app grows.

This is a cold-start liquidity problem common to multi-sided marketplaces: too few users per segment
to feel alive if split too aggressively, but a diluted, mixed-identity first impression if not split at
all. The closest real comparable is Facebook's own cold start, opened one college network at a time,
merged network by network as each grew dense enough, and eventually removed the walls entirely.

## Mechanism, REVISED 2026-08-25: hard filter at launch, softens once a city is dense enough

First resolved same day as pure soft ranking (cohort as one weighted signal, never a wall). Elvis
revised this once the recommendation algorithm's scoring was being reviewed in detail: at launch, same
cohort is a must, applied as a hard filter during retrieval, before scoring ever runs, not as one input
among several that a strong enough tag or recency match could still overcome. Kept here as a record of
the original call and why it changed, per this repo's own convention for superseded entries.

**Current resolution:** at launch, cohort match is a retrieval-stage hard filter, a candidate outside a
user's cohort is excluded before ranking, not merely down-weighted. There is still one single pool of
events, ideas, users, and moments underneath, nothing is partitioned at the data or infrastructure
level, but what a given user's retrieval query pulls back is restricted to their own cohort while a
city is thin. Once a city is confirmed dense enough (see the merge trigger below), the working
assumption is that cohort match transitions from a hard filter back to a weighted ranking signal, the
original soft design, rather than disappearing from the algorithm entirely. Elvis did not explicitly
confirm this transition point when revising the mechanism, flagged here rather than assumed silently,
worth a direct confirmation next time this comes up.

## Follow-graph exemption, RESOLVED 2026-08-26 (landed via the live 2026-08-26 team sync, synced here)

Not raised in this workspace originally, this came out of the live 2026-08-26 team sync (Elvis, Aakash,
Deepak) and landed directly as a change-history note on DEC-019 and DEC-020 in `shared/DECISIONS.md`.
Recorded here to keep this file in sync with the source of truth, not as a new decision made in this
session.

Elvis's own clarification on that call: the launch cohort hard filter should not apply to people you
already follow. If you follow someone outside your own cohort (his example: a user's mother, older and
not in college), her events should rank higher, not be hidden, because the follow relationship already
implies you know each other and want to see their activity.

**Current resolution:** a followed user's content is exempt from the DEC-019 cohort hard retrieval
filter. Instead of being excluded pre-scoring like any other out-of-cohort candidate, it is pulled into
the candidate set through the existing social-proximity ranking signal (w6 in the recommendation-
algorithm scoring formula) and ranked on that basis. This does not change the filter for anyone you do
not follow, it only carves out an exception for content from people you already have a direct
relationship with.

**Relationship to the hard-filter mechanism above:** the two are not in conflict. The retrieval stage
still excludes out-of-cohort candidates by default; the follow graph is a second, independent input into
that same retrieval query, unioned with the cohort-filtered set rather than replacing it. A user's
candidate pool becomes (their own cohort) union (people they follow), then ranking runs over that
combined pool as before.

## Cohort basis, RESOLVED 2026-08-25: a composite of life-stage and geography

Not a single axis. A cohort is effectively (city, age/life-stage bucket) together, not age alone and
not city alone. This matches Elvis's own Seoul example directly: the split that mattered there was
age within one city, not age in general. University-affiliated users are pulled out of this general
basis into their own cohort at launch, see below.

## Merge trigger, REVISED 2026-08-25: manual review at launch, automate later

First resolved same day as fully automatic (an active-user count crossing a set threshold triggers the
relaxation with no manual step). Elvis revised this in the same pass as the mechanism change above,
kept here per this repo's own convention for superseded entries.

**Current resolution:** at launch, whether a city has grown dense enough to loosen its cohort filter is
a manual, PM-reviewed call, not an automatic threshold check. The intent is to automate this later with
real logic and rules once there is enough operating experience to define the threshold with confidence,
not to keep it manual forever. Applies identically to the university-affiliated cohort, which already
shares the same trigger as the general age/geo cohort.

## Cohort assignment and the invite-first model, REVISED 2026-08-25

First resolved same day as "a new user inherits their inviter's cohort," consistent with the
invite-first model already clustering similar people through invite chains. Elvis revised this before
moving on to the algorithm discussion, kept here as a record of the original call and why it changed,
per this repo's own convention for superseded entries.

**Current resolution:** no inheritance step at all. Every user's cohort is examined independently,
computed from that user's own profile signals (their own city, their own age/life-stage bucket), not
from whoever invited them. This is a simpler rule than inheritance, and it removes the open question
below about how a waitlist-sourced (non-invited) user would be assigned a cohort, since invite status
no longer matters to the calculation either way.

## University affiliation cohort, RESOLVED 2026-08-25: a distinct, overriding cohort at launch

Elvis's own addition, raised after the algorithm scoping was first delivered: at launch, anyone
affiliated with a university should be specifically separated into their own cohort, not folded into
the general age/geo basis above.

**Affiliation signal, RESOLVED:** any of three signals qualifies a user as university-affiliated, not
just one. Self-declared at onboarding (a "current student at [school]" field), school email domain
verification, or membership in an Organization profile that is itself flagged as university-affiliated
(a university club Org profile). A user needs only one of the three to count.

**Override, RESOLVED:** university affiliation overrides the general age/geo cohort at launch. A
university-affiliated user's cohort becomes (city, university-affiliated), full stop, not further split
by their own age bucket, since students in one city are already a fairly homogeneous life-stage on
their own.

**Granularity, RESOLVED:** one combined university-affiliated cohort per city, not split further by
specific school. All university-affiliated users in, for example, Seoul share one cohort regardless of
which university they attend.

**Merge behavior, RESOLVED:** the university cohort relaxes on the same per-city density threshold as
the general age/geo cohorts, not a separate trigger or number.

## Not yet decided, deliberately parked

- Whether cohort match actually softens back into a ranking signal once a city is manually confirmed
  dense enough, versus being removed from the algorithm entirely at that point. Assumed to soften,
  matching the original design, but not explicitly confirmed, see the mechanism section above.
- What the manual review at launch actually looks at (an active-user count, a qualitative read, event
  supply, some combination), and who owns making that call city by city. Presumed to be a PM
  responsibility (Aakash) given the "manual, PM-reviewed" pattern already used elsewhere in this repo,
  not confirmed.
- What the later automated logic and rules should look like once there is enough operating experience
  to define them. Explicitly deferred, not a launch question.
- Whether a user can ever explicitly override or change their own computed cohort, for example someone
  whose age bucket does not match the peer group they actually want to see content from.
- Which specific school email domains count toward verification in each market, and what marks an
  Organization profile as "university-affiliated" versus any other club or business account. A
  compilation task, not a design decision.

## Flags for Deepak, implementation, not decided here

- Cohort is a composite value per user (city plus age/life-stage bucket, or city plus
  university-affiliated when that override applies), either stored at signup or computed at
  query/ranking time from existing profile signals, not decided which.
- Cohort computation needs to check university affiliation first (any of the three qualifying signals)
  and only fall back to the general age/geo basis when none apply.
- At launch, cohort is applied as a hard filter in the retrieval query (exclude anything outside the
  user's cohort), not as a scored ranking input, a real difference from how the recommendation
  algorithm doc originally described this signal, that doc has been updated to match.
- The per-city manual review needs a lightweight interface or process for whoever makes the call (a
  PM dashboard, a spreadsheet, a Slack decision logged somewhere), not real-time automated logic yet.
  Building the automated version is explicitly later work, do not over-invest in tooling for the manual
  phase.
- School email domain verification needs a maintained list per market (Korea and the US differ
  structurally here), and Organization profiles need a boolean or similar flag marking
  university-affiliation, set at Org profile creation or verification.
- No new data model entity needed for this by itself, since the mechanism is a ranking signal, not a
  partition. It becomes a real requirement on whatever the recommendation algorithm's feature/signal
  layer looks like, tracked there instead of duplicated here.
- Retrieval query needs to union the user's cohort-filtered set with content from users they follow, per
  the follow-graph exemption above, not just apply the cohort filter alone. This is stated directly in
  DEC-019's change history as a note to Deepak already, repeated here so this file stays the single place
  to look for cohort mechanics.
