# 02 / Requirements Summary

Prepared 9 November 2026 for the meeting on 10 November 2026. Draft - pending teacher/client confirmation.

## Users and permissions

| Role | Responsibility and boundary |
| --- | --- |
| Teacher (TCH) | Create and manage own classes, publish screen/audio, manage participants and select assigned approved profiles. No automatic network-administration permission. |
| Student (STU) | Request admission, watch authorized media, adjust personal playback and reconnect. Cannot publish teacher media or change policies. |
| System Administrator (SYS) | Manage application accounts/settings and assigned policy profiles within explicit permissions. No automatic classroom viewing or network-wide authority. |
| IT / Network Administrator (NET) | Configure approved integrations, manage assigned network scopes, verify enforcement and recover failures. Infrastructure-owner authorization remains necessary. |

## Six product areas

| Area | Included capability groups |
| --- | --- |
| Broadcasting | Screen capture, supported audio, quality controls and playback. |
| Classroom participation | Class creation, join information, admission, roster and participant access. |
| Network access control | Profiles, rules, exceptions, apply/verify and restoration. |
| Deployment / infrastructure | Campus and portable preparation, local services and connectivity. |
| Diagnostics / recovery | Status, reconnect, emergency/expiry and unresolved-operation recovery. |
| Administration / security | Scoped authorization, secrets, minimal logs and administrative settings. |

Inventory: 63 original numbered requirements and 68 feature cards, organized into 15 use cases and 18 process flows. These counts are different views of the system, not 68 completed features.

## Priority and status

The original numbered register contains 31 Must, 7 Should, 3 Could and 22 deployment obligations with no individual priority label. The latter are not automatically optional; proposed Must classification needs agreement. Green = Must; yellow = Should; gray = Could; red = proposed exclusion; white = context or unresolved decision. Color never means implemented or tested.

## Rules that the implementation must preserve

| Rule | Expected behavior |
| --- | --- |
| Admission is separate from viewing | A join code or pending request does not grant media access. Final admission checks current class, eligibility, blocking and capacity. |
| Class and media are separate | Pause/stop broadcast leaves the class open. A new source after capture ends requires fresh browser consent. |
| Policy state is explicit | Saved profile, accepted apply request and verified client-path enforcement are distinct. |
| End class safely | Close admission, revoke grants and verify media closure. Record restoration independently; unknown restoration is never reported as success. |
| Recover safely | Resume unfinished operations without repeating completed changes. Restore only ClassroomCast-owned changes; preserve unrelated administration changes. |

## Acceptance candidates - not test results

Agree a browser/OS/audio matrix and physical-device capacity. Existing drafts propose 720p/15 fps, p95 screen latency at most 1 second, 30-minute staged load tests, and healthy-network apply/restore within 30 seconds. These are proposed targets, not approved promises or measured results. Security tests must reject unauthorized viewing/control and prevent removed users from reconnecting.

## Decisions needed first

Agree test conditions for the teacher-specified 50–150 students; equipment for campus and portable deployment; code-only versus teacher approval; student identity and block persistence; pause/audio behavior; network authority; and continuation without verified restrictions (D05).

Detailed references: docs/01-requirements/04-functional-requirements.md, 06-user-roles-and-permissions.md, 07-business-rules.md; docs/traceability.md; docs/05-testing-and-evaluation/.
