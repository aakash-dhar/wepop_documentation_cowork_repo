# HOTSHEET.md - Wepop running summary

> Merger-only file. Everyone else proposes via `workspaces/[you]/proposed-hotsheet.md`.
> Newest at top. Priority order: Blocking, Needs Attention, Watching, Resolved. Resolved items
> move to Resolved, they are never deleted. No em-dashes. Use a lowercase x for Likelihood x Impact.

---

## Current state (as of 2026-08-17)

Project WEP001 - Wepop. First full design walkthrough completed 2026-08-17 (Elvis, Aakash, Deepak).
Nine decisions landed (DEC-001 to DEC-009). Coordination moving to a central GitHub repo plus a
Cowork PM harness. No blockers.

### Blocking

_None yet._

### Needs Attention

- **Repo and Cowork harness setup.** Aakash to create the Wepop GitHub repo, invite Elvis, and run
  a short setup call, gated on Elvis sending the project documentation (V1 ok) and his GitHub ID via
  Slack. Since 2026-08-17. Source: 2026-08-17 walkthrough. Action items tracked in `comms/todos.md`.
- **Location at registration not locked.** Optional/contextual (current lean) vs required is
  unresolved; confirm with Elvis before it hardens. Since 2026-08-17. Source: 2026-08-17 walkthrough.

### Watching

- Age verification across jurisdictions is legally messy; the DEC-002 logic is provisional and
  should not be finalized before legal counsel. Since 2026-08-17. Source: 2026-08-17 walkthrough. (Risk R1.)
- Solo-founder blind spot: Elvis is designing Wepop alone and asked for structured pushback. Since
  2026-08-17. Source: 2026-08-17 walkthrough. (Risk R2.)
- OTP/SMS deliverability can be blocked by geography without an in-region registered business;
  relevant on expansion beyond US/Korea. Since 2026-08-17. Source: 2026-08-17 walkthrough. (Risk R3.)

### Resolved

_None yet._

---

## Risk Register Snapshot

| # | Risk | Severity (Likelihood x Impact) | Owner | Mitigation | Status |
|---|------|-------------------------------|-------|------------|--------|
| R1 | Cross-jurisdiction age verification is legally messy (US 18, Korea 19, Germany 16; passive vs active location, travel jurisdiction); locking the age/location logic before counsel could ship a non-compliant flow. | Medium x High | Aakash | Consult a lawyer before locking the DEC-002 logic; keep the country-tied approach provisional until then. | ACTIVE (in-flight) |
| R2 | Solo-founder blind spot: Elvis designing alone, product/design calls may go unchallenged. | Medium x Medium | Aakash | Aakash and Deepak give structured critique on design and docs once shared; capture as proposals/suggestions. | ACTIVE |
| R3 | OTP/SMS (Twilio/WhatsApp) deliverability blocked by geography without an in-region registered business; breaks phone verification on expansion beyond US/Korea. | Low x Medium | Aakash | Ship the optional password fallback (DEC-004); check regional messaging-provider requirements before a new market. | ACTIVE |
