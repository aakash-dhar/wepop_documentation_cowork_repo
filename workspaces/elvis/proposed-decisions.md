# Proposed decisions from elvis - for merger review

> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Pending

Three proposals. Two from phase-1/1.5 review item #11 (Moments), working detail in
`workspaces/elvis/moments-2026-09-02.md`. One on the org membership model that item #11 turned out to depend
on, working detail in `workspaces/elvis/org-membership-2026-09-02.md`.

## DEC-NNN (PROPOSED)
**Date:** 2026-09-02
**Proposed by:** Elvis
**Source:** `workspaces/elvis/moments-2026-09-02.md`, phase-1/1.5 review item #11; amends DEC-015
**Topic:** Multiple Moments per event; card anchor loses the badge; DEC-015's stale video and cap text
corrected
**Type:** Product + Technical
**Decision:** Three amendments to DEC-015. (1) **A user may post multiple Moments to a completed event**,
replacing "one post per user per event". The motivation is structural rather than volumetric: a long event
may warrant the afternoon and the evening as separate posts instead of a false choice about which half to
keep. **There is no count limit on Moments.** A user may create as many as they want for an event; what is
bounded is their total media across all of them, per the clarification below. The constraint is on volume of
media rather than on number of posts, so someone who wants ten Moments of one photo each may have them.
(2) **The Moment card's event anchor frame is three elements, not four.** Handoff spec §3.5 defines the
anchor as structurally part of the Moment card and lists name, date, org and the attendance badge; DEC-045
withdrew that badge, so the component needs redesigning rather than shipping with an empty slot. (3)
**DEC-015's text on video length and media caps is corrected**, having been overtaken twice: its "flat
15-second cap and flat 10-media-item cap for everyone" was written while the paid tier was deferred, and
video is now 15 seconds free / 30 seconds paid at 720p H.264 on both Moments and event cover media, as
DEC-038 already asserts as standing.
**Clarification carried with this, not a change:** DEC-018's media caps are enforced **per attendee per
event**, summed across that attendee's Moments for the event, not per Moment.
`freemium-model-2026-08-19.md` states them that way in as many words ("50 media items per attendee, per
event") and gives the reason: per-user rather than a shared total, so every attendee independently gets their
allowance regardless of how many others already posted, with no blocked-after-the-cap-fills dynamic. The cap
only looked per-Moment because one Moment per event made the two the same object.
**Recap grid: every Moment is its own tile.** No grouping by author. The tradeoff is accepted rather than
overlooked and is recorded so it is not later filed as a bug: someone who posts eight Moments occupies
roughly eight times the grid space of someone who posts one, and at a twenty-person event a single prolific
poster can take a visible share of the recap page. Grouping by author was considered and rejected in favour
of the simpler flat treatment.
**Reasoning:** On the caps, moving to per-Moment would be a departure from what is decided rather than a
continuation, and it would remove any per-event bound: five Moments at ten items each is fifty items for a
free user, running straight through DEC-018's tiering and DEC-039's retention economics, which model 8 to 30
items per attendee per event. Holding the cap per attendee per event is also what makes an unlimited post
count safe, since the bound that matters is already enforced elsewhere and a second limit on post count would
constrain nothing that the media cap does not. Comparable practice supports the per-attendee shape for this
product specifically: Apple Shared Albums caps a shared album at 5,000 items **combined across all
contributors**, with per-contributor limits acting only as anti-abuse rate limits, which works at 5,000
because nobody reaches it but would bite constantly at 10 or 20 or 50, letting an enthusiastic early poster
consume the budget before other attendees get home. On the anchor frame, the denormalized fields are
unaffected and this is worth stating so nobody "fixes" it: `event_name`, `event_date` and `org_name` are
copied at creation so the card survives event deletion, and the badge was always derived at render time
rather than stored.
**Impact:** Amends DEC-015 on three points. Deepak flags: media caps are enforced per attendee per event,
summed across that attendee's Moments; the anchor component drops to three elements with no change to the
denormalized fields or the tombstone path. The recap page grid previously never had to render more than one
Moment per person and now does, as flat tiles with no author grouping.
**Relates to / Supersedes:** Amends DEC-015. Consistent with DEC-018 and DEC-038 (caps and video), DEC-039
(retention economics), and DEC-045 (badge withdrawal, which forces the anchor change).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-09-02
**Proposed by:** Elvis
**Source:** `workspaces/elvis/moments-2026-09-02.md`, phase-1/1.5 review item #11; closes handoff open item
O-4
**Topic:** Moment visibility composes two gates; org scope is not a special case; comments; org analytics
**Type:** Product
**Decision:** **Moment visibility caps at its source event's audience, whatever that audience is.** A public
event lets the author publish anywhere; a private event caps at that event's attendees; an org event
restricted to members caps at that event's attendees, who are the members. One rule with three instances
rather than three policies, which **closes handoff open item O-4** (organization-scoped Moment visibility)
rather than deferring it. The Moment row still carries the source event's scope from day one.
**Profile privacy and item visibility are two independent gates that compose, and both must pass.** A
private profile shows only name, username, cover photo and background photo to non-mutuals, while mutual
followers see the full profile including Moments; the Moment's own visibility is capped as above.
Most-restrictive-wins across both.
**Comments are governed by two orthogonal controls, and separating them removes a class of special case.**
**Moment visibility** (only me / attendees / public) governs who can *see* the Moment and therefore who is
able to comment at all. A separate **comments toggle** (on / off) governs whether comments are *displayed*:
when off, only the author sees them and no new ones can be added. Consequences of keeping the two separate:
visibility changes need no special handling, so an only-me Moment simply behaves normally (it has exactly one
viewer, who is therefore the only possible commenter, and a note to self is harmless); **setting a public
Moment to only-me does not hide its comments**, since nobody else can reach the Moment at all and the
author continues to see them. Hiding is the toggle's job and only the toggle's job. The toggle **defaults on
for public and attendees-only Moments**; off hides existing comments from everyone except the author and
prevents new ones; on restores them and allows new ones. Copy at the point of turning it back on:
**"Turning on comments will restore 8 comments."** Comments are never deleted by either control. **The
toggle's state is stored on the Moment as its own field rather than derived from visibility**, since the two
controls are fully orthogonal and deriving one from the other would silently discard a choice the author
already made. Comments continue to inherit the Moment's visibility, so a commenter can never be seen by
someone who cannot see the Moment.
**Org analytics never include Moment content, and there is no org exception to the attendee cap.** An org
event restricted to its attendees keeps its Moments capped to those attendees. **An org admin receives no
elevation**: they see exactly what any user in their position would see, plus the counts the org is entitled
to because the event carries its flag. An admin who did not join a members-only event sees general
information and counts, meaning how many Moments, how many media items and how much engagement, and no
content, meaning no images, no captions and no author names. An admin who did join sees the Moments the
ordinary way through the event page, as any attendee would.
**Reasoning:** Both gates are needed because **a Moment is reachable from two places**, the author's profile
and the event page. Someone who cannot see a private profile may still legitimately reach that person's
Moment through an event they both attended, so profile privacy alone would wrongly hide it and item
visibility alone would wrongly expose the profile. Meetup composes the same two gates the same way and is
worth recording as precedent: a member can independently hide their group membership from their profile,
while in a public group member details stay visible to outsiders regardless of that setting, so the item's
context governs the item and the profile setting governs the profile. Meetup also keeps private groups
**discoverable** in search, shielding membership data rather than the group's existence, which is the reason
a private WePop profile should stay findable by name and username rather than becoming invisible. On
comments, the handoff's "hidden entirely when private" line is tagged [D] (derived, never confirmed) and
does not survive the two-control model: it conflates who may see a Moment with whether its comments are
displayed, and once those are separate controls the private case needs no rule of its own. On org analytics,
granting content access through the analytics surface would quietly make "capped to that event's attendees"
untrue whenever an org hosts, because an admin who was not there would reach the content through a side door.
Counts give the org the operational figure it is paying for without touching the cap, and the split matches
DEC-018's own line between operational numbers and content. A stronger version giving admins full access to
org-flagged events was considered and withdrawn, since honouring it would have required disclosing at join
time and in the composer that club officers who did not attend can see attendees' photos.
**Impact:** Closes handoff open item O-4. Deepak flags: visibility checks compose two gates and must both be
evaluated at render time, since the same Moment is reachable from a profile and from an event page by
different viewers; the comment toggle is a stored field rather than a function of visibility; comment hiding
is a visibility filter and never a delete, and restoring must bring back the original rows; the org analytics pipeline reads
counts only and must not join to Moment content, including author identity. Org admins get no elevated read
path, so no admin bypass should be written on the event object.
**Also filed here, since the handoff carries them but no decision does:** the Moment composer is the sole
media intake path, with one uploader, one EXIF and GPS stripping pipeline and one moderation queue, and the
Event Media tab and recap grid are filtered views with no upload of their own (§6.1); tagging requires opt-in
consent as a request the tagged person accepts (§12.6); Moments never display a private venue's exact address
(§12.6); host takedown is a request routed to review rather than an instant delete (§12.6); and a Moment
under review is hidden from public surfaces with a neutral owner-facing status (§12.6).
**What counts as an org event** is settled by the companion proposal below: an event is an org event when it
was explicitly org-flagged at creation, not by virtue of who created it. That prevents a member's personal
events from appearing in the dashboards of every org they belong to.
**Not resolved by this proposal:** whether an org's analytics distinguish Moment counts on member-only events
from those on public events, or report them together.
**Relates to / Supersedes:** Extends DEC-015's most-restrictive-wins principle. Closes handoff O-4. Relates
to DEC-006 and DEC-017 (the anti-stalking reasoning these gates serve), and to DEC-018 (the operational
numbers versus content line that the org analytics rule follows).
**Status:** Awaiting merger

## DEC-NNN (PROPOSED)
**Date:** 2026-09-02
**Proposed by:** Elvis
**Source:** `workspaces/elvis/org-membership-2026-09-02.md`; arose from phase-1/1.5 review item #11
**Topic:** One account rather than personas; membership versus following; org-flagged content and what the
flag does; org admin access; the detach lever
**Type:** Product + Technical
**Decision:** **A user has one individual account.** An org is a page they may create and administer, or
belong to, never a second identity. Admins switch from their personal account into the org account to reach
analytics and management surfaces, so the org account is an administration console; **members do not switch
at all** and stay in their personal account.
**Membership and following are two distinct relations.** Anyone may follow. Membership is granted by
**request-and-approve (the default) or invite-only, at the admin's choice per org**, and it grants the org's
discussion board, member-only content, and the "Create as Member" button when enabled. **The org's privacy
setting shields members and member-only content, never the org's existence**: a private org still appears in
search by name.
**The org admin controls whether members may create events and ideas for the org.** When enabled, a **"Create
as Member"** button exists on the org's profile and content created through it is **org-flagged**. The
ordinary create flow offers the same choice as a second door, listing only orgs where the user actually holds
permission. Content not created that way is an ordinary personal event or idea, absent from the org page and
discoverable normally through search, home feed and the creator's profile.
**Org-flagged content is still hosted and attributed to the individual who created it, not to the org.** The
flag makes content appear on the org's page and count in the org's analytics. It does **not** display the org
as host, and it does **not** restrict the audience, since audience scope stays the separate per-event control
from item #11 and an org event open to the public is a normal thing a club wants.
**An org admin gets general information about an org-flagged event, and if they did not join it they see
neither its details nor its Moments.** Stated as implementation rather than policy: **the admin receives no
elevation.** They see exactly what any user in their position would see, plus the basic counts the org is
entitled to because the event carries its flag. A public event's page looks the same to an admin as to
anyone; attendee-gated content stays gated; counts are the org's, never content. **An org admin may detach
the org flag from an event or idea without ever having had access to its content**, which removes it from the
org page and from the org's analytics. **The org profile shows an aggregate rating derived from its org-flagged
events**, while the individual host keeps their own rating unchanged from DEC-045 to DEC-047; both exist. **A
creator leaving the org triggers no host takeover**, since the event was always theirs: past events keep the
flag so analytics history does not rewrite itself, and upcoming ones may be detached.
**Enforcement, restated for this model:** a **conduct sanction** (spam, no-shows, rudeness, low-grade policy
violations) means the org removes the member and they keep using WePop, while a **safety ban** on a short
**closed** list (violence or credible threats, sexual misconduct, CSAM, fraud, stalking or doxxing) suspends
the account, with DEC-041's propagation carrying it to any org that person operates. The list is enumerated
rather than left to reviewer discretion on severity.
**Reasoning:** A persona model was worked through and withdrawn. It solves a business-account problem student
orgs do not have, and it costs a linkage that must never be inferable from recommendations or mutual-contact
counts, a persistent mode with its own class of posting-to-the-wrong-account errors, a double-join problem on
capacity-limited events, and a ban model scoped across identities. Withdrawing it also keeps DEC-041 to
DEC-044 as written rather than extending them. Attribution to the individual reads better than org-as-host
for an in-person product, since someone deciding whether to meet strangers wants a human name attached, and
it keeps host accountability pointed at an account that can be sanctioned. Placing the create entry point on
the org's own page means location supplies the context, removing any persistent global mode to lose track of.
On admin access, a stronger version was drafted and withdrawn in which admins saw everything on an org-flagged
event including its Moments, on the reasoning that a club must be able to moderate what appears under its
name. It would have made item #11's attendee cap untrue whenever an org is involved, and honouring it would
have required telling attendees at join time and again in the composer that club officers who did not attend
can see their photos. Framing the result as no-elevation rather than as a carve-out also matters for
implementation, since there is no special admin path to write and therefore none to get wrong. The accepted
cost is that detach is the only moderation tool an admin holds over a member's event, which for student orgs
is proportionate, with the create-permission toggle covering a member who should not be posting under the
club's name at all. Membership defaults follow Meetup, which keeps private groups discoverable and
shields membership data rather than the group, since invisible orgs cannot be found in order to be joined.
**Impact:** Answers what an org event is, which item #11's analytics rule depended on. Deepak flags: an event
carries a nullable org reference set at creation and org analytics filters on it, with no second account
table and nothing to propagate; the create-permission setting is per org and must filter the create flow's
picker rather than merely hide it; org admins receive no elevated read path on the event
object, so existing visibility checks already produce the correct result and no admin bypass should be added;
the org's entitlement from the flag is counts only, and the analytics pipeline must not join to event details,
Moment content or author identity; the detach lever mutates only the org reference and must neither require
nor grant read access to content, and detaching a past event moves that slice of analytics history; org rating is derived at read time rather than stored; membership and following
are separate relations; a private org stays indexed for search by name.
**Not resolved by this proposal:** whether an org admin needs any moderation power beyond detaching, given
they cannot see a members-only event's details; whether org analytics distinguish counts on member-only events from public
ones; and whether a suspended member's org-flagged upcoming events are auto-detached or left for an admin.
**Relates to / Supersedes:** Consistent with DEC-041 to DEC-044 (host accountability, suspension propagation,
admin transfer) and DEC-045 to DEC-047 (host rating). Supplies the org-event definition the companion item
#11 visibility proposal depends on. Extends DEC-018's operational-numbers-versus-content line.
**Status:** Awaiting merger

---

## Landed

- **2026-08-31 (second merge): three decisions landed as DEC-045 to DEC-047** (check-in badge and scoring
  weight withdrawn with stars corrected to 1-5 and the display gate at 3 ratings; check-in reversed to
  host-scans-attendee as an operations tool; feedback uniformly anonymous with a 7-day edit window and
  author-visible only in the profile). DEC-034 carries a change-history note recording the partial
  supersession. Source: `workspaces/elvis/ratings-checkin-2026-08-31.md`.
- **2026-08-31: eleven decisions landed as DEC-034 to DEC-044**, covering the 2026-08-29 handoff-spec intake
  batch and the 2026-08-30 batch (Ideas lifecycle, event schedule, change notifications, completed-event
  deletion and detachment, host accountability).
- 2026-08-28: five decisions landed as DEC-029 to DEC-033.
