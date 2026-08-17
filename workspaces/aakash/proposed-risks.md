# Proposed risk register change from aakash, 2026-08-17 - for merger review

> Source: Wepop progress walkthrough, 2026-08-17. No em-dashes. Use a lowercase x for Likelihood x Impact.

## Proposed Risk
**Date:** 2026-08-17
**Proposed by:** aakash
**Risk:** Cross-jurisdiction age verification is legally messy (US 18, Korea 19, Germany 16, travel and passive vs active location questions); locking the age/location logic before counsel could ship a non-compliant flow.
**Likelihood:** Medium
**Impact:** High
**Mitigation:** Consult a lawyer on passive vs active location capture and travel-jurisdiction handling before locking the logic; keep the country-tied approach provisional until then.
**Owner:** Aakash
**Status:** ACTIVE (in-flight)

## Proposed Risk
**Date:** 2026-08-17
**Proposed by:** aakash
**Risk:** Solo-founder blind spot: Elvis is designing Wepop alone and product/design calls may go unchallenged; he explicitly asked Aakash and Deepak to push back.
**Likelihood:** Medium
**Impact:** Medium
**Mitigation:** Aakash and Deepak provide structured critique on the design and documentation once shared; capture feedback as suggestions/proposals rather than in passing.
**Owner:** Aakash
**Status:** ACTIVE

## Proposed Risk
**Date:** 2026-08-17
**Proposed by:** aakash
**Risk:** OTP/SMS (Twilio/WhatsApp) deliverability can be blocked by geography without a registered business in that region; would break phone verification on expansion beyond US/Korea.
**Likelihood:** Low
**Impact:** Medium
**Mitigation:** Ship the optional password fallback (per the auth decision); check regional messaging-provider requirements before entering a new market.
**Owner:** Aakash
**Status:** ACTIVE
