# Proposed decisions from aakash - for merger review

> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.
> These are recovered/uncaptured decisions from a 2026-09-02 governance audit of Elvis's design
> files. Several were filed as proposals earlier and lost in the 2026-08-28 merge queue-clear; others
> were never filed. Proposed by aakash on Elvis's behalf, each grounded in Elvis's source file.
> The merger assigns real DEC numbers at land time (next is DEC-048). Items marked [CONFIRM WITH ELVIS]
> amend an ACTIVE decision and go to the 2026-09-02 meeting agenda before they land.

## Pending

## DEC-NNN (PROPOSED) - Amend DEC-011: optional password reinstated (additive) and recovery becomes phone-first [CONFIRM WITH ELVIS]
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/auth-flow-2026-08-26.md; workspaces/elvis/onboarding-flow-2026-08-26.md. Originally filed as its own proposal, lost in the 2026-08-28 queue-clear, never re-filed.
**Topic:** Auth: password and account recovery
**Type:** Technical
**Decision:** DEC-011's "password deferred" provision is reversed. An optional password is additive to social and phone login, never a replacement, and lives in profile settings (not the account-creation sequence) with periodic reminder notifications while unset. DEC-011's recovery channel changes from email magic-link to phone OTP as the primary, always-available self-serve path, because email moved to optional and out of onboarding so phone is now the only universal credential; email magic-link stays a secondary option for users who set one, and customer service is the last resort when both phone and email are lost.
**Reasoning:** Adding a password put multiple credentials on one account, so "which credential logs me in" and "how do I recover" became real questions. Phone is mandatory and verified for every account regardless of signup provider, so it is the credential that is actually universal now that email is optional.
**Impact:** Amends DEC-011 (password + recovery). TASK-019's "password deferred" and HOTSHEET R3's "email magic-link recovery" notes become stale and need updating. Relates to the auth login/session model proposal below.
**Relates to / Supersedes:** Amends DEC-011.
**Status:** Awaiting merger (confirm with Elvis first)

## DEC-NNN (PROPOSED) - Amend DEC-015: private accounts pulled into phase 1 [CONFIRM WITH ELVIS]
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/private-accounts-2026-08-26.md
**Topic:** Private accounts in phase 1
**Type:** Strategic
**Decision:** Private accounts ship in phase 1, reversing DEC-015's deferral. A private account restricts the whole profile (moments, events attended, upcoming RSVPs) to approved followers, not just moments. Following a private account creates a pending follow-request that the owner accepts or declines; only accepted followers see restricted content. Accounts are public by default with private an opt-in toggle; switching to private grandfathers existing followers, and only new follow attempts after the switch require approval. A private account is distinct from a private event: the account setting gates the profile view, not an event's own visibility. Composes with DEC-015's most-restrictive-wins rule.
**Reasoning:** Private accounts were deferred only because the follow-request/approval machinery was new scope; Elvis has decided that machinery is worth building for phase 1.
**Impact:** Amends DEC-015. Needs a follow-request state (pending/accepted/declined), an approval queue, and bidirectional notifications. Four sub-items remain open and go to the meeting (agenda Q1): what a stranger sees on a private profile, whether private status suppresses the user on Explore/discovery (DEC-020), the approval-queue UX, and whether declining notifies the requester. The pre-join anti-stalking logic (DEC-006/DEC-017) needs a consistency check against this.
**Relates to / Supersedes:** Amends DEC-015; interacts with DEC-006, DEC-017, DEC-020.
**Status:** Awaiting merger (confirm with Elvis first; sub-items stay open)

## DEC-NNN (PROPOSED) - Auth login, session, and account-linking model
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/auth-flow-2026-08-26.md (RESOLVED 2026-08-26, confirmed by Elvis)
**Topic:** Returning login, persistent session, cross-provider linking
**Type:** Technical
**Decision:** The returning-login and session layer, never previously decided, is set. Any valid credential (Kakao/Apple/Google, phone OTP, or username-or-email plus password when set) resolves to the user's one account, with the verified phone number as the account anchor. Biometric quick-unlock (Face ID / Touch ID / Android equivalent) gates an already-active session locally via the OS API and is not a server credential. The session is always active (Instagram-style), ending only on explicit logout or app deletion, via a secure long-lived refresh token. Account linking across providers is consent-based, not silent: a new-provider signup on an already-registered phone completes phone verification, logs the user into their existing account, then explicitly asks before adding the new provider as a credential.
**Reasoning:** Adding a password made the login/session side a real gap; Elvis resolved it to the consumer-social-app standard rather than inventing bespoke behavior.
**Impact:** Deepak flags: first-launch-after-install check to wipe a leftover iOS Keychain session, and a server-side revocation capability held in reserve. Open and parked: username-change login continuity, multi-device concurrent sessions, and the customer-service recovery workflow.
**Relates to / Supersedes:** Extends DEC-011; relates to DEC-026.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED) - Invite model: two scoped exceptions to invite-first (org invites, founder-seed)
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/org-invites-2026-08-26.md; workspaces/elvis/onboarding-flow-2026-08-26.md (both RESOLVED 2026-08-26, confirmed by Elvis)
**Topic:** Invite types beyond event/idea-tied invites
**Type:** Strategic
**Decision:** Two new invite types are added as deliberate, scoped exceptions to the invite-first invariant (CLAUDE.md section 8: invites always tie to a specific event or idea). (1) Org invites: an org admin can invite someone to join the org itself with no event or idea required; admin-only in phase 1 (configurable policy deferred), the invite must display inviter name and org identity for credibility, and invited members land on a discussion board. (2) Founder-seed invites: at launch Elvis personally invites an initial batch of users with WePop itself as the inviter (no org, no event/idea), landing on the home feed. Individual person-to-person invites remain event/idea-tied and unchanged.
**Reasoning:** The invite-first rule's real job is giving the invitee a credible, non-spam reason to trust the invite; a real club president or WePop itself supplies that credibility through identity rather than through an event. Forcing a first event before inviting a club adds friction and misses the point.
**Impact:** Modifies a CLAUDE.md section 8 core invariant, so the invariant list needs the two exceptions recorded. Needs invite records carrying inviter and org/WePop identity, not just a token. Residual spam surface is narrowed by admin-only sending and university-club-first launch; revisit if promotional/business org accounts are added later.
**Relates to / Supersedes:** Scoped exception to CLAUDE.md section 8 invariant; relates to DEC-009, DEC-013, DEC-019, DEC-024.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED) - Categories and taxonomy v2.0 adopted
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/categories-taxonomy-2026-08-27.md (adapted into repo 2026-08-27, confirmed with Elvis)
**Topic:** Category/subcategory taxonomy for events, ideas, interests
**Type:** Technical
**Decision:** Adopt the v2.0 taxonomy: eight real top-level categories plus Other, 85 canonical subcategories, each node paired EN/KO under one canonical ID, colors respecified as 3-token sets (brand-palette AA conformance waived for small text). Selection limits are up to 5 subcategories from at most 3 categories for events, and up to 8 subcategories from at most 5 categories for profiles, enforced in the UI and validated server-side. Selecting a subcategory auto-selects its parent. "Other" is locked with zero user-submitted subcategories. "Casino & poker night" is removed for 도박죄 (gambling-offence) exposure. "travel_companion" is excluded from the initial set pending trust infrastructure, re-addable later via the Other-review promotion path.
**Reasoning:** Coverage over minimalism (every unfound node becomes a permanent hole in discovery data); the taxonomy gives concrete shape to DEC-020's previously-abstract internal keyword layer and to onboarding step 11.
**Impact:** Gives DEC-020's hidden keyword layer real content. Companion tasks: add gambling to the moderation blocklist (compliance) and a Korean-label review (owned by role, name withheld per Elvis). Backend needs a tag layer with canonical IDs and server-side limit validation.
**Relates to / Supersedes:** Gives shape to DEC-020; relates to DEC-005.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED) - Onboarding sequence adopted; profile completion moved out of onboarding
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/onboarding-flow-2026-08-26.md (RESOLVED 2026-08-26)
**Topic:** End-to-end onboarding and profile completion
**Type:** Technical
**Decision:** Adopt the assembled 15-step account-creation sequence as the build reference, with one Get Started entry screen for all branches (individual, org, founder-seed, promoted-waitlist) differing only in landing destination. Profile completion (optional email, optional password, profile description) moves out of the onboarding sequence into editable profile fields with periodic completion-nudge reminders. A distinct "languages I speak" profile field is added, separate in name and storage from the display-language field (DEC-027). Campus affiliation is optional, verified by school-email code with a suggest-a-school fallback. A device-permissions review screen presents location, notifications, camera, gallery, contacts, and calendar together as explanation only, firing no native OS dialogs (generalizing DEC-016's contextual-permission stance).
**Reasoning:** The full sequence had never been assembled; moving profile completion out keeps onboarding short and non-blocking.
**Impact:** The optional-password move is the same one in the DEC-011 amendment above. Cohort computation (DEC-019) must degrade gracefully to city plus age bucket when campus affiliation is skipped. Open/parked: nudge cadence and founder-seed invite copy.
**Relates to / Supersedes:** Assembles DEC-011, DEC-012, DEC-016, DEC-019, DEC-005, DEC-024, DEC-026, DEC-027; relates to the invite-model proposal.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED) - Shake-to-create gesture (phase 1)
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/shake-to-create-2026-08-26.md (RESOLVED 2026-08-26)
**Topic:** Shake-to-create entry point
**Type:** Technical
**Decision:** Shaking the phone while the app is foregrounded opens the standard creation flow in a bottom tray, a second entry point to the same flow as the primary create button (no separate quick-create variant). The gesture is suppressed during active input (focused text field, open form/modal, active call/video/camera), and the creation flow already being open is explicitly one of those suppression states. The gesture is open-only: it never closes anything, and the listener stays off while the creation flow is open, re-arming only on dismiss or completion. A settings toggle (default on) fully disables it.
**Reasoning:** A secondary physical entry point to creation; suppression and open-only behavior guard against the real false-positive risk (a phone in a bag or on rough transit).
**Impact:** Deepak flags: foreground-only motion listener torn down on background, on-device sensitivity tuning, distinct interaction-logging tag. Open/parked: exact suppression-state list, sensitivity threshold, whether it is taught via tips/guides.
**Relates to / Supersedes:** New phase-1 feature; relates to DEC-020 (interaction logging).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED) - Event-location map picker extends DEC-003; location poll scoped
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/event-location-map-picker-2026-08-27.md (RESOLVED 2026-08-27, confirmed by Elvis)
**Topic:** Location picker and location poll
**Type:** Technical
**Decision:** One map-plus-search component serves three surfaces: event/idea location capture, a newly-scoped location poll (creator adds options, attendees vote, host confirms the final location after voting), and Explore's browse map. Zoom determines precision with no minimum floor: a tap zoomed in resolves to a POI/address, zoomed out to a neighborhood, extending DEC-003 (which implied always-specific capture). An event's top-level location need not be its exact meeting point; the host supplies the findable spot separately, so no precision floor is forced. Each capture stores a canonical ID, centroid/boundary, and display name at the resolved tier, plus DEC-003's optional per-location comment, applied uniformly across all three surfaces and event-schedule stops.
**Reasoning:** Reuses one component rather than three; Elvis's correction that an event's headline location is not its meeting point removes the need for a precision floor that QR check-in seemed to require.
**Impact:** Extends DEC-003; reuses across DEC-025 schedule stops. Zoom-to-precision thresholds are tunable, not locked, and depend on the map-provider decision (raised separately on the HOTSHEET). Location-poll sub-mechanics (min/max options, vote changeability, anonymity, close condition, placement in the create flow) are open and go to the meeting.
**Relates to / Supersedes:** Extends DEC-003; relates to DEC-025, TASK-016.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED) - Redacted-ID verification fallback (Korea); feedback channel; flexible name field
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/internationalization-korea-2026-08-26.md (RESOLVED 2026-08-26)
**Topic:** Korea verification fallback, feedback channel, name field
**Type:** Technical
**Decision:** Three resolved items captured. (1) A Korea-based user without a Korean phone number gets a redacted-ID fallback (government photo ID, user self-redacts the ID number, name/DOB/photo/expiry visible, reviewed by a trained human, no facial recognition or biometrics), following Bumble's Korea flow, covering DEC-012's international-in-Korea and visiting cases without a Korean phone as a hard gate. (2) A single "Give Feedback" profile menu item (issues, general feedback, comments to WePop) lands in a distinct Admin Portal table, separate from the content-moderation queue and reusing existing Admin Portal access control. (3) The name field is a single flexible full-name field, not a Western first/last split, per Korean naming convention.
**Reasoning:** Each closes a real gap DEC-026 (which covered only PASS-for-Korean-numbers plus standard OTP) left open, without expanding scope.
**Impact:** Adds a human-review verification path (PIPA implications, its own review queue and tooling, open) and a feedback table. Extends DEC-026/DEC-012.
**Relates to / Supersedes:** Extends DEC-026, DEC-012.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED) - Apply-to-join placed in phase 1.5
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/session_log_2026-08-26_session2.md; DEC-033 (which notes the placement is still unmerged)
**Topic:** Apply-to-join phase placement
**Type:** Strategic
**Decision:** Apply-to-join (host screening questions on join) is placed in phase 1.5. This is the placement proposal that DEC-033 (the screening-question quota) explicitly depends on and that was lost in the 2026-08-28 queue-clear.
**Reasoning:** DEC-033 set the quota but references a phase placement that never landed, leaving a live decision resting on an unrecorded dependency.
**Impact:** Closes the DEC-033 dangling dependency. Scope-matrix apply-to-join row gets a confirmed phase.
**Relates to / Supersedes:** Completes a dependency of DEC-033; relates to DEC-024.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED) - Personality-tags catalog restructures DEC-005
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/personality-tags-catalog-2026-08-27.md
**Topic:** Personality-tags picker content
**Type:** Technical
**Decision:** DEC-005's flat "top 10-20 tags" picker is restructured into three named sections: MBTI (closed set, 16 values), social energy (closed set, 3 values), and general vibe/self-descriptors (open, searchable, user-addable, the section DEC-005's original design maps to). The self-reported nature and searchable/user-extensible behavior from DEC-005 are unchanged; only the flat list becomes sectioned, which supersedes the "10-20 tags" figure (MBTI alone is 16). Zodiac and Enneagram are considered and not included in the initial catalog.
**Reasoning:** Onboarding needs real seed content, and named sections make the picker scannable rather than one long list.
**Impact:** Refines DEC-005. Open and going to the meeting: whether MBTI and social energy are single-select while general vibe is multi-select, or all three allow multiple (onboarding step 10 says multiple at the step level, written before sections existed).
**Relates to / Supersedes:** Refines DEC-005.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED) - Explore filters are free, not a paid tier
**Date:** 2026-09-02
**Proposed by:** aakash
**Source:** workspaces/elvis/paid-tier-features-2026-08-27.md (RESOLVED 2026-08-27, confirmed by Elvis)
**Topic:** Explore filters tiering
**Type:** Commercial
**Decision:** Standard Explore filters are free functionality, not a paid tier, applying DEC-018's "never gate marketplace/discovery actions" bucket. This confirms filters stay out of the individual premium tier.
**Reasoning:** Gating discovery filters would contradict DEC-018's rule that marketplace and discovery actions are never gated.
**Impact:** Confirms and applies DEC-018; a scope note so filters are not later mistaken for a paid lever.
**Relates to / Supersedes:** Applies DEC-018.
**Status:** Awaiting merger

## Landed

- 2026-08-26 (sync): DEC-026 (Korea PASS auth), DEC-027 (localization), DEC-028 (A/B testing) landed
  into `shared/DECISIONS.md`; DEC-019 and DEC-020 gained a change-history note for the follow-graph
  cohort-filter exemption. Source: 2026-08-26 team sync. Nothing pending.
- 2026-08-26 (intake): DEC-010 to DEC-025 landed from the Elvis workspace intake.
- 2026-08-17: DEC-001 to DEC-009 landed from the 2026-08-17 walkthrough.
