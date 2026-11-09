# Testing strategy

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Objectives and evidence status

Verify source requirements, permissions, local runtime, media behavior and safe policy recovery. All product tests in this package are **Not run**; they are specifications for later execution. Documentation checks are reported separately in the validation report.

## 2. Test levels

| Level | Focus | Example evidence |
|---|---|---|
| Business-rule tests | Validation, transitions, idempotency, seat allocation | Concurrent last-seat approval; stale operation rejected |
| Component integration | API/database/SFU/adapter boundaries | Scoped grants, accepted-versus-verified policy result |
| End-to-end | Teacher/student/admin workflows | F01/F05/F06/F07/F08/F10/F13 outcomes |
| Fault/recovery | Isolated component failures and restart | Durable operations, truthful unresolved states, safe reconciliation |
| Performance | Declared physical/simulated loads and media quality | Raw timestamp samples, client metrics, server/AP topology |
| Security | Role/scope/media and secret boundaries | Denied cross-class calls, revoked subscriber, secret inspection |
| User acceptance | Teacher task completion and required results | Signed or pending disposition per requirement |

## 3. Entry criteria

Approved test scope and network authority; isolated/safe fixtures; declared build, configuration and browser/OS; known baseline and recovery plan; agreed acceptance targets or explicit exploratory label. Use synthetic identities and test domains; do not collect real student browsing history as a test shortcut.

## 4. Exit criteria

Execute all agreed required tests; link evidence to requirements/stories; triage defects and rerun affected scenarios after changes; report optional omissions and scope gaps. Release blockers follow Definition of Done. Teacher acceptance is separately recorded, with any exceptions and their authority.

## 5. Execution and defect record

Test ID, requirement, story, build, config, environment, tester, timestamp, preconditions, steps, expected result, observed result, pass/fail/blocked, evidence, defect ID, reviewer and retest reference. An unreachable dependency is a recorded blocked/failure outcome, never automatic success. Criteria approval and execution outcome occupy separate fields.
