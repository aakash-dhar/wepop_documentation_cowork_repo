# Private accounts, pulled into phase 1

> Elvis workspace working file, 2026-08-26. Private accounts were explicitly deferred at
> `conflict-review-2026-08-19.md` item 4 and recorded as deferred in DEC-015, specifically because the
> follow-request-and-approval machinery it needs was new scope not covered anywhere. Elvis has now pulled
> this into phase 1. This file scopes what that actually commits to.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

A private-account toggle was raised early as a natural extension of the follow button, but deferred
because of its real added scope: a follow-request and approval flow that didn't exist anywhere in the
design. Elvis has now decided this ships in phase 1, not later. This file resolves what "private" actually
gates and how the request/approval mechanism works, then flags what's still genuinely open.

## What's gated, RESOLVED 2026-08-26: the whole profile, not just moments

A private account restricts the whole profile to approved followers: moments, events attended, and
upcoming RSVPs, not only moments as the original narrower framing considered. This matches the private-
account behavior users already have intuitions for from other apps, one coherent setting rather than a
moments-only carve-out that would surprise people (a stranger blocked from seeing moments but still able
to see every event someone has RSVPed to would not feel private in any meaningful sense).

**Scope boundary worth stating precisely: a private account is not the same as a private event.** A
private-account user can still host or attend a public event, the event's own visibility (public or
private, per DEC-015's event-visibility model) is unaffected by their account setting. What's gated is
the *profile view*, whether a visitor to that person's profile page can see their moments and their
event history. This is an interpretation, not something Elvis stated explicitly, flagged for confirmation
rather than silently assumed.

## Follow-request and approval, RESOLVED 2026-08-26: requires approval, standard pattern

Following a private account is no longer immediate. A follow attempt creates a pending follow-request
state instead. The account owner sees pending requests and can accept or decline each one; only accepted
followers see restricted content. This needs new machinery that did not exist before: a request state
distinct from an active follow, a lightweight approval queue/inbox for the account owner, and
notifications in both directions (a new request arrived; a request was accepted).

## Interaction with existing visibility rules, mostly composes cleanly, one item to review

**Most-restrictive-wins (DEC-015):** composes without conflict. A private account's default content
visibility becomes follower-gated; the existing per-moment private override and the event-inherits-
visibility rule still layer on top under the same most-restrictive-wins principle DEC-015 already
established as general, not a rule specific to the two cases it was written for.

**Anti-stalking pre-join visibility (DEC-006, DEC-017):** worth a consistency review, not fully resolved
here. The existing pre-join rule already restricts a specific attendee's photo to mutual (bidirectional)
follows regardless of account privacy. Private accounts tighten general profile visibility further, but
the pre-join event-attendee-list behavior was designed independently of account privacy and should be
checked against this once built, rather than assumed to already handle it correctly.

## Default state and existing followers, assumed, flagged for confirmation

Two behaviors assumed as standard, matching how equivalent features work elsewhere, not explicitly
confirmed with Elvis:

- Accounts are public by default, private is an opt-in toggle in settings, consistent with DEC-015's
  original "every account is public for now" language, now read as the default rather than a permanent
  state.
- A user who switches an existing public account to private keeps their existing followers as active
  followers (grandfathered in). Only new follow attempts after the switch require approval.

## Not yet decided, deliberately parked

- What a stranger (a non-follower, non-pending-request visitor) actually sees on a private profile: a
  full stub page (name, photo, "this account is private, request to follow"), or something more minimal.
  A real UX question, not designed here.
- Whether private-account status affects discovery surfaces beyond the profile page itself, for example
  whether a private user's public-event participation should still show up in another user's home feed
  or Explore results the normal way, or whether anything about them gets suppressed there too. Not raised,
  worth a direct check before build given how central the recommendation algorithm already is.
- Exact approval-queue UX (a dedicated inbox screen, a notification-only flow, badge/count treatment).
- Whether declining a follow request notifies the requester or fails silently, a real product-feel
  question with no obviously correct default.

## Flags for Deepak, implementation, not decided here

- Needs a follow-request state distinct from an active follow (pending, accepted, declined), not just a
  boolean follow/not-follow relationship.
- Needs an approval queue/inbox for the account owner and notification hooks in both directions (new
  request received; request accepted).
- Needs a whole-profile content-visibility check (moments, event-attended history, upcoming RSVPs) gated
  on approved-follower status when the account is private, composed with the existing most-restrictive-
  wins moment-visibility logic from DEC-015, not a separate parallel system.
- Needs to confirm the pre-join anti-stalking visibility logic (DEC-006, DEC-017) still behaves correctly
  once private accounts exist, flagged above as a consistency review, not assumed automatically correct.
- Recommendation/discovery surfaces (DEC-020) need an explicit answer on whether private-account status
  changes what's shown to non-followers there, not just on the profile page, before this is considered
  fully specified.
