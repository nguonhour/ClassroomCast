# Source review and unresolved conflicts

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Evidence precedence and review boundaries

This package organizes the supplied specification and existing planning documents; it does not approve them. Teacher requirements specify 50–150 students and both campus and portable deployment. School-server context does not remove portable scope. The previously introduced lower-capacity target was unsupported and is withdrawn.

All existing v1 files were inventoried and hashed. Text-based artifacts were read for inventory and extraction. Substantive review focused on the requirements, workflows, architecture, project/Scrum plans, source specifications and board catalogue; feature CSV and requirements tables were cross-checked. Generator/SVG text was treated as derived artifact evidence, not executed or visually revalidated. Binary PNG/PDF/ZIP artifacts were inventoried as derived presentation copies, not independently validated requirements sources. Course alignment is reused from COURSE-APPLICATION.md; this revision does not claim a new page-by-page review of all twelve course PDFs. Supplied screenshots informed lifecycle corrections, but are not proof that their generated arrows faithfully match Mermaid.

## 2. Conflicts and disposition

| ID | Evidence conflict or gap | Treatment in this package | Decision |
|---|---|---|---|
| C01 | Unsupported lower-capacity wording removed | Teacher source specifies one teacher and 50–150 students; CN06 requires validation for 150. D12 concerns test conditions and evidence, not an alternative target. | Documentation corrected; D12 test details pending |
| C02 | School server/Ubuntu context vs source campus and portable modes | School host is intended context, not evidence of access, capacity or elimination of portable mode | D18; Needs Teacher Approval |
| C03 | Older architecture combines class LIVE/PAUSED states | Model class, publication and policy states separately; stop/pause media leaves class open | Proposed clarification of T02/F07/F13 |
| C04 | Older plan suggests continuation on enforcement failure | D05 remains unresolved; F10 reports outcome, F01 applies approved continuation rule | D05; Pending Decision |
| C05 | Older architecture proposes audio pause and retention durations | Pause semantics D08 and retention D13 remain pending; no fixed durations adopted | Needs Teacher Approval |
| C06 | Green CN/OR cards look approved Must | 22 source deployment obligations have no individual priority; Must* is only a proposal | Scope approval |
| C07 | Earlier exported use-case tables reused UC numbers for other goals | Keep main requirements UC01–UC15 meanings; no second numbering scheme | Traceability rule |
| C08 | Old paths reference classroomcast/ | Link actual classroomcast_v1/ paths from new package; do not rewrite old documents | Documentation maintenance |
| C09 | Sprint 1 began Nov 2; current date Nov 9 | No actual progress evidence supplied. Reforecast remaining Sprint 1; do not backdate completion | D20 |
| C10 | Generated workflow pictures contain mismatched labels/branches | Current overview diagrams are review proposals; preserve source IDs, check semantic paths before image export | Team review |

## 3. Status vocabulary

- **Confirmed:** explicitly present in supplied evidence, not automatically teacher-approved or implemented.
- **Proposed:** design, allocation, estimate or acceptance candidate requiring review.
- **Pending Decision:** an unresolved choice with an owner and due gate.
- **Needs Teacher Approval:** release scope, capacity, acceptance, schedule or material exclusions require recorded approval.
- Implementation: **Not assessed**. Test execution: **Not run**. Acceptance: **Pending**.

MoSCoW priority is independent of these statuses. Green means Must capability, never test passed. Yellow = Should; gray = Could; red = proposed Won't; white = context/unresolved choice. Decision diamonds can be white without changing the priority of the associated feature.

## 4. Canonical sources

The functional register and test catalogue below are structured transcriptions of v1 requirement IDs and criteria. Source snapshot is [supplied-specification.md](supplied-specification.md). Existing [main requirements](../../../classroomcast_v1/REQUIREMENTS-AND-ACTIVITIES.md), [feature cards](../../../classroomcast_v1/board/ROW-2-FEATURE-CARDS.csv), [backlog](../../../classroomcast_v1/BACKLOG.csv), and [course mapping](../../../classroomcast_v1/COURSE-APPLICATION.md) remain intact. Earlier stack selection is a proposal to validate, not a confirmed technology commitment.
