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
