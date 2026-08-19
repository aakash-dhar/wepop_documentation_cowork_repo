# TASK-017 - Build Elvis's client-specific input skill

## Overview
Build a client-specific Cowork skill for Elvis so he can feed project information to Claude in the
structure the dev harness (Deepak's) expects, rather than free-form prompts. Raised on the
2026-08-19 setup call: Aakash is building it and it is still in progress. The goal is to make Elvis's
regular inputs faster and consistent so they land cleanly in the shared record.

## Sources
- call | 2026-08-19 Elvis setup call | comms/meeting-notes/2026-08-19_Wepop_Elvis-setup-call.md | "I'm building for you like a client-specific skill so that you can give those information off to cloud."
- decision | DEC-001 | shared/DECISIONS.md | Central repo plus Cowork harness; this skill serves that workflow.

## Activity
- 2026-08-19 | Created from the Elvis setup call. In progress on Aakash's side.

## Definition of done
- [ ] Skill scaffolded with a clear trigger and the input structure Deepak's harness expects
- [ ] Writes to Elvis's workspace / proposal path, never to shared/ directly
- [ ] Registered in README, skills/README, skills/TRIGGERS
- [ ] Walked through with Elvis so he knows the trigger

## Blockers
