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
