# Session detail, 2026-08-29

> Intake and conflict review of `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx`, a large consolidated
> engineering/design handoff document Elvis brought in mid-session while item #7 of the phase-1/1.5 review
> list (Events + Ideas core objects) was being opened. The document reached much wider than item #7 and turned
> out to conflict with six ACTIVE decisions, so the session became a conflict review rather than a feature
> scoping pass. All six conflicts were walked to resolution with Elvis. Six proposals filed.

## Why this became a conflict review

The handoff spec declares itself as superseding three earlier source drafts (Phase 1 Creation / Event Detail /
Idea Hub spec, the Moments & Reflections brief v1.0, Plan Mode Spec v2.1, Subscription & Monetization Spec).
None of those three live in this repo, and the document does not reference `shared/DECISIONS.md` anywhere. So
its "supersedes" claim was against a document set that has itself already been adjudicated once, in
`conflict-review-2026-08-19.md` and the DEC-010 through DEC-025 merge. Reading it against DECISIONS.md rather
than against its own stated baseline is what surfaced the conflicts; taken at face value it would have
silently reversed six landed decisions.

## The six conflicts and how each resolved

**A. Ratings, DEC-014.** The handoff removed 0-5 star ratings entirely, replacing them with private
non-numeric sentiment. Elvis: not intended. Ratings stay exactly as DEC-014 merged them. The only intended
change was narrower: remove attendee-to-attendee thumbs-down (peer feedback becomes positive-only) and remove
the "follow all" affordance. Caught a real internal contradiction in the handoff's own new invariant I-12,
which as drafted ("no persistent peer rating of an individual visible to anyone") forbids host ratings on its
face; Elvis confirmed host and attendee rating are separate concepts and host rating is permitted, and
replacement wording was drafted carrying that distinction explicitly, so a future reader does not "fix" the
contradiction by deleting host ratings.

**B. Check-in, DEC-014's impact clause.** The handoff decoupled Moment and feedback eligibility from
check-in; DEC-014 had made check-in load-bearing for both. Elvis adopted the decoupling, and added that
check-in should now grant both a visible badge and invisible algorithmic weight. Recommended and filed a full
scoring model: 1.0 verified / 0.4 unverified, a minimum of 3 verified ratings before any public star average
displays (precedent: DEC-018's min-sample gating for org analytics), and Bayesian smoothing with C=5 on the
internal ranking signal. The smoothing is not decoration: DEC-020 deliberately builds in a new-host fairness
boost, and without smoothing a single early 2-star rating undoes it, reproducing the exact rich-get-richer
dynamic DEC-020 exists to prevent. Also named the integrity risk decoupling introduces, which neither
document had noticed: DEC-014's hard gate had been quietly ensuring only actual attendees could rate, and a
no-show can now rate. The weights are the mitigation, and they are specified as read-time config rather than
materialized values so the lever can be pulled without a backfill.

**C. Gender pre-join, DEC-017.** The handoff hides gender from attendees entirely, where DEC-017 showed an
aggregate ratio. Elvis confirmed the reversal. Separately confirmed, because the handoff never mentions it
and silence would have been read as assent either way: DEC-017's mutual-follow-only rule for pre-join
attendee photos is untouched. So DEC-017 is partially, not wholly, superseded.

**D. Media retention, DEC-018.** The handoff shipped retention OFF at launch, unbounded. DEC-018's 12-month
window is the actual input to the org-tier cost model in `freemium-model-2026-08-19.md`, so this was flagged
as a commercial problem rather than a product detail. Elvis instead chose a third position neither document
proposed: the handoff's tiered model (free degrades, paid keeps full resolution) but ON at launch as a paid
differentiator, at a 6-month boundary, with selected Wrapped media viewable at full quality. Accepted, with
three refinements recommended: (1) the Wrapped path has to be restore-from-cold rather than
exemption-from-demotion, since Wrapped runs at year-end when the media is already demoted and nothing can be
exempted retroactively; (2) the same path must serve P1.2 memories resurfacing, which runs continuously and
would otherwise ship surfacing thumbnails; (3) a ~1080px mid tier should sit between the 400px thumbnail and
the cold original, because 400px full-screen as the only view of a seven-month-old memory reads as punitive
in a memory-keeping product, and a 1080px derivative costs about a tenth of an original while leaving the
paid differentiator fully intact.

**E. Media caps, DEC-015 and DEC-018.** The handoff's numbers (20 items, 10s video) did not match the merged
ones. Elvis confirmed DEC-015/DEC-018 stand. New event-cover caps resolved: 5 items total, 15s free / 30s
paid video, which lines up exactly with the split DEC-018 already set for Moment video, so one rule governs
both surfaces. Elvis then asked whether 15s/30s was too expensive and whether to cut to 5-10s free / 20s
paid. Ran the actual numbers rather than answering by intuition: at 720p and ~3 Mbps a 15s clip is 5.6MB, and
holding an entire free-tier Moment of video for the full 6-month window costs about half a cent at R2 rates.
Recommended against the cut, on both cost grounds (clip length is a linear multiplier on the video subset
only; retention, which Elvis had just halved, is the real lever, exactly as `freemium-model-2026-08-19.md`
already concluded) and product grounds (5s is below the usable threshold for a toast or a performance, and a
cap that makes a feature unusable suppresses usage rather than converting, which costs content density the
cold-start problem depends on; it also edges against DEC-018's own never-gate-core-functionality rule).
Found where the real exposure actually is, which neither document had noticed: 50 items at 30s at an
org-paid event is 25 minutes of video in one Moment, a moderation problem before a storage one given §12.5
staffs the queue at two people alternating on-call. Recommended keeping the per-clip caps and adding a
total-video-duration cap per Moment instead (suggested 150s free, which is identical to today's worst case,
and 300s paid), which is a mechanism the handoff itself proposes and gives the right reason for but never
carries into numbers.

**F. Avoid signal, DEC-023.** Removing thumbs-down destroys the avoid signal's only data source, since it was
designed to run on "consistently rates another user low." Elvis chose block-only and explicitly rejected
running it on absence of a positive signal, on the principle that it matters more to focus on what to
recommend than what not to recommend. Recorded the rejection deliberately, since absence-of-positive is the
obvious repair a future reader will propose; it is also technically fragile, because most attendee pairs will
never exchange an optional low-uptake tap, so absence is overwhelmingly noise. Added the constructive half:
the positive tap is precisely the attendee-level feedback mechanism `group-dynamics-2026-08-25.md` flagged as
missing, and while it cannot feed an avoid signal it can feed a positive affinity ranking signal alongside
DEC-020's social proximity weight, so the amendment is not purely subtractive.

## Gaps closed, beyond the conflicts

- **General user blocking**, which the scope matrix carried as "later / proposed" with its own flag ("likely
  a phase-1 safety baseline, confirm") and which DEC-023 listed as an undesigned prerequisite, is fully
  designed by the handoff (bidirectional, total, scope stated at block time) and placed in the earliest build
  wave. Filed so the scope-matrix row can actually be corrected.
- **Item #7 itself** is mostly answered: Event vs Idea now has a hard structural definition (committed host
  and a date versus neither, invariant I-10), Discussion is specified as the persistent surface on both
  Events and Ideas (correcting the old Moments-brief line that conversation lived in event chat, and
  specifying the "photos go in the discussion board" surface DEC-009 only gestured at), a full seven-status
  event lifecycle is defined for the first time, and polls are unified into one primitive across three
  parents.

## Repo-state correction, mid-session

Elvis asked whether any of this was staged for the repo. It was not, and checking properly surfaced something
worse than a missing commit: the session had been reading a stale Aug-27 snapshot of the repo from the
uploads directory, while the live clone on Elvis's machine had moved on. In particular the merger had landed
five proposals as DEC-029 through DEC-033 and cleared the proposal queue on 2026-08-28. The locally
assembled `proposed-decisions.md` was built on the stale base and still carried all five already-merged
proposals, so filing it as-is would have re-proposed five landed decisions. Rebuilt against the live repo
instead: the queue file now carries only the six genuinely new proposals, preserving the merger's own Landed
section. Worth noting as a process lesson, not just an incident: the uploads-directory copy and the live
clone are different things, and the live clone is the one to read.

## Open at session close

- All six proposals filed 2026-08-29 are awaiting merger. The retention one additionally needs Aakash, since
  the retention window is a direct input to DEC-018's org-tier cost model, and the direction of the change is
  more margin rather than less.
- Three recommendations inside the retention proposal (restore-from-cold, extend to memories resurfacing,
  1080px mid tier) are recommendations only, not yet confirmed by Elvis.
- The total-video-duration-per-Moment cap is recommended, not confirmed. Suggested 150s free / 300s paid.
- Whether org-paid lifts Moment video to 30s or only the item count to 50 is still unspecified in DEC-018.
  Recommended lifting it, for consistency with most-generous-wins.
- Scoring weights (1.0 / 0.4, min 3 verified, C=5) are filed but are starting points, not data-backed.
- Not yet worked through from the intake, deferred to the next session: the DM and user-created group chat
  gap (DEC-013 is not mentioned anywhere in the handoff, presumably out of scope for that pass rather than
  cut, needs explicit confirmation), four new scope-matrix rows (polls, event status machine and attendance
  schema, `content_org_scopes`, event cover media caps), the two legal items worth routing into TASK-013
  (L-3 위치정보법 geofenced check-in, marked BLOCKING before P0, and L-8 PIPA under-14 guardian consent,
  which is a genuinely new angle TASK-013's adult-threshold framing has not covered), adopting the I-N
  invariant numbering into CLAUDE.md, the wave-label to phase-label mapping, and the sign-off pass on the
  handoff's [D]-tagged items.
- Carried forward untouched, and still unanswered from the 2026-08-18 review aid: DEC-009's "close to new
  joiners" toggle and whether it stays built-but-hidden in phase 1.
- The handoff spec's own open items O-1 through O-6 are not resolved here. O-5 in particular is not really an
  open product question but a stale-document problem: the Subscription spec it defers to still describes a
  single Pro tier where DEC-018 has two, so it needs updating to match rather than deciding.
- No `shared/` edits made. All writes stayed in `workspaces/elvis/`.
