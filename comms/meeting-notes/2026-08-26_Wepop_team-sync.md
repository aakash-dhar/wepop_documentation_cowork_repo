# Wepop team sync - 2026-08-26

**Attendees:** Aakash (PM), Elvis (client/designer), Deepak (tech lead)
**Verbatim:** [2026-08-26_Wepop_team-sync_TRANSCRIPT.md](2026-08-26_Wepop_team-sync_TRANSCRIPT.md)

## Note on the transcript

The auto-transcript's speaker labels are badly scrambled (many Elvis and Aakash lines are swapped).
This summary resolves speaker intent from context; the verbatim file is left uncorrected.

## Summary

Mostly a recap and coordination call. Elvis has been pushing design and doc updates since Monday
(2026-08-24); Aakash confirmed he pulled the cohorts/algorithm updates and landed them into the
decision record (DEC-010 to DEC-025). No blockers.

**Workflow confirmed for Deepak.** Just commit and push to origin, no merging. Capturing pushes into
the shared record and running the merge is Aakash's job. Deepak was added to the BetaCraft repo
(GitHub id `deepak1-1` per the call) and will pull it, set up a Cowork session reading from the repo
for UI answers, and research the Korean PASS technology.

**Recap of already-landed design (no change).** Elvis re-walked recurring events vs event series
(event series behaves like an idea hub but only the host can add events, DEC-021/DEC-022), the
recommendation algorithm and internal Netflix-style tagging/embeddings (DEC-020, DEC-005), and
community cohorts as a recommendation filter rather than separate servers (DEC-019). Aakash noted the
cohort filtering can double as a marketing angle ("recommendations by your age and interest, we do
not push older or boomer events at you"). Elvis clarified the follow graph should cut across cohorts:
if you follow someone (for example your mother, older and not in college) their events should rank
higher rather than be hidden, since the connection implies you know each other. Personalized per-user
weighting (Spotify-style) was reaffirmed as a later phase (DEC-020).

**New this call.**
- **A/B testing embedded early.** Elvis pushed a concept for A/B experimentation (push a change to
  group A, monitor against group B) for design, usability, and algorithm changes, so the team can
  learn fast post-launch. Phase not fixed; "seems good earlier than later," depends on build difficulty.
- **Korea PASS authentication.** Korean carrier phone numbers are tied to government identity, so for
  Korean numbers the plan is to verify via PASS (the common Korean carrier auth) rather than
  Twilio/OTP, getting success/fail and likely identity/age back through its API. A freelancer may help
  with Korea-specific integration.
- **Korea localization.** The app detects device language and serves the Korean version to
  Korean-language devices, user-switchable.

**Korea flags (deferred, not decided).**
- **Maps:** Korea has its own map providers with better local data (South Korea restricts map-data
  export); Google Maps is expanding coverage in Korea. Google is acceptable for now (DEC-003); revisit
  only if it becomes a real issue.
- **Payments:** Stripe is not usable in Korea, so payments will need multiple methods (card or a Korean
  gateway), detected per user. App-store IAP was discussed: 15 to 30 percent fees, the virtual-goods
  vs physical-experience distinction (a physical event ticket is not an app-store in-app purchase),
  and the web-payment workaround (Netflix pattern). All deferred to the payments conversation (phase
  1.5). Aakash can help source a cheaper India-style gateway when the time comes.

**Elvis's task for the day:** go feature by feature through phase 1 (sign-up, onboarding, home,
explore, creation, ideas, events) to verify the docs match his intent and Claude's understanding is in
sync, then finalize the design screens. He will ping Aakash on each push to pull and merge.

## Items filed from this call

- Proposed DEC-026 (Korea PASS auth), DEC-027 (localization), DEC-028 (A/B testing), and a DEC-019/020
  follow-exemption refinement - `workspaces/aakash/proposed-decisions.md`, pending merge.
- HOTSHEET watching items (Korea payments, Korean maps) - `workspaces/aakash/proposed-hotsheet.md`.
- Compliance register updated for Korea PASS / real-name verification.
- Todos #14 (Elvis phase-1 review), #15 (Deepak repo pull + PASS research); TASK-036 note on Korea payments.
- Follow-up: Elvis's latest push ("updates regarding tags & korea/eng") is new workspace design content
  to run through design-intake / a workspace intake next.
