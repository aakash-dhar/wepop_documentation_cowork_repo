# Conflict review - walkthrough vs drafts (TASK-012 working file)

> Elvis workspace working file, started 2026-08-19. Not a merge proposal yet.
> Source of the conflict list: `comms/attachments/2026-08-18_elvis-draft-docs/Wepop_Walkthrough-vs-Drafts_Review-Aid_2026-08-18.md`
> All items below are resolved except item 10, which escalates separately to Aakash rather than being
> promoted through the decisions route. Item 11 (recurring events and series pages) lives in its own
> file, `workspaces/elvis/recurring-events-2026-08-25.md`, promote it alongside this one.
> Once ready, promote the resolved set into `workspaces/elvis/proposed-decisions.md` for the merger
> (Aakash) to land.
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Progress

| # | Item | State |
|---|------|-------|
| 1 | Ratings and reviews | RESOLVED 2026-08-19 |
| 2 | Login: Kakao dominance, OTP skip, password | RESOLVED 2026-08-19 |
| 3 | Age gate: country-tied vs flat 18+ | RESOLVED 2026-08-19 |
| 4 | Comments on moments | RESOLVED 2026-08-19 |
| 5 | Video on moments and photo cap | RESOLVED 2026-08-19 |
| 6 | DMs, group chats, calendar phase markers | RESOLVED 2026-08-19 |
| 7 | Location at registration | RESOLVED 2026-08-24 |
| 8 | Gender and photos pre-join | RESOLVED 2026-08-24 |
| 9 | Undiscussed drafted surfaces (10 items) | RESOLVED 2026-08-24, series pages spun out as a follow-up |
| 10 | Moments doc names, budget, legal | ESCALATED 2026-08-24, routes to Aakash |
| 11 | Recurring events (follow-up from item 9) | RESOLVED 2026-08-25, see `recurring-events-2026-08-25.md` |
| 12 | Event Series (new concept, Elvis 2026-08-25) | RESOLVED 2026-08-25, see `event-series-2026-08-25.md` |

---

## Item 1 - Ratings and reviews: RESOLVED

**Conflict.** Phase 1 Brief v2 ships a rate-the-crew step, a profile with rating, and Reviews
screens. Moments spec v0.9 bans ratings, stars, 평점, "would you recommend" and all review
vocabulary as against product identity. The two drafts took opposite positions. No existing DEC
covered it.

**Resolution: ratings are in.** A post-event feedback session with three steps. Every field is
optional and every step is skippable. Eligibility is checked-in attendees only.

1. **Rate the event.** 0 to 5 stars plus optional free text. Anonymous. An on-screen visibility
   toggle lets the user choose everyone or host only. Default is everyone.
2. **Rate the people.** Host or organizer gets 0 to 5 stars plus a comment. Other attendees get a
   simple thumbs up or thumbs down. Anonymous. Follow buttons for the host and attendees appear on
   this page, visually separated from the rating controls because follow is a public act and rating
   is not.
3. **Add moments.** Photos, videos and/or a writeup, attached to the event, so the user and others
   can look back on the experience.

Steps 1 and 2 feed the host's overall rating and the recommendation engine for events and ideas.

**Attendee thumbs are an internal signal only.** Never shown to anyone, including the rated person.
They weight recommendations and nothing else. This is what keeps peer rating inside the reasoning
behind DEC-006 rather than turning attendee profiles into a scored surface.

**Consequences accepted.**

- **QR check-in becomes required for phase 1.** Gating feedback on check-in makes it load-bearing
  for ratings, host reputation and recommendations, not only for moments. Check-in was on the "never
  discussed on the call" list in the review aid. This answers the Moments spec open question OQ-1.
- **Moderation is a launch blocker.** Anonymous free text that is public by default means someone
  must be able to remove a comment on day one. The Moments spec open question OQ-9, who staffs
  moderation and the SLA, now needs a name against it before launch.
- **Low check-in rate is a product risk, not only an ops one.** No scans means no ratings and no
  recommendation signal. Watch after the first events. No fallback path is being built now.

**Document impact.** Moments spec v0.9 loses its ratings ban and its review-vocabulary ban. The
Phase 1 Brief rating and Reviews screens need rework to match the three-step flow above rather than
being removed.

**Still open, small.** Whether 0 is a real sixth star value a user can give, or whether 0 means not
rated. Affects the average, the data model and the empty state.

**Design note not yet settled.** Moments is step 3 of the feedback flow, but the Moments spec calls
for one composer with three entry doors. Need to confirm the feedback flow is one door among several
and that a user who skips feedback can still add a moment later.

---

## Item 2 - Login: Kakao dominance, OTP skip, password: RESOLVED

**Conflict.** DEC-004 (ACTIVE) requires phone OTP to verify every user, plus an optional password
and biometrics if feasible. Phase 1 Brief v2 makes Kakao visually dominant, skips OTP when Kakao
returns a verified phone, and contains no password screen at all.

**Kakao visual dominance is not a conflict.** DEC-004 says nothing about hierarchy. Leading with
Kakao in the Korean market is correct. No change needed.

**Resolution 2a - verification rule.** Social login via Kakao, Apple or Google may be used to create
an account or sign in. A phone number is always required to create an account. If the social
provider supplies verified identity, that satisfies verification. If it does not, the app runs its
own phone OTP.

Practical effect, worth recording because it narrows the exception:

| Provider | Returns a verified phone | Result |
|----------|--------------------------|--------|
| Kakao | Yes, under a phone-number scope requiring Kakao business review | Can satisfy verification |
| Apple | No. Name and email only, often a private relay address | OTP required |
| Google | No verified phone on standard scopes | OTP required |

The skip path is Kakao-only and Korea-only, and depends on Kakao approving that scope. The full OTP
flow is still built and still sits in the path for every provider, so this is a conditional skip for
one subset rather than reduced scope.

**Resolution 2b - password deferred.** Phase 1 login methods are: phone plus OTP, biometrics for
day-to-day re-login, social auth via Kakao / Apple / Google, and email where provided (magic link or
emailed code, since there is no password). Password moves to a later phase.

Reasoning captured: a password is a fallback channel, not a security upgrade, and phone OTP is
stronger. An optional password set after signup has very low adoption, so it would not exist for the
user who needs it. Email is already collected from every user at waitlist and signup, so an email
link covers 100 percent of accounts with no added onboarding step. Risk R3, SMS blocked by
geography, applies to markets beyond Korea and the US and is Low x Medium, so it does not justify
launch scope.

**Document impact.** DEC-004 gets marked SUPERSEDED with a pointer to a new DEC covering the above.
It is not edited in place, per the DECISIONS.md conventions. The invariant in CLAUDE.md section 8
changes from "Phone OTP verifies every user; optional password and biometrics are additive" to
every account having a verified phone number, with OTP as the default method and provider-supplied
verification as the exception.

**Revisit trigger.** Add a password when support data shows a real recovery gap, or when entering a
market where SMS is genuinely blocked.

---

## Item 3 - Age gate: RESOLVED

**Conflict.** DEC-002 (ACTIVE but provisional, pending counsel, risk R1 Medium x High, TASK-013
open) ties age to the country legal age: under a threshold around 19, trigger location early, check
the country, block with a message naming the country. US 18, Korea 19. Both drafts instead show a
flat 18+ gate ("Age gate 18+", "만 18세").

**Why a flat gate is wrong in both directions here.** The first target segment is university clubs.
In the US that is 18-year-old freshmen. In Korea the age of majority is 19. A flat 18 gate risks
sitting under Korea's line. A flat 19 gate locks out the American students the wedge depends on. The
target segment sits directly on the boundary.

**Problem with DEC-002's stated mechanism.** Triggering location permission early to establish the
country collides with open question O1, where the lean is that location should be optional and
contextual. It is also the most-declined prompt in mobile onboarding, and a decline leaves the age
gate with no country and no path forward.

**Research check.** Confirmed against current practice: the industry standard for consumer apps
(Instagram, TikTok, Discord, Bumble) is a self-declared birthdate checked against a per-country
minimum-age table, with no ID check for the general population. App-store-level age signals (Apple,
plus laws in Utah, Texas, Louisiana, Brazil, Australia, Singapore, and California's AB 1043) are
emerging as of 2025-2026 but are not yet something to build against in phase 1; worth revisiting as
an integration point later. Sources: EFF age assurance methods explainer, All Tech Is Human on
device-level age attestation, Privacy World on app store age verification laws.

**Resolution.**

- **Country** is determined once, at registration, via a fallback cascade rather than a single
  signal or a typed field: app store region first (tied to how the account and payment method were
  set up, harder to casually fake than free text), device location only if already granted for
  something else (never a forced early prompt), phone number country code as the last resort for
  anyone with no usable store signal and no location granted. Whichever resolves first sets the
  country permanently for that account. No re-checking as the user travels; this is a snapshot at
  registration, not a continuously tracked current location. Matches how most consumer apps handle
  geography and is the simplest default to hand to counsel under TASK-013.
- **Age** is a self-declared birthdate, typed once and locked after signup, correctable only through
  support. If a user is later found to have lied, ban under ToS. No ID verification in phase 1. This
  matches the industry norm, and the invite-first model is a real structural mitigation the
  comparison apps do not have, since signup is gated by a real person vouching for another, not an
  anonymous stranger.
- **Thresholds** live in a per-country config table, not hardcoded into a screen, so a legal answer
  from TASK-013 becomes a config change rather than a design revision.

**Flags carried forward, not decided here.**

- Signal-conflict handling for the country cascade (for example store region says Korea, phone
  number is a US number) is not resolved. Default read is first-available-signal-wins, no
  reconciliation logic. Flag to TASK-013 alongside the residence-vs-current-location question,
  since both are the same underlying legal-risk question R1 already covers.
- The exact platform APIs for reading app store region (StoreKit on iOS, the Play Billing equivalent
  on Android) need a short technical spike from Deepak to confirm availability and reliability
  before this is built.
- DEC-002 stays provisional until TASK-013 closes with counsel regardless of the above.

---

## Item 4 - Comments on moments: RESOLVED

**Conflict.** Phase 1 Brief v2 has a "Posted moment, comments open" screen. Moments spec v0.9 says
no comments at launch, reactions only, and explicitly "do not reserve layout space for a comment
affordance." The walkthrough never discussed comments at all; the brief added them and the spec
closed the door, so this was not two sides of a stated position, more the spec's default holding
until a reason emerged to overrule it.

**Resolution.** Moments are reframed around visibility rather than a flat in/out call. A moment is
the personal reflection the walkthrough described (photos and/or video, plus a writeup). Its
audience is Instagram-post-like: react, comment, and share are all available on any moment visible
to more than the owner. Reactions, comments, and share are all in for phase 1, no deferral.

**Visibility model for moments.**

1. Default, no user action: a moment inherits the visibility of the event it belongs to. Public
   event, public moment. Private event, visible to that event's participants only.
2. User override: the owner can set an individual moment to private, visible only to themselves,
   regardless of the event's visibility.
3. Governing principle: **most restrictive setting always wins**, not a fixed rule order. This is
   adopted as a general principle so it scales as more visibility settings get added later, not only
   for the two rules above.

**Private accounts, explicitly deferred.** A private-account toggle (limiting a user's moments to
followers) was raised as a natural extension of item 1's follow button, but the follow-request and
approval machinery it needs is new scope not previously covered anywhere in the walkthrough,
DEC-001 to DEC-009, or either draft. Decision: not phase 1. Every account is public for now; moment
visibility runs on the event-visibility rule plus the per-moment private override only. When private
accounts are built in a later phase, they slot into the same most-restrictive-wins principle without
needing a new rule.

**Consequences accepted.**

- This also resolves a secondary item on the list, the three different moment creation flows. The
  review aid flagged the brief's "IG moment" direction as leaning more social-feed than reflection,
  worth checking against the memory-keeping tone. This resolution settles that check: the social-feed
  interaction model (react, comment, share) is correct, but only for moments the owner has made
  visible beyond themselves. A private moment keeps the memory-keeping tone; a public one gets the
  full treatment. Not a contradiction, a resolution.
- Comments on public moments are a second commenting surface in the same post-event space, alongside
  the anonymous host-rating comment from item 1. Different rules (identity-attached and public vs
  anonymous and rating-attached), so they should read as visually distinct, not merged.
- Moderation load increases further on top of item 1's open moderation-staffing question (OQ-9),
  since public moment comments are now a second surface needing coverage.

**Flags carried forward, not decided here.**

- The share mechanism itself, in-app resharing versus an external share sheet, is an implementation
  detail for Deepak rather than a product decision made here.
- Recommend consolidating the visibility rules now spread across item 1 (per-submission feedback
  toggle), this item (moment visibility), and the deferred private-account concept into a single
  visibility model spec once all six items are resolved, rather than leaving them as separate
  fragments across decision entries.

---

## Item 5 - Video on moments and photo cap: RESOLVED

**Conflict.** Phase 1 Brief v2 allows video; the IG-style moment flow caps at 5 photos/videos
combined while the 3-step flow states no cap. Moments spec v0.9 is photos and text only, up to 10,
with video explicitly deferred to a later phase to avoid transcoding, storage, and upload-latency
cost at launch.

**Largely pre-settled by items 1 and 4.** Item 1's feedback-flow step 3 specified "photos and
videos." Item 4 confirmed moments run on an IG-style interaction model. Video is in. The only
question actually open was the cap.

**Resolution.** 10 items total, photos and video sharing one combined pool, for free users. Matches
the Moments spec's number rather than the brief's 5. One cap to explain in the UI and one limit to
enforce in the backend, rather than separate photo and video ceilings. Data model clarified
2026-08-19: a moment is one post per user per event, fixed at one for everyone, never a paid lever.
The 10-item cap is on media within that one moment, and it is where the individual premium tier's
media allowance (20 items) attaches; see `freemium-model-2026-08-19.md`.

**Consequence accepted.** Video's real cost (transcoding, thumbnailing, storage and bandwidth per
item, a longer upload with visible progress instead of near-instant photo upload) is now in scope
for phase 1, since the Moments spec's deferral is being deliberately overridden by item 1 and 4's
resolutions. Flag for Deepak's build estimate.

**Video technical spec (added 2026-08-19).** Raised directly by Elvis given the cost concern above.

- Resolution and frame rate: 720p (1280x720) at 30fps. Close to visually indistinguishable from
  1080p on a phone screen at normal viewing distance, roughly half the bitrate.
- Codec: H.264 (AVC) for phase 1. Universally compatible, simple pipeline. H.265 or AV1 would cut
  bitrate a further 30-50% at equal quality but add encoding complexity and compatibility risk;
  reasonable as a later optimization once real volume justifies it, not a phase-1 default.
- Bitrate target: approximately 3 Mbps at 720p30, a "good enough for a phone screen" target rather
  than broadcast quality, appropriate for a memory clip rather than a cinematic one.
- Build requirement, not optional: every upload is transcoded server-side regardless of source,
  since a camera-roll upload could arrive at 4K/25 Mbps with no way to control that at capture.
  Thumbnail generation for the grid is part of the same pipeline.
- **Length cap: 15 seconds, flat, for everyone in phase 1 (corrected 2026-08-19).** Originally
  written as 15 seconds standard / 30 seconds premium. The individual premium tier that would unlock
  30 seconds is now deferred (see `freemium-model-2026-08-19.md`), so no paid unlock ships in phase
  1. At the 3 Mbps target, approximately 5.6 MB per clip at 15 seconds.

**Flag, not decided here: the premium/paid tier itself.** No premium or paid tier appears anywhere
in the walkthrough, `shared/DECISIONS.md`, `shared/HOTSHEET.md`, or either draft. This is the first
place one has been introduced. Recording the video-length split as specified, but the premium-tier
concept is a pricing and business-model decision, and per `OWNERS.md`, pricing and the "dollar side
of scope classification" belong to Aakash as financials owner. This needs to route to him rather
than be treated as settled scope on the strength of a video-spec conversation. Added to the
escalation list at the bottom of this file.

---

## Item 6 - DMs, group chats, calendar phase markers: RESOLVED

**Conflict.** DEC-009 (ACTIVE) defers DM, user-created group chats, and the calendar to a later
phase, matching the walkthrough exactly, including a condition that DM/group chat should only defer
if they cannot be built one-shot with AI. The brief's own chat section text agrees, "no DMs in P0,"
but the draft still ships full direct message and create-chatroom screens with no phase tag, and the
calendar screens carry no phase marker at all. Unlike items 1, 4, and 5, this was not a real
disagreement about the decision, it was a labeling gap: screens contradicting the text next to them,
which reads as in-scope to anyone who has not seen this conversation, most importantly Deepak.

**Resolution.** Rather than fixing the label, phase 1 scope itself changes. DM and user-created group
chats are pulled fully into phase 1. Calendar is split: the full in-app calendar view moves to an
informal **phase 1.5** (not an integer phase per `CONVENTIONS.md`'s naming; if this is meant to
become a real contract phase with its own SOW and folder, that is Aakash's call as the phase-plan and
financials owner, flagged here rather than decided). Two lighter calendar pieces stay in phase 1.
This supersedes DEC-009's deferral of chat and calendar.

- **Chat.** Reasoning on record: core to the product experience, not primarily a build-difficulty
  call. Text-only stays, no audio or video chat, carrying the walkthrough's original constraint
  forward unchanged even though the feature itself is no longer deferred.
- **Calendar, phase 1 (revised 2026-08-19).** Two pieces, no in-app calendar UI for either:
  1. **Read-only busy-time ingestion.** Pull free/busy blocks from the device calendar to inform the
     recommendation engine, so events are not surfaced when the user is already busy. Privacy design
     requirement: neither iOS nor Android exposes a busy-only permission tier, granting calendar read
     gives full access to titles, locations, and attendees, so the app must extract only start and
     end times and discard everything else rather than storing it. Permission requested contextually,
     at the point it improves recommendations, not as a forced onboarding step, consistent with the
     O1 lean applied elsewhere this session.
  2. **Manual per-event write.** An "add to my calendar" action on a WePop event that writes that
     single event into the device calendar (native calendar intent or `.ics`). No ongoing sync, no
     calendar-read permission needed for this half.
  - **Calendar, phase 1.5.** The full in-app calendar, month and list views, as shown in the brief's
    calendar screens. Deferred, not built now.

**Consequences accepted.**

- This is the largest scope addition of the six items. Live messaging is infrastructure, not just a
  design surface: delivery, presence, and likely push notifications, on top of two other moderation
  surfaces already added today (host-rating comments from item 1, moment comments from item 4).
  Moderation staffing (OQ-9) was already an open launch blocker before this; it now covers a third
  surface.
- DEC-009 needs to be marked SUPERSEDED with a pointer to the new DEC per DECISIONS.md convention,
  not edited in place. Its "close to new joiners" and no-media-on-ideas provisions are unaffected and
  should carry forward into the new entry unchanged, only the chat and calendar deferrals change.

---

## Item 7 - Location at registration: RESOLVED

**Conflict.** Open question O1 since the walkthrough, also listed under Needs Attention on the
HOTSHEET. Aakash pushed for location required at registration; the walkthrough's lean was optional
and contextual; both drafts simply assumed optional, deciding it by default rather than by an actual
call. Interacts with item 3 (age gate): that resolution explicitly rules out ever forcing a device
GPS permission prompt at registration, so "required" could not mean an OS-level location ask without
reopening that decision.

**Resolution, 2026-08-24.** Splits into two distinct signals, deliberately kept separate rather than
conflated into one field or one ask:

- **A general city-level location, required at onboarding.** Typed or selected, for example picking a
  city or university from a list or search, not a device permission grant. This is the "required"
  half of Aakash's original push, satisfied without touching item 3's no-forced-GPS-prompt decision,
  since nothing OS-level is requested here.
- **Device GPS permission, optional, requested contextually rather than at registration.** If a user
  has not granted it, the app tells them plainly that recommendations will only be city-level accurate
  without it, not silently degraded with no explanation. The app re-surfaces this as an in-app nudge
  whenever the user hits a value point that benefits from precise location (for example, sorting
  events by distance, or a map view), rather than asking only once at signup and never again.

**Engineering note on the contextual reminder.** "Remind the user whenever they hit a value point"
should be read as an in-app nudge, not a literal repeated OS permission dialog. iOS allows the system
permission prompt once; Android caps re-prompts at two before requiring the user go to Settings
manually. Once the OS will no longer re-trigger its own dialog, the in-app nudge needs to deep-link to
the device's Settings screen instead, the standard pattern most consumer apps already use here.

**Kept distinct from item 3's country signal.** City-level location for discovery and recommendations,
and country for the age-gate legal-compliance cascade, are two different concepts serving two
different purposes (product personalization vs legal compliance) and should not be merged into one
signal or one field in implementation, even though both ultimately answer "where is this user." Item
3's cascade (app store region, then already-granted device location, then phone number country code)
stays exactly as resolved; this city field is not added to it as a fourth signal.

---

## Item 8 - Gender and photos pre-join: RESOLVED

**Conflict.** Elvis's own open question from the walkthrough, explicitly flagged as not settled by
DEC-006. DEC-006 establishes the anti-stalking model, aggregate-only visibility before someone joins
an event, but was written before two specific data types, gender and photos, were weighed on their
own; they carry very different risk.

**Resolution, 2026-08-24.**

- **Gender: aggregate ratio only, pre-join.** For example "roughly 60% women, 40% men," no individual
  attribution. Consistent with DEC-006 exactly as written, a real trust signal with no
  individual-identification risk attached.
- **Photos: not shown in an event's pre-join attendee list by default, except to a mutual follow.** A
  browser who has not joined the event does not see individual attendee photos, unless they and that
  specific attendee follow each other, both directions, not a one-way follow in either direction. A
  one-way follow must not unlock this: otherwise following someone, with no reciprocation and possibly
  without their awareness that it matters here, becomes a trivial way to learn whether a specific
  person will be at a specific place and time, exactly the surveillance vector DEC-006 exists to
  prevent. A mutual follow means both people already chose to connect with each other, so the
  visibility is reciprocal by construction, not one-sided.

**Distinction worth recording precisely.** This rule governs whether the pre-join *event attendee
list* surfaces a specific person's photo, not general profile-photo visibility. Since item 4 already
assumes public accounts for phase 1 (private accounts deferred), a stranger could likely already find
someone's profile photo by searching for them directly regardless of this rule. The actual risk being
protected against is not "can a stranger ever see this photo," it is "can a stranger learn, just by
browsing an event page, that this specific person will be at this specific place at this specific
time." That correlation, identity plus location plus time, is the dangerous combination DEC-006 was
written to prevent, not the photo by itself.

**Flag for Deepak.** Needs to check follow-state bidirectionally (both A follows B and B follows A)
when rendering an event's pre-join attendee list, not just whether the browser follows the attendee.
A single one-directional check would silently reopen the stalking vector this is meant to close.

---

## Item 9 - Undiscussed drafted surfaces: RESOLVED

**Conflict.** None of these ten surfaces came up in the 2026-08-17 walkthrough; the drafts introduced
them independently. QR check-in was already confirmed required as part of item 1 (it is the
attendance proof the whole Moments feature depends on). The remaining nine needed an explicit
phase-1-vs-later call each, per the review aid's own suggestion, rather than being silently carried
forward or silently dropped by omission.

**Resolution, 2026-08-24.**

Phase 1:

- **Waitlist auto-promote with a claim window.** Completes a mechanic that already exists as core
  scope (the waitlist itself is referenced throughout, including the org tier's free baseline), not a
  new feature.
- **Org ownership transfer.** Structural, not optional, for the target market: university club
  leadership turns over annually as officers graduate, and an org account with no transfer path
  becomes orphaned on a predictable, recurring schedule.
- **Org history / track-record module, public-facing.** A cold-start trust signal (event count,
  rating history) shown on an org's profile, consistent with the freemium model's own
  never-gate-trust-signals principle. Distinct from the private paid analytics dashboard already
  priced; this is a small, likely-already-collected slice of that same data surfaced publicly instead.

Later phase:

- ~~**Co-hosts**~~ **REVISED 2026-08-25, no longer purely later-phase.** Originally deferred here
  (invite another user as co-organizer, with permissions, on an individually-hosted event; org
  accounts already cover the multi-organizer case for clubs). Pulled forward to ship alongside Event
  Series once that concept needed "approved co-host" as a real permission for who can add events to a
  series, see `event-series-2026-08-25.md`. Kept as a record of the original call and why it changed,
  not deleted, per this repo's own convention for superseded entries.
- **Apply-to-join with host-defined questions**, as an alternative to simple RSVP. Real added scope
  (a question builder, an approval queue, applicant notifications) that phase 1's RSVP flow does not
  need to carry.
- **Sunday Deck** (swipeable event discovery stack). Needs real event density to be a good experience;
  density is explicitly the central go-to-market risk this project is still solving (`PROJECT_STRATEGY.md`),
  so this is a feature that benefits from density existing, not one that helps create it.
- **Wrapped, both org-level and individual-level, renamed to annual, not semester.** Corrects the
  review aid's original "semester Wrapped" framing per Elvis 2026-08-24. A natural companion to
  memories resurfacing below, both are retrospective features that benefit from there being enough
  history to look back on, which a new account will not have.
- **P1.2 memories resurfacing.** Confirmed matching the draft's own P1.2 tag.

Flagged as its own follow-up, not decided here:

- ~~Series pages (event lineage).~~ RESOLVED 2026-08-25, see
  `workspaces/elvis/recurring-events-2026-08-25.md`. Recurring events scoped in full (separate linked
  Event instances sharing a series ID, Google Calendar-style "this one / this and following"
  interaction across edit, delete, and join, batch-generated occurrences, both individual and org
  hosts). Series pages turned out to fall directly out of that design, an instance-embedded list of
  the other occurrences in its series, rather than needing to be a separate feature. Build still
  targeted for phase 1.5; this closes the design gap, not the build.

---

## Item 10 - Names, budget and legal in the Moments doc: ESCALATED

**What's in the draft.** Named engineering contact "Ratnadeep Deshmane" (confirm whether this is
Deepak under another name), "Joy Jeong (ops / legal)", a roughly $100K budget line, DLG Law as
counsel, and KPI targets.

**Why this is not resolved here.** Commercial and legal content, squarely `OWNERS.md` financials-owner
territory (Aakash), not a product or engineering call Elvis and I should be making in this file. No
design discussion attempted. Routes to Aakash as-is, same escalation path already used for the
premium-tier flag before it became the freemium model above.

---

## Where these land

`shared/DECISIONS.md` is merger-only. Resolved items get written into
`workspaces/elvis/proposed-decisions.md` using the format in `PROPOSAL-TEMPLATES.md`, and Aakash
lands them via run-merge. Items 1 and 2 also require edits to CLAUDE.md section 8 invariants, the
Moments spec v0.9, and the Phase 1 Brief v2 screens. Item 10 is commercial/legal content routed
directly to Aakash, not a DEC candidate. The freemium model (referenced in the old premium-tier flag,
now item-adjacent) has its own governance gap already flagged inside
`workspaces/elvis/freemium-model-2026-08-19.md`, unresolved as of this writing.

TASK-012 remains Blocked on TASK-010 (Elvis's reviewed documentation) on the board.
