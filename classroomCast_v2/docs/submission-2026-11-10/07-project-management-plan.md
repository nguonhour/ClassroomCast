# 07 — Project Management Plan

Prepared 9 November 2026 for teacher review on 10 November. **Draft; not approved or implemented.**

**Baseline precedence:** use the three-sprint meeting schedule first. Older six-sprint allocations are retained as historical proposals, not a second active schedule. Latest screenshot/document assignment conflicts are listed in the meeting overview; do not infer a final assignment without agreement.

---

Source: [03_ClassroomCast_Project_Planning_and_Design_Overview.md](../meeting-2026-11-10/03_ClassroomCast_Project_Planning_and_Design_Overview.md)

# 03 / Planning and Design

Prepared 9 November 2026 for the meeting on 10 November 2026. Draft - pending teacher/client confirmation.

## Architecture to explain

| Component / path | Purpose |
| --- | --- |
| Teacher -> local SFU -> students | The teacher publishes selected screen/audio; the Selective Forwarding Unit distributes media to authorized subscribers. Use an existing self-hosted SFU; stack choice remains proposed. |
| Browsers -> local backend | Class creation, admission, role/scope checks, status and control operations. Signaling establishes media connections; it is separate from media forwarding. |
| Backend -> database | Store sessions, grants, profiles, operation state and audit metadata; not live video streams. |
| Policy manager -> authorized DNS/gateway | Apply approved rules, verify the affected client path, persist recovery state and safely restore owned changes. A dashboard alone cannot enforce restrictions. |

## Main classroom lifecycle (F01)

Check local readiness -> create class (F04) -> authorize class start -> apply and verify selected policy (F10), or record no profile -> obtain the approved continuation decision if enforcement fails -> active class with joining (F05), broadcasting (F06/F07) and participant management (F08) -> authorized end and restoration (F13). Connection, diagnostics and emergency/expiry recovery use F12, F15 and F14.

Joining, broadcasting and participant controls are independent events while the class is open. F10 reports enforcement outcomes; it does not decide whether teaching continues. F13 records application/media closure separately from restoration.

## FigJam presentation route

Row 1: explain why and what. Row 2: show four roles and six capability areas. Row 3: walk through F01, then show F05, F06, F10 and F13 only when needed. Keep detailed recovery diagrams as backup. Use reviewed Mermaid as the source of truth; generated pictures may contain wrong arrows or labels.

## First technical proof

During design, run time-boxed feasibility experiments for trusted local HTTPS, SFU screen/audio, WAN-disconnected operation and authorized policy apply/restore. Record failures and limitations. This is feasibility work before full implementation, not a claim that development is already complete.

## Latest site schedule - proposed review baseline

| Phase | Dates | Deliverable / proposed ClassroomCast focus |
| --- | --- | --- |
| Preparation | Nov 10-17, 2026 | Requirements, stories, scope and proposal review. Approval is a pending milestone. |
| Design | Nov 18-27 | Architecture, data model, UI, API boundaries and test plan; feasibility evidence. |
| Sprint 1 | Nov 30-Dec 11 | Foundation: roles, classes, join/admission and a small local SFU demonstration. |
| Sprint 2 | Dec 14-25 | Core media controls, participant access and integrated policy apply/verify/restore. |
| Sprint 3 | Dec 28-Jan 13, 2027 | Required recovery, expiry/emergency, deployment coverage and hardening. Lower priorities only if capacity allows. |
| Testing / release | Jan 14-27 | Acceptance/defects; demo and guide planned Jan 14-20; site release Jan 27. |
| Closing | Jan 28-Feb 3 | Report, slides/rehearsal and final presentation Feb 3. |

The dates above come from the supplied site plan; sprint content is a project-specific proposal replacing vague labels such as CRUD, core use cases and search/reports/polish. This does not add a new reporting/search requirement. Testing and documentation occur within each sprint as well as in release preparation.

## Date conflict to resolve before commitment

The earlier page permits description/code/demo edits until January 25 at 23:59. Ask whether January 27 release and February 3 presentation are separate permitted milestones. Pending that answer, prepare an internal review package by January 22 and plan any required website uploads before January 25. Do not assume an extension or treat this as a confirmed final-report deadline.

## Scrum working agreement to confirm

Plan one goal and testable increment per sprint. Use team estimation, daily coordination, a review and retrospective. The third site sprint spans more than two calendar weeks; confirm the holiday/working-day calendar and intended sprint timebox. Do not convert story points or website working-day allocations into actual weekly hours.

## Team assignments visible in the site snapshot

| Member | Current task ownership shown / review responsibility |
| --- | --- |
| HENG NGUON HOUR | Representative; requirements/stories, sign-in/roles, search/reports/polish and presentation. Coordinate scope/date decisions. |
| CHANTHA MENGKONG | Architecture/data model, main-data operations and acceptance/bug fixes. |
| BUN SENGLEANG | UI mockups, core use cases and demo deployment. |
| HAK SENGKEA | Test plan, unit/integration tests and user guide. |
| HONG DYHENGMESA | Sprint planning/backlog, remaining use cases and final report. |

Assignments above preserve the edited document. The newer timeline differs: BUN owns main data and acceptance; CHANTHA owns core use cases and demo deployment; HONG also shares UI. Confirm one agreed allocation before approval. Role assignments do not establish expertise, availability or Scrum accountability.

## Risks and next evidence

| Risk | Mitigation / meeting action |
| --- | --- |
| No authorized enforcement path | Ask campus IT who owns DNS/gateway changes; run a scoped laboratory proof before promising campus blocking. |
| Wi-Fi/server capacity unknown | Inventory equipment; test progressively; distinguish simulator load from real laptop Wi-Fi results. |
| HTTPS or audio incompatibility | Test the intended browser/OS/source combinations and document trust provisioning. |
| Restoration or expiry failure | Persist operation ownership and prior state; test restart/unreachable/conflict recovery; show unresolved outcomes honestly. |
| Scope or schedule exceeds capacity | Confirm working hours and deadlines; split backlog items; defer lower priorities through an explicit scope decision. |

## Current progress and next gate

The earlier snapshot showed 0/24 tasks done. The latest timeline shows progress coloring but does not establish a completed-task count; verify status from task evidence. Do not mark proposal approval Done until approval evidence exists. Next gate: record teacher feedback, resolve key scope/date questions, then update SRS, backlog, design and the site plan consistently.

Detailed sources: docs/03-system-analysis-and-design/, 04-scrum-and-project-management/, 02-project-proposal/06-risks-and-mitigation.md and latest supplied screenshots. Live website state and FigJam sharing permissions were not checked.


---

Source: [01-scrum-plan.md](../04-scrum-and-project-management/01-scrum-plan.md)

# Scrum plan

> **9 November planning update:** Latest user-provided site screenshots show three development sprints starting November 30, different task allocations, and release/presentation dates through February 3. Earlier dates/allocations below are historical proposals, not the current meeting commitment. Use the [November 10 meeting package](../meeting-2026-11-10/README.md) to review the new baseline and January 25 editing-cutoff question. Approval remains pending.

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Product Vision and Product Goal

**Proposed Vision:** make local classroom demonstrations accessible on student laptops while providing transparent, authorized classroom and network controls.

**Proposed Product Goal:** deliver a tested local classroom release in which an authorized teacher broadcasts supported screen/audio to admitted students, manages participation, and uses approved policy application/restoration with honest status, within agreed deployment and capacity conditions by the course deadline.

## 2. Accountabilities and artifacts

Hour is proposed Product Owner; Dyhengmesa is proposed Scrum Master; all five members contribute as Developers. Developers jointly select and adapt Sprint Backlog work. Teacher/supervisor acceptance and campus IT authority are external governance responsibilities. Product Backlog has the Product Goal; Sprint Backlog has a Sprint Goal; each Increment must meet the agreed Definition of Done.

## 3. Team cadence retained from prior plan

| Event | Proposed timebox | Purpose and output |
|---|---|---|
| Sprint Planning | 90 minutes, first Monday | Agree Sprint Goal; Developers select achievable items and plan tasks |
| Daily Scrum | 15 minutes each working day | Developers inspect progress toward the goal and adapt the plan; record blockers |
| Backlog refinement | 30 minutes weekly | Split upcoming work, clarify acceptance and dependencies; supporting practice |
| Sprint Review | 60 minutes at the end of sprint | Demonstrate usable results with users/lecturer; capture feedback and reorder backlog |
| Sprint Retrospective | 45 minutes after review | Choose one measurable improvement and an owner |
| Weekly project status | 15 minutes to prepare, Friday | Hour records completed evidence, forecast, hours, top risks and decisions needed |

## 4. Planning and inspection

Use six proposed two-week sprints, check personal calendars and refine backlog continuously. Estimates are proposals until team planning poker. Story points indicate relative complexity, not fixed hours. Do not infer velocity from estimates. Review a usable increment with evidence, then choose one retrospective improvement with an owner and measurable check.

## 5. Board operation

Backlog → Ready → In progress → Review/test → Done. Record blockers, owner and next action; initial one main implementation item per person is a proposed working limit. Keep requirement/story/test links in each card. Routine scope refinement can occur with the Product Owner while preserving Sprint Goal; changing agreed release constraints requires teacher review.

## 6. Course connection

Reuse [COURSE-APPLICATION.md](../../../classroomcast_v1/COURSE-APPLICATION.md) for Chapters 1–12 and its source distinctions. The course website's plan is used for weekly progress per supplied screenshot; local docs do not update that website. No invitations or messages have been sent.


---

Source: [02-product-backlog.md](../04-scrum-and-project-management/02-product-backlog.md)

# Product backlog

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Epics and estimate policy

Epics correspond to the six product areas. CC-001/018/021/022 also cover cross-cutting discovery, acceptance and handover. Existing CC IDs and source order are preserved. Each CC item is a broad delivery slice to split before commitment; proposed story points below are discussion seeds, not team estimates or a forecast. Do not total these points with per-requirement story sizes.

## 2. Ordered delivery backlog

| CC ID | Delivery slice | Priority | Proposed SP | Sprint candidate | Lead proposed | Source requirements |
|---|---|---|---|---|---|---|
| CC-001 | Confirm scope capacity hardware and network authorization | Must | 3 | 1 | HENG NGUON HOUR | Project constraints |
| CC-002 | Provision local application SFU and trusted HTTPS | Must | 8 | 1 | CHANTHA MENGKONG | CN01 CN02 CN03 CN04 CN05 CN07 CN08 CN09 OR02 OR03 OR04 OR05 OR06 OR07 OR10 OR11 |
| CC-003 | Create class and validate admission credentials | Must | 5 | 1 | BUN SENGLEANG | T01 T08 S01 S02 |
| CC-004 | Build teacher start screen with joining information | Must | 3 | 1 | HAK SENGKEA | T01 T08 |
| CC-005 | Publish and subscribe through local SFU | Must | 8 | 1 | HONG DYHENGMESA | T03 S03 |
| CC-006 | Build student join and basic playback UI | Must | 5 | 1 | HENG NGUON HOUR | S01 S02 S03 S07 |
| CC-007 | Authorize classroom controls and participant actions | Must | 8 | 2 | BUN SENGLEANG | T05 T06 NAC16 |
| CC-008 | Add screen audio microphone and broadcast controls | Must | 5 | 2 | HONG DYHENGMESA | T02 T03 T04 T07 |
| CC-009 | Add student fullscreen volume and reconnect | Must | 5 | 2 | HENG NGUON HOUR | S04 S05 S06 S07 |
| CC-010 | Integrate teacher roster and sharing controls | Must | 5 | 2 | HAK SENGKEA | T02 T05 T06 T07 |
| CC-011 | Store and validate profiles categories rules and exceptions | Must | 8 | 3 | HONG DYHENGMESA | NAC02 NAC03 NAC04 NAC07 NAC08 NAC18 |
| CC-012 | Implement authorized enforcement adapter | Must | 8 | 3 | CHANTHA MENGKONG | NAC01 NAC10 NAC17 CN10 OR12 |
| CC-013 | Build policy editor and actual enforcement status | Must | 5 | 3 | HAK SENGKEA | NAC01 NAC02 NAC03 NAC04 NAC07 NAC08 NAC10 |
| CC-014 | Apply policies on class lifecycle with audit | Must | 8 | 3 | HONG DYHENGMESA | NAC05 NAC06 NAC11 NAC16 NAC19 |
| CC-015 | Implement durable expiry emergency restoration and recovery | Must | 8 | 4 | CHANTHA MENGKONG | NAC06 NAC12 NAC13 NAC18 |
| CC-016 | Verify policy effects and permission failures | Must | 5 | 4 | HENG NGUON HOUR | NAC01 NAC02 NAC03 NAC04 NAC05 NAC06 NAC08 NAC10 NAC11 NAC12 NAC13 NAC16 NAC17 NAC18 NAC19 |
| CC-017 | Validate both deployment modes and offline runtime | Must | 8 | 4 | CHANTHA MENGKONG | CN01 CN02 CN03 CN04 CN05 CN07 CN08 CN09 CN10 OR02 OR03 OR04 OR05 OR06 OR07 OR10 OR11 OR12 |
| CC-018 | Complete Must traceability and acceptance gap review | Must | 5 | 4 | HENG NGUON HOUR | T01 T02 T03 T04 T05 T06 T07 T08 S01 S02 S03 S04 S05 S06 S07 NAC01 NAC02 NAC03 NAC04 NAC05 NAC06 NAC07 NAC08 NAC10 NAC11 NAC12 NAC13 NAC16 NAC17 NAC18 NAC19 |
| CC-019 | Measure 50 and 150 subscriber capacity | Must | 8 | 5 | CHANTHA MENGKONG | CN06 OR01 OR08 OR09 |
| CC-020 | Run security offline rollback and restore drills | Must | 8 | 5 | HENG NGUON HOUR | NAC06 NAC10 NAC12 NAC13 NAC16 NAC17 NAC18 NAC19 CN09 OR11 |
| CC-021 | Run physical pilot and obtain acceptance decisions | Must | 5 | 6 | HENG NGUON HOUR | Release acceptance |
| CC-022 | Finish guides demonstration and submission | Must | 5 | 6 | HENG NGUON HOUR | Project handover |
| CC-023 | Add health diagnostics and reusable offline category maintenance | Should | 5 | After Must forecast | HONG DYHENGMESA | T09 NAC20 |
| CC-024 | Add schedules and policy import export | Should | 8 | After Must forecast | HONG DYHENGMESA | NAC09 NAC14 |
| CC-025 | Add permitted materials and optional student identifiers | Should | 8 | After Must forecast | HENG NGUON HOUR | T10 S08 S09 |
| CC-026 | Explore history participation tools and per-group policies | Could | 8 | Future release | HENG NGUON HOUR | T11 S10 NAC15 |

## 3. Acceptance and dependencies

| CC ID | Acceptance from existing backlog | Dependency |
|---|---|---|
| CC-001 | Roster roles and actual calendars recorded; hardware inventory and campus integration decision path recorded | Scope and feasible authorized environment |
| CC-002 | Two laptops reach trusted app and media endpoints; installation dependencies are listed | Scope and feasible authorized environment |
| CC-003 | Teacher creates session; active join code is unique; invalid and expired codes fail | Scope and feasible authorized environment |
| CC-004 | Teacher displays working local URL QR and join code | Scope and feasible authorized environment |
| CC-005 | Teacher-selected screen is visible on two browser viewers using local SFU | Scope and feasible authorized environment |
| CC-006 | Student joins valid class and sees playback or a useful connection error | Scope and feasible authorized environment |
| CC-007 | Teacher sees roster and admits rejects removes or blocks; unauthorized control and blocked rejoin fail | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-008 | Start stop pause resume and media settings pass supported-browser checks; audio source limitations recorded | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-009 | Playback controls work; interrupted connection recovers under agreed criterion; ended class remains closed | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-010 | UI reflects actual session state and results of authorized controls | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-011 | Versioned profiles cover both default modes and exceptions; protected local services remain reachable | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-012 | Adapter applies versioned rules and reads back state; credentials stay server-side; unsupported scope is explicit | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-013 | Administrator can configure profile and distinguish saved desired applying verified degraded and failed states | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-014 | Authorized class start/end invokes scope lease and restoration; audit excludes unnecessary browsing history | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-015 | End expiry emergency action and restart restore safely; conflicts and unreachable adapters stay visibly unresolved | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-016 | Client-path probes confirm block allow and local access; failure and bypass limitations are documented | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-017 | Same build works with mode-specific config; campus authorization recorded; new browser session works without WAN | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-018 | Each Must has an evidence case and named reviewer; missing or failing criteria remain open | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-019 | Report physical and simulated counts separately; bitrate loss delay CPU NIC and AP conditions recorded; unresolved capacity gap escalated | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-020 | Role failures service restarts external-rule conflicts WAN outage and backup restoration have recorded results | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-021 | Pilot device count results feedback and lecturer decisions recorded; open blockers resolved or explicit scope decision obtained | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-022 | Source/demo links build version runbooks acceptance evidence and operator handover ready by 22 Jan | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-023 | Dashboard shows useful metrics; versioned local lists can be refreshed before offline classes | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-024 | Schedules survive restart and timezone checks; exports exclude secrets and imports validate rules | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-025 | Allowed files and identifiers follow session permissions and retention rules | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-026 | Each feature is separately refined and depends on demonstrated capacity and supported enforcement scope | Relevant earlier classroom, media or policy slice plus current decisions |

## 4. Backlog status and sources

Every item is Proposed / implementation Not assessed. Original WBS and CSV remain [BACKLOG.csv](../../../classroomcast_v1/BACKLOG.csv) and [PROJECT-PLAN.md](../../../classroomcast_v1/PROJECT-PLAN.md). See [stories](../04-scrum-and-project-management/03-user-stories.md) and [traceability](../traceability.md) for detailed acceptance links. A delivery item can cover several requirements; test coverage is not proof of implementation.


---

Source: [03-user-stories.md](../04-scrum-and-project-management/03-user-stories.md)

# User stories and acceptance criteria

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Story status and granularity

These are 63 proposed requirement-level story candidates, with IDs US-{source requirement}. Deployment obligations are technical/enabler stories; split large candidates in refinement. Five supporting feature cards are covered through relevant CC work and architecture tests rather than invented source requirement IDs. Every candidate is Proposed; every acceptance test is Not run. Estimates are discussion seeds, not approved team velocity. Story estimates and CC estimates are alternative granularities and must not be added together.

## 2. Story catalogue and acceptance criteria

### US-NAC01 — Enable or disable network restrictions for a class

As a scoped policy administrator, I need the capability “enable or disable network restrictions for a class”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** NAC01 → F01 F10 / UC06 → CC-012, CC-013, CC-016, CC-018 → TC-NAC01.
- **Acceptance:** In a controlled authorized scope, enable and disable a profile; status and client-path probes show the effective result. Disabled/unreachable integration is not reported as verified.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC02 — Block website categories, including AI and coding agents

As a scoped policy administrator, I need the capability “block website categories, including AI and coding agents”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC02 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-016, CC-018 → TC-NAC02.
- **Acceptance:** For each configured category, predeclare representative denied domains and allowed controls; application produces the expected DNS/gateway results. Record list version and known coverage gaps.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC03 — Block or allow individual domains

As a scoped policy administrator, I need the capability “block or allow individual domains”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC03 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-016, CC-018 → TC-NAC03.
- **Acceptance:** A custom blocked domain is denied and an allowed domain is permitted through the configured enforcement path; invalid domain syntax is rejected before a network change.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC04 — Support allow-by-default and restricted-by-default policies

As a scoped policy administrator, I need the capability “support allow-by-default and restricted-by-default policies”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC04 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-016, CC-018 → TC-NAC04.
- **Acceptance:** Run allow-by-default and restricted-by-default profiles against the same declared test set; results match the agreed rule/exception precedence, including subdomain handling under D07.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC05 — Automatically apply policies when a class starts

As a scoped policy administrator, I need the capability “automatically apply policies when a class starts”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** NAC05 → F01 F10 / UC06 → CC-014, CC-016, CC-018 → TC-NAC05.
- **Acceptance:** Starting an authorized class with an approved profile creates an apply operation and audit outcome; healthy-scope verification meets proposed AT04. Starting from another class/scope cannot apply it.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC06 — Restore the previous policy when a class ends

As a scoped policy administrator, I need the capability “restore the previous policy when a class ends”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 8 points, to refine.
- **Trace:** NAC06 → F13 F14 / UC08 UC09 → CC-014, CC-015, CC-016, CC-018, CC-020 → TC-NAC06.
- **Acceptance:** After applying a temporary profile, end the class; prior effective rules and allowed/blocked client-path controls are restored within proposed AT05 when reachable. Restoration failures remain visible and retryable.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC07 — Save reusable policy profiles

As a scoped policy administrator, I need the capability “save reusable policy profiles”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC07 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-018 → TC-NAC07.
- **Acceptance:** Save two named profiles, reload the application/backend and retrieve equivalent rule versions; switching the selected profile does not itself falsely report network enforcement.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC08 — Add allowlist exceptions for approved websites

As a scoped policy administrator, I need the capability “add allowlist exceptions for approved websites”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC08 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-016, CC-018 → TC-NAC08.
- **Acceptance:** Given a blocked category, add an approved domain exception; that control resolves/connects where upstream permits, while another category domain remains denied. Protect local app/media access throughout.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC09 — Schedule restrictions by date and time

As a scoped policy administrator, I need the capability “schedule restrictions by date and time”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** NAC09 → F17 / UC12 → CC-024 → TC-NAC09.
- **Acceptance:** Schedule a start/end against a declared timezone and test clock; each executes once per agreed idempotency semantics after restart, rechecks scope approval and records actual result. Missed-run policy awaits D11.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC10 — Display active policy and actual enforcement status

As a scoped policy administrator, I need the capability “display active policy and actual enforcement status”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC10 → F10 F13 F14 F15 / UC06 UC08 UC09 UC10 → CC-012, CC-013, CC-016, CC-018, CC-020 → TC-NAC10.
- **Acceptance:** Compare desired version, adapter read-back and affected-client probe results; UI accurately differentiates saved, applying, verified, degraded, failed and restoration-pending outcomes with timestamps.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC11 — Record administrator actions and timestamps

As a scoped policy administrator, I need the capability “record administrator actions and timestamps”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC11 → F10 F13 F14 F15 / UC06 UC08 UC09 UC10 → CC-014, CC-016, CC-018 → TC-NAC11.
- **Acceptance:** Perform a profile edit, apply, failed apply and restore; each audit record includes actor/service identity, action, scope, time and outcome, with no credentials.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC12 — Provide an emergency disable and rollback function

As a scoped policy administrator, I need the capability “provide an emergency disable and rollback function”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC12 → F14 F15 / UC09 UC10 → CC-015, CC-016, CC-018, CC-020 → TC-NAC12.
- **Acceptance:** Apply restrictions then invoke authorized emergency restore; prior policy verifies under proposed AT05. Unauthorized request changes no rules; an unreachable adapter yields a visible unresolved result.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC13 — Support temporary rules with automatic expiry

As a scoped policy administrator, I need the capability “support temporary rules with automatic expiry”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 8 points, to refine.
- **Trace:** NAC13 → F14 F15 / UC09 UC10 → CC-015, CC-016, CC-018, CC-020 → TC-NAC13.
- **Acceptance:** Apply a rule with declared expiry; close the admin browser and restart the backend before expiry. Recovery executes restoration once safely and verifies it under AT05 or displays pending/failure if unreachable.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC14 — Import and export policy configurations

As a scoped policy administrator, I need the capability “import and export policy configurations”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** NAC14 → F17 / UC12 → CC-024 → TC-NAC14.
- **Acceptance:** Export and reimport a sample profile; normalized rule content matches, secrets are absent, malformed imports are rejected and applying requires its own authorized operation.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC15 — Apply different policies to student groups or devices where supported

As a scoped policy administrator, I need the capability “apply different policies to student groups or devices where supported”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Could; **proposed size:** 8 points, to refine.
- **Trace:** NAC15 → F18 / UC13 → CC-026 → TC-NAC15.
- **Acceptance:** Where the chosen adapter supports isolated identity/scope, apply a group rule to target A and demonstrate that control B retains its prior policy. Otherwise mark unsupported and record the scope decision.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC16 — Restrict policy management to authorized administrators

As a scoped policy administrator, I need the capability “restrict policy management to authorized administrators”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC16 → F09 F10 F13 F14 F15 / UC05 UC06 UC08 UC09 UC10 → CC-007, CC-014, CC-016, CC-018, CC-020 → TC-NAC16.
- **Acceptance:** Execute the role-permission matrix’s representative allowed and denied operations; Student/Teacher roles alone cannot edit policies or infrastructure, and out-of-scope administrators cannot mutate that scope.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC17 — Keep router credentials and API secrets on the server

As a scoped policy administrator, I need the capability “keep router credentials and API secrets on the server”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC17 → F09 F10 F13 F14 F15 / UC05 UC06 UC08 UC09 UC10 → CC-012, CC-016, CC-018, CC-020 → TC-NAC17.
- **Acceptance:** Inspect built frontend, network responses, profile exports and logs for test secret markers; none appear. Adapter secrets/signing keys are accessible only through protected server configuration.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC18 — Prevent restrictions from breaking ClassroomCast itself

As a scoped policy administrator, I need the capability “prevent restrictions from breaking ClassroomCast itself”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC18 → F09 F10 F13 F14 F15 / UC05 UC06 UC08 UC09 UC10 → CC-011, CC-015, CC-016, CC-018, CC-020 → TC-NAC18.
- **Acceptance:** Apply the most restrictive agreed profile; a fresh student join, teacher controls, live media, local names and restoration remain functional. Reject an explicit conflicting local-service rule.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC19 — Minimize student browsing-history collection

As a scoped policy administrator, I need the capability “minimize student browsing-history collection”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC19 → F09 F10 F13 F14 F15 / UC05 UC06 UC08 UC09 UC10 → CC-014, CC-016, CC-018, CC-020 → TC-NAC19.
- **Acceptance:** Review app/resolver logging and storage using synthetic browsing events; collect only agreed minimal data, mask/exclude unnecessary raw histories and demonstrate deletion according to D13.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC20 — Support locally stored rules for offline operation

As a scoped policy administrator, I need the capability “support locally stored rules for offline operation”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** NAC20 → F03 F17 / UC12 UC15 → CC-023 → TC-NAC20.
- **Acceptance:** After provisioning local lists, disable WAN and restart services; profiles/rules remain retrievable and local test-domain policy operations work without remote list fetching. Baseline offline behavior remains required.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T01 — Create a classroom with a unique session ID and join code

As a teacher, I need the capability “create a classroom with a unique session ID and join code”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T01 → F04 F05 / UC01 UC02 → CC-003, CC-004, CC-018 → TC-T01.
- **Acceptance:** Create 10 concurrent active classes with the same authorized teacher or test teachers; all session IDs and active join codes are distinct. Closed-code join is rejected.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T02 — Start, stop, pause, and resume broadcasting

As a teacher, I need the capability “start, stop, pause, and resume broadcasting”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** T02 → F06 F07 / UC03 → CC-008, CC-010, CC-018 → TC-T02.
- **Acceptance:** Run start → pause → resume → stop on the supported setup; both viewers see each agreed state and publication stops after stop. Stopping sharing leaves the class open; pause/audio semantics await D08.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T03 — Share an entire screen, window, or browser tab where supported

As a teacher, I need the capability “share an entire screen, window, or browser tab where supported”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T03 → F06 F07 / UC03 → CC-005, CC-008, CC-018 → TC-T03.
- **Acceptance:** For every supported capture type (screen/window/tab), publish the teacher-selected source to two viewers; denial/cancellation creates no published capture. Record unsupported browser/source combinations under D09.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T04 — Share supported system audio and optional microphone audio

As a teacher, I need the capability “share supported system audio and optional microphone audio”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** T04 → F06 F07 / UC03 → CC-008, CC-018 → TC-T04.
- **Acceptance:** On each agreed OS/browser/source combination, verify shared audio when supported, microphone audio when selected, and no microphone publication when not selected. Record unsupported sources explicitly.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T05 — View connected students and their connection status

As a teacher, I need the capability “view connected students and their connection status”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T05 → F05 F08 / UC02 UC04 → CC-007, CC-010, CC-018 → TC-T05.
- **Acceptance:** Join two viewers and disconnect one; roster shows the correct participant count and each current connection state within proposed 5 s after the server detects the event.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T06 — Approve, reject, remove, and block participants

As a teacher, I need the capability “approve, reject, remove, and block participants”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** T06 → F05 F08 / UC02 UC04 → CC-007, CC-010, CC-018 → TC-T06.
- **Acceptance:** Demonstrate approve, reject, remove and block separately. Removed access closes; blocked rejoin fails for the agreed identity/duration. Repeat cross-class control attempts and verify denial; D02/D03 define guarantees.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T07 — Configure resolution, frame rate, and bitrate

As a teacher, I need the capability “configure resolution, frame rate, and bitrate”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T07 → F06 F07 / UC03 → CC-008, CC-010, CC-018 → TC-T07.
- **Acceptance:** Apply two supported quality profiles; record configured and observed resolution, frame rate and bitrate with adaptation limits. Unsupported input is rejected or reported; do not assert exact network bitrate from settings alone.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T08 — Display the classroom URL, join code, and QR code

As a teacher, I need the capability “display the classroom URL, join code, and QR code”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T08 → F04 F05 / UC01 UC02 → CC-003, CC-004, CC-018 → TC-T08.
- **Acceptance:** From a second laptop, open the displayed URL and decoded QR destination; both point to the intended local class/join route and the displayed code joins that class.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T09 — Display streaming health and connection diagnostics

As a teacher, I need the capability “display streaming health and connection diagnostics”, so that I can operate an owned classroom.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** T09 → F15 / UC10 → CC-023 → TC-T09.
- **Acceptance:** During a controlled media fault, diagnostics distinguish connection state, missing/stalled media and available WebRTC statistics; display measurement time and refresh within proposed 5 s.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T10 — Share presentation files, PDFs, images, and videos

As a teacher, I need the capability “share presentation files, PDFs, images, and videos”, so that I can operate an owned classroom.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** T10 → F16 / UC11 → CC-025 → TC-T10.
- **Acceptance:** Exercise one approved presentation, PDF, image and video sample through the agreed sharing method; admitted viewers can access it and rejected formats show a useful error. D16 defines upload versus media presentation behavior.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T11 — Display session history and participant counts

As a teacher, I need the capability “display session history and participant counts”, so that I can operate an owned classroom.

- **Priority:** Could; **proposed size:** 3 points, to refine.
- **Trace:** T11 → F18 / UC13 → CC-026 → TC-T11.
- **Acceptance:** End two owned classes; retained history shows their correct IDs/times and participant counts. Another teacher cannot read them; summaries do not imply video recordings.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S01 — Join through a local URL or QR code

As a student, I need the capability “join through a local URL or QR code”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S01 → F05 / UC02 → CC-003, CC-006, CC-018 → TC-S01.
- **Acceptance:** From two test laptops on the selected network, the local URL and QR destination both reach the join page with trusted browser access. Record page-ready time against proposed AT01.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S02 — Enter a classroom join code

As a student, I need the capability “enter a classroom join code”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S02 → F05 / UC02 → CC-003, CC-006, CC-018 → TC-S02.
- **Acceptance:** In both proposed modes, missing, invalid, expired or closed codes are rejected. Code admission permits viewing only after final checks; code + approval keeps a valid request pending until owning-Teacher approval and fresh atomic admission/capacity checks. Wrong guesses follow the agreed rate-limit rule; execute TC-ADM01–TC-ADM07.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S03 — Watch the teacher's screen in real time

As a student, I need the capability “watch the teacher's screen in real time”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S03 → F06 F07 / UC03 → CC-005, CC-006, CC-018 → TC-S03.
- **Acceptance:** Two admitted viewers receive the selected live screen via the local SFU; non-admitted clients cannot subscribe. Measure physical-viewer playback and target-scale conditions under AT02/AT03.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S04 — Play supported shared audio with volume control

As a student, I need the capability “play supported shared audio with volume control”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S04 → F06 F07 / UC03 → CC-009, CC-018 → TC-S04.
- **Acceptance:** On supported audio combinations, each viewer can start playback and adjust/mute its own audio independently; another viewer’s volume and teacher publication are unchanged.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S05 — View the broadcast in fullscreen

As a student, I need the capability “view the broadcast in fullscreen”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S05 → F06 F07 / UC03 → CC-009, CC-018 → TC-S05.
- **Acceptance:** Enter/exit fullscreen on each supported browser using user interaction; playback continues or any unsupported behavior is explained and recorded.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S06 — Reconnect after temporary network interruptions

As a student, I need the capability “reconnect after temporary network interruptions”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** S06 → F12 / UC07 → CC-009, CC-018 → TC-S06.
- **Acceptance:** Interrupt one viewer’s network for 10 s; it reconnects to the same active class within proposed 15 s of reachability returning in at least 9/10 attempts. Removed/ended sessions never auto-readmit.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S07 — Show connection status and useful errors

As a student, I need the capability “show connection status and useful errors”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S07 → F05 F07 F12 F15 / UC02 UC03 UC07 UC10 → CC-006, CC-009, CC-018 → TC-S07.
- **Acceptance:** Inject invalid code, full class, denied admission, ended session, network loss and media failure; each produces the correct actionable status without exposing secrets.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S08 — Enter a student name or assigned student ID

As a student, I need the capability “enter a student name or assigned student ID”, so that I can participate in an authorized local class.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** S08 → F05 / UC02 → CC-025 → TC-S08.
- **Acceptance:** With the feature enabled, enter a valid name/assigned ID; invalid input receives validation feedback and the allowed identifier is associated with the admitted participant. Identity strength and retention await D03/D13.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S09 — Download teacher-provided materials when permitted

As a student, I need the capability “download teacher-provided materials when permitted”, so that I can participate in an authorized local class.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** S09 → F16 / UC11 → CC-025 → TC-S09.
- **Acceptance:** An admitted student downloads an allowed sample matching its recorded checksum; download denied when permission is off or admission is revoked; direct URL requests enforce the same checks.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S10 — Raise a hand, submit questions, or answer polls

As a student, I need the capability “raise a hand, submit questions, or answer polls”, so that I can participate in an authorized local class.

- **Priority:** Could; **proposed size:** 3 points, to refine.
- **Trace:** S10 → F18 / UC13 → CC-026 → TC-S10.
- **Acceptance:** For each selected interaction (hand/question/poll), an admitted student action reaches the owning teacher; unauthorized or closed-activity submissions are rejected. Specific interaction set awaits D17.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN01 — Use an approved local server address or hostname

As a authorized network installer, I need the capability “use an approved local server address or hostname”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN01 → F02 / UC14 → CC-002, CC-017 → TC-CN01.
- **Acceptance:** Campus IT approves server name/address; two campus laptops reach the correct server with trusted access. Preserve approval and configuration evidence.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN02 — Verify student devices can reach the application and signaling services

As a authorized network installer, I need the capability “verify student devices can reach the application and signaling services”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN02 → F02 / UC14 → CC-002, CC-017 → TC-CN02.
- **Acceptance:** From two representative student network locations, verify app/API and media-signaling connectivity; report each separate endpoint and any inaccessible segment.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN03 — Confirm required WebRTC media traffic is permitted

As a authorized network installer, I need the capability “confirm required WebRTC media traffic is permitted”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN03 → F02 / UC14 → CC-002, CC-017 → TC-CN03.
- **Acceptance:** Establish real audio/video over the approved configured media path; record actual ports/transports and approved firewall evidence. Signaling-only success does not pass.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN04 — Verify Wi-Fi client isolation and guest-network restrictions

As a authorized network installer, I need the capability “verify Wi-Fi client isolation and guest-network restrictions”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN04 → F02 / UC14 → CC-002, CC-017 → TC-CN04.
- **Acceptance:** Test the intended SSID/VLAN/isolation settings; students reach only the required server/enforcement paths, and guest restrictions affecting the flow are recorded.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN05 — Obtain campus IT approval for hosting and firewall changes

As a authorized network installer, I need the capability “obtain campus IT approval for hosting and firewall changes”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN05 → F02 / UC14 → CC-002, CC-017 → TC-CN05.
- **Acceptance:** Record written campus IT authorization for hosting and any required firewall changes before making those changes; absence leaves this criterion pending, not passed.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN06 — Validate Wi-Fi capacity and network throughput for 150 students

As a authorized network installer, I need the capability “validate Wi-Fi capacity and network throughput for 150 students”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 8 points, to refine.
- **Trace:** CN06 → F02 / UC14 → CC-019 → TC-CN06.
- **Acceptance:** Execute staged 50/100/150 subscriber tests and AT02/AT03 on the documented campus setup; identify physical versus simulated clients and whether 150-device Wi-Fi capacity is actually demonstrated.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN07 — Provide QR-code and manual URL discovery

As a authorized network installer, I need the capability “provide QR-code and manual URL discovery”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN07 → F02 / UC14 → CC-002, CC-017 → TC-CN07.
- **Acceptance:** Join from a campus laptop by both manual URL and QR destination; network instructions identify the correct campus network and server.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN08 — Avoid IP address conflicts with existing campus services

As a authorized network installer, I need the capability “avoid IP address conflicts with existing campus services”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN08 → F02 / UC14 → CC-002, CC-017 → TC-CN08.
- **Acceptance:** Campus IT checks reserved/static server addressing against DHCP/IP allocations; conflict checks show no duplicate address before the pilot.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN09 — Host required application components locally for offline operation

As a authorized network installer, I need the capability “host required application components locally for offline operation”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN09 → F02 / UC14 → CC-002, CC-017, CC-020 → TC-CN09.
- **Acceptance:** With images/assets/certificates provisioned, disconnect WAN and use a fresh browser session; class creation, joining and local media work without CDN/cloud requests.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN10 — Integrate network restrictions with campus-approved DNS or gateway controls

As a authorized network installer, I need the capability “integrate network restrictions with campus-approved DNS or gateway controls”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 5 points, to refine.
- **Trace:** CN10 → F02 / UC14 → CC-012, CC-017 → TC-CN10.
- **Acceptance:** Within written approved scope, apply an approved profile through the campus DNS/gateway adapter, verify client-path effects, and restore previous rules. Missing integration remains an acceptance gap.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR01 — Business-class Wi-Fi 6 or better equipment suitable for high client density

As a authorized network installer, I need the capability “business-class Wi-Fi 6 or better equipment suitable for high client density”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR01 → F03 / UC15 → CC-019 → TC-OR01.
- **Acceptance:** Record Wi-Fi 6-or-better equipment model/capabilities and staged load results for the intended client density; brochure client count alone is insufficient.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR02 — Configurable classroom SSID and Wi-Fi password

As a authorized network installer, I need the capability “configurable classroom SSID and Wi-Fi password”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR02 → F03 / UC15 → CC-002, CC-017 → TC-OR02.
- **Acceptance:** Configure the intended classroom SSID/password; two student laptops associate and obtain local connectivity without changing per-class infrastructure rules.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR03 — WPA2-AES or WPA3 security where compatible

As a authorized network installer, I need the capability “wPA2-AES or WPA3 security where compatible”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR03 → F03 / UC15 → CC-002, CC-017 → TC-OR03.
- **Acceptance:** Inspect negotiated Wi-Fi security on the supported clients: WPA2-AES or compatible WPA3 as agreed; record any incompatible devices and resolution.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR04 — DHCP capacity for all students and support devices

As a authorized network installer, I need the capability “dHCP capacity for all students and support devices”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR04 → F03 / UC15 → CC-002, CC-017 → TC-OR04.
- **Acceptance:** DHCP pool/lease configuration supports at least 150 students plus inventoried support devices; test lease assignment and no duplicate allocations using declared physical/simulated conditions.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR05 — Stable server IP address or local hostname

As a authorized network installer, I need the capability “stable server IP address or local hostname”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR05 → F03 / UC15 → CC-002, CC-017 → TC-OR05.
- **Acceptance:** Reboot router/server; the configured stable server address/local name still leads students to the intended application and media endpoint.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR06 — Wired Gigabit Ethernet or faster connection to the server where possible

As a authorized network installer, I need the capability “wired Gigabit Ethernet or faster connection to the server where possible”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR06 → F03 / UC15 → CC-002, CC-017 → TC-OR06.
- **Acceptance:** Use and record a negotiated Gigabit-or-faster wired server link where possible; if unavailable, record the exception and measured capacity impact for acceptance.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR07 — Appropriate client isolation settings that permit access to the server and approved enforcement services

As a authorized network installer, I need the capability “appropriate client isolation settings that permit access to the server and approved enforcement services”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR07 → F03 / UC15 → CC-002, CC-017 → TC-OR07.
- **Acceptance:** With intended isolation enabled/configured, two student clients still reach the server, media and approved enforcement paths; document permitted connectivity.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR08 — One or more access points based on classroom capacity testing

As a authorized network installer, I need the capability “one or more access points based on classroom capacity testing”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 8 points, to refine.
- **Trace:** OR08 → F03 / UC15 → CC-019 → TC-OR08.
- **Acceptance:** Test increasing client loads, measure bottlenecks and choose AP count/placement that meets agreed AT02/AT03; repeat after relevant configuration changes.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR09 — Support for additional access points and a wired switch

As a authorized network installer, I need the capability “support for additional access points and a wired switch”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR09 → F03 / UC15 → CC-019 → TC-OR09.
- **Acceptance:** Demonstrate adding the supported AP/switch arrangement without address conflicts or loss of class reachability; preserve a topology/configuration record.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR10 — Portable power, cables, and carrying equipment

As a authorized network installer, I need the capability “portable power, cables, and carrying equipment”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR10 → F03 / UC15 → CC-002, CC-017 → TC-OR10.
- **Acceptance:** Inventory required power supplies, cables/adapters and transport protection; perform one full setup and power/restart recovery using the portable kit.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR11 — Fully functional local services without WAN or internet access

As a authorized network installer, I need the capability “fully functional local services without WAN or internet access”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR11 → F03 / UC15 → CC-002, CC-017, CC-020 → TC-OR11.
- **Acceptance:** With WAN physically disconnected and local dependencies provisioned, start a fresh class and receive screen/supported audio on two laptops; apply/restore rules against controlled local test domains.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR12 — Local software-based policy management without requiring manual rule changes for each class

As a authorized network installer, I need the capability “local software-based policy management without requiring manual rule changes for each class”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 5 points, to refine.
- **Trace:** OR12 → F03 / UC15 → CC-012, CC-017 → TC-OR12.
- **Acceptance:** Apply and restore two class profiles through the supported software adapter with no manual router rule edits between classes; unsupported automation is visibly reported as a gap.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.


---

Source: [04-sprint-planning.md](../04-scrum-and-project-management/04-sprint-planning.md)

# Sprint planning

> **9 November planning update:** Latest user-provided site screenshots show three development sprints starting November 30, different task allocations, and release/presentation dates through February 3. Earlier dates/allocations below are historical proposals, not the current meeting commitment. Use the [November 10 meeting package](../meeting-2026-11-10/README.md) to review the new baseline and January 25 editing-cutoff question. Approval remains pending.

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Current planning position

You are preparing requirements, activity flows and approval material. Diagram completion does not establish implementation progress. The inherited Sprint 1 window is November 2–15; as of November 9 its actual work and remaining capacity are unknown. First record actual status, then select an achievable remaining Sprint Goal.

## 2. Candidate sprint backlogs

| Sprint | Goal | Candidate items | Review evidence |
|---|---|---|---|
| 1 | Prove local classroom and dependencies | CC-001–006 | One publisher/two viewers; trust and enforcement feasibility records |
| 2 | Complete classroom control and supported audio | CC-007–010 | Permission/admission, control and reconnect evidence |
| 3 | Integrate policy management and verified enforcement | CC-011–014 | Saved versus applied versus verified; safe prior-state restoration |
| 4 | Required recovery and deployment coverage | CC-015–018 | Expiry/emergency, isolated failures, both-mode readiness and RTM |
| 5 | Measure quality and security | CC-019–020 | Load/offline/security evidence and defect report |
| 6 | Obtain pilot acceptance and hand over | CC-021–022 | Pilot result, approved exceptions, runbooks, demo and report |

CC-023–026 are lower-priority candidates after required acceptance; no guaranteed sprint commitment. Split broad items and calculate actual individual load before selection. Do not carry incomplete work as Done.

## 3. Original first-sprint effort proposal

| Task | Owner | Estimate | Evidence at review |
|---|---|---:|---|
| Team agreement, requirement clarification and initial API/session contract | Hour | 5 h | Decision notes and shared contract |
| Minimal create-class/join-code API and session persistence | Sengleang | 8 h | Valid join succeeds; invalid/closed code fails |
| Teacher dashboard and URL/code/QR join display | Sengkea | 10 h | Teacher creates and displays a joinable session |
| SFU spike and teacher publishing / student subscription module | Dyhengmesa | 12 h | One publisher and two browser viewers on LAN |
| Local deployment, HTTPS trust test and DNS/network inventory | Mengkong | 10 h | Trust result on two laptops; enforcement prerequisites recorded |
| Student join/view screen and initial end-to-end checks | Hour | 9 h | Student can enter code, view screen and see connection state |
| Shared ceremonies, review, documentation and integration allowance | All | 10 h | Demo record, open defects and updated backlog |
| **Planned team effort** | | **64 h** | |

The original 64 hours is a pre-sprint plan, not November 9 remaining work. Approximate capacity is 20 hours/member/two weeks before exams and holidays. Track hours for resource planning; do not convert story points mechanically into hours.

## 4. Planning worksheet

Record sprint dates, Product Goal contribution, Sprint Goal, each person's available hours, carryover, selected story/CC IDs, dependencies, acceptance, tasks, estimate and owner. Developers negotiate achievable scope. At review attach demonstrations and tests; at retrospective agree one improvement and check it next sprint.

## 5. Forecast update

Actual completed work and remaining estimates determine forecast. Resolve equipment and scope blockers before promising capacity milestones. Keep January 22 internal readiness and January 25 final deadline visible; record any teacher-approved change.


---

Source: [05-team-roles-and-responsibilities.md](../04-scrum-and-project-management/05-team-roles-and-responsibilities.md)

# Team roles and responsibilities

> **9 November planning update:** Latest user-provided site screenshots show three development sprints starting November 30, different task allocations, and release/presentation dates through February 3. Earlier dates/allocations below are historical proposals, not the current meeting commitment. Use the [November 10 meeting package](../meeting-2026-11-10/README.md) to review the new baseline and January 25 editing-cutoff question. Approval remains pending.

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Named assignments — proposed except representative

| Member | Primary responsibility | Concrete deliverables | Review partner |
|---|---|---|---|
| **HENG NGUON HOUR ★** — ហេង ងួនហ៊ួរ | Representative, proposed Product Owner, application integration and student frontend | Ordered backlog; lecturer communication; weekly status; student join/view interface with Sengkea; end-to-end integration and acceptance coordination | Sengkea reviews UI; Sengleang reviews API integration |
| **BUN SENGLEANG** — ប៊ុន សេងលៀង | Classroom backend, REST APIs and database | Class/session APIs; authentication and roles; admission/removal; schema/migrations; join-code lifecycle; API tests | Dyhengmesa |
| **CHANTHA MENGKONG** — ចន្ថា ម៉េងគង់ | DevOps, SFU hosting and network enforcement adapter | Local LiveKit and Docker setup; CI/CD; HTTPS/DNS spike; AdGuard Home adapter; network diagnostics and recovery runbooks | Dyhengmesa for policy integration; Sengleang for server changes |
| **HAK SENGKEA** — ហាក់ សេងគា | Frontend and UI/UX lead | Teacher/admin dashboards; QR/code display; participant controls; policy editor/status UI; shared components; student UI support | Hour |
| **HONG DYHENGMESA** — ហុង ឌីហេងមេសា | NestJS policy service, media/application integration; proposed Scrum Master | Profile/lease/apply/expiry orchestration; LiveKit token/SDK integration; teacher publishing and student subscription module; Scrum facilitation | Sengleang for backend; Mengkong for media/network |

## 2. Responsibility matrix

| Deliverable | Hour | Sengleang | Mengkong | Sengkea | Dyhengmesa |
|---|---|---|---|---|---|
| Scope, backlog and status | A/R | C | C | C | R |
| Scrum facilitation and improvement actions | R | R | R | R | A/R |
| Session and identity APIs | C | A/R | C | C | R |
| Teacher/admin UI | R | C | C | A/R | C |
| SFU hosting and network deployment | C | C | A/R | C | R |
| Browser media and token integration | R | R | R | C | A/R |
| Student interface | A/R | C | C | R | C |
| Policy lifecycle service | C | R | R | C | A/R |
| Enforcement adapter and recovery | C | R | A/R | C | R |
| Acceptance evidence coordination | A/R | R | R | R | R |
| Final submission coordination | A/R | R | R | R | R |

R performs; A is accountable; C consulted; I informed. One A per deliverable; A/R is the same person performing and accountable. These are coordination proposals, not proof of accepted assignments or expertise. Technology names within the inherited assignments remain provisional.

## 3. Capacity and authority

Published approximate 10 hours/member/week must be reconfirmed against current calendars. All members test, review and document their work. Hour coordinates teacher communication and evidence; campus IT retains network authorization. Pair Mengkong and Dyhengmesa on media/enforcement learning and share knowledge to reduce concentrated dependency.


---

Source: [06-definition-of-done.md](../04-scrum-and-project-management/06-definition-of-done.md)

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


---

Source: [07-meeting-and-review-template.md](../04-scrum-and-project-management/07-meeting-and-review-template.md)

# Meeting and review templates

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Meeting record

Date/time/timezone: ___ · Meeting type: ___ · Participants: ___ · Facilitator: ___ · Goal: ___

| Topic | Evidence / observation | Decision or pending question | Owner | Due date |
|---|---|---|---|---|
| To complete | | | | |

## 2. Sprint Planning

Sprint: ___ · Dates: ___ · Product Goal contribution: ___ · Sprint Goal: ___

| Member | Available hours | Selected item and tasks | Estimate | Dependencies |
|---|---|---|---|---|
| To complete | | | | |

## 3. Daily coordination

Inspect progress toward Sprint Goal, remaining work, blockers and the next adaptation. Record blocker owner, needed assistance and next check. This is a proposed team working practice, not evidence a meeting happened.

## 4. Sprint Review

| Item / requirement | Build and demo | Test evidence | Stakeholder feedback | Backlog change |
|---|---|---|---|---|
| To complete | | | | |

Done items: ___ · Not Done: ___ · Forecast change: ___ · Formal acceptance separate: ___

## 5. Retrospective

What helped: ___ · What slowed delivery: ___ · Evidence: ___

Improvement: ___ · Owner: ___ · Success measure: ___ · Review next sprint: ___

## 6. Weekly teacher status

Completed evidence: ___ · Next milestone: ___ · Actual/remaining hours: ___ · Top risks: ___ · Decision needed: ___ · Recovery proposal: ___

Update the agreed course-site plan with actual tasks, owners and dates separately; this package does not publish it.

