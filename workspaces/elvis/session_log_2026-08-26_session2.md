# Session detail, 2026-08-26 (session 2)

> Full detail behind the summary entry in `SESSION-LOG.md`. No em-dashes. Governance values
> ALLOW / BLOCK / ESCALATE.

## Live team-sync sync

Synced the follow-graph exemption to the cohort hard filter (landed via the actual live Aakash/Elvis/Deepak
team sync, outside this session) into `community-segmentation-2026-08-25.md` and
`recommendation-algorithm-2026-08-25.md`. Followed users' content is now exempt from the cohort retrieval
filter, pulled in via the existing social-proximity signal (w6), retrieval query becomes (cohort) union
(followed users). Flagged for Deepak in both files that the retrieval query itself needs this union, not
just the ranking stage.

## Language switch, fully resolved

Closed out every open item in `internationalization-korea-2026-08-26.md` left over from the prior session:

- Language cascade (device setting, then app/Play Store region, then phone number) confirmed as a one-time
  read at account setup, not an ongoing check, Elvis explicit: "we do not need to keep checking."
- Day-one translation coverage confirmed full and bilingual for every WePop-authored string, no phased
  rollout, closing the earlier fallback question since no gap is expected. UGC stays exactly as authored,
  no translation pipeline at launch.
- Notifications (push, SMS, email) confirmed to follow the same profile language field, not the device/OS
  locale independently.
- New: a "Give Feedback" entry point in the profile menu (issues, feedback, comments in one place),
  triaged into a dedicated Admin Portal table, staff-viewable, a separate table from the content-moderation
  queue, reusing the existing Admin Portal access model with no new permission layer.

## Shake-to-create, new feature, fully scoped

New file `shake-to-create-2026-08-26.md`. A phone-shake gesture opens the creation flow via a bottom tray.
Resolved: suppressed during active input (typing, scrolling, media capture); opens the same creation
screen as the primary entry point, not a separate flow; a settings toggle exists (default on) to disable
the gesture entirely. Explicitly not a toggle on the gesture's own open-only behavior, a shake while the
creation flow is already open does nothing, distinct from the settings toggle. Flagged: exact motion
sensitivity threshold, full suppression-state enumeration, and whether the tips/guides system should cover
discoverability, none decided here.

## Phase 1/1.5 list reviewed, three items resolved

Walked the scope matrix (`architecture/phase-plan/wepop-scope-matrix.md`) and resolved three open
placements:

- **Private accounts** pulled into phase 1 (new file `private-accounts-2026-08-26.md`), superseding
  DEC-015's deferral. Gates the whole profile, not moments only. Follow-request-and-approval replaces the
  immediate follow public accounts still use. Distinct from a private event, which stays governed by
  DEC-015 independently.
- **General user blocking** confirmed phase 1, resolving an open dependency DEC-023's avoid signal had
  carried with no phase placement of its own (`group-dynamics-2026-08-25.md`).
- **Apply-to-join** given a firm phase 1.5 slot (revised in `conflict-review-2026-08-19.md` item 9), moved
  off the open-ended "later" bucket. Elvis's driving use case: orgs and clubs filtering who can join a
  specific event or idea. Confirmed available to both individual hosts and org accounts, not org-only.

## Org invites, new invite mechanism, fully scoped

New file `org-invites-2026-08-26.md`. Org accounts can invite users directly, not only through individual
members. Phase 1: admin-only sending, no member-suggestion or review-queue machinery yet, later phase
direction only (admin-only / suggest-and-review / open to all members). A deliberate, scoped exception to
the invite-first invariant (CLAUDE.md section 8): org invites are not tied to an event or idea, credibility
comes from organizational identity instead ("Minjun, president of Seoul Hiking Club, invited you..."). This
is a residual-risk-flagged exception, narrowed by admin-only sending and university-clubs-first org
accounts, worth revisiting once promotional/business org accounts are designed. Org-invited members land
on a discussion board on join, reusing the existing event/group chat pattern (DEC-009, DEC-013).

## Onboarding flow, assembled end to end for the first time

New file `onboarding-flow-2026-08-26.md`, synthesizing DEC-011, DEC-012, DEC-016, DEC-019, DEC-005,
DEC-024, DEC-026, DEC-027, and today's org-invites work into one ordered sequence for the first time.
Went through several rounds of refinement over the session:

- **Entry point**, resolved down to a single shared "Get Started" screen for every path (individual
  invite, org invite, a new third founder-seed invite, and organic/waitlist), not separate screens per
  branch. The three invite paths layer a toast on top of that same screen carrying inviter and destination
  context; the organic path shows no toast. A persistent language selector sits top left on this one
  screen, resolved after the earlier idea of a one-time confirmation toast was explicitly dropped in favor
  of an always-available override, no interruption screen.
- **Founder-seed invite**, new, confirmed by Elvis: at launch Elvis personally invites an initial batch of
  users to seed the platform, reusing the org-invite pattern's non-event-tied mechanism but with no org
  account attached, WePop itself is the credibility source. A third, distinct invite type alongside
  individual (event/idea-tied) and org (org-identity-tied) invites.
- **Account-creation sequence**, expanded from an initial 7-step synthesis to a full 15-step sequence
  matching Elvis's own detailed walkthrough: language (silent cascade), auth, age gate, name, username
  (auto-generate plus taken-name suggestions), location, profile photo (defaults to initials plus color),
  gender, language-and-proficiency (new, distinct from the display-language setting), personality tags,
  categories and subcategories (confirmed as a second, distinct taxonomy from personality tags), campus
  affiliation (email-code verification or self-declared fallback, confirmed optional), invisible cohort
  computation, device permissions review (confirmed as a lighter in-app screen only, no native OS prompts
  triggered), done.
- **Profile completion**, new: optional email, optional password, and the profile description field all
  moved out of onboarding entirely and into profile settings, nudged by periodic reminder notifications
  while empty, cadence not yet specified. Keeps onboarding itself short.
- **Optional password**, the one item here that reverses a landed decision (DEC-011's "password deferred"),
  filed as its own proposal to the merger, updated once its placement moved from an onboarding step to a
  profile-settings field.

Still open: exact founder-seed-invite copy, reminder cadence for profile-completion nudges, and whether a
one-time language-confirmation moment was needed (resolved: no, a persistent selector instead).

## Auth and login, item #2 of the phase review, fully detailed

New file `auth-flow-2026-08-26.md`. Sign-up methods were already decided (DEC-011 social-plus-phone,
DEC-026 Korea PASS, DEC-012's redacted-ID fallback leg), the real gap was login/session behavior once
password made multiple credentials possible on one account. Resolved:

- **Returning-user login**: any valid credential, social, phone OTP, or username-or-email-plus-password
  when set, logs the user into their one account, phone number is the durable anchor identifier.
- **Biometric quick-unlock**: Face ID / Touch ID / Android biometric gates access to an already-active
  session locally via the native OS API, not a new server-side credential, confirmed as the lighter,
  Instagram-style interpretation rather than a full passkey/WebAuthn credential.
- **Persistent session**: always active, including while the app is closed, ending only on explicit logout
  or app deletion, the same pattern Instagram uses. Validated against industry standard as a genuine match
  for how major consumer social apps behave, with two flagged additions rather than deviations: an
  explicit first-launch-after-install check to clear stale iOS Keychain session data (Keychain, unlike
  Android Keystore, can survive an uninstall), and a recommended server-side revocation capability (log out
  of all devices, forced logout on password change or suspicious activity) as an invisible safety net.
- **Account linking**, revised mid-session: Elvis's first answer was silent auto-link when a new provider
  signup matches an already-registered phone number. On being asked to align to industry standard instead,
  this was replaced with the actual pattern used by Auth0/Okta-style identity systems and apps like Slack,
  Discord, and Notion: since the new-provider signup still has to complete phone verification regardless,
  that verification doubles as login to the existing account (not a dead-end redirect, and not a silent
  merge), followed by an explicit opt-in prompt before the new provider is persisted as an added credential.
- **Account recovery**: phone OTP is always a valid, self-serve login method since phone is mandatory and
  verified for every account regardless of signup provider, so losing a social login alone is never a
  lockout. A lost or changed phone number falls to a WePop customer-service contact path, workflow not
  designed here.

Still open on auth: whether a changed username still works to log in under its old value, multi-device
concurrent session behavior and any device-management surface, and the customer-service recovery workflow
itself (queue, identity re-verification, possible reuse of the Give Feedback Admin Portal pattern).

## Proposals filed to the merger this session

Six entries added to `proposed-decisions.md`, all status "Awaiting merger": language preference storage,
cascade, and scope (refining DEC-027); private accounts into phase 1 (superseding DEC-015's deferral);
apply-to-join's firm phase 1.5 placement (refining DEC-024); general user blocking confirmed phase 1
(resolving an open DEC-023 dependency); org invites as a scoped invite-first exception (relates to CLAUDE.md
section 8, DEC-019, DEC-009/DEC-013); and the DEC-011 password-field reversal, updated in place once its
design moved from an onboarding step to a profile-settings field with reminder nudges.

## Open at session close

- Items #3 onward of the phase 1/1.5 review list not yet gone through in this detailed, flow-by-flow
  style, item #1 (invite-first onboarding, expanded well beyond its original scope via org invites and the
  full onboarding-flow file) and item #2 (auth) are the only two done this way so far.
- None of the six proposals filed this session, or any from prior sessions, have actually been merged yet.
- Item 10 (send to Aakash) still not resolved, not touched this session.
- No `shared/` edits made this session, all writes stayed in `workspaces/elvis/`.
