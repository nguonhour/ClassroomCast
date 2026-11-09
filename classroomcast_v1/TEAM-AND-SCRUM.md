# Team responsibilities and Scrum workflow

Updated 2 November 2026 using the skills and approximately 10 h/person/week published on the team page supplied by Hour. Technical assignments remain proposals; the representative designation is confirmed by the supplied roster. WebRTC and DNS enforcement expertise were not listed, so those areas include explicit learning spikes.

## Division among five members

| Member | Primary responsibility | Concrete deliverables | Review partner |
|---|---|---|---|
| **HENG NGUON HOUR ★** — ហេង ងួនហ៊ួរ | Representative, proposed Product Owner, application integration and student frontend | Ordered backlog; lecturer communication; weekly status; student join/view interface with Sengkea; end-to-end integration and acceptance coordination | Sengkea reviews UI; Sengleang reviews API integration |
| **BUN SENGLEANG** — ប៊ុន សេងលៀង | Classroom backend, REST APIs and database | Class/session APIs; authentication and roles; admission/removal; schema/migrations; join-code lifecycle; API tests | Dyhengmesa |
| **CHANTHA MENGKONG** — ចន្ថា ម៉េងគង់ | DevOps, SFU hosting and network enforcement adapter | Local LiveKit and Docker setup; CI/CD; HTTPS/DNS spike; AdGuard Home adapter; network diagnostics and recovery runbooks | Dyhengmesa for policy integration; Sengleang for server changes |
| **HAK SENGKEA** — ហាក់ សេងគា | Frontend and UI/UX lead | Teacher/admin dashboards; QR/code display; participant controls; policy editor/status UI; shared components; student UI support | Hour |
| **HONG DYHENGMESA** — ហុង ឌីហេងមេសា | NestJS policy service, media/application integration; proposed Scrum Master | Profile/lease/apply/expiry orchestration; LiveKit token/SDK integration; teacher publishing and student subscription module; Scrum facilitation | Sengleang for backend; Mengkong for media/network |

Hour coordinates acceptance evidence with the whole team. Each person tests and documents their own component; peer reviews and integration checks are shared. Mengkong and Dyhengmesa pair on the unfamiliar media/enforcement boundaries. Hour supports UI and integration rather than taking every backend task.

Scrum accountabilities and technical ownership are separate hats. Hour is the proposed Product Owner and still contributes code. Dyhengmesa is the proposed Scrum Master and still contributes code. The Scrum Master facilitates effectiveness and removes impediments; the role does not assign everyone's tasks. The Developers jointly plan and adapt the Sprint Backlog.

The lecturer/sponsor accepts course deliverables and approves changes to agreed release constraints. Their identity and authority must be confirmed; team representative status alone does not establish sponsor authority.

## Published capacity and sprint planning

The supplied team page states **approximately 10 hours per member per week**, or **50 team hours/week**, covering all project work. Use this as the current planning basis and confirm each person's exam/holiday calendar before a sprint.

For a two-week sprint: 5 people × 10 hours × 2 weeks = **100 team hours**. Initially select at most about **80 hours of planned work**, including ceremonies, reviews, learning and documentation. The first sprint deliberately remains at 64 h while the technical feasibility is unknown. Confirm personal capacity as well as the total.

Keep one main implementation item in progress per member. Pair when a blocked item needs another skill. Review queues should have at most three items before the team helps clear them.

## Scrum rhythm

Use six two-week sprints from 2 November 2026 through 24 January 2027. Holidays and exams must be reflected in capacity; calendar duration does not guarantee 100 hours.

| Event | Proposed timebox | Purpose and output |
|---|---|---|
| Sprint Planning | 90 minutes, first Monday | Agree Sprint Goal; Developers select achievable items and plan tasks |
| Daily Scrum | 15 minutes each working day | Developers inspect progress toward the goal and adapt the plan; record blockers |
| Backlog refinement | 30 minutes weekly | Split upcoming work, clarify acceptance and dependencies; supporting practice |
| Sprint Review | 60 minutes at the end of sprint | Demonstrate usable results with users/lecturer; capture feedback and reorder backlog |
| Sprint Retrospective | 45 minutes after review | Choose one measurable improvement and an owner |
| Weekly project status | 15 minutes to prepare, Friday | Hour records completed evidence, forecast, hours, top risks and decisions needed |

Agree meeting clock times in the first team session. Use the last available working day for live review/retro if the sprint ends on a weekend. Schedule availability before committing work across holidays.

The Product Backlog carries the Product Goal. The Sprint Backlog carries a Sprint Goal. Each usable Increment meets the Definition of Done. These commitments follow the [official Scrum Guide](https://scrumguides.org/scrum-guide.html).

## First sprint: 2–15 November 2026

**Sprint Goal:** On a local network, a teacher can create a class and share a screen that a student can join and view, while the team identifies the prerequisites for HTTPS and network enforcement.

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

Divide the 10 shared hours as 2 per member. Resulting planned totals: Hour 16, Sengleang 10, Mengkong 12, Sengkea 12, Dyhengmesa 14 hours. Each is within the published approximate 20-hour personal sprint capacity. The remaining capacity is uncommitted; use it for validated follow-up work, pairing or learning after checking progress. If an estimate grows, Developers adapt the scope with the Product Owner while protecting the Sprint Goal.

## Definition of Ready — team working agreement

An item has a requirement/WBS reference, owner, acceptance criteria, dependencies, rough estimate and a page sketch or API contract when relevant. Split work too large for one sprint. This checklist supports planning; it is not an additional Scrum artifact.

## Definition of Done

1. Acceptance criteria have been demonstrated and evidence attached to the item.
2. Another member reviews the change; relevant automated checks pass.
3. Meaningful tests cover new business rules and failure paths, especially permissions, session state and policy rollback.
4. Changed UI works on the agreed laptop/browser matrix; media limitations are described accurately.
5. Required runtime assets are local and the affected flow is checked without WAN when relevant.
6. Secrets stay on the server; browser permissions and server authorization are respected.
7. API/configuration changes and recovery steps are documented; known limitations are recorded.
8. The result integrates with the current application and is usable. Incomplete work returns to the backlog and earns no completed-story credit.

## Board and decision rules

Board columns: Backlog → Ready → In progress → Review/test → Done. Add a blocked flag and record the blocker, owner and next action. A pull request links its backlog item and requirement IDs. Review within one working day where availability permits.

The Product Owner orders the Product Backlog. Developers own their Sprint Backlog and may renegotiate selected scope with the Product Owner as they learn; changes must preserve the Sprint Goal. This corrects the overly rigid sprint-scope wording on Chapter 4 slides 19 and 23. Only the Product Owner can cancel a sprint if its goal becomes obsolete, consistent with the official Scrum Guide.

Record release-baseline changes with request, impact on scope/time/effort/risk, decision, owner and date. Refer changes to agreed Must requirements, acceptance criteria, cash or deadline to the lecturer/sponsor. Routine implementation decisions and backlog reordering stay with the team within the agreed constraints.

Escalate a blocker after one working day with a proposed solution. Hour contacts the lecturer or campus IT when it exceeds the team's authority. Keep decisions in the tracker/documents even if discussion happens in chat.
