# Elvis - Session detail, 2026-08-26

Session opened with "end session" from the prior stretch (community segmentation, recommendation
algorithm, group dynamics), then a fresh "start session" for this stretch, which repeated the full
mandated pre-read (CLAUDE.md, OWNERS.md, shared files, `comms/todos.md`, Aakash's and Deepak's session
logs) and, in the process, discovered Aakash had landed a large batch of new decisions, DEC-010 through
DEC-025, since the last briefing. Rather than assume the earlier briefing still held, this was verified
directly against the actual repo content (CLAUDE.md, HOTSHEET, PROJECT_INDEX, DECISIONS), which also
surfaced one real discrepancy: CLAUDE.md's own section 8 invariant had not been updated to match what
DEC-011 says it should say. Flagged per the repo's own rule (never silently resolve a conflict, flag it
for the merger) rather than fixed unilaterally, since section 8 sits outside Elvis's owned zone.

## What got done

**Embeddings and hidden internal tags, generation process, `recommendation-algorithm-2026-08-25.md`.**
Elvis's question: since this content can't be generated manually, what is the actual process? Resolved
with two distinct pipelines. Content-side (events, ideas, moments): triggered on create or edit, calls an
embedding model (hosted API or self-hosted, provider not yet chosen) plus a separate LLM-based tag
extraction step (resolved over simpler NLP techniques for extraction quality), both outputs stored, with
admin visibility differing by type (tags are directly readable, embeddings need a nearest-neighbor
inspection tool to be meaningful to a human). This pipeline was pulled forward into launch scope, since it
needs no behavioral history to run. User-side: seeded at onboarding from declared interests/tags, then
refined by a periodic batch job (not real-time) averaging engagement-weighted embeddings once real usage
exists, correctly deferred since it has a genuine cold-start dependency the content side does not.
Clarified the relationship between the new embedding-similarity signal (w9) and the existing exact
tag/keyword-overlap signal (w1): additive, not a replacement, each catches matches the other misses. Cost
model for the embedding/LLM calls flagged as a real, unbuilt concern, not estimated in this pass.

**Robustness roadmap and day-1 sequencing, `recommendation-algorithm-2026-08-25.md`.** Elvis asked what
else should be considered for a robust recommendation system, and specifically what belongs day 1 versus
later. Proposed four candidate day-1 investments (impression/position logging, basic experimentation
capability, anti-gaming, deletion handling) with the retroactive-data-loss tradeoff of deferring
impression logging explained upfront. Elvis's actual answer: build basic experimentation/bucketing
capability for day 1 (control/test group assignment, outcomes tagged by bucket), and explicitly defer
both impression/position logging and deletion handling to later, an informed tradeoff, not re-litigated
further since the risk had already been laid out clearly before the decision. On anti-gaming specifically,
Elvis substituted an entirely different mechanism than the rate-limiting/anomaly-detection approach
originally proposed: one personal account per user, enforced initially via phone-number uniqueness, with
ID verification planned eventually (untied to a specific phase); a user may hold multiple business/org
accounts, but each stays traceable to one specific personal user; reviews and ratings are already
restricted to checked-in attendees per DEC-014, reaffirmed here as a real anti-gaming mechanism already in
place. Residual risk flagged honestly: phone-number uniqueness deters but does not eliminate abuse
(burner numbers remain possible). This was documented as the user's actual resolution, not forced back
into the original framing. A longer list of near-term-but-not-day-1 items was captured for the record:
negative-feedback content-type suppression, a diversity re-ranking pass, a user-facing "why you're seeing
this" explainability label, formal offline evaluation metrics (NDCG and similar, needs real scale first),
a latency budget once embeddings go live, and session-stable feed ordering.

**Internationalization and Korea-specific concerns, new file, `internationalization-korea-2026-08-26.md`.**
Elvis's framing: launch is Korea-first to Korean users, but with a real international community in Korea
and a handful of US-based friends, so English and Korean both need to work at launch, plus whether
anything else needs adjusting to operate properly in Korea. Language architecture resolved as full i18n
from day one for the app's own interface (externalized, translatable strings, flagged hard to Deepak as a
day-1 architectural requirement, not a cheap retrofit later), with on-demand translation of user-generated
content (event descriptions, captions, chat) explicitly deferred to a later phase, Elvis's own choice, UI
translation still ships at launch regardless. Also resolved: a bilingual tag vocabulary (one canonical tag
ID with an English and a Korean label, not two disconnected vocabularies) and a flexible single full-name
field instead of a Western first/last split, to fit Korean naming order correctly. Multilingual embeddings
noted as likely adequate but untested. Korea-language moderation flagged as compounding the existing
HOTSHEET moderation-staffing gap, not a new separate item.

On Korea-specific concerns, used real web research rather than assumption, since these are current-world
factual questions: Stripe's own documentation did not confirm Korea-based merchant payouts or Korean local
payment method support (KakaoPay, Naver Pay, bank transfer/virtual account), a real, material gap against
DEC-010's existing Stripe-only plan and DEC-018's org tier proceeding now. Elvis chose to escalate this
immediately rather than hold it for the already-planned dedicated payments conversation, filed as
`proposed-hotsheet.md`, following the exact format in `PROPOSAL-TEMPLATES.md` (read first, since freestyle
text does not merge cleanly), assigned to Aakash. This is the first formal proposal filed to any
`proposed-*.md` channel in this visible stretch of sessions. Separately, researched how a comparable app
(Bumble) actually handles Korea age verification: a real government-issued photo ID with a self-redacted
ID number, name/DOB/photo/expiry left visible, reviewed by trained human reviewers, no facial recognition.
This is real evidence strengthening DEC-012's existing provisional self-declared-birthdate flag, folded
into the existing TASK-013 legal consult rather than treated as a new separate question. Also resolved:
plan to adopt Korea's own carrier-based identity verification (commonly delivered as PASS, via three
designated carriers and seven card companies as official verification agencies) for Korean users instead
of generic SMS OTP, subject to final TASK-013 confirmation, which also strengthens the account-integrity
anti-gaming approach for Korean users specifically as a natural byproduct. Finally, three concrete PIPA
points were folded into the TASK-013 consult: separated essential/optional consent, cross-border transfer
accountability that includes remote access by non-Korea-based team members (not just server location), and
Article 28-2 pseudonymization standards applying directly to the hidden internal keyword/embedding layer
already designed in the recommendation-algorithm doc.

**Korea-user detection, added to the internationalization file.** Elvis asked how to best determine
whether a user is in Korea, since that would drive timezone, language, the PASS flow, and payment method.
Reframed away from a single detection mechanism into four independent signals, each already available: 
timezone read live from the device OS's own timezone API; language defaulted from device locale; PASS
eligibility checked directly against the phone number's own carrier country code (one leg of DEC-012's
existing cascade, reused rather than duplicated, framed as a capability check rather than a location
question); and payment method options driven by the org's own billing setup, not the viewer's location.
For Korea-based users without a Korean phone number, a redacted-ID fallback path was resolved, following
Bumble's actual flow already researched above. In a follow-up message, Elvis confirmed the device-default
approach for both timezone and language and added one more detail: both should also carry a
settings-level manual override, so device detection is the default, not a hard lock, updated into the file
accordingly. Explicitly, no new location-detection service or "is user in Korea" flag was designed, since
that would cut against DEC-012's and DEC-016's own no-forced-GPS, no-re-checking stance.

## Files touched this session

- `recommendation-algorithm-2026-08-25.md` (revised: embeddings/tagging generation process added,
  robustness roadmap and day-1 sequencing added, anti-gaming reframed from rate-limiting to account
  integrity per Elvis's actual answer)
- `internationalization-korea-2026-08-26.md` (created, then revised: Korea-user-detection section added,
  then timezone section revised again to add the settings-override confirmation)
- `proposed-hotsheet.md` (created, first proposal filed in this visible stretch: the Stripe/Korea payments
  gap, assigned to Aakash, awaiting merger)
- No `shared/` edits. Everything correctly stayed in-workspace or in the formal proposal queue.

## Carried forward, open

- `proposed-decisions.md` still has nothing filed, despite several resolutions this session that read as
  real decisions rather than workspace notes (the embeddings/tagging pipeline architecture, day-1
  experimentation capability, the PASS adoption plan, the account-integrity anti-gaming approach). This
  gap is now four-plus sessions deep, though the hotsheet channel was used for the first time this
  session, a real step forward worth building on.
- Item 10 (Moments-doc names/budget/legal) still has not actually been sent to Aakash, still only marked
  ready to escalate, unchanged across multiple sessions now.
- Deliberately parked, not designed further: exact scope/timeline for Korea's carrier-based verification
  (pending TASK-013's actual findings); whether a Korea-specific payment processor replaces or supplements
  Stripe (pending Aakash's response to the hotsheet escalation); Naver login as a second Korean
  social-login option (not evaluated, not flagged as a gap); the redacted-ID fallback's own review-queue
  design and staffing; embedding model/provider choice and cost model; exact shape of the day-1
  experimentation capability.
- Two real feature gaps from the prior session remain undesigned: a general user-blocking capability, and
  attendee-level post-event thumbs-up/down feedback (the avoid-signal's actual data source).

TASK-012 remains Blocked on TASK-010 on the board, unchanged this session.
