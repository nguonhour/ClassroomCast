# Risks and mitigation

> **9 November planning update:** Latest user-provided site screenshots show three development sprints starting November 30, different task allocations, and release/presentation dates through February 3. Earlier dates/allocations below are historical proposals, not the current meeting commitment. Use the [November 10 meeting package](../meeting-2026-11-10/README.md) to review the new baseline and January 25 editing-cutoff question. Approval remains pending.

**Version:** 0.2 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

The team roster supplied by the user lists **HENG NGUON HOUR** (representative), **BUN SENGLEANG**, **CHANTHA MENGKONG**, **HAK SENGKEA**, and **HONG DYHENGMESA**. Full roster names are used below. Risk assignments remain proposed; this revision corrects naming without reallocating responsibilities.

## 1. Inherited risk register

Scores are provisional ordinal judgments (probability/impact 1–5), not measured probabilities. Review each sprint; score ≥12 or impact 5 merits active escalation. Historical response dates in the old plan need current follow-up.

| ID | Cause → event → effect | P/I | Proposed risk owner | Prevention, trigger and fallback |
|---|---|---|---|---|
| R01 | Campus control access unknown → integration unavailable → campus enforcement cannot be accepted | 4/5 | CHANTHA MENGKONG | Obtain IT decision in Sprint 1; trigger: no workable path by 13 Nov; use authorized portable network for development and escalate campus gap |
| R02 | High viewer density → Wi-Fi saturation → freezes and capacity failure | 4/5 | CHANTHA MENGKONG | Wired server, staged tests and measured AP placement; trigger: loss/delay above targets at next load stage; lower agreed media profile/add APs or seek scope decision |
| R03 | Laptop trust provisioning unknown → screen/SFU connection fails → offline demo blocked | 3/5 | CHANTHA MENGKONG | Two-laptop HTTPS test in Sprint 1; trigger: untrusted endpoint; obtain campus trusted cert/name or agreed trust provisioning and retest |
| R04 | Policies span sessions/process restarts → incomplete restore → network remains restricted | 3/5 | HONG DYHENGMESA | Durable lease/snapshot, idempotent recovery worker and restore drill; trigger: rules differ after end/expiry; emergency restore with visible failure and operator runbook |
| R05 | DNS bypass is possible → users reach restricted services → enforcement overstated | 4/4 | CHANTHA MENGKONG | Agree DNS scope/limitations; test alternate resolver/VPN cases on lab equipment; stronger authorized gateway/device controls or accepted limitation |
| R06 | Audio varies by platform → expected source unavailable → media acceptance fails | 3/3 | CHANTHA MENGKONG | Publish compatibility matrix early; trigger: missing required audio source; agree supported combination and explicit fallback |
| R07 | Initial work exceeds available hours → delivery slips → Must scope incomplete | 4/5 | HENG NGUON HOUR | Refine estimate and actual calendar by 15 Nov; trigger: forecast above remaining capacity; defer Should/Could and obtain explicit Must trade-off decision |
| R08 | Privileged credentials or tokens mishandled → unauthorized control → demo/data compromised | 2/5 | HENG NGUON HOUR | Server-only secrets, scoped tokens and permission tests; trigger: exposed credential or bypass; revoke/rotate and stop affected admin action until corrected |

## 2. Current additions

| ID | Cause / event / consequence | Proposed risk owner | Response and trigger |
|---|---|---|---|
| R09 | Insufficient physical devices or Wi-Fi evidence prevents demonstration of the specified 50–150 capacity | HENG NGUON HOUR | Agree D12 test conditions; plan 150-student capacity evidence and distinguish physical from simulated clients |
| R10 | School host chosen without inventory; deployment may conflict with existing workloads | CHANTHA MENGKONG | Inventory and maintenance authorization before installation |
| R11 | Repeated generated diagrams diverge from code; team implements wrong paths | BUN SENGLEANG | Review Mermaid as source; deterministic rendering; trace every failure outcome |
| R12 | Pending semantic decisions accumulate; late rework delays release | HENG NGUON HOUR / HONG DYHENGMESA | Assign D01–D20 owners; prioritize admission, authority and restoration before sprint commitment |

## 3. Issue and escalation template

Record ID, opened date, trigger observed, impact, owner, next action, due date, decision needed and evidence. An observed problem becomes an issue; do not keep calling an active failure only a risk. Network impact escalates promptly to the authorized operator. Other external blockers go through HENG NGUON HOUR under the prior one-working-day escalation proposal.

## 4. Residual risk acceptance

Teacher and network owner must explicitly accept limitations relevant to their authority. A portable demonstration does not prove campus integration. No known risk has been recorded as accepted or closed by this package.
