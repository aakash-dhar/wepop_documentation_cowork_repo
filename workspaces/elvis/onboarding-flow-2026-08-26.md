# Sign-up and onboarding flow, 2026-08-26

> Elvis workspace working file. The end-to-end onboarding sequence has never been assembled in one place
> before, it was scattered across DEC-011, DEC-012, DEC-016, DEC-019, DEC-005, DEC-024, DEC-026, DEC-027,
> and today's `org-invites-2026-08-26.md`. This file synthesizes those into one ordered flow and resolves
> the sequencing questions that weren't actually decided anywhere yet.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Reviewing the phase-1 list item by item, Elvis asked for the actual proposed flow for sign-up and
onboarding, not just a feature-status list. No single doc had this end to end; each piece (auth, age
gate, location, tags, cohorts) was decided independently. This assembles them into one sequence and
flags what's still genuinely undecided rather than inventing an order silently.

## Entry point, RESOLVED 2026-08-26: one screen, the Get Started screen, with a context toast for invites

All four branches below land on the same "Get Started" screen, not four separate screens. A deep-linked
invite (individual, org, or founder seed) opens the app to this same screen with a toast layered on top
sharing the invite context, who invited you and what to, per branch below. An organic, non-invited open
shows the same screen with no toast. This means the Get Started screen's language selector, top left (see
step 1 below), is automatically present for every entry path, since there is only one screen, resolving
the earlier open question about whether invited users get the same override.

**Individually invited (event/idea-specific):** Get Started screen, toast shows who invited you and to
what (event or idea), per the product overview's existing line. New users proceed into account creation
below; existing users just log in. Lands on the specific event/idea at the end, see "Landing destination"
below.

**Org-invited (`org-invites-2026-08-26.md`):** Get Started screen, toast shows who (the admin) and what
org, then join or log in. Lands on the org's discussion board at the end.

**Founder seed invite, RESOLVED 2026-08-26 (confirmed by Elvis):** at launch, Elvis will personally invite
an initial batch of users directly, to seed the platform before there is meaningful event/idea density for
the normal invite-first loop to run on. Confirmed by Elvis as following the same non-event-tied invite
mechanism just built for org admins (`org-invites-2026-08-26.md`), but with no org account associated,
WePop itself is the inviter, not an org. A third, distinct invite type alongside the person-to-person
individual invite and the org invite: individual invites are event/idea-tied, org invites carry
organizational identity, founder seed invites carry WePop's own identity as the credibility source instead
of either. Get Started screen, toast identifies WePop as the inviter. Lands on the home feed at the end,
not a specific event/idea, since there isn't one to return to.

**Not invited:** Get Started screen, no toast, this is the app's actual front door for anyone arriving
without a deep link, an organic download, not a distinct fifth branch. It offers log in for existing users
and funnels new users to the waitlist capture (email, phone, location, university), per DEC-024. A
waitlist user has no app access at all until auto-promoted (with a claim window). Once promoted, they enter
the same account-creation sequence below as any invited user, there is no separate onboarding path for a
promoted waitlist user, confirmed by Elvis explicitly. Lands on the home feed at the end, since nothing
invited them to one specific thing.

## Account creation and onboarding sequence, RESOLVED 2026-08-26 (expanded to Elvis's full detailed sequence)

1. **Language, RESOLVED 2026-08-26: cascade detection plus a persistent selector, no confirmation toast.**
   Detected on download and first open, from the device cascade (device language setting, then app/Play
   Store region, then phone number), a one-time read, not an ongoing check. No confirmation screen or toast,
   the app simply renders in the detected language from the very first screen onward. The manual override
   lives on the Get Started screen (see "Entry point" above), a language selector in the top left, always
   visible, letting the user change it before continuing into onboarding or logging in. This resolves the
   earlier open question about a one-time confirmation moment, Elvis's call was a persistent, always-
   available control instead of a one-time interruption.
2. **Auth.** Social login (Kakao, Apple, or Google), phone number always required regardless of provider.
   A provider-verified phone (Kakao, in Korea) can satisfy the phone requirement directly without a
   separate OTP step. Otherwise standard OTP, or Korea's carrier-based PASS verification specifically for
   Korean numbers (DEC-026).
3. **Age gate.** Self-declared birthdate, country determined by the existing store-region/device/phone
   cascade (DEC-012), locked at this point and never re-checked later, even as the user travels. Placed
   immediately after auth since it is a hard gate the user must pass, not an optional preference.
4. **Name.** A single flexible full-name field, not a Western first/last split, per the internationalization
   work. Broken out as its own step now, rather than bundled into auth, per Elvis's detailed sequence.
5. **Username.** Auto-generate feature offered by default, plus typed-suggestion matching, if the
   username the user types is taken, the system suggests close variants rather than just rejecting it.
6. **Location, city-level.** Required, typed or selected from a list/search, explicitly not a GPS prompt
   (DEC-016). Device GPS stays optional and contextual, requested later only when something specific
   benefits from it (Explore's map, for example). Moved to after the identity block above per Elvis's
   detailed sequence, was positioned right after the age gate in the earlier draft of this file.
7. **Profile photo.** Optional. Upload from library or capture via camera. If skipped, the profile
   defaults to the user's initials on a background color rather than a generic placeholder image.
8. **Gender.** Optional.
9. **Language and language proficiency, RESOLVED 2026-08-26: a new, separate field.** Optional, multiple
   entries allowed. This is distinct from the app's own display-language setting (the DEC-027/cascade
   field covering WePop's own UI copy), it represents languages the user personally speaks, confirmed by
   Elvis as its own field rather than reusing or inferring from the display-language setting.
10. **Personality tags.** Optional, multiple entries allowed, searchable, and extensible, the user can add
    a tag that doesn't already exist. Feeds the recommendation algorithm's personality-mix signal
    (DEC-005/group dynamics).
11. **Categories and subcategories, RESOLVED 2026-08-26: a distinct system from personality tags.**
    Optional, multi-select, topic/activity interests. Confirmed by Elvis as a second, separate taxonomy
    from personality tags above, not one shared tag system, even though both are searchable multi-selects.
    Feeds the recommendation algorithm's tag-overlap signal (DEC-020). The actual taxonomy content, 8
    categories (85 subcategories) plus Other, browse-only picker, and real selection limits (up to 5
    subcategories from at most 3 categories here at onboarding, matching the "user profile" row, not the
    tighter per-event limit), is specified in full in `categories-taxonomy-2026-08-27.md`, not invented
    here.
12. **Campus affiliation, RESOLVED 2026-08-26: optional.** Verified via school email with a code sent to
    that address, or, if the user's school isn't in the pre-populated list, a self-declared "suggest a
    school" fallback. Confirmed optional, a non-student or a student who prefers not to verify can skip
    it and proceed. This is the same university-affiliation step resolved earlier in this file (asked
    directly during onboarding, not inferred or deferred), now with its verification mechanism specified
    and repositioned later in the sequence per Elvis's detailed list, it was positioned right after
    location in the earlier draft. Since it's skippable, DEC-019's cohort computation at step 13 needs to
    degrade gracefully to city and age bucket alone when this step is skipped, see Deepak flags below.
13. **Cohort computation.** Invisible to the user, no explicit "pick your cohort" screen. Computed
    automatically from city (step 6), age bucket (step 3), and the campus-affiliation answer (step 12),
    per DEC-019, now running after step 12 rather than immediately following it as in the earlier draft.
14. **Device permissions review, RESOLVED 2026-08-26: a lighter in-app screen only.** Optional. Location,
    notifications, camera, gallery, contacts, and calendar are presented together as an in-app screen
    explaining what each is for, this does not itself trigger native OS permission dialogs. Consistent
    with DEC-016's contextual-only stance for location specifically, now generalized to the other
    permission types too, the actual native prompts stay deferred to first contextual use of each.
15. **Done.**

## Profile completion, moved out of onboarding, RESOLVED 2026-08-26

Optional email, optional password, and the profile description field (the latter previously an open todo,
"onboarding or later," now resolved) all move out of the account-creation sequence above entirely. None of
the three block or lengthen onboarding. Instead they live as editable fields in the profile, available for
the user to fill in whenever they choose, with periodic notification reminders nudging completion when a
field is still empty. This is a deliberate simplification of the sequence above, fewer required-feeling
steps between signup and the home feed, the fields that are least likely to affect first-session experience
(a backup login method, a bio) are exactly the ones pushed to "whenever," while identity, location, and
interest signals that shape what the user sees on day one stay in onboarding.

The optional-password decision itself is unchanged, still additive to social-plus-phone auth, still
reverses DEC-011's "password deferred" provision, only its placement changed, profile settings instead of
an onboarding step. The proposal in `proposed-decisions.md` is updated to reflect this.

## Landing destination, RESOLVED 2026-08-26

Once onboarding finishes, an invited user (individual or org) lands back on the specific thing that
brought them there, the event, idea, or org they were invited to, ready to act on it immediately rather
than needing to navigate back themselves. A user who was on the waitlist and just got promoted has no
specific destination, since nothing invited them to one thing, so they land on the home feed, immediately
cohort-filtered and ranked per the recommendation algorithm (DEC-020).

## Not yet decided, deliberately parked

- Exact copy/framing for the founder seed invite (entry point section above), what the invite screen says
  when WePop itself, not an org or an individual, is the inviter. Not written here, a ux-copy pass once
  this is built, same open item org invites already have for their own credibility copy.
- Reminder cadence for the profile-completion nudges (email, password, description). Elvis's own framing
  was "every so often," not a specific schedule, exact frequency, whether it decays over time, and whether
  a user can dismiss or snooze the reminder are not decided here.

## Flags for Deepak, implementation, not decided here

- This is the first time the full sequence has been assembled in one place, worth using as the actual
  build reference for the onboarding flow rather than reconstructing it from scattered DEC entries.
- Needs branch logic at entry: individual invite, org invite, founder seed invite, and promoted-waitlist
  all funnel into the same account-creation sequence, only the landing destination at the end differs.
- Entry is one screen (Get Started), not four. Deep-linked invites render the same screen plus a toast
  component sourced from the invite record (inviter identity, and event/idea or org name where relevant),
  organic opens render the screen with no toast. Simpler to build than separate per-branch screens, and
  it's why the language selector doesn't need separate handling per branch, it's on the one shared screen.
- Founder seed invite needs its own invite-record shape, alongside individual (event/idea-tied) and org
  (org-identity-tied) invites: WePop as inviter, no org reference, no event/idea reference, otherwise
  reusing the same non-event-tied invite pattern (`org-invites-2026-08-26.md`) end to end.
- Campus affiliation (step 12) is optional and needs to feed cohort computation at step 13 when present,
  alongside city and age bucket, consistent with DEC-019's existing three-signal affiliation check
  (self-declared here, plus school email domain and org-profile membership as the other two, which can
  still apply even when this onboarding answer is skipped or "no" at signup, if verified later). When
  skipped, cohort computation needs to degrade gracefully to city and age bucket alone rather than error
  or block, this graceful-degradation path is not itself designed in DEC-019, worth a dedicated check.
- Language cascade (step 1) needs to run on download and first open, before any UI renders, ideally
  resolved before the Get Started screen (with or without its invite toast) even shows, so the very first
  thing a user sees is already in the right language.
- Get Started screen needs a persistent language selector, top left, that lets the user override the
  cascade's result at any point before continuing, distinct from the profile settings language field a
  logged-in user already has, this is the pre-account version of the same override.
- Username step 5 needs both an auto-generate algorithm and a taken-username suggestion algorithm, exact
  generation logic (adjectives+nouns, handle-plus-number, etc.) not specified here.
- Device permissions screen (step 14) must not fire native OS permission dialogs itself, it is explanatory
  only, native prompts stay tied to first contextual use of each permission, same pattern as DEC-016.
- Language and proficiency (step 9) needs its own field, distinct in name and storage from the app's
  display-language setting (the DEC-027/cascade field), to avoid the two getting collapsed into one by
  accident at the schema level.
- Personality tags (step 10) and categories/subcategories (step 11) need two distinct taxonomies/data
  models, both searchable and extensible, but not backed by the same underlying tag table. Categories and
  subcategories are user-facing only and browse-only (no search, no user-submitted nodes), not the
  same shape as personality tags' general-vibe section, which is genuinely open and searchable. Full
  schema and picker behavior in `categories-taxonomy-2026-08-27.md`.
- Campus affiliation (step 12) needs an email-verification-code flow for the school-email path, plus a
  workflow for the "suggest a school not in our list" fallback, whether that queues for review or is
  auto-added is not specified here.
- Optional email, optional password, and description now live in profile settings, not onboarding, per
  the "Profile completion" section above. Backend still needs the same additive-password support as
  before, storage/hashing and a login-method fallback at sign-in, only the collection point moved.
- New: a profile-completion nudge system. Needs a scheduled/recurring job that checks each user's email,
  password, and description fields and sends a reminder notification while any stays empty, cadence not
  yet specified (see "Not yet decided"). Routes through the same notification pipeline that already
  follows the profile language field (`internationalization-korea-2026-08-26.md`), as one notification
  type among the pipeline's existing ones (event/idea activity, invites, and so on), not a new channel.
  Needs to stop once a field is filled.
