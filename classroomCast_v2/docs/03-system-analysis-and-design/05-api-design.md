# API and event design

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Contract status

The following endpoints come from the prior architecture sketch. They are proposed contracts, not implemented APIs. Concrete schemas, authentication mechanism, response codes and versioning require joint backend/frontend review. Host-service restart is an authorized operator procedure, not an implied web endpoint.

## 2. Existing proposed endpoint catalogue

| Action | Proposed endpoint | Permission / key behavior |
|---|---|---|
| Create class | POST /api/sessions | Teacher; generates unique active join code |
| Join class | POST /api/sessions/join | Validates code/admission and rate limits |
| Control broadcast/class | POST /api/sessions/:id/actions | Owning teacher; validates state transition |
| Admit/remove participant | POST /api/sessions/:id/participants/:pid/actions | Owning teacher; updates media access |
| Obtain room token | POST /api/sessions/:id/media-token | Admitted identity; scoped publish/subscribe grants |
| Save versioned profile | POST /api/policy-profiles | Administrator; validates rules and exceptions |
| Apply profile | POST /api/scopes/:id/policy-operations | Administrator; lease/idempotency required |
| Read enforcement | GET /api/scopes/:id/status | Authorized operator; desired and observed state |
| Emergency restore | POST /api/scopes/:id/restore | Administrator; recorded, idempotent operation |
| Diagnostics | GET /api/health | Public minimal readiness; detailed network status is restricted |

## 3. Shared request and response semantics

| Contract concern | Proposed requirement |
|---|---|
| Identity | Derive authenticated requester on server; do not trust a client-supplied role |
| Resource scope | Check class ownership/admission or explicit network scope on each request |
| Mutating intent | Include stable operation ID and relevant class/participant/profile/publication identifiers |
| Concurrency | Validate expected current state/version before mutation; return stale/conflict result truthfully |
| Idempotency | Same identity/intent returns previous result or resumes unfinished steps; mismatch denied |
| Async results | Return operation reference and pending state; later report actual result and evidence timestamp |
| Errors | Distinguish denied, invalid input, full, closed, stale, service unavailable and unresolved; no secrets |
| Media grants | Short-lived, class-scoped publish or subscribe permission; revoked access cannot refresh |
| Events | Backend-authoritative admission, participant, publication, closure and policy-status updates |

Event names and payloads are **Pending Decision**, not newly promised API features. SFU event authenticity must be checked using the selected service's documented mechanism. A notification is not proof of media revocation; backend evidence determines the state.

## 4. Example interaction contract

F08 approval: authorize requester → verify pending admission → atomically validate class/code/block/capacity → allocate seat → persist result → notify student → F05 obtains subscriber grant. A stale or denied action allocates no seat. F07 Stop: bind current publication → authorize and check closure/version → request termination → verify actual result → record stopped or unresolved; student admission remains unchanged.

## 5. Review checklist

For every endpoint agree input schema, response/error schema, caller permission, resource check, state transition, idempotency/concurrency rule, audit fields, failure path and test references. Use TC-AUTH, TC-ADM01–07 and source-specific TC IDs before freezing the contract.
