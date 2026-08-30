# Ideas lifecycle: pause new joins, archive, deletion and detachment

> Elvis workspace working file, 2026-08-30. Closes the last open thread of item #7 of the phase-1/1.5
> review list (Events + Ideas core objects), which the 2026-08-29 handoff-spec intake resolved except for
> the DEC-009 "close to new joiners" toggle. That thread is now closed too, so item #7 is complete.
> Grounded in Elvis's own 2026-08-17 walkthrough transcript,
> the handoff spec §10, and a 2026-08-30 working session that went well past the original question.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Two things collided. DEC-009 said to build an idea "close to new joiners" toggle but not expose it in
phase 1. The handoff spec §10 separately describes closing an idea as making it visible and read-only.
Read as one mechanic, the handoff exposes exactly what DEC-009 said to hide. Read as two, both exist and
neither has a proper record.

Underneath that sat a larger gap nobody had named: **Ideas have no lifecycle at all.** The handoff's §3
status machine is explicitly for Events (seven statuses, transitions, a 60-day expiry for a planning event
with no date proposed). Ideas have none of it. Since I-10 defines an Idea as the object where structurally
nobody is on the hook, ideas accumulate faster than events do and nothing ever sweeps them.

## They are two different mechanics, RESOLVED 2026-08-30

Elvis's own words on the 2026-08-17 walkthrough, on what DEC-009's toggle is for:

> "if for some reason the host, the person who created the idea was like, okay, we have too many people in
> this idea now, talking about so many things in creating, so I'm going to close it to new people. I just
> want to, I only want it for these people now. So they closed it, so no one can join anymore."

That freezes **membership** and keeps the idea alive. The purpose is protective: too many voices, so seal
the room and let the people already there converge on a plan.

The handoff's §10 state freezes **everything**, including the existing group. That is not a restriction,
it is an archive: the idea is finished and preserved rather than deleted.

Near-opposite intents. One protects an active conversation by sealing the room; the other ends the
conversation and keeps the record.

## Idea as a topic hub, Elvis's framing 2026-08-30

Elvis's mental model, which drives most of what follows: an Idea is closer to a subreddit than to a post.
It gathers conversation around a topic and **has a life of its own beyond its creator.** An Idea is a hub
for multiple inspired events, which may differ in date, time, location, theme, and schedule. Spawning an
event therefore never closes or archives the idea; the hub is the point.

**Distinct from Event Series (DEC-022), deliberately.** The two shapes look alike (a hub with events
attached over time) and DEC-022 already noticed this from the other side, calling a Series "closer to an
Idea than to a recurring event." The real difference is permission: a Series has a locked add-permission
(only the host or approved co-hosts attach events), an Idea is open (anyone inspired can spawn one).
Recorded explicitly so the two are not merged later by someone noticing the resemblance.

## Pause new joins, RESOLVED 2026-08-30: mechanic, copy, and exposure all settled

DEC-009's toggle, renamed. Membership freezes, the existing group keeps full access, and it is reversible,
which DEC-009's own word "toggle" already implied.

| Surface | Copy |
|---|---|
| Host action | Pause new joins |
| Host-facing state | New joins paused |
| Outsider-facing | This idea isn't taking new people right now |

**Why "pause" and not "close" or "lock".** Reversibility is the semantic that separates this from archive,
so putting it in the verb makes the two controls self-distinguishing and a host never has to reason about
which is which. "Lock" was rejected as actively misleading: on the subreddit model Elvis is using, a locked
thread means nobody comments at all, which is the archive behavior, not this one. Bare "Close" was rejected
as reading terminal, and because any surface truncating "Closed to new people" to "Closed" collides with
the archived state.

The outsider-facing line carries as much weight as the host-facing one. Someone who arrives and cannot join
should read "not right now" rather than "you were rejected." The idea stays visible to them and they can
still watch it.

**Korean, starting points only, needs a native pass:** "새 참여 잠시 중단" (action), "지금은 새로운 참여를
받지 않아요" (outsider-facing), "보관됨" (archived). The property to preserve in translation is
temporariness; Korean carries it naturally (지금은, 잠시) and dropping it flips the tone from managing to
rejecting.

**Exposure, RESOLVED 2026-08-30: ships visible in phase 1.** This closes the original item #7 question,
open since the 2026-08-18 review aid. Elvis's call: build the pause toggle for Ideas for phase 1, live and
usable by hosts, not built-and-hidden.

**This supersedes DEC-009's "do not expose" provision**, which is recorded here plainly so the change is
visible rather than inferred. DEC-009's reasoning was cold-start: a new app needs more joiners not fewer, so
a control that restricts joining is premature. What has changed since is that the mechanic is now understood
as protective rather than restrictive. It does not remove an idea from circulation; the idea stays visible,
stays discoverable, and keeps accumulating inspired events. It freezes one thing, the membership of the
conversation, so a group that has grown too noisy to converge can actually produce something. An idea that
gets to a real event is worth more to the joiner supply than an idea that collapses under its own
discussion, which is the failure DEC-009's reasoning did not have in view.

## Archive, RESOLVED 2026-08-30: automatic on inactivity, no reason, no host action

Elvis's reading of §10, which resolves the lifecycle gap directly: an idea with no activity for long enough
is eventually archived by the system. Archived means visible and read-only, preserved rather than deleted,
with links and spawned-event backlinks surviving.

- **Threshold: 90 days of no activity.** Longer than the events' 60-day planning expiry because ideas are
  slower-burning by design; having no date is the entire point of the object.
- **Activity means:** another user's Interested tap, a Discussion comment, or a spawned event. Views do not
  count. A stale idea collecting passive glances is still stale.
- **No reason string, CORRECTED 2026-08-30.** The handoff's §10 phrasing "with the reason if given" does
  not apply to ideas. Elvis: giving a reason belongs to **Events**, specifically to cancellation, where
  §3.2 already requires a written non-empty reason delivered to all attendees. Ideas archive silently as a
  lifecycle event, so there is no author to supply a reason.
- **No host-initiated early archive in phase 1.** This is the one inference in this file rather than a
  stated decision, and it follows from the above: with no reason string there is nothing for a host archive
  to say, and a host who wants to wind an idea down already has "Pause new joins" to stop growth and
  deletion if nothing has happened yet. Flagged as an inference, cheap to add later if wanted.

## Deletion and detachment, RESOLVED 2026-08-30

Three cases, driven by whether anyone other than the creator has engaged.

**1. No interaction from anyone but the creator: delete outright.** Elvis's stated motivation is the
created-by-mistake case, where someone wants it gone immediately, so this path is deliberately friction-free
and needs no review routing.

*Interaction is defined as:* another user's Interested tap, another user's Discussion comment, or any
spawned event. Views do not count, deliberately: otherwise a single passive viewer permanently blocks a
creator from deleting their own mistyped draft, which is exactly the case this path exists for. Same
definition as the archive-activity test above, kept identical on purpose rather than allowed to drift.

**2. Interaction exists: no deletion, but the creator can detach.** Once other people have engaged, or
events have been spawned from it, the idea belongs to more than its creator and deleting it would destroy
other people's work. The creator instead removes themselves as the attached creator. The idea survives.

*Consequence, RESOLVED: a detached idea becomes system-owned in phase 1.* Nobody can then pause new joins,
archive it early, or edit it; only admins can act on it. Passing the creator role to another user (earliest
interested, or whoever spawned the most events) was considered and rejected: handing ownership to someone
who never asked for it is worse than having no owner, and it matches how the subreddit analogy actually
behaves, where an abandoned sub goes unmoderated until someone requests it.

**3. Reported and found inappropriate: admins delete internally.** This runs through the existing
moderation path rather than a new one, mapping onto §12.4's reviewer decision set (keep, hide, remove,
remove and suspend). Inspired events are reviewed too, and if they are also inappropriate they are deleted
and their users notified.

*The mixed case, and the reason it needs its own rule:* an idea can be inappropriate while the events
inspired by it are perfectly fine. In that case the idea is deleted and the surviving events keep their
page, with the backlink to the deleted idea replaced by a tombstone reading something like "Idea removed."

**The tombstone is an existing pattern, not a new one.** §3.5 already defines exactly this shape for
deleted events: the anchor renders a tombstone, never a 404 and never an empty frame, built from fields
denormalized at creation time. The idea-to-event backlink is the same problem and should use the same
mechanism. Flag for Deepak: build one tombstone pattern serving both, not two.

## Summary table

| State | Trigger | Who can act | Effect | Reversible |
|---|---|---|---|---|
| Open | Default | Creator | Anyone can express interest, comment, spawn events | n/a |
| New joins paused | Creator action, live in phase 1 | Creator | Membership frozen, existing group keeps full access | Yes |
| Archived | 90 days no activity | System | Visible, read-only, backlinks survive | Not decided |
| Deleted | Creator, if no interaction | Creator | Gone | No |
| Deleted (moderation) | Admin, on report | Admin | Gone; inspired events keep pages with an "Idea removed" tombstone | No |
| Detached | Creator action, when interaction exists | Creator | Idea survives, becomes system-owned | Not decided |

## Flags for Deepak

- One tombstone mechanism serving both the deleted-event anchor on Moments (§3.5) and the deleted-idea
  backlink on inspired events. Same shape, denormalized fields copied at creation.
- Ideas need an `archived_at` and a last-activity timestamp, plus an inert-until-90-days scheduled sweep.
  Same discipline the handoff applies to media retention: ship the column and the job now so enabling or
  retuning the threshold is a config change rather than a migration against a live table.
- The interaction test (Interested tap, Discussion comment, spawned event; views excluded) is used by both
  the delete-eligibility check and the archive-activity check. One shared predicate, not two
  implementations that can drift apart.
- A system-owned idea needs a real ownerless state, not a null creator that every read path has to defend
  against. Whether that is a sentinel owner or an explicit flag is an implementation call.

## Not decided here

- Whether an archived idea can be un-archived, by anyone.
- Whether a detached idea can ever regain an owner.
- Whether archived ideas still surface in Explore and recommendations, or only by direct link. §10 says
  "visible," which does not settle discoverability.
- Whether existing interested users are notified when an idea is paused or archived. Covered in principle by
  the 2026-08-30 change-notification rule, but neither state change was named explicitly in it.
