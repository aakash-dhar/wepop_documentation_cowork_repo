# WePop categories and taxonomy, v2.0

> Elvis workspace working file. Authored by Elvis outside this repo and brought in for review
> 2026-08-27. Category and subcategory system for events, ideas, and user interest profiles. Covers the
> user-facing taxonomy (EN/KO), the color token system, picker interaction, data schema, and the backend
> tag layer. This is the actual content behind `onboarding-flow-2026-08-26.md` step 11 (categories and
> subcategories) and gives concrete shape to the hidden internal keyword layer
> `recommendation-algorithm-2026-08-25.md` already named but left abstract, see the cross-reference notes
> in both files.
>
> **Adapted into the repo, 2026-08-27:** three changes from the version Elvis brought in, reviewed and
> confirmed with him directly. `travel_companion` removed from the Travel & Outdoors subcategories (was
> gated on trust infrastructure that doesn't exist yet, verified attendance history, a host reputation
> floor, a safety interstitial); not rejected, just excluded from this initial set, can rejoin later via
> the same promotion path any Other-review graduate uses (§11.3). Joy Jeong's name removed from this
> written doc at Elvis's request, confirmed she's still the actual owner of Korean-label review, just not
> named in documentation for now, so referenced below by role rather than by name. Other-rate monitoring
> resolved as not applicable yet, pre-launch there's no live selection data to review, see §10. And a real
> cross-reference bug caught while doing this pass: §2.1 pointed at "the backend tag layer (§8)" when the
> backend tag layer is actually §9 (§8 is the color system), fixed here.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

**WePop Korea Co., Ltd., Internal, Confidential**

**Version 2.0, supersedes v1.0**
**Owner:** Elvis Ge (CEO)
**Audience:** Product designer, BetaCraft engineering (Aakash and Deepak's team)
**Companion documents:** Phase 1 Design Brief v1.0, Moments & Reflections Design Brief v1.0, Engagement &
Delight Directives v1.2

---

## 1. Purpose

The taxonomy serves three jobs at once, and every decision below is a tradeoff between them:

1. **Authoring**, a host can accurately describe what their event is, quickly, without hunting.
2. **Discovery**, an attendee can find the kind of experience they want.
3. **Self-expression**, a user can say what they're into on their profile, and the system can match on it.

Categories are the *user-facing* layer. They are deliberately coarse. Nuance lives in the backend tag
layer (§9), which users never see and never maintain.

### 1.1 What changed in v2.0

| # | Change | Rationale |
|---|---|---|
| 1 | Added **Travel & Outdoors** as a 9th category | 여행/캠핑/당일치기 had no home; travel does not decompose into sports, causes, or nightlife |
| 2 | Subcategories expanded 51 to 86 (85 as adapted into this repo, see above) | Coverage prioritized over minimalism; missing Korean-native formats (스터디, 언어교환, 노래방, 야식, 맛집 투어, 동아리 모집, 볼링/당구) were the real failure |
| 3 | **Strict MECE relaxed** | Overlap is now accepted where it improves findability. See §2.1 |
| 4 | **Cross-listing introduced** | One node can appear under two parents without duplicating data. See §5 |
| 5 | All labels **paired EN/KO** at the node level | Neither language is source of truth; parity is schema-enforced |
| 6 | **Learning & Career** reorganized into two groups (형식 / 분야) | Restores domain coverage removed during the v1.0 MECE pass |
| 7 | **Casino & poker night** removed | 도박죄 exposure; unacceptable in a Korean student app |
| 8 | **Other** locked: no user-submitted subcategories | Protects taxonomy integrity. See §10 |
| 9 | Colors respecified as **3-token sets** with semantic anchors | Base hues fail AA for small text; brand-palette conformance explicitly waived |

---

## 2. Design principles

**Categories are coarse, tags are fine.** If a distinction doesn't change what a user browses for, it
belongs in tags.

**Findability beats purity.** v1.0 optimized for a clean MECE structure. v2.0 optimizes for a user
finding the right node on the first try. Where those conflict, findability wins.

**Two doors, one room.** When a node plausibly lives in two categories, list it in both, but as the
*same* node, never a duplicate. Overlapping *listings* are fine; duplicated *nodes* are not.

**Korean-native, not translated.** Nodes are chosen from how Korean university students actually
describe gatherings. English labels are paired equivalents, not the origin.

**Coverage over minimalism.** A user who can't find their node picks "Other," and every "Other" is a
permanent hole in your discovery data. More choices is the cheaper failure.

### 2.1 On mutual exclusivity

Strict MECE is **no longer a requirement.** It was the right correction in v1.0, when categories were
mixing axes incoherently (time-of-day and content-type in the same list). That structural problem is
fixed. But taken further, MECE started deleting nodes users actually need, a 금융 스터디 is genuinely
both a format and a field, and forcing a choice between them helps nobody.

**Known tradeoff, accepted deliberately:** overlapping nodes split similar events across different
labels. A 금융 스터디 filed under 스터디 will not appear in a 금융 & 재테크 filter. At current scale
this is invisible. Past roughly 10k events it degrades filter completeness. The mitigations are already
in this spec, cross-listing (§5) covers the highest-traffic overlaps, and the backend tag layer (§9)
infers `format:study` *and* `domain:finance` regardless of what the user picked, so recommendations stay
intact even when browse-filters fragment.

This is a known limitation, not an oversight. Do not "fix" it by pruning nodes.

---

## 3. Category overview

Nine top-level categories: eight real, plus Other.

| Category (EN) | Category (KO) | Slug | Base color | Subcats |
|---|---|---|---|---|
| 🎵 Music | 음악 | `music` | `#7C3AED` | 8 |
| 🍽️ Food & Drink | 푸드 & 드링크 | `food_drink` | `#EA580C` | 12 |
| 🎨 Arts & Culture | 예술 & 문화 | `arts_culture` | `#0891B2` | 8 |
| 💪 Sports & Fitness | 스포츠 & 피트니스 | `sports_fitness` | `#16A34A` | 12 |
| 💡 Learning & Career | 학습 & 커리어 | `learning_career` | `#2563EB` | 14 |
| 🤝 Community & Causes | 커뮤니티 & 사회 | `community_causes` | `#DC2626` | 12 |
| 🎉 Nightlife & Entertainment | 나이트라이프 & 엔터테인먼트 | `nightlife_ent` | `#DB2777` | 11 |
| 🧳 Travel & Outdoors | 여행 & 아웃도어 | `travel_outdoors` | `#0F766E` | 8 |
| ⚪ Other | 기타 | `other` | `#64748B` | 0 |

**85 canonical subcategories** (86 in Elvis's original spec, minus `travel_companion`, see the adaptation
note above). Counts above are owned nodes only; cross-listed nodes (§5) appear in additional categories
without being counted twice.

---

## 4. Subcategories

Every node has one immutable `slug` and exactly two display labels. **The English and Korean labels
always refer to the same node**, there is no node that exists in one language and not the other.

Note that paired does not mean literally translated. `club_gathering` is "Club gathering & MT" / "동아리
모임 & MT", same node, same meaning to each audience, natural wording in each. Forcing loanwords in
either direction would be parity theater.

### 🎵 Music / 음악

| Slug | English | 한국어 |
|---|---|---|
| `concert_live` | 🎤 Concert & live show | 🎤 콘서트 & 라이브 |
| `dj_electronic` | 🎧 DJ & electronic | 🎧 DJ & 일렉트로닉 |
| `busking` | 🎸 Busking | 🎸 버스킹 |
| `open_mic` | 🎙️ Open mic | 🎙️ 오픈 마이크 |
| `listening_party` | 🎶 Listening party | 🎶 음악 감상회 |
| `jam_session` | 🥁 Jam session | 🥁 잼 세션 |
| `classical_jazz` | 🎹 Classical & jazz | 🎹 클래식 & 재즈 |
| `music_festival` | 🎪 Music festival | 🎪 음악 페스티벌 |

### 🍽️ Food & Drink / 푸드 & 드링크

| Slug | English | 한국어 |
|---|---|---|
| `breakfast_brunch` | ☕ Breakfast & brunch | ☕ 아침 & 브런치 |
| `lunch` | 🥗 Lunch | 🥗 점심 |
| `dinner` | 🍽️ Dinner | 🍽️ 저녁 |
| `late_night_eats` | 🌙 Late-night eats | 🌙 야식 |
| `dessert_cafe` | 🧁 Dessert & café | 🧁 디저트 & 카페 |
| `drinks_bar` | 🍻 Drinks & bar | 🍻 술자리 |
| `wine_whisky` | 🍷 Wine & whisky | 🍷 와인 & 위스키 |
| `beer_cocktails` | 🍺 Beer & cocktails | 🍺 맥주 & 칵테일 |
| `non_alcoholic` | 🫖 Non-alcoholic & wellness drinks | 🫖 논알콜 & 웰니스 음료 |
| `cooking_class` | 🍳 Cooking class | 🍳 쿠킹 클래스 |
| `food_crawl` | 🍜 Food crawl & tasting tour | 🍜 맛집 투어 |
| `food_market` | 🌮 Food market & festival | 🌮 푸드 마켓 & 축제 |

*Cross-listed in:* Travel & Outdoors (`food_crawl`)

### 🎨 Arts & Culture / 예술 & 문화

| Slug | English | 한국어 |
|---|---|---|
| `visual_art` | 🖼️ Visual art & exhibition | 🖼️ 전시 & 미술 |
| `photography` | 📷 Photography | 📷 사진 & 출사 |
| `theater_performance` | 🎭 Theater & performance | 🎭 연극 & 공연 |
| `dance_performance` | 💃 Dance performance | 💃 댄스 공연 |
| `film_screening` | 🎬 Film & screening | 🎬 영화 & 상영회 |
| `literature_poetry` | 📖 Literature & poetry | 📖 문학 & 시 |
| `craft_making` | ✏️ Craft & making | ✏️ 공예 & 만들기 |
| `heritage_history` | 🏛️ Heritage & history | 🏛️ 역사 & 문화유산 |

*Cross-listed in:* Travel & Outdoors (`photography`)

### 💪 Sports & Fitness / 스포츠 & 피트니스

| Slug | English | 한국어 |
|---|---|---|
| `yoga_mindfulness` | 🧘 Yoga & mindfulness | 🧘 요가 & 명상 |
| `running_cycling` | 🏃 Running & cycling | 🏃 러닝 & 자전거 |
| `team_sports` | ⚽ Team sports | ⚽ 팀 스포츠 |
| `racket_sports` | 🎾 Racket sports | 🎾 라켓 스포츠 |
| `bowling_billiards` | 🎳 Bowling, billiards & darts | 🎳 볼링 · 당구 · 다트 |
| `gym_strength` | 🏋️ Gym & strength training | 🏋️ 헬스 & 웨이트 |
| `combat_martial_arts` | 🥊 Combat & martial arts | 🥊 격투기 & 무술 |
| `adventure_sports` | 🧗 Extreme & adventure sports | 🧗 익스트림 스포츠 |
| `swimming_water` | 🏊 Swimming & watersports | 🏊 수영 & 워터스포츠 |
| `board_skate` | 🛹 Board & skate | 🛹 보드 & 스케이트 |
| `target_climbing_gym` | 🎯 Shooting, archery & climbing gym | 🎯 사격 · 양궁 · 클라이밍 짐 |
| `dance_fitness` | 🤸 Dance fitness | 🤸 댄스 피트니스 |

*Also shown here (owned elsewhere):* `hiking_trekking` (Travel & Outdoors)
*Cross-listed in:* Nightlife & Entertainment (`bowling_billiards`)

### 💡 Learning & Career / 학습 & 커리어

This is the only category using **subcategory groups**, 14 nodes is too many for a flat browse list.

**형식 / Format**

| Slug | English | 한국어 |
|---|---|---|
| `study_group` | 📚 Study group | 📚 스터디 |
| `language_exchange` | 🗣️ Language exchange | 🗣️ 언어교환 |
| `career_exam_prep` | 📝 Career & exam prep | 📝 취업 & 시험 준비 |
| `competition_team` | 🏆 Competition & team project | 🏆 공모전 & 팀 프로젝트 |
| `workshop_class` | 🛠️ Workshop & class | 🛠️ 워크숍 & 클래스 |
| `talk_seminar` | 🎓 Talk & seminar | 🎓 강연 & 세미나 |
| `hackathon_build` | 💻 Hackathon | 💻 해커톤 |
| `networking` | 🤝 Networking | 🤝 네트워킹 |

**분야 / Field**

| Slug | English | 한국어 |
|---|---|---|
| `field_tech` | 👨‍💻 Tech & development | 👨‍💻 테크 & 개발 |
| `field_design` | 🎨 Design & creative | 🎨 디자인 & 크리에이티브 |
| `field_finance` | 💰 Finance & investing | 💰 금융 & 재테크 |
| `field_marketing` | 📣 Marketing & media | 📣 마케팅 & 미디어 |
| `entrepreneurship` | 🚀 Entrepreneurship | 🚀 창업 |
| `self_development` | 🌱 Self-development & mindset | 🌱 자기계발 & 마인드셋 |

*Also shown here (owned elsewhere):* `club_recruiting` (Community & Causes)
*Cross-listed in:* Community & Causes (`language_exchange`)

### 🤝 Community & Causes / 커뮤니티 & 사회

| Slug | English | 한국어 |
|---|---|---|
| `club_recruiting` | 📣 Club & society recruiting | 📣 동아리 & 학회 모집 |
| `club_gathering` | 🎒 Club gathering & MT | 🎒 동아리 모임 & MT |
| `small_group` | 🧑‍🤝‍🧑 Small group & regular meetup | 🧑‍🤝‍🧑 소모임 & 정기모임 |
| `volunteering` | 🙌 Volunteering | 🙌 봉사활동 |
| `charity_fundraising` | ❤️ Charity & fundraising | ❤️ 기부 & 모금 |
| `social_advocacy` | ✊ Social justice & advocacy | ✊ 사회 참여 & 캠페인 |
| `environment` | 🌿 Environment & sustainability | 🌿 환경 & 지속가능성 |
| `faith_spirituality` | 🕊️ Faith & spirituality | 🕊️ 종교 & 영성 |
| `family_parenting` | 👨‍👩‍👧 Family & parenting | 👨‍👩‍👧 가족 & 육아 |
| `pets` | 🐾 Pets & animals | 🐾 반려동물 |
| `cultural_celebration` | 🎊 Cultural celebration | 🎊 문화 축제 |
| `neighborhood_local` | 🏘️ Neighborhood & local | 🏘️ 동네 & 지역 |

*Also shown here (owned elsewhere):* `language_exchange` (Learning), `camping` (Travel)
*Cross-listed in:* Learning & Career (`club_recruiting`)

### 🎉 Nightlife & Entertainment / 나이트라이프 & 엔터테인먼트

| Slug | English | 한국어 |
|---|---|---|
| `party_celebration` | 🥳 Party & celebration | 🥳 파티 & 기념일 |
| `club_night` | 🌙 Club night | 🌙 클럽 |
| `bar_hopping` | 🍸 Bar hopping & pub crawl | 🍸 바 호핑 & 펍크롤 |
| `social_mixer` | 🥂 Social mixer | 🥂 소셜 모임 |
| `karaoke` | 🎤 Karaoke | 🎤 노래방 |
| `comedy_improv` | 😂 Comedy & improv | 😂 코미디 & 즉흥극 |
| `board_games` | 🎲 Board games & trivia | 🎲 보드게임 & 퀴즈 |
| `video_games` | 🎮 Video games & esports | 🎮 게임 & e스포츠 |
| `escape_activity` | 🔐 Escape room & activity café | 🔐 방탈출 & 액티비티 카페 |
| `festival_fair` | 🎡 Festival & fair | 🎡 페스티벌 & 축제 |
| `immersive_themed` | 🔮 Immersive & themed | 🔮 이머시브 & 테마 이벤트 |

*Also shown here (owned elsewhere):* `bowling_billiards` (Sports & Fitness)

### 🧳 Travel & Outdoors / 여행 & 아웃도어

| Slug | English | 한국어 |
|---|---|---|
| `day_trip` | 🚌 Day trip | 🚌 당일치기 |
| `weekend_trip` | 🧳 Weekend & overnight trip | 🧳 주말 & 1박2일 |
| `camping` | ⛺ Camping | ⛺ 캠핑 |
| `hiking_trekking` | 🥾 Hiking & trekking | 🥾 등산 & 트레킹 |
| `picnic_outing` | 🧺 Picnic & outing | 🧺 피크닉 & 나들이 |
| `walking_tour` | 🚶 Walking tour & city exploring | 🚶 도보 여행 & 도시 탐방 |
| `beach_island` | 🏖️ Beach & island | 🏖️ 바다 & 섬 |
| `road_trip` | 🚗 Drive & road trip | 🚗 드라이브 & 로드트립 |

*Also shown here (owned elsewhere):* `photography` (Arts), `food_crawl` (Food & Drink)
*Cross-listed in:* Sports & Fitness (`hiking_trekking`), Community & Causes (`camping`)

**Removed from this set, 2026-08-27:** `travel_companion` (👥 Travel companion / 👥 여행 메이트). Elvis's
original spec flagged this as the highest-risk surface in the product, overnight travel with strangers,
requiring stricter trust gating than any other node: verified attendance history, a host reputation
floor, and a safety interstitial before joining, none of which exist yet. Rather than ship a node that
explicitly should not ship without infrastructure that isn't built, it's excluded from this initial
taxonomy. Not rejected, can be added back via the same promotion path (§11.3) once that trust layer
exists, worth cross-referencing against DEC-014's ratings/check-in work when that pass happens.

### ⚪ Other / 기타

**Zero subcategories. By design.** See §10.

---

## 5. Cross-listing

A subcategory may appear under more than one category. Selecting it from either door yields the same
`subcategory_id`, there is no duplication and no data fragmentation. Two doors, one room.

**Why this exists:** with a browse-only picker (§6), the only path to a node is guessing its parent
correctly. A user who thinks 볼링 is a night out opens Nightlife, doesn't find it, and gives up or files
under Other. Cross-listing removes that failure without splitting the data.

### 5.1 Rules

- **Maximum 2 parents per node.** No exceptions.
- **Exactly one parent is `is_primary`.** Primary is the canonical home for analytics and default display.
- Cross-listing requires a *"a reasonable person would look here first"* argument, not loose thematic
  fit. Without this discipline, every node drifts toward being in every category.
- Cross-listing is an **admin/config decision**, never user-editable.

### 5.2 Map

| Node | Primary | Also under | Rationale |
|---|---|---|---|
| `bowling_billiards` | Sports & Fitness | Nightlife | Most students file 볼링/당구 as a night out, not a sport |
| `hiking_trekking` | Travel & Outdoors | Sports | The challenge/destination ruling (§7) is invisible to users |
| `photography` | Arts & Culture | Travel | 출사 *is* a trip |
| `food_crawl` | Food & Drink | Travel | A 맛집 투어 is often the entire itinerary |
| `language_exchange` | Learning & Career | Community | Split reads: skill-building vs. meeting people |
| `club_recruiting` | Community & Causes | Learning | 학회 is academic; 동아리 is social |
| `camping` | Travel & Outdoors | Community | Club MT overlap |

### 5.3 Attribution vs. matching

These are different, and conflating them causes bugs.

**Attribution (what the user sees).** The event is labeled with the category the user *walked through*.
Picked 볼링 under Nightlife, the event shows a Nightlife chip. Showing them a category they never opened
is confusing. Store the entry category on the join row.

**Matching (what discovery queries).** Filters and recommendations match on the node's **full parent
set**, not the attributed one. A Sports filter still returns that event. Cross-listing therefore
*improves* recall rather than splitting it.

---

## 6. Picker interaction

**Browse-only. No search.** Users tap a category, then choose subcategories from that category's screen.
There is no type-ahead in the selection flow.

### 6.1 Flow

1. **Category grid**: 9 tiles (emoji + label + color). Fixed order, see §6.3.
2. **Subcategory screen**: that category's nodes as a wrapped chip grid. Learning & Career shows group
   headers (형식 / 분야); all others are flat.
3. **Back to grid**: selected categories show a count badge; user can enter another category or finish.

### 6.2 Selection rules

**Selecting a subcategory auto-selects its parent category.** Users express one intent, not two. Never
make them pick a category and then separately pick subcategories under it.

Consequences worth stating explicitly:

- A category can never be selected with zero subcategories under it. This kills an entire class of
  empty-filter results.
- Deselecting the last subcategory in a category deselects the category.
- Limits become: **up to 5 subcategories drawn from at most 3 categories** (events) / **up to 8
  subcategories from at most 5 categories** (profiles).

| Context | Max categories | Max subcategories |
|---|---|---|
| Event / Idea | 3 | 5 |
| User profile | 5 | 8 |

Limits are enforced in the UI **and** validated server-side at the API. UI enforcement alone is not
enforcement.

**Limit-reached behavior:** disable unselected chips with a quiet inline explanation ("최대 5개까지
선택할 수 있어요"). Do not show an error toast, the user did nothing wrong.

### 6.3 Category grid order

Grid order is load-bearing, because the two tight color pairs must never sit adjacent: Arts cyan / Travel
teal (close hue, separated only by lightness), and Community red / Nightlife pink.

```
Music       Food        Arts
Sports      Learning    Community
Nightlife   Travel      Other
```

Other is last and visually recessive, it should read as the residual option, never as an appealing ninth
choice.

### 6.4 Design notes

- **Progressive disclosure.** The category grid is the only thing on screen at step 1. Never preview
  subcategories on the grid.
- **Chip grid, not a list.** Nodes are short; wrapped chips fit 8 to 14 items without scrolling on most
  devices. Learning's 14 with group headers is the worst case, verify it on a 375pt viewport.
- **Cross-listed chips are visually identical** to owned chips. The user should never perceive the
  distinction.
- **Selection state must be legible without color alone**, checkmark or fill change, not just a hue
  shift (§7.3).
- No empty states are possible here; every category has nodes except Other, which has a dedicated
  treatment (§10).

---

## 7. Boundary rulings

Where two categories could plausibly claim the same event, these rulings decide. **Motivation decides,
not surface activity.** Ship these to engineering, they resurface as bugs otherwise.

| # | Boundary | Ruling |
|---|---|---|
| BR-1 | Dance | Physical activity → Sports (`dance_fitness`). Performance/expression → Arts (`dance_performance`). |
| BR-2 | Cultural events | Community belonging → Community (`cultural_celebration`). Curated creative work → Arts. |
| BR-3 | Workshops | Transferable skill as output → Learning (`workshop_class`). Creative artifact as output → Arts (`craft_making`). |
| BR-4 | Outdoors | Physical challenge is the point → Sports (`adventure_sports`). Going somewhere is the point → Travel (`hiking_trekking`). A 한라산 등반 for the summit is Travel; a climbing gym session is Sports. |
| BR-5 | Charity | Participation/labor → `volunteering`. Money → `charity_fundraising`. Different user intent, different events. |

---

## 8. Color system

**Brand-palette conformance is explicitly waived for categories.** The goal is maximum inter-category
distinguishability plus a loose semantic anchor. These do not need to sit inside WePop's pastel brand
palette.

### 8.1 Tokens

Each category needs **three tokens, not one.** Base hues are selected for hue separation, not contrast,
`#EA580C` is ~3.4:1 on white and fails WCAG AA for body text. Anything rendering a category *label* uses
`-text` on `-surface`. `-base` is for shape, dots, and icon tint, never small type.

| Category | `-base` | `-surface` | `-text` | Semantic anchor |
|---|---|---|---|---|
| Music | `#7C3AED` | `#F3EFFE` | `#5B21B6` | Stage light, neon |
| Food & Drink | `#EA580C` | `#FFF1E8` | `#9A3412` | Warmth, appetite |
| Arts & Culture | `#0891B2` | `#E6F6FA` | `#0E5F73` | Museum, ink |
| Sports & Fitness | `#16A34A` | `#E9F8EF` | `#15803D` | Turf, field |
| Learning & Career | `#2563EB` | `#EAF1FE` | `#1D4ED8` | Academic, trust |
| Community & Causes | `#DC2626` | `#FDECEC` | `#B91C1C` | Heart, solidarity |
| Nightlife & Ent. | `#DB2777` | `#FDECF4` | `#9D174D` | Neon, late hours |
| Travel & Outdoors | `#0F766E` | `#E6F4F2` | `#0F5F59` | Water, horizon |
| Other | `#64748B` | `#F1F3F6` | `#475569` | Deliberately recessive |

Naming: `--cat-{category_slug}-{base|surface|text}`. Example: `--cat-food-drink-surface`.

### 8.2 Rules

- **Color is reinforcement, never identification.** Nine distinguishable hues is at the practical
  ceiling; emoji + label do the identifying work. No UI may depend on color alone to distinguish a
  category, accessibility requirement as much as a design one.
- Dark mode needs a parallel triplet (deeper surface, lighter text). Not specified here; derive at
  implementation.
- Colors are config, not constants. Store on the category record so a palette revision doesn't require a
  code change.

---

## 9. Backend tag layer

Tags are **backend-only.** Never user-selectable, never user-editable, never shown in the primary
picker. Modeled on Netflix-style hidden taxonomies. **This is the same mechanism
`recommendation-algorithm-2026-08-25.md` names as the "hidden internal keyword layer" (DEC-020), this
section is its concrete specification, not a competing system, worth pointing Deepak at both files
together rather than building from either alone.**

**Assignment:**
1. **Rules engine**, deterministic, from structured event data. *(e.g. category = Music AND start time >
   22:00 AND capacity < 50 → `intimate-late-night`)*
2. **AI inference**, an LLM pass over title + description assigns semantic tags. This is the layer that
   recovers the granularity the user-facing taxonomy gives up (§2.1): a 금융 스터디 gets `format:study`
   **and** `domain:finance` regardless of which single node the host picked.
3. **Behavioral**, accrued over time from platform signals (`trending`, `sells-out-fast`,
   `frequently-saved`, `new-host`).

**Illustrative vocabulary:** `late-night`, `outdoor-friendly`, `intimate`, `beginner-friendly`,
`sober-friendly`, `free-entry`, `high-energy`, `recurring`, `pet-friendly`, `trending`, `sells-out-fast`,
`new-host`, `domain:finance`, `format:study`

Tags may drive filter *facets* in a later release (e.g. an adult/professional cohort browsing by
domain), but they never become subcategories.

---

## 10. Other / 기타

**Zero subcategories. No user-submitted subcategories. This is settled, do not reopen.**

The rejected feature was letting users type their own subcategory under Other. The reason is not content
moderation (WePop already accepts free text in titles, descriptions, and Moments reflections, one more
short string is marginal). The reason is **structural**:

- **Fragmentation.** 스터디 / 스터디모임 / study group / 공부모임 become four nodes with one event each.
  Every one is a dead-end filter, tap it, see one result, conclude the app is empty.
- **Signal dilution.** A one-off string has no relationship to anything else in the system. It
  contributes nothing to the recommender while consuming one of the user's 5 subcategory slots.
  Negative-value structured data.
- **Cannibalization.** If Other offers self-expression the real categories don't, it becomes the
  *attractive* choice. Users who should pick Food & Drink → 저녁 pick Other → "밥약" because it feels
  more like them. You degrade your primary signal precisely by making the escape hatch more appealing
  than the front door.

**What ships instead:**

1. A single optional free-text field on the creation form, *"한 줄로 설명해 주세요"*, living **outside**
   the taxonomy, present regardless of category. The AI reads it for backend tag assignment (§9). Users
   get expression; the system gets structured data.
2. Every Other selection is logged with that description.
3. **Monthly review, deferred, not a pre-launch task.** Owned by WePop's KR ops/localization reviewer
   (name kept out of this written doc at Elvis's request, the role is filled, not open). Confirmed with
   Elvis directly: there's no live Other-selection data to review before launch, so this doesn't need
   scheduling or staffing now, it's a real task once real usage exists, not before. Recurring patterns
   graduate into real subcategories via §11.3. This makes Other a product research instrument rather than
   a data graveyard, once there's something to instrument.

**Success metric:** Other selection rate should trend **below 3%** of events. A sustained rate above that
means the taxonomy has a real hole, treat it as a coverage bug, not user error.

---

## 11. Data model

### 11.1 Schema

```sql
categories (
  slug            TEXT PRIMARY KEY,     -- 'food_drink'
  emoji           TEXT NOT NULL,
  color_base      TEXT NOT NULL,
  color_surface   TEXT NOT NULL,
  color_text      TEXT NOT NULL,
  sort_order      INT  NOT NULL,
  is_active       BOOL NOT NULL DEFAULT TRUE
);

subcategory_groups (                    -- optional; only Learning uses this today
  slug            TEXT PRIMARY KEY,     -- 'learning_format'
  category_slug   TEXT NOT NULL REFERENCES categories(slug),
  sort_order      INT  NOT NULL
);

subcategories (
  slug            TEXT PRIMARY KEY,     -- 'study_group', immutable
  emoji           TEXT NOT NULL,
  group_slug      TEXT REFERENCES subcategory_groups(slug),   -- nullable
  is_active       BOOL NOT NULL DEFAULT TRUE
);

subcategory_parents (
  subcategory_slug TEXT REFERENCES subcategories(slug),
  category_slug    TEXT REFERENCES categories(slug),
  is_primary       BOOL NOT NULL,
  sort_order       INT  NOT NULL,
  PRIMARY KEY (subcategory_slug, category_slug)
);

-- i18n: neither language is source of truth
category_labels (
  category_slug   TEXT REFERENCES categories(slug),
  locale          TEXT NOT NULL,        -- 'en' | 'ko'
  display_name    TEXT NOT NULL,
  PRIMARY KEY (category_slug, locale)
);

subcategory_labels (
  subcategory_slug TEXT REFERENCES subcategories(slug),
  locale           TEXT NOT NULL,
  display_name     TEXT NOT NULL,
  PRIMARY KEY (subcategory_slug, locale)
);

-- assignment
event_subcategories (
  event_id            UUID REFERENCES events(id),
  subcategory_slug    TEXT REFERENCES subcategories(slug),
  entry_category_slug TEXT NOT NULL,    -- the door the user walked through (§5.3)
  PRIMARY KEY (event_id, subcategory_slug)
);

user_interest_subcategories (
  user_id             UUID REFERENCES users(id),
  subcategory_slug    TEXT REFERENCES subcategories(slug),
  entry_category_slug TEXT NOT NULL,
  PRIMARY KEY (user_id, subcategory_slug)
);
```

### 11.2 Invariants

| ID | Invariant | Enforcement |
|---|---|---|
| T-1 | Every active subcategory has **exactly 2** label rows (`en`, `ko`) | CI check + admin-write validation. UI-only enforcement will leak a single-locale node within months. |
| T-2 | Every active category has exactly 2 label rows | Same |
| T-3 | Every subcategory has **1 to 2** parents, **exactly one** `is_primary` | DB constraint or write-path validation |
| T-4 | `entry_category_slug` must be a valid parent of the selected subcategory | Write-path validation |
| T-5 | Selection limits enforced **server-side**, not only in the UI | API validation |
| T-6 | Slugs are immutable once live | Labels change freely; slugs never do, display copy must be revisable without a migration |
| T-7 | Deactivation, never deletion | `is_active = FALSE` preserves historical event assignments |

### 11.3 Promotion path

When Other-review (§10) surfaces a recurring pattern:

1. Insert the node into `subcategories` plus both label rows plus parent row(s).
2. Backfill `event_subcategories` for historical events matching the pattern, so past events gain the
   real node.
3. Ship. Existing filters pick it up with no client change.

This is also the path `travel_companion` would rejoin the taxonomy through, once its trust-gating
prerequisites exist, rather than being reintroduced as a special case.

### 11.4 Localization ownership

Korean labels are reviewed and owned by WePop's KR ops/localization reviewer, name kept out of this
written doc at Elvis's request, confirmed the role itself is filled, not open. Neither locale is a
translation of the other, both are authored for their audience. Any new node requires both labels before
it can go active (T-1).

---

## 12. Open items

| ID | Item | Owner | Notes |
|---|---|---|---|
| TX-1 | ~~`travel_companion` trust gating spec~~ | | Superseded, the node itself is removed from this taxonomy for now rather than shipped ungated. Revisit via §11.3 once trust infrastructure exists. |
| TX-2 | Korean label review pass | KR ops/localization (owned, name withheld from docs per Elvis) | Full sweep of all 85 + 9 labels for naturalness, not correctness |
| TX-3 | Dark-mode color triplets | Designer | Derive from §8.1 |
| TX-4 | Learning & Career chip grid on 375pt | Designer | 14 nodes + 2 group headers is the worst-case screen, verify no scroll or accept scroll |
| TX-5 | Add `gambling` to moderation blocklist | BetaCraft | Follows removal of casino/poker node (도박죄) |
| TX-6 | Other-rate monitoring | Deferred, not applicable pre-launch | No live selection data exists yet to monitor. Revisit once real usage exists, confirmed not a launch blocker. |

---

*WePop categories and taxonomy v2.0, adapted into the repo 2026-08-27, WePop Korea Co., Ltd., Confidential*
