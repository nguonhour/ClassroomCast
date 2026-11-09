# Functional requirements and deployment obligations

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Source classification

The 63 rows retain original IDs and source priorities: 31 Must, 7 Should, 3 Could, 22 individually unlabeled deployment obligations. CN/OR are not optional merely because priorities were unlabeled. Their proposed Must* classification needs confirmation. Capability availability is not established by documentation.

## 2. Requirement register

| ID | Requirement | Source priority | Flows | Use cases |
|---|---|---|---|---|
| NAC01 | Enable or disable network restrictions for a class | Must | F01 F10 | UC06 |
| NAC02 | Block website categories, including AI and coding agents | Must | F09 F10 F11 | UC05 UC06 |
| NAC03 | Block or allow individual domains | Must | F09 F10 F11 | UC05 UC06 |
| NAC04 | Support allow-by-default and restricted-by-default policies | Must | F09 F10 F11 | UC05 UC06 |
| NAC05 | Automatically apply policies when a class starts | Must | F01 F10 | UC06 |
| NAC06 | Restore the previous policy when a class ends | Must | F13 F14 | UC08 UC09 |
| NAC07 | Save reusable policy profiles | Must | F09 F10 F11 | UC05 UC06 |
| NAC08 | Add allowlist exceptions for approved websites | Must | F09 F10 F11 | UC05 UC06 |
| NAC09 | Schedule restrictions by date and time | Should | F17 | UC12 |
| NAC10 | Display active policy and actual enforcement status | Must | F10 F13 F14 F15 | UC06 UC08 UC09 UC10 |
| NAC11 | Record administrator actions and timestamps | Must | F10 F13 F14 F15 | UC06 UC08 UC09 UC10 |
| NAC12 | Provide an emergency disable and rollback function | Must | F14 F15 | UC09 UC10 |
| NAC13 | Support temporary rules with automatic expiry | Must | F14 F15 | UC09 UC10 |
| NAC14 | Import and export policy configurations | Should | F17 | UC12 |
| NAC15 | Apply different policies to student groups or devices where supported | Could | F18 | UC13 |
| NAC16 | Restrict policy management to authorized administrators | Must | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 |
| NAC17 | Keep router credentials and API secrets on the server | Must | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 |
| NAC18 | Prevent restrictions from breaking ClassroomCast itself | Must | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 |
| NAC19 | Minimize student browsing-history collection | Must | F09 F10 F13 F14 F15 | UC05 UC06 UC08 UC09 UC10 |
| NAC20 | Support locally stored rules for offline operation | Should | F03 F17 | UC12 UC15 |
| T01 | Create a classroom with a unique session ID and join code | Must | F04 F05 | UC01 UC02 |
| T02 | Start, stop, pause, and resume broadcasting | Must | F06 F07 | UC03 |
| T03 | Share an entire screen, window, or browser tab where supported | Must | F06 F07 | UC03 |
| T04 | Share supported system audio and optional microphone audio | Must | F06 F07 | UC03 |
| T05 | View connected students and their connection status | Must | F05 F08 | UC02 UC04 |
| T06 | Approve, reject, remove, and block participants | Must | F05 F08 | UC02 UC04 |
| T07 | Configure resolution, frame rate, and bitrate | Must | F06 F07 | UC03 |
| T08 | Display the classroom URL, join code, and QR code | Must | F04 F05 | UC01 UC02 |
| T09 | Display streaming health and connection diagnostics | Should | F15 | UC10 |
| T10 | Share presentation files, PDFs, images, and videos | Should | F16 | UC11 |
| T11 | Display session history and participant counts | Could | F18 | UC13 |
| S01 | Join through a local URL or QR code | Must | F05 | UC02 |
| S02 | Enter a classroom join code | Must | F05 | UC02 |
| S03 | Watch the teacher's screen in real time | Must | F06 F07 | UC03 |
| S04 | Play supported shared audio with volume control | Must | F06 F07 | UC03 |
| S05 | View the broadcast in fullscreen | Must | F06 F07 | UC03 |
| S06 | Reconnect after temporary network interruptions | Must | F12 | UC07 |
| S07 | Show connection status and useful errors | Must | F05 F07 F12 F15 | UC02 UC03 UC07 UC10 |
| S08 | Enter a student name or assigned student ID | Should | F05 | UC02 |
| S09 | Download teacher-provided materials when permitted | Should | F16 | UC11 |
| S10 | Raise a hand, submit questions, or answer polls | Could | F18 | UC13 |
| CN01 | Use an approved local server address or hostname | Unlabeled / proposed Must* | F02 | UC14 |
| CN02 | Verify student devices can reach the application and signaling services | Unlabeled / proposed Must* | F02 | UC14 |
| CN03 | Confirm required WebRTC media traffic is permitted | Unlabeled / proposed Must* | F02 | UC14 |
| CN04 | Verify Wi-Fi client isolation and guest-network restrictions | Unlabeled / proposed Must* | F02 | UC14 |
| CN05 | Obtain campus IT approval for hosting and firewall changes | Unlabeled / proposed Must* | F02 | UC14 |
| CN06 | Validate Wi-Fi capacity and network throughput for 150 students | Unlabeled / proposed Must* | F02 | UC14 |
| CN07 | Provide QR-code and manual URL discovery | Unlabeled / proposed Must* | F02 | UC14 |
| CN08 | Avoid IP address conflicts with existing campus services | Unlabeled / proposed Must* | F02 | UC14 |
| CN09 | Host required application components locally for offline operation | Unlabeled / proposed Must* | F02 | UC14 |
| CN10 | Integrate network restrictions with campus-approved DNS or gateway controls | Unlabeled / proposed Must* | F02 | UC14 |
| OR01 | Business-class Wi-Fi 6 or better equipment suitable for high client density | Unlabeled / proposed Must* | F03 | UC15 |
| OR02 | Configurable classroom SSID and Wi-Fi password | Unlabeled / proposed Must* | F03 | UC15 |
| OR03 | WPA2-AES or WPA3 security where compatible | Unlabeled / proposed Must* | F03 | UC15 |
| OR04 | DHCP capacity for all students and support devices | Unlabeled / proposed Must* | F03 | UC15 |
| OR05 | Stable server IP address or local hostname | Unlabeled / proposed Must* | F03 | UC15 |
| OR06 | Wired Gigabit Ethernet or faster connection to the server where possible | Unlabeled / proposed Must* | F03 | UC15 |
| OR07 | Appropriate client isolation settings that permit access to the server and approved enforcement services | Unlabeled / proposed Must* | F03 | UC15 |
| OR08 | One or more access points based on classroom capacity testing | Unlabeled / proposed Must* | F03 | UC15 |
| OR09 | Support for additional access points and a wired switch | Unlabeled / proposed Must* | F03 | UC15 |
| OR10 | Portable power, cables, and carrying equipment | Unlabeled / proposed Must* | F03 | UC15 |
| OR11 | Fully functional local services without WAN or internet access | Unlabeled / proposed Must* | F03 | UC15 |
| OR12 | Local software-based policy management without requiring manual rule changes for each class | Unlabeled / proposed Must* | F03 | UC15 |

## 3. Supporting features and count reconciliation

| Card | Capability | Basis | Priority/status |
|---|---|---|---|
| BF-05-07 | Basic health and operations | Shared architectural and classroom-administration obligations; no extra original ID | REQUIRED / source obligation |
| BF-06-05 | Classroom authorization | Unnumbered classroom-administration obligation; supports T01/T06 and S03 | REQUIRED / source obligation |
| BF-06-06 | Application account management | Proposed account model, not a separate original numbered feature | PROPOSED / no source priority |
| BF-06-07 | Role assignment | Proposed RBAC allocation | PROPOSED / no source priority |
| BF-06-08 | Application settings and scoped review | Proposed administration UI/permission details | PROPOSED / no source priority |

All 68 original board cards are available in [board/ROW-2-FEATURE-CARDS.md](../../../classroomcast_v1/board/ROW-2-FEATURE-CARDS.md). They are grouped feature descriptions; user stories and tasks may split or combine them. The [traceability matrix](../traceability.md) maps every numbered requirement to a story and test. No feature has been marked implemented.
