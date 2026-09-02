# Elvis meeting - open design calls to close (2026-09-02)

Prepared by Aakash for the 2026-09-02 sync with Elvis. Purpose: close the design
decisions left open with a "decide later" note. Each item is validated as genuinely
unresolved and as Elvis's call (validation pass 2026-09-02; sources cited per item).
No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Priority order

### 1. Private accounts (the one document-level conflict)
DEC-015 says private accounts are deferred, not phase 1. Elvis's
`private-accounts-2026-08-26.md` designs the feature and puts it in phase 1. Both
are in the repo pointing opposite ways; neither can land until Elvis confirms the
direction. If it is in (as his doc says), his own file parks four sub-questions that
must close before it can be filed: what a stranger sees on a private profile, whether
private status also hides the user from Explore and discovery, the approval-queue UX,
and whether declining a follow request notifies the requester.
Source: DEC-015; `workspaces/elvis/private-accounts-2026-08-26.md`.

### 2. Discovery / cohort filter transition
The recommendation engine uses a hard cohort filter (only same-cohort events shown),
deliberate while the app is thin. Open: once density is high enough, does the hard
filter soften to a ranking signal (prefers cohort, stops hiding the rest), and if so
does the Explore map loosen with it or stay locked? The density trigger itself is
Aakash's to own (now a single global call, not per-city, after DEC-030); only the
mechanism is Elvis's call. Source: HOTSHEET Needs Attention; DEC-019 impact; DEC-030.

### 3. Moments video and media caps
- Total video-duration cap per Moment: clips are capped at 15s each but total video
  per Moment is uncapped. Handoff suggests ~150s free / 300s paid. Add it or not?
- Org-paid Moment video length: DEC-018 never set a number. Recommendation ~30s.
- Media retention past the 6-month boundary: confirm free users see a mid-res ~1080px
  version full-screen (Elvis argued for this) rather than only the ~400px thumbnail.
Source: DEC-038 open note; DEC-018; DEC-039; `handoff-spec-v0.9-intake-2026-08-29.md`.

### 4. Ideas lifecycle edge cases
Can an archived idea be un-archived? Can an ownerless (detached) idea regain an owner?
Do archived ideas appear in Explore or only by direct link? Are interested users
notified when an idea is paused or archived? Source: DEC-040 open note; DEC-042 open note.

### 5. Check-in and feedback
- Self-report intent flow (on-my-way / running-late / cannot-make-it) is designed in
  Elvis's files but is documented nowhere in the repo. Elvis to push the design so it
  can be filed. Residual open detail: host notified individually vs roster view, and
  whether "running late" carries an ETA.
- What "check-in surfaces in analytics" means concretely (which surface, per-event or
  rollup).
- Whether the "claimed but unconfirmed" attendance state (7-day window) is visible to
  the attendee or the host is nudged to clear it before auto-close.
- Whether an edited rating shows as "edited" to viewers or changes silently within the
  7-day window. Source: DEC-046 open note; DEC-047 open note; `ratings-checkin-2026-08-31.md`.

### 6. Explore / location UX
Does Explore need its own manual location refresh separate from the home feed's, or do
they share one? And can a GPS-granted user opt back into the coarser saved home
location, or is live GPS forced once granted? Source: DEC-031 open note.

### 7. Free Now safety rails (needed before build)
Account-standing threshold to create a room, room duration cap, room auto-archival, and
whether organizations can create rooms. Related: do live stories count against the org
50-item media cap or get their own allowance? Source: HOTSHEET Watching; `free-now-2026-08-25.md`.

## Ratify recovered decisions (2026-09-02 governance audit)
A governance audit found decisions Elvis made in his design files that were never landed (several were
filed and lost in the 2026-08-28 merge). They are now drafted as proposals; three amend ACTIVE decisions
and need Elvis to confirm before they land:
- **Password (amends DEC-011):** optional password reinstated as additive, lives in profile settings.
  Confirm the reversal stands.
- **Account recovery (amends DEC-011):** recovery becomes phone-OTP-first (email magic-link secondary),
  because email moved out of onboarding. Confirm.
- **Private accounts (amends DEC-015):** confirm the phase-1 pull itself (the 4 design sub-items are Q1
  above).
The rest are pure captures and only need a nod that the record matches intent: auth session/linking model,
invite-model exceptions (org invites + founder-seed), categories taxonomy v2.0, onboarding sequence + profile
completion moved out, shake-to-create, map-picker/location-poll, Korea redacted-ID fallback + feedback
channel + name field, apply-to-join placed in phase 1.5, personality-tags restructure, Explore filters stay
free.

## New open items surfaced by the audit (need Elvis)
- **Korea map provider** (Google vs Naver/Kakao): the zoom-precision picker now depends on provider POI
  data, and it is unclear a non-Korean business can open a Naver/Kakao dev account. Now Needs Attention.
- **Personality tags select mode:** are MBTI and social energy single-select while general vibe is
  multi-select, or all three multi-select?
- **Location-poll sub-mechanics:** min/max options, vote changeability, anonymity, close condition, and
  where poll creation sits in the create flow.

## Deliverables still owed by Elvis
- Plan Mode spec: it exists but only inside the code tree (`code/we-pop-mobile-app/phase_two_docs/wepop_plan_mode_v2.1_0504202.docx` plus a Markdown v1.0 under `.../uploads/WePop_Plan_Mode_Specification.md`), not in the governed docs layer, and is superseded by the handoff spec v0.9. Decision for Aakash (design-intake): pull the still-relevant parts into architecture/elvis, or treat it as fully superseded and leave the docx as an archived source. Elvis confirms what still stands. Not a missing deliverable.
- Consolidated / reviewed design doc.
- CSAM preserve-and-report runbook draft and the one-page moderation guideline (Elvis is
  the reviewer on both; TASK-039, R4).

## Not Elvis's calls (do not spend meeting time here)
- Legal register L-1..L-12 and the 위치정보법 registration question go to DLG (TASK-040).
- Payments / ticketing scope and the freemium governance channel are Aakash's (financials).
- Event-schedule date storage, retention storage mechanics, and Free Now location rounding
  are Deepak's.

## Removed after validation
- Localization fallback (English fallback vs block launch): already resolved by Elvis on
  2026-08-26 (full bilingual coverage committed at launch, no fallback path needed). The
  stale open-note in DEC-029 is reconciled separately by the merger.
