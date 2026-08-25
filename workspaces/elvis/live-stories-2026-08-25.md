# Live event recordings (Stories-style), scoping (from `feature-backlog-2026-08-25.md` item 2)

> Elvis workspace working file, started 2026-08-25. Full scoping done same day, second item picked
> from the 2026-08-25 batch intake.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Users want to post live media while at an event, distinct from Moments (the single post-event
reflection already locked elsewhere: one per user per event, posted afterward). Elvis's own framing:
similar to Instagram Stories.

## A separate content type from Moments, RESOLVED 2026-08-25

Live stories are not a Moments variant. Potentially many per event (or none), posted during, or even
before, the event, not after it. Ephemeral by nature (see below), where Moments are permanent.
Different content type, different rules, from visibility to who can post.

## Who can post, RESOLVED 2026-08-25: RSVP is enough, check-in not required

Unlike Moments and ratings, which require actual verified check-in, posting a live story only
requires having RSVP'd. Deliberate, not an oversight: Elvis's own reasoning is that a user should be
able to post their journey or excitement on the way to an event, before they've physically arrived or
checked in, which a check-in gate would wrongly block. This is a real, correct difference in what each
feature needs to guarantee, not an inconsistency: Moments and ratings feed an org's public track
record and a host's rating, so their integrity matters and check-in verifies real attendance. A live
story is casual, ephemeral, unverified social content, it never feeds analytics, ratings, or track
record, so it does not need the same authenticity bar.

## Visibility, RESOLVED 2026-08-25: poster-chosen per post, not inherited from the event

This does not follow the event's own visibility the way Moments and the event schedule do. Real
reason it needed to be different: the same event can have posters with opposite needs, a private
individual wants protection, a promoter, celebrity, or influencer at that same event wants maximum
reach. One inherited rule cannot serve both. Instead, the poster picks the audience for each story
at post time, from four tiers:

1. **Mutuals only** (both directions follow each other). The default, most restrictive tier, applied
   unless the poster deliberately changes it, consistent with the project's privacy-by-design posture
   held throughout (DEC-006, item 8's mutual-follow rule for pre-join photos).
2. **Followers** (one-directional, anyone who follows the poster, no reciprocation required).
3. **Event attendees only** (anyone RSVP'd to this specific event, regardless of follow relationship).
4. **Public** (anyone).

This was a real correction of how I first framed the question, I'd proposed a single fixed rule
(either inherit the event's visibility, or require mutual follows globally); Elvis's answer recognized
the actual tension (a promoter's needs versus a private user's needs on the exact same event) and
solved it by moving the choice to the poster instead of picking one rule to govern everyone.

## Ephemeral, RESOLVED 2026-08-25: 24-hour expiry

Matches Elvis's own comparison to Instagram Stories directly. A live story disappears 24 hours after
posting, consistent with the "casual, unverified, not a permanent record" framing above, and distinct
from Moments' 12-month retention window already locked in the org tier's cost model.

## Not yet decided, flagged, does not block writing this up

- **Duration cap on live video clips.** Not asked. Reasonable to assume something in the same range as
  Moments' existing 15/30-second caps, but not confirmed, and does not need to block scoping the rest
  of this feature.
- **Interaction with the org tier's 50-item media cap.** Real open question, not decided. The org
  tier's media cap and its whole cost model were built around Moments specifically, persistent content
  with a 12-month retention window. Ephemeral 24-hour content has a fundamentally different, much
  smaller storage cost profile, so treating live stories as counting against that same cap would be
  wrong without redoing the cost math, and treating them as a separate, more generous allowance
  entirely is the more likely right answer, but this needs its own explicit decision before build, not
  a silent assumption either way.
- **Reactions, replies, or view counts on a story.** Not designed here. Likely a DM-reply pattern
  similar to Instagram given DM is already being pulled into phase 1, but out of scope for this pass.

## Flags for Deepak, implementation, not decided here

- The audience selector needs to be a clear, visible choice at post time, not a hidden default, and
  should probably remember the poster's last choice for convenience, while still showing it plainly
  before each post so nobody accidentally broadcasts publicly by forgetting a prior selection.
- "Event attendees" as an audience tier checks RSVP status, not check-in, consistent with the posting
  gate above, so the two attendance checks in this feature use the same bar.
- 24-hour expiry needs a cleanup job (or equivalent), not just a client-side hide, if this content
  should not remain queryable or storage-billed past its expiry window.
