# PROJECT_STRATEGY.md - Wepop commercial narrative and positioning

> Merger-only file (owner: PM / financials, Aakash). Proposals only from others. This is the
> commercial narrative. Keep the section skeleton; fill the content as the strategy firms up.
> No em-dashes. Where a point is not yet discussed, it is marked "to fill" rather than invented.
> Source grounding: Wepop progress walkthrough, 2026-08-17.

## What is being sold

Wepop is an invite-first, location-based events and meetup app. It helps people discover, create,
and join real-world events and "ideas" (activities someone wants to do without hosting), and to meet
people they would not otherwise meet. The app itself is treated as roughly half of the offering; the
other half is how the community is built and handled off the app (seeding, invites, curation). Near
term it targets university communities in Korea and the US.

## Market thesis

Event and meetup apps are established in the US and growing in Korea. The timing thesis is that the
current generation is fluent with AI and social media yet increasingly wants real-world experience
and connection rather than pure screen time. Wepop aims to use the engaging design patterns of
social apps for a pro-social end (getting people out to do things together) rather than for
maximizing time-on-app.

## Moat

- Cold-start solution: invites are always to a specific event or idea, so a new user always arrives
  to someone they know plus something live to join. This is the hardest problem for a local network
  and the core defensibility.
- Community handling off the app (invite curation, where to expand next) as much as the software.
- Mission-driven, privacy-by-design product stance (anti-stalking, no in-app AI media) as brand
  differentiation against generic social clones.
- Waitlist data (location, university) that guides expansion into dense pockets of demand.
- To fill: durable network effects and switching costs once density is achieved.

## Build vs integrate

- Build: the app experience, on top of an existing Wepop codebase salvaged and extended with AI, to
  shorten the timeline. Design by Elvis, technical build by Deepak.
- Integrate: maps and place data for the location picker; phone OTP messaging (for example Twilio),
  with a password fallback where regional messaging is restricted; device calendars (Google / iCal)
  in a later phase.
- Explicitly not building: in-app AI image or video generation. The only AI the user touches is text
  prompt-to-create for an event or idea.

## Go-to-market

- Invite-only seeding at the start, from Elvis directly and from existing members, always tied to a
  specific event or idea.
- Public / app-store interest routes to a waitlist that collects email, phone, location, and
  university; that data selects the next expansion areas and universities.
- First communities are university clubs (multi-member organization profiles). Later, promotional
  organization profiles (for example a Spotify or Apple) can validate interest via ideas before
  committing to an event, Kickstarter-style.
- To fill: paid acquisition, campus ambassador model, launch sequencing per market.

## Commercial structure

- To fill: pricing model, revenue model, and any phase / SOW structure and payment terms. Not
  discussed in the 2026-08-17 walkthrough. Dollar detail lives in `contracts/`.

## Risks to the narrative

- Cold-start still has to be executed well per location; density is the make-or-break.
- Solo-founder blind spot: Elvis is designing alone and has asked for structured pushback.
- Cross-jurisdiction legal exposure on age gating and location handling (see `shared/HOTSHEET.md` and
  the risk register).
- "Just another Instagram/event clone" perception if the mission-led differentiators are not visible
  to users.
- The no-AI-media stance is a deliberate brand bet that could age as user expectations shift.
