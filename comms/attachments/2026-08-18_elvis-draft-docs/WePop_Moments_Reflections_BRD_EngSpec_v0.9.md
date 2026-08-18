# WePop Moments & Reflections — Business Requirements & Engineering Specification

**WePop Korea Co., Ltd. · Internal — Confidential**

| Field | Value |
|---|---|
| Version | v0.9 (draft for review) |
| Date | 2026-08-18 |
| Owner | Elvis Ge (CEO) |
| Audience | BetaCraft engineering (Ratnadeep Deshmane), product designer, Joy Jeong (ops/legal coordination) |
| Source of truth | *WePop Moments & Reflections Design Brief v1.0* (2026-07-03) |
| Companion docs | Phase 1 Design Brief v1.0 · Engagement & Delight Directives v1.2 · Phase 1 Product Spec (account model, event model, access model) |
| Release target | P0 groundwork in Phase 1 (late Aug 2026 MVP) · P1.1 Moments release |

**Version note.** This document is v0.9, not v1.0, because it contains unresolved `[D]` and `[O]` items (§14). It promotes to v1.0 once those are decided and written back in.

### Annotation legend

Every requirement below carries one of three tags. This is deliberate: the design brief is settled product intent, but this document adds engineering derivations that were never explicitly approved. Those are marked so they can be rejected cheaply.

| Tag | Meaning |
|---|---|
| `[C]` | **Confirmed.** Stated or directly implied by Design Brief v1.0 / prior settled specs. Build to this. |
| `[D]` | **Derived.** Engineering or product proposal introduced in this document. Needs sign-off before build. |
| `[O]` | **Open.** Genuine unresolved decision. Do not assume a default. Listed in §14. |

---

# PART I — BUSINESS REQUIREMENTS

## 1. Problem definition

WePop's core content object — the event — is **depreciating**. An event card has value from publication until start time, then decays to zero. This produces three compounding business problems:

1. **Feed starvation.** Outside club-recruitment peaks (March, September), joinable-event inventory in a single beachhead (Sinchon/Hongdae) is thin. An inventory-honest feed with nothing in it teaches users to stop opening the app. Retention collapses in the trough between semesters — precisely when we most need to hold the cohort we acquired in September.
2. **Empty profiles.** Without user-generated history, a profile is a list of RSVPs. There is nothing to browse, nothing that makes a person feel present, and nothing that makes an org look credible to a student deciding whether to join.
3. **Evaporating social energy.** The value created at an event — new connections, shared experience — has nowhere to accrue in the product. The user leaves the venue and the platform captures none of it.

**Moments** convert finished events into permanent, evergreen content: photos and first-person written reflections (후기) posted by people who **verifiably attended**. `[C]`

## 2. Strategic rationale

**2.1 Defensible differentiation.** `[C]` Korean students already write 후기 constantly (Naver blogs, Everytime, 맛집 reviews). Nobody owns the **verified 모임 후기**. WePop's version carries proof of attendance — a trust property Somoim, Munto, and Instagram structurally cannot render, because they have no check-in ground truth. Verification is the format's identity, not a footnote.

**2.2 Club distribution flywheel.** `[C]` Clubs are our distribution channel, not our product. The org history module ("12 events hosted · 340 attendees" + recent moments) is a **recruitment trust ledger**. A club that can show prospective members what its events actually feel like has a reason to run recruitment through WePop rather than an Instagram account it already controls. Moments are therefore a *supply-side* acquisition lever, not only a demand-side retention lever.

**2.3 Anti-meat-market consistency.** `[C]` Moments are reflection, not review, and not appearance-forward. The invariants (I-9 anti-attraction, I-6 save-privacy, I-11 block bidirectionality) extend fully. A photo layer is the single highest-risk surface for drifting into attraction-based selection; the guardrails in §8 are not optional polish.

## 3. Business objectives & success metrics

Targets below are `[D]` — proposed, not agreed. Instrumentation (§13) must ship with P0 so we have a pre-Moments baseline to measure against.

| ID | Objective | Metric | Proposed target |
|---|---|---|---|
| BO-1 | Close the between-events retention gap | D7 return rate, users who posted or viewed ≥1 moment vs. matched control | +8pp `[D]` |
| BO-2 | Establish the format | % of verified attendees who publish ≥1 moment within 48h of an attended event | ≥20% `[D]` |
| BO-3 | Event coverage | % of completed events with ≥3 attendees that carry ≥1 user moment | ≥35% `[D]` |
| BO-4 | Feed inventory health | % of feed sessions that reach an empty state | −50% vs. pre-Moments baseline `[D]` |
| BO-5 | Org acquisition | % of new org signups whose funnel touched an org history module | tracked, no target v1 `[D]` |
| BO-6 | Safety | Report rate per 1,000 published moments; median time-to-resolution | <5 / <24h `[D]` |
| BO-7 | Unit cost | Media storage + egress cost per MAU | <₩150 / MAU / mo `[D]` |

**BO-7 matters more than it looks.** Moments is the first feature that gives WePop a variable infrastructure cost that scales with engagement rather than with users. Against a ~$100K total budget, an uncapped media pipeline is a real risk. §11.4 specifies the controls.

## 4. Scope

### 4.1 In scope

| Wave | Deliverable | Tag |
|---|---|---|
| **P0** (Phase 1 MVP) | System recap generation; past-event page recap state; attendance-verification primitive; analytics baseline; data model provisioned for P1.1 | `[C]` |
| **P1.1** (Moments release) | Composer (3 doors) + event picker; attendee posts (1–10 photos and/or text); host photos; profile three-tab restructure + per-section visibility; feed moment card; moment detail; recap page with moments grid; series strip + series page; org history module; report/takedown flows | `[C]` |
| **P1.2** | Memories resurfacing ("1년 전 이맘때"); semester Wrapped artifact | `[C]` |
| **Phase 2** | Video moments; public web recap pages (SEO); moment comments — *comments gated on moderation staffing, not on engineering readiness* | `[C]` |

### 4.2 Explicitly out of scope

- **Comments at launch.** `[C]` Reactions only. Conversation lives in event chat. Do not reserve layout space for a comment affordance — dead space invites re-litigation.
- **Ratings, stars, 평점, "would you recommend."** `[C]` Not deferred. Excluded by product identity.
- **Freeform posting.** `[C]` There is no composer path that does not begin from a completed, attended event. This is structural, not policy.
- **Video.** `[C]` Photos + text only for P1.1. Layouts must accept a video tile later without restructuring.
- **UI-enforced face privacy.** `[C]` Untagged faces are governed by community guidelines + takedown, not by detection or blurring.

### 4.3 Critical dependency — flag

**Moments cannot ship without a working attendance-verification primitive.** `[C]` Eligibility is defined as "checked in, or confirmed + marked 'Here'." If check-in does not land in P0 with adequate participation, the eligible-event set collapses and the composer is unreachable for most users — the feature would appear broken rather than empty.

**Action required:** confirm check-in is in the late-August MVP cut, and instrument check-in rate from day one. If check-in rate runs below ~40% of confirmed attendees, we need a fallback eligibility rule before P1.1 design is locked. `[O]` — see OQ-1.

## 5. Users & jobs

| Segment | Job | Primary surface |
|---|---|---|
| Attendee (student) | "Keep the memory; show I was there; find the next one" | Composer door 1 (post-event), profile Moments tab |
| Host (student organizer) | "Prove the event was good; recruit for the next one" | Host photos, recap page, series strip |
| Org manager (club) | "Show prospective members what we're actually like" | Org history module, org profile |
| Browser (not-yet-attended) | "Decide whether this is for me" | Feed moment cards, recap pages, forward doors |

The **browser** is the conversion target. Every moment surface must end in a forward door to something joinable. `[C]`

## 6. Compliance & legal requirements

Moments materially expands WePop's personal-data exposure: user-generated photographs of identifiable people at physical locations. `[C]` requirements below are already in the brief; the rest need DLG Law confirmation.

| ID | Requirement | Tag |
|---|---|---|
| LC-1 | Tagging is opt-in only: tag request → accept. Only accepted tags render. | `[C]` |
| LC-2 | Moments never display a private venue's exact address. Location precision is capped at the event's own disclosed granularity. | `[C]` |
| LC-3 | GPS/EXIF metadata is stripped from all uploaded media server-side before any derivative is generated or served. LC-2 is unenforceable without this. | `[D]` |
| LC-4 | Host takedown is a **request routed to review**, never an instant delete. Copy must set that expectation ("검토 후 처리됩니다"). | `[C]` |
| LC-5 | Deleting a source event never destroys attendee writing. Moment soft-hides from public surfaces; owner retains access. | `[C]` |
| LC-6 | Account deletion / PIPA erasure request behavior for published moments on other people's events | `[O]` OQ-7 |
| LC-7 | Minor-related handling if the 만 18세 age gate shifts, or if under-18 users appear in photos | `[O]` OQ-8 — DLG |
| LC-8 | Retention period for removed/under-review media before hard deletion | `[D]` propose 90 days, DLG to confirm |

---

# PART II — PRODUCT REQUIREMENTS

## 7. Content model

Three kinds, one table. `[C]`

| Kind | Author | Contents | Ships |
|---|---|---|---|
| `system_recap` | Auto-generated | Event name, group size, "새로 만난 사람 N명", date. No user media. | P0 |
| `host_photos` | Event host | Photo set + optional caption, attached to the recap | P1.1 |
| `attendee_post` | Any verified attendee | 1–10 photos and/or written reflection (either alone valid); event anchor; visibility control | P1.1 |

**Validity rule** `[C]`: an `attendee_post` requires `body IS NOT NULL OR media_count > 0`. Text-only is a first-class case, not a degraded one — the profile grid needs a designed quote-tile treatment so writers without photos aren't second-class.

**Cardinality** `[D]`:
- Exactly one `system_recap` per completed event.
- At most one `host_photos` per event (the host's set attaches to the recap; re-posting edits the existing set).
- Multiple `attendee_post` per user per event permitted, rate-limited (§11.5). `[O]` OQ-3 — confirm whether a hard cap is wanted.

## 8. Functional requirements

### 8.1 Creation — one composer, three doors `[C]`

| Door | Entry | Composer opens at |
|---|---|---|
| D1 — post-event | **After** the feedback sheet completes, never inside it. The ≤15-second feedback contract is untouchable. Warm offer card; skippable forever; skipping leaves a quiet "add later from the event page" hint. | Media step (event pre-selected) |
| D2 — profile | `+` action in the Moments tab | Event picker (mandatory step 1) |
| D3 — past event page | "내 모먼트 남기기" CTA on any recap page where the viewer is a verified attendee | Media step (event pre-selected) |

**Composer steps after event selection** `[C]`: (1) media — 1–10 photos, reorderable, optional if text present; (2) reflection — open text field with rotating reflection-oriented placeholder prompts; optional if photos present; (3) visibility — Private default, publish-up option showing the event-inherited cap; (4) publish. Publishing plays a modest delight beat — warm and small, not a top-five beat.

**Event picker** `[C]`: completed + attendance-verified events only, recent-first, searchable. Old events allowed — nostalgia posts are good content. Non-qualifying events are **never shown**, so no error state exists for them.

### 8.2 Visibility — floor-and-cap `[C]`

Effective visibility is the **most restrictive** of three inputs:

1. the source event's own scope,
2. the author's per-moment choice (default **Private**),
3. the author's profile-section setting.

An org-members-only MT moment can never appear publicly, regardless of the other two. The UI must make the cap **legible**, not silently enforce it — the visibility control's label adapts to the event-inherited ceiling (전체 공개 / 팔로워 / [org] 멤버) so users understand why "public" sometimes isn't offered.

Private-first framing celebrates the diary: "나만 보기로 저장했어요 — 언제든 공개할 수 있어요." Publishing up is one tap from the tile.

> **Engineering note (§10.3).** "Most restrictive" is not a `min()` over an ordered enum. `followers` and `org_members` are not comparable ranks — they are overlapping audience sets. This must be implemented as a **conjunction of audience predicates**, not an ordinal comparison. Getting this wrong is the single most likely source of a privacy incident in this feature.

### 8.3 Profile restructure — three tabs `[C]`

| Tab | Contents | Default visibility |
|---|---|---|
| Moments (primary, grid) | Photo tiles, text-only quote tiles, private tiles with lock glyph (owner view only) | Per-section cap, default public `[D]` |
| Created | Events + ideas authored (existing compact cards) | Public `[D]` |
| Joined | Upcoming · attended · interested ideas | Upcoming **hidden from others by default** `[C]` (safety); attended defaults to followers `[C]` |

Settings gain per-section visibility caps (Moments / Created / Joined-upcoming / Joined-past), each with plain-language explanation of what others see. Per-item visibility still overrides downward. `[C]`

### 8.4 Consumption `[C]`

- **Feed.** Moment cards are **tier-2** content per Directives v1.2. They interleave only after upcoming-event inventory thins, and **never above a same-org joinable event**. Past-tense treatment + forward door mandatory.
- **Recap page.** The event details page transforms at completion: hero becomes memory treatment, moments grid is the page's heart, attendee aggregate ("14명이 함께했어요 · 새 연결 9") gives numbers emotional framing, prominent forward door ("다음 이벤트"), "add your moment" CTA for verified attendees.
- **Moment detail.** Full swipeable photos, full reflection, tappable event anchor card → recap page, reactions, share, report entry. Owner additionally sees edit + visibility. The forward door persists (sticky or footer).
- **Series.** Where `series_id` exists, a horizontal strip of past instances ("보드게임 나이트 #7") → series page listing all instances and their moments.
- **Reactions only.** Single warm reaction set. No comment affordance.

### 8.5 Governance `[C]`

- **Report** (any viewer): existing report pattern + moment-specific reason "행사와 무관한 내용" (off-experience content).
- **Host takedown request**: from any moment on their event → short reason → admin review queue. Hosts cannot directly delete attendee posts and the design must not imply they can.
- **Under review**: hidden from public, neutral owner-facing status, no shame framing.

### 8.6 Required states `[C]`

| State | Treatment |
|---|---|
| No attended events (picker empty) | Invitation, not error: "첫 이벤트를 다녀오면 모먼트를 남길 수 있어요" + one recommended event card |
| Moments tab, brand-new user | Warm empty state + door to feed; never a blank grid |
| Recap page, zero user moments | System recap carries the page; "add your moment" CTA prominent for attendees |
| Private moment (owner view) | Lock glyph, muted frame, one-tap visibility change from tile |
| Source event deleted | Soft-hide from public; owner sees "이벤트 정보가 삭제되었어요" |
| Block in either direction | Moment invisible bidirectionally (I-11) |
| Under review | Hidden from public, neutral owner status |
| Upload failure / offline compose | Local draft autosave, retry affordance, **written reflection text is never lost** |

## 9. Copy & tone `[C]`

Voice is memory-keeping with a friend — warm and specific. Composer prompts point at experience, never evaluation ("가장 기억에 남는 순간은?", "누구를 새로 만났나요?", "다음에 또 하고 싶은 것?"). Review vocabulary appears nowhere. The verification badge is quiet confidence — "참석 인증 ✓", never "BADGE EARNED!". If a user writes critique, the product does not amplify it (no featuring); host-feedback copy elsewhere reminds users where critique belongs.

---

# PART III — ENGINEERING SPECIFICATION

## 10. Data model

Postgres-flavored DDL is used as the **canonical logical model**. Backend stack remains BetaCraft's call; column semantics, constraints, and index intent are the binding part. `[D]` unless noted.

### 10.1 Core tables

```sql
CREATE TABLE moments (
  id                    uuid PRIMARY KEY,
  kind                  text NOT NULL
                          CHECK (kind IN ('system_recap','host_photos','attendee_post')),
  event_id              uuid NOT NULL REFERENCES events(id) ON DELETE RESTRICT,  -- LC-5
  series_id             uuid,          -- denormalized from events at publish, for series queries
  author_user_id        uuid REFERENCES users(id),   -- NULL only for system_recap
  body                  text,
  body_lang             text,          -- detected; used for future search/i18n
  visibility_choice     text NOT NULL DEFAULT 'private'
                          CHECK (visibility_choice IN ('private','event_scope')),
  status                text NOT NULL DEFAULT 'draft'
                          CHECK (status IN ('draft','published','under_review','hidden','removed')),
  media_count           smallint NOT NULL DEFAULT 0 CHECK (media_count BETWEEN 0 AND 10),
  reaction_count        integer NOT NULL DEFAULT 0,
  is_public_cached      boolean NOT NULL DEFAULT false,  -- fast-lane feed prefilter, §10.4
  source_event_hidden_at timestamptz,  -- set when source event deleted
  created_at            timestamptz NOT NULL DEFAULT now(),
  updated_at            timestamptz NOT NULL DEFAULT now(),
  published_at          timestamptz,

  CONSTRAINT moment_has_content CHECK (
    kind = 'system_recap' OR body IS NOT NULL OR media_count > 0
  ),
  CONSTRAINT system_recap_has_no_author CHECK (
    (kind = 'system_recap') = (author_user_id IS NULL)
  )
);

CREATE UNIQUE INDEX one_recap_per_event
  ON moments(event_id) WHERE kind = 'system_recap';
CREATE UNIQUE INDEX one_host_set_per_event
  ON moments(event_id) WHERE kind = 'host_photos';

CREATE INDEX moments_by_event   ON moments(event_id, published_at DESC)
  WHERE status = 'published';
CREATE INDEX moments_by_author  ON moments(author_user_id, published_at DESC)
  WHERE status = 'published';
CREATE INDEX moments_feed_fast  ON moments(published_at DESC)
  WHERE status = 'published' AND is_public_cached;
```

`ON DELETE RESTRICT` on `event_id` is deliberate: LC-5 forbids destroying user writing when an event is deleted. Event deletion sets `source_event_hidden_at` on child moments via the deletion service; the row survives. `[D]`

```sql
CREATE TABLE moment_media (
  id            uuid PRIMARY KEY,
  moment_id     uuid NOT NULL REFERENCES moments(id) ON DELETE CASCADE,
  position      smallint NOT NULL CHECK (position BETWEEN 0 AND 9),
  media_type    text NOT NULL DEFAULT 'photo'
                  CHECK (media_type IN ('photo','video')),   -- video reserved, Phase 2
  storage_key   text NOT NULL,
  width         integer, height integer,
  bytes         integer,
  blurhash      text,                 -- progressive placeholder, avoids layout shift
  status        text NOT NULL DEFAULT 'pending'
                  CHECK (status IN ('pending','processing','ready','failed')),
  created_at    timestamptz NOT NULL DEFAULT now(),
  UNIQUE (moment_id, position)
);

CREATE TABLE moment_reactions (
  moment_id     uuid NOT NULL REFERENCES moments(id) ON DELETE CASCADE,
  user_id       uuid NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  reaction_key  text NOT NULL,
  created_at    timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (moment_id, user_id)     -- one reaction per user per moment
);

CREATE TABLE moment_tags (
  id              uuid PRIMARY KEY,
  moment_id       uuid NOT NULL REFERENCES moments(id) ON DELETE CASCADE,
  tagged_user_id  uuid NOT NULL REFERENCES users(id),
  requested_by    uuid NOT NULL REFERENCES users(id),
  status          text NOT NULL DEFAULT 'pending'
                    CHECK (status IN ('pending','accepted','declined','revoked')),
  created_at      timestamptz NOT NULL DEFAULT now(),
  responded_at    timestamptz,
  UNIQUE (moment_id, tagged_user_id)
);
-- LC-1: only status='accepted' rows render anywhere.

CREATE TABLE moment_moderation_cases (
  id            uuid PRIMARY KEY,
  moment_id     uuid NOT NULL REFERENCES moments(id) ON DELETE CASCADE,
  case_type     text NOT NULL CHECK (case_type IN ('viewer_report','host_takedown')),
  opened_by     uuid NOT NULL REFERENCES users(id),
  reason_code   text NOT NULL,
  detail        text,
  status        text NOT NULL DEFAULT 'open'
                  CHECK (status IN ('open','reviewing','upheld','dismissed')),
  resolved_by   uuid, resolved_at timestamptz,
  created_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE profile_section_visibility (
  user_id   uuid NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  section   text NOT NULL
              CHECK (section IN ('moments','created','joined_upcoming','joined_past')),
  cap       text NOT NULL CHECK (cap IN ('public','followers','private')),
  PRIMARY KEY (user_id, section)
);
-- Defaults on account creation [D]:
--   moments=public, created=public, joined_upcoming=private, joined_past=followers
```

### 10.2 Attendance verification

Eligibility is a **derived predicate**, not a stored flag, so it can't drift from the attendance source of truth. `[D]`

```
is_verified_attendee(event_id, user_id) :=
     event.status = 'completed'
  AND EXISTS attendance(event_id, user_id) WHERE
        checked_in_at IS NOT NULL
     OR (rsvp_status = 'confirmed' AND marked_here_at IS NOT NULL)
```

The composer's event picker is a query over this predicate. Because the picker only shows qualifying events `[C]`, this predicate must also be re-evaluated server-side at publish time — a client that constructs a publish request for a non-qualifying event is rejected with `403 not_verified_attendee`.

### 10.3 Visibility resolution — conjunction of predicates

**Do not implement as `min()` over a scope enum.** `followers` and `org_members` are overlapping sets, not ordered ranks; collapsing them loses information and will eventually leak an org-scoped moment to a follower who is not a member.

```
can_view(viewer v, moment m) :=
      m.status = 'published'
  AND NOT blocked_either_direction(v, m.author)               -- I-11
  AND ( v = m.author                                          -- owner always sees own
        OR (  m.visibility_choice = 'event_scope'
          AND m.source_event_hidden_at IS NULL                -- LC-5
          AND event_audience(v, m.event)
          AND profile_section_audience(v, m.author, 'moments')
        )
      )

event_audience(v, e) := CASE e.visibility_scope
    WHEN 'public'      THEN true
    WHEN 'followers'   THEN follows(v, e.host_identity)
    WHEN 'org_members' THEN is_member(v, e.scope_org_id)
    WHEN 'invite_only' THEN was_participant(v, e)
  END

profile_section_audience(v, author, section) := CASE cap(author, section)
    WHEN 'public'    THEN true
    WHEN 'followers' THEN follows(v, author)
    WHEN 'private'   THEN false
  END
```

**Display label** (the "legible cap" requirement) is computed separately from enforcement and is purely presentational:
`display_cap(m) = label_for(m.event.visibility_scope) ∩ label_for(profile cap)`. When the two disagree, show the narrower one and explain why in plain language.

**Performance strategy.** Evaluating three predicates per candidate row per viewer does not scale in SQL joins. Two lanes: `[D]`

- **Fast lane.** `is_public_cached = true` (event scope public ∧ profile cap public ∧ choice = event_scope) → served from the ordinary feed index and CDN-cacheable payloads. This will be the large majority of feed-eligible moments.
- **Slow lane.** Everything else → resolved against a **request-scoped viewer context** loaded once per request: `{following_ids, org_member_ids, blocked_ids, participated_event_ids}`, cached in Redis for 60s. Predicates evaluate in memory against that context.

`is_public_cached` must be recomputed on: moment publish, moment visibility change, profile-section cap change (bulk update over the author's moments), event scope change (bulk update over the event's moments). Treat those last two as async jobs with a **read-side safety net**: the slow-lane predicate is always authoritative on moment detail fetch, so a stale cache can under-serve but never over-serve. `[D]`

### 10.4 Co-attendance ledger (for "새로 만난 사람 N명")

```sql
CREATE TABLE user_co_attendance (
  user_a uuid NOT NULL, user_b uuid NOT NULL,   -- stored with user_a < user_b
  first_event_id uuid NOT NULL,
  first_at timestamptz NOT NULL,
  event_count integer NOT NULL DEFAULT 1,
  PRIMARY KEY (user_a, user_b)
);
```

Written by the event-completion job: for each attendee pair, upsert. Cost is O(n²) in attendee count — 30 attendees = 435 pairs (trivial); guard with a cap at 200 attendees (19,900 pairs) before falling back to sampled/skipped computation. `[D]`

`[O]` **OQ-2:** Is "새 연결 9" a **global** event statistic or **per-viewer**? Per-viewer is far more emotionally resonant ("*you* met 9 new people") and is what the ledger above supports, but it makes the recap card non-cacheable and non-shareable as a single artifact. Decide before recap-page design is locked.

## 11. Services & API

### 11.1 Endpoints

All authenticated. Cursor pagination is keyset on `(published_at DESC, id DESC)`, opaque cursor string. `[D]`

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/v1/me/eligible-events?q=&cursor=` | Event picker. Returns completed + verified-attendance events only. |
| `POST` | `/v1/media/uploads:sign` | Returns presigned PUT URL + `media_id`. Body: content_type, bytes. |
| `POST` | `/v1/moments` | Create draft. Body: `event_id`, `kind`, `body?`, `media_ids[]?` |
| `PATCH` | `/v1/moments/{id}` | Edit draft or published moment (body, media order, visibility) |
| `POST` | `/v1/moments/{id}/publish` | Requires `Idempotency-Key`. Re-validates attendance + content rule. |
| `GET` | `/v1/moments/{id}` | Detail. Authoritative visibility check (§10.3). |
| `DELETE` | `/v1/moments/{id}` | Author-only soft delete → `removed` |
| `GET` | `/v1/users/{id}/moments?cursor=` | Profile grid |
| `GET` | `/v1/events/{id}/recap` | Recap page: system recap + moments grid + aggregate + forward door payload |
| `GET` | `/v1/series/{id}` | Series page: instances + their moments |
| `GET` | `/v1/orgs/{id}/history` | Org history module: counts + recent moments |
| `PUT` / `DELETE` | `/v1/moments/{id}/reaction` | Toggle reaction |
| `POST` | `/v1/moments/{id}/tags` | Request tag (creates `pending`) |
| `POST` | `/v1/moment-tags/{id}:accept` / `:decline` | Tagged user responds |
| `POST` | `/v1/moments/{id}/reports` | Viewer report |
| `POST` | `/v1/moments/{id}/takedown-requests` | Host takedown → review queue |
| `PATCH` | `/v1/me/profile-visibility` | Per-section caps |

### 11.2 Lifecycle state machine

```
draft ──publish──> published ──author edit──> published
  │                    │
  │                    ├──report/takedown upheld──> under_review ──> hidden
  │                    ├──source event deleted────> published (source_event_hidden_at set;
  │                    │                              public surfaces suppress, owner retains)
  │                    └──author delete───────────> removed
  └──abandon (TTL 30d)─> removed
```

`hidden` and `removed` retain the row and media for the LC-8 retention window, then hard-delete via a scheduled purge job. `[D]`

### 11.3 Media pipeline

```
client picks photos
   → POST /v1/media/uploads:sign  (one call per file, or batched)
   → direct PUT to object storage (no app-server proxying — avoids memory pressure)
   → POST /v1/moments (draft) with media_ids
   → async worker per object:
        validate real MIME (magic bytes, not extension)
        STRIP ALL EXIF, GPS mandatory            ← LC-3, hard gate
        re-encode → derivatives: thumb 400w, feed 1080w, full 2048w (WebP + JPEG fallback)
        compute blurhash
        [Phase 2 hook] automated moderation scan
        status → ready
   → publish allowed when all media status ∈ {ready, processing}; client renders blurhash
     placeholders for still-processing items
```

`[O]` **OQ-4:** block publish until all media are `ready`, or allow publish with processing placeholders? The latter is better UX on Korean mobile networks (publish feels instant) but means a moment can briefly appear with placeholder tiles in a friend's feed. Recommendation: allow, with a 60s server-side grace before the moment enters feed distribution. `[D]`

### 11.4 Cost controls (BO-7)

`[D]` — all proposed, none confirmed.

- Client-side downscale to max 2048px long edge **before** upload. Cuts typical upload from ~4MB to ~600KB.
- Hard cap 10 photos/moment `[C]`, 10MB/file, 40MB/moment.
- Serve WebP with JPEG fallback; CDN with 1-year immutable cache on derivative keys.
- Purge originals 30 days after processing, retain derivatives only. `[O]` OQ-5 — affects future re-encoding flexibility (e.g. if we later want higher-res or video stills). Recommend retaining originals in cold/archive storage rather than deleting.
- Monthly storage-growth alert at 80% of budgeted cost line.

### 11.5 Abuse & rate limits `[D]`

| Action | Limit |
|---|---|
| Publish moment | 5 / user / hour, 20 / user / day |
| Media sign request | 60 / user / hour |
| Tag request | 20 / user / day |
| Report | 10 / user / day |
| Reaction | 300 / user / hour |

### 11.6 Client (React Native) `[D]`

- **Draft store.** Local persistence (MMKV) keyed by `draft_id`, autosaved on 500ms debounce. Written text is persisted **before** any network call, satisfying the "never lose the reflection" requirement. Server draft is created on first successful media upload or on explicit save.
- **Upload queue.** Background-capable, resumable, retry with exponential backoff. Failure surfaces a retry affordance, never a data-loss dialog.
- **Rendering.** `FlashList` for feed and profile grid; blurhash placeholders to prevent layout shift; `expo-image` (or equivalent) with memory + disk cache.
- **Optimistic UI.** Reactions and visibility toggles apply optimistically with rollback on failure. Publish does **not** — it is confirmed by the server before the delight beat plays, so the beat never fires on a write that failed.

## 12. Feed integration

Two hard constraints from the brief `[C]`: moments are tier-2 (interleaved only after upcoming-event inventory thins), and a moment must **never appear above a same-org joinable event**.

**Assembly algorithm** `[D]`:

```
1. Build tier-1 list: joinable events, ranked by existing feed logic.
2. Compute floor[org] = index of the LAST tier-1 joinable event for each org.
3. Score tier-2 candidates:
     score = recency_decay(published_at)
           × affinity(viewer, author, org)      -- follows, prior co-attendance
           × content_boost(has_media, has_text)
4. Insert candidates only at positions:
     - index >= TIER2_FLOOR (default 5), and
     - index > floor[candidate.org]             -- enforces the same-org rule
5. Density caps: max 1 moment per 4 items; max 2 moments per org per session.
```

Step 4's second condition is the literal encoding of the same-org rule and should carry a test that fails loudly if the ordering inverts. It is the kind of constraint that quietly regresses during a ranking change six months from now.

## 13. Observability & analytics

**Product events** `[D]` — must ship with P0 so BO-1/BO-4 have a pre-Moments baseline:

`moment_composer_opened{door}` · `moment_event_picker_shown{eligible_count}` · `moment_draft_saved` · `moment_published{kind, media_count, has_text, visibility_choice, effective_cap, seconds_since_event_end}` · `moment_visibility_changed{from,to}` · `moment_viewed{surface, position}` · `moment_reaction_toggled` · `moment_forward_door_tapped{destination_type}` · `recap_page_viewed{has_user_moments}` · `org_history_module_viewed` · `moment_reported{reason}` · `takedown_requested` · `media_upload_failed{stage, error}`

**System metrics** `[D]`: publish p95 latency; media processing queue depth and p95 time-to-ready; EXIF-strip failure count (must be zero — page on any non-zero); visibility slow-lane resolution p95; feed assembly p95; storage bytes/day; moderation queue age.

**NFR targets** `[D]`: feed `GET` p95 < 400ms server-side · moment detail p95 < 300ms · publish ack p95 < 800ms · media time-to-ready p95 < 20s · zero tolerance on EXIF-strip failures reaching a served derivative.

## 14. Open questions

Nothing below should be resolved by assumption during build.

| ID | Question | Why it matters | Owner |
|---|---|---|---|
| OQ-1 | Is check-in confirmed in the P0/MVP cut, and what is the fallback eligibility rule if check-in rate is low? | Moments is unreachable without verified attendance (§4.3) | Elvis / BetaCraft |
| OQ-2 | Is "새 연결 N" global or per-viewer? | Determines cacheability and shareability of the recap card (§10.4) | Elvis / designer |
| OQ-3 | Hard cap on attendee posts per user per event? | Feed quality vs. expression; affects rate-limit design | Elvis |
| OQ-4 | Publish gated on all media `ready`, or allow processing placeholders? | Perceived speed vs. brief placeholder tiles in others' feeds (§11.3) | Elvis / designer |
| OQ-5 | Purge or archive original uploads after derivative generation? | Cost vs. future re-encoding flexibility (video stills, higher-res) | Elvis / BetaCraft |
| OQ-6 | Single reaction key, or a small warm set the user picks from? | Brief says "single warm reaction set" — ambiguous between one glyph and one palette | Elvis / designer |
| OQ-7 | On account deletion / PIPA erasure, what happens to that user's published moments on other people's events? | Legal obligation vs. destroying an event's shared record | DLG Law |
| OQ-8 | Minor-related handling if the 만 18세 gate shifts, or if under-18 people appear in photos | Photo layer materially raises exposure | DLG Law |
| OQ-9 | Who staffs the moderation queue at launch, and what is the SLA? | BO-6 target is meaningless without an owner; also gates Phase 2 comments | Elvis / Joy |
| OQ-10 | Brand tokens for the past-tense treatment | Brand color unresolved; placeholders only (§15) | Elvis |

## 15. Hard rules (binding on both design and implementation) `[C]`

1. Effective visibility never exceeds the source event's scope. The UI must make the cap legible, not silently enforce it.
2. No moment surface exists without a forward door to joinable content.
3. Past-tense content is always visually distinct from joinable content.
4. No comments, no ratings, no review affordances at launch.
5. Save-privacy (I-6), block bidirectionality (I-11), and the anti-attraction rule (I-9 — no appearance-forward layouts, no gender framing of attendee aggregates) extend to every Moments surface.
6. Upcoming-attendance remains hidden-by-default on profiles.
7. Brand colors remain placeholder tokens. Do **not** carry `#6B3FA0` or any prior value into these designs.
8. Every new microinteraction follows Trigger → Feedback → Loop and the §6.3 system rules of Directives v1.2 (spring family, <100ms acknowledgment, reduce-motion alternatives, quiet haptics).
9. A moment can only exist as a child of a completed event the author attended. Enforced structurally in the UI **and** re-validated server-side at publish.

## 16. Delivery sequencing

**Design order** `[C]`: (1) moment card family + verified badge + event anchor frame — everything composes from these; (2) composer + event picker; (3) profile tabs + visibility settings; (4) recap page transformation; (5) series + org modules; (6) governance sheets; (7) full state-coverage pass.

**Engineering order** `[D]` — deliberately front-loads the two things that are expensive to retrofit (the visibility predicate and the media pipeline):

| # | Workstream | Depends on | Notes |
|---|---|---|---|
| E1 | Attendance-verification predicate + eligible-events endpoint | Check-in (OQ-1) | P0. Blocks everything. |
| E2 | `moments` schema + system recap generation job + co-attendance ledger | E1 | P0. Ships the recap card with no composer. |
| E3 | Visibility predicate service + viewer context cache | E2 | Build and test in isolation with a dedicated predicate test matrix before any UI consumes it. |
| E4 | Media pipeline (sign → upload → EXIF strip → derivatives) | — | Parallelizable with E3. EXIF-strip test is a release gate. |
| E5 | Composer API + client draft store + upload queue | E3, E4 | |
| E6 | Read surfaces: profile grid, moment detail, recap page | E3 | |
| E7 | Feed integration (tier-2 assembly + same-org constraint) | E3, E6 | |
| E8 | Series strip, series page, org history module | E6 | |
| E9 | Governance: reports, takedown queue, admin review tool | E2 | Must land **before** public launch of P1.1, not after. |
| E10 | Analytics instrumentation | all | Baseline events ship in P0. |

**Release gate for P1.1:** E9 complete and staffed (OQ-9), EXIF-strip metric at zero failures over a 7-day soak, and a passing visibility predicate matrix covering every (event scope × moment choice × profile cap × block state) combination.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v0.9 | 2026-08-18 | Initial BRD + engineering spec derived from Design Brief v1.0. All engineering derivations tagged `[D]`; 10 open questions raised in §14. |
