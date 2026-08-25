# Feature backlog, 2026-08-25 intake

> Elvis workspace working file. Twelve items raised together 2026-08-25, explicitly a mixed batch,
> Elvis's own framing: "some of the things can be done in a later phase, but I want to discuss a bit
> now." This file captures and sizes all twelve so nothing is lost, and flags which already connect
> to decisions made elsewhere. Deep design happens item by item, prioritized separately, not all at
> once in this pass.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Sizing key

Small: a contained addition to an existing surface, one real design conversation covers it. Medium:
a real new mechanic with several genuine decisions, worth its own file. Large: effectively a new
product pillar, likely its own multi-session design thread, possibly its own phase.

## 1. Event schedule / itinerary. Size: Small. RESOLVED 2026-08-25.

Host adds structured stops to an event, time, location, a note ("Meet at Hongdae Station at 9am").
Fully scoped 2026-08-25, see `event-schedule-2026-08-25.md`: visibility inherits the event's own
access level exactly (whatever granularity that turns out to be, not a binary public/private rule),
each stop's location reuses the DEC-003 map picker, and multi-day stops are supported only when the
event itself spans multiple days, flagged as a data-model dependency for Deepak to confirm.

## 2. Live recordings during an event (Stories-style). Size: Medium, real safety flag. RESOLVED 2026-08-25.

Fully scoped 2026-08-25, see `live-stories-2026-08-25.md`. A separate content type from Moments,
ephemeral (24-hour expiry, matching Instagram Stories directly), posting only requires RSVP not
check-in (deliberate, to allow pre-arrival journey/excitement posts). Visibility is poster-chosen per
post from four tiers (mutuals, followers, event attendees, public), defaulting to the most
restrictive, rather than inherited from the event the way Moments and the schedule work, since the
same event can have posters with opposite needs (a private user versus a promoter or influencer).
Two real items flagged, not yet decided: whether live stories count against the org tier's existing
50-item media cap (likely not, given the very different ephemeral cost profile, but not confirmed),
and reactions/replies (parked, not designed).

## 3. Free Now (real-time availability plus location-pinned chatrooms). Size: Large, highest safety flag on this list. RESOLVED 2026-08-25.

Fully scoped 2026-08-25, see `free-now-2026-08-25.md`. Location is rounded/approximate, not an exact
pin. Room visibility is aggregate-first (anyone can browse which rooms exist and roughly how many
people are free), with individual identities revealed only on reciprocal join, matching yourself as
free too, mirroring the mutual-follow reciprocity already locked in item 8. A new binary avatar status
badge (no location attached) is visible to followers/mutuals only. Creating a pinned room requires
account standing beyond normal phone verification, exact threshold still open. Several secondary
details flagged with recommendations but not confirmed: duration cap, the exact account-standing
number, room auto-archival, whether org accounts can create a room, and moderation tooling called out
as a required baseline, not optional scope.

## 4. Ticketing, tiers, discounts, a WePop fee on sales. Size: Large. Already captured.

Already flagged in `freemium-model-2026-08-19.md` as "likely the single largest piece of technical
scope in the project," needing Stripe-Connect-style payment splitting, host identity verification,
refunds, chargebacks, and tax reporting. Not re-opened here, still pending its own dedicated
conversation. Item 10 below ("commission/fees on ticket transactions") is the same thread, not a
separate one.

## 5. Gamification and a virtual goods store. Size: Large. Already captured.

Already flagged in `freemium-model-2026-08-19.md` as deferred, "this will be introduced when we do
gamification at a much later phase." Directly connects to item 12 below (mascot and customizable
avatars, spent via the same virtual goods store) and to the individual paid tier's parked idea of
monthly points redeemable toward tickets. These three belong in one dedicated gamification-and-economy
conversation, not designed piecemeal.

## 6. Event icebreakers. Size: Medium. RESOLVED 2026-08-25, split across phases.

Fully scoped 2026-08-25, see `icebreakers-2026-08-25.md`. Split into three mechanics rather than one
feature: phase 1 is a host-authored question game only (up to 3 read-only questions, check-in gated,
opt-in by construction via a button on the event page). Aggregate-tag matching and a card/scavenger
matching game both moved to later phase, not designed in detail yet, though the scavenger game's
match-confirmation mechanic (in-app tap/scan, like check-in) is already locked for whenever it's
built.

## 7. Tips and guides for shy/introverted users and first-time hosts. Size: Small to medium. RESOLVED 2026-08-25.

Fully scoped 2026-08-25, see `tips-guides-2026-08-25.md`. A contextual "more info" icon, available
wherever relevant, shows tips for the current situation, with a "see all" option leading to a static
browsable guide. Opt-in by construction, matching the phase-1 icebreakers pattern. Targeted by
situation and status (first-time user, first-time host) rather than any inferred or self-identified
personality trait. No content written yet, deliberately, this scoping covers mechanism and placement
only; actual copy is future work for the `design:ux-copy` skill.

## 8. Event music (host playlist or attendee-add, likely Spotify integration). Size: Medium to large, real external dependency.

Two distinct product questions (host-curated vs collaborative attendee-add) plus a real third-party
integration decision (Spotify API, OAuth, licensing considerations for shared/public playback). Worth
its own conversation once prioritized, the integration choice alone has real cost and scope attached.

## 9. Supporters marketplace (sponsors and supporters, financial or in-kind, get analytics/promotion in return). Size: Large.

A genuine two-sided marketplace: sponsors providing money or resources, supporters providing services
(venue, food and beverage, entertainment), in exchange for something (shared analytics, on-page and
in-space promotion). Likely depends on ticketing/payments infrastructure (item 4) existing first for
the financial-sponsorship half. Its own dedicated future conversation, not designed here.

## 10. Other business models: ticket transaction fees, ads and ad-bidding, promoted listings. Size: Large, partly already captured.

Ticket transaction fees are item 4, not a separate thread. Ads and ad-bidding were already flagged in
`freemium-model-2026-08-19.md` as deferred, Elvis's own words, "we can discuss about ads later."
Promoted listings (paying to boost an event, idea, or org in discovery, similar to a boosted post or a
promoted marketplace listing) is a new, lighter-weight idea not previously raised, worth noting as
related to but smaller than a full ad-bidding system.

## 11. Web version. Size: Not a feature design question, a platform roadmap item.

Explicitly later-phase per Elvis. Nothing to design yet beyond logging it as a known future platform
target; revisit when the mobile build is far enough along that a second platform is a real question.

## 12. Mascot and customizable character avatars. Size: Large. Already grouped, see item 5.

Spent via the same virtual goods store as item 5, and explicitly funded by the same later-phase points
system. Branding plus gamification, belongs in the same dedicated conversation as item 5, not designed
separately.

## Grouped for one future conversation each, not this pass

- **Payments and monetization infrastructure:** items 4 and 10 (ticketing, transaction fees), and item
  9 (supporters marketplace) once payments infrastructure exists.
- **Gamification and economy:** items 5 and 12 (virtual goods, points, avatars, mascot).
- **Ads and promotion:** the ads/ad-bidding half of item 10, plus the new promoted-listings idea.
- **Platform roadmap, not a design thread:** item 11 (web version).

## Recommended near-term candidates, given the rest is genuinely later-phase or its own dedicated thread

Items 1 (schedule), 6 (icebreakers), and 7 (tips/guides) are contained enough to fully design in a
normal session each. Items 2 (live recordings) and 3 (Free Now) are not small, but carry real safety
implications worth addressing deliberately rather than leaving open indefinitely, they deserve
priority even though they're bigger, precisely because of the risk profile, not despite it. Item 8
(event music) is a real but self-contained integration decision whenever it's picked up.
