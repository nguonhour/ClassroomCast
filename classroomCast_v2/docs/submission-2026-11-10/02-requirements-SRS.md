# 02 — Requirements Documentation (SRS)

Prepared 9 November 2026 for teacher review on 10 November. **Draft; not approved or implemented.**



---

Source: [03-software-requirements-specification.md](../01-requirements/03-software-requirements-specification.md)

# Software requirements specification

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Purpose and authority

This SRS is a navigation and baseline-control document for the proposed release. It composes the linked requirement, role, rule and acceptance registers without creating alternative requirement IDs. Teacher acceptance, campus authorization, implementation and tests are separate decisions/evidence.

## 2. Product perspective

ClassroomCast comprises a local browser interface, application backend, SFU/signaling services, policy manager, approved enforcement integration and persistent operational records. Campus infrastructure ownership and browser capture consent remain external constraints.

## 3. Normative candidate sections

| Topic | Authoritative location in this package |
|---|---|
| Original numbered capabilities and infrastructure obligations | [Functional register](../01-requirements/04-functional-requirements.md) |
| Quality, offline and security constraints | [Non-functional requirements](../01-requirements/05-non-functional-requirements.md) |
| Role and resource boundaries | [Permissions](../01-requirements/06-user-roles-and-permissions.md) |
| State and concurrency rules | [Business rules](../01-requirements/07-business-rules.md) |
| Actor goals | [Use cases](../01-requirements/08-use-cases.md) |
| Acceptance evidence | [Test catalogue](../05-testing-and-evaluation/02-test-cases.md) |
| Requirement/story/test connections | [Traceability](../traceability.md) |
| Unresolved choices and changes | [Decision log](../07-teacher-review/03-feedback-and-decision-log.md) |

## 4. Definitions

SYS = System Administrator; TCH = Teacher; STU = Student; NET = IT/Network Administrator. SFU = Selective Forwarding Unit: receives publication and forwards media to permitted viewers. Signaling exchanges connection/session information; it is distinct from the media stream. Policy manager validates and orchestrates policies; enforcement service applies supported rules. T = Teacher requirements; S = Student requirements; NAC = Network Access Control; CN = Campus Network; OR = teacher-owned router / portable-network requirements. These are original requirement families; F denotes workflow, UC user goal, CC delivery item, US story, TC test specification, D unresolved decision.

## 5. Assumptions and dependencies

Supported laptop browsers, trusted local endpoints, reachable SFU/media paths, authorized network integration and usable server/AP capacity must be established by feasibility tests. No cloud runtime dependency is assumed. External websites require WAN; offline media does not prove internet availability or selective restriction effectiveness.

## 6. Baseline/change procedure

Before implementation commitment, agree test conditions for the specified 50–150 students and equipment for both deployment modes, sign off supported browsers and acceptance targets, and assign decision owners. For changes record requested text, affected IDs, effort/schedule/risk/test impact, decision maker, date and evidence. Preserve supplied Must requirements until an explicit change is approved. Approval fields remain blank; revision 0.1 is not a signed baseline.


---

Source: [04-functional-requirements.md](../01-requirements/04-functional-requirements.md)

# Functional requirements and deployment obligations

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Source classification

The 63 rows retain original IDs and source priorities: 31 Must, 7 Should, 3 Could, 22 individually unlabeled deployment obligations. CN/OR are not optional merely because priorities were unlabeled. Their proposed Must* classification needs confirmation. Capability availability is not established by documentation.

## 2. Requirement register

| ID | Requirement | Source priority | Flows | Use cases |
|---|---|---|---|---|
| NAC01 | Enable or disable network restrictions for a class | Must | F01 F10 | UC06 |
| NAC02 | Block website categories, including AI and coding agents | Must | F09 F10 F11 | UC05 UC06 |
| NAC03 | Block or allow individual domains | Must | F09 F10 F11 | UC05 UC06 |
| NAC04 | Support allow-by-default and restricted-by-default policies | Must | F09 F10 F11 | UC05 UC06 |
| NAC05 | Automatically apply policies when a class starts | Must | F01 F10 | UC06 |
| NAC06 | Restore the previous policy when a class ends | Must | F13 F14 | UC08 UC09 |
| NAC07 | Save reusable policy profiles | Must | F09 F10 F11 | UC05 UC06 |
| NAC08 | Add allowlist exceptions for approved websites | Must | F09 F10 F11 | UC05 UC06 |
| NAC09 | Schedule restrictions by date and time | Should | F17 | UC12 |
| NAC10 | Display active policy and actual enforcement status | Must | F10 F13 F14 F15 | UC06 UC08 UC09 UC10 |
| NAC11 | Record administrator actions and timestamps | Must | F10 F13 F14 F15 | UC06 UC08 UC09 UC10 |
| NAC12 | Provide an emergency disable and rollback function | Must | F14 F15 | UC09 UC10 |
| NAC13 | Support temporary rules with automatic expiry | Must | F14 F15 | UC09 UC10 |
| NAC14 | Import and export policy configurations | Should | F17 | UC12 |
| NAC15 | Apply different policies to student groups or devices where supported | Could | F18 | UC13 |
| NAC16 | Restrict policy management to authorized administrators | Must | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 |
| NAC17 | Keep router credentials and API secrets on the server | Must | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 |
| NAC18 | Prevent restrictions from breaking ClassroomCast itself | Must | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 |
| NAC19 | Minimize student browsing-history collection | Must | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 |
| NAC20 | Support locally stored rules for offline operation | Should | F03 F17 | UC12 UC15 |
| T01 | Create a classroom with a unique session ID and join code | Must | F04 F05 | UC01 UC02 |
| T02 | Start, stop, pause, and resume broadcasting | Must | F06 F07 | UC03 |
| T03 | Share an entire screen, window, or browser tab where supported | Must | F06 F07 | UC03 |
| T04 | Share supported system audio and optional microphone audio | Must | F06 F07 | UC03 |
| T05 | View connected students and their connection status | Must | F05 F08 | UC02 UC04 |
| T06 | Approve, reject, remove, and block participants | Must | F05 F08 | UC02 UC04 |
| T07 | Configure resolution, frame rate, and bitrate | Must | F06 F07 | UC03 |
| T08 | Display the classroom URL, join code, and QR code | Must | F04 F05 | UC01 UC02 |
| T09 | Display streaming health and connection diagnostics | Should | F15 | UC10 |
| T10 | Share presentation files, PDFs, images, and videos | Should | F16 | UC11 |
| T11 | Display session history and participant counts | Could | F18 | UC13 |
| S01 | Join through a local URL or QR code | Must | F05 | UC02 |
| S02 | Enter a classroom join code | Must | F05 | UC02 |
| S03 | Watch the teacher's screen in real time | Must | F06 F07 | UC03 |
| S04 | Play supported shared audio with volume control | Must | F06 F07 | UC03 |
| S05 | View the broadcast in fullscreen | Must | F06 F07 | UC03 |
| S06 | Reconnect after temporary network interruptions | Must | F12 | UC07 |
| S07 | Show connection status and useful errors | Must | F05 F07 F12 F15 | UC02 UC03 UC07 UC10 |
| S08 | Enter a student name or assigned student ID | Should | F05 | UC02 |
| S09 | Download teacher-provided materials when permitted | Should | F16 | UC11 |
| S10 | Raise a hand, submit questions, or answer polls | Could | F18 | UC13 |
| CN01 | Use an approved local server address or hostname | Unlabeled / proposed Must* | F02 | UC14 |
| CN02 | Verify student devices can reach the application and signaling services | Unlabeled / proposed Must* | F02 | UC14 |
| CN03 | Confirm required WebRTC media traffic is permitted | Unlabeled / proposed Must* | F02 | UC14 |
| CN04 | Verify Wi-Fi client isolation and guest-network restrictions | Unlabeled / proposed Must* | F02 | UC14 |
| CN05 | Obtain campus IT approval for hosting and firewall changes | Unlabeled / proposed Must* | F02 | UC14 |
| CN06 | Validate Wi-Fi capacity and network throughput for 150 students | Unlabeled / proposed Must* | F02 | UC14 |
| CN07 | Provide QR-code and manual URL discovery | Unlabeled / proposed Must* | F02 | UC14 |
| CN08 | Avoid IP address conflicts with existing campus services | Unlabeled / proposed Must* | F02 | UC14 |
| CN09 | Host required application components locally for offline operation | Unlabeled / proposed Must* | F02 | UC14 |
| CN10 | Integrate network restrictions with campus-approved DNS or gateway controls | Unlabeled / proposed Must* | F02 | UC14 |
| OR01 | Business-class Wi-Fi 6 or better equipment suitable for high client density | Unlabeled / proposed Must* | F03 | UC15 |
| OR02 | Configurable classroom SSID and Wi-Fi password | Unlabeled / proposed Must* | F03 | UC15 |
| OR03 | WPA2-AES or WPA3 security where compatible | Unlabeled / proposed Must* | F03 | UC15 |
| OR04 | DHCP capacity for all students and support devices | Unlabeled / proposed Must* | F03 | UC15 |
| OR05 | Stable server IP address or local hostname | Unlabeled / proposed Must* | F03 | UC15 |
| OR06 | Wired Gigabit Ethernet or faster connection to the server where possible | Unlabeled / proposed Must* | F03 | UC15 |
| OR07 | Appropriate client isolation settings that permit access to the server and approved enforcement services | Unlabeled / proposed Must* | F03 | UC15 |
| OR08 | One or more access points based on classroom capacity testing | Unlabeled / proposed Must* | F03 | UC15 |
| OR09 | Support for additional access points and a wired switch | Unlabeled / proposed Must* | F03 | UC15 |
| OR10 | Portable power, cables, and carrying equipment | Unlabeled / proposed Must* | F03 | UC15 |
| OR11 | Fully functional local services without WAN or internet access | Unlabeled / proposed Must* | F03 | UC15 |
| OR12 | Local software-based policy management without requiring manual rule changes for each class | Unlabeled / proposed Must* | F03 | UC15 |

## 3. Supporting features and count reconciliation

| Card | Capability | Basis | Priority/status |
|---|---|---|---|
| BF-05-07 | Basic health and operations | Shared architectural and classroom-administration obligations; no extra original ID | REQUIRED / source obligation |
| BF-06-05 | Classroom authorization | Unnumbered classroom-administration obligation; supports T01/T06 and S03 | REQUIRED / source obligation |
| BF-06-06 | Application account management | Proposed account model, not a separate original numbered feature | PROPOSED / no source priority |
| BF-06-07 | Role assignment | Proposed RBAC allocation | PROPOSED / no source priority |
| BF-06-08 | Application settings and scoped review | Proposed administration UI/permission details | PROPOSED / no source priority |

All 68 original board cards are available in [board/ROW-2-FEATURE-CARDS.md](../../../classroomcast_v1/board/ROW-2-FEATURE-CARDS.md). They are grouped feature descriptions; user stories and tasks may split or combine them. The [traceability matrix](../traceability.md) maps every numbered requirement to a story and test. No feature has been marked implemented.


---

Source: [05-non-functional-requirements.md](../01-requirements/05-non-functional-requirements.md)

# Non-functional requirements

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Quality obligations

Local runtime, SFU delivery, trusted capture context, server-side secrets, truthful enforcement status, health/logging/recovery and minimal data collection come from supplied architectural obligations. Performance numbers below remain proposals. These constraints apply across selected features, including optional ones once included.

## 2. Candidate measurable conditions

| Test basis | Proposed setup/target | Approval/evidence rule |
|---|---|---|
| AT01 — Local UI | Fresh browser reaches join page within 5 s on a reachable healthy test LAN; 10 trials per supported browser | Timing starts at navigation and ends when code input is interactive; record cold/cache conditions |
| AT02 — Playback quality | Agreed starting profile 720p/15 fps; source-to-display p95 ≤1 s; report received bitrate, freezes, packet loss and per-client results | Proposed threshold needs D12 approval; measure visible source timestamp at source/viewer in a common recording; separate screen content from encoder adaptation |
| AT03 — Capacity/stability | 50/100/150 concurrent subscribers, 30 min each; per-viewer playback active at ≥98% of declared one-minute checks; no open release-blocking defect | Record physical/simulated counts, AP/SSID/topology, OS/browser, source, bitrate, server CPU/RAM/NIC and samples; simulation does not prove 150-laptop Wi-Fi airtime |
| AT04 — Policy apply | Healthy reachable authorized adapter reports verified outcome within 30 s of class-start/apply event in 10 trials | Must include client-path denied/allowed controls and local app/media access; upstream conditions recorded |
| AT05 — Restoration | Prior policy verified within 30 s of end/emergency/expiry trigger in 10 healthy reachable trials | In unreachable/conflicting-state tests, class still closes; durable pending/failure shown within proposed 5 s of detecting failure; safe retry/operator recovery required |
| AT06 — Reconnect | After a 10 s interruption, same-class playback recovers within 15 s of reachability returning in ≥9/10 attempts | Also test class ended and participant revoked while offline; those clients must not regain access |
| AT07 — Offline | Preprovision runtime assets/images, names/cert trust and lists; disconnect WAN and open fresh browser | External public-site failure is not evidence of selective blocking; use controlled local domains for offline rule checks |

Use the teacher-specified 50–150 students, including CN06 validation for 150. D12 defines test conditions and quality thresholds. Lower-load exploratory stages do not discharge the 150-student target; simulated subscribers do not prove physical Wi-Fi capacity.

## 3. Cross-cutting acceptance

| Criterion/test | Proposed acceptance |
|---|---|
| AC-AUTH / TC-AUTH | Matrix allow/deny and cross-class/scope tests pass; stale/forged/revoked room grants fail; role removal affects new privileged requests; no permission is inferred only from visible UI |
| AC-LOCAL / TC-LOCAL | AT07 confirms local app, API, signaling, SFU, policy storage and required filtering service operation without cloud/CDN runtime dependence |
| AC-SFU / TC-SFU | Documented transport path shows teacher publication to local SFU and per-viewer subscriptions; actual negotiated streams/bitrates and load are recorded |
| AC-RECOVERY / TC-RECOVERY | Execute isolated scenarios TC-FAIL01–TC-FAIL08; health distinguishes network, application, media, trust/name and enforcement faults; unfinished temporary policy operations resume safely; backup/database/config restoration drill documented |
| AC-PRIVACY / TC-PRIVACY | Server secrets absent from clients/exports/logs; retained participant/audit data matches approved minimal collection and deletion rules |

## 4. Operational quality and unknowns

Availability/SLA, exact hardware sizing, supported browser versions, data retention, backup frequency, recovery point/time objectives and retry ceilings are not confirmed. Measure feasibility and decide with the teacher/network owner; do not invent numeric service guarantees. Record these decisions under D09–D13 and D18–D20.


---

Source: [07-business-rules.md](../01-requirements/07-business-rules.md)

# Business rules

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Proposed rules derived from existing requirements and reviewed workflows

| Rule | Required behavior / proposed mechanism | References |
|---|---|---|
| BR01 | Authorization checks action, class ownership, network scope and current state; default deny | NAC16, TC-AUTH |
| BR02 | Join code required; a valid code does not imply admission, identity or media grant | S02, D02/D03 |
| BR03 | Final admission and seat allocation are atomic; recheck pending state, block, code, capacity and class state | F05/F08, TC-ADM05/06 |
| BR04 | Publishing may start with zero viewers; current admitted viewers alone receive media | F06, S03 |
| BR05 | Pause/stop sharing does not end a classroom or revoke student admission | T02, F07 |
| BR06 | Operation IDs bind requester, class, target/publication and action; same completed request returns recorded outcome; unfinished requests resume remaining work | F07/F08/F13 |
| BR07 | Recheck authorization/state and publication version before SFU mutation and when responses arrive; stale responses cannot revive closed or replaced publications | F07/F12/F13 |
| BR08 | Remove/block revoke grants and prevent refresh; verify actual media denial separately; unknown cleanup schedules recovery | T06, F08/F15 |
| BR09 | Saved profile, accepted apply request and verified enforcement are separate states | NAC07/NAC10, F09/F10 |
| BR10 | Preserve prior policy and operation record before changes; restore only owned changes and reconcile conflicts | NAC06/NAC12/NAC13 |
| BR11 | A class is ended only when admission/grant closure and media termination or effective denial are verified; policy restoration is a separate result | F13 |
| BR12 | Expiry survives browser close and backend restart; unreachable services produce persistent unresolved status | F14/F15, D11 |
| BR13 | Local classroom paths remain protected; domain filtering does not imply universal device control | NAC18, F11 |
| BR14 | Evidence distinguishes configured/requested from observed/verified state | NAC10; all recovery flows |

## 2. Proposed state dimensions

| Dimension | Candidate states | Important distinction |
|---|---|---|
| Classroom | Created, Open, Ending, Ended | Paused media does not close class |
| Participant | Pending, Admitted, Rejected, Removed, Blocked | Connection loss is not removal |
| Publication | Not publishing, Publishing, Broadcasting, Paused, Stopping, Stopped, Unresolved | New capture after source ends requires browser consent via F06 |
| Policy operation | Not applied, Applying, Verified, Degraded, Restoring, Restored, Unresolved | Record scope, version, evidence and time |

These names are design proposals, not established database enums. Each transition needs validation, durable outcome and appropriate notification. Final D08/D11 choices can refine them.

## 3. Closure outcome selection

First check application/media closure. If unverified: **Class ending — cleanup unresolved**, regardless of policy result. If verified: report **Class ended** plus restoration **not required**, **verified**, or **pending/failed**. Never label an unknown restore as not required. An unauthorized end request leaves class and publication unchanged.


---

Source: [traceability.md](../traceability.md)

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

TC-AUTH, TC-LOCAL, TC-SFU, TC-RECOVERY and TC-PRIVACY cover shared architectural obligations; TC-ADM01–07 and TC-FAIL01–08 supplement admission/fault cases; proposed TC-CTRL01–04 and TC-CLOSE01–03 cover reviewed control/closure races. See [test catalogue](../05-testing-and-evaluation/02-test-cases.md). Five supporting cards remain identified in [functional register](../01-requirements/04-functional-requirements.md); do not invent original source IDs for them.

