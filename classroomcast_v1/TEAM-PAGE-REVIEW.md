# Team-page alignment review

Updated 2 November 2026 from the screenshot and pasted team-page content supplied by Hour. This records the supplied snapshot; it is not a live verification or an edit of gicitc.com.

## Confirmed from the supplied page

- Team: **CodeHub**, presented as **Code Hub** in the profile.
- Project: **ClassroomCast — Local Network Screen Sharing and Access Control System**.
- Five members, with **HENG NGUON HOUR** designated representative.
- Published approximate availability: **10 h/member/week**, **50 team h/week**.
- The team page provides a planning-poker room for estimating backlog stories together.

## Revised assignments based on listed skills

| Member | Skills stated on the profile | ClassroomCast lead responsibility |
|---|---|---|
| HENG NGUON HOUR | Web, Java/Spring Boot, React/Vue, database design | Representative, proposed Product Owner, student UI and end-to-end integration |
| BUN SENGLEANG | Full stack, backend, REST APIs, database management | Classroom/session backend, authorization and database |
| CHANTHA MENGKONG | Backend/APIs, PostgreSQL, DevOps/CI/CD | Local deployment, SFU hosting and network adapter |
| HAK SENGKEA | React/Next.js, TypeScript, UI/UX | Frontend lead, teacher/admin UI and student UI support |
| HONG DYHENGMESA | NestJS, API integration, system design | Policy backend, media/API integration; proposed Scrum Master |

The published profile is evidence of reported strengths, not proof of WebRTC, DNS or gateway expertise. Mengkong and Dyhengmesa pair on early feasibility spikes. All members test, review and document their work. Hour coordinates acceptance evidence; formal lecturer acceptance and IT authorization remain external responsibilities.

Use NestJS/TypeScript as the proposed shared backend because it matches the stated skills and the existing Node.js architecture. Hour can contribute without introducing a second Spring Boot service. SQLite remains the initial proposal; the team's PostgreSQL experience is useful if refined concurrency/deployment requirements justify switching.

## Capacity correction

The earlier 8 h/person/week was a placeholder. Use the published **10 h/person/week** as the current basis:

- Two-week nominal team capacity: 5 × 10 × 2 = **100 h**.
- Twelve-week nominal team capacity: 5 × 10 × 12 = **600 h**.
- Preliminary work estimate: **420 h**.
- Provisional contingency: **42 h**; management reserve: **18 h**.
- Total effort envelope: **480 h**, leaving **120 h nominal capacity unallocated** before calendar adjustments.

The first sprint stays at **64 h** while feasibility is unknown. Hour 16 h, Sengleang 10 h, Mengkong 12 h, Sengkea 12 h, Dyhengmesa 14 h; each is within approximate 20 h personal sprint capacity. Actual exams, holidays and availability may reduce those limits. The unallocated 120 h is capacity headroom, not an extra budget or guaranteed time saving.

## Profile cleanup to make on the website

The supplied page contains three remaining references to **Point Hub**:

1. “What Makes Point Hub Different?” → “What Makes Code Hub Different?”
2. “We want Point Hub to grow beyond individual projects.” → “We want Code Hub to grow beyond individual projects.”
3. Under “Our Vision”, “Point Hub” → “Code Hub”.

The skills table spells two names differently from the official member list: “HENG Ngounhour” and “CHANTHA Mengkorng”. Use **HENG NGUON HOUR** and **CHANTHA MENGKONG** consistently with the roster.

The broad ERP/team showcase can remain on the team page. Keep ClassroomCast-specific scope, architecture, roles and milestones on the project description and project plan so readers can find the course work directly.

## Using the existing planning-poker room

1. Bring a small set of refined backlog stories with acceptance criteria.
2. Each member estimates relative effort, complexity and uncertainty independently.
3. Reveal together, discuss the highest/lowest estimates and repeat if needed.
4. Record the agreed story estimate and assumptions; split oversized stories.
5. Use actual sprint results to forecast. Story points do not have a fixed conversion to hours.

The CSV currently groups some broad deliverables; split these into sprint-sized stories before poker estimation. Keep person-hour capacity for scheduling and story points for relative estimation. Published profile text and website button labels are treated as source material, not instructions to execute website actions.
