# Wepop - Complete Project Reference (WEP001)

> A full, in-depth walkthrough of the product: what it is, every module, how the flows work, the
> phase plan, the data-model and build notes, and the governing decisions, risks, and open items.
>
> **Grounding.** Everything here is drawn from the project record. `shared/DECISIONS.md` (DEC-001 to
> DEC-044) is the source of truth and wins wherever anything else disagrees. This document was
> generated 2026-08-31, immediately after DEC-034 to DEC-044 landed. Where the older
> `wepop-product-overview.md` and `wepop-compliance-register.md` (both dated 2026-08-26) still describe
> the pre-DEC-034 state, this reference reflects the current decisions and those source files are
> flagged for a `spec-sync` / `compliance-watch` refresh. No em-dashes; governance values are
> ALLOW / BLOCK / ESCALATE.
>
> **How to read it.** Section 1 is the product in one page. Section 2 is the object model. Section 3
> is the phase plan. Section 4 is the module-by-module deep dive (the bulk of the document). Sections
> 5 to 11 are the cross-cutting layers: principles, data model, legal, risks, open items, governance,
> and a one-line index of every decision.

---

## 1. What Wepop is

Wepop is an **invite-first, location-based events and meetup app**: a tool for getting people together
in the real world around shared activities. It is deliberately a meetup app, **not a dating app**, and
much of the product design exists to hold that line (the anti-stalking visibility model, the
attendee-list gating, the no-paid-boost rule). The focus launch markets are **Korea and the US**.

The product is being **rebuilt on top of an existing Wepop codebase** rather than from scratch:
salvage and extend with AI-assisted build (DEC-008). This shapes the technical decisions toward reuse
(for example, recurring events are modeled as linked copies rather than a new multi-date object, so
every existing per-event screen keeps working).

Two structural ideas run through everything:

- **Invite-first.** New users arrive through an invitation to a specific event or host, or wait on a
  waitlist that auto-promotes. This is both a growth model and a genuine safety mitigation (it is cited
  as a real structural protection in the age-gate reasoning).
- **Real-world-first.** The app pushes people toward attending, hosting, and remembering real events
  (moments, ratings, check-in, cohorts) rather than browsing people. Discovery is about activities and
  who you already know, not a directory of strangers.

Current status (2026-08-31): **Phase 1 design deepening, build not yet started.** RAG is green with a
watch. There is no hard build blocker, but three launch blockers are open on the HOTSHEET: moderation
capability, Korea 위치정보법 registration for the geofenced check-in mode, and a CSAM
preserve-and-report runbook. The team is Aakash (PM, merger, financials owner), Elvis (client and
designer), and Deepak (tech lead and developer).

---

## 2. Core objects

Everything in the app hangs off five objects.

- **Event** - a concrete activity at a place and time. Carries details, a Discussion board, media, and
  chat. An Event can be standalone, one occurrence of a recurring group (DEC-021), or a member of one
  or more Event Series (DEC-022). Events have a lifecycle (planning, live, completed, cancelled,
  deleted) and, once completed, become largely immutable to protect their rating record (DEC-043).
- **Idea** - something a user wants to do but is not yet hosting. Others rally around it (an Interested
  tap, Discussion, time/place polls) and can spin a real Event out of it. Ideas have **no fixed date**
  and behave like a subreddit for a topic: a hub that lives beyond its creator, with its own lifecycle
  (DEC-040). No media upload on Ideas (photos live in the Discussion).
- **Event Series** - a host-created thematic **hub page** (cover, title, description, tags) that is not
  itself joinable but can be liked, shared, and discussed, with events attached to it over time.
  Closer to an Idea than to a recurring event, but with a **locked add-permission** (only the host or
  approved co-hosts attach events). Build target phase 1.5 (DEC-022).
- **User profile** - the person. Onboarding data (birthdate, city/neighborhood, gender, languages,
  personality and interest tags, university), plus followers, created events and ideas, saved items,
  and moments. Accounts are public in phase 1 (private accounts deferred).
- **Business / Organization profile** - a multi-member account. **University clubs first**,
  promotional accounts later. Ownership transfers cleanly as officers turn over (DEC-024), and
  enforcement now propagates from a user to the orgs they operate (DEC-044).

---

## 3. Phase plan

Phase boundaries are set by DEC-009 (superseded for chat/calendar by DEC-013), DEC-024, and DEC-025,
and refined by the later decisions. Per-feature status lives in `wepop-scope-matrix.md`.

### Phase 1 (the build in front of the team)

Core objects; invite-first onboarding and waitlist auto-promote; auth (social login plus always-required
phone, Korea PASS branch); self-declared age with a country cascade; required neighborhood-level home
location and the map picker; Events and Ideas (with the Ideas lifecycle); event schedule; ratings and
post-event feedback with QR check-in (now a badge, not a gate); Moments with video; live stories; DMs
and group chat (text only); the two lightweight calendar pieces; community cohorts and the
recommendation algorithm; Free Now; icebreakers; tips/guides; general user blocking; change
notifications; host accountability; localization (Korean); and A/B testing. **Payment provisions are
built but gated off.**

### Phase 1.5 (end of phase 1, "go-live" wave)

Payments go live (ticketing with a platform fee); the individual premium tier (held pending phase-1
usage data); the full in-app calendar view; recurring events; Event Series; and co-hosts.

### Later phases

Sunday Deck (swipe discovery, needs event density); apply-to-join with host questions; annual Wrapped;
P1.2 memories resurfacing; private accounts; learned per-user recommendation weights; look-alike host
affinity; and the dedicated payments / gamification / ads / marketplace / web-version threads.

---

## 4. Modules in depth

Each module below is: **what it is**, the **user flow**, the **rules that govern it**, the
**data-model and build notes** flagged for Deepak, the **decisions** it rests on, and any **open
items**.

### 4.1 Waitlist and invite onboarding

**What it is.** The front door. Non-invited users land on a waitlist; invited users see who invited
them and to what, then join or log in.

**Flow.** Waitlist collects email, phone, location, and university. When capacity or timing allows,
users are **auto-promoted** off the waitlist with a **claim window** (a bounded time to accept before
the slot recycles). An invited user's onboarding screen names the inviter and the event/host, which
sets context before signup.

**Rules.** Invite-first is a deliberate growth and safety choice, not just a launch gate. Auto-promote
with a claim window is phase-1 scope (DEC-024).

**Build notes.** Waitlist promotion needs a claim-window timer and a recycle path. The inviter/event
attribution needs to survive into the new account for the first-session context.

**Decisions.** DEC-024. **Open.** None material.

### 4.2 Registration, auth, and verification

**What it is.** Account creation and identity verification.

**Flow.** Social login via **Kakao, Apple, or Google** can create or sign in an account, but a **phone
number is always required**. If the provider supplies a verified phone (Kakao only, business-reviewed
scope, Korea in practice) that satisfies verification; otherwise the app runs its own **phone OTP**.
For **Korean carrier numbers**, verification routes through **PASS** (the Korean carrier real-name
authentication, government-linked, which returns success/fail plus identity and age); non-Korean
numbers stay on the standard OTP path (DEC-026). **Password is deferred** to a later phase; the
recovery channel is an **email magic-link** (email is collected from every account, so this covers
100 percent of accounts); **biometrics** handle day-to-day re-login.

**Rules.** Every account ends up with a verified phone. A password is treated as a weaker fallback than
phone OTP, and optional post-signup passwords have near-zero adoption, so building one now would not
help the user who needs it; the revisit trigger is real support data showing a recovery gap or entering
a market where SMS is genuinely blocked.

**Build notes.** One global auth flow with two branches (Korea PASS, everyone else OTP) plus the Kakao
verified-phone skip. PASS brings CI/DI sensitive-identity data and PIPA/designated-agency handling
(compliance register). A freelancer may be engaged for the PASS integration; Deepak to research PASS
before build.

**Decisions.** DEC-011 (supersedes DEC-004), DEC-026. **Open.** Confirm PASS adoption with Elvis before
build; PASS data-handling obligations pending counsel.

### 4.3 Age gate and country determination

**What it is.** The legal-eligibility check at signup.

**Flow.** Age is a **self-declared birthdate**, typed once and **locked at signup** (correctable only
via support, with a ToS ban if falsified). No ID verification in phase 1, except that Korean users
verified through PASS get a **verified age** for that market (DEC-026). **Country** is set **once at
registration** via a fallback cascade (app-store region first, then device location only if already
granted, then phone-number country code) and **never re-checked as the user travels**. Per-country
legal-age thresholds live in a **config table**, not hardcoded in a screen (US 18, Korea 19, Germany 16
are the reference points).

**Rules.** No forced GPS prompt at registration (the most-declined onboarding step). Invite-first is
counted as a real structural mitigation. The config table means a legal answer from counsel becomes a
config change, not a redesign.

**Build notes.** Store-region APIs (StoreKit, Play Billing) and signal-conflict handling (store region
vs phone code) are flagged to Deepak and to the legal consult. The country field for the age gate is
kept **deliberately separate** from the city/home location and from the Explore country field (three
different purposes, do not conflate in the data model).

**Decisions.** DEC-012 (supersedes DEC-002, **provisional pending legal counsel**, TASK-013). **Open.**
The exact logic (passive vs active location, travel jurisdiction, under-14 guardian consent) is pending
DLG Law; risk R1.

### 4.4 Location: home location and the map picker

**What it is.** Two distinct location concepts: the **map picker** used to place things, and the user's
**home location** used to anchor discovery.

**The map picker (DEC-003).** A Google-Maps-style model: **search plus tap a named place**, showing the
place name, with zoom, a free-text address field, and an optional per-event note for the exact unit.
This is not the Uber-style fixed center-pin. One picker pattern is reused everywhere a place is chosen
(events, event-schedule stops, and now home location).

**Home location (DEC-016, refined by DEC-031).** Required at onboarding. Originally city-level typed or
selected; DEC-031 revised it to **reuse the map picker at neighborhood-scale granularity** (roughly
dong-level in Korea, a neighborhood/postal-code-sized area elsewhere). The confirmed point is
**reverse-geocoded to a canonical neighborhood ID, that area's centroid, and its country code**, and
the **precise tapped coordinate is discarded and never persisted** (consistent with the anti-stalking
model). A fallback chain (neighborhood, then postal code, then city) covers markets without a clean
neighborhood tier.

**Mutability (DEC-031).** After onboarding, home location can be changed **only by granting device
location permission and selecting current location** (a live GPS read through the same
reverse-geocode-and-discard flow). The unrestricted picker does not reopen for a later edit, and there
is **deliberately no fallback** for a user who never grants location permission. This is anti-gaming
design: it stops a free user from defeating the Explore country gate (DEC-032) by dropping a pin
anywhere.

**Runtime anchor (DEC-031).** The stored home location is only the **default anchor** for the home feed
and Explore. When device GPS is granted, **live current location is preferred**, pulled on-demand per
screen load (never continuous background tracking, never persisted), with a manual refresh on the home
feed.

**Build notes.** Every home-feed or Explore retrieval call needs request-time anchor resolution (live
GPS if granted, else stored default) plus a fallback so a feed load never hard-fails on a location
error. Device GPS is always optional and requested contextually with a plain explanation, never at
registration.

**Decisions.** DEC-003, DEC-016, DEC-031. **Open.** Whether Explore needs its own manual refresh
distinct from the home feed's; whether a GPS-granted user can opt back into the coarser stored default.

### 4.5 Profile and tags

**What it is.** The user's identity and interest surface.

**Flow.** Onboarding captures birthdate, city/neighborhood, gender, languages, **personality and
interest tags**, and university affiliation. The personality field is an **extensible, searchable tag
list** (MBTI values are included as tags), not an MBTI selector: show the top 10-20 common tags, make
them searchable, and let users add their own (DEC-005). A profile description field and profile screens
(user and organization) are still owed from Elvis (todos).

**Rules.** A growing tag database is richer for matching than a fixed type. Tags feed the recommendation
tag/keyword signal.

**Decisions.** DEC-005. Interacts with the recommendation algorithm (DEC-020).

### 4.6 Events

**What it is.** The central object: a concrete activity at a place and time.

**Flow.** A host creates an event, placing it with the map picker (DEC-003), adding details, and
optionally building a **structured schedule/itinerary** of ordered stops (each stop reuses the map
picker; visibility inherits the event). An event can be created **directly from an Idea** without
re-prompting. Attendees discover it, see gated pre-join info (see 4.20), join, attend, check in, rate,
and post moments. A save-as-draft screen is still to be added (todos).

**Event schedule (DEC-041, refining DEC-025).** The Event model **supports differing start and end
dates** (multi-day), exposed as an Airbnb-style calendar picker where a single day and a range are the
same interaction. A host may build a schedule **before the date/time is resolved** (a `planning` status
under poll); stops carry their times and bind to the date on confirmation. For recurring events the
itinerary is copied at generation with dates shifted per occurrence and participates in the
"this / this and following" propagation (DEC-021).

**Completion immutability (DEC-043).** Once an event **completes**, the host **cannot delete or edit**
it, and cannot leave it at will. After completion, deletion is **admin-only** and arises from exactly
two sources: moderation removal or a PIPA legal-erasure request. A host who wants to be unlinked
requests **detachment**, which is **reviewed by an admin** rather than taking effect immediately.
Crucially, **ratings persist** through both detachment and deletion. All of this is enforced
server-side, not by hiding the button. This closes a laundering hole where a host could delete a
completed event to erase a bad rating.

**Build notes.** `scheduled_end` ships on the Event row; store an explicit date on every stop (even
single-day) and derive the display, because a live event can be extended across midnight. A host's
rating aggregate must **not** be computed by joining live event rows (deletion would silently destroy
ratings); ratings carry a **denormalized host reference** and survive their source event, reusing the
Moment tombstone pattern. Enforce the completion boundary server-side for deletion, detachment, and
edits.

**Decisions.** DEC-003, DEC-025, DEC-041, DEC-043. **Open.** The calendar-picker design has not landed;
revisit the schedule against it.

### 4.7 Recurring events (phase 1.5)

**What it is.** A repeating event (a semester-long club meetup).

**Flow.** Modeled as **separate, fully linked Event instances** sharing a `recurring_group_id`, not one
multi-date object. Edit, delete, and join/interest all use a uniform Google-Calendar-style **"this
occurrence / this and following"** choice. Occurrences are **batch-generated** from a host-set pattern
plus an end date or count (re-run to extend). Joining "this and all future" is a **snapshot** of the
occurrences that exist at that moment, not a standing subscription; members are notified and opt in when
a group is extended. Both individual and org hosts can create them.

**Rules.** Separate instances keep every per-event decision (ratings, check-in, media caps, pre-join
gating, org track record) working unchanged, which fits the salvage approach (DEC-008). "Series pages"
fall out as an instance-embedded list of the other occurrences, with no master hub page (that is what
Event Series is for).

**Build notes.** Nullable `recurring_group_id` plus occurrence ordering; a batch-generation tool; an
extend-notification hook; one shared "this/following" UI pattern across delete/edit/join. Recurring-group
membership is distinct from Event Series membership (separate keys).

**Decisions.** DEC-021. Build target phase 1.5.

### 4.8 Event Series and co-hosts (phase 1.5)

**What it is.** A thematic hub grouping events that share a theme rather than a repeating template (a
touring act, a multi-venue weekend).

**Flow.** A host creates a **Series hub page** (cover, title, description, tags) that is **not itself
joinable** but can be liked, shared, and discussed. The host attaches events over time. Curation is
**self-only** (only the host or approved co-hosts attach their own events). An event may belong to
**multiple series**. A private event attached to a public series follows most-restrictive-wins.
**Co-hosts** are pulled forward to ship alongside Series, since "who can add events to a series" needs a
co-host permission.

**Build notes.** Series membership is a **many-to-many join table**, distinct from `recurring_group_id`.
Per-viewer render-time visibility checks; distinct UI badges for recurring-group vs series membership.
Detaching (assumed to only remove the link) to be confirmed.

**Decisions.** DEC-022 (revises DEC-024 on co-host timing). Build target phase 1.5.

### 4.9 Ideas and their lifecycle

**What it is.** A no-date hub for something a user wants to do, closer to a subreddit than a post.

**Flow.** A user posts an Idea (summary, details, a Discussion board, and time/location polls). Others
tap **Interested**, comment, and vote on polls, and anyone inspired can **spin a real Event out of it**.
Spawning an event never closes the Idea (an Idea is a hub for multiple inspired events). No media upload
on Ideas.

**Lifecycle (DEC-040, superseding DEC-009's "do not expose" provision).** Five parts:

1. The old "close to new joiners" toggle is confirmed as a **membership freeze, not a shutdown**, is
   **reversible**, is renamed **"Pause new joins"** (outsider-facing "This idea isn't taking new people
   right now"), and now **ships visible and usable in phase 1**. The existing group keeps full access;
   only new joins stop.
2. An Idea with **no activity for 90 days** is **auto-archived** by the system (visible, read-only,
   with links and spawned-event backlinks surviving). Activity means an Interested tap, a Discussion
   comment, or a spawned event; views do not count.
3. A creator may **delete** an Idea outright **only while no one else has interacted** with it
   (created-by-mistake case; friction-free, no review).
4. Once interaction exists the Idea cannot be deleted, but the creator may **detach** themselves; a
   detached Idea becomes **system-owned** (admin-actionable only) in phase 1.
5. An Idea removed by moderation leaves its inspired events standing (where those events are fine), with
   the backlink replaced by an **"Idea removed" tombstone**.

**Rules.** "Pause" beats "Close"/"Lock" because reversibility is the semantic that distinguishes it from
archive. 90 days (vs events' 60) because Ideas are slower-burning by design. Views are excluded from the
interaction test so a passive viewer cannot block a creator from deleting a mistyped draft.

**Build notes.** One tombstone mechanism serves both the deleted-event anchor on Moments and the
deleted-idea backlink. Ideas need `archived_at` plus a last-activity timestamp and an inert scheduled
sweep. The interaction test is one shared predicate used by both delete-eligibility and archive-activity.
A system-owned Idea needs a real ownerless state.

**Decisions.** DEC-040 (supersedes DEC-009's idea provision). Distinguished from Event Series (DEC-022):
both are hubs, but a Series has a locked add-permission while an Idea is open to anyone inspired.
**Open.** Un-archiving; whether a detached Idea can regain an owner; whether archived Ideas surface in
Explore; whether interested users are notified on pause/archive.

### 4.10 Discovery: cohorts, recommendation, group dynamics

This is the engine behind the home feed and Explore. It is a **two-stage pipeline: cheap retrieval,
then weighted ranking** (DEC-020), rule-based at launch with no learned model (there is no engagement
history yet), but architected so a learned ranker can slot into the ranking stage later.

**Cohorts (DEC-019, simplified by DEC-030).** Originally `(city, age/life-stage bucket)`; DEC-030
**simplified the cohort key to a single binary value, university-affiliated or not**, and **removed
location from the cohort formula entirely**. University affiliation is verified by any of three signals
(self-declared student status, a school email domain, or membership in a university-flagged Org). At
launch the cohort is a **hard retrieval filter** (a candidate outside the cohort is excluded before
ranking), relaxing via a **manual density call** that DEC-030 turned from a per-city PM decision into a
**single global call**. Content from **users you follow is exempt** from the cohort filter and is pulled
in via social proximity instead (so a connection surfaces out-of-cohort content rather than hiding it).

**Recommendation ranking (DEC-020).** A normalized **weighted sum** over launch-available signals:
tag/keyword overlap, cohort, recency, geo distance, popularity, social proximity, a deliberate
**new-host fairness boost** (counters a rich-get-richer loop), and group-composition fit. Keyword
extraction from titles/descriptions and an evolving per-user interest profile feed the tag signal, plus
a **hidden internal keyword layer** (admin-visible) across ideas/events/moments/users. **Interaction
logging ships day one.** One global weight formula at launch; learned per-user weights are a later phase.

**Explore (DEC-020).** Splits into an **unranked, viewport-bounded map view** and a **fully-ranked list
view**, with filters and search scoped to a location.

**Group dynamics (DEC-023, amended by DEC-036).** "Who else is attending" feeds the recommender. The
**avoid signal is now block-only** (DEC-036): the original soft, inferred half (down-weight people you
rate low) is **dropped**, because the thumbs-down mechanism it depended on is being removed, and running
it on absence-of-a-positive-signal was explicitly rejected as noise. In its place a **positive affinity
signal**: events attended by people you tapped the positive "또 만나고 싶어요" (want to meet again) tap on
are boosted, alongside social proximity. Look-alike host affinity stays parked (needs scale). Group
personality-mix compatibility is a ranking signal only, no host-facing surface.

**General user blocking (DEC-037), the safety prerequisite.** Confirmed **phase-1**, earliest build
wave. A block is **bidirectional and total**: the blocked user's events, ideas, moments, comments, and
profile are mutually invisible across every surface (home feed, Explore, comment threads). The **scope
is stated to the user at the moment they block**. Block state is checked at retrieval time on every
content-bearing surface (a hard exclusion here, while the avoid signal treats block as a heavy ranking
penalty; two consumers of the same state).

**Build notes.** Retrieval-before-ranking with a shared scoring function across surfaces; a logging
pipeline; a low-history indicator; a featured flag (for Sunday Deck later); keyword-extraction and
internal-keyword storage with an admin view; a live viewport query for the map. No per-user-pair negative
history is stored; block state and positive-tap history are the only per-pair reads at ranking time.

**Decisions.** DEC-019, DEC-020, DEC-023, DEC-030, DEC-036, DEC-037. **Open.** The cohort softening
trigger itself (the global density call's threshold); behavioral-inference disclosure in the privacy
policy.

### 4.11 Ratings, post-event feedback, and QR check-in

**What it is.** The post-event loop that produces host reputation, the recommendation signal, and
moments.

**Flow (DEC-014, amended by DEC-034).** After an event, attendees see a **three-step flow, every field
optional and every step skippable**: (1) rate the event 0-5 stars plus optional anonymous text with an
everyone/host-only visibility toggle (default everyone); (2) rate the host 0-5 plus a comment, and give
other attendees a **single positive-only tap** (the old thumbs up/down is gone); (3) add moments.

**The 2026-08-34 amendment (DEC-034), which changed this significantly:**

- **Peer feedback is positive-only.** Attendee thumbs up/down is replaced by one positive tap; **no
  negative peer record is created anywhere**, and no negative peer table exists.
- **No bulk follow.** The "follow all" affordance is removed; individual follow taps only.
- **Check-in is decoupled.** QR check-in is **no longer a gate** on feedback or moment authorship. Any
  attendee of a completed event may rate and post moments regardless of check-in. Check-in instead
  grants a **visible verification badge** and an **invisible scoring weight**: verified feedback is
  weighted **1.0**, unverified **0.4** (joined and completed but never checked in, or self-attested and
  unresolved at a 7-day auto-close).
- **Display gate.** A host or org public star average does not display until at least **3 verified
  ratings** exist (below that, only event count and rating count show).
- **Smoothing.** The internal recommendation signal reads the weighted rows through Bayesian smoothing
  toward the global mean: `R = (C*m + sum(w_i*r_i)) / (C + sum(w_i))` with `C = 5`.

**Rules.** Decoupling removes check-in as a single point of failure for the whole evergreen content
layer (a host who forgets to run check-in costs attendees a badge, not their memories). The 0.4 weight
keeps a cluster of no-shows from moving a host's score against people who actually attended. The
smoothing constant protects the new-host fairness boost from a single early low rating.

**Build notes.** Store `method` and `verified_at` on the feedback row; compute the weight at read time
from a config table (retuning is a config change, not a backfill). A verification badge on anonymous
feedback discloses attendance, not identity, so it coexists with anonymity. The weights, the display
threshold, and `C` are starting points, not data-backed; revisit with real usage.

**Check-in itself.** Remains phase-1 scope. The **printed-poster mode** constrains scans to a location
radius, which raises a Korea 위치정보법 registration question (see 4.19 and risk R5); a clean fallback
exists (drop the radius, rely on the time window plus a live-display QR that regenerates every 60
seconds).

**Decisions.** DEC-014, DEC-034. **Open.** Whether a 0 star is a real value or means unrated.

### 4.12 Moments and media

**What it is.** The evergreen, memory-keeping content layer: one post-event post per user per event.

**Flow (DEC-015).** A **moment is one post per user per event** (never a paid lever). Moments visible
beyond the owner support **reactions, comments, and share** (all phase 1). A moment **inherits the
visibility of its event** by default; the owner can override an individual moment to private; the
**most-restrictive setting always wins** (a general principle applied across moments and series).
Private accounts are deferred.

**Media rules.** Video is phase 1 at **720p H.264, roughly 3 Mbps**, with tier-based caps. Base caps
(DEC-015, DEC-018): **10 media items free / 20 individual-paid / 50 at org-paid events**
(most-generous-wins), video **15s free / 30s paid**. Server-side transcode of every upload is required;
the per-clip 50MB ceiling is an abuse/corruption guard, and client-side compression before upload is
mandatory.

**Event cover media (DEC-038), a separate surface.** Distinct from moment media: **up to 5 items total**
(photos/videos any mix), video **15s free / 30s paid** for either account type. A cover is a cover, not
a gallery; volume belongs in the Moment composer, which keeps the single-uploader, single-moderation-queue
architecture intact.

**Media retention (DEC-039), a tiered paid differentiator active at launch.** Nothing is ever deleted.
Past a **6-month boundary**, **free-tier media moves to cheaper storage** and the user sees a thumbnail
plus a download of the original; **paid accounts keep full-resolution access indefinitely**. Two advance
warnings (T-14 and T-3 days), each with a bulk-download affordance; silent degradation is not acceptable.
Thumbnails persist indefinitely (~400px). The preservation path is device download, explicitly not
copy-to-moment. `storage_tier` and `expires_at` ship on the media row with a scheduled job. Retrospective
surfaces (annual Wrapped, memories resurfacing) **restore from cold storage** at full quality.

**Build notes.** Public moment comments are a moderation surface. Cold-storage retrieval has real latency
and needs a designed loading state. Infra recommendation (DEC-018): Cloudflare R2 over S3+CloudFront,
self-hosted 720p transcode over a managed stream service.

**Decisions.** DEC-014 (the feedback flow that reaches moments), DEC-015, DEC-018, DEC-038, DEC-039.
**Open.** A total-video-duration cap per moment (recommended 150s free / 300s paid, not confirmed);
org-paid moment video length (DEC-018 never set it); DEC-039's three implementation refinements
(restore-from-cold Wrapped path, a general retrospective-surface capability, a 1080px mid-tier for free
full-screen); per-uploader vs per-room retention scope.

### 4.13 Live stories (phase 1)

**What it is.** A separate ephemeral 24-hour content type, distinct from moments.

**Flow.** RSVP (not check-in) to post; the poster chooses the audience from **four tiers, defaulting to
most restrictive**. Content disappears after 24 hours.

**Rules.** Kept separate from moments because moments are evergreen memories and live stories are
in-the-moment and ephemeral.

**Decisions.** DEC-025. **Open.** Whether live stories count against the org 50-item media cap (likely a
separate allowance).

### 4.14 Free Now (phase 1, highest safety flag)

**What it is.** Real-time availability plus **location-pinned rooms** for spontaneous meetups. The
highest-exposure surface in the product.

**Flow.** A user signals they are free now; location-tied rooms let nearby available people converge.
Location is **rounded** (never precise), the view is **aggregate-first** with identities revealed only
on **reciprocal join**, and **room creation is gated on account standing**. Moderation is a required
baseline, not optional.

**Build notes.** Rounded location with a concrete rounding method (open); reciprocal-join enforced
server-side; room-creation standing threshold, duration cap, room auto-archival, and org-created rooms
all open details to confirm before build.

**Decisions.** DEC-025. **Open.** Account-standing threshold, duration cap, archival, org rooms; the
location-rounding method. This surface is a top driver of the moderation launch blocker.

### 4.15 Chat and calendar

**Chat (DEC-013).** Event chat, group chat, **DMs, and user-created group chats** are **all phase 1**,
**text only** (no audio or video chat). This was the largest single scope addition of the conflict-review
set, because live messaging is real infrastructure (delivery, presence, push) and adds a **third
moderation surface**. The event chat is announcement-only by default until 24 hours before the event,
which is the mode system change-notices ride in (see 4.16).

**Calendar (DEC-013).** Split. **Phase 1** gets read-only **device busy-time ingestion** (start/end
times only, everything else discarded) plus a manual per-event **"add to my calendar"** write. The full
in-app calendar view (month/list) is **phase 1.5**. Calendar-read permission is requested contextually,
not at onboarding, and the app extracts only times (data minimization).

**Decisions.** DEC-013 (supersedes DEC-009 for chat/calendar).

### 4.16 Notifications and change notifications

**What it is.** How the app tells people something happened.

**Base notifications.** Invites, follows, event/idea activity.

**Change notifications (DEC-042), a general rule.** **All changes to an event or idea generate a
notification.** Event changes additionally **post into the event's chat**. Notifications **batch per
save** (one save, one notification, however many fields changed). The audience for an event change is
**three groups**: joined attendees, waitlisted users, and users with a pending apply-to-join
application. Followers and passive viewers are not notified. Idea changes notify their interested users.
Completed events are not editable, so no change notifications arise after completion (but admin removal
of a completed event still notifies).

**Rules.** The failure mode is concrete: someone standing at the old meeting point because a silent
change moved it. This satisfies the invariant that consequential actions are never silent, and rides on
existing machinery (poll-resolution announcements, the announcement-only chat mode). Per-save batching
answers the launch-level risk that notification volume drives users to disable push.

**Build notes.** Batch at the save boundary, not per field; the audience query unions three membership
sets; a completed event must reject detail edits server-side.

**Decisions.** DEC-042. **Open.** Whether pausing/archiving an Idea counts as a change for notification
purposes.

### 4.17 Icebreakers and tips/guides (phase 1)

**Icebreakers (DEC-025).** A host-authored, **up-to-3-question, read-only** question game, opt-in. Was
check-in gated in the original design; note that check-in is no longer a hard gate elsewhere (DEC-034),
so this should be revisited for consistency. Tag-matching and a scavenger game are later.

**Tips/guides (DEC-025).** A contextual **info-icon** plus a static guide, **targeted by
situation/status, not personality**. Copy is written later (a ux-copy pass).

**Decisions.** DEC-025.

### 4.18 Moderation and safety

**What it is.** The cross-cutting safety layer, and the product's main launch blocker.

**Surfaces needing day-one moderation.** Anonymous public-by-default host-rating comments (DEC-014),
public moment comments (DEC-015), DM and user-created group chat (DEC-013), Free Now location-tied rooms
(DEC-025), and **Discussion on every event and idea**. Eleven reportable target types span these five
surfaces (user profile, org profile, event, idea, moment, individual photo/video, moment comment,
Discussion comment, chat message, chat room, plus general app feedback).

**The 2026-08-31 reframe (HOTSHEET Blocking).** The blocker splits into two halves:

- **Response-time SLAs are deferred** by Elvis until there are employees to meet them (the handoff
  spec's urgent-under-4h / 24h-weekday / 48h-weekend / 72h-appeal numbers are recorded for reuse, not
  committed). Independent appeal review is structurally impossible with one reviewer.
- **Moderation capability cannot be deferred.** UGC ships at launch, so without a place for reports to
  land and someone able to act, there is no removal path at all. Three pre-launch artifacts, none of
  which exist yet and none of which are SLA commitments: a **basic internal admin queue**, **urgent-report
  push alerts** to whoever is on call, and a **one-page written moderation guideline**.

**Load reducers already designed in.** One **generic report model** (`report(target_type, target_id,
reason_code, reporter_id, note)`) feeding a single queue; **idempotent** repeat reports; **auto-hide on
a double condition** (5+ distinct reporters AND at least 10 percent of distinct viewers, so a small
group cannot coordinate a takedown); and a **brigade_suspected** flag when reporters cluster.

**Day-one metrics** (reports per 1,000 moments, median time-to-decision, backlog depth, appeal overturn
rate) become the **hiring trigger** rather than compliance measures.

**Legal duties that do not wait for hiring.** Korea's 정보통신망법 imposes illegal-content takedown and
the 임시조치 (temporary-measure) blinding procedure, and 불법촬영물 obligations under 전기통신사업법 apply
to the service. A **CSAM preserve-and-report runbook** is required before launch: if CSAM appears it
must **not be deleted** (that destroys evidence); the required handling is preserve, restrict access,
report. The runbook is a written one-page procedure any reviewer can follow unaided.

**Decisions / tracking.** DEC-013, DEC-014, DEC-015, DEC-025; TASK-034 (stand up moderation), TASK-039
(CSAM runbook), plus risk **R4** (single-reviewer moderation). This is the top launch blocker.

### 4.19 Host accountability and enforcement

**What it is.** The model that keeps ratings and bans meaningful and closes gaming loopholes (DEC-044,
building on DEC-043).

**Reputation vs enforcement split.** **Reputation** (host ratings, public track record) is personal
data and is **deleted with the account**. **Enforcement** (ban and suspension records) is
fraud-prevention data and **survives account deletion**, retained under a disclosed 부정이용 방지
(abuse-prevention) privacy-policy item. This follows the Danggeun (Korean market) model; their Karrot
Score is explicitly **not** adopted (DEC-014's 0-5 stars stand).

**Re-registration and the ban list.** Re-registration after deletion is allowed, subject to a cooldown
and a **ban-list check at signup**. The ban list stores a **hashed identifier** (phone hash plus device
and environment signals), not a readable roster, with **CI (연계정보)** from the PASS flow as the strong
key for Korean users (a phone number can be swapped, a CI cannot).

**Organizations.** Enforcement **propagates**: suspending an individual suspends the orgs they operate.
Admins can see every org a user operates. Org creation is gated on **standing** (no active suspensions
plus a minimum account age), not on a rating (so a brand-new club officer is not blocked). A suspended
admin may **transfer** their admin role to another member, subject to three qualifications (the target
has standing; was a member before the suspension with a minimum tenure; and the transfer is
admin-reviewed). A suspended individual loses org access entirely. A cap on org accounts per user and
public display of connected profiles were both **rejected** (the latter would fight the anti-stalking
model and create a deanonymization surface).

**Completed-event immutability (DEC-043).** See 4.6: a host cannot delete or edit a completed event;
ratings persist through detachment and deletion.

**Build notes.** The ban list is a hashed lookup at signup, not a stored roster. Suspension propagation
walks the existing org-to-user traceability link. Suspension-triggered admin transfer is a distinct path
from routine ownership transfer. The deletion path must distinguish **account deletion** (ratings
deleted) from **event deletion** (ratings survive).

**Decisions.** DEC-043, DEC-044 (extend DEC-024, DEC-026). **Open.** Re-registration cooldown period;
ban-list retention period; minimum account age and member tenure; whether propagation is automatic or
reviewer-gated; DLG legal review of the retention model.

### 4.20 Anti-stalking pre-join visibility

**What it is.** The rule set that keeps Wepop a meetup app rather than a way to find where a specific
person will be.

**The model (DEC-006).** Before a user joins an event or idea, show only **mutual friends' attendance
plus aggregate signals** (people near your age, area, interests), **not the full attendee list**. Fuller
info unlocks only after joining or marking interested. Only mutuals' profile pictures appear pre-join.

**Gender and photos (DEC-017, then DEC-035).** DEC-017 set gender pre-join to an **aggregate ratio
only** and individual photos to **mutual (bidirectional) follows only** (a one-way follow never
unlocks). DEC-035 then **removed gender from the attendee-facing pre-join view entirely** (even the
aggregate, which is re-identifiable on a small event), while **hosts keep a host-facing aggregate**.
Gender **never** appears on a per-person row in any accept/decline or selection UI (new invariant
I-13), because the same data becomes a discriminatory selection mechanism at the moment of a yes/no on a
specific person. A host with a genuine balance requirement declares it at creation and it is enforced at
join eligibility, so nobody is silently rejected. The DEC-017 **photo** provision stands.

**Build notes.** Follow-state is checked **bidirectionally** server-side. The pre-join aggregate payload
drops gender for attendee-facing requests but keeps it for host-facing ones (a per-audience response
shape, not a stored-data change). Gender stays optional at signup and purpose-limited to host planning
(a PIPA stated-purpose point).

**Decisions.** DEC-006, DEC-017, DEC-035.

### 4.21 Monetization

**Phasing (DEC-010).** Payments (event ticketing with a platform fee, and gated premium features) are
**architected into phase 1 as toggle-able, gated provisions** but **not wired live** until phase 1.5.
Wepop uses Programination's existing Stripe account (but see the Korea caveat below).

**Freemium structure (DEC-018).** Two premium tiers on separate timelines:

- **Individual tier** at **$3.99/month or $36/year** (30s video, 20 media items per moment, own-content
  engagement analytics). Ship timing is **HELD** until phase-1 usage data exists.
- **Organization tier** at **$19.99/month or $199/year** (per-org billing, 7-day trial), **proceeding
  now**, split so per-event operational numbers stay free while aggregate rollups, trends, and export
  are paid.

**The three-bucket gating rule.** Never gate marketplace actions; quota-gate personal expression;
insight-gate analytics. A **paid ranking or discovery boost is explicitly locked out** (it would cut
against the fairness and anti-stalking moat). Retention (not sticker price) is the real cost lever.

**Extensions.** DEC-032 added an **Explore cross-country content-detail gate** as an individual-premium
lift (see 4.22), cleared against the paid-boost lockout as differing in kind. DEC-033 set the
**apply-to-join screening-question quota** at 3 free / 10 individual-paid. DEC-039 turned **media
retention** into a tiered paid differentiator (see 4.12).

**Korea payments caveat (HOTSHEET Needs Attention).** Stripe's actual support for Korea-based merchant
payouts, KRW, and local methods (KakaoPay, Naver Pay, bank transfer/virtual account) is unconfirmed, and
Korean consumers prefer local methods over cards. Since the org tier is live now, evaluating
Korea-specific processors (Toss Payments, NHN KCP, PortOne/Iamport) is not distant work. App-store IAP
(15-30 percent) is also in play.

**Governance.** This is financials-owner (Aakash) territory. The `PROJECT_STRATEGY.md` commercial-structure
rewrite is deferred until a proposal channel for it is defined (a known governance gap, TASK-037).

**Decisions.** DEC-010, DEC-018, DEC-032, DEC-033, DEC-039. **Open.** The commercial-structure channel;
the ticketing/payments build scope (TASK-036); the Korea payment path.

### 4.22 Explore country gate (individual-premium lift)

**What it is.** A monetization gate layered onto Explore (DEC-032).

**Flow.** Explore's map and search stay **fully unrestricted** for everyone (pan and search anywhere).
What is gated is **content detail**: for a **free** user, events in a country other than their
current-location country render as an **aggregate teaser only** (a clustered count, no pin-level or
listing detail); events in the **same** country render in full. **Individual-tier premium lifts the
gate.** The stated use case is browsing another country's events before a trip.

**Rules.** Reuses the "aggregate visible, individual detail gated" pattern from the anti-stalking model
rather than inventing a mechanic. Gating detail (not the map interaction) avoids the map reading as
broken. It compares against **current location**, so a user physically present in another country sees
it in full; the flip side (a traveling free user loses full access to home-country content unless they
disable GPS) is a deliberate, examined consequence. Cleared by the financials owner against the
paid-boost lockout because it never touches ranking within a user's own market.

**Build notes.** Needs a **country field distinct** from the locked legal-compliance country (different
purpose and mutability, must not be conflated). **Server-side enforcement** is the real gate; the client
map is never the authority. Depends on DEC-031's mutability restriction to stop a free user re-picking a
foreign home location to defeat the gate.

**Decisions.** DEC-032 (extends DEC-018; depends on DEC-031; distinct from DEC-012). **Open.** Explore
UI details (teaser markers at country/world zoom; whether the ranked list view gets the same treatment).

### 4.23 Localization and i18n (phase 1)

**What it is.** Korean-language support for the focus market.

**Flow (DEC-027, refined by DEC-029).** Language is a **synced profile field**, not a device-only
setting. Its initial value comes from a first-launch cascade (device language, then app/store region,
then phone number), and a **manual override always wins**. Notifications (push, SMS, email) read this
same field. Scope is split: every **WePop-authored string ships fully bilingual** selected by this
field, while **user-generated content renders as authored** with no translation pipeline at launch
(on-demand UGC translation is deferred).

**Build notes.** String externalization, a Korean locale, and a language switcher are phase-1 scope.
Deepak on the i18n framework; Elvis on Korean copy. Open: the fallback for a WePop string with no Korean
translation at ship (English fallback vs blocking launch on full coverage); whether the field re-reads
device signals after initial set or is captured once like the age value.

**Decisions.** DEC-027, DEC-029.

### 4.24 A/B testing and experimentation (phase 1 candidate)

**What it is.** An experimentation capability built early rather than retrofitted (DEC-028).

**Flow.** Assign users to buckets (A vs B), ship a change to one group, and measure the effect, applied
to design, usability, and algorithm changes. It complements the day-one interaction logging from the
recommendation work.

**Status.** Phase-1 candidate, exact phase set by build difficulty (Deepak); tracked as proposed on the
scope matrix until confirmed.

**Decisions.** DEC-028.

---

## 5. Cross-cutting principles and invariants

These hold across modules and are the quickest way to sanity-check any new design.

- **Meetup, not dating.** Pre-join, show only mutuals plus aggregates, never the full attendee list
  (DEC-006). Gender is never shown to attendees pre-join and never on a per-person selection row
  (DEC-035, invariant I-13).
- **Most-restrictive-visibility-wins.** Applied across moments and series (DEC-015).
- **Consequential actions are never silent.** Poll resolutions and event/idea changes always notify
  (DEC-042).
- **No paid ranking or discovery boost.** Monetization never buys visibility (DEC-018).
- **No in-app AI image or video generation.** The only AI the user touches is text prompt-to-create for
  an event or idea (DEC-007).
- **Accountability cannot be laundered.** Ratings survive event deletion and host detachment (DEC-043);
  enforcement survives account deletion (DEC-044).
- **Anti-gaming location.** The precise tapped point is never persisted; post-onboarding home-location
  edits are current-location-only (DEC-031), which also protects the Explore gate (DEC-032).
- **Server-side is the authority.** Follow-state checks, block exclusion, the Explore gate, and
  completed-event immutability are all enforced server-side, never by hiding a control.
- **Config over hardcode.** Per-country age thresholds and feedback weights live in config tables so a
  policy change is a config edit, not a migration.
- **Invariant registry.** The handoff spec cites invariants I-6 to I-20; adopting a maintained registry
  into `CLAUDE.md` (and re-scoping I-12 so it does not forbid host ratings) is tracked as TASK-041.

---

## 6. Data-model notes (the entities and flags Deepak carries)

Not a schema, but the recurring model decisions that shape the build:

- **Event** carries `scheduled_end` (multi-day), a status machine (planning/live/completed/cancelled/
  deleted) with actor-split deletion, and a nullable `recurring_group_id`. Per-stop schedule rows should
  store an explicit date.
- **Recurring group** is separate linked Event instances sharing `recurring_group_id`; **Event Series**
  is a separate many-to-many join table. The two memberships never share a key.
- **Ratings** carry a denormalized host reference (`event_name`, `event_date`, `org_name` copied at
  creation) so they survive their source event; the host aggregate is never a live-row join. Feedback
  rows carry `method` and `verified_at`; weights are read-time config.
- **Media** rows carry `storage_tier` and `expires_at`; a scheduled job demotes free-tier media at the
  6-month boundary; thumbnails persist; a restore-from-cold path serves retrospective surfaces.
- **Cohort** is a computed value (university-affiliated or not), not a stored entity; it is a retrieval
  filter and a ranking weight, computed per user from profile signals.
- **Home location** is a canonical neighborhood ID plus centroid plus country code; the precise point is
  discarded. The **age-gate country**, the **home-location country**, and the **Explore current-country**
  are three distinct fields.
- **Block** state and **positive-tap** history are the only per-user-pair reads at ranking time; no
  negative peer table exists.
- **Ban list** is a hashed lookup (phone hash plus device/environment signals, CI for Korea), not a
  readable roster. Enforcement records persist past account deletion; reputation does not.
- **Reports** use one generic model `report(target_type, target_id, reason_code, reporter_id, note)`
  feeding a single queue; idempotent; auto-hide on the double condition; `brigade_suspected` flag.
- **Tombstones** are one shared mechanism for deleted-event anchors on moments and deleted-idea
  backlinks on events.

---

## 7. Legal, privacy, and compliance

Tracked in `wepop-compliance-register.md` (dated 2026-08-26, so it predates the handoff-spec legal
register and the DEC-034 to DEC-044 items; a `compliance-watch` refresh is due). Current picture:

**Pending counsel (route to DLG Law).** The age-gate mechanism and travel-jurisdiction logic (DEC-012,
R1); minors handling and PIPA 만 14세 미만 under-14 guardian consent; PIPA personal-data basis; Korea
PASS real-name verification and CI/DI handling (DEC-026); payments KYC and tax (phase 1.5); the
host-accountability retention model and whether a 부정이용 ban list survives an erasure request
(DEC-044).

**Blocking legal gates (HOTSHEET, 2026-08-31).** Korea **위치정보법** registration
(위치기반서비스사업 신고) for the geofenced printed-poster check-in mode, blocking before P0 (risk R5,
clean radius-drop fallback exists); the **CSAM preserve-and-report runbook** (TASK-039); and the
statutory 정보통신망법 / 임시조치 takedown duties that attach from the day the service has users.

**The legal register (L-1 to L-12), never yet routed.** To go to DLG as a single consult (TASK-040),
with L-3 (위치정보법) as P0 and L-8 (under-14 guardian consent) folded into the age/location consult.

**Open (design/ops).** Behavioral-inference disclosure in the privacy policy (DEC-020); Free Now safety
details; media-of-people moderation; the moderation launch blocker; the retention policy (now DEC-039).

**Mitigated (design covers it, verify in build).** OTP/email recovery (DEC-011); anti-stalking
visibility (DEC-006/017/035); calendar minimization (DEC-013); attendee-contact-export exclusion and
reimbursement invoicing (DEC-018).

---

## 8. Risk register

From the HOTSHEET Risk Register Snapshot (Likelihood x Impact):

- **R1 - Cross-jurisdiction age verification** (Medium x High, Aakash). Locking the DEC-012 logic before
  counsel could ship a non-compliant flow. Mitigation: consult before locking; keep provisional. Active,
  in-flight.
- **R2 - Solo-founder blind spot** (Medium x Medium, Aakash). Elvis designs alone; calls may go
  unchallenged. Mitigation: Aakash and Deepak give structured critique. Active.
- **R3 - OTP/SMS deliverability by geography** (Low x Medium, Aakash). Email magic-link now covers
  recovery; check regional messaging rules before a new market. Active.
- **R4 - Single-reviewer moderation** (Medium x High, Elvis). One reviewer across eleven target types
  and five surfaces; no cover for sleep/travel/illness, no independent appeals, growth may outpace
  hiring. Mitigation: the designed load reducers plus the four day-one metrics as the hiring trigger.
  Active.
- **R5 - 위치정보법 registration exposure** (Medium x High, Aakash). The check-in geofence may require
  KCC registration before shipping in Korea. Mitigation: DLG before the geofence ships; default to the
  radius-drop fallback if registration is burdensome; residual exposure limited by DEC-034 (a forged
  check-in unlocks only a badge). Active.

Two informal watch items (not yet numbered): a user who never grants GPS has no path to update a stale
home location (DEC-031); the Explore gate's current-location integrity depends on GPS resisting spoofing
(DEC-031/DEC-032).

---

## 9. Open items and decisions still pending

- Moderation: the three pre-launch artifacts (admin queue, urgent alerts, guideline) and the CSAM
  runbook (TASK-034, TASK-039).
- Legal: the L-1 to L-12 consult with DLG (TASK-040); the age/location consult (TASK-013, deprioritized
  operationally 2026-08-31 but still real, R1 stands).
- Media: DEC-038's total-video-duration cap and org-paid video length; DEC-039's three retention
  refinements and per-uploader vs per-room scope.
- Accountability: DEC-044's cooldown, ban-list retention, org-creation account age, transfer tenure, and
  propagation-automation questions.
- Discovery: the cohort softening trigger and its global density threshold; behavioral-inference
  disclosure.
- Free Now: account-standing threshold, duration cap, archival, org rooms, location-rounding method.
- Payments: the commercial-structure proposal channel and PROJECT_STRATEGY rewrite (TASK-037); the
  ticketing/payments build scope and Korea non-Stripe path (TASK-036).
- Ideas: un-archiving, detached-idea ownership, Explore surfacing of archived ideas, pause/archive
  notifications.
- Housekeeping: adopt the I-N invariant registry and fix the stale phone-OTP invariant line in CLAUDE.md
  (TASK-041); refresh the stale `wepop-product-overview.md` (spec-sync) and `wepop-compliance-register.md`
  (compliance-watch) to the post-DEC-044 state.

---

## 10. Governance: how the project record works

- **Ownership (OWNERS.md).** Aakash owns the shared record, the merge, the hotsheet, the dashboard,
  financials, and final approval of client-facing material. Elvis owns design docs and is the client-side
  approver. Deepak owns technical design and code (in separate code repos). Everyone else **proposes**;
  only the merger writes `shared/`.
- **The merge (run-merge).** The one skill that writes `shared/` directly. It lands clean proposals into
  `shared/DECISIONS.md`, `HOTSHEET.md`, etc., parks same-topic conflicts in `MERGE-REVIEW.md`, and
  empties the landed `proposed-*.md` files. It never runs git.
- **Decisions are the source of truth.** `shared/DECISIONS.md` wins over every derived doc. Superseded
  decisions are never deleted; they are marked SUPERSEDED with a pointer and a change-history note.
- **The board.** `shared/TASK-BOARD.md` is the data; `team/board-render.py` regenerates the internal
  board and the public `docs/` board (which carries a simple login gate re-applied after every regen).
  Going live needs a human commit and push in GitHub Desktop.
- **Derived views.** `PROJECT_INDEX.md` (grounding), `PROJECT_TRACKER.md` (one-screen roll-up), the
  scope matrix, the product overview, and the compliance register are all regenerated from the source of
  truth and never hand-authored divergently.
- **House rules.** No em-dashes anywhere; governance values are ALLOW / BLOCK / ESCALATE (never DENY).

---

## 11. Decision index (DEC-001 to DEC-044)

Foundational (2026-08-17): **DEC-001** central repo + Cowork harness; **DEC-002** age gate tied to
country (SUPERSEDED by DEC-012); **DEC-003** Google-style map picker; **DEC-004** auth OTP + optional
password (SUPERSEDED by DEC-011); **DEC-005** extensible tag list; **DEC-006** anti-stalking visibility;
**DEC-007** no in-app AI image/video; **DEC-008** salvage existing code; **DEC-009** phase-1 scope
(SUPERSEDED by DEC-013 for chat/calendar).

Conflict-review and planning batch (2026-08-19 to 25, landed 2026-08-26): **DEC-010** payments phasing;
**DEC-011** auth (social + phone, password deferred); **DEC-012** age/country cascade (provisional);
**DEC-013** chat + calendar into phase 1; **DEC-014** ratings + feedback (check-in required, later
amended); **DEC-015** moments content/visibility + video; **DEC-016** location at registration;
**DEC-017** pre-join gender/photos; **DEC-018** freemium/commercial structure; **DEC-019** cohorts;
**DEC-020** recommendation algorithm; **DEC-021** recurring events (1.5); **DEC-022** Event Series +
co-hosts (1.5); **DEC-023** group-dynamics signals; **DEC-024** undiscussed-surface phase triage;
**DEC-025** new-feature scoping batch (schedule, live stories, Free Now, icebreakers, tips).

Korea/localization sync (2026-08-26/27, landed 2026-08-28): **DEC-026** Korea PASS auth; **DEC-027**
localization/Korean; **DEC-028** A/B testing; **DEC-029** language storage + i18n scope; **DEC-030**
cohort simplified to student-vs-not; **DEC-031** home-location mechanism + mutability; **DEC-032**
Explore country gate; **DEC-033** apply-to-join screening quota.

Handoff-spec intake and phase-1/1.5 review (2026-08-29/30, landed 2026-08-31): **DEC-034** peer feedback
positive-only, check-in decoupled; **DEC-035** gender out of attendee pre-join; **DEC-036** avoid signal
block-only + positive affinity; **DEC-037** general user blocking phase-1; **DEC-038** event cover media
caps; **DEC-039** tiered media retention; **DEC-040** Ideas lifecycle; **DEC-041** event schedule
multi-day; **DEC-042** change notifications; **DEC-043** completed-event immutability; **DEC-044** host
accountability split.

---

## 12. Glossary of Korean terms used in the record

- **PASS** - the common Korean carrier real-name authentication (government-linked); returns identity and
  age. Used for Korean carrier numbers (DEC-026).
- **CI / DI (연계정보)** - connecting information; a stable per-person identifier from the PASS flow, used
  as the strong ban-list key because a phone number can be swapped but a CI cannot (DEC-044).
- **PIPA** - Korea's Personal Information Protection Act; governs personal-data collection and purpose
  limitation.
- **위치정보법** - the Location Information Act; may require **위치기반서비스사업 신고** (location-based
  service provider registration) with the **KCC** before shipping the check-in geofence (R5).
- **정보통신망법** - the Network Act; imposes illegal-content takedown and the **임시조치** (temporary
  measure: blinding content pending assessment).
- **불법촬영물** - illegal filming / non-consensual intimate imagery; carries obligations under
  **전기통신사업법** (the Telecommunications Business Act).
- **부정이용 방지** - abuse prevention; the disclosed privacy-policy basis under which enforcement records
  are retained (DEC-044).
- **또 만나고 싶어요** - "want to meet again"; the positive peer tap that replaced thumbs up/down (DEC-034,
  DEC-036).
- **참석 인증** - attendance verification; the check-in badge shown on moments and feedback (DEC-034).
- **Danggeun / 매너온도** - the Korean neighborhood app (Karrot) and its manners-temperature score, cited
  as the model for splitting reputation from enforcement (DEC-044).

---

_End of reference. Generated 2026-08-31 from shared/DECISIONS.md (DEC-001 to DEC-044) and the
architecture/phase-plan source files. When this document and DECISIONS.md ever disagree, DECISIONS.md
wins._
