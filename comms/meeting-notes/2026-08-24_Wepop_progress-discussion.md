# Wepop progress discussion - 2026-08-24

**Attendees:** Elvis (client/designer), Aakash (PM), Deepak (tech lead - present, sick, near-silent)
**Length:** 11 min
**Recording:** https://fathom.video/share/C9wnjkajMGqdiWs75z1vTk9yXzyDfxKf
**Verbatim:** [2026-08-24_Wepop_progress-discussion_TRANSCRIPT.md](2026-08-24_Wepop_progress-discussion_TRANSCRIPT.md)

## Summary

Short check-in call, mostly Elvis and Aakash. Two new topics surfaced: payments and community
segmentation. No blockers reported.

**Payments.** Elvis wants two payment features: event ticketing (Wepop collects and pays out to the
organizer) with a 10 percent platform fee on ticket sales, and a gated premium tier that unlocks
features. Aakash proposed phasing: architect the code with payment provisions from the start
(toggle-able, gated) but do not wire payments live until the end of Phase 1 ("Phase 1.5"), so Phase
1 delivers a demo-ready product for investors first, with payments enabled as a fast follow once the
core structure is solid. Elvis agreed, on the condition that the payments vision goes into the docs
now so the architecture is built for it from day one even though the live build is deferred. On
Stripe: Wepop will use Programination's existing Stripe account (used across Elvis's other projects)
rather than setting up a new one.

**Community segmentation ("sharding").** Elvis raised launching Wepop as separate, unmixed
communities at first (for example university students vs a general/friends audience, or Korea vs
US), similar to early Facebook's per-university server model, then merging them later once the app
is bigger. Motivation: preserve a coherent community (for example, keep a university-student
audience from immediately mixing with an older general audience) since community cohesion is a
success factor for the app. Open question raised alongside it: onboarding could ask whether a user
is a student to route them into a "shard", but it is unclear what happens when someone joins
generally first and later enrolls in a university, and whether they should get access to both data
sets. Aakash will research technical and product options (including input from Deepak on the server
side) and present a couple of feasible approaches by Wednesday, 2026-08-26.

**Algorithm (deferred).** Aakash flagged that the recommendation/matching algorithm has not yet been
discussed; Elvis will add it to the docs so it can be discussed on a future call, ideally with
Deepak present (he was sick and largely silent on this call).

**Elvis's ask back:** primarily to keep updating the docs (design and documents drop folders) -
iteratively, not all at once - and to message Aakash when an update is ready to pull.

## Note on the transcript

The Fathom auto-transcript misattributes several consecutive lines between Elvis and Aakash around
timestamps 5:53-9:20 (a stretch of cross-talk where the "Facebook per-university server" story and
its follow-on points are split oddly between speaker labels). This summary resolves speaker intent
from context; the verbatim transcript file is left exactly as transcribed, uncorrected.

## Items filed from this call

- Proposed DEC-010 (payments phasing) - `workspaces/aakash/proposed-decisions.md`, pending merge.
- HOTSHEET additions (Phase-1.5 payments scope; community segmentation open question; algorithm
  watching item) - `workspaces/aakash/proposed-hotsheet.md`, pending merge.
- Todos #12 (Elvis - update docs) and #13 (Aakash - segmentation options, due 2026-08-26) -
  `comms/todos.md`.
