# Proposed decisions from elvis - for merger review

> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Pending

Three proposals. The first is a **correction to DEC-034** and should be read before the other two, which
depend on it.

DEC-034 landed on 2026-08-31 carrying a badge-plus-weight model that later work the same day withdrew. The
merge and the revision crossed: the merger reviewed the proposal as it stood at 15:02, and the revisions
were committed at 18:52. No error on either side, but `shared/DECISIONS.md` and the working file currently
disagree, and this queue closes that gap.

Working detail for all three: `workspaces/elvis/ratings-checkin-2026-08-31.md`.

## DEC-NNN (PROPOSED) - CORRECTION TO DEC-034, HIGHEST PRIORITY IN THIS QUEUE
**Date:** 2026-09-01
**Proposed by:** Elvis
**Source:** `workspaces/elvis/ratings-checkin-2026-08-31.md`, superseding DEC-034
**Topic:** Withdraw DEC-034's badge and scoring weight; stars are 1 to 5; display gate is 3 ratings
**Type:** Product + Technical
**Decision:** DEC-034's verification badge and feedback scoring weight are **withdrawn in full**. Check-in
awards no 참석 인증 badge, carries no scoring weight, and gates nothing; it produces an operational record
surfaced in analytics only. **Anyone who joined an event through the app may give feedback and post a Moment
once the event completes; that is the whole eligibility rule.** Two protections replace the weighting,
neither depending on check-in: a public star average displays once a host has **3 ratings** (not 3
*verified* ratings), showing event count and rating count only below that; and the internal recommendation
signal applies Bayesian smoothing toward the global mean, now unweighted, R = (C·m + Σrᵢ) / (C + n) with
C = 5. Separately, **stars run 1 to 5, not 0 to 5**, and an unrated field is NULL rather than 0.
**Why this correction exists, and it is nobody's error.** DEC-034 landed on 2026-08-31 at 15:02 from the
proposal as it stood when the merger reviewed it. Work later the same day (items #9 and #10 of the
phase-1/1.5 review) revised that proposal twice and then withdrew its central mechanism; those revisions
were committed at 18:52, after the merge. The merger merged what was in front of them. This proposal simply
brings `shared/DECISIONS.md` back into agreement with the working file.
**Reasoning, the three findings that undid the weighting.** (1) Check-in ceased to be universal: it now runs
only on ticketed events and on capacity-limited events whose host enables it, so at an open event nobody can
be verified and every rating would weight 0.4 permanently, leaving a host who runs only open events with
**no public star average ever**, including an org whose track record is a cold-start trust signal under
DEC-024. (2) A three-state fix (verified / unverified / axis-not-applicable) solved that but introduced a
perverse incentive: a host who turned check-in **on** would have some ratings discounted to 0.4 while a host
with no check-in had all ratings at full weight, so the host who did more to verify attendance reached the
display gate *later*. (3) The machinery was nearly inert at launch anyway, since ticketing is not live until
phase 1.5 (DEC-010) and the individual paid tier is HELD (DEC-018), so it would have served org-tier capacity
events and almost nothing else. On the star scale: a 0-star rating is not expressible in a star widget
(tapping the first star yields 1, and not tapping is indistinguishable from skipping), DEC-014 makes every
field skippable so a distinct sentinel for "did not answer" is required, and a 0 entering the average would
count in the denominator and drag the numerator, penalising every host whose attendees skipped feedback.
**Accepted cost:** a user who joined and never attended is now indistinguishable from a real attendee when
rating. Judged acceptable because the motive is thin at a free casual meetup, the 3-rating gate stops one
person establishing a public number alone, smoothing absorbs a single outlier, and a host can report a rating
from someone who was not there, making it a moderation rather than a scoring problem.
**Impact:** Supersedes DEC-034's badge and weighting provisions and its "0 to 5 stars" reading of DEC-014.
DEC-034's other provisions stand unchanged (positive-only peer tap, no bulk-follow, check-in decoupled from
eligibility). **Two `wepop-scope-matrix.md` rows need correcting**, both currently describing the withdrawn
model: the "Ratings + post-event feedback" row states "verified feedback weighted 1.0, unverified 0.4 ...
public average gated at 3 verified", and the "QR check-in (verification badge + weight)" row is titled for a
badge that is not shipping and describes check-in as granting a weight. Deepak flags: no weight column, no
badge surfaces, aggregates recomputed from rows rather than accumulated, and
`attendance(event_id, user_id, method, verified_at, approved_by)` **stays a first-class transactional table**
so that reinstating weighting later is a config change plus a runnable backfill rather than a rebuild, which
is the condition making this a deferral rather than a deletion.
**Relates to / Supersedes:** Supersedes DEC-034 in part. Prerequisite for the check-in proposal below.
Interacts with DEC-018 (min-sample precedent) and DEC-020 (new-host boost, which the smoothing protects).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-31
**Proposed by:** Elvis
**Source:** `workspaces/elvis/ratings-checkin-2026-08-31.md`, phase-1/1.5 review item #10; reverses the
handoff spec's §4.2 check-in direction
**Topic:** Check-in reverses to host-scans-attendee, becomes an operations tool only, applies to a defined
subset of events, self-service mode deferred
**Type:** Product + Technical
**Decision:** Phase 1 follows the ticketing industry standard: **the host scans the attendee**, reversing
handoff spec §4.2, where the host displays a rotating QR that attendees scan. **Check-in produces an
operational record only**: it is recorded and surfaces in analytics, awards no badge, carries no scoring
weight, and gates nothing. The 참석 인증 badge is removed and does not ship. **Check-in is not universal**,
and applies as follows: required on ticketed events; a host choice on capacity-limited events via a
"Check-In Required" toggle shown when capacity is set, **available to every host, free and paid**; and not
available in phase 1 on open events with neither ticketing nor capacity. What is paid is the **analytics**
built on check-in data, not the ability to record it, which sits inside DEC-018's existing split of
per-event operational numbers free and aggregate rollups paid. Attendees scanning a displayed QR or typing a
numeric code becomes **self-service mode, deferred to a later phase**, possibly paid.
**Attendance data is retained deliberately for later use.** No-show and punctuality behaviour is tracked
from launch so that users who consistently show up, and show up on time, can eventually be incentivised and
rewarded; nothing acts on it in phase 1. Attendance is recorded as **two independent axes, not one enum.**
*Observed attendance* exists only where check-in ran, with four states: attended (host-scanned or
self-attested and host-approved), claimed-unconfirmed (self-attested, host never acted before §4.3's 7-day
auto-close), no-show (joined, then nothing), and **not tracked** (the event ran no check-in, a property of
the event rather than the person). Neither "not tracked" nor "claimed, unconfirmed" may collapse into
no-show. *Self-reported intent* exists on **every** event including those with no check-in: as the event
approaches the attendee receives a notification, an in-app pop-up, and a button on the event detail page
offering on my way / running late / cannot make it. Because check-in coverage in phase 1 is narrow while
self-report reaches every event, **self-report is the primary reliability source at launch and check-in the
secondary one.** The host check-in timestamp is recorded but is **not an arrival time**, since a host who
batch-scans twenty minutes in makes everyone look late.
**Design rule attached to the data, and it must hold from day one:** declining in advance must not be scored
like a silent no-show. Someone who taps "cannot make it" has given the host what they need, so the host can
release a spot or stop waiting; someone who says nothing has not. If both resolve to "did not attend", the
product teaches users that warning the host costs the same as ghosting and they will stay silent, defeating
the feature. How it is weighted is a later decision, but the two states must stay distinct in the data now
or the choice is gone.
**Reasoning:** Staff scanning the attendee is universal in ticketing, and while the stated operational reason
is throughput, the structural reason is enforcement: a gate must be able to deny entry, and denial only works
if the venue controls the decision, since an attendee who scans their own phone has already walked in.
WePop is committed to paid ticketing (DEC-010 puts payment provisions in the phase-1 codebase, TASK-036 flags
ticketing as the largest technical scope), so building the direction that supports enforcement now avoids
inverting the whole attendance surface later. Check-in is not universal because a host of an open event may
not want the hassle of checking people in, or of asking their attendees to do it, and should not have to.
Reducing check-in to an operational record follows from that: once it is optional and rare, a badge and a
scoring weight hanging off it created more problems than they solved (see the DEC-034 correction above for the
three reasons), and check-in becomes honestly what it now is, the door at a ticketed event and a headcount at
a capacity event. Self-service is deferred because it serves the low-stakes case that no longer needs it.
Two problems were being conflated and are now separated: *rating integrity* (someone who did not attend
rates the event), whose mitigation is withdrawn as an accepted cost, and *attendee reliability* (someone
joins and does not show, or shows late, and the host has planned around them), which is a behavioural
problem rather than an opinion one, is significant in the event space, and is what the retained attendance
data is for.
**Impact:** Corrects the scope-matrix row "QR check-in (required)" on two counts, since check-in is neither
required of all events nor load-bearing. Requires the DEC-034 correction filed above, since DEC-034 landed carrying the badge-plus-weight model this
proposal removes.
Removing the badge also dissolves a governance escalation that was about to be filed: paid-gating check-in
brushed against DEC-018's "never gate marketplace actions" rule and against I-16 ("a paid feature may not
degrade another user's experience"), because the party losing out was the attendee, who could never earn a
badge no matter what they did, purely because their host did not pay. With no badge there is no degradation
and nothing to escalate.
**Likely de-blocks L-3**: the 위치정보법 exposure attaches to the printed-poster mode, whose static token
needs a location radius to resist forgery, and printed posters exist to support attendee self-scan; with
self-scan deferred, the poster and its geofence defer with it and L-3 becomes a later-phase legal question
rather than a gate before P0. Confirm with DLG rather than assuming. Anti-forgery also simplifies: the
60-second rotating QR existed because a host-displayed code could be screenshotted and forwarded, and once a
host scans a person standing in front of them the host's own eyes are the strongest available control, so a
static per-attendee credential suffices; the handoff's rejection of SafeTix-class rotating attendee
credentials still holds for the reason it gave. The co-host `run_checkin` permission flag (§8.1) becomes more
useful, since a co-host can work the door at a larger event. Deepak flags: `attendance.method` must stay an
open discriminator, with phase 1 adding a host-scan method and the deferred self-service mode adding another
later, and nothing hard-coding the assumption that the attendee initiates; an event carries a boolean for
whether check-in runs, read by every consumer of the feedback weighting. **Naming correction worth
preserving:** the deferred mode is *self-service*, not offline, since it needs every attendee's device online
to submit; the genuinely offline-capable path is the ticketing one, where the host's device caches the roster
before doors and scans with no network. Building it later as "offline mode" on the attendee-scan design would
not work offline.
**Corrects an I-12 drafting error rather than requiring a carve-out.** The handoff §13 states I-12 as "no
mechanic may create a persistent peer rating of an individual that is **visible to anyone**". The 2026-08-29
replacement wording widened this to "whether visible or internal", which was not asked for and was wrong on
its own terms, since DEC-014 already permits an internal-only attendee signal in as many words ("attendee
thumbs are an internal recommendation signal only, never shown to anyone"). The widened version therefore
contradicted DEC-014, and it is the clause that would otherwise block retained no-show data. **Revert to the
visibility scope**, keeping the host carve-out: I-12 prohibits a persistent peer rating of a participant
*that is visible to anyone*; internal signals are permitted, and making one visible or using it to gate event
access is a separate decision requiring its own review. Retained no-show data then needs no exception, being
internal and never surfaced. An earlier reading that I-12 had been "carved out twice" and was eroding is
withdrawn: one of the two was this drafting error, not an erosion of principle. Also for the DLG register: a
reliability score is personal data about that person, the same character as L-1's peer affinity records, and
belongs in the same consult.
**Documentation gap this depends on:** self-reported intent (on my way / running late / cannot make it)
exists in Elvis's design files but is defined nowhere in this repo. The work is documenting it, not
designing it, but it is a real gap since engineering builds from the repo. Detail still to settle: whether
the host is notified individually or sees a roster view, whether "running late" carries an estimate, and
whether it can attach to a stop on a DEC-025 schedule.
**Future direction, noted not designed:** check-in on all event types including open ones, as *self*-check-in
where attending earns something concrete (Elvis's example: an open Valorant event where those who showed up
scan to receive an in-game virtual good). A real use case for the deferred self-service mode, dependent on a
rewards mechanic that does not exist under DEC-025's deferred gamification thread. Also possible later:
geo-location to establish actual arrival time, which would need its own privacy pass against DEC-016 and
DEC-012's no-forced-GPS stance and 위치정보법.
**Not resolved by this proposal:** what "surfaces in analytics" means concretely (which surface, per-event or
rollup); how and when no-show and punctuality data is eventually used, and whether any of it is surfaced to
users; and whether the claimed-but-unconfirmed state is visible to the attendee or the host nudged to resolve
the queue before it auto-closes.
**Relates to / Supersedes:** Reverses handoff spec §4.2. Depends on the DEC-034 correction filed above. Relates to DEC-010 and TASK-036 (ticketing), DEC-024 (capacity and waitlist).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-31
**Proposed by:** Elvis
**Source:** `workspaces/elvis/ratings-checkin-2026-08-31.md`, phase-1/1.5 review item #9
**Topic:** Feedback stays uniformly anonymous; 7-day edit and withdraw window; author-visible in profile
**Type:** Product
**Decision:** Post-event feedback is **uniformly anonymous**, with no option for a user to attach their name.
A user may **edit or withdraw their own feedback for 7 days after submitting it**, measured from submission
rather than from the event; after that, removal goes through moderation. A user can see all feedback they
have given via a menu entry in their profile ("My feedback / 내가 남긴 후기") listing what they wrote, which
event it was for, and whether the 7-day window is still open, with edit and withdraw living there.
**Reasoning:** Optional attribution would destroy anonymity for the people who used it: if most attendees
sign and a few do not, the few are no longer anonymous but identifiable as the ones with something to hide,
which on a ten-person event is close to naming them. It would also create pressure, since a host asking to
know who said what puts everyone in a position where declining reads as hostile. Structurally, anonymity is
currently doing the work that Airbnb needs double-blind simultaneous publication to do (Airbnb locks reviews
and publishes both sides at once specifically to prevent retaliation); WePop needs none of that machinery
because a host cannot identify a rater, and optional attribution trades that away for nothing. The signed
channel already exists and is the follow button, which DEC-014 deliberately places on the feedback screen
separated from the rating controls "because follow is a public act and rating is not". On the window: 7 days
from submission rather than from the event, because Airbnb's edit window works only by being tied to a review
period that *closes*, and §5.2 says WePop's feedback window never closes, so the same pattern would mean
"editable forever". Not indefinite, because ratings feed host reputation and the recommendation engine, so a
rating that can change forever means the aggregate never stabilises and it opens a coercion vector where a
host pressures someone months later to revise a score. 7 days also matches the self-attest auto-resolve
window in §4.3, giving the product one "we wait a week" period rather than two competing ones.
**Impact:** Deepak flags, one of which is easy to build wrong first: **weighted aggregates must be recomputed
from rows rather than accumulated as a running sum**, since an incremental aggregate is silently corrupted by
the first edit or withdrawal. And the **"My feedback" screen is the only place the author-to-feedback link
ever surfaces to a human** - private to that user, never to a host, never in an admin UI that could leak it,
never in an export; anonymity is doing structural work here and this linkage is the single point at which it
could be undone. The screen should slot into the profile three-tab restructure already scheduled in the
handoff's P1.1 wave rather than being added separately.
**Not resolved by this proposal:** whether an edited rating shows as edited to viewers or changes silently
within the window, and where feedback aggregates surface to the host and in what form.
**Relates to / Supersedes:** Extends DEC-014 and DEC-034 (as corrected above).
**Status:** Awaiting merger

---

## Landed

- **2026-08-31: eleven decisions landed** into `shared/DECISIONS.md` by the merger as **DEC-034 to DEC-044**,
  covering the 2026-08-29 handoff-spec intake batch (peer feedback positive-only and check-in decoupled,
  gender removed from the pre-join aggregate, avoid signal block-only, general user blocking as a phase-1
  baseline, event cover media caps, media retention tiered at a 6-month boundary) and the 2026-08-30 batch
  (Ideas lifecycle, event schedule, change notifications, completed-event deletion and detachment, host
  accountability). Sources: `handoff-spec-v0.9-intake-2026-08-29.md`, `ideas-lifecycle-2026-08-30.md`,
  `event-schedule-2026-08-25.md`, `host-accountability-2026-08-30.md`.
  **Note: DEC-034 landed pre-revision and is corrected by the proposal above.**
- 2026-08-28: five decisions landed as DEC-029 to DEC-033 (language preference storage, cohort formula,
  home-location mechanism, Explore country gate, apply-to-join quota).
