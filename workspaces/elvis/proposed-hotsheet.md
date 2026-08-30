# Proposed HOTSHEET changes from elvis, 2026-08-30 - for merger review

> Five entries, all arising from the 2026-08-29 intake of
> `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx`. Two update existing entries that the
> pending proposal batch has made stale; two are new blocking-class items the handoff surfaced that
> never reached the HOTSHEET or the risk register; one reframes the standing launch blocker around what
> is actually blocking now that response-time targets have been deferred. Source detail throughout: `workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md`.
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Proposed Hotsheet Entry
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx` §12.1, §12.3, §12.5, §7; intake review
`workspaces/elvis/handoff-spec-v0.9-intake-2026-08-29.md`
**Type:** Blocking
**Summary:** The moderation launch blocker splits into two halves: response-time targets, which Elvis has
deferred until there are employees to meet them, and moderation capability, which cannot be deferred
because UGC ships at launch and Korean takedown obligations attach from day one.
**Key Points:**
- Updates the existing Blocking entry (open since 2026-08-26) rather than replacing it. Tracked as
  TASK-034. The blocker does not clear until the pre-launch artifacts below exist.
- **SLAs deferred, Elvis 2026-08-30.** The handoff spec §12.5 proposes an urgent lane under 4 hours in
  waking hours, standard 24 hours weekday and 48 hours weekend, and appeals within 72 hours. Elvis's call
  is not to commit to these now and to revisit once employees are hired. Recorded rather than dropped, so
  the numbers are available when staffing exists. Two structural notes that go with the deferral: the
  "waking hours" phrasing was already undefined for a Korea-first launch, and the spec's appeal rule
  (reviewed by whoever did not make the first decision) is structurally impossible with a single reviewer,
  so appeals cannot be independent until there is a second person.
- **Staffing, as it actually stands.** The second reviewer named in the handoff spec is being replaced, so
  the rota is one reviewer (Elvis) plus a placeholder. This proposal uses **"Reviewer B (to be hired)"**
  rather than a name-shaped pseudonym, deliberately: a plausible-looking fake name reproduces exactly the
  failure this entry caught, where an unconfirmed name sat in a spec long enough to be read downstream as
  a real staffed position.
- **What is NOT deferred, and why this stays Blocking.** Response *speed* depends on headcount. Response
  *capability* does not, and it is what the blocker has always been about. At launch the app ships
  anonymous public-by-default host-rating comments (DEC-014), public Moment comments (DEC-015), DM and
  user-created group chats (DEC-013), Free Now location-tied rooms (DEC-025), and Discussion on every
  event and idea. All are live UGC surfaces. Without somewhere for reports to land and someone able to act
  on them, there is no removal path at all, which is a different and more serious condition than a slow
  removal path.
- **Three artifacts required before launch, none of which exist yet, and none of which are SLA
  commitments:** a basic internal admin queue (a plain web view, explicitly not a product), urgent-report
  push alerts to whoever is on call, and a one-page written guideline so decisions stay consistent (which
  matters for a single reviewer over time as much as it does between two people).
- **Legal obligations do not wait for hiring, and this is the part worth flagging hardest.**
  정보통신망법 imposes illegal-content takedown duties and the 임시조치 procedure for blinding content
  pending assessment on a rights-infringement request (legal register L-5 and L-11), and 불법촬영물
  obligations under 전기통신사업법 apply to the service (L-12). These attach to the service from the day
  it has users, not from the day it has staff. A deferred internal target is a business choice; a missed
  statutory takedown window is not.
- **Day-one metrics, worth keeping even without SLAs:** reports per 1,000 Moments, median
  time-to-decision, backlog depth, appeal overturn rate. With SLAs deferred these stop being compliance
  measures and become the hiring trigger instead, which is arguably their more useful role: they are how
  Elvis learns that one person is no longer enough before it becomes an incident rather than after.
- **The surface count has grown since the blocker was written.** It originally named four surfaces
  (anonymous host-rating comments per DEC-014, public moment comments per DEC-015, DM and user-created
  group chat per DEC-013, Free Now rooms per DEC-025). The handoff adds Discussion, a threaded persistent
  comment surface present on every event and every idea, before and after the event (§7), and its
  reportable-target list spans eleven types: user profile, organization profile, event, idea, Moment,
  individual photo or video, Moment comment, Discussion comment, chat message, chat room, plus a general
  app feedback entry. One reviewer covering eleven target types across five surfaces is the real exposure;
  filed as a companion risk in `proposed-risks.md`.
- **Real mitigations the handoff adds, worth recording because they reduce the load rather than only
  adding to it:** one generic report model (`report(target_type, target_id, reason_code, reporter_id,
  note)`) feeding a single queue rather than per-surface tooling; repeat reports by the same user on the
  same target are idempotent; auto-hide requires a double condition (5+ distinct reporters AND reports
  from at least 10 percent of distinct viewers) rather than a raw count, which matters in a student
  community where coordinating five taps is trivial and a raw threshold would hand any group a takedown
  button; and a `brigade_suspected` flag when reporters are heavily clustered, so coordinated reporting is
  visible rather than invisible.
**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| Moderation response-time SLAs deferred until employees are hired; §12.5 numbers recorded for reuse, not committed | Elvis | 2026-08-30 |
| Moderation rota is one reviewer plus "Reviewer B (to be hired)"; the previously named second reviewer is being replaced | Elvis | 2026-08-30 |
| Single generic report model and one queue rather than per-surface tooling | Elvis | 2026-08-30 |
| Auto-hide gated on a double condition (5+ distinct reporters AND 10 percent of distinct viewers) | Elvis | 2026-08-30 |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Build the internal admin moderation queue plus urgent-report push alerts (feeds TASK-034). Not an SLA commitment, this is the removal path itself | Deepak | Before launch |
| Write the one-page moderation guideline | Elvis | Before launch |
| Confirm with DLG whether 정보통신망법 / 임시조치 takedown windows impose an external response deadline that a single-reviewer setup can actually meet, since statutory windows do not defer with internal targets | Aakash | Before launch |
| Remove "Joy Jeong ops/legal" from the conflict-review item 10 name-confirmation list; that position is being refilled | Aakash | Next merge |
| Revisit response-time SLAs and independent appeal review once a second reviewer exists | Elvis | On hiring |

---

## Proposed Hotsheet Entry
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx` §4.2, §16 item L-3
**Type:** Blocking
**Summary:** The printed-poster check-in mode collects location data and may require
위치기반서비스사업 신고 to the KCC under 위치정보법, which the handoff marks BLOCKING before P0.
**Key Points:**
- Check-in has three host-side modes. The printed-poster mode uses a static event-scoped token, so its
  only anti-forgery controls are a server-side time window and a **location radius**. That radius is
  location-data collection, which is what triggers the question.
- Korea's 위치정보법 (Location Information Act) may require registering as a location-based service
  provider (위치기반서비스사업 신고) with the KCC before shipping it. This must be answered by DLG Law
  before the geofence ships.
- **There is a clean fallback if registration proves burdensome**, and it is worth stating up front so
  this does not become a hard stop: drop the radius constraint entirely and rely on the time window plus
  the live-display mode (a QR regenerated every 60 seconds from a short-TTL signed token, where a
  forwarded screenshot dies within a minute). Live display is already the default mode, so the fallback
  costs the printed-poster path some anti-forgery strength rather than costing the feature.
- The stakes are also lower than they look, because of the pending DEC-014 amendment: once Moment and
  feedback eligibility decouple from check-in, a forged check-in unlocks a badge and nothing else.
- Distinct from TASK-013, which scopes the age/location *logic* consult. This is a separate regulatory
  registration question about collecting location data at all.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| None yet. Legal answer required before the geofence ships. | | |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Route L-3 (위치정보법 registration for geofenced check-in) to DLG Law | Aakash | Before P0 |
| If registration is burdensome, drop the radius and ship printed-poster with time-window plus live-display only | Elvis + Deepak | On legal answer |

---

## Proposed Hotsheet Entry
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** `WePop_Phase1_P1.1_Consolidated_Handoff_Spec_v0.9.docx` §12.5, §16 item L-12
**Type:** Blocking
**Summary:** A written CSAM preservation-and-report runbook, reviewed by DLG, is required before launch
and does not exist; the default engineering instinct (delete it) is the legally wrong action.
**Key Points:**
- If child sexual abuse material appears it must not simply be deleted. The required handling is
  preserve, restrict access, and report to the authorities. **Deleting destroys evidence.**
- This is a pre-launch requirement, not a post-launch process improvement, and it is specifically a
  *written page* a reviewer can follow without calling Elvis at the moment it happens. With the rota
  currently at one person plus Reviewer B (to be hired), the runbook is what makes the procedure
  transferable to whoever is hired, rather than knowledge living in one head.
- Ties to 불법촬영물 obligations under 전기통신사업법 (L-12), whose user and revenue thresholds are a
  growth trigger rather than a launch trigger; the runbook itself is needed at launch regardless.
- Interacts with the moderation entry above: the urgent lane already auto-hides this content class on
  report, so the runbook governs what happens after auto-hide, not whether it is caught.
- Never reached the HOTSHEET or the risk register despite being a hard pre-launch legal gate.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| None yet. | | |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Write the CSAM preservation-and-report runbook as a one-page procedure any reviewer can follow unaided | Elvis | Before launch |
| Have DLG Law review the runbook | Aakash | Before launch |

---

## Proposed Hotsheet Entry
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** Pending DEC-014 amendment in `workspaces/elvis/proposed-decisions.md` (filed 2026-08-29)
**Type:** Watching
**Summary:** The "QR check-in is load-bearing, low check-in rate is a product risk" entry is being
reversed by a pending proposal and should be rewritten rather than left standing as-is.
**Key Points:**
- The current entry states that check-in gates ratings, host reputation, and the recommendation signal
  (DEC-014), that no scans means no ratings and no recommendation signal, and that no fallback path is
  being built. That was accurate when written on 2026-08-26.
- The pending DEC-014 amendment decouples check-in from both Moment authorship and feedback eligibility.
  A user who joined an event that completed can do both regardless of whether they checked in. Check-in
  now grants a visible verification badge and a scoring weight (1.0 verified, 0.4 unverified), not access.
- **Net effect: the risk drops substantially but does not disappear, and it changes shape.** A low
  check-in rate no longer means no ratings and no recommendation signal; it means a weaker-confidence
  signal and fewer badges. The remaining risk is different and worth watching in its place: with
  eligibility decoupled, a user who RSVP'd and never attended can now rate an event and its host, which
  DEC-014's hard gate had been quietly preventing. The 0.4 weight is the designed mitigation and the
  lever to pull if abuse appears, which is why it is specified as read-time config rather than a
  materialized value.
- Should only be rewritten if and when the DEC-014 amendment actually merges. Filed now so the entry is
  not left contradicting a landed decision at the moment it lands.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| None. Contingent on the pending DEC-014 amendment merging. | | |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| On merging the DEC-014 amendment, rewrite this Watching entry to track no-show rating abuse instead of signal starvation | Aakash (merger) | On merge |

---

## Proposed Hotsheet Entry
**Date:** 2026-08-30
**Proposed by:** Elvis
**Source:** Pending DEC-023 amendment and general-blocking proposal in
`workspaces/elvis/proposed-decisions.md` (filed 2026-08-29)
**Type:** Resolved
**Summary:** Both undesigned prerequisites for group-dynamics recommendations (DEC-023) are now designed
and filed, so this Needs Attention entry closes on merger.
**Key Points:**
- The entry named two prerequisites: a general user-blocking capability (assumed by DEC-023 to exist,
  never designed) and an attendee-level thumbs up/down post-event feedback mechanism (the avoid-signal
  data source, which did not exist).
- **Blocking is now fully designed** and proposed as a phase-1 safety baseline in the earliest build
  wave: bidirectional and total across every surface including feed, Explore, and comment threads, with
  the scope of the block stated to the user at the moment they block. This also resolves the scope
  matrix's own flagged question ("likely a phase-1 safety baseline, confirm") and the corresponding entry
  in its "Unbacked / needs a decision" section.
- **The attendee-feedback prerequisite is resolved by removing the need for it rather than by building
  it.** Thumbs-down is being removed entirely, so the avoid signal has no negative data source and never
  will. Per Elvis, the avoid signal becomes block-only, and running it on absence of a positive signal was
  explicitly considered and rejected, on the principle that it matters more to focus on what to recommend
  than on what not to recommend.
- The positive tap that replaces thumbs-down is redirected into a positive affinity ranking signal
  alongside DEC-020's social-proximity weight, so DEC-023 gains a usable attendee-level input rather than
  simply losing one.
- Closes on merger of the two pending proposals, not before.

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|
| Avoid signal becomes block-only; absence-of-positive explicitly rejected | Elvis | 2026-08-29 |
| General user blocking confirmed phase-1 baseline, earliest build wave | Elvis | 2026-08-29 |

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
| Move this entry to Resolved once both pending proposals merge | Aakash (merger) | On merge |
| Update the scope matrix row for general user blocking from later/proposed to phase 1, and clear its "Unbacked / needs a decision" entry | Aakash | On merge |

---

## Landed

- 2026-08-26: The Korea/Stripe payments item was consolidated with Aakash's Korea-payments item and
  landed into `shared/HOTSHEET.md` as a single Needs Attention entry by the merger. Source:
  `workspaces/elvis/internationalization-korea-2026-08-26.md`.
