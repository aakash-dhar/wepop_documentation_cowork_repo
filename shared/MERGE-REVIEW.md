# MERGE-REVIEW.md - Wepop merge-review queue

> Merger-only file. When the merger finds conflicting proposals from different people on the same
> topic, both versions land here for Aakash (the PM) to resolve. Also used to surface best-judgment
> merges that need sign-off. Dated run sections; resolved items move to a dated Resolved note.
> Price / contract / scope conflicts escalate to the financials owner. No em-dashes.

---

## Open

### 2026-09-02 run - held for client sign-off

- **Amend DEC-011 (optional password reinstated; recovery becomes phone-first).** This proposal amends an ACTIVE decision (DEC-011 currently defers the password and names email magic-link as recovery). It was NOT discussed on the 2026-09-02 call, so it is held rather than landed, per the earlier plan to confirm the active-decision reversals with Elvis first. Recommended ruling: land once Elvis confirms the password reversal and the phone-first recovery change (it is on the meeting agenda). No conflict between proposers; this is a single proposal contradicting a locked decision, parked for sign-off.

  Proposal text as filed:

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

---

## Resolved

- **2026-09-02: DEC-029 stale open-note reconciled by the merger.** A 2026-09-02 validation pass found the "Open, not resolved here" note in DEC-029 stale on both counts. The missing-string fallback question (English fallback vs blocking launch) is closed by Elvis's committed full bilingual coverage at launch, and the re-read-vs-captured-once question is answered as a one-time read at account setup, both stated in `workspaces/elvis/internationalization-korea-2026-08-26.md`. The note was replaced with a Change history line pointing to that file. Best-judgment merger edit; no new decision, no conflict.
