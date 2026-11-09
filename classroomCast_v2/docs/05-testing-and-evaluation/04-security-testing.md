# Security testing

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Authorization and test scope

Run tests only within the approved classroom/network test scope. Use synthetic users and secrets. Product security results are Not run; this document defines the review plan.

## 2. Scenario matrix

| Test group | Positive control | Negative/abuse scenario | Expected result |
|---|---|---|---|
| TC-AUTH | Owning teacher controls own class | Student/SYS-only/other teacher uses same endpoint | Deny without state change or unauthorized data |
| TC-NAC16 | Scoped administrator changes approved profile | Out-of-scope mutation or teacher arbitrary network edit | Deny and audit |
| TC-S03/S06 | Admitted subscriber receives media | Expired/forged/revoked grants; reconnect after removal/end | No unauthorized subscription/refresh |
| TC-ADM05/06 | Eligible pending request approved | Concurrent final seat; block/close while pending | Atomic allocation; stale request does not bypass checks |
| TC-NAC17 | Server uses test secret | Search client bundles, responses, exports and logs for marker | No secret disclosure |
| TC-NAC18 | Restrictive profile preserves local paths | Rule conflicts with required local names/control/media | Reject unsafe configuration or report failure safely |
| TC-NAC06/12/13 | Restore owned changes | External IT edit, partial apply, restart, unreachable service | Reconcile, preserve unrelated changes, no false restored status |
| TC-NAC19 | Minimal audit fields retained | Unexpected browsing histories or excessive identifiers | Remove/limit collection; match approved D13 |
| TC-CTRL01/02 | Current control operation succeeds | Stale publication version, mismatched reused operation ID | No replay or resurrection |

## 3. Evidence and reporting

Record endpoint/action, authenticated role, class/scope, pre-state, request, observed effect, sanitized evidence and expected denial. UI button visibility is not a security test. Separate finding severity, affected requirement, fix owner, retest and release disposition. Never publish real credentials in the report.

## 4. Limitations

Domain-control tests do not certify whole-device restrictions. Record bypass conditions and accepted limitations with the network owner. No compliance certification, penetration-test completion or browser support certification is implied.
