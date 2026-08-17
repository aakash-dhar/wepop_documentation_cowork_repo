# Wepop product overview - app feature map and phase-1 scope

> Owner: Aakash (phase-plan). Operational product map derived from the 2026-08-17 design walkthrough
> with Elvis. Design detail is Elvis's (`architecture/elvis/`); technical detail is Deepak's
> (`architecture/technical/`). This file is the shared, plain-language map of what the app does.
> No em-dashes. Contested points defer to `shared/DECISIONS.md`.

## One-liner

An invite-first, location-based events and meetup app. Get people together in the real world around
shared activities. A meetup app, not a dating app.

## Core objects

- **Event** - a concrete activity at a place and time, with details, a discussion board, media, and
  chat.
- **Idea** - something a user wants to do without hosting it. Others rally around it (interested /
  polls for time and place) and can spin an event out of it. Ideas have no fixed date.
- **User profile** - the person. Onboarding data (age, location, gender, languages, personality
  tags, interests, university), plus followers, created events/ideas, saved items, and moments.
- **Business / Organization profile** - multi-member account (regular members, admins, followers).
  Admins can let members create events/ideas; privacy settings can gate content to members.
  University clubs first; promotional accounts (for example Spotify, Apple) later.

## Screen / feature areas

- **Waitlist** - for non-invited users who find the app store or landing page. Collects email,
  phone, location, university. Feeds expansion decisions.
- **Onboarding (invited)** - shows who invited you and to what, then join or log in. Three-step
  intro to the app.
- **Registration** - phone number plus OTP verification (required), optional password, optional
  biometrics. Birthday / age with country-tied legal-age gating. Username with generator. Location
  via a Google-style map picker (search plus tap, place name shown), profile location is general
  city only. Then optional profile photo, gender, languages, personality tags, interest categories,
  university, and permissions (notifications, photos now; contacts and calendar later).
- **Login** - single input that auto-detects phone / email / username, with a dropdown to override;
  forgot-password flow; biometrics.
- **Ideas** - summary before joining, then details, discussion board, and time/location polls (map
  view with per-location notes). "Close to new joiners" toggle is built but not exposed in phase 1.
- **Events** - similar to ideas with a fixed place and time; details, discussion, media, chat.
  Create from an idea without re-prompting. Save-as-draft screen still to be added.
- **Explore** - map view with a bottom list tray ("local vibe" style), toggle to full list view,
  filters (date, type, distance), and search across events, ideas, and users, scoped to a location.
- **Home** - recommended things for you.
- **Chat** - event / group chat first (text, photos, replies, reactions). DMs and user-created group
  chats later if not one-shot with AI. No audio or video chat for now.
- **Notifications** - invites, follows, event/idea activity. Simple set now, more later.
- **Calendar** - things you are going to / interested in, list or calendar view. Later phase.
- **Profiles** - user and organization, with cover plus profile photo, full vs list density views,
  moments (post-event photo reflections), and a planned rating system for event creators.

## Privacy and product principles

- Pre-join, show only mutual friends plus aggregate signals (people near your age, area, interests),
  not the full attendee list. Lock fuller info until the user joins or marks interested.
- Show only mutuals' profile pictures pre-join. Whether to show gender and photos at all is still
  being debated.
- No in-app AI image or video generation. The only AI the user touches is text prompt-to-create for
  an event or idea.

## Phase-1 scope boundaries

In phase 1: build but do not expose the idea "close to new joiners" toggle; defer calendar view and
device calendar (Google / iCal) integration; ship event/group chat first (DMs and user group chats
later, no audio/video); no media upload on ideas (photos go in the discussion board).

## Open items

- Location at registration: optional/contextual (current lean) vs required. Not yet locked.
- Map picker: one interaction detail still to be finalized by Elvis and Deepak.
- How much legacy code is reused vs rebuilt with AI.
- Age/location logic pending legal counsel.
