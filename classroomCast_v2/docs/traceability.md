# Requirements, stories, delivery items and tests

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Traceability policy

Every original requirement has one requirement-level story candidate and original test specification. CC rows are inherited delivery work, not new requirements. All rows: criteria approval Pending; implementation Not assessed; tests Not run; acceptance Pending. Coverage links do not prove test execution. Supporting architectural and administration capabilities use cross-cutting tests and source feature-card references.

## 2. Complete matrix

| Requirement | Source priority | Story | Flows | Use cases | Delivery items | Test |
|---|---|---|---|---|---|---|
| NAC01 | Must | US-NAC01 | F01 F10 | UC06 | CC-012, CC-013, CC-016, CC-018 | TC-NAC01 |
| NAC02 | Must | US-NAC02 | F09 F10 F11 | UC05 UC06 | CC-011, CC-013, CC-016, CC-018 | TC-NAC02 |
| NAC03 | Must | US-NAC03 | F09 F10 F11 | UC05 UC06 | CC-011, CC-013, CC-016, CC-018 | TC-NAC03 |
| NAC04 | Must | US-NAC04 | F09 F10 F11 | UC05 UC06 | CC-011, CC-013, CC-016, CC-018 | TC-NAC04 |
| NAC05 | Must | US-NAC05 | F01 F10 | UC06 | CC-014, CC-016, CC-018 | TC-NAC05 |
| NAC06 | Must | US-NAC06 | F13 F14 | UC08 UC09 | CC-014, CC-015, CC-016, CC-018, CC-020 | TC-NAC06 |
| NAC07 | Must | US-NAC07 | F09 F10 F11 | UC05 UC06 | CC-011, CC-013, CC-018 | TC-NAC07 |
| NAC08 | Must | US-NAC08 | F09 F10 F11 | UC05 UC06 | CC-011, CC-013, CC-016, CC-018 | TC-NAC08 |
| NAC09 | Should | US-NAC09 | F17 | UC12 | CC-024 | TC-NAC09 |
| NAC10 | Must | US-NAC10 | F10 F13 F14 F15 | UC06 UC08 UC09 UC10 | CC-012, CC-013, CC-016, CC-018, CC-020 | TC-NAC10 |
| NAC11 | Must | US-NAC11 | F10 F13 F14 F15 | UC06 UC08 UC09 UC10 | CC-014, CC-016, CC-018 | TC-NAC11 |
| NAC12 | Must | US-NAC12 | F14 F15 | UC09 UC10 | CC-015, CC-016, CC-018, CC-020 | TC-NAC12 |
| NAC13 | Must | US-NAC13 | F14 F15 | UC09 UC10 | CC-015, CC-016, CC-018, CC-020 | TC-NAC13 |
| NAC14 | Should | US-NAC14 | F17 | UC12 | CC-024 | TC-NAC14 |
| NAC15 | Could | US-NAC15 | F18 | UC13 | CC-026 | TC-NAC15 |
| NAC16 | Must | US-NAC16 | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 | CC-007, CC-014, CC-016, CC-018, CC-020 | TC-NAC16 |
| NAC17 | Must | US-NAC17 | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 | CC-012, CC-016, CC-018, CC-020 | TC-NAC17 |
| NAC18 | Must | US-NAC18 | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 | CC-011, CC-015, CC-016, CC-018, CC-020 | TC-NAC18 |
| NAC19 | Must | US-NAC19 | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 | CC-014, CC-016, CC-018, CC-020 | TC-NAC19 |
| NAC20 | Should | US-NAC20 | F03 F17 | UC12 UC15 | CC-023 | TC-NAC20 |
| T01 | Must | US-T01 | F04 F05 | UC01 UC02 | CC-003, CC-004, CC-018 | TC-T01 |
| T02 | Must | US-T02 | F06 F07 | UC03 | CC-008, CC-010, CC-018 | TC-T02 |
| T03 | Must | US-T03 | F06 F07 | UC03 | CC-005, CC-008, CC-018 | TC-T03 |
| T04 | Must | US-T04 | F06 F07 | UC03 | CC-008, CC-018 | TC-T04 |
| T05 | Must | US-T05 | F05 F08 | UC02 UC04 | CC-007, CC-010, CC-018 | TC-T05 |
| T06 | Must | US-T06 | F05 F08 | UC02 UC04 | CC-007, CC-010, CC-018 | TC-T06 |
| T07 | Must | US-T07 | F06 F07 | UC03 | CC-008, CC-010, CC-018 | TC-T07 |
| T08 | Must | US-T08 | F04 F05 | UC01 UC02 | CC-003, CC-004, CC-018 | TC-T08 |
| T09 | Should | US-T09 | F15 | UC10 | CC-023 | TC-T09 |
| T10 | Should | US-T10 | F16 | UC11 | CC-025 | TC-T10 |
| T11 | Could | US-T11 | F18 | UC13 | CC-026 | TC-T11 |
| S01 | Must | US-S01 | F05 | UC02 | CC-003, CC-006, CC-018 | TC-S01 |
| S02 | Must | US-S02 | F05 | UC02 | CC-003, CC-006, CC-018 | TC-S02 |
| S03 | Must | US-S03 | F06 F07 | UC03 | CC-005, CC-006, CC-018 | TC-S03 |
| S04 | Must | US-S04 | F06 F07 | UC03 | CC-009, CC-018 | TC-S04 |
| S05 | Must | US-S05 | F06 F07 | UC03 | CC-009, CC-018 | TC-S05 |
| S06 | Must | US-S06 | F12 | UC07 | CC-009, CC-018 | TC-S06 |
| S07 | Must | US-S07 | F05 F07 F12 F15 | UC02 UC03 UC07 UC10 | CC-006, CC-009, CC-018 | TC-S07 |
| S08 | Should | US-S08 | F05 | UC02 | CC-025 | TC-S08 |
| S09 | Should | US-S09 | F16 | UC11 | CC-025 | TC-S09 |
| S10 | Could | US-S10 | F18 | UC13 | CC-026 | TC-S10 |
| CN01 | Unlabeled / proposed Must* | US-CN01 | F02 | UC14 | CC-002, CC-017 | TC-CN01 |
| CN02 | Unlabeled / proposed Must* | US-CN02 | F02 | UC14 | CC-002, CC-017 | TC-CN02 |
| CN03 | Unlabeled / proposed Must* | US-CN03 | F02 | UC14 | CC-002, CC-017 | TC-CN03 |
| CN04 | Unlabeled / proposed Must* | US-CN04 | F02 | UC14 | CC-002, CC-017 | TC-CN04 |
| CN05 | Unlabeled / proposed Must* | US-CN05 | F02 | UC14 | CC-002, CC-017 | TC-CN05 |
| CN06 | Unlabeled / proposed Must* | US-CN06 | F02 | UC14 | CC-019 | TC-CN06 |
| CN07 | Unlabeled / proposed Must* | US-CN07 | F02 | UC14 | CC-002, CC-017 | TC-CN07 |
| CN08 | Unlabeled / proposed Must* | US-CN08 | F02 | UC14 | CC-002, CC-017 | TC-CN08 |
| CN09 | Unlabeled / proposed Must* | US-CN09 | F02 | UC14 | CC-002, CC-017, CC-020 | TC-CN09 |
| CN10 | Unlabeled / proposed Must* | US-CN10 | F02 | UC14 | CC-012, CC-017 | TC-CN10 |
| OR01 | Unlabeled / proposed Must* | US-OR01 | F03 | UC15 | CC-019 | TC-OR01 |
| OR02 | Unlabeled / proposed Must* | US-OR02 | F03 | UC15 | CC-002, CC-017 | TC-OR02 |
| OR03 | Unlabeled / proposed Must* | US-OR03 | F03 | UC15 | CC-002, CC-017 | TC-OR03 |
| OR04 | Unlabeled / proposed Must* | US-OR04 | F03 | UC15 | CC-002, CC-017 | TC-OR04 |
| OR05 | Unlabeled / proposed Must* | US-OR05 | F03 | UC15 | CC-002, CC-017 | TC-OR05 |
| OR06 | Unlabeled / proposed Must* | US-OR06 | F03 | UC15 | CC-002, CC-017 | TC-OR06 |
| OR07 | Unlabeled / proposed Must* | US-OR07 | F03 | UC15 | CC-002, CC-017 | TC-OR07 |
| OR08 | Unlabeled / proposed Must* | US-OR08 | F03 | UC15 | CC-019 | TC-OR08 |
| OR09 | Unlabeled / proposed Must* | US-OR09 | F03 | UC15 | CC-019 | TC-OR09 |
| OR10 | Unlabeled / proposed Must* | US-OR10 | F03 | UC15 | CC-002, CC-017 | TC-OR10 |
| OR11 | Unlabeled / proposed Must* | US-OR11 | F03 | UC15 | CC-002, CC-017, CC-020 | TC-OR11 |
| OR12 | Unlabeled / proposed Must* | US-OR12 | F03 | UC15 | CC-012, CC-017 | TC-OR12 |

## 3. Cross-cutting coverage

TC-AUTH, TC-LOCAL, TC-SFU, TC-RECOVERY and TC-PRIVACY cover shared architectural obligations; TC-ADM01–07 and TC-FAIL01–08 supplement admission/fault cases; proposed TC-CTRL01–04 and TC-CLOSE01–03 cover reviewed control/closure races. See [test catalogue](05-testing-and-evaluation/02-test-cases.md). Five supporting cards remain identified in [functional register](01-requirements/04-functional-requirements.md); do not invent original source IDs for them.
