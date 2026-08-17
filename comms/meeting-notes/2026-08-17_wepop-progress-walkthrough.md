# Wepop progress walkthrough - summary - 2026-08-17

> Synthesized meeting notes. Companion verbatim: `2026-08-17_wepop-progress-walkthrough_TRANSCRIPT.md`.
> Speakers normalized by role (the raw Fathom labels are swapped in places). Source recording:
> https://fathom.video/share/vz8mFFBynigDhjxeMpMsq_HfZS7Kfnor (91 mins).
> Scope note: the final ~12 minutes of the call covered a separate engagement (Dan / Reflex SEO
> and a voice-tutor product). Per the ingest scope decision, that portion was set aside and is not
> reflected in this Wepop summary or in any Wepop proposal. It remains verbatim in the transcript
> file under "Non-Wepop section".

## Attendees

- Aakash Dhar - PM (project owner, merger, financials).
- Elvis Ge - client and designer. Walked the full app design.
- Deepak Tewatia - tech lead and developer.

## Purpose

Design walkthrough of the Wepop app (a location-based events and meetup app) covering onboarding,
login, ideas, events, explore, chat, notifications, calendar, and profiles. Elvis is designing solo
and asked Aakash and Deepak for critique. No code was reviewed. First working session for Aakash on
this project (previously run by "Behata"); Deepak is also new to it.

## Product context (for grounding)

- Wepop is an invite-only, location-centric events and meetup app, positioned explicitly as "not a
  dating app" but a meetup app. Focus markets for now are Korea and the US.
- Invites are to a specific event or idea (not generic), issued by Elvis directly or by existing
  members, so a new user always lands on someone they know plus something to interact with.
- Non-invited users hitting the app store or landing page join a waitlist that collects email,
  phone, location, and university; that data guides where to expand next.
- Core objects: Events, Ideas (something someone wants to do without hosting it; others can spin an
  event out of an idea), and Business/Organization profiles.
- Existing Wepop code exists and will be salvaged and built on top of to shorten the timeline.

## Decisions reached (filed as proposals D1-D9 in workspaces/aakash/proposed-decisions.md)

1. Central GitHub repo as the single source of truth, plus a Cowork PM harness. Elvis shares his
   GitHub ID; Aakash creates the repo, invites Elvis, and runs a short setup call.
2. Age gating is tied to the user's country legal age. If the entered age is under a threshold
   (~19), trigger location permission early, check the country's legal age, and block under-age
   users with a message naming the country. Lawyer to be consulted on passive vs active location
   capture and travel-jurisdiction nuance.
3. Event location picker uses Google-Maps-style select (search plus tap a place, show the place
   name), not the Uber-style center-pin, with zoom, a text-address field, and an optional per-event
   note for the exact unit. Profile location only needs the general city.
4. Auth: OTP phone verification is required to verify the user; an optional password is also
   offered (fallback where SMS/OTP is regionally blocked, and enables reset). Biometric login if
   feasible.
5. Replace MBTI with an extensible tag list (MBTI values included as tags). Show the top 10-20
   common tags, searchable, user-extendable; feeds recommendation and event matching.
6. Anti-stalking visibility model: before joining, show only mutual friends' attendance plus
   aggregate signals (people near your age, area, and interests), not the full attendee list; lock
   fuller info until the user joins or marks interested; show mutuals' profile pics only. Whether to
   show gender and photos at all is still being debated.
7. No in-app AI image or video generation for now. The only AI the user interacts with is text
   prompt-to-create an idea or event. Rationale: quality concerns and token cost.
8. Salvage and reuse the existing Wepop code and build on top with AI, to reduce the timeline.
9. Phase-1 scope boundaries (defer to later phases): the idea "close to new joiners" toggle is
   built but not exposed in phase 1; calendar view plus device calendar (Google / iCal) integration
   is a later phase; chat ships event/group chat first, with DM and user-created group chats later
   if not one-shot with AI, and no audio or video chat for now (text only); no media upload on ideas
   (photos go in the discussion board).

## Design direction (feedback, not locked decisions)

- Location at registration: leaning optional and contextual rather than hard-required. App picks a
  default location and prompts "turn on location for personalized results" at the point of value;
  the invite flow needs no location. Not crisply closed in the call. (See open item O1.)
- Card density: two to three density versions (large-image vs compact text), toggled, with an
  expandable one-line detail so images are not covered.
- Business/organization profiles: any user can create multiple; two member types (regular and
  admin, with admins controlling whether members can create events/ideas) plus followers; privacy
  settings can gate content to members. Near-term use case is university clubs; promotional profiles
  (for example Spotify or Apple, Kickstarter-style validation before creating an event) are a later
  vision. "Moments" are post-event photo reflections on a profile.

## Open items and questions

- O1 - Confirm whether location at registration is optional/contextual (current lean) or required,
  and lock it. Owner: Elvis with Aakash.
- O2 - Map picker: one interaction detail Elvis and Deepak still need to finalize.
- O3 - How much of the legacy code is reused vs rebuilt with AI is not yet settled.

## Action items

See `comms/todos.md` for the tracked list. In brief: Elvis to generate and share the full project
documentation (doc/MD/HTML, V1 acceptable) and his GitHub ID via Slack today; Aakash to create the
repo, invite Elvis, and run the Cowork setup call; Aakash to consult a lawyer on the age/location
logic; Aakash to investigate pushing design output (HTML) from Cowork desktop to the repo; Elvis to
add the missing "save as draft" and profile-description screens and finish the profile screens.

## Risks flagged

- Cross-jurisdiction age verification is legally messy; do not lock the logic before counsel (R1).
- Solo-founder blind spot: Elvis explicitly asked for pushback (R2).
- OTP/SMS deliverability can be blocked by geography without an in-region registered business,
  relevant on expansion beyond US/Korea (R3).

See `workspaces/aakash/proposed-risks.md` for the register entries.
