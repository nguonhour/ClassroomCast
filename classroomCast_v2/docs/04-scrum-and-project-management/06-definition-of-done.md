# Definition of Ready and Definition of Done

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Definition of Ready — proposed working agreement

An item has a source/requirement reference, user value or technical purpose, acceptance criteria, relevant role/scope, dependencies and unresolved decisions identified, estimate, and enough UI/API detail to implement. Split items that exceed sprint capacity. Ready is a planning aid; it does not authorize campus operations.

## 2. Definition of Done — proposed release-quality agreement

1. Acceptance criteria demonstrated with build/configuration and evidence attached.
2. Peer review complete and relevant checks pass; no unresolved release-blocking defect in the delivered behavior.
3. Positive and negative permission/state/failure paths tested, including recovery when relevant.
4. UI works on agreed browser/source combinations and displays honest supported/unsupported states.
5. Required affected runtime dependencies remain local; offline test run when relevant.
6. Secrets remain server-side; relevant privacy and logging rules checked.
7. API/configuration changes and recovery guidance documented.
8. Increment integrates with the application and is usable; incomplete work earns no Done credit.

## 3. Documentation versus product completion

This documentation package can pass link, ID and Mermaid validation without any product story being Done. Requirements approval, implementation completion, test result and client acceptance must be tracked separately.

## 4. Release blockers and exceptions

Unauthorized control/media access, false enforcement/restoration success, unsafe restoration, broken required classroom flow or missing required offline behavior block release unless an explicit scope change is approved by the proper authority. Record other known limitations and agreed disposition. A Sprint Review alone is not formal acceptance.
