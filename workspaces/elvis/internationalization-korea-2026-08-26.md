# Internationalization (English/Korean) and Korea-specific operating concerns

> Elvis workspace working file, started and mostly resolved 2026-08-26. Covers language handling for
> launch and Korea-market-specific technical/legal/business adjustments, grounded in current research,
> not assumed from training data alone. Sources cited inline.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

WePop launches in Korea, to Korean users, but also has an international community in Korea and a small
number of US-based users. Elvis's own framing: at minimum, English and Korean need to work at launch.
Separately, whether anything needs adjusting for the app to work properly in Korea specifically, both
language and non-language concerns.

## Language architecture, RESOLVED 2026-08-26: full i18n from day one, on-demand UGC translation deferred

**App interface (chrome, navigation, system messages, push notifications), RESOLVED:** needs full
translation in both languages, which requires an internationalization architecture with externalized,
translatable strings built in from day one. Retrofitting this into a codebase not built for it is a real
and painful project, not a quick pass, worth a firm day-1 flag for Deepak even though it produces no
visible feature on its own.

**User-generated content (event titles/descriptions, moment captions, chat messages), RESOLVED: on-demand
translation deferred to a later phase, not launch.** A host does not write bilingually, and the standard
pattern for this (an on-demand "see translation" tap on a piece of content, Instagram/Facebook-style,
machine-translated only when requested) is real and worth building eventually, but Elvis chose to defer
it rather than scope it for launch. UI/system translation still ships at launch regardless, this deferral
is specifically about translating other people's content, not the app itself.

**Bilingual tag vocabulary, RESOLVED:** the DEC-005 tag list needs each tag to carry both an English and
a Korean display label under one canonical tag ID, so a Korean host tagging an event and an
English-speaking user browsing hit the same underlying tag for exact-match purposes, not two
disconnected tags in two languages.

**Name field structure, RESOLVED:** onboarding should not assume a rigid Western first-name/last-name
split. Korean naming convention puts family name first with no middle name, a single flexible full-name
field is safer than a fixed two-field structure.

**Multilingual embeddings, noted:** modern text embedding models (see `recommendation-algorithm-
2026-08-25.md`) are generally multilingual and should provide reasonable semantic matching across
languages even without full UGC translation, worth testing once built, not assumed as guaranteed
quality.

**Moderation, flagged, connects to an existing HOTSHEET blocking item:** the content moderation staffing
gap already on the HOTSHEET (anonymous host-rating comments, moment comments, DM/group chat, Free Now
rooms) now needs explicit Korean-language moderation capability, not just English-language coverage,
for the Korea launch. This compounds the existing blocker, it does not replace it.

## Korea-specific concerns, grounded in current research

### Payments, ESCALATED 2026-08-26: a real gap in DEC-010's existing plan

DEC-010 commits to using Programination's existing Stripe account for payments. Checking Stripe's own
documentation for Korea coverage did not confirm whether a Korea-based merchant relationship, KRW payouts,
or Korean local payment methods (KakaoPay, Naver Pay, direct bank transfer/virtual account, all strongly
preferred by Korean consumers over card payment) are actually supported the way the org tier's Korean
customers would need. Korea has established local payment processors built specifically for this (Toss
Payments, NHN KCP, and PortOne, formerly Iamport, are the standard names), worth evaluating alongside or
instead of Stripe for the Korea market.

**Elvis's decision, RESOLVED:** flag to Aakash now rather than hold for the already-planned dedicated
payments conversation, since this touches an already-landed decision and Korea is the launch market, not
a future expansion market. Filed as `workspaces/elvis/proposed-hotsheet.md` for the merger, since
financials and payments sit with Aakash per OWNERS.md.

### Age verification, strengthens an already-provisional decision

DEC-012 currently plans a self-declared birthdate with no ID verification in phase 1, explicitly marked
provisional pending legal counsel (TASK-013). Checking how a comparable app (Bumble, a close analog on
social verification needs) actually handles Korea specifically: it requires an actual government-issued
photo ID, with a custom flow where the user self-redacts their ID number but leaves name, date of birth,
photo, and expiry visible, reviewed by trained human reviewers, not automated facial recognition or
biometrics. That is meaningfully stronger than self-declaration, real evidence the DEC-012 provisional
flag was the right call. Worth bringing directly into the TASK-013 legal consultation, not treated as a
new, separate question, since it is the same open item with better grounding now.

### Identity verification infrastructure, RESOLVED 2026-08-26: plan for Korea's carrier-based verification

Korea has a formalized, government-recognized identity verification system: three designated mobile
carriers and seven credit card companies serve as official verification agencies, and carrier-based
verification (commonly delivered through a system called PASS) is the standard mechanism Korean users
already expect for age and identity checks, distinct from a generic SMS OTP.

**Elvis's decision, RESOLVED:** plan to use Korea's standard carrier-based verification for Korean users
instead of generic SMS OTP, subject to final confirmation from the TASK-013 legal consult. Reasoning
beyond legal alignment: it is what Korean users already trust and expect, and because it is tied to real
identity rather than just a phone number, it meaningfully strengthens the one-account-per-user
anti-gaming approach from `recommendation-algorithm-2026-08-25.md`'s robustness section, for Korean
users specifically this effectively delivers the eventual ID-verification step early, as a natural
byproduct of using the standard local verification flow, rather than as separate future work.

### Determining Korea vs elsewhere, RESOLVED 2026-08-26: four separate signals, not one detection mechanism

Elvis's question: how do we best determine whether a user is in Korea versus elsewhere, since that
determination would drive timezone, language, the PASS flow, and payment method. The framing of "detect
whether the user is in Korea" is the wrong problem shape. Each of those four things has its own natural
signal already available, and none of them require building a new location-detection mechanism. Introducing
one would also cut against DEC-012 and DEC-016's existing stance of no forced GPS and no continuous
re-checking of a user's location as they travel.

**Timezone, RESOLVED 2026-08-26 (confirmed with a settings override):** default from the device OS's own
timezone API, dynamic by nature, a user who flies from Seoul to New York should see event times in their
new local timezone immediately with no separate detection logic and no stored "home country" concept
involved. Elvis confirmed device detection as the default, plus a manual settings-level override so a user
can pin a different timezone if the automatic read is not what they want (traveling but still tracking home
events, a device with an incorrect system timezone, and similar cases).

**Language, RESOLVED 2026-08-26 (confirmed):** default from the device locale at first launch, then a
manual setting the user can override at any time. This is a preference, not a detection problem. A
Korean-fluent international user in Seoul and a Korean user visiting the US both just pick what they want
to read in. Elvis confirmed this device-default-plus-override approach for language as well.

**PASS eligibility, RESOLVED:** check the phone number's own carrier country code directly, not DEC-012's
full blended legal-country value (self-declared birthdate plus store region plus device location plus phone
country code, set once at signup). This reuses one leg of that existing cascade rather than introducing
anything new, and is framed correctly as a capability check ("can this specific phone number complete
Korea's carrier-based verification"), not a location or identity question. A user with a Korean phone number
gets the PASS-style flow regardless of where they currently are; a user without one does not, regardless of
where they currently are.

**Fallback for Korea-based users without a Korean phone number, RESOLVED:** offer a redacted-ID fallback
path, following Bumble's actual Korea flow already researched above (government-issued photo ID, user
self-redacts the ID number, name/date of birth/photo/expiry stay visible, reviewed by a trained human
reviewer, no facial recognition or biometrics). This covers the international-in-Korea and visiting-friend
cases in DEC-012's own scope without requiring a Korean phone number as a hard gate.

**Payment method options, RESOLVED:** driven by the org's own billing details and payment instrument on
file, not by the physical location of whoever is browsing. An org set up for the Korea market shows Korea
payment options to everyone who views its listings; this is a property of the org, not a per-viewer
location check.

**Net result:** there is no single "is this user in Korea" flag anywhere in the system. Four independent,
already-available signals each answer their own question directly, and the two device-read signals
(timezone, language) both come with a settings-level manual override so device detection is a sensible
default, not a hard lock. This is simpler to build, avoids a new privacy surface, and does not need to be
kept in sync with a user's actual physical location over time.

### PIPA (Personal Information Protection Act), specifics beyond the general disclosure already flagged

Three concrete points worth folding into the TASK-013 legal consult, beyond the general
privacy-policy-disclosure item already flagged for the recommendation engine's behavioral inference:

- Consent must clearly separate essential data use from optional/marketing use, not one blended consent.
- Cross-border data transfer accountability is broader than server location. Even remote access to
  Korean user data by a team member not based in Korea counts as a transfer requiring documentation,
  worth knowing given how this team and any infrastructure or AI vendors are structured.
- PIPA has specific pseudonymization standards (Article 28-2) for analytics use, which applies directly
  to the hidden internal keyword and embedding layer already designed in
  `recommendation-algorithm-2026-08-25.md`. That system needs to be built with this standard in mind for
  Korean users specifically, not covered by a generic policy mention alone.

## Not yet decided, deliberately parked

- Exact scope and timeline for adopting Korea's carrier-based verification, pending the TASK-013 legal
  consult's actual findings, direction only confirmed here, not implementation detail.
- Whether a Korea-specific payment processor gets added alongside Stripe or used instead of it for
  Korean transactions, pending Aakash's response to the payments escalation.
- Whether Naver login should join Kakao (already in DEC-011) as a second Korean social-login option, not
  raised as a real gap, just not evaluated in this pass.
- On-demand UGC translation remains real, useful, deferred work, not designed further here since it was
  explicitly pushed to a later phase.
- Exact review process and staffing for the redacted-ID fallback path (who reviews, turnaround time, tooling)
  is not designed here, only the flow itself is confirmed.

## Flags for Deepak, implementation, not decided here

- i18n architecture (externalized, translatable strings) is a day-1, ground-floor requirement, not
  retrofittable cheaply later.
- Tag vocabulary needs a canonical-tag-ID-plus-per-language-label data model, not two separate
  vocabularies.
- Name field should be a single flexible full-name field, not a fixed first/last split.
- Korea's carrier-based verification (PASS-style) needs its own integration, distinct from the generic
  SMS OTP flow already planned per DEC-011, once TASK-013 confirms the requirement.
- The hidden internal keyword/embedding layer needs Korea-specific pseudonymization handling per PIPA
  Article 28-2, not just the general privacy-policy disclosure already flagged.
- No new "is user in Korea" flag or location-detection service should be built. Timezone reads from the
  device OS API live and language seeds from device locale, both need a settings-screen manual override
  control, not just a one-time default; PASS eligibility is a direct check against the phone number's own
  carrier country code (reusing one leg of DEC-012's cascade, not the blended value); payment options are
  a property of the org's billing setup, not the viewer. The redacted-ID fallback flow needs its own review
  queue and reviewer tooling, similar in shape to Bumble's manual ID check process.

## Sources

- [How to accept payments in South Korea | Stripe](https://stripe.com/resources/more/payments-in-south-korea)
- [Accept South Korean payment methods Payments | Stripe](https://stripe.com/payment-method/korea)
- [Age Verification in South Korea (Manual ID Check Process) - Bumble Support](https://support.bumble.com/hc/en-us/articles/32118920328989-Age-Verification-in-South-Korea-Manual-ID-Check-Process)
- [South Korea's Approach to Age Assurance | TechPolicy.Press](https://www.techpolicy.press/south-koreas-approach-to-age-assurance/)
- [Korea PIPA Compliance in 2026: Cross-Border Data and New Duties | Korea Business Hub](https://www.koreabusinesshub.kr/blog/pipa-compliance-cross-border-data-2026)
- [South Korea PIPA: Complete Privacy Information Protection Act Guide for SaaS](https://complydog.com/blog/south-korea-pipa-privacy-information-protection-act-saas)
