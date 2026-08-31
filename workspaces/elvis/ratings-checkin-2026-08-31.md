# Ratings, post-event feedback, and check-in

> Elvis workspace working file, 2026-08-31. Items #9 (ratings and post-event feedback) and #10 (QR
> check-in) of the phase-1/1.5 review list, taken as one pass because they turned out to be one problem.
> Closes two items DEC-014 flagged as open on 2026-08-19 and never resolved, reverses the handoff spec's
> check-in direction, and removes the verification-weighting layer designed on 2026-08-29. Grounded in
> research into ticketing and review practice; sources at the bottom.
>
> **Reading note:** the scoring model in this file went through three versions in two days (two-state
> weighting on 2026-08-29, three-state on 2026-08-31 morning, then removed entirely). Only the final one
> is described as current; the path is recorded at the end because the reasoning for removing it depends
> on what it was for.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Item #9: two things DEC-014 left open

### Stars are 1 to 5, and unrated is NULL, RESOLVED 2026-08-31

`conflict-review-2026-08-19.md` item 1 flagged this and it sat untouched: "whether 0 is a real sixth star
value a user can give, or whether 0 means not rated. Affects the average, the data model and the empty
state." Resolved: **stars run 1 to 5, and an unrated field is NULL, never 0.** DEC-014's "0 to 5 stars"
phrasing is corrected wherever it appears.

1. **A 0-star rating is not expressible in a star widget.** Tapping the first star yields 1. There is no
   gesture that produces 0; not tapping is indistinguishable from skipping.
2. **DEC-014 makes every field optional and every step skippable**, so a distinct sentinel for "did not
   answer" is required. If 0 means both "terrible" and "did not answer", the two are indistinguishable.
3. **It would corrupt the average.** Unrated rows entering as 0 would count in the denominator and drag the
   numerator, so every host whose attendees skipped feedback would be penalised for the skipping.

### Moments as one door among several, CLOSED 2026-08-31 (no change needed)

The other flagged item asked to confirm the feedback flow is one entry door to the Moment composer rather
than the only one, and that a user who skips feedback can still post later. The handoff settles it: §5.1
step 3 is a warm offer card that pre-selects the event and opens the composer at the media step, §15 lists
the composer as "3 doors", and §4.1 says the composer's event picker shows every qualifying event. Closing
the flag, no decision needed.

## Who can give feedback and post a Moment, RESOLVED 2026-08-31

**Anyone who joined the event through the app, once the event has completed.** That is the whole rule.
No check-in requirement, no verification tier, no badge, no weighting.

## Feedback is uniformly anonymous, RESOLVED 2026-08-31

No opt-in attribution.

**Optional attribution destroys anonymity for the people who use it.** If eight attendees sign and two do
not, the two are no longer anonymous, they are "the ones with something to hide". On a ten-person event that
is close to naming them. Anonymity only functions when it is uniform; make it a choice and the choice
becomes the signal. It also creates pressure, since a host who asks to know who said what puts everyone in a
position where declining reads as hostile.

It would also give away something structural. **Anonymity is doing the work that Airbnb needs double-blind
simultaneous publication to do.** Airbnb locks reviews and publishes both sides at once specifically to
prevent retaliation; WePop needs none of that machinery because a host cannot identify a rater at all.

**The signed channel already exists.** DEC-014 places follow buttons on the feedback screen, deliberately
separated from the rating controls "because follow is a public act and rating is not". A user who wants a
host to know they loved it follows them.

## Editing and withdrawing feedback, RESOLVED 2026-08-31: 7 days from submission

- Edit or withdraw your own feedback for **7 days after submitting**. After that, removal goes through
  moderation, matching Airbnb's post-publication handling.
- Measured **from submission, not from the event**. Airbnb's edit window works by being tied to a review
  period that *closes* (14 days after checkout). §5.2 says WePop's feedback window never closes, so the same
  pattern would mean "editable forever".
- 7 days matches the self-attest auto-resolve window in §4.3, giving the product one "we wait a week" period
  rather than two competing ones.
- Not indefinite, deliberately: ratings feed host reputation and the recommendation engine, so a rating that
  can change forever means the aggregate never stabilises, and it opens a coercion vector where a host
  pressures someone months later to revise a score.

**Flag for Deepak, easy to build wrong first:** edits and withdrawals change a host's average, so the
aggregate must be **recomputed from rows** rather than accumulated as a running sum. An incremental
aggregate is silently corrupted by the first edit.

## Where a user sees their own feedback, RESOLVED 2026-08-31

A profile menu entry, "My feedback / 내가 남긴 후기", listing what they wrote, which event it was for, and
whether the 7-day window is still open, with edit and withdraw living there rather than being hunted for on
the old event page. **Slot it into the profile three-tab restructure already scheduled in the handoff's P1.1
wave** rather than bolting it on.

**Rule for Deepak, load-bearing:** this screen is the **only** place the author-to-feedback link ever
surfaces to a human. Private to that user, never to a host, never in an admin UI that could leak it, never
in an export. Anonymity is doing structural work here and this linkage is the single point at which it could
be undone.

## Scoring, RESOLVED 2026-08-31: no verification weighting

Every rating counts equally. Two protections remain, and neither depends on check-in:

- **A public star average displays once a host has 3 ratings.** Below that, show event count and rating
  count only. Three distinct raters is the real protection against a public number being established by one
  person. Precedent: DEC-018 already uses min-sample gating for org analytics.
- **Bayesian smoothing toward the global mean** on the internal recommendation signal:
  `R = (C·m + Σrᵢ) / (C + n)`, with `C ≈ 5` and `m` the global mean. This is unrelated to check-in and stays
  regardless. It exists because DEC-020 builds in a deliberate new-host fairness boost, and without smoothing
  a single early 2-star rating undoes it, reproducing exactly the rich-get-richer dynamic DEC-020 was
  written to prevent.

**The accepted cost, stated plainly.** Someone who joins, never attends, and leaves a rating is
indistinguishable from a real attendee. DEC-014 blocked that with a hard gate; the 2026-08-29 weighting
replaced the gate; now there is neither. Judged acceptable at launch because the motive is thin at a free
casual meetup, the 3-rating gate stops one bad actor establishing a public number alone, smoothing absorbs a
single outlier, and a host can report a rating from someone who was not there. It becomes a moderation
problem rather than a scoring problem, which is a reasonable place for a low-frequency issue.

## Item #10: check-in is an operations tool

### Direction reversed, RESOLVED 2026-08-31: the host scans the attendee

Reverses handoff §4.2, where the host displays a rotating QR that attendees scan.

Staff scanning the attendee is universal in ticketing. The stated operational reason is throughput, but the
structural reason is **enforcement**: a gate must be able to *deny* entry, and denial only works if the
venue controls the decision, since an attendee who scans their own phone has already walked in. Stadium
turnstiles are the exception that proves it, where the attendee taps but against venue-owned hardware that
will not turn. Since WePop is committed to paid ticketing (DEC-010 puts payment provisions in the phase-1
codebase, TASK-036 flags ticketing as the largest technical scope), building the enforcing direction now
avoids inverting the whole attendance surface later.

### Where check-in applies, RESOLVED 2026-08-31

| Event | Check-in | Toggle available to |
|---|---|---|
| Ticketed | Required | n/a |
| Capacity set | Host choice, via a "Check-In Required" toggle shown when capacity is set | **Everyone, free and paid** |
| Open, no ticketing and no capacity | Not in phase 1 | n/a |

**The toggle is free, RESOLVED 2026-08-31.** An earlier version of this decision gated it to paid accounts;
that is withdrawn. What is paid is the **analytics** built on check-in data, which sits naturally inside
DEC-018's existing split (per-event operational numbers free, aggregate rollups and trends paid). Recording
attendance is free; analysing it across events is not.

Elvis's reasoning for check-in staying optional: a host of an open event may not want the hassle of checking
people in, or of asking their attendees to do it, and should not have to.

**Future direction, noted not designed:** check-in on all event types, including open ones, as
*self*-check-in where attending earns something concrete. Elvis's example: an open Valorant event where the
people who showed up scan a code, or are scanned, to receive an in-game virtual good. That is a real use
case for the deferred self-service mode and gives it a purpose beyond convenience, but it depends on a
rewards mechanic that does not exist (the gamification and virtual-goods thread deferred under DEC-025).

### What check-in produces, RESOLVED 2026-08-31: an operational record only

Attendance is recorded and surfaces in **analytics** (paid). It does not award a badge, does not weight
feedback, and does not gate anything. Check-in is the door at a ticketed event and a headcount at a capacity
event.

**But the record itself is load-bearing for something later, RESOLVED 2026-08-31.** Attendance data is
retained deliberately so that no-show and punctuality behaviour can eventually feed user-side scoring.
Elvis: people saying they will attend and then not showing, or showing late, is a significant problem in the
event space and makes a host's job much harder. The intent is to track now, and to incentivise and reward
users who consistently show up and show up on time later. **Tracked now, not acted on now.**

**The 참석 인증 badge is removed entirely.** It appears in the handoff (§4.1, §3.5) and in the 2026-08-29
proposal; it does not ship.

### Self-service mode, deferred

Attendees scanning a displayed QR or typing a numeric code moves to a later phase, possibly paid.

**Naming correction worth keeping:** this is **self-service** mode, not offline mode. It needs every
attendee's device online to submit. The genuinely offline-capable path is the ticketing one, where the
host's device caches the roster before doors and scans with no network. Built later as "offline mode" on the
attendee-scan design, it would not work offline.

### Consequences

- **L-3 likely stops being a P0 blocker.** The 위치정보법 exposure attaches to the *printed poster* mode,
  whose static token needs a location radius to resist forgery, and posters exist to support attendee
  self-scan. With self-scan deferred, the poster and its geofence defer too, and L-3 becomes a later-phase
  legal question. **Confirm with DLG rather than assuming**; the exposure returns intact when self-service
  is built.
- **Anti-forgery simplifies.** The 60-second rotating QR existed because a host-displayed code could be
  screenshotted and forwarded. Once a host scans a person standing in front of them, the host's own eyes are
  the strongest control available, so a static per-attendee credential suffices. The handoff's rejection of
  SafeTix-class rotating attendee credentials still holds for the reason it gave.
- The co-host `run_checkin` permission flag (§8.1) becomes more useful, since a co-host can work the door.

## Attendance data and future user scoring, RESOLVED 2026-08-31 in direction only

Elvis's requirement, and the reason removing the feedback weighting costs nothing here: **no-show and
punctuality data is tracked from launch, for use later.** These are two different problems and conflating
them caused a wrong framing earlier in this file, so stating both:

- **Rating integrity**: someone who did not attend rates the event. That is what the withdrawn 0.4 weight
  addressed, and its loss is still an accepted cost.
- **Attendee reliability**: someone joins and does not show, or shows late, and a host has planned around
  them. A different problem, about behaviour rather than opinion, and a significant one in the event space.

Only the second is being tracked. Nothing acts on it in phase 1.

### I-12: correcting an overreach of mine, not carving out an exception

**Recorded plainly because the error was mine.** The handoff spec §13 states I-12 as "no mechanic may create
a persistent peer rating of an individual that is **visible to anyone**", marked "Restated". On 2026-08-29 I
flagged that this contradicted DEC-014's host ratings and drafted replacement wording; Elvis confirmed the
*distinction* (host rating and attendee rating are separate, host rating permitted) but the wording was mine,
and I widened it to "**whether visible or internal**".

That widening was not asked for and was wrong on its own terms, because DEC-014 already permits an
internal-only attendee signal in as many words: "attendee thumbs are an internal recommendation signal only,
never shown to anyone". So the widened version contradicted DEC-014 a second way, and it is the clause that
would otherwise block retained no-show data.

**Resolution: revert to the visibility scope**, keeping only the host carve-out Elvis actually confirmed.
No-show and punctuality data then needs no exception at all, being internal and never surfaced.

Proposed wording:

> **I-12 Anti-reputation-ledger.** No mechanic may create a persistent peer rating of an individual, in their
> capacity as a participant, that is visible to anyone. Internal signals are permitted, and making one
> visible, or using one to gate access to events, is a separate decision requiring its own review. Rating a
> *host* is explicitly out of scope and permitted: hosting is a role a user opts into and is accountable for,
> and host ratings are load-bearing for trust and for the recommendation engine.

**Why the rule exists at all**, since its purpose was never written down: a *visible* peer score turns
attendee profiles into a judged surface. People optimise for the number, avoid low-scored people, and a
meetup app grows a social caste system. That is DEC-006's anti-stalking and anti-dating reasoning applied to
scoring. Internal signals do not do this, which is why DEC-014 permitted one from the outset.

**Withdrawn:** an earlier version of this file warned that I-12 had been "carved out twice in three days" and
that the invariant was eroding. That framing was wrong. One of the two was this drafting error, not an
erosion of principle.

### Three constraints on the data being collected

**Coverage equals check-in coverage.** At an event with no check-in, an attendee and a no-show are
indistinguishable. The eventual dataset is exactly as broad as check-in adoption, which in phase 1 means
ticketed events plus capacity events whose host turned the toggle on.

**A host-scan timestamp is not an arrival time, RESOLVED 2026-08-31.** In a host-scans-attendee model the
timestamp records when the *host scanned*, not when the person arrived; a host who batch-scans twenty minutes
in makes everyone look late. Elvis's call: record both the host check-in timestamp and self-reported
lateness, rely on neither as truth for now, and decide later how to use them. Possible future direction,
noted not designed: geo-location to determine actual arrival, which would need its own privacy pass given
DEC-016 and DEC-012's no-forced-GPS stance and 위치정보법 exposure.

**Self-reported intent exists in Elvis's designs but is undocumented in this repo, CORRECTED 2026-08-31.**
An earlier version of this file said it did not exist. What is actually true is narrower: nothing in the
handoff spec, DECISIONS.md, or any workspace file defines it. Elvis has it designed. That is still a real
gap, because Deepak builds from the repo, but the work is **documenting** it rather than inventing it. Now
captured in the attendance-states section below. Remaining detail worth settling when it is specced
properly: whether the host is notified individually or sees a roster view, whether "running late" carries an
estimate, and whether it is per-event only or can attach to a stop on a DEC-025 schedule.

### Attendance states, RESOLVED 2026-08-31: two independent axes

Attendance is not one enum. Two axes, recorded separately, because they have different coverage and
different meaning.

**Axis 1, observed attendance. Only exists where check-in ran.**

| State | How it arises |
|---|---|
| Attended | Host-scanned, or self-attested and host-approved |
| Claimed, unconfirmed | Self-attested, host never acted before the 7-day auto-close |
| No-show | Joined, then nothing: no check-in, no self-attest, no advance notice |
| **Not tracked** | The event ran no check-in. A property of the event, not of the person |

"Not tracked" is its own state and must never collapse into no-show. Where check-in did not run, every
attendee lands there and it carries no information about anyone.

"Claimed, unconfirmed" must never collapse into no-show either. §4.3 auto-resolves an unresolved self-attest
after 7 days, and folding that into absence would record an honest attendee whose host simply never got
round to approving as someone who did not come, which is precisely the user self-attest exists for.

**Axis 2, self-reported intent. Available on every event, including those with no check-in.**

As the event approaches, the attendee gets a notification, an in-app pop-up, and a button on the event detail
page offering **on my way / running late / cannot make it**.

**This axis is the more important one at launch, and that is worth stating loudly.** Check-in coverage in
phase 1 is narrow: ticketed events plus capacity events whose host turned the toggle on. Self-reported intent
reaches *every* event, including the open ones that will be the majority. So for the reliability data Elvis
wants to accumulate, the self-report channel is the primary source and check-in is the secondary one, which
is the opposite of how it first appeared.

### Declining in advance must not be scored like a silent no-show

The single most important rule attached to this data, and it is a design rule rather than a data one.

Someone who taps "cannot make it" has done exactly what a host needs: given notice, so the host can release
a spot, adjust a booking, or stop waiting. Someone who says nothing has not. If both resolve to "did not
attend", the product teaches its users that warning the host costs the same as ghosting, so they stay
silent, which is the precise opposite of what the feature exists for.

**The reliability signal must reward the notification, not only penalise the absence.** How that is weighted
is a later decision, but the two states must stay distinct in the data from day one or the choice is gone.

## Why the weighting layer was removed, recorded because the reasoning matters

The 2026-08-29 proposal decoupled check-in from eligibility and replaced DEC-014's hard gate with a weight
(1.0 verified / 0.4 unverified) plus a visible badge. That was correct while check-in was expected on every
event. Three things then changed it:

1. **Check-in stopped being universal** (2026-08-31), so at most events nobody could be verified and every
   rating would have weighted 0.4 permanently. A host running only open events could never reach the
   display threshold and would have **no public star average at all, ever**, including an org whose track
   record is meant to be a cold-start trust signal under DEC-024.
2. **A three-state fix** (verified 1.0 / unverified 0.4 / axis not applicable) solved that but introduced a
   perverse incentive: a paid host who turned check-in **on** would have some ratings discounted to 0.4,
   while a free host with no check-in had all ratings at full weight, so the host who did more to verify
   attendance reached the display gate **later**. Backwards.
3. **Check-in is nearly nonexistent at launch anyway.** Ticketing is not live until phase 1.5 (DEC-010) and
   the individual paid tier is HELD pending phase-1 usage data (DEC-018), so the toggle realistically
   reaches org-tier accounts with capacity events and nobody else. The machinery would serve a sliver of
   events.

Removing it deletes a category, a config, an event-level boolean threaded through every consumer of ratings,
two badge surfaces, an incentive bug, and a governance escalation (below). The cost is one mitigation for a
low-frequency problem.

**The governance escalation it removes, worth noting since it was about to be filed.** Paid-gating check-in
brushed against DEC-018's "never gate marketplace actions" three-bucket rule and against I-16, "a paid
feature may not degrade another user's experience", because the person losing out was the **attendee**, who
could never earn a badge no matter what they did, purely because their host did not pay. With no badge there
is no degradation, check-in becomes purely host tooling, and there is nothing to escalate. This dissolved
the problem rather than routing it.

## The condition that makes this a deferral, not a deletion

**`attendance(event_id, user_id, method, verified_at, approved_by)` stays a first-class transactional
table**, not merely an analytics event stream. Nothing reads it for scoring at launch, but it is there. If
no-show ratings become a real problem, or when ticketing lands and check-in becomes common, turning
weighting back on is a config change plus a backfill that can actually be run.

Same discipline already applied to `storage_tier` and `expires_at` on media, and to DEC-012's per-country
age thresholds: ship the data, leave the behavior off.

## Flags for Deepak

- Stars are 1 to 5. Unrated is NULL and excluded from every aggregate, never 0.
- Aggregates are recomputed from rows, not accumulated, so edits and withdrawals cannot corrupt them.
- `attendance` stays first-class and transactional. `attendance.method` stays an open discriminator: phase 1
  adds a host-scan method, deferred self-service adds another later. Nothing hard-codes that the attendee
  initiates.
- An event carries a boolean for whether check-in runs, driven by the table above. Nothing in the ratings
  path reads it at launch.
- Attendance is **two independent axes**, not one enum. Observed attendance (attended /
  claimed-unconfirmed / no-show / not-tracked) exists only where check-in ran; self-reported intent (on my
  way / running late / cannot make it / nothing) exists on every event. Neither "not tracked" nor "claimed,
  unconfirmed" may collapse into no-show, and "cannot make it" must stay distinct from silent absence. All
  of this matters specifically because the data is destined to score people later, and a collapsed state is
  a choice that cannot be recovered afterward.
- Record the host check-in timestamp, but do not treat it as an arrival time.
- The "My feedback" screen is the only surface exposing the author-to-feedback link, and only to its author.
- Worth borrowing from ticketing when host-scan is built: a readiness check confirming the scanner device
  holds what it needs before doors open, converting a silent failure into a visible one.

## Confirmed from the handoff spec, no change

Three-step feedback flow, every field optional and every step skippable (DEC-014). Attendee-to-attendee
feedback is a single positive tap, no thumbs-down, no bulk follow (2026-08-29 amendment). Self-attest review
queue: batch-approvable, never denied, neutral pending state (but see the three-state correction below).
Check-in window closes at event end plus 2 hours, following any host extension. Notification cadence §5.3:
T+2h then T+24h, deferred to 09:00 if it would fire between 22:00 and 09:00, no third prompt, persistent
entry points remain. The feedback submission window never closes.

## Not decided here

- Whether an edited rating shows as edited to viewers, or changes silently within the 7-day window.
- Where feedback aggregates surface to the host, and in what form.
- What "check-in appears in analytics" means concretely: which surface, free or paid, per-event or rollup.
  Interacts with DEC-018's split (per-event operational numbers free, aggregate rollups paid).
- How and when no-show and punctuality data actually gets used, and whether any of it is ever surfaced to
  users. Tracked now, deliberately not acted on.
- Self-reported lateness as a feature: entirely undesigned, see above.
- Whether the claimed-but-unconfirmed state is visible to the attendee, and whether the host is nudged to
  resolve a queue before it auto-closes.

## Sources

- [Best practice for managing entry with scanning, TryBooking](https://learn.trybooking.com/en/articles/41791-best-practice-for-managing-entry-with-scanning)
- [Can I scan tickets at a venue with no Internet connection? More.com Ticketing](https://help-teller.more.com/en/articles/5639240-can-i-scan-tickets-at-a-venue-with-no-internet-connection)
- [Check in attendees with the Eventbrite organizer app](https://www.eventbrite.com/help/en-us/articles/741083/how-to-check-in-attendees-at-the-event-with-eventbrite-organizer/)
- [Airbnb Review Policy: How Does It Work? Hospitable](https://hospitable.com/airbnb-review-policy)
- [Authentic and trustworthy reviews, Airbnb Help Center](https://www.airbnb.com/help/article/2673)
