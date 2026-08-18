# Wepop: what you said in the walkthrough vs what the drafts produced

*A review aid for Elvis, built from the 2026-08-17 design walkthrough transcript, checked against the two drafts you shared: **Phase 1 Design Brief v2** and **Moments & Reflections BRD + Eng Spec v0.9**.*

**How to use this.** Most of both documents faithfully reflects the walkthrough. This sheet only surfaces the places worth your eyes: where a draft made a different call than you stated, where the two drafts disagree with each other, where something appears that was never discussed, and where a point is still genuinely open. Both drafts are your own unreviewed versions (the Moments doc is v0.9 with its own open items), so nothing here is a correction, just a fast path to your review.

**Status key**

- **MATCH** - reflects what you said or a locked decision
- **CHANGED** - the draft made a different call than you stated
- **ADDED** - in the draft, not discussed on the call
- **DOCS DISAGREE** - the two drafts contradict each other
- **OPEN** - left unresolved on the call

---

## Start here: the six worth confirming first

1. **Ratings and reviews.** Your Phase 1 Brief includes a rate-the-crew step and profile rating / review screens. Your Moments spec bans ratings and reviews outright as against the product identity. The two drafts take opposite positions.
2. **Login: Kakao and OTP.** The brief makes Kakao dominant and skips OTP when Kakao returns a verified phone. On the call you said OTP still verifies every user, and you would add a password field. The brief drifts on both counts (Kakao dominance and the OTP skip); the Moments spec does not touch login.
3. **Age gate: 18 vs 19.** You landed on a country-tied age with a trigger around 19 and a country-named block. Both drafts show a flat 18+ gate.
4. **Comments on moments.** The brief has a "comments open" moment screen. The Moments spec says no comments at launch and to not even reserve space for them.
5. **Video on moments.** The brief's moment flow takes photos and videos (up to 5). The Moments spec is photos and text only for this release, up to 10, with video deferred to a later phase.
6. **DMs and calendar.** You said DMs, user-made group chats, and the calendar are later-phase. The brief's chat section text does say "no DMs in P0", yet it still ships full DM and group-chat screens; and the calendar screens carry no phase marker at all.

---

## Onboarding, login and identity

### Onboarding structure and invites - MATCH

- **You said:** Invite-only to a specific event or idea, so a new user lands on someone they know plus something to do; non-invited users hit a waitlist collecting email, phone, location, university; a three-step intro.
- **Drafts produced:** Welcome, invited-flow, and onboarding screens match this closely.
- **To confirm:** Nothing. Faithful.

### Age gate: country-tied vs flat 18+ - CHANGED

- **You said:** Age tied to the country's legal age. If age is under a threshold (around 19), trigger location early, check the country, and block under-age users with a message that names the country. US 18, Korea 19.
- **Drafts produced:** Both drafts show a single flat **18+** gate ("Age gate 18+", "만 18세"). The country-tied logic and the ~19 trigger are not reflected.
- **To confirm:** Keep the country-tied logic (locked as DEC-002, still pending legal counsel), or simplify to flat 18+. If country-tied stays, the screens need the location-first trigger and the country-named block.

### Login: Kakao dominance and skipping OTP - CHANGED

- **You said:** Social auth is an option, but "at the end of the day we still need to collect their phone number to verify that user." OTP verifies everyone. You also said you would add a password field for reset and for regions where SMS/OTP is blocked.
- **Drafts produced:** The brief makes **Kakao visually dominant and skips OTP when Kakao returns a verified phone**. No password screen appears in the auth set.
- **To confirm:** Two things: is it acceptable to skip OTP on a Kakao-verified phone, or must OTP always run (DEC-004 says OTP verifies every user); and is the optional password still in, since it is missing from the screens.

---

## Location and maps

### Map picker style - MATCH

- **You said:** Google-Maps-style: search and tap a named place (not the Uber center-pin), with zoom, a text address field, and an optional per-event note for the exact unit. Profile location is only the general city.
- **Drafts produced:** Place picker with search and drop-a-pin, specific-address entry, per-event note, and location polls. Matches DEC-003.
- **To confirm:** Nothing structural. One picker interaction detail you and Deepak parked (O2) is still yours to close.

### Location at registration: required or optional - OPEN

- **You said:** You leaned optional and contextual: pick a default location, then prompt "turn on location for personalized results" at the point of value; the invite flow needs no location. Aakash pushed to make it required. Left unresolved on the call (O1).
- **Drafts produced:** The onboarding treats location as optional / contextual with later inline prompts, which is your lean, but effectively makes the call for you.
- **To confirm:** Lock optional-contextual vs required. The drafts assume optional; confirm that is the decision.

---

## Profile fields and matching

### MBTI replaced by tags - MATCH

- **You said:** Drop the MBTI selector for an extensible, searchable tag list (MBTI values as tags), top 10-20 shown, user-extendable, feeding matching.
- **Drafts produced:** Interests / tags picker ("pick 3+"). Matches DEC-005.
- **To confirm:** Nothing.

### Anti-stalking visibility before joining - MATCH

- **You said:** Before joining, show only mutual friends plus aggregate signals (people near your age, area, interests), never the full attendee list; mutuals' profile pictures only. Whether to show gender and photos at all is still your open debate.
- **Drafts produced:** Details-before-join shows summary and aggregate only, no attendee names, with a followers-only visibility chip. Matches DEC-006.
- **To confirm:** Your own open question stands: show gender and photos at all, or not. The drafts do not settle it.

### No in-app AI image or video generation - MATCH

- **You said:** No AI image or video generation; the only AI a user touches is text prompt-to-create for an idea or event.
- **Drafts produced:** AI limited to text suggestions in create; no generation. Matches DEC-007.
- **To confirm:** Nothing.

---

## Chat, notifications, calendar

### DMs and user-made group chats - CHANGED

- **You said:** Event and group-event chat first. DMs and user-created group chats are later, and only if they cannot be done one-shot with AI. No audio or video chat, text only.
- **Drafts produced:** Text-only chat matches, and the brief's chat section text says "no DMs in P0". But it still ships full **Direct message (1:1)** and **Create chatroom** screens, so the section text and the screen set disagree with each other.
- **To confirm:** Fine to have designed ahead, but make the screens carry the later-phase marker your section text already implies, so they are not read as phase 1 (DEC-009).

### Calendar - CHANGED

- **You said:** Calendar is nice to have but likely a later phase; it connects to the device calendar.
- **Drafts produced:** Calendar month and list screens are present with no phase marker.
- **To confirm:** Tag calendar as later-phase (DEC-009), or pull it into phase 1 deliberately.

---

## Ideas and events

### No media upload on ideas - MATCH

- **You said:** Ideas get a cover photo only; no media gallery on ideas for now, photos live in the discussion board.
- **Drafts produced:** Idea has a cover image and a "no image" variant, no media gallery. Matches DEC-009.
- **To confirm:** Nothing.

### "Close to new joiners" toggle - OPEN

- **You said:** Build the "close to new joiners" control but do not expose it in phase 1, since a new app wants more joiners.
- **Drafts produced:** The idea hub references closing to new people. Whether it is exposed as a phase-1 control is not clear from the screens.
- **To confirm:** Check the idea screens keep this built-but-hidden in phase 1.

---

## Profiles and ratings

### Ratings and reviews - DOCS DISAGREE

- **You said:** On the call: "once we do feedback for events, I think we'll start adding some rating system for people," so you can see how a host is doing.
- **Phase 1 Brief:** Includes a rate-the-crew feedback step, profile "with rating," and Reviews screens (others positive-only anonymous; mine positive plus improvement).
- **Moments spec:** Explicitly excludes ratings, stars, 평점, and "would you recommend" as excluded by product identity, and bans review vocabulary everywhere.
- **To confirm:** Your two drafts point opposite ways. Decide: a rating / review system in, or the anti-review stance from the Moments spec. This one shapes a lot downstream.

---

## Moments and Reflections

### Comments on moments - DOCS DISAGREE

- **You said:** On the call, a moment is a post-event reflection: upload photos and write your thoughts. Comments were not mentioned.
- **Phase 1 Brief:** Has a "Posted moment, comments open" screen.
- **Moments spec:** No comments at launch, reactions only, and explicitly "do not reserve layout space for a comment affordance."
- **To confirm:** Remove or defer comments to match the spec, or change the spec. They cannot both stand.

### Video on moments and photo count - DOCS DISAGREE

- **You said:** A moment is photos plus your written reflection (no explicit photo-only-vs-video call on the record).
- **Phase 1 Brief:** Allows video. The IG-style moment flow caps at **5 photos/videos**; the other (3-step) moment flow states no cap.
- **Moments spec:** **Photos and text only** for this release, up to **10**; video deferred to a later phase.
- **To confirm:** Reconcile video in or out for launch, and the 5-vs-10 photo cap.

### Three different moment creation flows - CHANGED

- **You said:** A simple reflection created after an event.
- **Drafts produced:** The brief shows three patterns: a 3-step "Create moment," a 5-step "IG moment," and the ported Reflections composer with three entry doors. The Moments spec calls for **one composer, three doors**.
- **To confirm:** Pick one composer. The "IG moment" direction also leans more social-feed than reflection, worth a look against the memory-keeping tone you want.

---

## Introduced in the drafts, not discussed on the call

### New product surfaces the AI added - ADDED

- **In the drafts:** Event **check-in with QR** (host QR, attendee scan), **Sunday Deck** (swipeable event stack), **waitlist with auto-promote** and claim window, **co-hosts** (invite and permissions), **apply-to-join** with host questions, **series pages** (event lineage), an **org history / track-record module**, **org ownership transfer**, and P1.2 **memories resurfacing** plus a semester **Wrapped**.
- **Note:** None of these came up in the walkthrough. One is load-bearing: **check-in** is the attendance proof the whole Moments feature depends on, so it is good it exists, but confirm it is really in the first build.
- **To confirm:** Scan this list and keep what you want for phase 1; mark the rest later-phase so the scope stays honest.

### New names, budget and legal assumptions in the Moments doc - ADDED

- **In the draft:** The Moments spec names BetaCraft engineering as "Ratnadeep Deshmane" (the named engineering contact), a "Joy Jeong (ops / legal)," a roughly $100K budget line, DLG Law as counsel, and specific KPI targets (all tagged as proposed).
- **To confirm:** Confirm the names (is "Ratnadeep Deshmane" the same person as Deepak?), and note the budget figure and legal-counsel reference are commercial and should be checked with Aakash before they sit in a shared doc. Also OQ-9: who staffs moderation at launch.

---

## Open questions your own spec raised

### The design-blocking few - OPEN

- **From the spec:** OQ-1 check-in confirmed in the first build, plus a fallback if the check-in rate is low; OQ-2 is "새 연결 N" a global count or per-viewer (it changes whether the recap card is shareable); OQ-9 who staffs moderation and the SLA.
- **To confirm:** These three gate design decisions. The full OQ-1 to OQ-10 list in the spec is a good checklist for your pass.

---

*Prepared from the 2026-08-17 walkthrough transcript and the two draft files Elvis shared (Phase 1 Design Brief v2, Moments & Reflections v0.9). Draft for Aakash to review before sending to Elvis. Based on unreviewed drafts; a revised version was expected the following day. No em-dashes; governance values ALLOW / BLOCK / ESCALATE.*
