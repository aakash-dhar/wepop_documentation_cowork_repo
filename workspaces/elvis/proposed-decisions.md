# Proposed decisions from elvis, 2026-08-26 - for merger review

## DEC-NNN (PROPOSED)
**Date:** 2026-08-26
**Proposed by:** Elvis
**Source:** `workspaces/elvis/internationalization-korea-2026-08-26.md`, refining DEC-027 (landed
2026-08-26 from the live team sync)
**Topic:** Language preference storage, detection cascade, and scope
**Type:** Technical
**Decision:** The language setting is a profile field, not a device-only setting, so it syncs across a
user's devices. Its initial value comes from a fallback cascade run once, at account setup: device
language setting first, then app/Play Store region if that signal is unavailable or ambiguous, then
phone number as a last resort, mirroring the shape of DEC-012's own age/country cascade. This is a
one-time read, not an ongoing check, the app does not monitor the device's language setting afterward. A
manual override in profile settings always takes precedence over the cascade, both at first set and any
time after. Notifications (push, SMS, email) follow this same profile field rather than the device/OS
locale independently. Scope is split explicitly in two: every WePop-authored string (chrome, system
messages, transactional text) ships fully bilingual, selected by this field; user-generated content
(event titles/descriptions, moment captions, chat) renders exactly as authored with no translation
pipeline at launch, on-demand translation deferred to a later phase per the existing UGC deferral already
in DEC-027's source doc.
**Reasoning:** DEC-027 only specified device-detection-plus-manual-switch; it did not specify storage
model, initial-detection fallback order, whether it re-checks the device over time, or whether
notifications follow the same setting. A profile field avoids a real "I lost my language setting"
complaint on a new device or reinstall, and reusing the DEC-012 cascade shape (including the same
set-once, not re-checked, behavior) keeps the codebase consistent rather than inventing a second pattern.
Splitting WePop-copy from UGC scope prevents the i18n coverage requirement from silently expanding to
content translation, which was deliberately deferred.
**Impact:** Adds a profile-level language field and a first-launch cascade to the auth/onboarding flow
alongside DEC-012's existing cascade logic, no background job or listener needed since the read is
one-time. Notification pipeline (push/SMS/email) needs to read this field rather than infer language
independently. Does not change DEC-027's core detect-plus-switch design, refines its implementation. Both
English and Korean versions of every WePop-authored string ship together on day one, translation is not a
phased rollout, closing the earlier open question about a fallback for an untranslated string since no
gap is expected. A separate issue-reporting feature (users can report issues they encounter) was raised
as the backstop for anything that slips through despite that commitment, its own scope is not yet
confirmed and is not part of this proposal, tracked as a new open item in the source doc.
**Relates to / Supersedes:** Refines DEC-027. Reuses the cascade pattern from DEC-012. Does not supersede
either.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-26
**Proposed by:** Elvis
**Source:** `workspaces/elvis/private-accounts-2026-08-26.md`
**Topic:** Private accounts pulled into phase 1
**Type:** Strategic
**Decision:** Private accounts, previously deferred (DEC-015, `conflict-review-2026-08-19.md` item 4),
move into phase 1. A private account gates the whole profile (moments, event-attended history, upcoming
RSVPs), not just moments as originally scoped, restricted to approved followers. Following a private
account creates a pending follow-request that the account owner must accept or decline, replacing the
immediate follow that public accounts still use. A private account is distinct from a private event, the
account setting gates the profile view only, an event's own visibility is set independently per DEC-015.
**Reasoning:** Elvis's own call, made once the real scope this needs (follow-request-and-approval
machinery) was priced out clearly, this was the specific reason it was deferred originally, not a change
in appetite for the feature itself. Whole-profile gating rather than moments-only matches the private-
account behavior users already expect from comparable apps, a moments-only carve-out would look
incomplete and confusing (a stranger blocked from moments but still able to see full RSVP history would
not read as private).
**Impact:** Adds new machinery: a follow-request state distinct from an active follow, an approval
queue/inbox for the account owner, notifications in both directions. Composes with DEC-015's most-
restrictive-wins moment-visibility principle without conflict. Flags a consistency review against the
DEC-006/DEC-017 anti-stalking pre-join visibility rules (designed independently of account privacy, not
yet confirmed to compose correctly). Still open, not resolved by this proposal: what a non-follower
actually sees on a private profile (stub page design), whether private-account status changes anything
about discovery/recommendation surfaces (DEC-020) beyond the profile page itself, exact approval-queue
UX, and default-state/grandfathering assumptions (public by default, existing followers kept on switch to
private) that are inferred, not explicitly confirmed. All flagged in the source doc for a future pass.
**Relates to / Supersedes:** Supersedes the phase-1 deferral of private accounts recorded in DEC-015 and
`conflict-review-2026-08-19.md` item 4. Does not change DEC-015's moment-visibility model itself, extends
it to account level.
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-26
**Proposed by:** Elvis
**Source:** `workspaces/elvis/conflict-review-2026-08-19.md` item 9 (revised)
**Topic:** Apply-to-join given a firm phase 1.5 placement
**Type:** Strategic
**Decision:** Apply-to-join with host-defined questions moves from an open-ended "later" placement (DEC-024)
to a firm phase 1.5 slot, available to both individual hosts and org accounts, not org-only.
**Reasoning:** Elvis's own driving use case: organizations and clubs may want to filter who can join a
specific event or idea rather than accept anyone who RSVPs, a real, named need for the org-account
audience, not a speculative feature. Phase 1 stays on plain RSVP, this reasoning does not change, simple
RSVP is still sufficient at launch and apply-to-join remains real added scope (a question builder, an
approval queue, applicant notifications) that phase 1 does not need to carry. It earns a dated phase 1.5
slot rather than staying in the undifferentiated "later" bucket alongside items like Sunday Deck and
Wrapped that are waiting on density or history, since org demand does not depend on either of those.
**Impact:** Moves this item's row on the scope matrix from "later, deferred" to "later (1.5), decided."
Confirms availability spans both individual hosts and org accounts. Full design (question builder shape
and fields, approval-queue UX) is not scoped by this proposal, needs its own dedicated pass when phase 1.5
work begins.
**Relates to / Supersedes:** Refines DEC-024's phase placement for this one item. Does not change DEC-024's
other phase-1/later calls (waitlist auto-promote, org ownership transfer, org track-record module stay
phase 1; Sunday Deck, Wrapped, memories resurfacing stay later, unaffected).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-26
**Proposed by:** Elvis
**Source:** `workspaces/elvis/group-dynamics-2026-08-25.md`
**Topic:** General user blocking confirmed as phase-1 scope
**Type:** Strategic
**Decision:** General user blocking, previously an unresolved dependency of DEC-023's avoid signal with no
phase placement of its own, is confirmed as phase-1 scope.
**Reasoning:** Basic user blocking is a baseline safety expectation for a location-based social product
that engineers real-world meetups between strangers, not a feature that should wait on the recommendation
algorithm's own readiness to consume it. Elvis's own call, independent of whether the avoid-signal itself
has enough data to use it at launch.
**Impact:** Resolves the "unbacked, needs a decision" item on the scope matrix (general user-blocking
feature, phase-1 safety baseline versus later). The blocking feature's own design, what exactly gets
blocked or hidden, symmetric or asymmetric, interaction with the new private-accounts follow/approval flow
(a separate proposal in this same file), is not scoped here, needs its own dedicated design pass. DEC-023's
avoid signal keeps its existing dependency note, now resolved to phase 1 rather than an open question.
**Relates to / Supersedes:** Resolves an open item flagged in DEC-023, does not change DEC-023's own
decision text. Relates to the private-accounts proposal above (follow/approval is a related but distinct
mechanism from blocking).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-26
**Proposed by:** Elvis
**Source:** `workspaces/elvis/org-invites-2026-08-26.md`
**Topic:** Org invites, admin-only in phase 1, a scoped exception to invite-first
**Type:** Strategic
**Decision:** Org accounts can invite users directly, not only through individual members. Phase 1: only
an org's admin(s) can send org invites, no member-suggestion or review-queue machinery at launch. Org
invites are a second, distinct invite type from the existing person-to-person invite, not tied to a
specific event or idea, unlike every individual invite, which keeps working exactly as it does today. An
org invite must display who is inviting and what org it is for, so the invitee gets the same concrete,
credible context an event-tied invite provides for free. Org-invited members land with access to a
discussion board on join, the same pattern events and ideas already have (DEC-009, DEC-013), full
organizational-account design deferred to a dedicated later pass.
**Reasoning:** A real, named early-growth path: convincing an existing club's president to bring their
whole membership onto WePop at once, rather than relying only on one-at-a-time member invites. The
invite-first invariant's actual purpose is giving the invitee a credible, non-spam reason to trust the
invite, an event does that by being specific; a real club president inviting an actual member of their
real club satisfies the same purpose through the existing relationship and community, not through an
event. Forcing an admin to invent a first event or idea unilaterally just to unlock invites creates
friction and skips the point, a newly onboarded club should plan its first activity together, not have it
decided for them. Admin-only sending in phase 1 and org accounts launching with university clubs first
(not yet-designed promotional accounts) both narrow the reopened spam surface this exception creates,
worth revisiting once promotional/business org accounts are designed later.
**Impact:** Adds a second invite type alongside the existing event/idea-tied invite. Needs an invite
record that carries inviter and org identity for display. Org-invited members get discussion-board access
on join, reusing the existing event/group chat mechanism's pattern rather than a new chat system. Confirms
university-affiliated cohort assignment (DEC-019) already covers these members automatically via the
existing Org-profile-affiliation signal, no new cohort logic needed. Later phase, direction only: an
org-level configurable invite policy (admin-only, suggest-and-review, or open to all members), not
designed here.
**Relates to / Supersedes:** A scoped exception to the invite-first invariant recorded in CLAUDE.md
section 8, individual invites are unaffected, this applies to org-issued invites specifically. Relates to
DEC-019 (cohorts), DEC-009/DEC-013 (event/group chat, the discussion-board pattern reused here).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-08-26
**Proposed by:** Elvis
**Source:** `workspaces/elvis/onboarding-flow-2026-08-26.md`, "Profile completion, moved out of onboarding"
section
**Topic:** Optional password field, additive auth method, reverses DEC-011's deferral
**Type:** Technical
**Decision:** An optional password field is added as an additive login method alongside the existing
social-login-plus-phone auth model, not a replacement for either. A user can set a password whenever they
choose, or leave it unset and continue relying on social/phone sign-in only. It lives in profile settings,
not the account-creation sequence, so it never lengthens or blocks onboarding. Along with optional email
and the profile description field, it's nudged via periodic reminder notifications while left empty,
cadence not yet specified.
**Reasoning:** DEC-011 explicitly deferred password auth in favor of social-plus-phone only. While working
through the full detailed onboarding sequence step by step, Elvis specified a password field belongs in
the product now, an explicit reversal of that provision rather than an incidental addition, surfaced
directly by Elvis when asked whether to keep DEC-011's deferral or add it now. Elvis then moved it (along
with optional email and description) out of the onboarding sequence itself and into profile settings, to
keep onboarding short, backed by reminder nudges instead of an upfront ask.
**Impact:** Backend needs to support password as a real, additive auth method, storage and hashing, plus a
login-method-selection or fallback flow at sign-in for users who set one. Does not remove or weaken
social/phone auth, both remain fully supported and phone stays a hard requirement regardless of provider,
per DEC-011's other provisions, which are otherwise unchanged. Also needs a scheduled reminder-notification
job for the three profile-completion fields (email, password, description), routed through the same
pipeline that already follows the profile language field, cadence and dismissal behavior not yet decided.
Username auto-generate-and-suggest is new alongside it, part of the same onboarding-sequence work, not
separately proposed here since it doesn't reverse any existing landed decision.
**Relates to / Supersedes:** Reverses DEC-011's password-deferred provision specifically. DEC-011's phone-
required and social-login provisions are unaffected and stay as landed.
**Status:** Awaiting merger
