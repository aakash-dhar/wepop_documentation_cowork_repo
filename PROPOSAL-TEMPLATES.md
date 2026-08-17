# PROPOSAL-TEMPLATES.md - parseable proposal formats (Wepop)

The merger parses these formats, so freestyle does not merge cleanly. Copy the matching block into
the right `proposed-*.md` file in your workspace, fill it in, and let the merger land it. No
em-dashes. Governance values are ALLOW / BLOCK / ESCALATE, never DENY.

## proposed-decisions.md

```markdown
## DEC-NNN (PROPOSED)
**Date:** YYYY-MM-DD
**Proposed by:** [you]
**Source:** {{email NN / meeting / call / your session}}
**Topic:** {{short title}}
**Type:** Technical | Strategic | Commercial | Operational
**Decision:** {{one clear sentence}}
**Reasoning:** {{why this over the alternatives}}
**Impact:** {{what changes as a result}}
**Relates to / Supersedes:** {{DEC-xxx or none}}
**Status:** Awaiting merger
```

## proposed-hotsheet.md

```markdown
# Proposed HOTSHEET changes from [you], YYYY-MM-DD - for merger review

## Proposed Hotsheet Entry
**Date:** YYYY-MM-DD
**Proposed by:** [you]
**Source:** {{where this came from}}
**Type:** Blocking | Needs Attention | Watching | Resolved
**Summary:** {{one line}}
**Key Points:**
- {{point}}

**Decisions Made:**
| Decision | Owner | Date |
|----------|-------|------|

**Action Items:**
| Item | Owner | Due |
|------|-------|-----|
```

## proposed-risks.md

```markdown
# Proposed risk register change from [you], YYYY-MM-DD - for merger review

## Proposed Risk
**Date:** YYYY-MM-DD
**Proposed by:** [you]
**Risk:** {{what could go wrong}}
**Likelihood:** Low | Medium | High
**Impact:** Low | Medium | High
**Mitigation:** {{action}}
**Owner:** {{who}}
**Status:** ACTIVE | ACTIVE (in-flight) | RESOLVED
```

## proposed-project-index.md

```markdown
# Proposed PROJECT_INDEX refresh from [you], YYYY-MM-DD - for merger review

## Proposed PROJECT_INDEX Update
**Date:** YYYY-MM-DD
**Proposed by:** [you]
**Section to update:** {{section}}
**Current text:** {{what is there now}}
**Proposed text:** {{what it should say}}
**Reason:** {{why}}
```

## suggestions/suggestion-[topic].md

```markdown
## Suggestion
**Date:** YYYY-MM-DD
**From:** [you]
**Target path:** {{the owned folder / file}}
**Suggestion:** {{what you propose}}
**Priority:** Low | Medium | High
```
