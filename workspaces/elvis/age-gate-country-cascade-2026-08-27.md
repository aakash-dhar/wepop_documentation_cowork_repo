# Age gate and country cascade, research input for TASK-013

> Elvis workspace working file. Not a decision, not a revision to DEC-012. DEC-012 stays ACTIVE and
> provisional exactly as landed; this file is background research to hand to counsel (TASK-013: "Consult
> a lawyer on the age/location logic") plus one flagged reasoning error in DEC-012's own text. Nothing
> here changes scope or unblocks TASK-020 (build the age gate and country cascade) on its own.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## What DEC-012 currently says

Self-declared birthdate, typed once, locked at signup, correctable only via support with a ToS ban if
falsified. No ID verification in phase 1. Country determined once at registration via a fallback cascade
(app store region first, then device location only if already granted, then phone number country code),
set permanently, never re-checked as the user travels. Per-country age thresholds live in a config table.
Reasoning given: "Legal age differs by country (US 18, Korea 19, Germany 16)." Provisional pending counsel
per TASK-013.

## Flag 1: DEC-012's own reasoning mixes two different legal concepts under "Germany 16"

"US 18, Korea 19, Germany 16" is written as if all three numbers answer the same question. They don't.
US 18 and Korea 19 are ages of majority (the legal capacity to act as an adult generally). Germany's 16 is
almost certainly GDPR's digital-consent age (the age at which a minor can consent to online data
processing without a parent), which the EU sets at a default of 16 but lets each member state lower to as
low as 13. Germany's actual age of majority is 18, same as the US.

Age of majority and GDPR digital-consent age are separate legal questions that happen to share a number in
some countries and diverge in others. For a data-processing-only feature (say, an ML recommendation
feature or a marketing email), the GDPR number is arguably the relevant one. For WePop specifically, the
age gate governs something else: whether a person is old enough to independently agree to meet strangers
in person at real-world events. That reads much closer to age of majority, or a country's own
locally-set social/contact minimum, than to a data-processing consent threshold. Right now the per-country
config table DEC-012 calls for has no documented method for choosing which of these two concepts, or some
third country-specific minimum, each entry should use. That's a real gap for counsel to close, not
something to guess at in engineering.

**Recommendation carried forward from the earlier discussion:** where a country's age-of-majority and
digital-consent figures diverge, default the config table to the stricter (higher) of the two until
counsel gives a country-specific answer, rather than defaulting to whichever number is easiest to source.
Cheap to implement (one comparison per config-table entry) and fails safe in the direction of doing less
harm if wrong.

## Flag 2: the industry landscape behind the "store-region cascade" pattern has moved

DEC-012's cascade (app store region, then device location if already granted, then phone country code) is
Wepop's own invention for solving "which country's age rule applies," built from first principles rather
than from a platform-native mechanism, because at the time no such mechanism was assumed. That's worth
revisiting before counsel finalizes anything, since two different playbooks have emerged elsewhere and
neither is what DEC-012 assumes:

**Apple's Declared Age Range API** is a first-class OS-level answer to exactly this problem, expanded
again in February 2026 to cover new national and state-level age-assurance laws (Brazil, Australia, and
Singapore requiring 18+ apps to block unverified users as of February 24, 2026; Utah and Louisiana
requiring age-sharing for new accounts starting May and July 2026 respectively). Instead of an app
inventing its own country-guessing cascade, the OS tells the app the user's age bracket (shared only with
parent/guardian consent; no birthdate collected by the app) plus a signal about which regulatory regime
applies and how the age was assured, tied to the Apple Account's own creation region and jurisdiction, not
app-store region used as a separate proxy. That's a materially different model from DEC-012's
"store-region-first, GPS-second, phone-code-third" cascade: it shifts jurisdiction determination to the
platform rather than having each app reconstruct it from indirect signals.

**Discord went the opposite direction**: global, mandatory AI-based age verification (facial-age-inference
plus an optional video selfie or ID upload, no stored biometrics on their end) rather than trusting
self-declaration at all, explicitly to get ahead of tightening regulation in the EU, UK, Australia, Canada,
and New Zealand.

The self-declared-birthdate part of DEC-012 is still a reasonable phase-1 baseline; that piece isn't
unusual and doesn't need to change on this alone. What's dated is the country-determination mechanism
sitting underneath it. Worth putting three real questions to counsel rather than assuming an answer:

1. Does relying on a self-built store-region/GPS/phone-code cascade, instead of a platform-native signal
   like Apple's Declared Age Range API, create any additional compliance exposure in the jurisdictions
   above, given that Apple's mechanism now exists specifically to answer this?
2. Do any of Wepop's target or likely-early markets (Korea and the US are the named focus markets in
   DEC-002/DEC-012; add Brazil, Australia, Singapore, Utah, or Louisiana if those are plausible early
   markets) fall under the new laws Apple's February 2026 update targets, such that self-declaration alone
   would be insufficient regardless of the cascade mechanism?
3. Given WePop's real-world in-person nature, should the config table's per-country threshold be sourced
   from age of majority, a locally-set social/contact minimum, or GDPR-style digital consent age, per Flag
   1 above, and does that answer change depending on which of the above laws apply?

## What this does not change

- DEC-012 stays ACTIVE and provisional, unchanged, pending TASK-013.
- TASK-020 (build the age gate and country cascade) stays To Do; this file is input to counsel, not a
  build unblock.
- No scope-matrix or DECISIONS.md edit accompanies this file. If counsel's answer changes the mechanism
  DEC-012 specifies, that becomes a new decision (DEC-012 revision or a superseding DEC) at that time, not
  an edit made here ahead of the actual answer.

## Sources

- [Age requirements for apps distributed in Brazil, Australia, Singapore, Utah, and Louisiana - Apple Developer](https://developer.apple.com/news/?id=f5zj08ey)
- [Apple updates Declared Age Range API for national, state-level age assurance laws - Biometric Update](https://www.biometricupdate.com/202602/apple-updates-declared-age-range-api-for-national-state-level-age-assurance-laws)
- [Region-specific rules for managing an Apple Account - Apple Support](https://support.apple.com/en-us/125666)
- [Discord to Roll Out Global Age Verification Using Facial Scans, ID - TechRepublic](https://www.techrepublic.com/article/news-discord-global-age-verification-teens/)
- [GDPR Age of "Digital" Consent - PRIVO](https://www.privo.com/blog/gdpr-age-of-digital-consent)
