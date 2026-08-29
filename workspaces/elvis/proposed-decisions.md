# Proposed decisions from elvis - for merger review

> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Pending

Six proposals from the 2026-08-29 intake of `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx`.
All six arise from conflicts between that document and already-ACTIVE decisions; each conflict was
walked with Elvis on 2026-08-29 and resolved. Full working detail, including the resolutions not
filed here and the items still open, is in `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md`.

## DEC-NNN (PROPOSED)
**Date:** 2026-08-29
**Proposed by:** Elvis
**Source:** `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md` items A and B, amending DEC-014
**Topic:** Post-event feedback, three amendments: peer feedback becomes positive-only, no bulk follow, and
check-in decouples from eligibility in favor of a badge plus a scoring weight
**Type:** Product + Technical
**Decision:** DEC-014's 0-5 star ratings on events and hosts are retained exactly as merged, including the
optional anonymous text and its everyone/host-only visibility toggle, and their feed into host reputation.
Three amendments. (1) Attendee-to-attendee thumbs up/down is replaced by a single positive-only tap; no
negative peer record is created anywhere, and no negative peer table exists in the schema. (2) The "follow
all" affordance is removed; individual follow taps only, nothing pre-selected. (3) Check-in is no longer a
gate on feedback or on Moment authorship. A user who joined an event that completed may do both. Check-in
instead grants a visible verification badge (on Moments per the existing 참석 인증 badge, and now also on
feedback) and an invisible scoring weight: verified feedback is weighted 1.0, unverified feedback (joined and
completed but never checked in, or self-attested and unresolved at the 7-day auto-close) is weighted 0.4. A
host or org public star average does not display until at least 3 verified ratings exist, showing event count
and rating count only below that threshold. The internal recommendation signal reads the same weighted rows
through a Bayesian smoothing toward the global mean, R = (C·m + Σwᵢrᵢ) / (C + Σwᵢ) with C = 5.
**Reasoning:** Bulk-follow destroys follow as a recommendation signal, which DEC-020 weights as social
proximity (w6); a one-tap bulk action makes that weight meaningless. Removing thumbs-down reflects Elvis's
stated principle that the product should focus on what to recommend rather than what not to recommend.
Decoupling check-in removes it as a single point of failure for the entire evergreen content layer: a host
who forgets to run check-in should cost their attendees a badge, not their memories. The weights exist
because decoupling reintroduces a real integrity risk that DEC-014's hard gate was quietly handling, namely
that a user who RSVP'd and never attended can now rate. At 0.4 it takes two and a half unverified ratings to
outweigh one verified one: unverified feedback genuinely counts, which it must since launch check-in rates
will be low, but a cluster of no-shows cannot move a host's score against the people who turned up. The
minimum-verified display gate has direct precedent in DEC-018's min-sample gating for org analytics. The
smoothing constant protects DEC-020's deliberate new-host fairness boost, which a single early 2-star rating
would otherwise undo immediately, reproducing exactly the rich-get-richer dynamic DEC-020 was written to
prevent.
**Impact:** Supersedes DEC-014's attendee thumbs up/down provision and its "QR check-in becomes REQUIRED"
impact clause. QR check-in remains phase-1 scope but is no longer load-bearing for feedback, ratings, or
recommendations; the scope-matrix row's "Load-bearing for ratings, reputation, recommendations, moments" note
needs correcting. DEC-023's avoid signal loses its data source as a direct consequence, handled in a separate
proposal below. Deepak flags: store `method` and `verified_at` on the feedback row, mirroring the attendance
schema; compute the weight at read time from a config table rather than baking 0.4 into a materialized
aggregate, so retuning is a config change rather than a backfill against a large live table, the same
discipline DEC-012 used for per-country age thresholds. A verification badge on anonymous feedback discloses
attendance status and not identity, so it coexists with DEC-014's anonymity option; worth stating explicitly
so it is not "fixed" later. The weights (1.0 / 0.4), the display threshold (3), and the smoothing constant
(C = 5) are starting points and not data-backed, carrying the same caveat DEC-018's media caps carried;
revisit once real usage exists.
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
