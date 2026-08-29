# Elvis - Session Log

> Append each session summary here. Most recent at top. This is the audit trail of your work.

---

## 2026-08-29 - Handoff spec v0.9 intake: six conflicts with ACTIVE decisions found and resolved,
scoring model designed, six proposals filed; stale-repo drift caught and corrected

Elvis brought in `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx`, a large consolidated
engineering/design handoff, while item #7 of the phase-1/1.5 list (Events + Ideas core objects) was being
opened. It reached far wider than item #7. Read against `shared/DECISIONS.md` rather than against its own
stated baseline (it declares supersession over three drafts that are not in this repo and never references
DECISIONS.md), it conflicted with six ACTIVE decisions; taken at face value it would have silently reversed
all six. All six were walked to resolution with Elvis (`handoff-spec-v0.9-intake-2026-08-29.md`). Ratings are
NOT removed, DEC-014 stands; the only intended change is dropping attendee thumbs-down and the follow-all
affordance, making peer feedback positive-only. Caught that the handoff's own new invariant I-12 forbids host
ratings on its face, confirmed with Elvis that host and attendee rating are separate concepts, and drafted
replacement wording carrying that distinction. Check-in decouples from Moment and feedback eligibility, with
a visible badge plus invisible algorithmic weight; designed the full scoring model (1.0 verified / 0.4
unverified, minimum 3 verified before any public star average displays, Bayesian smoothing with C=5 on the
internal signal to protect DEC-020's new-host boost from a single early bad rating), and named the integrity
risk neither document had noticed, that DEC-014's hard gate had been quietly ensuring only real attendees
could rate and a no-show now can. Gender hidden from the attendee-facing pre-join aggregate, partially
superseding DEC-017; separately confirmed DEC-017's mutual-follow-only photo rule is untouched, since the
handoff's silence on it would otherwise have been read as assent either way. Media retention resolved at a
6-month tiered boundary active at launch as a paid differentiator (Elvis's own third position, neither
document's), with three refinements recommended: restore-from-cold rather than exemption-from-demotion for
Wrapped, the same path extended to P1.2 memories resurfacing, and a ~1080px mid tier so 400px is not what a
free user sees of their own memory. DEC-015/DEC-018 media caps confirmed to stand; new event-cover caps set
at 5 items, 15s free / 30s paid. Ran real cost math on Elvis's question about shortening video and
recommended against it (a free-tier Moment of video costs about half a cent to hold for the whole window;
clip length is not the lever, retention is), while finding where the exposure actually is: 50 items at 30s at
an org-paid event is 25 minutes of video in one Moment, a moderation problem before a storage one, answered
by a total-duration-per-Moment cap the handoff proposes but never numbers. Avoid signal becomes block-only
per Elvis, with absence-of-positive explicitly considered and rejected, and the positive tap redirected into
a positive affinity ranking signal so the DEC-023 amendment is not purely subtractive. Also closed the scope
matrix's own open question on general user blocking (phase-1 baseline, fully designed, earliest wave) and
most of item #7 itself (Event vs Idea structural definition, Discussion as the persistent surface, a
seven-status event lifecycle, polls unified into one primitive). Six proposals filed, all awaiting merger.
Mid-session, on Elvis asking whether anything was staged for the repo, found the session had been reading a
stale Aug-27 uploads snapshot while the live clone had moved on: the merger landed DEC-029 through DEC-033 on
2026-08-28 and cleared the queue, and the locally assembled proposal file still carried all five already-
merged items, which would have re-proposed landed decisions. Rebuilt against the live clone.
Open: all six proposals awaiting merger, the retention one additionally needing Aakash since the window is a
direct input to DEC-018's cost model; three retention refinements and the video total-duration cap are
recommendations not yet confirmed; whether org-paid lifts Moment video to 30s is still unspecified in
DEC-018. Not yet worked: the DM/group-chat gap (DEC-013 unmentioned in the handoff), four new scope-matrix
rows, two legal items for TASK-013 (L-3 geofence, BLOCKING before P0; L-8 PIPA under-14 guardian consent),
adopting the I-N invariant scheme into CLAUDE.md, the wave-to-phase label mapping, and the sign-off pass on
[D]-tagged items. DEC-009's "close to new joiners" toggle still unanswered. No `shared/` edits made.

**Detail:** [session_log_2026-08-29.md](session_log_2026-08-29.md)

---

## 2026-08-27 - Age gate research filed to counsel, home location fully reworked (granularity, mutability,
Explore country gate), paid-tier features scoped, event location map picker closed out with real market
research

Continued the phase-1/1.5 review list from item #3. Filed age-gate research to TASK-013
(`age-gate-country-cascade-2026-08-27.md`): flagged DEC-012's own reasoning conflating age-of-majority with
GDPR digital-consent age, and Apple's Declared Age Range API as a platform-native alternative worth putting
to counsel; DEC-012 stays provisional, unchanged. Item #4, home location, went through several real
revisions in one file (`city-location-registration-2026-08-27.md`): input reuses the DEC-003 map picker,
granularity revised from city down to neighborhood-scale once Elvis caught that city-level starved
DEC-020's `geo_distance` ranking of real precision, mutability revised to current-location-only
(GPS-confirmed) with no fallback for a user who never grants permission (Elvis's explicit call against my
recommendation), and DEC-019's cohort formula revised to drop location entirely (student-vs-not only) after
correcting my own oversimplification about how geographic relevance actually works in DEC-020. Elvis then
proposed, refined, and had me flag for Aakash specifically an Explore content gate by country as an
individual-premium perk, reusing the DEC-006/DEC-017 aggregate-teaser pattern; flagged rather than filed as
routine because DEC-018 explicitly locks out paid discovery boosts and this needs Aakash's own read against
that rule. Confirmed item #5 (personality tags) already done via files from earlier the same day. A detour
into paid-tier feature design (`paid-tier-features-2026-08-27.md`) resolved apply-to-join screening
questions at 3 free / 10 paid (filed), surfaced two low-effort next candidates (live stories, icebreakers),
and corrected an over-reach on my part, Explore's filters (multi-category, host-quality, date range) got
reclassified from premium candidates to ordinary free functionality once Elvis pointed out they're core
discovery, not power-user extras. Closed out item #6, the event location map picker
(`event-location-map-picker-2026-08-27.md`), resolving a walkthrough flag that had carried unresolved since
2026-08-17 with no detail ever recorded: one map component in two modes serving three surfaces (event/idea
location, newly-scoped location polls, Explore), zoom-determines-precision with no minimum floor after
Elvis corrected my initial instinct on it. Escalated the HOTSHEET's Korea map-coverage "watching" item to an
actual decision point after researching that Google's Feb 2026 conditional map-export approval has stalled
with no timeline; researched dual Google/Naver feasibility (Elvis's own simplification, locked per session,
no live cross-border swap, no visual wrapper for now, removed most of the real difficulty); caught and
corrected an unverified claim of my own about precedent companies, then found real supporting evidence on a
second pass (`react-maps-loader`, a real open-source project combining both providers) alongside the
higher-severity China/Baidu analogy, honest throughout about what searching could and couldn't confirm.

Open: none of today's four proposed decisions (DEC-019 revision, DEC-016 refinement, the Explore
country-gate extending DEC-018, the apply-to-join quota extending DEC-018) merged yet; the country-gate
specifically needs Aakash's explicit sign-off against DEC-018's own rule before normal merger; whether a
non-Korean-registered business can even open a Naver or Kakao developer account is unresolved and needs an
actual signup attempt, not more research; location-poll mechanics (min/max options, vote changeability,
anonymity) not decided; items #7 onward of the phase-1/1.5 list not yet reached. No `shared/` edits made.

**Detail:** [session_log_2026-08-27.md](session_log_2026-08-27.md)

---

## 2026-08-26 (session 2) - Live team-sync synced, language switch resolved, four new features scoped,
full onboarding and auth flows detailed; six proposals filed to the merger

Synced the live team-sync's follow-graph cohort-filter exemption into two files. Fully closed out the
language-switch open items in `internationalization-korea-2026-08-26.md`: cascade confirmed one-time not
ongoing, day-one full bilingual coverage for WePop's own copy (UGC stays as-authored), notifications follow
the same profile field, and a new "Give Feedback" entry point landing in a dedicated Admin Portal table.
Scoped shake-to-create as a new feature (`shake-to-create-2026-08-26.md`), gesture-triggered creation tray,
suppressed during active input, its own open-only behavior kept explicitly distinct from its settings
toggle. Reviewed the phase 1/1.5 list and resolved three placements: private accounts into phase 1
(`private-accounts-2026-08-26.md`, superseding DEC-015's deferral, whole-profile gating with
follow-request approval), general user blocking confirmed phase 1 (resolving an open DEC-023 dependency),
apply-to-join given a firm phase 1.5 slot and extended to org accounts too. Scoped org invites as a new
invite mechanism (`org-invites-2026-08-26.md`), admin-only in phase 1, a deliberate scoped exception to the
invite-first invariant (organizational identity substitutes for event/idea specificity), landing on a
discussion board. Assembled the full onboarding flow end to end for the first time
(`onboarding-flow-2026-08-26.md`): a single shared "Get Started" screen for every entry path (individual,
org, a new third founder-seed invite type, and organic/waitlist) with an invite-context toast layered on
for invited paths and a persistent language selector instead of a one-time confirmation toast; a full
15-step account-creation sequence built from Elvis's own detailed walkthrough; optional email, password,
and description moved out of onboarding entirely into profile settings with reminder nudges. Reviewed item
#2 of the phase list, auth, in the same depth (`auth-flow-2026-08-26.md`): multi-credential returning
login with phone as the durable anchor, biometric quick-unlock as a local session gate, an always-active
Instagram-style persistent session validated against industry standard with two flagged safeguards
(iOS Keychain-reinstall handling, server-side revocation capability), and an account-linking flow revised
mid-session from Elvis's own initial silent-auto-link answer to the actual industry-standard pattern
(verified-phone login plus explicit opt-in consent) once he asked to align to standard practice instead.
Filed six real decisions to `proposed-decisions.md` this session, all still awaiting merger: language
storage/cascade/scope, private accounts into phase 1, apply-to-join's phase 1.5 placement, user blocking
confirmed phase 1, org invites as a scoped invite-first exception, and the DEC-011 password-field
reversal (updated in place once its design moved from onboarding to profile settings).
Open: items #3 onward of the phase 1/1.5 list not yet reviewed in this detailed style; several flagged
sub-questions remain across every file touched this session (username-change login continuity, multi-device
session management, and the customer-service recovery workflow on auth; founder-seed-invite copy and
reminder cadence on onboarding); none of the six proposals filed this session, or any filed previously,
have actually been merged yet. Item 10 still hasn't actually been sent to Aakash, not touched this session.
No `shared/` edits made this session, all writes stayed in `workspaces/elvis/`.

**Detail:** [session_log_2026-08-26_session2.md](session_log_2026-08-26_session2.md)

---

## 2026-08-26 - Embeddings/tagging pipeline, robustness roadmap, internationalization, and Korea-user
detection resolved; first proposal filed to the merger
Second start-session of the visible stretch (first re-verified Aakash's large DEC-010 through DEC-025
merge against the actual repo state rather than assuming the earlier briefing still held, catching one
real stale-doc discrepancy in CLAUDE.md section 8, flagged rather than fixed unilaterally). Elvis then
worked through four linked topics. Resolved how embeddings and hidden internal tags actually get
generated, since Elvis correctly identified this cannot be manual
(`recommendation-algorithm-2026-08-25.md`): a create/edit-triggered pipeline (embedding model call plus
LLM-based tag extraction) for content, pulled into launch scope since it needs no behavioral history,
versus a periodic batch job refining user-side embeddings from engagement data, deferred until real usage
exists. Scoped a day-1-versus-later robustness roadmap: basic experimentation/bucketing capability
resolved for day 1, impression/position logging and deletion handling explicitly deferred by Elvis
despite the retroactive-data-loss tradeoff already being explained, and anti-gaming reframed away from a
rate-limiting system toward account integrity (one personal account per phone number, ID verification
later, Org accounts always traceable to a specific user, reviews already gated to checked-in attendees).
Then scoped internationalization and Korea-specific concerns in a new file
(`internationalization-korea-2026-08-26.md`), grounded in real research rather than assumption: full i18n
architecture from day one with on-demand UGC translation explicitly deferred, a bilingual tag vocabulary,
a flexible full-name field for Korean naming order, and on the Korea side a genuine gap found in DEC-010's
Stripe-only payments plan (escalated to `proposed-hotsheet.md`, the first proposal filed to the merger in
over three sessions), Bumble's actual Korea ID-verification flow strengthening the already-provisional
DEC-012 age gate, a resolved plan to adopt Korea's carrier-based PASS verification, and three concrete
PIPA points tied directly to the embedding/tag layer. Closed with a Korea-user-detection design that
reframed "is this user in Korea" into four independent signals rather than one new detection mechanism:
timezone and language read from the device with a settings-level manual override on each (Elvis
confirmed both), PASS eligibility checked directly against the phone number's own carrier country code
rather than DEC-012's blended value, payment options driven by the org's own billing setup, and a
redacted-ID fallback path for Korea-based users without a Korean number.
Open: `proposed-decisions.md` still has nothing filed despite several launch-scoped resolutions this
session (embeddings/tagging pipeline, day-1 experimentation capability, PASS adoption plan) that read as
real decisions, not just workspace notes, this gap is now four-plus sessions deep even though the hotsheet
channel was used for the first time. Item 10 still has not actually been sent to Aakash. No `shared/`
edits made.

**Detail:** [session_log_2026-08-26.md](session_log_2026-08-26.md)

---

## 2026-08-25 (session 2) - Community segmentation, recommendation algorithm, and group dynamics scoped
Elvis raised two new strategic topics unprompted: how to handle very different early cohorts sharing a
city (a college student and a 40s professional joining Seoul around the same time), and the
recommendation algorithm behind home feed, explore, and Sunday Deck. Resolved community segmentation
(`community-segmentation-2026-08-25.md`) as cohort = (city, age/life-stage bucket), computed
independently per user, with university-affiliated users pulled into their own overriding cohort at
launch. The mechanism itself was revised mid-session from a soft ranking signal to a hard retrieval
filter at launch (same cohort is a must), softening once a city is manually confirmed dense enough, both
changes recorded not overwritten. Scoped the recommendation algorithm in detail
(`recommendation-algorithm-2026-08-25.md`): rule-based weighted scoring now, architected two-stage
(retrieval then ranking) so a learned model can slot in later, extended with text keyword matching,
evolving user interest profiles, and a hidden internal keyword layer across ideas/events/moments/users.
Explore was split into an unranked, viewport-bounded map view and a fully-ranked list view. Documented a
future per-user learned-weighting direction (Netflix/YouTube/Spotify-style), explicitly deferred, launch
keeps one global formula. A new concept, group dynamics, split out into its own file
(`group-dynamics-2026-08-25.md`): an avoid-signal (soft penalty, amplified by an explicit block),
look-alike host affinity (parked, needs scale), and personality-mix compatibility (ranking signal only),
surfacing two real gaps, a general blocking feature and attendee-level feedback, neither designed yet.
Open: several mechanism transitions flagged rather than assumed (does cohort truly revert to a ranking
signal once a city softens, does the map's cohort restriction loosen too); nothing from this session or
the prior two has been promoted to `proposed-decisions.md`, that gap is now three full sessions deep;
item 10 still hasn't actually been sent to Aakash. No `shared/` edits made.

**Detail:** [session_log_2026-08-25_session2.md](session_log_2026-08-25_session2.md)

---

## 2026-08-25 - Recurring events closed out, new Event Series concept, five-item feature batch scoped
Closed out the recurring-events follow-up (`recurring-events-2026-08-25.md`): separate linked Event
instances sharing a recurring group, Google Calendar-style edit/delete/join semantics, batch-generated
occurrences, both individual and org hosts. Elvis introduced a second, different series concept mid-
session (a thematic hub for heterogeneous events, closer to Idea than to recurring events), fully
scoped in `event-series-2026-08-25.md`: self-curation only, phase 1.5, pulls co-hosts forward from
later-phase, multi-series membership allowed. Caught and fixed a real naming collision between the two
concepts before it caused confusion downstream. Then worked through a twelve-item feature batch Elvis
raised in one message (`feature-backlog-2026-08-25.md`): triaged and sized all twelve, logged seven as
their own future dedicated conversations, fully scoped five (event schedule, live stories, Free Now,
icebreakers, tips/guides), each in its own file. Free Now got the most careful treatment, grounded in
documented failure patterns from comparable real-time-location products, safety-first defaults locked
throughout (rounded location, aggregate-first visibility, reciprocal join, restricted room creation).
Open: several flagged sub-details across the five scoped items still need answers before build; nothing
from this session or the last has been promoted to `proposed-decisions.md`, that gap is now two full
sessions deep; item 10 still hasn't actually been sent to Aakash. No `shared/` edits made.

**Detail:** [session_log_2026-08-25.md](session_log_2026-08-25.md)

---

## 2026-08-19 through 2026-08-24 - Conflict review closed out, freemium model built and priced
Walked all ten items in `conflict-review-2026-08-19.md` to resolution (the six headline
draft-vs-walkthrough conflicts, location at registration, gender/photos pre-join, the ten undiscussed
drafted surfaces) plus one escalation (Moments doc names/budget/legal, routed to Aakash). Built the
full freemium model in `freemium-model-2026-08-19.md`: individual tier at $3.99/mo or $36/yr, org tier
at $19.99/mo or $199/yr, both fully specified and priced, with a real infrastructure cost model
grounded in current Cloudflare R2/AWS pricing behind the org tier's media caps (50 items/attendee/
event), a 12-month retention policy, and a manual safety valve for extreme-usage outliers instead of
defensive pricing. Recommended R2 over S3+CloudFront and self-hosted transcode over Cloudflare Stream,
flagged for Deepak. Open: series pages need recurring events scoped first, not yet started. Neither
workspace file has been promoted to `proposed-decisions.md` yet, and item 10 has not actually been
sent to Aakash yet, only marked ready. No `shared/` edits made, all governance-correct.

**Detail:** [session_log_2026-08-24.md](session_log_2026-08-24.md)

---
