# Wepop open-questions call and repo migration - 2026-09-02

**Attendees:** Aakash (PM), Elvis (client/designer), Deepak (tech lead)
**Verbatim:** [2026-09-02_Wepop_open-questions-and-repo-migration_TRANSCRIPT.md](2026-09-02_Wepop_open-questions-and-repo-migration_TRANSCRIPT.md)

## Note on the transcript

The auto-transcript's speaker labels are scrambled (long design passages spoken by Elvis are labelled
"Aakash Dhar"). This summary resolves speaker intent from context. The verbatim file is lightly condensed
for readability and left otherwise as received.

## Summary

Aakash walked Elvis through the client project reference page and the plan to migrate the repo to the
BetaCraft GitHub, then Elvis answered the blocking open questions Aakash had queued. Several answers Elvis
says he had already written in his files but which a recent version conflict may have dropped, consistent
with the governance audit that found the 2026-08-28 merge lost proposals.

## Decisions and answers

**Private accounts: phase 1.** Elvis confirmed directly. The only question was in-or-out; it is in. This
confirms the parked DEC-015 amendment.

**Discovery / cohort is not a hard filter.** Recommendations run on cohort plus the user's network (people
they directly follow, for example a parent or older sibling) plus location/distance, all as ranking
signals rather than a hard gate. Network members' events surface even outside the cohort. Location stays a
hard constraint: far-away events are searchable but never recommended. On density, no automatic
de-hardening logic is built; whether to loosen further is a manual call made later, and the growing
network is expected to solve density on its own. Amends the hard-retrieval-filter framing in DEC-019/020.

**Moments video caps.** Per-clip cap is 15s free / 30s paid, applied uniformly to moment videos and event
cover carousel videos (may rise to 60s later). No separate total-video-duration cap per Moment; the
earlier "150s" was just 10 media items times 15s. The governing cap is the number of media items per
moment (10 free; 20 or 50 paid, per the doc), because storage is the cost. Multiple moments per event per
user are allowed; text-only moments are effectively unlimited, with spam handled by reporting. Elvis
raised linking out to YouTube for long-form video as a future idea, not decided.

**Org-paid Moment video length: still open.** Currently every attendee of a paid-org event gets the 30s
cap, but Elvis is reconsidering (a free user suddenly getting 30s at an org event may confuse). Options on
the table: keep it with an explanatory notice, or restrict to org members only. Not decided.

**Media retention: 1080p confirmed, window open.** Past the retention boundary, free users see a ~1080p
version (not a thumbnail); the original is always kept, with an advance-warning message before downgrade.
The window (six vs twelve months) is left for later. Related: at launch everyone gets an extended free
trial of the paid plan (possibly around six months), so retention will not bite during the trial.

**Ideas lifecycle.** An idea can live on with no owner; there is no owner-takeover mechanism in phase 1
(deferred to a future phase, since a taker could hijack an active idea's topic). Archiving is automatic
after roughly six months of inactivity (algorithm-driven, not user-chosen); archived ideas are not
recommended or shown in feed but stay reachable by direct link or save, and nothing is deleted. Interested
users are not notified on archive (it happens quietly). Still open, now an Elvis research item: whether an
archived idea can be un-archived, and whether commenting on an archived idea is allowed (commenting would
effectively revive it).

**Free Now (not phase 1).** Individuals only, not orgs. Free feature, no account-standing gate to create a
room. The creator sets how long they are free; a timer runs; the room auto-closes at the end of that
window and on inactivity (Aakash's point that duration must be asked was accepted). Per-area chat rooms by
location, joinable open or with a set theme/pinned location.

**Live stories (not phase 1).** Ephemeral 24-hour Instagram-story style (not live streaming), archived
after 24h for the owner only. Not counted against the org 50-item media cap; uncapped for now.

## Action items

- **Repo migration to BetaCraft GitHub (Aakash).** Migrate the repo from Aakash's personal GitHub to
  Deepak's new BetaCraft repo, then send Elvis the sync steps. Elvis has pushed his latest and is freezing
  all work until Aakash confirms done, then accepts the invite, re-clones, updates origin, and re-points
  his Cowork connected folder to the new local clone. Deepak already shared the Git remote URLs.
- **Project Reference comment-sync workflow (Aakash).** Build the ability for Elvis to comment directly on
  the project reference page and have those comments sync back into the repo.
- **Ideas archiving research (Elvis).** Decide un-archive behavior and whether commenting on an archived
  idea is allowed.
- **Version hygiene.** A prior push-without-fetch caused a minor version conflict; reinforces
  pull-before-commit.
