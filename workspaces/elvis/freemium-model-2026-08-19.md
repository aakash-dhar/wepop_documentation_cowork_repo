# Freemium model - working draft, 2026-08-19

> Elvis workspace working file. Grounded against `shared/PROJECT_STRATEGY.md`, whose "Commercial
> structure" section is explicitly marked "to fill, not discussed" as of 2026-08-17, so this is new
> content, not a revision of anything existing. Born out of the premium-tier flag raised while
> resolving item 5 (video on moments) in `conflict-review-2026-08-19.md`.
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Governing principle

Three buckets, so future "should this be premium" questions have a rule to check against rather
than being decided one at a time:

1. **Never gate marketplace actions.** Creating events, creating ideas, joining, RSVPing,
   waitlisting, chat, following. These are supply and demand in the network. Gating them shrinks the
   whole marketplace, not just one user's experience, and directly undermines the cold-start
   strategy `PROJECT_STRATEGY.md` names as the core moat: every invited user must be able to freely
   create the event or idea their invite points to.
2. **Quota-gate personal expression.** Depth or length of personal content, for example moment video
   clip length. Does not touch marketplace supply, closer to a storage or expression quota (Google
   Photos, Discord Nitro upload limits) than to gating who can host.
3. **Insight-gate analytics.** Reporting and insight layered on top of a user's own activity data.
   Touches neither supply nor expression. Well-precedented: Eventbrite, Meetup Pro, Discord Server
   Insights, and Instagram/TikTok business/creator tools all keep creation and posting free while
   charging for performance insight.

Deliberately kept out of this model for now: anything that pays for more visibility or discovery
placement. That is a materially more sensitive lever, since it risks cutting against the fairness
and anti-stalking brand stance already named as a moat differentiator. Not folded into "analytics"
implicitly; would need its own explicit decision if ever considered. Confirmed as a firm, locked
decision on 2026-08-19, not just a working lean: no paid ranking boost for events or ideas, full
stop.

**Bucket 1 refined, 2026-08-19.** Icebreaker activities were initially proposed as a paid personal
perk (bucket 2), then correctly moved to free. Reasoning worth keeping: an icebreaker improves the
quality of the event experience itself, which benefits the whole marketplace (a better event is
better for every attendee, not just the host who paid), not just the individual who paid for it. The
test for bucket 1 vs bucket 2 is not "does this touch content the user made" but "does gating this
shrink the marketplace or event quality for people other than the payer." Useful precedent for the
next feature that comes up ambiguous.

## Tier structure: RESOLVED, shape settled 2026-08-19

Two separate premium tiers, not one flat tier, priced differently, each on its own timeline.

- **Individual tier: content fully specified 2026-08-19, ship timing still HELD, not phase 1.** The
  bundle is no longer thin, three real perks (see feature detail below), but the decision to delay
  building App Store / Play Store IAP infrastructure until phase 1 has usage data still stands. Phase
  1 ships a flat 15-second video cap and a flat 10-media-item moment cap for everyone; see the
  correction in `conflict-review-2026-08-19.md` item 5. Revisit trigger for shipping: once real
  phase-1 usage data exists, no longer blocked on finding more candidate perks, that part is done.
- **Organization tier: proceeding, one price for now (not split by club vs. promotional/business).**
  Content is a free/paid split, not all analytics behind the paywall (see feature detail below, this
  refined 2026-08-19 after this summary was first written): per-event operational numbers are free
  hosting functionality, aggregate rollups, cross-event trends, and export are the paid layer. V1 and
  phase-1.5 feature split confirmed below. One subscription covers the whole multi-member
  Organization account rather than per-officer billing. Mechanics (trial, billing cadence,
  grandfathering) below.

**Reasoning on record.** Willingness to pay differs by roughly an order of magnitude between an
individual casual host and an organization that needs the data to justify budget or validate a real
activation. A single flat price either underprices organizations or overprices individuals. The
split is not new complexity, it follows an account-type distinction the product already has
(individual vs Organization profile). It also keeps the individual tier's personal-perk lever
(video length) and the organization tier's analytics lever from being forced into one undifferentiated
bundle that serves neither buyer well.

**Price points, RESOLVED:** individual $3.99/month or $36/year (2026-08-19 / annual set 2026-08-24),
organization $19.99/month or $199/year (2026-08-24). Ratio between the two lands close to the
directional market pattern this section originally flagged before either number was set: consumer
"supporter" tiers in comparable apps typically run a few dollars a month, team or organization tiers
in comparable products typically run five to ten times higher.

## Individual tier: feature detail, RESOLVED 2026-08-19

**Price, RESOLVED 2026-08-24: $3.99/month, or $36/year on annual billing.** $36/year works out to
$3/month equivalent, about 25% off the $47.88 monthly-equivalent annual cost. Anchored slightly above
a pure storage-bump comparable like Discord Nitro Basic, reflecting the added engagement-analytics
feature, while staying accessible to the near-term student market.

**Included, three items:**

1. **30-second moment video clips**, versus 15 seconds free. Carries real incremental storage and
   transcoding cost per the video spec in `conflict-review-2026-08-19.md` item 5.
2. **20 media items per moment**, versus 10 free. Clarifying the data model this rests on: a moment
   is one post per user per event, fixed at one for everyone, not a paid lever. Media items within
   that one moment is the real lever. Also carries real incremental storage cost, and stacks with
   item 1, a paying user's worst-case moment (20 items at full 30-second length) runs to roughly 4x
   the storage of a free user's worst case. Still cheap in absolute terms, a small fraction of a cent
   per user in object storage at this volume, easily covered by the price above, but a real cost, not
   a free one, worth being accurate about rather than treating the tier as costless to deliver.
3. **Engagement analytics on the user's own events, ideas, and moments.** Aggregate breakdown by
   country, gender, age, and time of engagement. Same privacy boundary as the org tier: aggregate
   only, never named or individually identifiable, consistent with DEC-006. Note the dependency:
   gender as a breakdown dimension assumes gender is collected as profile data at all, which touches
   the still-open secondary item from the original review aid, whether to show gender and photos
   pre-join. That question is about pre-join display, not collection, so should not conflict, but
   flagged since it is the same underlying data.

**Explicitly considered and cut, recorded so they are not re-proposed without this context:**

- Profile background color customization. Cut for now.
- Profile banner customization. Not cut, but not paid either, made free for everyone.
- Personal activity recap (events attended/hosted, ideas created) and a new-connections count.
  Not included. A free user already has visibility into their own activity and connections without
  needing a paid feature to see it; this would not have been real insight, just a restated fact.
- Icebreaker activities. Not a paid perk. See the bucket-1 refinement above, moved to free for
  everyone since it improves event quality for the whole marketplace, not just the payer.
- Higher-resolution media export/download. Still fully parked, no free-vs-paid decision made either
  way, not part of this tier's launch content.

## Organization tier: analytics feature detail, RESOLVED 2026-08-19, refined 2026-08-19

Split the same way the calendar split in item 6: a real v1-at-launch bundle, and a phase-1.5 set that
needs real usage history to be meaningful at all. Confirmed 2026-08-19 after Elvis endorsed the
history-dependency principle. Refined same day to share an analytics engine with the individual tier
rather than building two bespoke systems.

**Billing unit: per-organization, RESOLVED 2026-08-19.** Not per-user across every org a person
administers. Standard shape for multi-tenant products (Slack workspaces, GitHub orgs, Notion Team
are all billed per-entity), matches how the actual buyer works (an org's budget pays for that org's
subscription), avoids a real arbitrage hole where one person managing several orgs, or later a
promotional/agency account managing multiple brand profiles, could cover many orgs' worth of value
on one subscription, and makes org ownership transfer clean, the subscription stays with the org
regardless of who currently administers it. Creating an Organization account itself stays fully
free regardless of how many a person creates, only the analytics layer on a given org is paid.

**Shared analytics engine with the individual tier.** One pipeline, one dimension set, two scopes
of query rather than two bespoke systems. Base dimensions match the individual tier exactly: country,
gender, age, time of engagement. Org tier adds two dimensions on top, since they matter more at org
scale than for a single person's own content: interest tags (which event types are landing, informs
what to plan next) and a new-versus-repeat split per event (a lighter, v1-appropriate cousin of the
full retention trend, which stays in phase 1.5).

**Reframed 2026-08-19: what's actually free versus what's actually paid.** Corrects the earlier
wording, which said "all analytics behind the paywall, no free baseline even for basic counts."
That refines rather than reopens: per-event operational numbers were never really "analytics" in the
sense that decision meant, they are baseline information a host needs to run their own event, the
same category as waitlist size. What the paid tier actually sells is the aggregation, trending, and
holistic reporting layer across the org's full event and idea history, plus the consolidated
exportable report.

**Free for everyone, no subscription needed, visible per-event or per-idea on its own page:**

- Views, joins, join rate, waitlist size
- Check-in rate and no-show rate, pulled from QR check-in
- Interested count on ideas and events (ties to the Kickstarter-style interest-validation mechanic
  named in `PROJECT_STRATEGY.md`'s go-to-market)
- Number of events actually made from an idea (maps directly to the idea-to-event core object model)
- Average event rating and average host rating, from item 1's post-event feedback

**Paid, v1, ships at launch:**

- Aggregate rollup of every free per-event/idea metric above, averaged and totaled across the org's
  entire event and idea history, holistic level and per-event/idea level together in one
  consolidated view, not scattered across individual event pages
- Attendee composition, aggregate only, on the shared dimension set with the individual tier
  (country, gender, age, time), plus interest tags and new-versus-repeat split, consistent with the
  DEC-006 privacy boundary, never named or individually identifiable
- Org member activity, aggregate only, never tied to a named member: ideas/events/moments created,
  last login, session duration. Deliberate choice, not an oversight: even for an org's own internal
  team, a named breakdown turns the tool into internal surveillance, which cuts against the same
  trust-first stance the product is built on. This is the principle to point back to if an org admin
  later asks for a per-member breakdown.
- Export: PDF primary, presentable enough to attach to a funding request, CSV as a secondary
  raw-data option. Two report shapes, a single event's report and a rolled-up period summary (for
  example "this semester"). Delivered both ways, not either/or: always available in-app in a
  receipts/reports section, and also emailed automatically when the org has an email on file.

**Paid, phase 1.5, needs real event history to be meaningful or safe to show:**

- Retention: share of past attendees who return to a later event
- Growth trend charts across an org's event history
- Segment and category performance: which demographic segments and which tags/categories perform
  best and worst, added 2026-08-19. Real value, tells an org exactly what to build more of, but
  needs a minimum-sample threshold before any segment or tag breakdown surfaces, for two reasons at
  once: statistical honesty (a "best performing" conclusion off two events is noise, not insight),
  and privacy (a small enough segment, three attendees in one age bracket, starts to approach
  identifying those specific people, the same small-sample problem already guarded against in item
  1's ratings design). Refined 2026-08-19: unlocks progressively, per tag and per segment
  independently, rather than as one all-or-nothing gate. Proposed starting thresholds, at least 3
  events under a given tag before that tag's performance shows, at least 5 attendees in a given
  demographic bucket before that segment's performance shows. Below threshold, the report states
  this directly rather than the feature silently not appearing, for example "Outdoor activities: 1
  more event needed for reliable data." Secondary effect worth keeping in mind: this nudges an org
  toward hosting more events regardless of whether they ever check the analytics, which helps the
  marketplace either way.
- Benchmarking, both against the org's own history and, once there is meaningful platform-wide
  volume, against similar orgs in aggregate, anonymized, never naming another org
- Scheduled recurring reports (for example an automatic monthly email summary). Not history-
  dependent like the rest, held back on build-priority grounds instead.

## Media caps, RESOLVED 2026-08-19

**Revised 2026-08-24: 50 media items per attendee, per event, at events hosted by an org on the
paid tier.** (Originally set at 100 on 2026-08-19, lowered to 50 on 2026-08-24 alongside locking the
org tier price, see below.) Per-user rather than a shared total, so it genuinely solves the fairness
problem a shared pool only partially addresses, every attendee independently gets up to 50 items
regardless of how many others already posted, no "whoever posts after the cap fills gets blocked"
dynamic at all. As a side effect, this also lowers the absolute worst-case cost ceiling per attendee
per event, reinforcing the manual safety-valve approach below rather than fighting it.

Precedence rule, since three numbers now apply depending on who's asking: whichever cap applies is
most generous wins, not additive. Free individual baseline (10) versus a paying individual's own
tier (20) versus an org-sponsored event (50), the highest applicable number governs, so a paying
individual at a paying org's event gets 50, not 70.

Worth naming as a real strength, not just a mechanic: this makes an org's subscription a benefit the
whole club feels directly at their events, richer moments, not just something the treasurer sees in
a back-office dashboard. That can create grassroots pressure from ordinary members for their club to
subscribe, not only a top-down budget decision.

**Event listing's own media (the host's cover photo and promotional gallery, separate from attendee
moments entirely): free tier gets 5 photos, org paid tier gets 20.** New lever, not previously
scoped; DEC-009 only restricted this for ideas (cover photo only, no gallery), events were never
limited the same way. Legitimate paid differentiator, a richer gallery genuinely helps a paying org's
event look more professional, and it is a real but modest storage cost, consistent with how the
individual tier's media perks are priced.

**Adjacent to this tier, both settled 2026-08-19, neither adds cost to the subscription:**

- **Moderation tools on an org's own events and moments: free for everyone, not part of the paid
  tier.** Same reasoning as icebreakers, moderating your own event's quality benefits every attendee,
  not just the org that paid, so it belongs in the never-gate bucket.
- **Attendee contact export for an org's own outreach: explicitly excluded, not just unaddressed.**
  Would cross the aggregate-only privacy boundary the analytics model is built on, an attendee did
  not consent to a host having their contact info for outreach beyond the event. If ever wanted,
  needs its own consent-flow design (an opt-in toggle somewhere in the join flow), not a quiet bundle
  into this tier.

**Price, RESOLVED 2026-08-24: $19.99/month, or $199/year on annual billing.** $199/year works out to
$16.58/month equivalent, about 17% off the $239.88 monthly-equivalent annual cost, a smaller discount
than the individual tier's roughly 25% since the org tier's margin is thinner in absolute dollars per
account and the annual commitment is worth more to WePop's cash flow here (club funding is typically
approved once per semester, so an annual option that clears in one approval cycle matters more for
this buyer). Set against the realistic-upper usage scenario modeled below (roughly $6.15/month per
org), not the extreme-tail scenario (roughly $24.60/month), which the manual safety valve exists to
catch instead of being priced against directly. At the monthly rate this nets roughly $10.99 a month
after the 15% App Store/Play Store commission even at realistic-upper usage, about a 55% margin; at
the annual-equivalent rate it nets roughly $7.94/month, about a 48% margin, before general
infra/support overhead not modeled here. Still reads as a reasonable line item against Meetup Pro's
$30 to $42/month, not a dominant one for a club budget.

## Deferred to future dedicated conversations, not designed here

Three threads surfaced while discussing what belongs in the individual tier. Deliberately not
designed today, recorded so they are not lost and not accidentally decided as a side effect of a
different conversation.

- **Ticketing and transaction fees.** Elvis wants a small transaction-fee discount for individual
  paid subscribers on ticket sales. This cannot be scoped or priced until ticketing itself exists,
  and ticketing is new, real scope: nothing about paid ticket sales appears anywhere in the
  walkthrough, `DECISIONS.md`, `HOTSHEET.md`, or either draft. Everything scoped so far is free to
  join, no money moves between users at all. Adding it means real marketplace-payments
  infrastructure: a payment-splitting provider (something like Stripe Connect), host identity
  verification before payout, refund and chargeback handling, and tax reporting obligations for
  hosts earning through the platform. Flagging plainly: this is likely the single largest piece of
  technical scope raised anywhere in this project so far, bigger than pulling chat and calendar into
  phase 1. Needs its own dedicated conversation, including whether it is phase 1 at all, before the
  fee-discount perk can be designed.
- **Ads and an ad-bidding system.** Elvis's own words: "we can discuss about ads later." Recorded, no
  design attempted.
- **Gamification and a points system**, spendable on in-app virtual goods or toward event tickets.
  Elvis's own words: "this will be introduced when we do gamification at a much later phase."
  Recorded, no design attempted. Depends on the ticketing thread above for the "pay for tickets with
  points" half.

## Org tier mechanics: RESOLVED 2026-08-19

**Trial.** 7 days, locked 2026-08-19. Full analytics access before the paywall engages, gives a
treasurer real data from their own events to bring to a funding request before committing.

**Billing cadence, RESOLVED 2026-08-24.** Monthly and annual, no separate semester tier. $19.99/month
or $199/year, about 17% off the monthly-equivalent annual cost (see price detail above). Practical
note carried forward, not a blocker: club funding is usually approved once per semester, so the
annual discount will be most accessible to a club that can get a full year approved at once. Worth watching whether
early adoption skews monthly for exactly this reason, and revisiting a semester option if so.

**Reimbursement support, detailed 2026-08-19.** Standard App Store / Play Store subscription
receipts are often too generic for a university reimbursement process; this needs to look like a
real invoice a treasurer can attach to a funding request, not a generic payment confirmation.
Fields: WePop's legal business name and address as issuer, the org's name as billed party, a
unique sequential invoice number, date of charge and the billing period it covers, plan name and
description, amount charged and currency. Standard business invoicing, nothing exotic. Delivered
both ways, confirmed 2026-08-19: always available in-app (a receipts/billing history section) and
also emailed automatically when the org has an email on file.

**Grandfathering.** Explicitly left open. No commitment made either way on whether early club
subscribers keep their price once a business/promotional tier launches. Decide when it actually
comes up rather than now.

## Cost context for margin modeling

Apple takes 30% of subscription revenue in a subscriber's first 12 months, dropping to 15% after
that, or a flat 15% from day one under the App Store Small Business Program (developers under
$1M/year in that store, which a startup at this stage would very likely qualify for). Google Play is
a flat 15% regardless of program or subscriber tenure. Practical planning assumption: budget around
15% off the top for now, not 30%, unless revenue crosses roughly $1M a year in a given store.

Sources: RevenueCat, "The 15% App Store Fee: A Guide for Developers (2026)"; Adapty, "App Store
Small Business Program: Everything developers need to know in 2026."

### Media infrastructure cost model, added 2026-08-24

Note: modeled against the 100-item cap that was in effect when this analysis was run; the cap was
lowered to 50 later the same day once the price was set (see Media caps above). The dollar figures
below are unaffected, none of the three scenarios modeled attendee usage anywhere near 50 items, let
alone 100, they model realistic behavior under the cap, not the cap itself. Left as originally
written rather than rewritten, so the modeling record matches what was actually run.

Modeled directly against the 100-items-per-attendee-per-event cap, using current published pricing
(Cloudflare R2, AWS S3/CloudFront, AWS MediaConvert, Cloudflare Stream), not estimated from memory.

**Architecture recommendation, not yet built, flagging for Deepak.** Store photos and finished video
files on Cloudflare R2 rather than AWS S3 plus CloudFront. R2's storage rate ($0.015/GB-month) is
close to S3 Standard ($0.023/GB-month), but R2 charges nothing for egress while CloudFront charges
$0.085/GB after a 1TB monthly allowance. For a social app where the same moment gets viewed
repeatedly by many attendees, egress, not storage, is normally the dominant cost, so this is a real
architecture decision, not a rounding difference. For video specifically, recommend a lightweight
self-hosted transcode step (a single 720p output, matching the individual tier's existing 720p30
H.264 spec) writing finished files to R2, rather than Cloudflare Stream. Stream is priced for
longer-form adaptive-bitrate libraries ($5 per 1,000 minutes stored, $1 per 1,000 minutes delivered),
and modeled below it comes out roughly 10x more expensive than R2 plus self-hosted transcode for
WePop's use case: short, single-rendition 15 to 30 second clips. Self-hosted transcode compute is
estimated, not sourced, at roughly $0.001 per clip on serverless compute (a 720p 15 to 30 second
encode is a small job); this needs a short build-time spike to confirm rather than being taken as
firm.

**Assumptions, flagged as estimates, not real usage data.** WePop has no live usage yet, so these are
reasoned estimates, not measurements, and should be revisited once the beta has real numbers. Average
photo size after client-side compression: 1.5MB. Average video: 20 seconds blended between the
15-second free cap and 30-second paid cap, at 3Mbps, about 7.5MB. Item mix: 80% photos, 20% video,
consistent with most social apps where video capture has more friction than photos. Uploads per
attendee per event: the 100-item number is a ceiling, not a typical case, the same way a paid
individual's 20-item cap does not mean every paid user posts 20 items to every moment. Two scenarios
modeled below to bound it.

**Moderate-usage org.** 4 org-paid events a month, 50 attendees per event, 8 items per attendee per
event average. That is 1,600 items a month. Holding 12 months of media online at any time (a
retention assumption, not yet a decision, see below), storage plus operations plus transcode comes to
roughly $1.10 a month per org. At this usage level, cost is close to a rounding error against any of
the three price points under discussion.

**Heavy-usage org.** 8 events a month, 150 attendees per event, 30 items per attendee per event
average, still well under the 100-item ceiling. That is 36,000 items a month. Under the same 12-month
retention assumption, cost comes to roughly $24.60 a month per org, with video (transcode compute
plus video storage) responsible for about two-thirds of that even though video is only a fifth of
item count, because a video file runs roughly 5x the bytes of a photo. At this usage level, a
$19.99/month price would be running a loss on infrastructure alone, before the App Store or Play
Store commission above is even subtracted.

**The real lever is retention, not the price point.** The heavy-usage number above compounds because
it assumes 12 months of full media held online indefinitely for an org that keeps producing at that
rate every month. An org that sustains heavy usage for years, not just one year, would see the
storage component keep climbing without bound. This is the same shape of problem "unlimited" plans
run into elsewhere: a flat price holds up fine against typical usage and only breaks against a
committed power user, which is exactly the kind of org WePop most wants to keep. Recommend deciding a
retention or archival policy for attendee-uploaded media (for example, full-resolution media stays
online for a fixed window, older media is archived to cheaper storage or the org is prompted to
export before it ages out) as its own decision, separate from the price point. That is the lever that
actually bounds the cost, the 100-item cap already exists specifically to protect the fairness of the
feature, not to cap cost.

Sources: Cloudflare, R2 pricing; Cloudflare, Stream pricing; AWS, S3 pricing; AWS, CloudFront
pay-as-you-go pricing; AWS, MediaConvert pricing.

**Retention window, RESOLVED 2026-08-24: 12 months.** Full-resolution attendee media stays online for
12 months from upload, then archives (exact archive mechanism, delete vs cold storage vs export
prompt, is an implementation detail for Deepak, not a pricing input). Matches a full academic year, a
member can look back across the whole year's events. This is the assumption already used for both
scenarios above, the heavy-usage ceiling of roughly $24.60/month is what a sustained heavy-usage org
actually costs under this window, not an unbounded number.

**Tail handling, RESOLVED 2026-08-24: price for realistic usage, not the extreme case, with a manual
safety valve.** The heavy-usage scenario above (8 events/month, 150 attendees, sustained every month)
is a top-1%-of-orgs extreme, not a case worth pricing the entire tier against. Rather than charging
every typical org more to defend against a rare one, or building automated usage-based overage
billing (real added scope: metering, an overage flow, a warning notification, none of it justified
before there is even one org near this usage level), the org's usage should simply surface as a flag
once it crosses a defined threshold, so the decision is a manual conversation with that org, not an
automatic charge. Threshold not yet set, natural follow-up once usage data exists.

**A more realistic upper bound, added 2026-08-24, to price against instead of the extreme case.** A
genuinely very active but plausible club: 6 org-paid events a month, 100 attendees per event, 15
items per attendee per event average. That is 9,000 items a month, and under the same 12-month
retention window, storage plus operations plus transcode comes to roughly $6.15 a month per org. This
is the number the price should carry real margin over, the $24.60 extreme is what the safety valve
exists to catch, not what the sticker price is sized against.

## Governance flag

`PROJECT_STRATEGY.md` is merger-only (Aakash), proposals only from others, per `OWNERS.md`. But
`CLAUDE.md` section 6's proposal table does not define a `proposed-project-strategy.md` channel, the
way it does for decisions, hotsheet, risks, the project index, and tasks. This is a real gap, not
something to route around by inventing an unrecognized filename the merger skill may not parse.
Flagging for Aakash to either add that channel or say how he wants commercial-structure content
proposed. Until then, this content stays here as a working draft rather than being pushed toward
`shared/`.
