# ClassroomCast — Summary for the Teacher

**Team:** HENG NGUON HOUR (representative), CHANTHA MENGKONG, BUN SENGLEANG, HAK SENGKEA, HONG DYHENGMESA  
**Meeting:** 10 November 2026 · **Status:** Planning documents only. Nothing is built or tested yet.

## 1. What the project is

ClassroomCast is a local-network web system with three main functions:

1. **Screen sharing.** The teacher shares their screen and audio with 50–150 students. Students watch in a browser and install nothing.
2. **Class control.** The teacher creates a class with a join code and QR code, then approves, removes or blocks students.
3. **Website blocking from the dashboard.** An admin blocks AI sites, coding agents, social media and games using profiles such as Normal Class, Programming Lab and Exam Mode. A local DNS filter (AdGuard Home) enforces the rules, so nobody has to change router settings by hand.

It runs without internet, in two modes: on the **campus Wi-Fi** (with campus IT approval) or on a **teacher-owned router**.

## 2. What we uploaded (read in this order)

| # | File | What it shows | Size |
|---|---|---|---|
| 01 | Project Proposal | Goal, scope, what is excluded, team hours (about 480 h) | 234 lines |
| 02 | Requirements (SRS) | All 63 of your requirements (NAC, T, S, CN, OR) in one table | 309 lines |
| 03 | Roles & Permissions | 4 roles (Admin, Teacher, Student, Network Admin) and who can do what | 90 lines |
| 04 | Feature Catalogue | 68 feature cards grouped into 6 areas | 793 lines |
| 05 | Use Cases & Flows | 15 use cases (UC01–UC15) and 18 flow diagrams (F01–F18) | 1,936 lines |
| 06 | System Design | Architecture, database design, API list | 315 lines |
| 07 | Project Plan | Schedule: 3 sprints from Nov 30 to Jan 13, presentation Feb 3; task owners; risks | 967 lines |
| 08 | Test Plan | 63 test cases, one per requirement. Status: *Not run* | 303 lines |

**To review quickly, read 01, 03 and the schedule table in 07.** The other files hold the detail behind them.

## 3. How your requirements are covered

| Your requirement section | Our file |
|---|---|
| 1. Overview and target environment | 01 |
| 2. Network blocking (NAC01–NAC20) | 02, 04 (Area 03), 05 (F09–F15) |
| 3. Broadcasting (T01–T11, S01–S10) | 02, 04 (Areas 01–02), 05 (F04–F08) |
| 4–5. Campus mode (CN01–CN10) and router mode (OR01–OR12) | 02, 04 (Area 04), 05 (F02–F03) |
| 6. Architecture (React, Node.js, SFU, SQLite, AdGuard, Caddy, Docker) | 06 |

Priorities copied from your list: 31 Must, 7 Should and 3 Could. The 22 CN/OR items had no priority label, so we proposed treating them as Must.

## 4. The two folders

- **classroomcast_v1:** our first draft. It contains the requirements, architecture and the FigJam board images (feature cards, flow diagrams).
- **classroomCast_v2:** the cleaned-up, organised version. It reuses v1 content and fixes errors. Capacity is 50–150 students. Files 01–08 come from v2.

## 5. Proposed MVP scope (for your approval)

We have about 325 team hours for development and 3 sprints that include the holidays. To finish on time, we propose building a working minimum product (MVP) first, in **teacher-owned router mode**. We control that equipment, so we do not have to wait for campus IT.

| Level | What it includes | Requirement IDs |
|---|---|---|
| **A. Build and demo** | Teacher creates a class, students join with a code or QR, teacher approves them, then shares screen and audio. | T01–T08, S01–S08 |
| | Admin blocks categories and domains with profiles. Rules apply when class starts and restore when it ends, with status, audit log, emergency rollback and auto-expiry. | NAC01–08, NAC10–13, NAC16–20 |
| | Teacher-owned router setup that works fully offline | OR02, OR03, OR05, OR07, OR11, OR12 |
| **B. Design and document** | Campus mode: setup guide and IT checklist. We deploy it only if campus IT approves. | CN01–CN10 |
| | Full 150-student test: we test with 10–20 real laptops, simulate the rest, and report both results separately. | CN06, OR01, OR04, OR08 |
| | Hardware items: equipment list and setup guide | OR06, OR09, OR10 |
| **C. Only if time allows** | Streaming diagnostics, file sharing, history, downloads, hand-raise/polls, scheduling, import/export, group policies | T09–T11, S09–S10, NAC09, NAC14, NAC15 |

**Sprint goals:**

- **Sprint 1 (Nov 30 – Dec 11):** create a class, join with a code or QR, approve students; 1 teacher shares their screen with 3 laptops on our router; AdGuard blocks one domain.
- **Sprint 2 (Dec 14 – 25):** audio, quality settings, pause/resume, remove/block, reconnect; policy profiles and categories; apply when class starts and restore when it ends.
- **Sprint 3 (Dec 28 – Jan 13):** emergency rollback, auto-expiry, audit log, local-traffic protection; test with 10–20 laptops; bug fixing only, no new features.

## 6. Questions for you

1. Do you approve the MVP scope above (A = build, B = document, C = optional)?
2. Is testing with 10–20 real laptops plus simulation acceptable for the 150-student requirement?
3. Is it acceptable to deliver campus mode as design and documentation only, unless campus IT approves DNS blocking?
4. Deadlines: is the final editing deadline **Jan 25**, with the **Jan 27** release and **Feb 3** presentation as separate dates?
5. Two documents list different task owners. Which one is correct?
