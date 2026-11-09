# Security design

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Assets and trust boundaries

Protect teacher publication authority, student admission/media access, application accounts, network credentials, policy baselines and minimal audit data. Boundaries include browser-to-backend, browser-to-SFU, backend-to-enforcement adapter, operational storage and campus infrastructure ownership. A role assignment cannot replace network-owner permission.

## 2. Threat and control mapping

| Threat | Proposed control | Verification |
|---|---|---|
| Cross-class control or roster disclosure | Server-side role plus ownership checks | TC-AUTH, TC-T06 |
| Subscriber publishes or stale participant reconnects | Scoped grants, current admission, revocation/refresh checks | TC-S03, TC-S06, TC-AUTH |
| Concurrent seat approval or stale action | Atomic transition and operation/version checks | TC-ADM05/06; F07/F08 race tests |
| Secret leakage | Protected server config; redacted logs/exports/client responses | TC-NAC17, TC-PRIVACY |
| Unauthorized network changes | Explicit scope authority, validated rules, protected local paths | TC-NAC16/18 |
| Unsafe restore overwrites IT changes | Owned-change tracking, read-back, conflict reconciliation | TC-NAC06/12/13 |
| Misleading restriction status | Affected-client verification; scope/time/limitations displayed | TC-NAC10 |
| Excessive browsing/identity retention | Data minimization and agreed deletion/access rules | TC-NAC19, D13 |

## 3. Capture and transport

User consent to browser capture is independent of application authorization. Local trusted secure endpoints and supported media paths must be tested. Do not count bypassed certificate checks as a passing deployment. Student mute/fullscreen is local playback control, not teacher publication authority.

## 4. Incident and recovery procedure proposal

Identify affected scope, restrict unauthorized operations, preserve minimal diagnostic evidence, notify authorized operator, revoke/rotate affected credentials where necessary, reconcile state and retest access. Do not restart all services or reset campus rules indiscriminately. F15 records unresolved recovery and next action. Operational ownership and secret-rotation/retention details remain pending.

## 5. Enforcement limits

DNS/gateway integration controls supported paths only. Alternate resolvers, encrypted DNS, VPNs, direct IP or offline tools may bypass domain-only restrictions. Test and report limitations; do not claim device lockdown. Stronger controls require explicit supported integration and authorization, not hidden new scope.
