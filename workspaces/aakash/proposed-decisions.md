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

## Landed

- **2026-09-02: sixteen aakash proposals landed as DEC-048 to DEC-063** into `shared/DECISIONS.md` (private accounts phase 1, auth session/linking, founder-seed invite, categories taxonomy v2.0, onboarding sequence, shake-to-create, map picker, redacted-ID fallback, apply-to-join placement, personality-tags, Explore filters free, cohort soft signal, ideas lifecycle, Free Now, live stories, launch free-trial). The map-provider HOTSHEET entry also landed (Needs Attention). The DEC-011 password/recovery amendment is HELD in `shared/MERGE-REVIEW.md` pending Elvis sign-off and stays in Pending below.

- 2026-08-26 (sync): DEC-026 (Korea PASS auth), DEC-027 (localization), DEC-028 (A/B testing) landed
  into `shared/DECISIONS.md`; DEC-019 and DEC-020 gained a change-history note for the follow-graph
  cohort-filter exemption. Source: 2026-08-26 team sync. Nothing pending.
- 2026-08-26 (intake): DEC-010 to DEC-025 landed from the Elvis workspace intake.
- 2026-08-17: DEC-001 to DEC-009 landed from the 2026-08-17 walkthrough.
