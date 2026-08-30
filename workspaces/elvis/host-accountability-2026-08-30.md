# Host accountability: reputation, enforcement, account deletion, and the org loophole

> Elvis workspace working file, 2026-08-30. Started as a single flagged question inside
> `event-schedule-2026-08-25.md` (do a detached host's ratings stay on their record) and grew into its own
> topic once three real escape routes turned up. Grounded in research into Korean practice rather than
> assumption; sources cited at the bottom.
>
> No em-dashes. Governance values ALLOW / BLOCK / ESCALATE.

## Problem

Elvis's principle, stated 2026-08-30: accountability matters and we do not want people to find loopholes.
Three routes for a host to escape a bad record were closed the same day (deleting a completed event,
detaching from one, and deleting an event to launder its ratings). Three more were open: statutory erasure,
account deletion and re-registration, and hosting through disposable org accounts.

The mistake to avoid is treating all of this as one problem. It is two, with different legal footing.

## The load-bearing split: reputation is not enforcement

**This is the architectural decision everything else follows from**, and it came out of looking at how
Danggeun (당근) actually handles it rather than reasoning from first principles.

| | Reputation | Enforcement |
|---|---|---|
| What it is | Host ratings, the public track record | Ban and suspension records |
| Legally | Personal data *about* the host | Fraud-prevention record |
| On account deletion | Dies with the account | Survives it |
| Basis for retention | None needed, it is deleted | Privacy-policy disclosure, purpose-limited |

Trying to make one object do both jobs is what creates the conflict between accountability and PIPA. Split
them and both work.

Danggeun does exactly this. 매너온도 is attached to the account and disappears when a user withdraws, so
they never have to defend retaining it. What survives is the enforcement record: their own rules state that
동일한 환경에서 탈퇴 후 재가입한 경우 기존 이용정지 내용이 새 계정에도 적용될 수 있다, existing
suspensions may carry over to a new account created in the same environment. The score dies; the ban does
not.

**Elvis's decision 2026-08-30: follow Danggeun's handling, but not their scoring scheme.** WePop keeps
DEC-014's 0-5 star ratings on events and hosts. The 0-1,000 Karrot Score is explicitly not adopted.

**Scope note, so this is not read as reversing an earlier decision.** Ratings still persist through *event*
deletion and through *detachment*, both decided 2026-08-30 and unchanged. What dies is ratings on *account*
deletion. Those are different events and the distinction is deliberate: deleting an event is an action a
host takes against a record; deleting an account is a data-subject exercising a right over their own
personal data.

**Worth knowing, on the score design itself:** Danggeun is moving off 매너온도 toward a Karrot Score
partly because scores below 50 made *new* users look untrustworthy. That is the same cold-start failure the
2026-08-29 feedback proposal already guards against with a minimum of 3 verified ratings before any public
average displays, plus Bayesian smoothing toward the global mean. Independent validation that the naive
version of this bites in production.

## Account deletion and re-registration, RESOLVED 2026-08-30

- **Re-registration is allowed.** Elvis's call, matching Danggeun.
- **A cooldown applies.** Danggeun uses 7 days. Number not fixed here; the mechanism is the decision.
- **The ban list is checked at signup.** This is what makes allowing re-registration safe.
- Ratings do not survive account deletion, per the split above.

### The ban list, mechanism

- **Store a hashed identifier, not a readable roster.** Hash the phone number, plus device and environment
  signals. A signup can be checked against the list without WePop ever holding a browsable directory of
  banned people, which is both better privacy practice and a smaller breach surface.
- **Retain only the ban reason and date alongside it.** Minimum necessary.
- **A better key already exists for Korean users.** DEC-026's PASS verification returns CI (연계정보), a
  per-person identifier that persists across phone-number changes. A phone number can be swapped; a CI
  cannot. For Korean users this makes the ban list meaningfully harder to evade. CI carries its own PIPA
  handling obligations, already flagged in `internationalization-korea-2026-08-26.md`, so this is a real
  asset with real strings attached.
- **Device and environment signals cover users without a Korean number**, which is Danggeun's own fallback.

### The legal basis, and why it is not the obvious one

PIPA Article 36(1) grants a correction and deletion right with a narrow proviso: deletion cannot be demanded
where **another law** specifies that data as a collection target. That proviso does **not** reach "we want to
keep it for accountability," so it is not the basis for a ban list.

The basis Korean platforms actually use is a disclosed 부정이용 방지 retention item in the privacy policy,
with a stated period, under 회사 내부 방침. Concrete precedent: JobKorea's privacy policy states 회사
내부 방침에 의해 부정이용 등에 관한 기록은 5년간 보관합니다, abuse records retained five years. The
GDPR analogue usually cited is the "establishment, exercise or defence of legal claims" exemption.

**ESCALATE to DLG, not resolved here.** This retention rests on disclosure and purpose limitation rather
than on a statutory carve-out, so it needs counsel sign-off rather than a design decision. It belongs in the
legal-register consult already proposed 2026-08-30, and it interacts with L-1 (peer affinity records are
personal data about the rated user) and L-10 (data retention and deletion policy).

## The organization loophole, RESOLVED 2026-08-30

**The reframe that made this tractable.** The problem was never that multiple orgs exist. It is that
enforcement does not travel along a link that already exists:
`recommendation-algorithm-2026-08-25.md` already requires org accounts to be traceable to a specific user.
The traceability is built and no consequence flows down it. Fix that and most of the hole closes without
caps or public exposure.

### Adopted

**1. Enforcement propagates.** Suspend an individual and the orgs they operate are suspended too. This is
Danggeun's carryover principle applied internally, it is the actual teeth, and it costs nothing new because
the link already exists.

**2. Admins see every org a user operates.** Free, already traceable, closes the moderation blind spot with
zero public exposure.

**3. Org creation is gated on standing, not rating.** Elvis's own suggestion, revised. A *rating* threshold
would block brand-new users, which is precisely the launch market: university club officers with no history
yet. Gate instead on no active suspensions plus a minimum account age. Blocks known bad actors without
punishing newcomers, and avoids the cold-start trap Danggeun ran into from the other direction.

**4. A suspended admin may transfer their admin role to another org member.** Elvis's addition, and the
reasoning is sound: a 40-member club should not die because one officer misbehaved. It also reuses
machinery DEC-024 already put in phase 1, org ownership transfer, built for officer turnover.

### The evasion that addition opens, and how to close it

Left unqualified, rule 4 undoes rule 1. A bad actor plants an accomplice (or a second account they control)
as an org member, gets suspended, transfers admin to them, and keeps de facto control of the org. Three
qualifications, none expensive:

- **The transfer target must have standing themselves**, no active suspensions. Otherwise the org passes
  between two suspended accounts.
- **The target must have been a member before the suspension**, with a minimum tenure. This is the one that
  actually closes it: without it, an accomplice can be added at the moment of suspension.
- **A suspension-triggered transfer is reviewed by an admin, not self-serve.** Normal ownership transfer
  under DEC-024 (officer graduating) stays routine. A transfer occurring *because* its owner was just
  suspended is not routine and should not use the routine path.

Two consequences worth stating rather than leaving to implementation:

- **The suspended individual loses org access entirely, not just the admin title.** Stripping the role while
  leaving them as a regular member who can still post and create events under the org would make the
  suspension largely cosmetic in the context that matters most.
- **A single-member org has nobody to transfer to and stays suspended.** Correct outcome, worth stating so
  it is not treated as a bug.

### Rejected, with reasons recorded

- **A cap on org accounts per user.** Blunt: people legitimately run several clubs, and a cap of N just
  means a bad actor uses N. Raises cost slightly, closes nothing. Elvis: not for now.
- **Publicly showing all connected profiles of a person.** The most effective option and the most dangerous.
  It fights DEC-006 and DEC-017 head-on, which exist to limit what a stranger learns by browsing, and a
  public list of every account a person operates is a real deanonymization surface. Concretely: someone
  running an org for an LGBTQ+ student group and another for a church group could be outed by the linkage
  alone. Elvis: not for now. If it is ever revisited, it should be opt-in as a credibility signal a host
  chooses to show, never a forced disclosure.

## Flags for Deepak

- The ban list is a hashed-identifier lookup at signup, not a stored roster. Phone hash plus device and
  environment signals, with CI as the strong key for Korean users once PASS is integrated per DEC-026.
- Suspension propagation walks the existing org-traceability link. No new data model, a new consequence on
  an existing one.
- Suspension-triggered admin transfer is a distinct path from DEC-024's routine ownership transfer, with
  eligibility checks (target standing, target tenure predating the suspension) and admin review. Do not
  reuse the routine path with a flag.
- A suspended user is removed from org access entirely, not merely demoted from admin.
- Ratings are deleted on account deletion. Note this cuts against the denormalization required elsewhere
  (ratings must survive *event* deletion, per the 2026-08-30 completed-event decision), so the deletion path
  has to distinguish the two cases rather than treating any orphaned rating as garbage to collect.

## Escalations for DLG, via the legal-register consult

- Whether a disclosed 부정이용 방지 retention item supports a ban list surviving an erasure request, and
  what retention period is defensible. JobKorea's five years is precedent, not authority.
- Whether retaining a hashed identifier changes the analysis versus retaining the raw value.
- CI (연계정보) handling obligations if CI becomes the ban-list key.
- Interacts with L-1 and L-10 already on the register.

## Not decided here

- The re-registration cooldown period. Danggeun uses 7 days; WePop's number is unset.
- The ban-list retention period.
- Minimum account age for org creation, and minimum member tenure for a suspension-triggered transfer.
- Whether suspension propagation is automatic or a reviewer decision per org. Automatic is simpler and is
  the assumption above, but a reviewer may want to spare an org whose suspended admin was a minor
  contributor.
- Whether an org suspended by propagation is restored automatically when a valid transfer completes, or
  requires a separate reinstatement.

## Sources

- [개인정보의 열람 및 정정·삭제 요구, 찾기쉬운 생활법령정보 (PIPA Art. 36)](https://www.easylaw.go.kr/CSP/CnpClsMainBtr.laf?popMenu=ov&csmSeq=1702&ccfNo=1&cciNo=2&cnpClsNo=2)
- [South Korea Personal Information Protection Act (PIPA), Securiti](https://securiti.ai/south-korea-personal-information-protection-act/)
- [당근마켓 탈퇴 후 재가입 방법과 7일 제한, 같은 번호 재가입 주의사항](https://jab-guyver.co.kr/3195)
- [당근이 매너온도를 포기한 이유, 36.5도의 비밀과 Karrot Score](https://redbusbagman.com/karrotuxresearch/)
- [잡코리아 개인정보처리방침 (부정이용 기록 5년 보관)](https://m.jobkorea.co.kr/Service_JK/privacy.asp)
- [Right to erasure, ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-erasure/)
