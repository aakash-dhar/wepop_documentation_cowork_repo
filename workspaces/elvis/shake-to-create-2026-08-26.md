# Shake-to-create gesture, 2026-08-26

> Elvis workspace working file. A small feature Elvis introduced unprompted: shaking the phone while
> the app is open triggers the creation screen via a bottom tray. Resolved same day via a three-question
> round.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Elvis's own framing: shaking the phone while WePop is open should trigger the creation screen, presented
as a bottom tray. A secondary, physical-gesture entry point into creation, alongside whatever the app's
existing primary create entry point is (a "+" or similar).

## UX considerations

Shake gestures are a real, established mobile pattern, several apps use "shake to report a bug" or
"shake to undo," so users have some existing familiarity with shake-as-a-shortcut generally, though not
specifically for content creation. The real risk with any shake gesture is false positives: a phone in a
bag, a workout, a car on a rough road, anything that produces enough physical motion to look like an
intentional shake. A false trigger that pops a creation tray over whatever the user was actually doing
(typing a message, filling a form) is a real, annoying interruption, worse than a missed gesture.
Discoverability is also inherently low for any shake gesture, unlike a visible button, nobody stumbles
onto it by looking at the screen, it has to be taught or it goes largely unused by anyone who doesn't
already know mobile apps sometimes do this.

## Technical considerations

Requires device accelerometer/motion API access (iOS motion events, Android SensorManager), active only
while the app is foregrounded, matching "while the app is open" as scoped, no background listening, no
extra battery cost when the app isn't in use. Shake-detection sensitivity (how much motion counts as a
deliberate shake) needs real on-device tuning, not a value guessed in a doc, get this wrong in either
direction and it either doesn't fire when a user tries it or fires constantly from ordinary phone
movement.

## Suppression, RESOLVED 2026-08-26 (clarified further 2026-08-26): disabled during active input

The gesture is suppressed whenever the user is actively doing something the interruption would damage: a
text field is focused, a form or modal is already open, or the user is in a call, video, or camera view.
Outside those states, it fires normally anywhere the app is open. This avoids the worst version of a
false positive, popping the creation tray over someone mid-message or mid-form and disrupting or
discarding what they were doing.

**Open-only behavior, RESOLVED 2026-08-26: the shake is not a toggle.** Not to be confused with the
settings toggle below (a separate concept, a user preference switch to turn the whole feature on or
off). This is about the gesture's own behavior: shaking never closes anything, it only ever opens the
creation flow. Elvis explicitly confirmed the creation flow being already open is itself one of the
suppression states, the leading, most important case of the general "a form or modal is already open"
rule above, not just an incidental example of it. Practically: shake once, the tray opens. Shake again
while it's still open, nothing happens, the gesture listener is off for as long as the creation flow
stays open, whether it was opened by the shake or by the primary create entry point. It only re-arms once
the creation flow is dismissed or completed.

## Target flow, RESOLVED 2026-08-26: opens the same creation screen as the primary entry point

The shake is a second way to reach creation, not a different experience. It opens the identical
creation flow the app's existing primary create entry point opens (the event-vs-idea choice and
whatever else that flow already involves), presented in a bottom tray specifically for the
shake-triggered case. No separate lightweight or quick-create variant.

## Settings toggle, RESOLVED 2026-08-26: user-controllable, off switch available

Users can disable shake-to-create from settings. Given the real false-positive risk above, someone who
finds it more annoying than useful (a runner, a commuter on rough transit, anyone who carries their phone
loosely) needs a way to turn it off without losing anything else. Default is on.

## Discoverability, recommended, not yet confirmed with Elvis

Not explicitly asked, flagged as a recommendation rather than decided here. Given shake gestures are
inherently low-discoverability, worth surfacing this once through the existing tips/guides system
(`tips-guides-2026-08-25.md`, contextual info icon plus a static guide) rather than leaving it purely as
an undocumented shortcut. A single one-time tip (for example, the first time a user opens the creation
screen normally, or during onboarding) seems like a light, low-cost way to teach it without forcing
every user through an explainer. Not built or scoped further here, flagged for a future pass alongside
the rest of the tips/guides content.

## Not yet decided, deliberately parked

- Exact shake-detection sensitivity/threshold (how much motion counts as a deliberate shake) is a
  device-testing question, not a design decision, left to implementation.
- The precise, exhaustive list of "active input" states that suppress the gesture (every modal type,
  every text field, whether DM/chat screens count, whether the map view counts) is an implementation
  enumeration, the principle is resolved above, the exact list is not.
- Whether shake-to-create should be taught via the tips/guides system, recommended above but not
  confirmed with Elvis.
- Whether shake should log as its own interaction-logging event distinct from tapping the primary create
  button (useful for knowing how often the gesture actually gets used), not raised, worth a quick flag to
  Deepak since day-one interaction logging already exists per DEC-020.

## Flags for Deepak, implementation, not decided here

- Needs a foreground-only accelerometer/motion listener (iOS motion events, Android SensorManager), torn
  down or paused whenever the app backgrounds, no background listening.
- Needs a suppression check against current UI state (focused text field, open modal/form, active
  call/video/camera) before acting on a detected shake, not just a raw motion threshold. The creation
  flow itself being open is explicitly included in this check, the gesture listener stays off for the
  entire time the creation flow is open, regardless of what opened it, and only re-arms on dismiss or
  completion. The gesture is open-only, it must never be wired to close or dismiss the creation flow on a
  second shake.
- Opens the same creation flow/screen as the primary create entry point, presented as a bottom tray for
  this trigger path specifically, not a new or separate creation screen to build and maintain.
- Needs a settings toggle (on by default) that fully disables the gesture listener when off, not just
  hides the resulting tray.
- Recommend tagging shake-triggered creation-opens distinctly from primary-button opens in the
  interaction-logging pipeline, so usage of the gesture itself is measurable later.
