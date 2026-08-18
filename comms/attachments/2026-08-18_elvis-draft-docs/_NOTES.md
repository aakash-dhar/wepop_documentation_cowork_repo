# _NOTES - Elvis draft docs drop, 2026-08-18

Companion notes for the material in this folder. No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## What this is

On 2026-08-18 Elvis shared his first project documentation for Wepop via Slack, together with his
GitHub ID (`programinator-elvis`, logged in `comms/todos.md` item 2). This closes the documentation
half of the DEC-001 harness-setup gate, as a draft.

## Provenance and authority

- **Shared by:** Elvis (client and designer), via Slack, 2026-08-18.
- **Elvis's own note:** "I haven't reviewed these. I will review and send an updated version tomorrow.
  But here is what I have so far."
- **Authority:** DRAFT / PROVISIONAL. Do not treat as settled product intent. When any of this
  conflicts with `shared/DECISIONS.md`, DECISIONS controls. A reviewed version is expected; when it
  lands, run the design-side intake against it and supersede these files (move this dated folder to a
  nearby `_archive/` rather than editing in place).

## Files received

| File | What it is | Version |
|------|-----------|---------|
| `WePop_Phase_1_Brief_v2.html` | Full MVP screen set for the Sinchon/Hongdae launch (tokens, component library, auth, home/Sunday Deck, explore/map, create, event lifecycle, ideas, chat, notifications, calendar, profiles, org, governance, moments). Standalone React page, 16 sections, 233 artboards. | Brief v2 |
| `WePop_Moments_Reflections_BRD_EngSpec_v0.9.md` | Business requirements plus engineering spec for the Moments/Reflections feature (post-event 후기 with verified attendance): data model, visibility logic, media pipeline, API, feed integration, 10 open questions, delivery sequencing. | Moments v0.9 |

## Produced from these (PM cross-check)

| File | What it is |
|------|-----------|
| `Wepop_Walkthrough-vs-Drafts_Review-Aid_2026-08-18.md` | A said-vs-produced review aid: the 2026-08-17 walkthrough transcript checked against both drafts, flagged as MATCH / CHANGED / ADDED / DOCS DISAGREE / OPEN. Built for Elvis to speed his own review (Markdown so his Claude can act on it). |
| `Wepop_Walkthrough-vs-Drafts_Review-Aid_2026-08-18.pdf` | Same content, human-readable. |

The review aid was independently validated by a separate agent against the transcript and both source
docs before delivery: no hallucinations, no wrong numbers, no misattributions; four minor wording fixes
applied.

## What the cross-check surfaced (for tracking, to resolve after the reviewed version)

- **The two drafts contradict each other** on three points: ratings/reviews (the Phase 1 Brief has
  them, the Moments spec bans them), comments on moments (brief has a comments-open screen, spec
  forbids), and video on moments (brief allows video up to 5, spec is photos and text only, up to 10).
- **Diverges from locked decisions:** age gate shown as flat 18+ vs the country-tied ~19 of DEC-002;
  Kakao dominance with OTP skipped vs DEC-004's "OTP verifies every user"; DM, user-group-chat, and
  calendar screens shown without the later-phase marker DEC-009 implies.
- **Introduced but never discussed on the call:** check-in QR (load-bearing for Moments), Sunday Deck,
  waitlist auto-promote, co-hosts, apply-to-join, series pages, org track-record module, ownership
  transfer, and P1.2 memories/Wrapped.
- **Commercial/legal items in the Moments doc** (ESCALATE to financials owner before they harden):
  a ~$100K budget line and DLG Law as counsel; plus new named people (Ratnadeep Deshmane as the
  engineering contact, Joy Jeong ops/legal).

All of the above are on unreviewed drafts, so nothing is proposed as a decision here. Reconcile after
Elvis's reviewed version lands (`comms/todos.md`).
