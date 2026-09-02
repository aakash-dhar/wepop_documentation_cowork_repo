# Org membership and org-flagged content

**Date:** 2026-09-02
**Owner:** Elvis
**Status:** Resolved
**Arose from:** phase-1/1.5 review item #11 (Moments), open question on what an "org event" is

The item #11 org analytics rule depended on knowing what makes an event an org event. Answering that
turned out to require the account and membership model underneath it, which had never been written down.

## The persona model was considered and withdrawn

A model was worked through in which a user held a personal account and a separate org member account,
switchable in their profile, with separate follower graphs, separate ratings and separate feeds, linked in
the backend but never linked in the interface. The motivating case was a user who uses WePop personally and
also as an employee of a business.

**Withdrawn for phase 1, may return when businesses are onboarded.** It solves a business-account problem
that student orgs do not have. In a student org the person running the climbing club is the same person you
would meet at the bar, and everyone involved already knows it, so a separated identity buys nothing and
costs a great deal: a linkage that must never be inferable from recommendations or mutual-contact counts, a
persistent mode with its own class of posting-to-the-wrong-account errors, a double-join problem on
capacity-limited events, and a ban model that has to be scoped across identities.

Withdrawing it also puts this back in line with DEC-041 to DEC-044 rather than extending them, since those
were written for a one-identity world.

**Recorded for the future:** if personas return, the seam that survived scrutiny was reputation
persona-scoped and enforcement person-scoped, which is the reputation-versus-enforcement split from
2026-08-30 applied on a second axis. The privacy constraint that would need building alongside it is that
follow recommendations must never traverse the person record, which is the documented way this pattern
leaks in other products.

## One account, RESOLVED 2026-09-02

A user has **one individual account.** An org is a page they may create and administer, or belong to, not a
second identity.

- **Admins** switch from their personal account into the org account to reach analytics and org management
  surfaces. The org account is an administration console rather than an identity.
- **Members do not switch.** They stay in their personal account and see the orgs they have joined.

## Membership is distinct from following, RESOLVED 2026-09-02

Two different relationships to an org.

| | Following | Membership |
|---|---|---|
| Who may | Anyone | Approved or invited |
| Grants | The org's public content in feed | The org's discussion board, member-only content, and the "Create as Member" button when enabled |

**Joining is the admin's choice per org, in two modes: request-and-approve, or invite-only.**
Request-and-approve is the default, since student orgs mostly recruit openly and an approval queue is the
lightest control that still gives an admin a say. Invite-only covers closed groups.

**The org's privacy setting governs visibility of members and member-only content, never the org's
existence.** A private org still appears in search by name, with its member list and member-only content
shielded. Making orgs invisible would mean nobody can find a club in order to request to join it, which
defeats the purpose of the page. This follows Meetup, which keeps private groups discoverable in search and
shields the membership data rather than the group.

## Creating content for an org, RESOLVED 2026-09-02

**The org admin controls whether members may create events and ideas for the org.** When enabled, a
**"Create as Member"** button exists on the org's profile. When disabled, it does not.

Content created that way is **org-flagged**: it appears on the org's page and counts in the org's analytics.

**Two entry points, one action.** The button on the org page is the primary path. The ordinary create flow
also offers a choice of creating as yourself or for a specific org. Both must produce identical results, and
the picker in the ordinary flow lists only orgs where the user actually holds create permission.

**Why the button lives on the org page.** Placing the entry point inside the org's own page means location
supplies the context, so there is no persistent global mode to lose track of and no class of error where a
user attaches the wrong org because they forgot which mode they were in. The affordance is where the meaning
is.

**Content not created that way is an ordinary personal event or idea.** It does not appear on the org page,
and it is discoverable normally through search, the home feed and the creator's profile.

## The event is not created under the org's name, RESOLVED 2026-09-02

Org-flagged content is still hosted and attributed to **the individual who created it.** The org supplies
context and discovery; the person carries responsibility.

An attendee sees something of the shape "Seoul Climbing Club, Weekend Bouldering, hosted by Minjun." This
reads better than org-as-host for an in-person meetup product, because someone deciding whether to meet
strangers wants a human name attached, and it keeps host accountability pointed at an account that can be
sanctioned.

### What the org flag does and does not do

| | |
|---|---|
| Counts in the org's analytics | **Yes**, basic figures, meaning counts |
| Appears on the org's page | **Yes** |
| Displays under the org's name as host | **No** |
| Restricts the audience to org members | **No.** Audience scope is a separate control |

**Audience scope stays independent of the flag.** A user may create an event that is open to org members and
to others. An org-flagged event that is open to the public is a normal thing a club would want, and
restricting it is the existing per-event audience control from item #11 rather than a consequence of the
flag.

## Org admin access: no elevation, RESOLVED 2026-09-02

**An org admin gets general information about an org-flagged event or idea. If they did not join it, they see
neither its details nor its Moments.**

The simplest correct statement of this is that **the admin receives no elevation at all.** They see exactly
what any user in their position would see, plus the basic counts the org is entitled to as analytics:

- A **public** event's page looks the same to an admin as to anyone else.
- **Attendee-gated content stays gated.** Moments require having joined, for an admin as for anyone.
- **Basic counts** are the org's, since the event carries its flag: how many joined, how many Moments and
  media items, engagement figures. Counts, never content.

Framing it as no-elevation rather than as a carve-out matters for implementation. There is no special admin
path on the event object to write, and therefore none to get wrong. The existing visibility checks already
produce the right answer.

A stronger version was considered and rejected: full admin access to everything on an org-flagged event
including its Moments, on the reasoning that a club must be able to moderate what appears under its name. It
was withdrawn because it would make item #11's attendee cap untrue whenever an org is involved, and honouring
it would have required telling attendees at join time and again in the composer that club officers who did
not attend can see their photos. **The attendee cap therefore holds as originally written, with no exception
and nothing to disclose.**

**The cost, recorded rather than argued.** Detach is the only moderation tool an admin has over a member's
event. They cannot edit it and cannot take it down, only remove its association with the club. For student
orgs that is proportionate, and the create-permission toggle is the control for a member who should not be
posting under the club's name in the first place.

## The detach lever, RESOLVED 2026-09-02

**An org admin may remove the org flag from an event or idea, without ever having had access to its
content.** The event leaves the org page and leaves the org's analytics.

Title, date, host and basic counts are enough to judge that something does not belong on the club's page.
This is disassociation rather than surveillance, and it is the control that handles the case the
create-permission toggle does not anticipate, since the toggle is pre-approval and this operates after the
fact.

**Detaching a past event removes it from analytics history for that slice.** That is the intended reading of
a deliberate detach, since the admin is asserting the event was never the club's, but it does mean detach is
not purely forward-looking and the figures move.

## Ratings, RESOLVED 2026-09-02

**The org profile shows an aggregate rating derived from its org-flagged events.** The individual host keeps
their own rating regardless, unchanged from DEC-045 to DEC-047, since there is one identity in this model.
Both exist; they are not alternatives. The org aggregate is derived rather than a new rating flow, and it is
useful to someone deciding whether to join the club.

## When the creator leaves the org, RESOLVED 2026-09-02

The event was always theirs, so no host takeover is required. This is simpler than the org-account model,
where the org owned the event and administration had to pass.

- **Past events keep the flag**, so analytics history does not rewrite itself.
- **Upcoming events** may be detached by an admin with the lever above.

## Conduct sanction versus safety ban, RESOLVED 2026-09-02

The distinction survives the withdrawal of personas, in a simpler form: it is the ordinary difference between
**removal from an org** and **suspension of the account.**

- **Conduct sanction.** Spam, no-shows, rudeness, low-grade policy violations, most reports. The org removes
  the member. They keep using WePop.
- **Safety ban.** A short **closed** list: violence or credible threats, sexual misconduct, CSAM, fraud,
  stalking or doxxing. The account is suspended, and DEC-041's propagation carries it to any org the person
  operates.

**The list must be enumerated and closed, not "serious violations at reviewer discretion."** Open-ended
severity judgments are how an escalation path drifts. Adding a sixth category should be a decision rather
than a reviewer's call.

## Flags for Deepak

- An event carries a nullable org reference set at creation. Org analytics filters on it. No second account
  table, no persona linkage, nothing to propagate.
- The create-permission setting is per org, and the ordinary create flow's org picker must be filtered by
  it, not merely hidden in the UI.
- **Org admins receive no elevated read path on the event object.** Existing visibility checks already
  produce the correct result. Do not add an admin bypass; there is nothing to add.
- The org's entitlement from the flag is **counts only**. The analytics pipeline must not join to event
  details, Moment content or author identity.
- The detach lever mutates only the org reference. It must neither require nor grant read access to content.
- Org rating is derived from org-flagged events at read time rather than stored as a second rating.
- Membership and following are two separate relations, not a flag on one. Member-only content checks
  membership.
- Private org means the member list and member-only content are shielded. The org record stays indexed for
  search by name.

## Not decided here

- Whether an org admin needs any moderation power beyond detaching, given they cannot see a members-only
  event's details. Detach is specified as the only lever; editing or taking down another person's event is
  not.
- Whether an org's analytics distinguish counts on member-only events from those on public events, or report
  them together. Carried over from item #11.
- How a member's create permission interacts with suspension, meaning whether a suspended member's
  org-flagged upcoming events are auto-detached or left for an admin.

## Sources

- Meetup private group behaviour: groups remain discoverable in search with membership data shielded.
