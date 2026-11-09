# ClassroomCast — Local Network Screen Sharing and Access Control System

ClassroomCast is a browser-based classroom platform for sharing a teacher's screen and supported audio over a local network. It combines classroom participation controls with administrator-managed website restriction policies. Required application and media services run locally, allowing classroom operation without internet access after installation and provisioning.

**Team:** CodeHub · IT Project Management, I5, 2026–2027 Semester 1  
**Submission deadline:** 25 January 2027, 11:59 PM, as shown on the course project page  
**Current stage:** Planning and feasibility validation. Implementation and capacity results will be reported as they are verified.

## Objectives and target environment

- Support one teacher and a target of 50–150 students using supported laptop browsers.
- Let students join through a local URL or QR code and a classroom join code, without installing a student application.
- Share a selected screen, window or tab, supported system/tab audio, and optional microphone audio.
- Run on either the approved campus network or a portable teacher-owned network through the same application.
- Let authorized administrators configure domain/category restrictions, exceptions and reusable profiles through the dashboard.
- Show actual enforcement verification, failures and restoration status accurately.

The target capacity will be validated through staged load tests and a physical classroom pilot. Reported results will distinguish simulated subscribers from real devices and Wi-Fi capacity.

## Main features

### Teacher dashboard

Create classroom sessions, display URL/code/QR joining information, start/stop/pause/resume sharing, select supported media sources, manage streaming settings, and monitor participants. Teachers can approve, reject, remove and block participants. Publishing and class control require authorized teacher access.

### Student interface

Join a classroom, watch live screen content, play supported audio with volume controls, enter fullscreen, see useful connection status/errors, and reconnect after temporary interruptions. Optional student names, material downloads and interactive activities will be prioritized after required features.

### Administrator dashboard

Manage allow-by-default and restricted-by-default profiles, categories, domain rules and approved exceptions. Apply policies when a class starts and restore the previous policy when it ends. Provide temporary-rule expiry, action auditing, emergency restoration and server-side credential protection.

A saved policy and verified network enforcement are shown separately. The application protects its local classroom services from its own restrictions and minimizes student browsing-data collection.

## User flow

1. Teacher signs in, creates a classroom and displays its local URL, QR code and join code.
2. Students connect to the classroom network, open the application and request admission.
3. Teacher admits participants, selects a capture source and starts sharing to the local media server.
4. Students receive the broadcast and use playback, fullscreen and connection controls.
5. An authorized administrator applies the selected profile to the supported network scope; the dashboard displays verification results.
6. When the session ends, participants are disconnected and temporary policy changes are restored and verified.

## Architecture

| Layer | Proposed implementation |
|---|---|
| Teacher, student and administrator interfaces | React + Vite + TypeScript |
| Classroom API and policy manager | NestJS + TypeScript |
| Real-time media and signaling | WebRTC through a self-hosted LiveKit SFU |
| Local data | SQLite initially |
| Network enforcement | Local AdGuard Home integration or an approved compatible service |
| HTTPS and deployment | Caddy and Docker Compose on a local server |

The teacher publishes to a local Selective Forwarding Unit, which distributes media to students. The backend manages sessions, admission, permissions, policy profiles and recovery. Enforcement credentials and API secrets remain on the server.

Local HTTPS uses a certificate trusted by client browsers. Capture requires the teacher's permission, and audio support depends on browser, operating system and selected capture source. Supported combinations will be documented after testing.

## Network modes and enforcement limits

**Campus network:** use approved hosting, connectivity, certificates, media ports and DNS/gateway integration in coordination with campus IT. Display enforcement as unavailable until the required integration is authorized and configured.

**Portable network:** deploy local services behind a suitable router and access points. Provision network settings during installation, then manage classroom policies through the dashboard. Validate device capacity and offline operation on the actual equipment.

A browser application cannot directly block other websites across student laptops. Domain filtering requires traffic to use the supported enforcement service. VPNs, alternate or encrypted DNS, direct IP access, and locally operating agents may bypass domain-only controls. Stronger restrictions require supported, authorized gateway or managed-device controls. The project will document these limits and will not claim universal blocking.

## Team responsibilities

| Member | Proposed responsibility |
|---|---|
| HENG NGUON HOUR ★ — ហេង ងួនហ៊ួរ | Representative, Product Owner, integration and student frontend |
| BUN SENGLEANG — ប៊ុន សេងលៀង | Classroom backend, REST APIs and database |
| CHANTHA MENGKONG — ចន្ថា ម៉េងគង់ | DevOps, SFU hosting and enforcement adapter |
| HAK SENGKEA — ហាក់ សេងគា | Frontend and UI/UX lead; teacher/admin dashboards |
| HONG DYHENGMESA — ហុង ឌីហេងមេសា | Policy backend, media/API integration and Scrum Master |

All members contribute implementation, tests, reviews and documentation. Assignments reflect the supplied team skills profile. Published capacity is approximately 10 hours per member per week (50 team hours/week), subject to individual calendars. WebRTC and enforcement integration require early learning spikes.

## Delivery approach and milestones

Use a hybrid approach: agreed scope, milestone and effort baselines with six two-week Scrum sprints. Each sprint includes planning, a Daily Scrum, a working-result review and a retrospective. Backlog priorities follow the supplied Must/Should/Could requirements.

| Dates | Planned outcome |
|---|---|
| 2–15 November 2026 | Local teacher-to-student screen-sharing demonstration and feasibility checks |
| 16–29 November | Classroom controls, admission, audio and reconnection |
| 30 November–13 December | Profile management and verified policy application/restoration demonstration |
| 14–27 December | Remaining Must behavior and deployment/recovery validation |
| 28 December–10 January 2027 | Capacity/offline testing and release candidate |
| 11–24 January | Physical pilot, corrections, acceptance, guides and demo package |
| 25 January | Final submission contingency before the editing deadline |

This schedule is provisional until weekly availability, hardware access and campus integration are confirmed. The team will record risks, effort, working evidence and scope decisions in weekly progress updates and maintain the task plan on the course website.

## Acceptance and deliverables

Acceptance covers the supplied Must requirements, supported-browser classroom flows, role checks, policy verification and restoration, offline operation, measured performance and documented network limits. Proposed media/recovery targets will be agreed with the lecturer before being treated as acceptance commitments.

Deliver source code, deployment configuration, architecture and flow diagrams, requirements/backlog records, test and pilot evidence, installation/recovery guides, a demonstration and final report. Source and demo links will be added once available.
