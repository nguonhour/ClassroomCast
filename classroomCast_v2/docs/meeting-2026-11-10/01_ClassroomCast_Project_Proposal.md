# 01 / Project Proposal

Prepared 9 November 2026 for the meeting on 10 November 2026. Draft - pending teacher/client confirmation.

## What we propose

ClassroomCast is a locally hosted classroom screen-sharing and access-control system. A teacher shares a selected screen and supported audio to admitted students in web browsers. Authorized administrators manage network restriction profiles through the application and an approved local enforcement service.

## Problem to validate with the teacher

Students may struggle to read demonstrations on a distant projector. Internet-dependent sharing can interrupt lessons when WAN service is unavailable. Teachers need simple class admission and participation controls; network staff need a consistent way to apply, verify and restore temporary restrictions. These are proposed problem statements, not measured research findings.

## Objectives and evidence

| Objective | Evidence expected later |
| --- | --- |
| Readable live demonstrations | Screen and supported-audio demonstration on agreed devices and browsers. |
| Controlled classroom access | Valid admission succeeds; rejected, removed and unauthorized viewers cannot receive media. |
| Local operation | New browser session joins and views with WAN disconnected after local provisioning. |
| Safe network controls | Approved policy blocks a test domain, permits an exception, preserves ClassroomCast and restores only its own changes. |
| Realistic capacity | Staged load tests with physical and simulated clients reported separately. Teacher-specified target: 50-150 students; CN06 validates capacity for 150. |

## Current stage

Requirements and design drafts exist; the earlier course-board screenshot reported 0 of 24 tasks completed; verify current completion from task evidence. Documents and diagrams are planning evidence, not evidence of working software or approved requirements.

## Scope for discussion

| Category | Proposed treatment |
| --- | --- |
| Required classroom behavior | Create class, local URL/QR and join code, admission and roster controls, screen/supported audio, pause/resume/stop, connection feedback and recovery. |
| Required network behavior | Approved profiles, scoped authorization, application/verification, expiry, emergency recovery and safe restoration. Feasibility depends on network-owner permission. |
| Deployment obligations | Campus and portable modes remain in the source specification. School-server hosting does not automatically remove portable scope. |
| Lower priorities | Materials/downloads, identity entry and scheduling/configuration transfer are Should items; history, optional interaction and group targeting are Could items. |
| Proposed exclusions | Custom SFU development and universal control of unmanaged devices are not proposed release commitments. Confirm exclusions with the teacher. |

## Resources and feasibility

Five CodeHub members will deliver the project. Confirm actual weekly hours, server specifications, access points, test laptops, certificate trust and authorized DNS/gateway integration. Budget and equipment availability are not yet established. Test local HTTPS, one publisher/two viewers, offline operation and apply/restore on an authorized test network before committing to scale.

## Schedule and approval requested

The latest supplied site plan uses preparation November 10-17, design November 18-27 and three development sprints November 30-January 13. Earlier files use six sprints starting November 2; those are historical planning drafts. The editing cutoff previously shown was January 25, 2027 at 23:59, while the site plans release January 27 and presentation February 3. Confirm which deliverables each date governs.

Requested decisions: problem and scope, acceptance test conditions, deployment equipment, infrastructure authority, three-sprint schedule and review milestones. All decisions remain pending until recorded.

Source: v2 proposal, scope, feasibility and risk documents; original supplied specification; latest user-provided course-board screenshots. Submitted PDF originals were unavailable at the named Downloads paths.
