# Proposed decisions from elvis - for merger review

> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Pending

Thirteen proposals, in three batches.

**2026-08-29, six proposals** from the intake of `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx`.
All six arise from conflicts between that document and already-ACTIVE decisions; each conflict was
walked with Elvis on 2026-08-29 and resolved. Full working detail, including the resolutions not
filed here and the items still open, is in `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md`.

**2026-08-30, five proposals** from phase-1/1.5 review items #7 (Ideas lifecycle, closing the last
open thread of that item) and #8 (event schedule), plus a general change-notification rule that arose
from #8 but applies across events and ideas, and a host-accountability model that grew out of questioning
why a host would delete a finished event. Detail in `workspaces/elvis/ideas-lifecycle-2026-08-30.md`, the
2026-08-30 update section of `workspaces/elvis/event-schedule-2026-08-25.md`, and
`workspaces/elvis/host-accountability-2026-08-30.md`.

**2026-08-31, two proposals** from phase-1/1.5 review items #9 (ratings and post-event feedback) and #10
(QR check-in), taken as one pass. These also revise the 2026-08-29 DEC-014 amendment **in place**, before
merger, since check-in ceasing to be universal broke its two-state weighting; merge the revised version, not
a cached earlier reading. Detail in `workspaces/elvis/ratings-checkin-2026-08-31.md`.

## DEC-NNN (PROPOSED)
**Date:** 2026-08-29
**Proposed by:** Elvis
**Source:** `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` items A and B, amending DEC-014
**Topic:** Post-event feedback: peer feedback becomes positive-only, no bulk follow, check-in decoupled from
eligibility entirely, stars corrected to 1-5
**Type:** Product + Technical
**Decision:** DEC-014's star ratings on events and hosts are retained as merged (scale corrected to 1-5, see
below), including the
optional anonymous text and its everyone/host-only visibility toggle, and their feed into host reputation.
Three amendments. (1) Attendee-to-attendee thumbs up/down is replaced by a single positive-only tap; no
negative peer record is created anywhere, and no negative peer table exists in the schema. (2) The "follow
all" affordance is removed; individual follow taps only, nothing pre-selected. (3) Check-in is no longer a
gate on feedback or on Moment authorship. A user who joined an event that completed may do both.
**REVISED 2026-08-31, before merger, twice in one day; merge this version, not a cached earlier reading.**
The badge-plus-weight model this amendment originally proposed is **withdrawn entirely**. Check-in awards no
badge, carries no scoring weight, and produces an operational record surfaced in analytics only (see the
check-in proposal below). The 참석 인증 badge does not ship. **Anyone who joined an event through the app may
give feedback and post a Moment once the event completes; that is the whole eligibility rule.** Two
protections replace the weighting, neither depending on check-in: a public star average displays once a host
has **3 ratings** (below that, event count and rating count only, precedent being DEC-018's min-sample gating
for org analytics), and the internal recommendation signal applies Bayesian smoothing toward the global mean,
R = (C·m + Σrᵢ) / (C + n) with C = 5, which is unrelated to check-in and stays regardless.
**Also revised 2026-08-31: stars run 1 to 5, not 0 to 5**, and an unrated field is NULL rather than 0,
closing an item `conflict-review-2026-08-19.md` item 1 flagged as open and never resolved. A 0-star rating is
not expressible in a star widget (tapping the first star yields 1, and not tapping is indistinguishable from
skipping); DEC-014 makes every field skippable so a distinct sentinel for "did not answer" is required; and a
0 entering the average would count in the denominator and drag the numerator, penalising every host whose
attendees skipped feedback.
**Reasoning:** Bulk-follow destroys follow as a recommendation signal, which DEC-020 weights as social
proximity (w6); a one-tap bulk action makes that weight meaningless. Removing thumbs-down reflects Elvis's
stated principle that the product should focus on what to recommend rather than what not to recommend.
Decoupling check-in removes it as a single point of failure for the entire evergreen content layer: a host
who forgets to run check-in should cost their attendees nothing. On withdrawing the weighting: it was correct
while check-in was expected on every event, and three things then undid it. Check-in stopped being universal,
so at most events nobody could be verified and every rating would have weighted 0.4 permanently, leaving a
host who runs only open events with no public star average ever, including an org whose track record is meant
to be a cold-start trust signal under DEC-024. A three-state fix solved that but introduced a perverse
incentive, since a host who turned check-in **on** would have some ratings discounted while a host with no
check-in had all ratings at full weight, so the host who did more to verify attendance reached the display
gate later. And check-in is nearly nonexistent at launch anyway, because ticketing is not live until phase
1.5 (DEC-010) and the individual paid tier is HELD (DEC-018), so the machinery would serve a sliver of
events. The accepted cost is that a user who joined and never attended is now indistinguishable from a real
attendee when rating; judged acceptable because the motive is thin at a free casual meetup, the 3-rating gate
stops one person establishing a public number alone, smoothing absorbs a single outlier, and a host can
report a rating from someone who was not there, which makes it a moderation problem rather than a scoring
one. The smoothing constant protects DEC-020's deliberate new-host fairness boost, which a single early 2-star rating
would otherwise undo immediately, reproducing exactly the rich-get-richer dynamic DEC-020 was written to
prevent.
**Impact:** Supersedes DEC-014's attendee thumbs up/down provision, its "0 to 5 stars" scale, and its "QR
check-in becomes REQUIRED" impact clause. QR check-in remains phase-1 scope but is no longer load-bearing for feedback, ratings, or
recommendations; the scope-matrix row's "Load-bearing for ratings, reputation, recommendations, moments" note
needs correcting. DEC-023's avoid signal loses its data source as a direct consequence, handled in a separate
proposal below. Deepak flags: aggregates are recomputed from rows rather than accumulated, since an
incremental aggregate is silently corrupted by the first edit or withdrawal; and
`attendance(event_id, user_id, method, verified_at, approved_by)` **stays a first-class transactional table
rather than only an analytics event stream**, so that turning weighting back on later (if no-show ratings
become a real problem, or when ticketing makes check-in common) is a config change plus a runnable backfill
rather than a rebuild. That is the condition making this a deferral rather than a deletion, and it is the
same discipline already applied to `storage_tier`/`expires_at` on media and DEC-012's per-country age
thresholds: ship the data, leave the behavior off. The display threshold (3) and the smoothing constant
(C = 5) are starting points and not data-backed, carrying the same caveat DEC-018's media caps carried.
**Relates to / Supersedes:** Amends DEC-014. Interacts with DEC-020 (both the social-proximity weight and the
new-host boost) and DEC-018 (min-sample precedent). Forces the DEC-023 amendment below.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-29
**Proposed by:** Elvis
**Source:** `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item C, partially superseding DEC-017
**Topic:** Gender removed from the attendee-facing pre-join aggregate; host-facing aggregate retained
**Type:** Product / Safety
**Decision:** Gender is not shown to attendees pre-join in any form, including the aggregate ratio DEC-017
established. Hosts continue to see an aggregate on the event details page and in analytics. Gender never
appears on a per-person row in any accept/decline or selection UI. DEC-017's separate provision on individual
attendee photos is untouched: photos remain visible pre-join only between two users who mutually follow each
other in both directions, and a one-way follow never unlocks them.
**Reasoning:** An aggregate ratio on a small event is re-identifiable in practice, which DEC-017's original
reasoning did not weigh. The per-row prohibition addresses a different and sharper problem: the same data
that informs planning becomes a selection mechanism when it sits inside an accept/decline UI at the moment a
yes/no is made about a specific person, and it recreates on the supply side exactly the sorting DEC-006 and
DEC-017 exist to prevent on the demand side, with the added harm of silent rejection with no feedback and no
recourse. Hosts with a genuine balance requirement declare it at creation and it is enforced at join
eligibility, so nobody applies and is quietly rejected.
**Impact:** Partially supersedes DEC-017 (the gender-aggregate provision only; the photo provision stands).
Extends DEC-006. Introduces a new invariant, proposed as I-13 in the handoff spec's numbering: gender is never
displayed on a per-person row in any accept/decline or selection UI. Deepak flag: the pre-join aggregate
composition payload drops its gender field for attendee-facing requests but retains it for host-facing ones,
so this is a per-audience response shape rather than a stored-data change. Gender remains optional at signup
and purpose-limited to host aggregate planning, which is a stated-purpose requirement under PIPA and is
already flagged as L-2 in the handoff spec's legal register.
**Relates to / Supersedes:** Partially supersedes DEC-017. Extends DEC-006.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-29
**Proposed by:** Elvis
**Source:** `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item F, amending DEC-023
**Topic:** Avoid signal becomes block-only; positive affinity added as the constructive half
**Type:** Product / Technical
**Decision:** DEC-023's avoid signal runs solely off an explicit block. The soft, inferred half ("if a user
consistently rates another user low, down-weight events that person attends") is dropped rather than
deferred, since the thumbs-down mechanism it depended on is being removed. Running it instead on the absence
of a positive signal was considered and explicitly rejected. In its place, the positive peer tap feeds a
positive affinity ranking signal: events attended by people this user has tapped "또 만나고 싶어요" on are
boosted, sitting alongside DEC-020's existing social-proximity weight.
**Reasoning:** Elvis's stated principle, recorded because it is general and not specific to this feature: it
matters more to focus on what to recommend than on what not to recommend. Absence-of-positive is also
technically fragile as a proxy, since most attendee pairs at most events will never exchange an optional
low-uptake tap, so absence is overwhelmingly noise rather than signal. Recording the rejection matters
because absence-of-positive is the obvious repair a future reader will propose on noticing the avoid signal
has a single input; it was examined and declined, not overlooked. Flipping the polarity means DEC-023 does
not actually lose its attendee-level data source, it gains a usable one: the positive tap is precisely the
attendee-level feedback mechanism `group-dynamics-2026-08-25.md` flagged as missing.
**Impact:** Amends DEC-023. Closes DEC-023's flagged dependency on an undesigned attendee-level feedback
mechanism, in the positive direction only. Its other flagged dependency, a general user-blocking capability,
is closed by the proposal below. Look-alike host affinity stays parked as DEC-023 already had it. Deepak
flags: no per-user-pair negative rating history is needed or stored; block state and positive-tap history are
the only per-pair reads at ranking time.
**Relates to / Supersedes:** Amends DEC-023. Consequence of the DEC-014 amendment above. Interacts with
DEC-020.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-29
**Proposed by:** Elvis
**Source:** `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item G, resolving a scope-matrix flag
**Topic:** General user blocking confirmed as a phase-1 safety baseline, fully specified
**Type:** Product / Safety
**Decision:** General user blocking is phase-1 scope, in the earliest build wave. A block is bidirectional
and total: the blocked user's events, ideas, Moments, comments, and profile are mutually invisible across
every surface, including home feed, Explore, and comment threads. The scope of the block is stated to the
user at the moment they block, rather than left to be discovered.
**Reasoning:** The scope matrix already flagged this as "likely a phase-1 safety baseline, confirm," and
DEC-023 depends on it existing. Bidirectionality is the same reasoning DEC-017 used for mutual follows: a
one-directional block leaves the blocking user visible to the person they blocked, which inverts the
protection. Stating the scope at block time is required because a user who believes a block is broader than
it is will make safety decisions on a false premise.
**Impact:** Moves the scope-matrix row "General user-blocking capability" from later/proposed to phase 1, and
resolves the corresponding entry in the matrix's "Unbacked / needs a decision" section. Closes one of
DEC-023's two flagged prerequisites. Deepak flags: block state is checked at retrieval time on every
content-bearing surface rather than filtered at render, and block is a hard exclusion here even though
DEC-023 treats it as a heavy ranking penalty for the avoid signal; those are two different consumers of the
same state and both are intended.
**Relates to / Supersedes:** Resolves a scope-matrix open question. Prerequisite for DEC-023.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-29
**Proposed by:** Elvis
**Source:** `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item E, extending DEC-015 and DEC-018
**Topic:** Event cover media caps, a new surface distinct from Moment media
**Type:** Product
**Decision:** DEC-015's and DEC-018's Moment media caps stand unchanged (10 items free / 20 individual-paid /
50 at org-paid events, most-generous-wins, video 15s free and 30s paid, 720p H.264). Event cover media is a
separate surface with its own caps: up to 5 items total, photos and videos in any mix, with video capped at
15s for free accounts and 30s for paid accounts of either type, individual or organization.
**Reasoning:** The 15s-free / 30s-paid split matches the split DEC-018 already established for Moment video,
so one rule governs both surfaces rather than two. A 5-item cover is a cover, not a gallery; the Moment
composer remains the place volume belongs, which keeps the single-uploader and single-moderation-queue
architecture intact.
**Impact:** Adds a scope-matrix row for event cover media, which has no home today. Deepak flag: the
per-clip technical ceiling of 50MB is compatible with these caps (30s at 720p and roughly 3 Mbps is about
11MB) and functions as an abuse and corruption guard rather than a product limit; client-side compression
before upload is mandatory rather than an optimization.
**Video length reviewed and retained, 2026-08-29.** Whether to cut clip caps to 5-10s free and 20s paid
across the app was raised and examined on cost grounds. The numbers do not support it: at 720p and roughly
3 Mbps a 15s clip is 5.6MB, and holding an entire free-tier Moment of video (10 clips, 56MB) for the whole
6-month retention window costs about half a cent at R2 rates. Clip length is a linear multiplier on the video
subset only; the actual cost levers in order of magnitude are the retention window (just halved, saving far
more than any length change), item count, and transcode compute, which is what
`freemium-model-2026-08-19.md` already concluded when it said the real lever is retention rather than the
price point. The product cost of short caps is meanwhile high: 15s is the established floor for social video
because shorter clips stop being usable for a toast, a performance, or a room reaction, and a cap that makes
a feature unusable suppresses usage rather than converting to paid, which costs content density this
product's cold-start problem depends on. A 5s free cap would also edge against DEC-018's own three-bucket
rule (quota-gate personal expression, never gate core functionality).
**Recommended addition, not yet confirmed: a total-video-duration cap per Moment.** The real exposure is not
the free tier's 2.5-minute worst case but the paid tiers': 20 items at 30s is 10 minutes in one Moment, and
50 items at 30s at an org-paid event is 25 minutes. That is a moderation problem before it is a storage
problem, since §12.5 of the handoff spec sizes the moderation lane at two people alternating on-call and a
queue item taking 25 minutes to watch breaks that staffing model whatever it costs to store. The handoff spec
already proposes this mechanism and gives the right reason ("when raising the length limit, cap total
duration per Moment rather than per clip, so moderation burden stays bounded"); it is simply not carried into
the numbers. Suggested starting values: 150s total free (identical to the current worst case, so nothing
changes in practice for free users) and 300s total for paid and org-paid, cutting the 10-minute and
25-minute worst cases to 5 minutes without touching the ordinary case of two or three good clips.
**Open, not resolved by this proposal:** DEC-018 gives org-paid an item count (50) but never specified video
length for Moments at org-paid events. Recommend extending 30s there for consistency with most-generous-wins,
which is already DEC-018's pattern, but that is not decided here.
**Relates to / Supersedes:** Extends DEC-015 and DEC-018 rather than superseding either.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-29
**Proposed by:** Elvis
**Source:** `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` item D, revising DEC-018's retention
provision
**Topic:** Media retention becomes a tiered paid differentiator, active at launch
**Type:** Product / Commercial (financials-owner territory)
**Decision, direction confirmed:** DEC-018's flat "media retention is 12 months" becomes a tiered policy that
is active at launch rather than deferred. Nothing is ever deleted. Past the retention boundary, free-tier
media moves to cheaper storage and the user sees a thumbnail plus a download of the original; paid accounts,
individual and organization, keep full-resolution access indefinitely. Two advance warnings (T-14 days and
T-3 days) precede any tier change, each carrying a bulk-download affordance; silent degradation is not
acceptable. Thumbnails persist indefinitely at roughly 400px longest edge so no conversation develops holes.
The preservation path is device download and explicitly not copy-to-Moment. `storage_tier` and `expires_at`
ship on the media row with a scheduled job regardless.
**Threshold, RESOLVED 2026-08-29: 6 months**, between the handoff spec's 90 days and DEC-018's 12 months. It
covers the semester a memory was made in plus the break after it, which for a university-first product is the
window in which the memory is still live, and it roughly halves the steady-state storage assumption behind
DEC-018's pricing. Retrospective surfaces (annual Wrapped, and P1.2 memories resurfacing) restore their
selected items from cold storage and serve them at full quality, so a fast boundary does not degrade the
features whose entire value is looking back.
**Three implementation refinements, recommended, not yet confirmed by Elvis:** (1) build the Wrapped
full-quality path as restore-from-cold rather than exemption-from-demotion, since Wrapped runs at year-end
when the media in question has already been demoted and nothing can be exempted retroactively; this is a
retrieval cost on a small selected set rather than a permanent hot-storage cost on an ever-growing pinned
set, and it depends on the policy being tiering rather than deletion, which it is. (2) Build that path once
as a general "retrospective surface requests full quality" capability so P1.2 memories resurfacing consumes
it too; memories resurfacing runs continuously rather than annually, so at a 6-month boundary it hits demoted
media constantly and would otherwise ship surfacing thumbnails. (3) Introduce a mid-resolution tier of
roughly 1080px longest edge as what free users see full-screen past the boundary, rather than the ~400px
thumbnail: 400px is correct for grids and conversation previews but visibly soft full-screen, and as the only
thing a free user can view of a seven-month-old memory in a memory-keeping product it reads as punitive
rather than as a reason to upgrade. The paid differentiator is unaffected, since paid still means full
resolution served instantly and indefinitely, and a 1080px derivative costs roughly a tenth of an original.
**Reasoning:** Elvis's stated goal is that retention create real value for paid individual and paid org
accounts, which DEC-018's flat everyone-archives model does not do and the tiered model does. Turning it on
at launch rather than shipping unlimited retention and revisiting later avoids setting an expectation that
is expensive to walk back and avoids unbounded storage growth against a price that was never modeled for it.
**Impact:** Revises DEC-018's retention provision. Aakash flag, not a blocker: this moves the cost math in a
favorable direction rather than an adverse one, since DEC-018's $6.15 realistic and $24.60 extreme monthly
org figures assumed 12 months of full-resolution media held online for everyone; under this policy free-tier
media leaves hot storage at the boundary while paid-tier media stays hot indefinitely, so net effect depends
on the paid/free mix within an org's attendees. The bounded shape DEC-018 priced against is preserved. Worth
a re-check before ship. Deepak flag: cold-storage retrieval has real latency and needs a designed loading
state rather than a spinner that reads as broken.
**Also still open:** whether retention scope is per-uploader or per-room, carried over from the handoff
spec's own open item O-3. Nothing at launch depends on it.
**Relates to / Supersedes:** Revises DEC-018. Interacts with DEC-024 (Wrapped, memories resurfacing).
**Status:** Awaiting merger; three implementation refinements above awaiting Elvis, and Aakash review on the
commercial half (the retention window is a direct input to DEC-018's org-tier cost model)

---

## Landed

- 2026-08-28: Five decisions landed into `shared/DECISIONS.md` by the merger: DEC-029 (language
  preference storage, detection cascade, i18n scope split; refines DEC-027), DEC-030 (cohort formula
  simplified to student-vs-not, location removed; revises DEC-019), DEC-031 (home-location input
  mechanism, neighborhood granularity, mutability; refines DEC-016), DEC-032 (Explore content gated
  by country, individual-premium lift; extends DEC-018, cleared by the financials owner against the
  paid-boost lockout), and DEC-033 (apply-to-join screening question quota 3 free / 10 individual-paid;
  extends DEC-018). Change-history notes added to DEC-016, DEC-018, DEC-019, and DEC-027. Sources:
  `internationalization-korea-2026-08-26.md`, `city-location-registration-2026-08-27.md`,
  `paid-tier-features-2026-08-27.md`.

---

# Proposals from the 2026-08-30 session (phase-1/1.5 review items #7 and #8)

## DEC-NNN (PROPOSED)
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `workspaces/elvis/ideas-lifecycle-2026-08-30.md`, closing the last open thread of phase-1/1.5
review item #7; clarifies DEC-009's surviving idea provision and corrects handoff spec §10
**Topic:** Ideas lifecycle: pause new joins, auto-archive on inactivity, deletion, detachment, tombstone
**Type:** Product
**Decision:** Ideas gain a defined lifecycle, which they did not previously have (the handoff spec's §3
status machine covers Events only). Five parts. (1) DEC-009's "close to new joiners" toggle is confirmed as
a membership freeze, not a shutdown: the existing group keeps full access and only new joins stop. It is
reversible, is renamed "Pause new joins" (state "New joins paused", outsider-facing "This idea isn't taking
new people right now"), and **ships visible and usable in phase 1, superseding DEC-009's "do not expose"
provision.** (2) An idea with no activity for 90 days is archived automatically by the
system: visible, read-only, with links and spawned-event backlinks surviving. Activity means another user's
Interested tap, a Discussion comment, or a spawned event; views do not count. There is no reason string on
an idea archive, correcting handoff spec §10, because reasons belong to Events, specifically to cancellation
where §3.2 already requires a written non-empty reason delivered to all attendees. (3) A creator may delete
an idea outright only while no one else has interacted with it, using that same interaction test; the
motivating case is created-by-mistake, so this path is deliberately friction-free and needs no review
routing. (4) Once interaction exists the idea cannot be deleted, but the creator may detach themselves; a
detached idea becomes system-owned in phase 1, actionable only by admins. (5) An idea removed by moderation
leaves its inspired events standing where those events are themselves fine, with the backlink replaced by an
"Idea removed" tombstone. Spawning an event never archives or closes an idea, because an idea is a hub for
multiple inspired events that may differ in date, time, location, theme, and schedule.
**Reasoning:** Elvis's framing is that an Idea is closer to a subreddit than to a post: it gathers
conversation around a topic and has a life of its own beyond its creator. Every part above follows from
that. The two-mechanic split (pause vs archive) is grounded in Elvis's own 2026-08-17 walkthrough, where
the toggle's purpose was "we have too many people in this idea now... I only want it for these people now",
which is protective of an active conversation rather than an ending of it, the opposite of what §10's
read-only state does. "Pause" was chosen over "Close" and "Lock" because reversibility is the semantic that
separates this control from archive, so encoding it in the verb makes the two self-distinguishing; "Lock"
was rejected as actively misleading, since a locked thread on the subreddit model Elvis is using means
nobody comments at all, which is archive behavior. 90 days rather than the events' 60 because ideas are
slower-burning by design, having no date being the entire point of the object. Views are excluded from the
interaction test deliberately: counting them would let a single passive viewer permanently block a creator
from deleting their own mistyped draft, which is the exact case that path exists for. Detached ideas become
system-owned rather than transferring ownership because handing an idea to a user who never asked for it is
worse than having no owner, and it matches how the subreddit analogy behaves in practice.
**Impact:** Gives Ideas their first defined lifecycle and closes a real accumulation gap, since I-10 makes
Ideas the object where nobody is structurally on the hook and nothing previously swept them. Deepak flags:
one tombstone mechanism should serve both the deleted-event anchor on Moments (§3.5) and the deleted-idea
backlink on inspired events, since they are the same shape; ideas need `archived_at` plus a last-activity
timestamp and an inert scheduled sweep, shipped now so retuning the threshold is a config change rather than
a migration against a live table; the interaction test is one shared predicate used by both the
delete-eligibility and archive-activity checks, not two implementations that can drift; a system-owned idea
needs a real ownerless state rather than a null creator every read path defends against. Also records the
deliberate distinction between an Idea and an Event Series (DEC-022): both are hubs with events attached
over time, and the difference is permission, since a Series has a locked add-permission while an Idea is
open to anyone inspired.
**Not resolved by this proposal:** whether an
archived idea can be un-archived; whether a detached idea can regain an owner; whether archived ideas still
surface in Explore or only by direct link; and whether interested users are notified when an idea is paused
or archived. A host-initiated early archive is deliberately not included, an inference from there being no
reason string, cheap to add later.
**Supersedes DEC-009's "do not expose" provision for the idea toggle**, the last surviving idea provision of
a decision already superseded for chat and calendar by DEC-013. DEC-009's reasoning was cold-start (a new app
needs more joiners not fewer, so a joining restriction is premature). What changed is that the mechanic is
now understood as protective rather than restrictive: it does not remove an idea from circulation, since the
idea stays visible, discoverable, and able to accumulate inspired events. It freezes only the membership of
the conversation, so a group grown too noisy to converge can still produce something, and an idea that
reaches a real event is worth more to the joiner supply than one that collapses under its own discussion.
This closes phase-1/1.5 review item #7, open since the 2026-08-18 review aid.
**Relates to:** Corrects handoff spec §10 on the reason string. Relates to DEC-022 (Event Series
distinction) and to the handoff's §3.5 tombstone pattern.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `workspaces/elvis/event-schedule-2026-08-25.md` (2026-08-30 update), phase-1/1.5 review item #8;
refines DEC-025's event-schedule provision
**Topic:** Event schedule: multi-day dependency closed, schedule allowed pre-confirmation, recurring
propagation
**Type:** Product + Technical
**Decision:** Three resolutions completing the event schedule design. (1) The multi-day dependency flagged
2026-08-25 is closed: the Event model does support a start and end date that differ. The handoff spec ships
`scheduled_end` on the Event row as "ship now" and states multi-day events are covered, and Elvis confirms
the creation flow exposes it as an Airbnb-style calendar picker where a single day and a range are the same
interaction. (2) A host may build a schedule on an event whose date or time is still unresolved
(`planning` status, under poll); stops carry their times and bind to the date on confirmation. (3) Recurring
events copy the full itinerary at batch generation with dates shifted per occurrence, a host may edit a
single occurrence's itinerary, and the schedule participates in DEC-021's "this occurrence / this and
following" choice rather than being copied once and left as independent rows.
**Reasoning:** On (1), nothing in DEC-001 through DEC-009 had ever established that an Event could span
calendar days, and every prior description read as singular, so the 2026-08-25 design's multi-day branch was
resting on an unverified assumption; two independent confirmations now close it. On (2), sketching the shape
of a day is what a host does while rallying people and it tells prospective attendees what they are signing
up for; blocking the itinerary until a date poll resolves would make Plan Mode feel half-built for no
protective benefit, since an unresolved date does not make a 9am first stop meaningless. On (3), copy-at-
generation and propagate-on-edit look like one feature and are two, which is exactly why it is stated
explicitly.
**Impact:** Clears the scope-matrix note "multi-day depends on Event date-range (Deepak to confirm)" on the
event schedule row. Deepak flags: the schedule must be part of the same this/following propagation path
DEC-021 already requires for edit, delete, and join, not a special case added afterward. Recommended and not
yet confirmed by Elvis: store an explicit date on every stop including single-day events and derive the
display rather than the storage, because §3.4 permits a host to extend a Live event at any time and an
extension crossing midnight retroactively turns a single-day event into a two-day one, silently corrupting
every time-only stop; one column removes the class. Elvis's calendar-picker design has not landed yet and
this should be revisited against it, particularly for how a date range interacts with per-stop date entry.
**Relates to / Supersedes:** Refines DEC-025's event schedule provision. Depends on DEC-021 (recurring) for
the propagation path and DEC-003 (map picker) for per-stop location, both unchanged.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `workspaces/elvis/event-schedule-2026-08-25.md` (2026-08-30 update) and
`workspaces/elvis/ideas-lifecycle-2026-08-30.md`; general rule arising from item #8, applies well beyond it
**Topic:** Change notifications on events and ideas: what notifies, where it lands, and who receives it
**Type:** Product
**Decision:** All changes to an event or an idea generate a notification. Event changes additionally post
into the event's chat. Notifications batch per save, so one save produces one notification regardless of how
many fields changed. The audience for an event change is three groups: joined attendees, waitlisted users
(DEC-024), and users with a pending apply-to-join application (DEC-033). Followers and passive viewers are
not notified. Idea changes notify their interested users; whether they also post into the idea's Discussion
is deferred to a later phase. Completed events are not editable at all, so no change notifications arise
after completion; admin-initiated removal of a completed event still notifies (see the completed-event
deletion proposal below).
**Reasoning:** The failure mode is concrete: someone who read an itinerary yesterday and is standing at the
old meeting point is not refreshing the event page, so a silent change strands them with information that
was correct when they read it. This satisfies I-14 (consequential actions are never silent) and rides
entirely on existing machinery rather than adding any, since §11 already establishes that poll resolution
posts an announcement and is never silent, and §7.2's chat is announcement-only by default until T-24h,
which is precisely the mode system change notices belong in. Per-save batching answers §7.3's warning that
notification volume is a launch-level risk capable of driving users to disable push entirely. The three-way
audience matters because an attendees-only rule would miss the waitlisted user, who can be auto-promoted
into an event whose date moved while they were waiting and would arrive never having been told.
**Impact:** Establishes a general rule spanning events, ideas, and every sub-object including schedule
stops, rather than leaving each feature to invent its own notification behavior. Deepak flags: notifications
batch at the save boundary, not per field; the audience query for an event change unions three membership
sets rather than reading the attendee list alone; a completed event must reject detail edits server-side,
not merely hide the affordance. Interacts with §7.3's notification-grouping requirement, which groups by
event and collapses by surface, and these change notices are one more input to that grouping.
**Not resolved by this proposal:** whether pausing or archiving an idea counts as a change for notification
purposes; both state transitions were designed 2026-08-30 but neither was named explicitly in this rule.
**Relates to / Supersedes:** Extends DEC-025 (event schedule) and interacts with DEC-024 (waitlist
auto-promote) and DEC-033 (apply-to-join). No supersession.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `workspaces/elvis/event-schedule-2026-08-25.md` (2026-08-30 update); amends handoff spec §3.2
**Topic:** Completed events cannot be deleted or left by their host; detachment is a reviewed request
**Type:** Product / Safety
**Decision:** A host may not delete an event once it has completed. After completion, deletion is admin-only
and arises from exactly two sources: moderation removal (an event found inappropriate after it ran) and a
legal erasure request under PIPA. A host who wants to be unlinked from a completed event may request
detachment, which is reviewed by an admin rather than taking effect immediately. Detail edits on a completed
event are likewise prohibited. All three restrictions are enforced server-side, not by hiding the
affordance.
**Reasoning:** Raised by Elvis asking why anyone would want to delete an event after it is over. Following
that through found a real hole: handoff spec §3.2 permits `any -> deleted` for "host or admin" without
distinguishing them, so a host could delete a completed event and with it that event's ratings. A host with
a poor rating or a report against them could then clean their record, which directly undermines DEC-014's
host reputation and DEC-024's public org track-record module. That module exists specifically as a
cold-start trust signal, and a trust signal its subject can selectively delete is not a trust signal. The
same principle is already settled elsewhere in the product and this only extends it consistently: an idea
creator cannot delete once other people have engaged (2026-08-30 Ideas lifecycle proposal above), and §12.6
routes host takedown of a Moment to review rather than allowing an instant delete. Detachment is
deliberately stricter for events than for ideas, where a creator detaches directly with no review, because
an idea creator carries no accountability record while an event host carries ratings, attendance, and a
public track record; self-serve detachment would reopen the same laundering hole through a different door.
Routing it through review lets an admin distinguish a legitimate request (harassment, leaving the
organization) from an attempt to escape a rating history, and reuses the existing §12.6 pattern rather than
adding a new one.
**Impact:** Amends handoff spec §3.2's deletion transition, which must now split by actor: host-initiated
deletion permitted only before completion, admin-only after. Detachment on a completed event becomes a
request object entering the existing admin or moderation review queue, which is new scope with no current
home on the scope matrix. Deepak flags: enforce the completion boundary server-side for deletion,
detachment, and detail edits alike; the §3.5 Moment tombstone behavior is unchanged and still applies when
an admin does remove a completed event.
**Ratings persist through both detachment and deletion, confirmed by Elvis 2026-08-30.** A detached host
keeps the event's ratings on their record, and ratings survive even when the completed event carrying them
is itself deleted. Elvis's stated principle: accountability matters and we do not want people to find
loopholes. Deepak flag, and this is easy to get wrong: a host's rating aggregate must not be computed by
joining live event rows, since that makes event deletion silently destroy the ratings, which is exactly the
outcome this rejects. Ratings carry their own denormalized host reference and survive their source event,
reusing the pattern §3.5 already defines for Moments (denormalized `event_name`, `event_date`, `org_name`
copied at creation so the card survives deletion). One mechanism, two consumers.
**Three further accountability loopholes surfaced from this work** (statutory erasure, account deletion and
re-registration, and disposable organization accounts). All three are resolved in the companion proposal
below and in `workspaces/elvis/host-accountability-2026-08-30.md`.

**2026-08-31, two proposals** from phase-1/1.5 review items #9 (ratings and post-event feedback) and #10
(QR check-in), taken as one pass. These also revise the 2026-08-29 DEC-014 amendment **in place**, before
merger, since check-in ceasing to be universal broke its two-state weighting; merge the revised version, not
a cached earlier reading. Detail in `workspaces/elvis/ratings-checkin-2026-08-31.md`.
**Relates to / Supersedes:** Amends handoff spec §3.2. Protects DEC-014 (host reputation) and DEC-024
(public org track-record module). Consistent with the 2026-08-30 Ideas lifecycle proposal and with §12.6.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `workspaces/elvis/host-accountability-2026-08-30.md`; grounded in research into Korean practice
(Danggeun withdrawal and suspension-carryover rules, PIPA Art. 36, Korean 부정이용 retention precedent)
**Topic:** Host accountability: reputation and enforcement split, ban list, and closing the org loophole
**Type:** Product / Safety / Technical
**Decision:** Reputation and enforcement are separated as distinct objects with distinct retention.
**Reputation** (host ratings, public track record) is personal data about the host and is deleted with the
account. **Enforcement** (ban and suspension records) is fraud-prevention data and survives account
deletion, retained under a disclosed 부정이용 방지 privacy-policy item. This follows Danggeun's model;
their 0-1,000 Karrot Score is explicitly not adopted, and DEC-014's 0-5 star ratings stand. Re-registration
after account deletion is allowed, subject to a cooldown and a ban-list check at signup. The ban list stores
a hashed identifier (phone hash plus device and environment signals) rather than a readable roster, with CI
(연계정보) from DEC-026's PASS flow as the strong key for Korean users, since a phone number can be swapped
and a CI cannot. On organizations: enforcement propagates, so suspending an individual suspends the orgs
they operate; admins can see every org a user operates; org creation is gated on standing (no active
suspensions plus a minimum account age) rather than on a rating; and a suspended admin may transfer their
admin role to another org member, subject to three qualifications, namely that the target has standing, that
the target was a member before the suspension with a minimum tenure, and that a suspension-triggered
transfer is admin-reviewed rather than self-serve. A suspended individual loses org access entirely, not
merely the admin title. A cap on org accounts per user and public display of a person's connected profiles
were both considered and rejected.
**Reasoning:** The conflict between accountability and PIPA dissolves once reputation and enforcement stop
being one object. PIPA Art. 36(1)'s deletion right carries only a narrow proviso (where another law
specifies the data as a collection target), which does not reach "we want to keep it for accountability", so
retained ratings are not defensible against an erasure request while a disclosed, purpose-limited abuse
record is the route Korean platforms actually use (JobKorea retains 부정이용 records five years under
회사 내부 방침). Danggeun demonstrates the pattern working in this exact market: 매너온도 dies with the
account while suspensions carry over to a new account created in the same environment. On the org loophole,
the reframe is that the problem was never that multiple orgs exist but that no consequence flowed along the
org-to-user traceability that `recommendation-algorithm-2026-08-25.md` already requires; making enforcement
propagate closes most of it with no new data model. Standing rather than rating as the creation gate avoids
blocking brand-new university club officers, which is the launch market, and avoids the cold-start failure
Danggeun hit from the other direction where scores below 50 made new users look untrustworthy. The admin
transfer exists because a 40-member club should not die for one officer's misconduct, and its three
qualifications exist because without them a bad actor plants an accomplice, transfers, and keeps de facto
control, which would undo the propagation rule entirely. Public profile linking was rejected because it
fights DEC-006 and DEC-017 directly and creates a real deanonymization surface: someone operating orgs for
an LGBTQ+ student group and a church group could be outed by the linkage alone.
**Impact:** Establishes the accountability model spanning users, hosts, and orgs. Deepak flags: the ban list
is a hashed lookup at signup, not a stored roster; suspension propagation walks the existing traceability
link and is a new consequence rather than a new model; suspension-triggered admin transfer is a distinct
path from DEC-024's routine ownership transfer and should not reuse it with a flag; a suspended user is
removed from org access entirely; and the deletion path must distinguish account deletion (ratings deleted)
from event deletion (ratings survive, per the completed-event proposal above), rather than treating any
orphaned rating as garbage to collect. Legal escalation for DLG via the already-proposed legal-register
consult: whether a disclosed 부정이용 retention item supports a ban list surviving an erasure request and
what period is defensible; whether hashing changes the analysis; and CI handling obligations if CI becomes
the ban-list key. Interacts with L-1 and L-10 already on that register.
**Not resolved by this proposal:** the re-registration cooldown period (Danggeun uses 7 days); the ban-list
retention period; minimum account age for org creation and minimum member tenure for a suspension-triggered
transfer; whether suspension propagation is automatic or a per-org reviewer decision; and whether an org
suspended by propagation is restored automatically on a valid transfer or needs separate reinstatement.
**Relates to / Supersedes:** Extends DEC-024 (org ownership transfer, public track record) and DEC-026
(PASS/CI). Consistent with DEC-014 (ratings retained as-is) and with DEC-006/DEC-017 (why public profile
linking was rejected). Builds on the anti-gaming baseline in `recommendation-algorithm-2026-08-25.md`.
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
scoring weight hanging off it created more problems than they solved (see the DEC-014 amendment above for the
three reasons), and check-in becomes honestly what it now is, the door at a ticketed event and a headcount at
a capacity event. Self-service is deferred because it serves the low-stakes case that no longer needs it.
Two problems were being conflated and are now separated: *rating integrity* (someone who did not attend
rates the event), whose mitigation is withdrawn as an accepted cost, and *attendee reliability* (someone
joins and does not show, or shows late, and the host has planned around them), which is a behavioural
problem rather than an opinion one, is significant in the event space, and is what the retained attendance
data is for.
**Impact:** Corrects the scope-matrix row "QR check-in (required)" on two counts, since check-in is neither
required of all events nor load-bearing. Forces the three-state revision to the feedback weighting in the
2026-08-29 DEC-014 amendment above, which is revised in place before merger rather than left stale.
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
**Relates to / Supersedes:** Reverses handoff spec §4.2. Amends the 2026-08-29 DEC-014 amendment (revised in
place). Relates to DEC-010 and TASK-036 (ticketing), DEC-024 (capacity and waitlist).
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
**Relates to / Supersedes:** Extends DEC-014. Interacts with the 2026-08-29 DEC-014 amendment.
**Status:** Awaiting merger
