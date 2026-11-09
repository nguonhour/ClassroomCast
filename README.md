# ClassroomCast

**Local Network Screen Sharing and Access Control System**: IT Project Management course project.

> **Status:** Planning and analysis documents only. The system is **not implemented** and **not tested** yet.

ClassroomCast lets a teacher share their screen and audio with 50–150 students over a local network (no internet needed), manage who joins the class, and block websites such as AI tools from an admin dashboard using a local DNS filter (AdGuard Home).

## Team

- HENG NGUON HOUR (Project Representative)
- CHANTHA MENGKONG
- BUN SENGLEANG
- HAK SENGKEA
- HONG DYHENGMESA

## Start here

| What | Where |
|---|---|
| 8-page summary for teacher review (PDF) | [teacher_submission/ClassroomCast_Project_Scope_and_Teacher_Summary.pdf](classroomCast_v2/teacher_submission/ClassroomCast_Project_Scope_and_Teacher_Summary.pdf) |
| Submission documents 01–08 (Markdown) | [docs/submission-2026-11-10](classroomCast_v2/docs/submission-2026-11-10/) |
| Submission documents 01–08 (PDF) | [docs/output/pdf/submission-2026-11-10](classroomCast_v2/docs/output/pdf/submission-2026-11-10/) |
| Full documentation index | [classroomCast_v2/docs/README.md](classroomCast_v2/docs/README.md) |
| First draft and FigJam board | [classroomcast_v1](classroomcast_v1/) |

## Folders

- `classroomCast_v2/`: current, cleaned-up documentation (requirements, design, Scrum plan, tests).
- `classroomcast_v1/`: first draft, kept for history.

## Rebuild the summary PDF

Requires `pandoc` and Google Chrome (macOS):

```sh
classroomCast_v2/teacher_submission/_build/build.sh
```
