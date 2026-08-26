# Group dynamics as a recommendation factor, scoping

> Elvis workspace working file, started and mostly resolved 2026-08-25, raised as part of the
> recommendation-algorithm discussion and split into its own file once it was clearly a distinct
> concept, one input feeding `recommendation-algorithm-2026-08-25.md`'s scoring function, not a
> separate ranking system.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Elvis's own framing: who is already attending an event matters just as much to the experience as the
event itself. A great event can still be a bad experience for a specific person because of who else is
there, and a recommender that only scores the event's own attributes (tags, location, time) is missing
this entirely. This is a genuine, well-grounded idea, it sits inside an actual academic subfield called
group recommender systems, which studies exactly this question: how to score an item not just for one
person in isolation, but accounting for who else will be experiencing it alongside them.

Three distinct sub-mechanisms came out of this discussion, each with a different data dependency and a
different resolution.

## Avoid signal, RESOLVED 2026-08-25: soft penalty, amplified by an explicit block

If a user consistently rates one specific other user low (through whatever rating mechanism exists post
event), events that person is also attending get down-weighted in the first user's recommendations, not
excluded outright, since a rating pattern is a signal, not a certainty, and a full exclusion risks
hiding something the user would still want to attend for reasons unrelated to that one person.

**Elvis's refinement:** if the user has explicitly blocked the other person (a separate, deliberate
action from a rating pattern), the down-weighting factor should be substantially greater than the
inferred-pattern case. Both stay on the same penalty spectrum, an explicit block is not automatically a
hard exclusion, but it should weigh far more heavily than an inferred pattern alone. The exact magnitude
of "substantially greater" is a tuning question, not locked here, consistent with how every other weight
in this system is being treated.

**Real dependency, RESOLVED 2026-08-26: general user blocking confirmed as phase-1 scope.** This assumes
a general user-blocking capability, and Elvis has now confirmed it directly, phase 1, not later, treated
as a baseline safety expectation for a location-based social product, independent of whether the
avoid-signal itself is ready to consume it at launch. The blocking feature's own design (what exactly
gets blocked or hidden, symmetric or asymmetric, interaction with the private-accounts follow/approval
flow, notification behavior) is not scoped in this pass, needs its own dedicated design pass, this only
resolves the phase placement.

**Also flagged:** the rating-pattern side of this needs an actual data source, "consistently rates one
user low" implies a mechanism for rating individual attendees, not just events or hosts. That mechanism
does not exist yet either, see the note below.

## Look-alike host affinity, not designed in detail: needs real scale first

Elvis's idea: if a user similar to you likes an event with a particular host, that host might be a good
fit for you too, independent of the specific event. This is a real collaborative-filtering technique,
but it needs a large enough user base to compute "similar user" meaningfully in the first place, a form
of the cold-start problem in its own right. Bucketed alongside the rest of
`recommendation-algorithm-2026-08-25.md`'s future signal roadmap, a post-launch phase once there is
real usage data, not something to attempt against day-one user volumes.

## Group personality-mix compatibility, RESOLVED 2026-08-25: ranking signal only, to start

Elvis's example: a group that's heavily extrovert-skewed may be a difficult fit for one introvert. This
is modeled as a compatibility score between a user's own personality-related tags (DEC-005's extensible
tag list, MBTI-style tags included) and the aggregate composition of an event's current or likely
attendees, feeding into whether that event is recommended to that specific user.

**Confirmed:** ranking signal only, to start. This factors invisibly into recommendation scoring, no
host-facing tool or UI surfacing "your group skews extroverted" at this stage. A host-facing version of
this (letting a host see and manage their own group's composition) is a distinct, separate feature, not
ruled out, just not built now.

## What feeds the avoid signal, flagged: attendee-level feedback does not exist yet as a feature

Both the avoid signal and (eventually) the personality-mix signal above depend on data that currently
has no collection mechanism: rating or reacting to specific individual attendees after an event, as
distinct from rating the event or the host. Elvis referenced this as "thumbs up/down on attendees during
the feedback phase," which reads as an intended feature, but it has not been scoped anywhere in this
repo. Flagged here as a real dependency and a real gap, worth its own dedicated design pass (UX for how
and when this is asked, privacy handling for the data, how it aggregates into the avoid signal) rather
than assumed into existence by this document.

## Not yet decided, deliberately parked

- Exact magnitude of the avoid-signal penalty, both the inferred-pattern case and the
  explicit-block-amplified case.
- General user blocking's own design: what exactly gets blocked or hidden, symmetric or asymmetric,
  interaction with the private-accounts follow/approval flow. Phase placement is resolved above (phase
  1), the feature itself is not designed, needs its own scoping pass.
- The attendee-level feedback mechanism itself (thumbs up/down post-event), not designed, needs its own
  scoping pass.
- Exact scale threshold at which look-alike host affinity becomes computable with real confidence, not
  addressed, bucketed as post-launch.
- Whether personality-mix compatibility ever graduates to a host-facing tool, left open, not ruled out.

## Flags for Deepak, implementation, not decided here

- Avoid-signal computation needs per-user-pair rating history (how has user A rated user B, has user A
  blocked user B) and needs to check both at ranking time for any event user B is attending.
- Personality-mix scoring needs an aggregate view of an event's confirmed or likely attendee list's
  personality-tag composition, computed at ranking time, likely cached rather than recomputed per
  request given it changes as RSVPs come in.
- Depends on a general blocking feature and an attendee-level feedback feature, neither designed here,
  both real prerequisites before this can be built, not just tuned.
