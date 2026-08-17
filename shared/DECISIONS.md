# DECISIONS.md - Wepop decision log (SOURCE OF TRUTH)

> Merger-only file. Everyone else proposes via `workspaces/[you]/proposed-decisions.md`.
> This file is the single source of truth. When any document conflicts with it, defer to the
> latest DECISIONS.md entry.

## Conventions

- Each decision has a unique ID `DEC-NNN` (zero-padded, never reused).
- Status is one of `ACTIVE` / `SUPERSEDED` / `PENDING`.
- Superseded decisions are never deleted. They are marked SUPERSEDED with a pointer to the replacement.
- If a decision is ever modified, add a change-history note to that entry.
- No em-dashes. Governance values are ALLOW / BLOCK / ESCALATE, never DENY.

## Entry format

```markdown
### DEC-NNN: {{Title}}
**Date:** YYYY-MM-DD
**Participants:** {{who}}
**Status:** ACTIVE

**Decision:** {{one clear statement}}
**Reasoning:** {{why this over alternatives}}
**Impact:** {{what changes as a result}}
```

---

## Decisions

_No decisions logged yet. The first landed proposal becomes DEC-001._
