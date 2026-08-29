# Intake review: WePop Phase 1 + P1.1 Consolidated Handoff Specification v0.9

> Elvis workspace working file, 2026-08-29. Source document: `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx`
> (dated 2026-08-30, owner Elvis Ge/CEO, audience PM/Deepak/Designer), uploaded to this session and converted
> for review. This is an INTAKE review, not a merge. Per this repo's own convention, `shared/DECISIONS.md` is
> the single source of truth and this document does not automatically supersede it just by asserting it
> supersedes three other (unmerged, not-in-repo) source drafts. Cross-referenced against DECISIONS.md
> (through DEC-028), `proposed-decisions.md`, `wepop-scope-matrix.md`, and the relevant workspace files.
>
> **Status 2026-08-29:** all six Part 1 conflicts have been walked with Elvis and resolved. Resolutions are
> recorded in place below (this repo's convention: changes recorded, not overwritten). Two follow-up
> questions remain open, both with a recommendation attached, neither blocking.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## How to read this file

Each item is tagged the way `conflict-review-2026-08-19.md` tags things, plus one new tag this review needs:

- **CONFLICT** - the handoff spec states something that contradicts an ACTIVE entry in DECISIONS.md.
- **RESOLVES** - the handoff spec answers a real open question from the scope matrix or a prior DEC.
- **GAP** - the handoff spec is silent on something we need an answer to; not a conflict, just unaddressed.
- **NEW SCOPE** - real, undecided scope the handoff spec introduces that has no home in the scope matrix yet.

---

## Part 1: Conflicts with ACTIVE decisions, all resolved 2026-08-29

### Item A - Post-event ratings: CONFLICT with DEC-014, RESOLVED 2026-08-29 in DEC-014's favor

**What DEC-014 says (ACTIVE, merged 2026-08-19):** checked-in attendees see event stars (0-5, optional public
text with an everyone/host-only toggle), a host rating (0-5 + comment), and attendee thumbs up/down on each
other (internal signal only).

**What the handoff spec said (§5, §1 item 1):** stars gone entirely. Step 1 became non-numeric sentiment,
private to the host, never public, never aggregated into a public score. Step 2 dropped the host star rating
and the attendee thumbs, replaced by a single positive tap plus follow.

**RESOLVED 2026-08-29, Elvis:** ratings are NOT being removed. DEC-014's 0-5 star ratings on both events and
hosts stand exactly as merged, including the public/host-only visibility toggle and the feed into host
reputation. The handoff spec's §5.1 "non-numeric sentiment, private to host, never aggregated into a public
score" is overridden and does not ship.

**The only intended change to DEC-014 is narrower than the handoff spec implied, two removals:**

1. **Attendee-to-attendee thumbs-down is removed.** Attendee-level peer feedback becomes positive-only: a
   single "또 만나고 싶어요"-style tap, with no negative counterpart. The handoff spec's supporting schema
   rule holds for this narrow case ("positive-only affinity record, no negative peer table exists anywhere in
   the schema") and its invariant I-12 is correct as scoped to *peer* rating.
2. **The "follow all" affordance is removed.** Individual follow taps only, nothing pre-selected. The
   handoff spec's reasoning is adopted: bulk-follow destroys follow as a recommendation signal (it is a
   weighted input to DEC-020's social-proximity signal w6, and a one-tap bulk action makes that weight
   meaningless).

**Invariant I-12 re-scoping, RESOLVED 2026-08-29.** As drafted, I-12 reads "no mechanic may create a
persistent peer rating of an individual that is visible to anyone," which contradicts DEC-014's host rating
on its face, since a host rating is a persistent, visible rating of an individual. Elvis confirmed the
intended distinction: host rating and attendee rating are separate things, and host rating is permitted.
Proposed replacement wording, carrying that distinction explicitly rather than leaving it to be inferred:

> **I-12 Anti-reputation-ledger.** No mechanic may create a persistent rating of an individual in their
> capacity as a *participant*, whether visible or internal, and no negative peer record is created anywhere
> in the system. Rating a *host* is explicitly out of scope and permitted: hosting is a role a user opts into
> and is accountable for, and host ratings are load-bearing for trust and for the recommendation engine.

The principle underneath is that the invariant protects people from being scored for showing up, not from
being scored for taking responsibility. Worth stating in the invariant itself so a future reader does not
re-derive it, or worse, "fix" the apparent contradiction by removing host ratings.

### Item B - Check-in decoupled from eligibility: CONFLICT with DEC-014's impact clause, RESOLVED 2026-08-29 in the handoff spec's favor

DEC-014's impact clause states "QR check-in becomes REQUIRED for phase 1 (it gates feedback, ratings, and
recommendations, not only moments)," and the scope matrix row still reads "Load-bearing for ratings,
reputation, recommendations, moments."

**RESOLVED 2026-08-29, Elvis:** the handoff spec's decoupling is adopted. A user who joined an event that
completed may give feedback and post a Moment, whether or not they checked in. Check-in is no longer a gate
on either. What check-in now buys is a **badge plus weight**, and Elvis confirmed both halves explicitly:
the visible badge for users, and the invisible weight for internal data and algorithms.

- **Moments:** a Moment from a checked-in user carries the 참석 인증 badge. Unchanged from the handoff spec.
- **Feedback:** feedback from a checked-in user also carries a verification badge, AND counts more heavily
  in every score that consumes it. This is new relative to both documents; the handoff spec only badged
  Moments.

**Badge and anonymity interact cleanly, no conflict:** DEC-014 allows event feedback text to be anonymous.
A verification badge on an anonymous review discloses attendance status, not identity, so the two coexist
without either being weakened. Worth stating explicitly in the spec so nobody "fixes" it later.

**The integrity risk this creates, and its mitigation.** Gating feedback behind check-in was doing real work
in DEC-014: it meant only people who actually showed up could rate. Decoupling means a user who RSVP'd and
never attended can now rate an event and its host. The weighting model below is the mitigation, and it is
deliberately a config value rather than a hardcoded one so the lever can be pulled if abuse appears.

#### Recommended scoring weights, for Elvis to confirm

Elvis asked for a recommended weight for algorithms consuming event and host scores. Recommendation:

**Per-feedback weight, one value, read at scoring time:**

| Attendance state | Weight | Rationale |
|---|---|---|
| Checked in (QR scan, host confirm, or self-attest host-approved) | **1.0** | Attendance is verified. Full trust. |
| Joined + completed, never checked in | **0.4** | Probably attended (they joined and did not cancel), but unproven. |
| Self-attested, unresolved after the 7-day auto-close | **0.4** | Same as unverified. The handoff spec already auto-resolves these to unverified rather than denied, so they should not be penalized below a plain no-check-in user. |
| Never joined | not eligible | No feedback row exists. |

**Why 0.4 rather than 0.5.** At 0.4 it takes two and a half unverified ratings to outweigh one verified one:
enough that unverified feedback genuinely counts (it has to, since check-in rates at launch will be low and
that is precisely why we decoupled), but not enough for a cluster of no-shows to move a host's score against
the people who actually turned up. Any value in the 0.3 to 0.5 band is defensible. This is a starting point,
not data-backed, and carries the same caveat DEC-018's media caps carried ("price against realistic usage,
revisit once real usage exists").

**Two consumers, two different rules.** The same weighted rows should not be read the same way by both
systems, because a public trust signal and an internal ranking input have different failure modes:

1. **Public-facing host and org rating** (profile star average, the DEC-024 org track-record module).
   Weighted average, but **gated on a minimum of 3 verified ratings before any star average displays at
   all.** Below that, show event count and rating count only, no average. This prevents a single unverified
   rating from establishing a public number on a new host, and it has direct precedent in this repo:
   DEC-018 already uses min-sample gating for org analytics segment performance.

2. **Internal recommendation signal** (DEC-020's quality/popularity input). Weighted average with Bayesian
   smoothing toward the global mean, so a low-count host is not ranked off one bad early rating:

   ```
   R = (C · m + Σ wᵢ · rᵢ) / (C + Σ wᵢ)
   ```

   where `m` is the global mean rating across all events, `C ≈ 5` is the smoothing constant (read as "worth
   5 average ratings of prior"), `rᵢ` is each rating, `wᵢ` is its weight from the table above. This is the
   standard weighted-rating form, needs no ML, and matters here specifically because DEC-020 deliberately
   builds in a new-host fairness boost. Without smoothing, one 2-star rating on a brand-new host's first
   event undoes that boost immediately, which is the exact rich-get-richer dynamic DEC-020 was written to
   prevent. `C = 5` is likewise a starting point.

**Implementation discipline, flag for Deepak.** Store `method` and `verified_at` on the feedback row (the
handoff spec's §14 attendance schema already carries both for attendance; feedback needs the same). Compute
the weight at read time from a config table. Do not bake 0.4 into a materialized aggregate, or retuning it
becomes a backfill against a large live table instead of a config change. This is the same reasoning DEC-012
used for per-country age thresholds and the same discipline the handoff spec applies with `storage_tier` /
`expires_at`.

### Item C - Gender pre-join visibility: CONFLICT with DEC-017, RESOLVED 2026-08-29 in the handoff spec's favor

**DEC-017 (ACTIVE, merged 2026-08-24):** pre-join, gender shown as an aggregate ratio, no individual
attribution.

**RESOLVED 2026-08-29, Elvis:** gender is hidden from the attendee-facing pre-join aggregate entirely, for
now. The handoff spec's §9.1 position is adopted, superseding DEC-017's aggregate-ratio provision. Hosts
still see the aggregate (§9.2: event details page and analytics), and the handoff spec's new invariant I-13
holds: gender never appears on a per-person row in any accept/decline or selection UI.

**DEC-017's photo rule is untouched, confirmed by Elvis 2026-08-29.** Individual attendee photos remain
visible pre-join only between two people who mutually follow each other, both directions; a one-way follow
never unlocks it. The handoff spec never mentions photos, so this needed an explicit confirmation rather than
an assumption, and it now has one. DEC-017 is therefore partially superseded (the gender provision), not
wholly.

### Item D - Media retention: CONFLICT with DEC-018's cost model, RESOLVED 2026-08-29 in direction, one number still open

**DEC-018 (ACTIVE, merged 2026-08-24):** "Media retention is 12 months." Not a throwaway line, it is the
actual input to the org-tier cost math in `freemium-model-2026-08-19.md` ($6.15/month realistic upper bound,
$24.60/month extreme case), and that file's own reasoning for 12 months was that it "matches a full academic
year, a member can look back across the whole year's events."

**What the handoff spec said (§6.4):** retention OFF at launch, nothing ever expires, full resolution for
everyone indefinitely, with a *later* tiered policy sketched (hot 0-90 days, cold 90+ days, free users drop
to thumbnail plus a download link, paid users keep full resolution, nothing ever deleted) and only inert
schema shipped now.

**RESOLVED 2026-08-29, Elvis:** the cap is ON at launch, and it is a paid differentiator. This is a third
position neither document proposed, and it is coherent: it adopts the handoff spec's **tiered model** (free
degrades to thumbnail plus original download, paid keeps full resolution) rather than DEC-018's flat
everyone-archives-at-12-months model, but turns it on at launch rather than deferring it. Elvis's stated
reason: "so that there is more value for paid individual and paid orgs."

**Threshold RESOLVED 2026-08-29: 6 months**, Elvis's call, between the handoff spec's 90 days and DEC-018's
12 months, paired with his addition that selected Wrapped media can still be viewed at full quality. Accepted,
with three refinements below. 6 months is defensible on its own terms: it covers the semester a memory was
made in plus the break after it, which for a university-first product is the window in which the memory is
still live, and it roughly halves the steady-state storage assumption behind DEC-018's pricing.

**Refinement 1: the Wrapped mechanism is restore-from-cold, not exemption-from-demotion.** These are two
different builds and the difference is load-bearing. Wrapped runs at year-end, by which point months 7
through 12 of a user's media has already been demoted; nothing can be exempted retroactively. What makes
Elvis's idea work is that this is a *tiering* policy and not a deletion policy (the handoff spec is explicit
that nothing is ever deleted and the original persists), so the items Wrapped selects can be pulled back from
cold storage and served at full quality on demand. That is a retrieval cost at Wrapped time on a small
selected set, rather than a permanent hot-storage cost on an ever-growing pinned set. Recommend building it
that way. The alternative reading, a user-facing "pin this to keep it full quality" control, is a permanent
cost leak and adds a product concept users have to learn; not recommended, but worth flagging in case that
was the intent.

**Refinement 2: the same mechanism must cover P1.2 memories resurfacing, not only Wrapped.** Memories
resurfacing has the same shape as Wrapped (a retrospective surface pulling old media forward) but runs
continuously rather than annually, so at a 6-month boundary it hits demoted media constantly. If
restore-from-cold is built only for Wrapped, memories resurfacing ships surfacing thumbnails. Build it once
as a general "retrospective surface requests full quality" path and both features consume it.

**Refinement 3, the one worth arguing: do not let 400px be what a free user sees of their own memory.** The
handoff spec's ~400px thumbnail has a stated and correct purpose, keeping grids and conversation previews
from developing holes. But 400px on the longest edge is visibly soft full-screen on any current phone, and if
it is also the only thing a free user can view of a seven-month-old memory in a memory-keeping product, the
degradation reads as punitive rather than as a reason to upgrade. Recommend a three-step ladder rather than
two: ~400px thumbnail for grids and previews (persists indefinitely, unchanged), a mid-resolution tier around
1080px longest edge as what free users see full-screen past the boundary, and the full-resolution original
held in cold storage, downloadable by the user at any time and served in full to paid accounts. The paid
differentiator stays fully intact (paid means full resolution, served instantly, forever) while most of the
goodwill risk of a fast boundary disappears. Cost impact is small, since a 1080px derivative is roughly a
tenth of a full-resolution original.

**One tension worth naming, not a blocker.** This product's identity per the Moments brief is memory-keeping
and reflection rather than a feed, and degrading memories at 6 months sits in some tension with that pitch;
12 months reads as generous where 6 reads as aggressive. Two things soften it substantially: nothing is ever
deleted, and the original stays downloadable at any time. With refinement 3 applied, the free experience past
the boundary is "your photo, at good quality, plus a download button," which is a fair free tier rather than
a degraded one.

**Note for Aakash, not a blocker:** this moves the cost math in a favorable direction. DEC-018's $6.15
realistic and $24.60 extreme monthly org figures assumed 12 months of full-resolution media held online for
everyone. A 6-month boundary roughly halves the steady-state hot-storage assumption behind both, offset
upward by paid-tier media now staying hot indefinitely and by cold-retrieval costs on retrospective surfaces.
Net effect depends on the paid/free mix within an org's attendees, but the bounded shape DEC-018 priced
against is preserved and the direction is more margin, not less. Worth a re-check before ship, not an
escalation.

**Also adopt regardless:** the handoff spec's inert-schema discipline (`storage_tier` and `expires_at` on the
media row, plus an inert scheduled job) is correct and should ship whatever threshold is chosen, along with
its two advance warnings (T-14 days, T-3 days) and the "전체 다운로드" affordance. Its rule that the
preservation path is device download and NOT copy-to-Moment is also correct and worth keeping explicitly:
copying to a Moment just moves the file to a bucket we keep forever, which cancels the saving.

### Item E - Media caps: CONFLICT with DEC-015/DEC-018, RESOLVED 2026-08-29 in DEC-015/DEC-018's favor, plus new event-cover caps

**RESOLVED 2026-08-29, Elvis:** DEC-015 and DEC-018 stand exactly as merged. The handoff spec's §6.2 numbers
are overridden where they differ.

**Moment media, unchanged, per DEC-015 + DEC-018:**

| | Item cap (photos and video share one pool) | Video length | Quality |
|---|---|---|---|
| Free | 10 | 15s | 720p H.264, ~3 Mbps |
| Individual paid | 20 | 30s | same |
| At an org-paid event | 50 | see open flag below | same |

Most-generous-wins still applies (an attendee at an org-paid event gets 50 regardless of their own tier).
The handoff spec's "up to 10 photos and/or up to 10 videos" (which read as 20 items) and its 10-second video
cap are both out.

**Event cover media, NEW, resolved 2026-08-29.** This is a genuinely new surface with no prior decision, and
it is separate from Moment media:

- Up to **5 items total**, photos and videos in any mix.
- Video: **15s free / 30s for paid accounts, both individual and org.**

**Consistency check, passes:** the 15s-free / 30s-paid split Elvis just set for event cover media is exactly
the split DEC-018 already established for Moment video (DEC-015 set a flat 15s explicitly *because* the
individual premium unlock was deferred; DEC-018's individual tier then specified 30s video). So the same two
numbers now govern both surfaces, which is a good outcome: one rule to explain, one rule to build.

**Small open flag, recommendation attached.** DEC-018 gives the org tier an item count (50) but never
specified video *length* for org-paid events. Elvis's event-cover answer extends 30s to org accounts, so the
question is whether org-paid also lifts Moment video to 30s at org events, or whether org-paid gets 50 items
at 15s each. **Recommend extending it (30s at org-paid events)**, for consistency with most-generous-wins,
which is already the DEC-018 pattern, and because "50 items but each capped shorter than an individual
subscriber's" is an odd thing to have to explain to a club treasurer deciding whether to pay.

**Compatible, keep:** the handoff spec's 50MB-per-clip technical ceiling does not conflict with anything. At
720p/~3 Mbps, 30 seconds is roughly 11MB, so 50MB is generous headroom and functions purely as an
abuse/corruption guard. Its mandatory client-side compression rule is also correct and worth keeping.

#### Video length: should free drop to 5-10s and paid to 20s? Recommendation: no, and here is where the cost actually is

Elvis asked 2026-08-29 whether 15s free / 30s paid is too expensive, and whether to cut to 5-10s free / 20s
paid across every video surface in the app. Running the numbers first, at 720p H.264 and roughly 3 Mbps:

| Clip length | Size |
|---|---|
| 5s | 1.9 MB |
| 10s | 3.8 MB |
| 15s | 5.6 MB |
| 20s | 7.5 MB |
| 30s | 11.3 MB |

At R2's $0.015/GB/month, holding an entire free-tier Moment of video (10 clips at 15s, 56MB) for the full
6-month retention window costs about half a cent. Even the worst case below, a 50-item org-paid Moment
entirely of 30s video, is about five cents for six months. **Clip length is not where the money is.** The
cost levers, in order of magnitude, are retention window (which Elvis just halved, saving far more than any
length change would), item count, and transcode compute. Cutting free clips from 15s to 10s would trim
roughly a third off the video subset of storage and transcode, which is real but small, and the freemium
model's own conclusion already said this: "the real lever is retention, not the price point."

**The product argument against short caps is stronger than the cost argument for them.** 15 seconds is the
established floor for social video, and it is where it is because shorter clips stop being usable: a toast, a
performance, a group cheer, a room reaction all need more than 5 seconds. A cap that makes a feature
unusable does not convert users to paid, it makes them stop using the feature, which costs the content
density this product's whole cold-start problem depends on. It also edges against DEC-018's own three-bucket
rule (quota-gate personal expression, never gate core functionality) and against the handoff spec's new
I-16 (a paid feature may not gate the social core). 15s free is a quota; 5s free is closer to a disabled
feature with a demo attached.

**Where the real exposure is, and it is not the free tier.** Worst-case video duration in a single Moment,
if every allowed item is a video at the maximum clip length:

| Tier | Items | Clip cap | Worst case |
|---|---|---|---|
| Free | 10 | 15s | 2.5 minutes |
| Individual paid | 20 | 30s | 10 minutes |
| At an org-paid event | 50 | 30s | **25 minutes** |

25 minutes of video in a single Moment is the actual outlier, and it is a moderation problem before it is a
storage problem: §12.5 sizes the moderation lane at two people alternating on-call, and a queue item that
takes 25 minutes to watch breaks that staffing model regardless of what it costs to store.

**Recommendation: keep 15s free / 30s paid per clip, and add a total-video-duration cap per Moment.** The
handoff spec already proposes exactly this mechanism for the paid tiers and gives the right reason ("when
raising the length limit, cap total duration per Moment rather than per clip, so moderation burden stays
bounded"); it just is not carried into the numbers. Suggested starting values: 150s total for free (which is
the current worst case, so nothing changes in practice for free users) and 300s total for paid and org-paid,
which cuts the 10-minute and 25-minute worst cases down to 5 minutes without touching the ordinary case of
someone posting two or three good clips. This bounds the exposure precisely where it exists, rather than
taxing every free user's ordinary 15-second clip to solve a problem the free tier does not have.

### Item F - Avoid signal: CONFLICT with DEC-023's mechanism, RESOLVED 2026-08-29 as block-only

DEC-023's avoid signal was designed to run on "a user consistently rates another user low," which required a
negative per-attendee rating. With thumbs-down removed (item A), that data source will never exist.

**RESOLVED 2026-08-29, Elvis:** block-only. The avoid signal runs solely off an explicit block. The soft,
inferred-from-a-rating-pattern half is dropped, not deferred pending a replacement signal, and it is
explicitly NOT redesigned to run on absence of a positive signal. Elvis's reasoning, worth recording because
it is a general principle and not just a call on this feature: it is more important to focus on what to
recommend than on what not to recommend.

**Two consequences worth writing into the amendment:**

1. **Absence-of-positive was considered and rejected on purpose.** Recording the rejection matters, because
   it is the obvious thing for a future reader to propose as a fix once they notice the avoid signal has one
   input. It was examined and declined as a product-philosophy call, not overlooked. It is also, on
   reflection, technically fragile: most attendee pairs at most events will never exchange a positive tap
   simply because the tap is optional and low-uptake, so absence is overwhelmingly noise rather than signal.
2. **DEC-023 does not lose its data source, it flips polarity.** The positive tap IS the attendee-level
   feedback mechanism `group-dynamics-2026-08-25.md` flagged as missing. It cannot feed an avoid signal, but
   it can feed a positive affinity signal in ranking (boost events attended by people this user has wanted
   to meet again), which sits naturally alongside DEC-020's existing social-proximity weight and directly
   serves the "focus on what to recommend" principle. Recommend adding that as the constructive half of the
   DEC-023 amendment rather than leaving the amendment purely subtractive.

Block itself is now fully designed by the handoff spec (§12.2: bidirectional, total, across every surface,
scope stated to the user at the moment of blocking) and lands in the P0 build wave, so DEC-023's
"undesigned prerequisite" flag closes at the same time. See item G.

---

## Part 2: Real gaps closed

### Item G - General user blocking: RESOLVES the scope-matrix's own open question

The scope matrix lists general user-blocking as "later / proposed," flagged explicitly: "likely a phase-1
safety baseline, confirm." DEC-023 separately flagged it as an undesigned prerequisite, and the scope
matrix's "Unbacked / needs a decision" section names it first. The handoff spec fully designs it (§12.2) and
puts it in the P0 wave, the earliest build wave. That answers the scope matrix's own question: phase-1
baseline, not later. This should be filed so the scope-matrix row can actually be corrected rather than left
reading "later / proposed" while the design says P0.

### Item H - Events + Ideas core objects: RESOLVES most of item #7 of the phase-1/1.5 review list

- **Event vs Idea, structurally (§2, invariant I-10):** Event = a plan with a committed host and a date (or
  date poll), someone is on the hook. Idea = no date, no host commitment, structurally nobody is on the
  hook. Clean, and now a hard invariant rather than an implicit convention.
- **Discussion, the persistent surface (§7, §1 item 11):** corrects the old Moments-brief line that
  conversation lived in event chat. Discussion is threaded and persistent, exists on both Events and Ideas,
  readable by anyone who can see the item and writable by joiners, available before and after. This is the
  "photos go in the discussion board" surface DEC-009 gestured at without ever specifying.
- **Event lifecycle (§3):** a full seven-status state machine with transitions, expiry nudges, and a
  live-grace/extension model. Nothing in DECISIONS.md defined this before; no conflicts found against
  existing decisions.
- **Polls as a shared primitive (§11):** one poll model across creation date polls, live-event polls, and
  idea polls. Advisory only, host resolves. Clean design, but no scope-matrix row (see item K).
- **The Interested-tap gate on idea summaries (§10):** retained deliberately, with instrumentation added so
  the decision can be revisited on data. The instrumentation list is good, particularly time-to-undo, which
  is the only thing that separates a curiosity tap from real interest.

**Still open from item #7, not answered by this document:** DEC-009's "close to new joiners" toggle (build it,
do not expose it in phase 1) is not addressed anywhere in the handoff spec. §10 covers a different mechanic.
Confirming the toggle stays built-but-hidden is still carried forward untouched from the 2026-08-18 review
aid.

---

## Part 3: Gaps, unaddressed rather than conflicting

### Item I - DM and user-created group chats (DEC-013) are not mentioned

DEC-013 pulled DM and user-created group chats fully into phase 1. The handoff spec's vocabulary table
defines Chat narrowly as "real-time messaging for the crew of a single event," and §7's three-surface model
never mentions standalone DM or a user-initiated group chat unrelated to an event. The document's own scope
line suggests DM was simply out of scope for this pass rather than cut, but that needs an explicit
confirmation that DEC-013 still stands and is undesigned here rather than silently dropped.

---

## Part 4: New scope with no home yet

### Item K - Scope-matrix rows this document needs that do not exist

- **Polls** (§11): a real reusable feature across three parents, no row anywhere in the scope matrix.
- **Event status machine / attendance schema** (§3, §4, §14): arguably infrastructure rather than a feature
  row, but foundational enough (touches Events, Ideas, DEC-024's waitlist, DEC-021's recurring events) that
  it needs a line so it does not fall through as "implied by other rows."
- **content_org_scopes multi-select org visibility** (§8.1): new schema requirement, ties to DEC-024's org
  work but is not reflected there.
- **Event cover media caps** (resolved in item E above): new, needs a home.

### Item L - Subscription tier reconciliation (the handoff's own O-5) is a stale-doc problem, not an open question

O-5 flags that "the Subscription spec documents a single Pro tier; a two-tier model was discussed," and
declines to assert pricing. But DEC-018 is already ACTIVE and merged with two tiers on separate timelines
(individual $3.99/mo HELD, org $19.99/mo proceeding). If the underlying Subscription & Monetization Spec
still describes a single tier, that source doc is stale against DECISIONS.md, and O-5 is really "update the
Subscription spec to match DEC-018," not an open product question. Flag to Aakash, since pricing is
financials-owner territory per DEC-018's own governance note.

---

## Part 5: Cross-cutting concerns

1. **Invariant numbering (I-6 through I-20) does not exist in `CLAUDE.md`.** CLAUDE.md's key-invariants
   section is a plain bullet list with no ID scheme. The handoff spec marks several invariants "Existing"
   (I-6, I-9, I-10, I-11) as though they are already tracked under these IDs; they are not, in this repo.
   Either a newer registry has not been synced in, or the numbering originates from one of the three
   superseded source drafts and was never reconciled. Recommend formally adopting the I-N scheme into
   CLAUDE.md as part of whatever merges here. **I-12 needs the re-scoping described in item A before
   adoption**, and **I-13 is new and correct as written.**

2. **Wave labels (P0 / P1 MVP / P1.1 / P1.2 / Phase 2) do not map cleanly onto the scope matrix's phase 1 /
   phase 1.5 / later.** The handoff's waves all appear to sit inside what the scope matrix calls phase 1,
   except P1.2 (memories resurfacing, Wrapped) which matches existing "later" rows. Note that the handoff
   still says "semester Wrapped" where DEC-024 renamed it annual. Recommend a short explicit mapping note so
   "P1.1" in engineering conversation and "phase 1" on the scope matrix are known to mean the same launch.

3. **Legal register (§16) has real new items to route, not just file.** Two stand out. **L-3** (위치정보법,
   the printed-poster check-in geofence, marked BLOCKING before P0) and **L-8** (PIPA 만 14세 미만 guardian
   consent, which is a genuinely new angle: TASK-013's existing framing has been about adult-age thresholds,
   never about under-14 guardian consent, and the handoff is right that the requirement exists regardless of
   the target audience being university students). Both belong in the TASK-013 consult alongside the existing
   age-gate and payments questions.

4. **Items tagged [D] rather than [C] are engineering/design inferences, not decisions Elvis made.** Per the
   document's own annotation key they need a sign-off pass: anomaly clustering on check-in (§4.4),
   server-side transcode and poster-frame generation (§6.2), comments hidden on private Moments (§6.3),
   comment visibility inheritance and bidirectional block filtering in threads (§6.3), the chat default-on
   rationale (§7.2), the third-prompt-is-nagging call (§5.3), and the derived Upcoming display tag (§3.1).
   Worth confirming each rather than letting [D] quietly read as settled once this merges.

---

## Status table

| # | Item | Type | Status |
|---|------|------|--------|
| A | Ratings kept; thumbs-down and follow-all removed | CONFLICT (DEC-014) | RESOLVED 2026-08-29. Amend DEC-014. I-12 wording resolved. |
| B | Check-in decoupled; badge + weight instead | CONFLICT (DEC-014 impact) | RESOLVED 2026-08-29. Weights recommended, awaiting Elvis confirm. |
| C | Gender hidden pre-join; photos rule untouched | CONFLICT (DEC-017) | RESOLVED 2026-08-29. Partially supersede DEC-017. |
| D | Retention tiering ON at launch, 6-month boundary | CONFLICT (DEC-018) | RESOLVED 2026-08-29 at 6 months. Three refinements recommended. |
| E | DEC-015/018 caps stand; new event-cover caps | CONFLICT (DEC-015/018) | RESOLVED 2026-08-29. Video length reviewed: recommend keeping 15s/30s, adding a per-Moment total-duration cap. |
| F | Avoid signal becomes block-only | CONFLICT (DEC-023) | RESOLVED 2026-08-29. Amend DEC-023, add positive-affinity half. |
| G | General blocking designed, P0 | RESOLVES scope-matrix gap | Ready to file; correct the scope-matrix row. |
| H | Events/Ideas, Discussion, lifecycle, polls | RESOLVES item #7 (mostly) | Ready to file. "Close to new joiners" toggle still open. |
| I | DM/group chat scope silent | GAP | Confirm DEC-013 stands, undesigned here. |
| K | Polls, status machine, org_scopes, cover caps | NEW SCOPE | Add scope-matrix rows. |
| L | Subscription spec vs DEC-018 | Stale doc | Flag to Aakash. |
| - | Invariant ID scheme | Cross-cutting | Adopt into CLAUDE.md, using the I-12 wording in item A. |
| - | Wave labels vs phase labels | Cross-cutting | Add mapping note. Handoff still says "semester" Wrapped. |
| - | L-3, L-8 | Route to TASK-013 | Add to legal consult scope. |
| - | [D]-tagged items | Cross-cutting | Sign-off pass before build. |

## Open, with recommendations attached

1. **Retention, three refinements to the 6-month call** (item D): build the Wrapped exemption as
   restore-from-cold rather than exemption-from-demotion; extend the same path to P1.2 memories resurfacing;
   and add a ~1080px mid tier so 400px is not what a free user sees of their own memory full-screen.
2. **Video length** (item E): recommend keeping 15s free / 30s paid rather than cutting to 5-10s / 20s, and
   adding a total-video-duration cap per Moment instead (suggested 150s free / 300s paid), which bounds the
   real exposure (25 minutes in a single org-paid Moment) without taxing the ordinary free clip.
3. **Does org-paid lift Moment video to 30s, or only the item count to 50?** Recommend lifting it (item E),
   consistent with most-generous-wins.
4. **Weights for confirmation** (item B): 1.0 verified / 0.4 unverified, min 3 verified before a public star
   average displays, Bayesian smoothing with C=5 on the internal ranking signal.
5. Carried forward, unrelated to this document: DEC-009's "close to new joiners" toggle exposure.
