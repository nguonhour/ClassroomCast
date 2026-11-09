# Applying Chapters 1–12 to ClassroomCast

Reviewed from the twelve supplied PDFs in `IT-project-management/`. The notes below adapt the concepts, summaries and relevant worked examples to ClassroomCast. The chapters' Realtime Quiz names, budgets, dates, technology and pilot assumptions are teaching examples, not facts about this project. Slide numbers refer to the numbered slides/pages in those PDFs.

| Chapter and relevant slides | Lesson applied | ClassroomCast output |
|---|---|---|
| 1 — Introduction; 11, 13–15, 18–21 | Authorize purpose and roles through a charter; define measurable success and business justification; distinguish project delivery from ongoing operation | Charter, proposed Product Goal, sponsor-to-confirm field and handover in PROJECT-PLAN |
| 2 — Triple constraint; 8–10, 15–20 | Decide which constraints are fixed; validate assumptions; use MoSCoW and explicit trade-offs; compare baseline with actual results | Deadline fixed by supplied page; capacity assumed; original Must priorities preserved; capacity assumptions and reserve envelope made visible |
| 3 — Life cycle; 10–12, 19–24 | Tailor governance around iterative delivery; retain Scrum accountabilities/events/artifacts; close with acceptance and lessons | Six sprints, four review gates, DoD, Scrum responsibilities and closure package |
| 4 — Scope; 7–11, 14–24 | Link requirements to stories, WBS and tests; define exclusions; apply 100% rule; control baseline changes | WBS with estimates and evidence, BACKLOG.csv requirement links, scope/change rules |
| 5 — Scheduling; 4, 6, 8, 10–18, 20, 28 | Separate effort from duration; record dependencies; estimate in three points; level resources; calculate critical path from actual durations | Calendar roadmap, first-sprint personal capacity check and dependency diagram; CPM pending refined durations |
| 6 — Costs; 7–16, 27 | Estimate work packages, separate cash from effort, identify reserves, time-phase budget and measure earned value consistently | 420 h preliminary work estimate plus 60 h reserves versus 600 h published nominal capacity; pending cash budget; one proposed BAC convention |
| 7 — Quality; 8, 10, 18, 20, 28 | Make quality measurable; review the process and test the product; define Done; accept verified results | Q01–Q10 criteria, peer review, meaningful tests, pilot evidence and separate acceptance record |
| 8 — People; 4, 6, 8, 10–12, 29 | Give clear responsibility/authority; one accountable role per RACI row; respect individual resource calendars; avoid late staffing assumptions | Five named component leads, review partners, provisional capacity and shared quality ownership |
| 9 — Risk; 8, 12, 18–23, 27 | Write cause/event/effect; score risk; give owner, trigger, response and fallback; buy information through spikes | R01–R08, early HTTPS/SFU/DNS spikes, capacity decision and response triggers |
| 10 — Communication; 8, 18, 20, 24, 27 | Plan communication around audience decisions, document actions, keep one source of truth and define escalation | Weekly status, Scrum cadence, recorded decisions and external-blocker escalation |
| 11 — Stakeholders; 6, 12–13, 17, 20, 26 | Identify users and decision-makers; engage them through measurable actions; obtain acceptance and measure adoption | Lecturer/IT/teacher/student register, early IT decision, teacher trials and January pilot feedback |
| 12 — Procurement; 4, 7–8, 15–16, 25, 28 | Compare make/reuse/buy and total ownership cost; specify measurable acceptance; document procurement closure | Reuse SFU/filtering; inventory/borrow hardware; weighted selection if buying; renewal/return and ownership checklist |

## Responsibility matrix

R = performs the work; A = accountable for the result; C = consulted; I = informed. One A per row; A/R means the same person also performs work. This matrix proposes team coordination; lecturer and campus IT retain their actual acceptance/authorization powers.

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

## Correct interpretation and source boundaries

The course decks use different illustrative hours, dates and cost examples across chapters. Their numbers should not be combined into one ClassroomCast baseline. Our baseline stays a draft until actual availability, package estimates and approval are recorded.

Chapter 4 slides 19/23 describe sprint scope too rigidly. The [official Scrum Guide](https://scrumguides.org/scrum-guide.html) allows scope clarification and renegotiation with the Product Owner as learning occurs, without endangering the Sprint Goal; Developers own the Sprint Backlog. We use that rule in TEAM-AND-SCRUM.

A Sprint Review inspects results and adapts plans with stakeholders. A project's formal acceptance/sign-off is an additional governance practice, rather than an automatic outcome of holding the Scrum event.

Some cost slides switch between including and excluding contingency in earned-value BAC. PROJECT-PLAN explicitly chooses an inclusive convention and separates management reserve, so the project's own reporting can remain internally consistent.

## Technical sources checked alongside the course

- [MDN: getDisplayMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getDisplayMedia) — secure context, source selection and permission requirements for the teacher flow.
- [LiveKit deployment](https://docs.livekit.io/transport/self-hosting/deployment/) — trusted certificates and self-hosted connectivity; informs early feasibility tests.
- [LiveKit ports and firewall](https://docs.livekit.io/transport/self-hosting/ports-firewall/) — signaling and media have different connectivity needs.
- [AdGuard Home clients](https://adguard-dns.io/kb/adguard-home/clients/) and [DNS rule syntax](https://adguard-dns.io/kb/general/dns-filtering-syntax/) — client identification and domain-rule capabilities to validate during adapter development.

These sources support platform constraints. The selected stack, sprint durations, estimates, risk ratings and proposed quality targets are project design judgments and must be validated by the team.
