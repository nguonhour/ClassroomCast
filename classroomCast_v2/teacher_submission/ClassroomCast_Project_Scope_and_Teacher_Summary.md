---
pagetitle: ClassroomCast — Project Scope & Summary for Teacher Review
lang: en
---

<header class="cover">
<div class="kicker">IT Project Management · Teacher review package · Version 1.0</div>
<h1>ClassroomCast — Project Scope &amp; Summary for Teacher Review</h1>
<div class="sub">Local Network Screen Sharing and Access Control System</div>
</header>

| | |
|---|---|
| **Team** | HENG NGUON HOUR (Project Representative) · CHANTHA MENGKONG · BUN SENGLEANG · HAK SENGKEA · HONG DYHENGMESA |
| **Meeting** | 10 November 2026 |
| **Status** | Planning and analysis documents only. <span class="b ni">NOT IMPLEMENTED</span> <span class="b nt">NOT TESTED</span> |
| **Sources** | Files 01–08 in `classroomCast_v2/docs/submission-2026-11-10`, checked on 9 November 2026 |

<div class="legend">Status labels used in this document: <span class="b c">CONFIRMED</span> stated in the source files · <span class="b p">PROPOSED</span> team recommendation, not approved · <span class="b pe">PENDING</span> needs a teacher, team or campus IT decision · <span class="b cf">CONFLICTING</span> the source files disagree · <span class="b ni">NOT IMPLEMENTED</span> · <span class="b nt">NOT TESTED</span></div>

## 1. Project overview

**Problem.** In a classroom of 50–150 students, many students cannot read the projector screen clearly. Teachers also have no simple way to stop students from opening AI assistants, coding agents or other distracting websites during labs and exams. Today, blocking websites means changing router settings by hand for every class.

**Vision** <span class="b p">PROPOSED</span>. Teachers can show their screen directly on student laptops over the local network, manage who joins, and apply approved website restrictions from one dashboard. The system keeps working without an internet connection.

**Three main functions**

1. **Classroom broadcasting.** The teacher shares a screen, window or tab with supported audio. Students watch in a web browser and install no application.
2. **Classroom management.** The teacher creates a class with a join code and QR code, then approves, rejects, removes or blocks participants.
3. **Software-managed website restrictions.** Authorized administrators choose profiles such as *Normal Class*, *Programming Lab* and *Exam Mode*. A local DNS filter enforces the rules. The team proposes **AdGuard Home** for this: a self-hosted service that refuses to look up blocked website names.

**Key figures** (verified against Files 01–08)

<div class="kpis">
<div><b>63</b><span>original requirements</span></div>
<div><b>4</b><span>user roles</span></div>
<div><b>68</b><span>feature entries in 6 areas</span></div>
<div><b>15</b><span>use cases (UC01–UC15)</span></div>
<div><b>18</b><span>process flows (F01–F18)</span></div>
<div><b>90</b><span>test specifications (63 + 27)</span></div>
</div>

Requirement priorities as given in the specification: **31 Must, 7 Should, 3 Could**. The 22 campus-network (CN) and teacher-owned-router (OR) obligations have no priority label. The team proposes treating them as Must <span class="b pe">PENDING</span>.

<div class="pb"></div>

## 2. Objectives and project scope

**Objectives** <span class="b p">PROPOSED</span>. Each objective has a measurable check in File 01.

- Deliver teacher screen and audio to admitted students on the local network (F04–F07).
- Allow only the owning teacher to control a class and its participants (role and admission checks).
- Keep working when the internet (WAN) is disconnected (test AT07).
- Apply only authorized website restrictions, and verify them from a student device (F10).
- Restore the previous network policy safely when a class ends, a rule expires, or an emergency occurs (AT05).
- Report capacity and quality honestly, keeping physical-device and simulated results separate (AT02/AT03).

**Target users.** One teacher and 50–150 students per classroom <span class="b c">CONFIRMED</span>, plus system and network administrators.

<div class="cols">
<div>

**In scope** <span class="b c">CONFIRMED</span>

- Local screen and audio broadcasting through a shared media server
- Class creation, join code, QR code and admission control
- Policy profiles, categories, domains and exceptions
- Automatic apply when a class starts and restore when it ends
- Enforcement status, audit log, emergency rollback, rule expiry
- Offline operation, diagnostics, and both deployment modes

</div>
<div>

**Out of scope** <span class="b p">PROPOSED</span> (W01–W05)

- W01 Building our own media server; we reuse an existing one
- W02 A required student app; access stays browser-only
- W03 Recording or archiving class video
- W04 LMS or ERP integration
- W05 Remote control or capture of student screens

</div>
</div>

**Deployment assumptions**

| Mode | Assumption | Status |
|---|---|---|
| A. Campus Wi-Fi / LAN | Uses the existing campus network. Hosting and DNS changes require written approval from campus IT (CN05). The system must never bypass campus controls. | <span class="b pe">PENDING</span> |
| B. Teacher-owned router | A portable network controlled by the team: server plus Wi-Fi access points, fully offline (OR01–OR12). | <span class="b c">CONFIRMED</span> in scope |
| Host | An existing school Ubuntu/Linux server was mentioned. Its hardware and permissions have not been inventoried. | <span class="b pe">PENDING</span> |

**Technical constraints**

- Browsers allow screen and microphone capture only on secure (HTTPS) pages, so the local server needs a trusted certificate.
- Supported audio sources differ by browser and operating system; system audio is not available everywhere.
- DNS filtering can be bypassed with VPNs, alternate or encrypted DNS, direct IP addresses, or locally installed AI tools. We will document this limitation, not hide it.
- Restrictions must never block ClassroomCast itself (NAC18).
- Router credentials and API secrets stay on the server (NAC17). We collect as little browsing history as possible (NAC19).

<div class="pb"></div>

## 3. System roles and product structure

**Four roles** <span class="b c">CONFIRMED</span> (File 03). Permissions are checked on the server. Each role is limited to its own classes or assigned network scope.

| Role | Main responsibility | Cannot do |
|---|---|---|
| **System Administrator (SYS)** | Manage accounts, roles, application settings, policy profiles; read audit and health records | Teach, view class media, or change network infrastructure |
| **Teacher (TCH)** | Create and run own classes; share screen and audio; admit, remove or block students; select an approved profile | Edit DNS or router settings, see secrets, or edit policy rules |
| **Student (STU)** | Request admission; watch and listen; use permitted materials | Publish media, control the class, or change policies |
| **IT / Network Administrator (NET)** | Connect DNS, gateway or router integrations; apply, verify and recover network policies | Act without campus IT or equipment-owner authorization |

**Six capability areas and 68 feature entries** <span class="b c">CONFIRMED</span> (File 04). The four product pillars in the specification map to these six areas. Area 06 supports all four.

| Area | Pillar | Entries | Main requirement IDs |
|---|---|---|---|
| 01 Classroom broadcasting | Broadcasting | 7 | T02–T04, T07, S03–S05 |
| 02 Management and participation | Classroom management | 11 | T01, T05, T06, T08, T10, T11, S01, S02, S08–S10 |
| 03 Network access control | Network access control | 13 | NAC01–09, NAC14, NAC15, NAC18, NAC20 |
| 04 Deployment and infrastructure | Network administration | 22 | CN01–CN10, OR01–OR12 |
| 05 Diagnostics, verification, recovery | Network administration | 7 | S06, S07, T09, NAC10, NAC12, NAC13 + 1 basic-health entry |
| 06 Administration and security | Supports all pillars | 8 | NAC11, NAC16, NAC17, NAC19 + 4 administration entries |

68 entries = 63 original requirements + 2 required obligations with no ID + 3 proposed administration entries (accounts, role assignment, settings). **These entries describe requirements. They are not finished features.** <span class="b ni">NOT IMPLEMENTED</span>

**Traceability** <span class="b c">CONFIRMED</span>. Every one of the 63 requirements links to a feature entry, a process flow, a use case, a user story and a test case.

| Requirement group | Features | Flows | Use cases |
|---|---|---|---|
| NAC01–NAC20 Network access control | Areas 03, 05, 06 | F01, F03, F09–F15, F17, F18 | UC05, UC06, UC08–UC10, UC12, UC13, UC15 |
| T01–T11 Teacher | Areas 01, 02, 05 | F04–F08, F15, F16, F18 | UC01–UC04, UC10, UC11, UC13 |
| S01–S10 Student | Areas 01, 02, 05 | F05–F07, F12, F15, F16, F18 | UC02, UC03, UC07, UC10, UC11, UC13 |
| CN01–CN10 Campus network | Area 04 | F02 | UC14 |
| OR01–OR12 Teacher-owned router | Area 04 | F03 | UC15 |

<div class="pb"></div>

## 4. Proposed system architecture

The architecture keeps every component on the local network. One teacher stream goes to a **Selective Forwarding Unit (SFU)**: a media server that receives the stream once and forwards a copy to each admitted student. The teacher's laptop does not have to upload 150 separate streams.

<figure class="arch">
<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Helvetica, Arial, sans-serif" font-size="12">
<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1e3a8a"/></marker></defs>
<rect x="8" y="8" width="744" height="314" rx="10" fill="#f5f9ff" stroke="#c7d6ee" stroke-dasharray="5 4"/>
<text x="22" y="28" fill="#1e3a8a" font-weight="700" font-size="11">LOCAL NETWORK — campus LAN/Wi-Fi or teacher-owned router (works without internet)</text>
<g fill="#fff" stroke="#1e3a8a" stroke-width="1.4">
<rect x="24" y="50" width="150" height="50" rx="8"/><rect x="24" y="140" width="150" height="50" rx="8"/><rect x="24" y="232" width="150" height="50" rx="8"/>
</g>
<text x="99" y="71" text-anchor="middle" font-weight="700" fill="#0b1f4d">Teacher browser</text><text x="99" y="88" text-anchor="middle" fill="#334155">screen + audio capture</text>
<text x="99" y="161" text-anchor="middle" font-weight="700" fill="#0b1f4d">Admin dashboard</text><text x="99" y="178" text-anchor="middle" fill="#334155">SYS / NET roles</text>
<text x="99" y="253" text-anchor="middle" font-weight="700" fill="#0b1f4d">Student browsers</text><text x="99" y="270" text-anchor="middle" fill="#334155">50–150 laptops</text>
<rect x="262" y="118" width="190" height="94" rx="8" fill="#1e3a8a"/>
<text x="357" y="142" text-anchor="middle" font-weight="700" fill="#fff">Web app + backend API</text>
<text x="357" y="160" text-anchor="middle" fill="#dbeafe">sessions · admission · roles</text>
<text x="357" y="176" text-anchor="middle" fill="#dbeafe">policy manager · audit</text>
<text x="357" y="198" text-anchor="middle" fill="#93c5fd" font-size="11">behind local HTTPS proxy</text>
<g fill="#fff" stroke="#0f766e" stroke-width="1.4">
<rect x="262" y="40" width="190" height="52" rx="8"/><rect x="262" y="246" width="190" height="52" rx="8"/>
<rect x="540" y="118" width="190" height="52" rx="8"/><rect x="540" y="232" width="190" height="66" rx="8"/>
</g>
<text x="357" y="62" text-anchor="middle" font-weight="700" fill="#0b1f4d">SFU media server</text><text x="357" y="80" text-anchor="middle" fill="#334155">forwards one stream to many</text>
<text x="357" y="268" text-anchor="middle" font-weight="700" fill="#0b1f4d">Database</text><text x="357" y="286" text-anchor="middle" fill="#334155" font-size="11">sessions · profiles · audit (no video)</text>
<text x="635" y="140" text-anchor="middle" font-weight="700" fill="#0b1f4d">DNS filter (AdGuard Home)</text><text x="635" y="158" text-anchor="middle" fill="#334155">applies domain rules</text>
<text x="635" y="254" text-anchor="middle" font-weight="700" fill="#0b1f4d">Optional router / firewall</text><text x="635" y="272" text-anchor="middle" fill="#334155">adapter, only where</text><text x="635" y="288" text-anchor="middle" fill="#334155">supported and authorized</text>
<g stroke="#1e3a8a" stroke-width="1.5" fill="none" marker-end="url(#a)">
<path d="M174,70 L260,66"/><path d="M262,80 C210,140 210,200 176,250"/>
<path d="M174,92 L262,140"/><path d="M174,165 L260,165"/><path d="M174,250 L262,195"/>
<path d="M357,212 L357,244"/><path d="M357,118 L357,94"/>
<path d="M452,148 L538,144"/><path d="M452,190 C500,220 510,250 538,262"/>
<path d="M110,282 V312 H496 V190 H610 V174"/>
</g>
<g fill="#475569" font-size="10.5">
<text x="190" y="58">publish media</text><text x="186" y="216">watch</text><text x="200" y="142">controls</text>
<text x="462" y="138">apply / verify</text><text x="300" y="307">student DNS lookups</text>
</g>
<text x="660" y="100" text-anchor="middle" fill="#64748b" font-size="10.5">→ internet only when WAN is available</text>
</svg>
<figcaption>High-level architecture. Box roles <span class="b c">CONFIRMED</span>; product names inside boxes <span class="b p">PROPOSED</span>.</figcaption>
</figure>

**Design decisions in the specification** <span class="b c">CONFIRMED</span>

- Use an SFU, not a direct teacher-to-every-student connection.
- Keep the web app, signaling, SFU, policy manager and DNS filter on the local network.
- Keep secrets on the server only. Show the configured policy and the actually enforced policy separately.
- Provide health checks, logs and recovery procedures. Serve the app over local HTTPS for screen capture.

**Proposed technology** <span class="b p">PROPOSED</span>. Final choice after feasibility tests (decision D19).

| Layer | Proposed choice |
|---|---|
| Frontend | React + Vite + TypeScript |
| Backend API and signaling | Node.js (NestJS) |
| Media server (SFU) | Self-hosted LiveKit (mediasoup is the alternative named in the specification) |
| Database | SQLite first; PostgreSQL if needed |
| DNS enforcement | AdGuard Home |
| HTTPS proxy / deployment | Caddy · Docker Compose |

**Data and API design** <span class="b p">PROPOSED</span>. The conceptual model has 8 entities: User, ClassroomSession, Participant, PolicyProfile/PolicyVersion, EnforcementScope, PolicyLease, PolicyOperation and AuditEvent. A list of 10 API endpoints is drafted, such as `POST /api/sessions` and `POST /api/scopes/:id/restore`. Detailed field and request formats are still to be designed.

<div class="pb"></div>

## 5. Proposed MVP scope

<div class="callout"><b>Why an MVP?</b> Five members at about 10 hours a week each (File 01) give roughly <b>320 hours</b> across the three build sprints (30 Nov – 13 Jan). This figure is <b>our own calculation, not stated in the source files</b>. The whole project estimate is 480 hours (420 work + 42 contingency + 18 reserve). This covers design, testing and closing as well as the sprints. The sprints include the year-end holidays. We therefore propose building and demonstrating the core product first in <b>teacher-owned router mode</b>, because the team controls that equipment and does not need to wait for campus IT. <span class="b p">PROPOSED</span> <span class="b pe">PENDING</span> teacher approval.</div>

<div class="level la">

**Level A — Build and demonstrate**

| What will work in the demo | Requirement IDs |
|---|---|
| Create a class; students join by URL, QR or code with a name; teacher approves | T01, T05, T06, T08, S01, S02, S07, S08 |
| Teacher shares screen and audio; start, stop, pause and resume; quality settings | T02, T03, T04, T07 |
| Students watch live, control volume, use fullscreen, and reconnect after short drops | S03, S04, S05, S06 |
| Profiles, categories, domains, allow or block by default, exceptions | NAC01–NAC04, NAC07, NAC08 |
| Rules apply when a class starts and restore when it ends; status shown; actions logged | NAC05, NAC06, NAC10, NAC11 |
| Emergency rollback, automatic rule expiry, admin-only control, server-side secrets, ClassroomCast never blocked, minimal browsing data, offline rule storage | NAC12, NAC13, NAC16–NAC20 |
| Teacher-owned router setup that works fully offline | OR02, OR03, OR05, OR07, OR11, OR12 |

All 31 Must requirements are in Level A. Two Should items move up because the core needs them: **S08** (student name, needed for the approval step) and **NAC20** (offline rules, built into AdGuard Home).

</div>

<div class="level lb">

**Level B — Design and document**

| Deliverable | Requirement IDs |
|---|---|
| Campus-mode architecture, setup guide and campus IT approval checklist. We deploy in campus mode only if campus IT gives written approval. | CN01–CN10 |
| Capacity evaluation: test with about 10–20 real laptops, simulate the rest at 50/100/150 viewers, and report the two separately | CN06, OR01, OR04, OR08 |
| Hardware list and portable-kit setup guide | OR06, OR09, OR10 |

*Moving campus deployment to documentation only is a **scope change**. Under our change-control rule, the teacher must approve it.*

</div>

<div class="level lc">

**Level C — Optional, only if time allows**

| Feature | Requirement IDs | Source priority |
|---|---|---|
| Streaming diagnostics · file sharing · downloads | T09, T10, S09 | Should |
| Scheduled restrictions · policy import/export | NAC09, NAC14 | Should |
| Session history · hand-raise/questions/polls · group/device policies | T11, S10, NAC15 | Could |

</div>

<div class="pb"></div>

## 6. Project schedule and team plan

**Timeline** <span class="b c">CONFIRMED</span> from the course website plan (File 07). Sprint goals <span class="b p">PROPOSED</span>.

| Phase | Dates | Goal |
|---|---|---|
| Preparation | 10–17 Nov 2026 | Requirements, stories, scope and proposal review; **teacher approval** |
| Design | 18–27 Nov | Architecture, data model, UI, API, test plan; feasibility tests SP01–SP03 (HTTPS, SFU, DNS apply/restore) |
| **Sprint 1** | 30 Nov – 11 Dec | Create a class, join by code or QR, approve students. One teacher shares a screen with about 3 laptops on our router. AdGuard blocks one test domain. |
| **Sprint 2** | 14 – 25 Dec | Audio, quality, pause/resume, remove/block, reconnect; profiles and categories; apply at class start and restore at class end |
| **Sprint 3** | 28 Dec – 13 Jan 2027 | Emergency rollback, expiry, audit log, protect local traffic; test with 10–20 laptops; **bug fixing only, no new features** |
| Testing and release | 14 – 27 Jan | Acceptance tests and defect fixes; demo and user guide 14–20 Jan; site release 27 Jan |
| Closing | 28 Jan – 3 Feb | Final report, slides and rehearsal; **final presentation 3 Feb** |

The sprint goals above follow File 07's sprint focus. They add the teacher-owned router as the first environment. <span class="b cf">CONFLICTING</span> File 01 and the Scrum plan in File 07 still describe an older **six-sprint** plan (2 Nov – 24 Jan). File 07 says the three-sprint plan replaces it. The teacher should confirm.

**Team roles** <span class="b p">PROPOSED</span>. HENG NGUON HOUR is Product Owner and HONG DYHENGMESA is Scrum Master; all five members are Developers.

**Task owners** <span class="b cf">CONFLICTING</span>. The sources contain three different allocations. The edited planning document is shown below, followed by the differences in the newer timeline.

| Member | Edited planning document | Newer timeline differs |
|---|---|---|
| HENG NGUON HOUR | Requirements/stories, sign-in/roles, search/reports/polish, presentation | — |
| CHANTHA MENGKONG | Architecture/data model, main-data operations, acceptance/bug fixes | Core use cases, demo deployment |
| BUN SENGLEANG | UI mockups, core use cases, demo deployment | Main data, acceptance |
| HAK SENGKEA | Test plan, unit/integration tests, user guide | — |
| HONG DYHENGMESA | Sprint planning/backlog, remaining use cases, final report | Also shares UI work |

A third allocation, the backlog leads for CC-001 to CC-026, follows the old six-sprint plan. Task names such as "search/reports/polish" come from a generic template and should be renamed to match ClassroomCast features.

**Key dependencies and schedule risks**

| Risk / dependency | Response |
|---|---|
| Campus IT may not authorize DNS changes (R01) | Develop on the teacher-owned router; campus mode stays Level B until written approval |
| Wi-Fi or server capacity unknown (R02) | Wired server, staged tests, equipment inventory before Sprint 1 |
| Trusted HTTPS on student laptops (R03) | Two-laptop HTTPS test during the design phase |
| Policy restore fails after a crash (R04) | Store the previous policy first; restart and restore drills in Sprint 3 |
| Work exceeds available hours (R07) | MVP levels A/B/C; defer Level C first |
| Holidays inside Sprints 2–3 | Confirm each member's availability; no new features in Sprint 3 |

<div class="pb"></div>

## 7. Testing and evaluation

**Current status:** test cases are specified, but none has been run. <span class="b nt">NOT TESTED</span> All five feasibility tests (SP01–SP05) are also *Not run*. No result in this package is a pass.

**Test inventory** <span class="b c">CONFIRMED</span> (File 08)

| Test group | Count | What it checks |
|---|---|---|
| Requirement test cases (TC-NAC, TC-T, TC-S, TC-CN, TC-OR) | 63 | One test case for each original requirement |
| Admission edge cases (TC-ADM01–07) | 7 | Invalid codes, rejection, last-seat race, unauthorized approval |
| Architectural cases (TC-AUTH, LOCAL, SFU, RECOVERY, PRIVACY) | 5 | Permissions, offline operation, SFU path, recovery, secret protection |
| Isolated failure scenarios (TC-FAIL01–08) | 8 | Internet loss, Wi-Fi loss, backend/SFU/DNS/HTTPS failure |
| Workflow race cases (TC-CTRL01–04, TC-CLOSE01–03) | 7 | Late or repeated actions during stop and end class |
| **Total** | **90** | |

**Test levels**

- **Functional:** class creation, joining, broadcasting, roster control, profiles and full teacher/student workflows.
- **Security:** cross-class access is denied, students cannot publish, revoked students cannot rejoin, secrets never reach the browser, and audit records exclude browsing history.
- **Network-policy verification and restoration:** from a student laptop, a blocked domain fails and an allowed domain works. ClassroomCast stays reachable throughout. After a class ends, an emergency or an expiry, the previous policy returns. A saved profile is never shown as "enforced" without this check.
- **Performance:** staged 50 / 100 / 150 viewers for 30 minutes each, measuring delay, freezes, packet loss and server/Wi-Fi load.

**Proposed acceptance targets** <span class="b p">PROPOSED</span> (need agreement, decision D12)

| ID | Target |
|---|---|
| AT01 | Join page loads within 5 s on the local network |
| AT02 | 720p at 15 fps; screen-to-student delay ≤ 1 s (95th percentile) |
| AT03 | 50/100/150 viewers for 30 min with playback active in ≥ 98% of checks |
| AT04 / AT05 | Policy applied and verified within 30 s; previous policy restored within 30 s |
| AT06 | Reconnect within 15 s after a 10 s drop, in at least 9 of 10 attempts |
| AT07 | A fresh browser joins a class with the internet disconnected |

**Physical versus simulated clients.** Real laptops on Wi-Fi test the radio network and the browsers. Simulated viewers test only server load. We will report the two separately and **will not claim 150-student capacity until it is measured**.

<div class="pb"></div>

## 8. Teacher approval and next steps

**Decisions requested at the meeting** <span class="b pe">PENDING</span>

| # | Decision | Our proposal |
|---|---|---|
| 1 | **MVP scope.** Approve Levels A (build), B (document) and C (optional)? | Approve. This includes moving S08 and NAC20 into Level A. |
| 2 | **Capacity evaluation.** Is testing with 10–20 real laptops plus simulated viewers acceptable for the 150-student target? | Yes, reported separately (D12) |
| 3 | **Campus mode.** Deliver it as design and documentation unless campus IT gives written approval? Who is the campus IT contact? | Yes, as a recorded scope change |
| 4 | **Schedule.** Is the 25 Jan editing deadline separate from the 27 Jan release and the 3 Feb presentation? Does the three-sprint plan replace the six-sprint plan? | Finish internal review by 22 Jan |
| 5 | **Task owners.** Which of the three allocations is authoritative? | Team agrees one list at this meeting |
| 6 | **Acceptance targets.** Accept AT01–AT07 as written, or adjust them? | Accept as starting targets |
| 7 | **Exclusions.** Approve the out-of-scope items W01–W05? | Approve |
| 8 | **Technology.** Accept the proposed stack, subject to feasibility tests (D19)? | Accept as a proposal |

**Next steps after approval**

1. Record the teacher's decisions in the decision log (`07-teacher-review/03-feedback-and-decision-log.md`).
2. Update the backlog and sprint plan in File 07 to match the approved MVP and one agreed task allocation.
3. List the available equipment: router, access points, server or mini-PC, and test laptops.
4. During the design phase (18–27 Nov), run the feasibility tests: trusted HTTPS (SP01), SFU screen and audio with two viewers (SP02), and AdGuard apply/restore (SP03).
5. Contact campus IT about DNS authorization (CN05). Record the answer, whatever it is.
6. Rename the generic task names to ClassroomCast features before Sprint 1 starts on 30 Nov.

<div class="end">This document is a summary. The full detail is in Files 01–08, and the fact checks are in <i>ClassroomCast_Source_Verification.md</i>.</div>
