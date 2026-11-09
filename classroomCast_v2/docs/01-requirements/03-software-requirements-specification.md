# Software requirements specification

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Purpose and authority

This SRS is a navigation and baseline-control document for the proposed release. It composes the linked requirement, role, rule and acceptance registers without creating alternative requirement IDs. Teacher acceptance, campus authorization, implementation and tests are separate decisions/evidence.

## 2. Product perspective

ClassroomCast comprises a local browser interface, application backend, SFU/signaling services, policy manager, approved enforcement integration and persistent operational records. Campus infrastructure ownership and browser capture consent remain external constraints.

## 3. Normative candidate sections

| Topic | Authoritative location in this package |
|---|---|
| Original numbered capabilities and infrastructure obligations | [Functional register](04-functional-requirements.md) |
| Quality, offline and security constraints | [Non-functional requirements](05-non-functional-requirements.md) |
| Role and resource boundaries | [Permissions](06-user-roles-and-permissions.md) |
| State and concurrency rules | [Business rules](07-business-rules.md) |
| Actor goals | [Use cases](08-use-cases.md) |
| Acceptance evidence | [Test catalogue](../05-testing-and-evaluation/02-test-cases.md) |
| Requirement/story/test connections | [Traceability](../traceability.md) |
| Unresolved choices and changes | [Decision log](../07-teacher-review/03-feedback-and-decision-log.md) |

## 4. Definitions

SYS = System Administrator; TCH = Teacher; STU = Student; NET = IT/Network Administrator. SFU = Selective Forwarding Unit: receives publication and forwards media to permitted viewers. Signaling exchanges connection/session information; it is distinct from the media stream. Policy manager validates and orchestrates policies; enforcement service applies supported rules. T = Teacher requirements; S = Student requirements; NAC = Network Access Control; CN = Campus Network; OR = teacher-owned router / portable-network requirements. These are original requirement families; F denotes workflow, UC user goal, CC delivery item, US story, TC test specification, D unresolved decision.

## 5. Assumptions and dependencies

Supported laptop browsers, trusted local endpoints, reachable SFU/media paths, authorized network integration and usable server/AP capacity must be established by feasibility tests. No cloud runtime dependency is assumed. External websites require WAN; offline media does not prove internet availability or selective restriction effectiveness.

## 6. Baseline/change procedure

Before implementation commitment, agree test conditions for the specified 50–150 students and equipment for both deployment modes, sign off supported browsers and acceptance targets, and assign decision owners. For changes record requested text, affected IDs, effort/schedule/risk/test impact, decision maker, date and evidence. Preserve supplied Must requirements until an explicit change is approved. Approval fields remain blank; revision 0.1 is not a signed baseline.
