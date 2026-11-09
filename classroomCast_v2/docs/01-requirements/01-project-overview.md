# ClassroomCast project overview

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Purpose

ClassroomCast lets a teacher share a selected screen and supported audio with admitted students over a local network. Teachers manage their own classrooms; authorized administrators manage website restriction profiles through supported local network integrations. The application exposes whether restrictions are actually verified and whether temporary network changes have been restored.

## 2. Context and boundaries

| Item | Evidence and status |
|---|---|
| Team | CodeHub; five named members; Hour is representative in supplied roster |
| Application | Browser-based; students do not require a native application |
| Hosting | Existing school server running Ubuntu/Linux: latest user-stated context; inventory/access unverified |
| Capacity | Teacher-specified 50–150 students per classroom; CN06 validates capacity for 150. D12: test conditions and evidence pending. |
| Connectivity | Local runtime without WAN after provisioning; local network and server must remain available |
| Deployment | Campus and portable modes in source; portable inclusion under D18 |
| Submission | 25 January 2027, 23:59 on supplied course page; verify site timezone |
| Current stage | Requirements, workflow and feasibility planning; implementation completion not assessed |

## 3. Product structure

| Area | Feature entries |
|---|---|
| Classroom broadcasting | 7 |
| Classroom management and participation | 11 |
| Network access control | 13 |
| Deployment and infrastructure | 22 |
| Diagnostics, verification and recovery | 7 |
| Application administration and security | 8 |

There are 68 feature entries, 63 original numbered requirements, 15 use cases and 18 process flows. These are different units; no atomic-function count has been approved. Five feature entries supplement the numbered source: two architectural obligations and three proposed administration capabilities.

## 4. Reading route

Read the [SRS](03-software-requirements-specification.md), [roles](06-user-roles-and-permissions.md), then [workflows](../03-system-analysis-and-design/02-system-workflows.md). Review the [decision log](../07-teacher-review/03-feedback-and-decision-log.md) before treating any draft as an implementation baseline.
