# Org invites, 2026-08-26

> Elvis workspace working file. Raised while reviewing item 1 of the phase-1/1.5 list (invite-first
> onboarding + waitlist): should an org be able to invite users directly, not just individual members.
> Resolved same day via a discussion round.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

The existing invite-first model (walkthrough, CLAUDE.md section 8) is person-to-person: an invite always
points to a specific event or idea, from Elvis or an existing member, to defeat the cold-start problem
and avoid generic recruitment spam. Elvis raised whether an org account should also be able to invite
users, since a real early-growth path is convincing an existing club's president to bring their whole
membership onto WePop, rather than relying only on individual members inviting one person at a time.

## Who can send an org invite, RESOLVED 2026-08-26: admins only in phase 1, configurable later

**Phase 1:** only an org's admin(s) can invite users into the org. No member-suggestion or review-queue
machinery is needed at launch, this keeps phase-1 scope small and matches how org accounts already have
an owner/officer structure (ownership transfer for officer turnover is already phase-1 scope).

**Later phase, direction only, not designed here:** org settings gain a configurable invite policy, an
org can choose between admin-only (the phase-1 default), a member-suggests/admin-reviews model (any
member can propose an invite, it only reaches the invitee once an admin approves it from a queue, so a
declined suggestion never reaches the invitee and never creates a bad experience for them), or open to
all members. Not scoped further, a future pass once real org usage shows which pattern orgs actually
want.

## Invite type, RESOLVED 2026-08-26: org invites are not tied to an event or idea

This is a deliberate, scoped exception to the invite-first invariant, not a general loosening of it.
Individual, person-to-person invites keep working exactly as they do today, always tied to a specific
event or idea. Org invites are a second, distinct invite type that draws its credibility from
organizational identity instead: an org admin can invite someone to join the org itself, with no event or
idea required first.

**Reasoning, worth recording precisely since this touches a core product invariant:** the invite-first
rule's actual job is giving the invitee a concrete, credible reason to trust the invite is not spam, an
event does that by being specific, but a real club president inviting an actual member of their real,
existing club satisfies the same underlying purpose through the relationship and community itself, not
through an event. Elvis's own example: WePop convincing a student club president to bring the club's
existing membership onto the app is a real, meaningful early-growth path, and forcing the president to
invent a first event or idea unilaterally before being able to invite anyone creates unnecessary friction
and skips the point, the club should be able to plan together once they're in the app, not have their
first activity decided for them by one person just to unlock invites.

**Residual risk, flagged, not fully mitigated by phase-1 scope alone:** removing the event/idea
requirement does reopen some of the spam surface invite-first was built to close, an admin could in
principle paste a large, low-context contact list into an org invite. Admin-only sending in phase 1
narrows this (a smaller, more accountable set of actors than "any member"), and org accounts launching
with university clubs first (not yet-undesigned promotional accounts) further narrows it, since these are
real, identifiable organizations, not anonymous actors. Worth remembering this exception was scoped
against that specific context: revisit whether it should still apply unmodified once promotional/business
org accounts are designed later, they were not part of this decision.

## Invite credibility, RESOLVED 2026-08-26: the invite must show who and what

Since there's no event to lend an org invite its specificity, the invite itself needs to carry that
context directly: who is inviting (the admin's name) and what they're being invited to (the org's name
and identity), for example "Minjun, president of Seoul Hiking Club, invited you to join their club on
WePop." This is necessary design hygiene to preserve the same credibility an event-tied invite gets for
free, not optional polish.

## Landing experience, RESOLVED (pointer only) 2026-08-26: a discussion board, same pattern as events/ideas

Once invited members join an org, they get access to a discussion board, the same pattern events and
ideas already have on their detail pages (per DEC-009/DEC-013's event and group chat: text, photos,
replies, reactions). This gives a newly onboarded club a place to plan their first activity together
rather than requiring the admin to have already decided one. Elvis explicitly deferred the fuller design
of organizational accounts to a later, dedicated pass, this is recorded as the resolved landing-state
direction only, not a full spec of org-level discussion boards (permissions, whether it differs from the
event/idea version in any way, moderation surface, and so on all remain open for that future pass).

## Not yet decided, deliberately parked

- The later-phase configurable invite-policy setting (admin-only / suggest-and-review / open to all
  members) is direction only, not designed, see above.
- Whether the event/idea-exemption for org invites should be narrowed once promotional/business org
  accounts exist, flagged above, not a phase-1 question.
- Full design of the org-level discussion board (any permission differences from the event/idea version,
  moderation ownership, whether it's a distinct chat thread or literally the same underlying mechanism)
  explicitly deferred to a dedicated organizational-accounts pass.
- Exact invite-credibility copy/UI (org logo, admin photo, any additional context) not written here, a
  ux-copy pass once this is built. The delivery mechanism itself is resolved though: the org-invited user
  lands on the same "Get Started" screen every entry path uses, with a toast layered on top carrying this
  context (`onboarding-flow-2026-08-26.md`), not a separate dedicated screen.

## Flags for Deepak, implementation, not decided here

- Needs a second invite type distinct from the existing event/idea invite: org-issued, no event/idea
  reference required, admin-only sender in phase 1.
- Invite record/notification needs to carry inviter identity and org identity for display, not just an
  invite token, so the credibility framing above can actually render.
- Org-invited members should land with discussion-board access on join, reusing the existing event/group
  chat mechanism's pattern (DEC-009, DEC-013) rather than a new chat system, exact reuse-vs-new-instance
  shape to be confirmed in the future org-accounts pass.
- University-affiliated cohort assignment (DEC-019) already covers org-invited members automatically via
  the existing "membership in a university-flagged Org profile" signal, no new cohort logic needed for
  this specifically.
- Later-phase invite-policy setting (admin-only / suggest-and-review / open) needs its own settings-model
  and review-queue work when scoped, not phase-1 build scope.
