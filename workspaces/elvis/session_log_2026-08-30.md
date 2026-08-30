# Session detail, 2026-08-30

> Start-session verification, the hotsheet/risk/task backlog from the 2026-08-29 handoff intake, and then
> phase-1/1.5 review items #7 and #8, both of which grew well past their original scope. Eleven decision
> proposals now pending, plus five hotsheet entries, two risks, and three tasks.

## Start-session: live repo verified, five decisions had landed

Read the live clone rather than the uploads snapshot, per the lesson recorded 2026-08-29. Found the merger
had landed DEC-029 through DEC-033 on 2026-08-28 and cleared the proposal queue, and that the four files
from the previous session were committed and pushed as `0d26bda`. Confirmed DEC-018's clauses that the
pending proposals touch (media caps, 30s paid video, 12-month retention) were unchanged by that merge, so
nothing filed needed reworking.

## The unfiled backlog from the 2026-08-29 intake

Elvis asked to start with the hotsheet proposals. The intake had produced real hotsheet-class findings that
were never filed, which is the recurring gap the session logs keep noting. Filed to three channels.

**The moderation launch blocker, reframed rather than answered.** The handoff spec §12.5 proposes SLAs
(urgent under 4h, standard 24h/48h, appeal 72h) and names two reviewers. Elvis deferred the SLAs until he
has employees to meet them, and confirmed the named second reviewer is being replaced. The entry stays
Blocking, and the reason is worth recording: response *speed* depends on headcount, response *capability*
does not, and the blocker was always about the latter. At launch the app ships anonymous public-by-default
rating comments, public Moment comments, DM and group chats, Free Now rooms, and Discussion on every event
and idea. Without a queue reports land in and someone able to act, there is no removal path at all.
Flagged hardest: 정보통신망법 takedown duties and the 임시조치 procedure attach to the service from the day
it has users, not the day it has staff, so a deferred internal target is a business choice while a missed
statutory window is not. Used **"Reviewer B (to be hired)"** as the placeholder rather than a name-shaped
pseudonym, deliberately, since a plausible fake name reproduces exactly the failure this entry caught, where
an unconfirmed name sat in a spec long enough to read downstream as a staffed position.

**Two blocking-class items that had never reached the HOTSHEET or risk register.** L-3 (위치정보법: the
printed-poster check-in geofence is location-data collection and may require 위치기반서비스사업 신고 to the
KCC), which the handoff itself marks BLOCKING before P0, with the clean fallback stated up front so it does
not become a hard stop. And the CSAM preservation-and-report runbook, required written and DLG-reviewed
before launch, where the intuitive response (delete it) is the legally wrong one.

**Two stale entries corrected.** The Watching entry stating QR check-in is load-bearing now says the
opposite of where the design went, and the DEC-023 prerequisites entry is closed by the pending batch.

Also filed two risks (single-reviewer moderation, re-cut around three distinct failure modes since one
reviewer is not "two but slower"; and 위치정보법 registration exposure) and three tasks, deliberately
minimal since TASK-034 already covers standing up moderation and TASK-013 the age/location consult.

## Item #7 closed, open since 2026-08-18

The remaining thread was DEC-009's "close to new joiners" toggle. Found Elvis's own walkthrough transcript,
which settled that the toggle freezes *membership* while keeping the idea alive ("I only want it for these
people now"), where the handoff's §10 state freezes *everything*. Near-opposite intents, so two mechanics,
not one.

Elvis then reframed §10 as time-based auto-archive, which filled a gap nobody had named: Ideas had no
lifecycle at all, while Events have a seven-status machine with expiry. Resolved at 90 days of inactivity,
no reason string (Elvis: reasons belong to Event cancellation), with activity defined as another user's
Interested tap, a Discussion comment, or a spawned event.

Copy resolved via the ux-copy skill: **"Pause new joins"**, state "New joins paused", outsider-facing "This
idea isn't taking new people right now". "Lock" was rejected as actively misleading on Elvis's own subreddit
model, where a locked thread means nobody comments, which is archive behavior. Reversibility is the semantic
separating this from archive, so encoding it in the verb makes the two self-distinguishing.

Elvis's Idea-as-subreddit framing drove the rest: an idea has a life beyond its creator, so spawning an
event never closes it (the hub is the point), a creator can only delete while nobody else has engaged
(motivated by the created-by-mistake case), and once others have engaged the creator may only detach,
leaving the idea system-owned. Recorded the deliberate Idea-versus-Event-Series distinction (permission:
Series has a locked add-permission, an Idea is open) so the two are not merged later.

**Exposure resolved: ships visible in phase 1, superseding DEC-009's "do not expose" provision.** The
supersession reasoning is written out rather than just the outcome: DEC-009's logic was cold-start, and the
mechanic is now understood as protective rather than restrictive, since the idea stays visible and keeps
accumulating events while only the conversation's membership freezes.

## Item #8, event schedule

The 2026-08-25 multi-day dependency is closed from two directions: the handoff ships `scheduled_end` on the
Event row and states multi-day is covered, and Elvis confirmed the creation flow exposes an Airbnb-style
calendar picker (design done, not yet uploaded). Schedule allowed on an unresolved `planning` event, host's
call. Change notifications resolved as a general rule broader than schedule: all changes to an event or idea
notify, event changes also post to the event chat, one notification per save, audience is joined attendees
plus waitlisted users plus pending apply-to-join applicants. Recurring events copy the itinerary at batch
generation and the schedule participates in DEC-021's "this occurrence / this and following" propagation,
which is the part most likely to be missed since copy-at-generation and propagate-on-edit look like one
feature and are two.

## Completed events: the question that found a real hole

Elvis asked why anyone would delete an event after it is over. Following it through found that handoff §3.2
permits `any -> deleted` for "host or admin" without distinguishing them, so a host could delete a completed
event and with it that event's ratings, cleaning their record. That runs straight through DEC-014's host
reputation and DEC-024's public track-record module, which exists as a cold-start trust signal. Resolved:
host self-deletion of a completed event is not allowed, deletion after completion is admin-only (moderation
or legal erasure), and detachment is a request reviewed by an admin. Elvis added that ratings stay connected
to the host through both detachment and event deletion. Flagged the implementation trap: a host's rating
aggregate cannot be computed by joining live event rows, or event deletion silently destroys the ratings,
which is the outcome this rejects; ratings need their own denormalized host reference, reusing the §3.5
Moment-anchor pattern.

## Host accountability, researched rather than assumed

Elvis's principle: we do not want people to find loopholes. Three remained. Researched Korean practice
directly rather than reasoning from priors, prompted by his question about Danggeun's 매너온도.

**The finding that resolved it:** Danggeun splits reputation from enforcement. 매너온도 is attached to the
account and dies with it, so they never defend retaining it; what survives is the suspension record, which
carries over to a new account created in the same environment. Ratings are personal data about the host and
are hard to defend against an erasure request; a ban record is fraud-prevention data and is defensible.
Trying to make one object do both jobs is what creates the conflict.

Verified PIPA Art. 36(1)'s deletion right carries only a narrow proviso (where another law specifies the
data as a collection target), which does not reach "we want to keep it for accountability" - so the ban list
rests on a disclosed 부정이용 방지 privacy-policy item instead, the route Korean platforms actually use
(JobKorea: 부정이용 records retained five years under 회사 내부 방침). Escalated to DLG rather than
asserted.

Also surfaced that Danggeun is moving off 매너온도 partly because scores below 50 made *new* users look
untrustworthy, which independently validates the min-3-verified-ratings and Bayesian-smoothing guards in the
2026-08-29 feedback proposal.

**Org loophole, reframed and closed.** The problem was never that multiple orgs exist; it was that no
consequence flowed along the org-to-user traceability `recommendation-algorithm-2026-08-25.md` already
requires. Adopted: enforcement propagates (suspending an individual suspends their orgs), admins see every
org a user operates, and org creation is gated on standing (no active suspensions plus minimum account age)
rather than on a rating, since a rating gate would block brand-new university club officers, the actual
launch market. Elvis added that a suspended admin may transfer the role to another member so a 40-person
club is not punished for one officer. Flagged and closed the evasion that opens: without qualification a bad
actor plants an accomplice, transfers, and keeps control, so the target must have standing, must have been a
member before the suspension with minimum tenure, and a suspension-triggered transfer is admin-reviewed
rather than self-serve. Also stated that a suspended user loses org access entirely rather than just the
admin title, and that a single-member org correctly stays suspended. Rejected with reasons recorded: a cap
on org accounts (blunt, a cap of N just means a bad actor uses N) and public display of connected profiles
(fights DEC-006/DEC-017 and creates a real deanonymization surface; someone running orgs for an LGBTQ+
student group and a church group could be outed by the linkage alone).

## Open at session close

- Eleven decision proposals pending, plus five hotsheet entries, two risks, three tasks. None merged.
- The moderation blocker needs its three pre-launch artifacts (admin queue, urgent push alerts, one-page
  guideline) regardless of the SLA deferral, and DLG confirmation on whether statutory takedown windows
  impose an external deadline a single reviewer can meet.
- Retention: three refinements recommended and unconfirmed (restore-from-cold for Wrapped rather than
  exemption-from-demotion, extend that path to P1.2 memories resurfacing, add a ~1080px mid tier so 400px
  is not what a free user sees of their own memory).
- Video: total-duration-per-Moment cap recommended (150s free / 300s paid) and unconfirmed; whether org-paid
  lifts Moment video to 30s still unspecified in DEC-018.
- Numbers unset across today's work: re-registration cooldown (Danggeun uses 7 days), ban-list retention
  period, minimum account age for org creation, minimum member tenure for a suspension-triggered transfer.
- Whether suspension propagation is automatic or a per-org reviewer decision; whether a propagated
  suspension lifts automatically on a valid transfer.
- Elvis's Airbnb-style calendar picker design not yet uploaded; revisit the schedule file against it.
- Whether stops store an explicit date always (recommended, protects against a live extension crossing
  midnight) or only on multi-day events.
- Items #9 (ratings and post-event feedback) and #10 (QR check-in) not started; both are reshaped by the
  pending DEC-014 amendment and are probably one pass rather than two.
- Still carried: the DM/group-chat gap (DEC-013 unmentioned in the handoff), four new scope-matrix rows,
  adopting the I-N invariant scheme into CLAUDE.md with I-12 re-scoped, the wave-to-phase label mapping, and
  the sign-off pass on the handoff's [D]-tagged items.
- No `shared/` edits made. All writes stayed in `workspaces/elvis/`.
