# ClassroomCast — Source Verification Report

Checked 9 November 2026 against the eight files in `classroomCast_v2/docs/submission-2026-11-10/`. `classroomcast_v1` was consulted only to trace the origin of some content. No source file was modified.

**Files inspected (8 of 8):** 01-project-proposal (234 lines) · 02-requirements-SRS (309) · 03-roles-and-permissions (90) · 04-product-feature-catalogue (793) · 05-use-cases-and-process-flows (1,936) · 06-system-design-and-architecture (315) · 07-project-management-plan (967) · 08-testing-and-evaluation-plan (303).

## 1. Verified facts

| Item | Value | Source evidence | Status |
|---|---|---|---|
| Project name | ClassroomCast — Local Network Screen Sharing and Access Control System | v2 docs README; teacher specification | CONFIRMED |
| Team members | HENG NGUON HOUR (representative), CHANTHA MENGKONG, BUN SENGLEANG, HAK SENGKEA, HONG DYHENGMESA | 01 (risk register roster); 07 (team table) | CONFIRMED |
| Requirements | 63: NAC 20, T 11, S 10, CN 10, OR 12 | 02 register (63 unique IDs counted) | CONFIRMED |
| Priorities | 31 Must, 7 Should, 3 Could, 22 unlabeled (CN/OR, "proposed Must*") | 02 register | CONFIRMED (Must* is PROPOSED) |
| Roles | 4: SYS, TCH, STU, NET | 03 role model and permission matrix | CONFIRMED |
| Capability areas | 6 (entries per area: 7 / 11 / 13 / 22 / 7 / 8) | 04 area headings | CONFIRMED |
| Feature entries | 68 = 63 original + 2 unnumbered obligations + 3 proposed admin entries | 04 (68 `BF-` entries counted) | CONFIRMED |
| Product pillars | 4, mapped to the 6 areas | 04 opening table | CONFIRMED |
| Use cases | 15 (UC01–UC15) | 05 use-case catalogue | CONFIRMED |
| Process flows | 18 (F01–F18) | 05 section headings | CONFIRMED |
| Test specifications | 90 = 63 requirement cases + 7 admission + 5 architectural + 8 failure + 7 race | 08 test-case catalogue | CONFIRMED |
| Test execution status | All "Not run"; feasibility spikes SP01–SP05 "Not run" | 08 §1; 01 feasibility §5 | CONFIRMED — NOT TESTED |
| Implementation status | Documentation only; no software built | Every file header: "no teacher approval or product test execution claimed" | CONFIRMED — NOT IMPLEMENTED |
| Technology stack | React/Vite/TS, NestJS, SQLite (PostgreSQL alt.), self-hosted LiveKit, AdGuard Home, Caddy, Docker Compose | 06 architecture §1 ("Proposed"); 01 ("exact stack remains provisional"); decision D19 | PROPOSED |
| Deployment modes | Campus network and teacher-owned (portable) router; both in source scope | 06 infrastructure §2; 02 CN/OR | CONFIRMED in scope; campus authorization PENDING |
| Total effort estimate | 480 h = 420 work + 42 contingency + 18 reserve; about 10 h per member per week; 600 h nominal 12-week capacity | 01 resources §4 | CONFIRMED (as an estimate) |
| Development hours (~320 h) | 5 × 10 h × about 6.4 weeks (30 Nov – 13 Jan) | **Not found in sources.** Derived calculation; an earlier draft summary said ~325 h | NOT FOUND — derived |
| Sprint dates | S1 30 Nov–11 Dec · S2 14–25 Dec · S3 28 Dec–13 Jan 2027 | 07 latest site schedule | CONFIRMED (sprint content PROPOSED) |
| Release / presentation | Site release 27 Jan 2027; presentation 3 Feb 2027; editing deadline 25 Jan 23:59 | 07 schedule and date-conflict section; 01 timeline | CONFLICTING (see §2, item 9) |
| Scrum roles | Hour: Product Owner; Dyhengmesa: Scrum Master | 07 Scrum plan §2 | PROPOSED |
| Task owners | Three different allocations | 07 team table, 07 text note, 07 backlog leads | CONFLICTING |
| Out of scope | W01–W05 (custom SFU, native app, recording, LMS/ERP, student-screen control) | 01 scope §4 | PROPOSED |
| Database / API | 8 conceptual entities; 10 proposed endpoints | 06 database §2, API §2 | PROPOSED |

## 2. Discrepancies checked

| # | Issue | Finding | Needs confirmation from |
|---|---|---|---|
| 1 | Student capacity | The capacity is 50–150 students per classroom, as stated in the teacher specification and Files 01–08. | — confirmed |
| 2 | 480 h vs ~325 h | 480 h is the source estimate for the whole project. ~325 h (corrected to ~320 h) was a derived figure for the three build sprints only, not in any source file. They measure different things, so they do not contradict each other. The summary now labels 320 h as derived. | Team: confirm actual weekly availability over the holidays |
| 3 | Task owners | Three allocations: (a) the edited planning document table in 07; (b) the newer timeline described in 07 (BUN: main data and acceptance; CHANTHA: core use cases and demo deployment; HONG: shares UI); (c) backlog leads CC-001–CC-026 on the old six-sprint plan. Risk owners in 01 are a further, separate assignment. | Teacher and team |
| 4 | F01–F17 vs F01–F18 | The sources contain 18 flows. F01–F17 appears only in the README as an error to correct (from an external checklist). | — resolved |
| 5 | 63 requirements vs 68 features | Not a conflict: 68 = 63 + 2 unnumbered obligations + 3 proposed admin entries (stated in 04). | — |
| 6 | Tech stack consistency | 01 ("provisional") and 06 ("Proposed") agree. Both match the teacher specification's options (LiveKit or mediasoup; Node.js with optional NestJS). Not yet approved (D19). | Teacher (D19) |
| 7 | Campus vs teacher-owned router | Both modes are in source scope (06 infra §2: portable stays in scope until D18). The new MVP proposal builds router mode and documents campus mode. This is a **scope change** under the change-control rule in 01 ("do not remove Must requirements merely to fit a sprint"). | Teacher |
| 8 | Must / Should / Could | 31/7/3 confirmed; 22 CN/OR are unlabeled and only *proposed* as Must. The MVP moves two Should items (S08, NAC20) into Level A. | Teacher |
| 9 | 25 Jan vs 27 Jan vs 3 Feb | 01 gives a final editing deadline of 25 Jan 23:59. 07 shows release 27 Jan and presentation 3 Feb. 07 itself asks whether these are separate milestones. | Teacher |
| 10 | Six sprints vs three sprints | 01 (method, feasibility, timeline) and the 07 Scrum plan still describe six two-week sprints (2 Nov – 24 Jan). The 07 meeting overview states the three-sprint schedule takes precedence. | Teacher |
| 11 | Requirement → feature/flow/UC/test | All 63 requirements have a feature entry (04), flow and use case (02 register), user story and test case (08). No missing mapping found. | — |
| 12 | Earlier summary's mapping table | The earlier `00-SUMMARY-FOR-TEACHER.md` was too narrow. NAC is spread over Areas 03, 05 and 06 (not only 03), and over flows F01, F03, F09–F15, F17, F18 (not only F09–F15). T and S also use F12, F15, F16, F18. CN maps to F02 only and OR to F03 only. Corrected in the new document. | — |
| 13 | Earlier summary's test count | It said "63 test cases". The correct figure is 63 requirement cases plus 27 supplementary tests (90 in total). | — |

## 3. Correct requirement → feature → flow → use case mapping

| Group | Feature areas | Flows | Use cases |
|---|---|---|---|
| NAC01–NAC20 | 03 (NAC01–09, 14, 15, 18, 20); 05 (NAC10, 12, 13); 06 (NAC11, 16, 17, 19) | F01, F03, F09–F15, F17, F18 | UC05, UC06, UC08–UC10, UC12, UC13, UC15 |
| T01–T11 | 01 (T02–04, T07); 02 (T01, 05, 06, 08, 10, 11); 05 (T09) | F04–F08, F15, F16, F18 | UC01–UC04, UC10, UC11, UC13 |
| S01–S10 | 01 (S03–05); 02 (S01, 02, 08–10); 05 (S06, S07) | F05–F07, F12, F15, F16, F18 | UC02, UC03, UC07, UC10, UC11, UC13 |
| CN01–CN10 | 04 | F02 | UC14 |
| OR01–OR12 | 04 | F03 | UC15 |

## 4. MVP coverage check

All 63 requirements are placed in exactly one MVP level:

- **Level A (39):** T01–T08, S01–S08, NAC01–08, NAC10–13, NAC16–20, OR02, OR03, OR05, OR07, OR11, OR12. This includes all 31 Must items plus S08 and NAC20 (Should).
- **Level B (16):** CN01–CN10, OR01, OR04, OR06, OR08, OR09, OR10. CN06 appears in two Level B rows (campus documentation and capacity evaluation) but is counted once.
- **Level C (8):** T09, T10, S09, NAC09, NAC14 (Should); T11, S10, NAC15 (Could).

Total: 39 + 16 + 8 = 63 unique IDs, with no requirement left out.

## 5. Unresolved questions

See `ClassroomCast_Teacher_Meeting_Questions.md`. Other open design decisions in `07-teacher-review/04-open-questions.md` (D01/D14 accounts, D04 start trigger, D06/D07 rule precedence, D08/D09 pause and browser support, D10 certificates, D11 expiry timing, D13 data retention) are team design work. They do not need the teacher at this meeting.
