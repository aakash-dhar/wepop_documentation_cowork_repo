# Session detail, 2026-08-31

> Phase-1/1.5 review items #9 (ratings and post-event feedback) and #10 (QR check-in), taken as one pass.
> Two long-open items from DEC-014 closed, the check-in model reversed, a verification layer designed and
> then removed, and one invariant reverted after finding the error in it was mine. Two proposals filed, one
> earlier proposal revised twice in place before merger.

## Start-session

Read the live clone. Elvis had committed the previous session's nine files as `f6a76c7`. DECISIONS.md still
at 34 entries through DEC-033, `shared/HOTSHEET.md` and `shared/TASK-BOARD.md` untouched since 2026-08-26,
nothing new in `comms/`. So the eleven proposals then pending had not moved. Flagged that several of them
supersede active decisions that items #9 and #10 sit directly on top of, meaning the review would either
work from stale ground or reason against proposals that could still change. Elvis chose to proceed on his
own decisions and to chase the merge separately.

## Item #9: two things DEC-014 left open since 2026-08-19

**Stars are 1 to 5, unrated is NULL.** `conflict-review-2026-08-19.md` item 1 flagged this as "still open,
small" and it never moved. Three reasons it is not small: a 0-star rating is not expressible in a star widget
(tapping the first star yields 1, and not tapping is indistinguishable from skipping); DEC-014 makes every
field skippable so a distinct sentinel for "did not answer" is required; and most importantly a 0 entering
the weighted average would count in the denominator and drag the numerator, penalising every host whose
attendees skipped feedback.

**Moments as one door among several: closed, no change needed.** The handoff already answers it (§5.1 step 3
is a warm offer card, §15 lists the composer as "3 doors", §4.1 shows every qualifying event in the picker).

## Item #9: anonymity, editing, and where a user sees their own feedback

**Uniformly anonymous, no opt-in attribution.** Optional attribution destroys anonymity for the people who
use it: if most attendees sign and a few do not, the few become "the ones with something to hide", which on a
ten-person event is close to naming them. Structurally, anonymity is doing the work Airbnb needs double-blind
simultaneous publication for, and optional attribution trades that away for nothing. The signed channel
already exists and is the follow button, which DEC-014 deliberately separates from the rating controls.

**7-day edit and withdraw window, measured from submission.** Airbnb's edit window works only because it is
tied to a review period that closes; §5.2 says WePop's feedback window never closes, so the same pattern
would mean "editable forever". 7 days also matches the self-attest auto-resolve window, giving one "we wait a
week" period rather than two. Deepak flag, easy to get wrong first: aggregates must be recomputed from rows
rather than accumulated, since an incremental aggregate is corrupted by the first edit.

**"My feedback" in the profile**, slotted into the P1.1 three-tab restructure. Load-bearing rule: this screen
is the only place the author-to-feedback link ever surfaces to a human, private to that user, never to a
host, never in an admin UI or an export.

## Item #10: check-in reversed, then reduced

Elvis asked whether WePop should follow the ticketing standard given paid events are coming. Researched it:
staff scanning the attendee is universal, and while the stated reason is throughput, the structural reason is
enforcement, since a gate must be able to deny entry and an attendee who scans their own phone has already
walked in. **Direction reversed to host-scans-attendee**, which also means the migration risk Elvis was
worried about is avoided, and attendee self-scan becomes a deferred **self-service** mode (not "offline"
mode, a naming correction worth keeping since it needs every attendee online; the genuinely offline path is
the ticketing one where the host device caches the roster).

**Check-in is not universal.** Required on ticketed events, a host choice on capacity-limited events via a
"Check-In Required" toggle available to every host free or paid, and unavailable on open events in phase 1.
What is paid is the analytics built on the data, not the ability to record it, which sits inside DEC-018's
existing free/paid split.

**Likely de-blocks L-3.** The 위치정보법 exposure attaches to the printed-poster mode, whose static token
needs a location radius; posters exist to serve attendee self-scan, so both defer together and L-3 stops
being a gate before P0. Filed as a scoped DLG question rather than dropped, since the exposure returns when
self-service is built. Updated the pending hotsheet entry rather than leaving it stating a blocker.

## The verification layer: designed, then removed

The 2026-08-29 amendment had replaced DEC-014's hard gate with a badge plus a 1.0/0.4 weight. Check-in
ceasing to be universal broke it, and the repair chain is worth recording because each step was found by
following the previous one:

1. **Two-state weighting broke**: at an event with no check-in nobody can be verified, so every rating would
   weight 0.4 permanently, and a host running only open events would never reach the display gate, meaning
   **no public star average ever**, including orgs whose track record is a cold-start trust signal.
2. **Three-state fix introduced a perverse incentive**: a host who turned check-in *on* would have some
   ratings discounted to 0.4 while a host with no check-in had all ratings at full weight, so the host who
   did more to verify attendance reached the display gate *later*. Backwards.
3. Elvis then asked whether to remove weighting and badge altogether. Thought through and agreed: the
   machinery was already nearly inert (ticketing is not live until 1.5 and the individual tier is HELD, so
   the toggle realistically reaches org-tier capacity events and nobody else), and removing it deletes a
   category, a config, an event-level boolean threaded through every ratings consumer, two badge surfaces,
   the incentive bug, and a governance escalation.

**The governance escalation it dissolved**, which had been about to be filed: paid-gating check-in brushed
against DEC-018's "never gate marketplace actions" rule and I-16 ("a paid feature may not degrade another
user's experience"), because the party losing out was the *attendee*, who could never earn a badge no matter
what they did, purely because their host did not pay. No badge, no degradation, nothing to escalate.

**The condition that makes it a deferral rather than a deletion:** `attendance` stays a first-class
transactional table, not merely an analytics event stream, so turning weighting back on later is a config
change plus a runnable backfill. Same discipline as the inert `storage_tier`/`expires_at` columns and
DEC-012's per-country age thresholds.

## No-show tracking, and two corrections of mine

Elvis pushed back on framing no-shows as an accepted cost. He was right, and two different problems had been
conflated: *rating integrity* (someone who did not attend rates the event, mitigation withdrawn as an
accepted cost) and *attendee reliability* (someone joins and does not show, or shows late, and a host has
planned around them). Only the second is being tracked, from launch, to act on later.

**Correction 1, the I-12 overreach was mine.** The handoff §13 states I-12 as prohibiting a persistent peer
rating "visible to anyone". On 2026-08-29 I drafted replacement wording after finding it contradicted
DEC-014's host ratings, and widened it to "whether visible or internal". That widening was not asked for and
was wrong on its own terms, since DEC-014 explicitly permits an internal-only attendee signal. It was also
the clause that would have blocked no-show tracking. **Reverted to the visibility scope**, keeping the host
carve-out Elvis actually confirmed, after which no-show data needs no exception at all. Also withdrew a
warning raised earlier the same day that I-12 had been "carved out twice in three days and was eroding":
one of the two was this drafting error, and reporting it as governance strain was wrong.

**Correction 2, self-reported lateness does exist.** I had said nothing defined it. What was true is narrower:
nothing in *the repo* defines it. Elvis has it designed (a notification as the event approaches, an in-app
pop-up, and a button on the event detail page offering on my way / running late / cannot make it). Still a
real gap since engineering builds from the repo, but the work is documenting rather than inventing.

## Attendance states: two axes, and one rule that must hold from day one

Elvis's challenge ("why remove did not attend?") was answered by finding the model was under-specified rather
than the state missing. Split into two independent axes:

- **Observed attendance**, only where check-in ran: attended / claimed-unconfirmed / no-show / **not
  tracked**. "Not tracked" is a property of the event, not the person, and can never collapse into no-show,
  since where check-in did not run everyone lands there and it carries no information. "Claimed,
  unconfirmed" must not collapse either, or §4.3's 7-day auto-close records an honest attendee whose host
  never acted as absent.
- **Self-reported intent**, on every event: on my way / running late / cannot make it / nothing.

**This flipped an assumption.** Check-in coverage in phase 1 is narrow, while self-report reaches every
event including the open ones that will be the majority. So self-report is the *primary* reliability source
at launch and check-in the secondary one, the opposite of how it first appeared.

**The rule that must hold from day one:** declining in advance must not be scored like a silent no-show.
Someone who taps "cannot make it" has given the host what they need; someone silent has not. If both resolve
to "did not attend", the product teaches users that warning the host costs the same as ghosting and they go
quiet, defeating the feature. Weighting is a later decision, but the states must stay distinct in the data
now or the choice is gone.

Also recorded: a host check-in timestamp is **not** an arrival time (a host batch-scanning twenty minutes in
makes everyone look late), so both it and self-reported lateness are recorded and neither treated as truth
for now. Geo-location for actual arrival is noted as a possible later direction needing its own privacy pass
against DEC-016, DEC-012's no-forced-GPS stance, and 위치정보법.

## Open at session close

- Thirteen decision proposals pending, plus five hotsheet entries, two risks, three tasks. None merged. The
  2026-08-29 DEC-014 amendment has now been revised in place twice; the merger must take the current version
  rather than a cached reading.
- Self-reported intent needs documenting properly: whether the host is notified individually or sees a
  roster view, whether "running late" carries an estimate, whether it can attach to a DEC-025 schedule stop.
- L-3's de-blocking needs DLG confirmation rather than assumption.
- How and when no-show and punctuality data is eventually used, and whether any of it is surfaced to users.
- Whether the claimed-but-unconfirmed state is visible to the attendee, and whether the host is nudged to
  clear the queue before it auto-closes.
- What "surfaces in analytics" means concretely for check-in data, against DEC-018's per-event-free /
  rollups-paid split.
- Whether an edited rating shows as edited to viewers, or changes silently within the 7-day window.
- Carried from before: three retention refinements unconfirmed, the total-video-duration cap unconfirmed,
  explicit per-stop dates unconfirmed, Elvis's calendar-picker design not yet uploaded, the DM/group-chat
  gap, four scope-matrix rows, the I-N invariant adoption into CLAUDE.md (now carrying two I-12 corrections),
  the wave-to-phase mapping, and the [D]-tag sign-off pass.
- Item #11 (Moments) not started.
- No `shared/` edits made. All writes stayed in `workspaces/elvis/`.
