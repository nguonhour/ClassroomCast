# 04 — Complete Product Feature Catalogue

Prepared 9 November 2026 for teacher review on 10 November. **Draft; not approved or implemented.**

## Four product pillars mapped to six capability areas

| Product pillar | Capability areas |
|---|---|
| Classroom broadcasting | 01 Broadcasting |
| Classroom management | 02 Management and participation |
| Software-managed network access control | 03 Network access control |
| Network administration and diagnostics | 04 Deployment and infrastructure; 05 Diagnostics, verification and recovery |

Area 06 (application administration and security) supports all four pillars. These are two organizational views of the same scope, not four additional feature commitments.

68 entries = 63 original numbered obligations + 2 unnumbered required obligations + 3 proposed administration capabilities. The 22 CN/OR obligations have no individual source priority label; green Must* is a proposal, not a teacher-assigned label.


---

Source: [ROW-2-FEATURE-CARDS.md](../../../classroomcast_v1/board/ROW-2-FEATURE-CARDS.md)

# Row 2 — Six-area feature catalogue

Prepared 6 November 2026 from REQUIREMENTS-AND-ACTIVITIES.md revision 0.5. Draft for client review.

**Board placement:** beside Roles & Permissions, before Use Cases. Import the full SVG or the six individual area SVGs. Markdown is the editable content source for copying native text/sticky cards; SVG import is a visual artifact and may not create individually editable FigJam cards.

Green = Must; yellow = Should; gray = Could; red = proposed Won't; white = unclassified/proposed. CN/OR green Must* is proposed, not source-labeled. No red feature card is included because this catalogue contains capabilities, not excluded proposals.

**Counts:** 68 entries = 63 original IDs + 2 unnumbered required obligations + 3 proposed administration entries. This is not 68 approved client requirements or an atomic-function count.

## Area 01 — Classroom broadcasting — 7 entries

### BF-01-01 — Broadcast controls

- **Priority:** MUST
- **Requirement / basis:** T02
- **Actor / service:** Teacher, Backend, SFU
- **Functions:** Start, stop, pause and resume publication; show the agreed sharing state
- **Workflows / references:** F06, F07
- **Test references:** TC-T02
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-01-02 — Screen capture

- **Priority:** MUST
- **Requirement / basis:** T03
- **Actor / service:** Teacher, browser
- **Functions:** Select an entire screen, window or browser tab where supported; request browser consent
- **Workflows / references:** F06
- **Test references:** TC-T03
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-01-03 — Audio publication

- **Priority:** MUST
- **Requirement / basis:** T04
- **Actor / service:** Teacher, browser, SFU
- **Functions:** Share supported system/tab audio and optional microphone audio; disclose unsupported combinations
- **Workflows / references:** F06, F07
- **Test references:** TC-T04
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-01-04 — Media quality

- **Priority:** MUST
- **Requirement / basis:** T07
- **Actor / service:** Teacher, media service
- **Functions:** Configure supported resolution, frame rate and bitrate; report limitations/adaptation
- **Workflows / references:** F06, F07
- **Test references:** TC-T07
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-01-05 — Live screen viewing

- **Priority:** MUST
- **Requirement / basis:** S03
- **Actor / service:** Student, SFU
- **Functions:** Receive and display the teacher's live screen after admission
- **Workflows / references:** F06, F07
- **Test references:** TC-S03
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-01-06 — Personal audio playback

- **Priority:** MUST
- **Requirement / basis:** S04
- **Actor / service:** Student
- **Functions:** Play supported shared audio; adjust or mute this student's volume
- **Workflows / references:** F06, F07
- **Test references:** TC-S04
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-01-07 — Fullscreen playback

- **Priority:** MUST
- **Requirement / basis:** S05
- **Actor / service:** Student
- **Functions:** Enter and exit fullscreen on the student's supported browser
- **Workflows / references:** F07
- **Test references:** TC-S05
- **Approval:** Pending confirmation
- **Test result:** Not run

## Area 02 — Classroom management and participation — 11 entries

### BF-02-01 — Classroom creation

- **Priority:** MUST
- **Requirement / basis:** T01
- **Actor / service:** Teacher, Backend
- **Functions:** Create a unique session ID and active classroom join code
- **Workflows / references:** F04
- **Test references:** TC-T01
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-02 — Joining information

- **Priority:** MUST
- **Requirement / basis:** T08
- **Actor / service:** Teacher, application
- **Functions:** Display the local URL, join code and QR code
- **Workflows / references:** F04, F05
- **Test references:** TC-T08
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-03 — Participant monitoring

- **Priority:** MUST
- **Requirement / basis:** T05
- **Actor / service:** Teacher, Backend
- **Functions:** Show connected participants and their connection status
- **Workflows / references:** F05, F08
- **Test references:** TC-T05
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-04 — Admission and participant control

- **Priority:** MUST
- **Requirement / basis:** T06
- **Actor / service:** Teacher, Backend, SFU
- **Functions:** Approve/reject admission; remove/block participants; enforce owning-teacher authority
- **Workflows / references:** F05, F08
- **Test references:** TC-T06
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-05 — Local classroom access

- **Priority:** MUST
- **Requirement / basis:** S01
- **Actor / service:** Student
- **Functions:** Open the application through a local URL or QR destination
- **Workflows / references:** F05
- **Test references:** TC-S01
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-06 — Join-code validation

- **Priority:** MUST
- **Requirement / basis:** S02
- **Actor / service:** Student, Backend
- **Functions:** Enter required code; validate current class/code, block state and capacity; apply the configured approval gate
- **Workflows / references:** F05
- **Test references:** TC-S02
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-07 — Student identifier

- **Priority:** SHOULD
- **Requirement / basis:** S08
- **Actor / service:** Student, Backend
- **Functions:** Enter a student name or assigned ID; apply agreed validation and retention
- **Workflows / references:** F05
- **Test references:** TC-S08
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-08 — Materials sharing

- **Priority:** SHOULD
- **Requirement / basis:** T10
- **Actor / service:** Teacher, application
- **Functions:** Share presentations, PDFs, images and videos through the agreed supported method
- **Workflows / references:** F16
- **Test references:** TC-T10
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-09 — Permitted downloads

- **Priority:** SHOULD
- **Requirement / basis:** S09
- **Actor / service:** Student, Backend
- **Functions:** Download teacher-provided materials only when admitted and permitted
- **Workflows / references:** F16
- **Test references:** TC-S09
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-10 — Session history

- **Priority:** COULD
- **Requirement / basis:** T11
- **Actor / service:** Teacher, Backend
- **Functions:** Display retained session history and participant counts within authorized ownership
- **Workflows / references:** F18
- **Test references:** TC-T11
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-02-11 — Classroom interaction

- **Priority:** COULD
- **Requirement / basis:** S10
- **Actor / service:** Student, Teacher, Backend
- **Functions:** Raise a hand, submit a question or answer a poll where the selected feature/activity is available
- **Workflows / references:** F18
- **Test references:** TC-S10
- **Approval:** Pending confirmation
- **Test result:** Not run

## Area 03 — Network access control — 13 entries

### BF-03-01 — Restriction switch

- **Priority:** MUST
- **Requirement / basis:** NAC01
- **Actor / service:** Scoped SYS/NET, Policy Manager
- **Functions:** Enable or disable class restrictions within the approved scope
- **Workflows / references:** F10
- **Test references:** TC-NAC01
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-02 — Category rules

- **Priority:** MUST
- **Requirement / basis:** NAC02
- **Actor / service:** Scoped SYS/NET
- **Functions:** Select blocked website categories, including selected AI and coding-agent domains
- **Workflows / references:** F09, F10, F11
- **Test references:** TC-NAC02
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-03 — Domain rules

- **Priority:** MUST
- **Requirement / basis:** NAC03
- **Actor / service:** Scoped SYS/NET, Policy Manager
- **Functions:** Add blocked/allowed domains and validate their syntax/matching behavior
- **Workflows / references:** F09, F10, F11
- **Test references:** TC-NAC03
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-04 — Default policy modes

- **Priority:** MUST
- **Requirement / basis:** NAC04
- **Actor / service:** Scoped SYS/NET, enforcement service
- **Functions:** Configure allow-by-default or restricted-by-default behavior within adapter capabilities
- **Workflows / references:** F09, F10, F11
- **Test references:** TC-NAC04
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-05 — Automatic class-start policy

- **Priority:** MUST
- **Requirement / basis:** NAC05
- **Actor / service:** Teacher event, Backend automation
- **Functions:** Trigger the class's approved profile when the agreed Start event occurs
- **Workflows / references:** F01, F10
- **Test references:** TC-NAC05
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-06 — Class-end restoration

- **Priority:** MUST
- **Requirement / basis:** NAC06
- **Actor / service:** Backend, enforcement service
- **Functions:** Restore the prior policy when the class ends; track unresolved restoration separately
- **Workflows / references:** F13, F14
- **Test references:** TC-NAC06
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-07 — Reusable profiles

- **Priority:** MUST
- **Requirement / basis:** NAC07
- **Actor / service:** Scoped SYS/NET, Backend
- **Functions:** Save and retrieve versioned restriction profiles for later classes
- **Workflows / references:** F09
- **Test references:** TC-NAC07
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-08 — Approved exceptions

- **Priority:** MUST
- **Requirement / basis:** NAC08
- **Actor / service:** Scoped SYS/NET, enforcement service
- **Functions:** Add allowlist exceptions to category/domain restrictions and evaluate agreed precedence
- **Workflows / references:** F09, F10, F11
- **Test references:** TC-NAC08
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-09 — Scheduled restrictions

- **Priority:** SHOULD
- **Requirement / basis:** NAC09
- **Actor / service:** Scoped SYS/NET, scheduler
- **Functions:** Schedule start/end with timezone, authorization and restart semantics
- **Workflows / references:** F17
- **Test references:** TC-NAC09
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-10 — Policy configuration transfer

- **Priority:** SHOULD
- **Requirement / basis:** NAC14
- **Actor / service:** Scoped SYS/NET, Backend
- **Functions:** Import/export validated policy configurations without secrets
- **Workflows / references:** F17
- **Test references:** TC-NAC14
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-11 — Group/device targeting

- **Priority:** COULD
- **Requirement / basis:** NAC15
- **Actor / service:** Scoped SYS/NET, adapter
- **Functions:** Apply different policies only where target identity and isolation are supported
- **Workflows / references:** F18
- **Test references:** TC-NAC15
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-12 — Classroom protection

- **Priority:** MUST
- **Requirement / basis:** NAC18
- **Actor / service:** Policy Manager, enforcement service
- **Functions:** Prevent configured restrictions from breaking local application, names and media paths
- **Workflows / references:** F09, F10, F13, F14
- **Test references:** TC-NAC18
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-03-13 — Local rule storage

- **Priority:** SHOULD
- **Requirement / basis:** NAC20
- **Actor / service:** Backend, enforcement service
- **Functions:** Keep required rule data locally usable without remote fetching during class
- **Workflows / references:** F03, F17
- **Test references:** TC-NAC20
- **Approval:** Pending confirmation
- **Test result:** Not run

## Area 04 — Deployment and infrastructure — 22 entries

### BF-04-01 — Campus endpoint

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN01
- **Actor / service:** NET, campus IT
- **Functions:** Use an approved local server address/hostname
- **Workflows / references:** F02
- **Test references:** TC-CN01
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-02 — Campus application reachability

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN02
- **Actor / service:** NET, installer
- **Functions:** Verify student access to application and signaling services
- **Workflows / references:** F02
- **Test references:** TC-CN02
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-03 — Campus media connectivity

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN03
- **Actor / service:** NET, campus IT, SFU
- **Functions:** Permit and test required WebRTC media traffic
- **Workflows / references:** F02
- **Test references:** TC-CN03
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-04 — Campus network isolation

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN04
- **Actor / service:** NET, campus IT
- **Functions:** Check Wi-Fi client isolation and guest-network restrictions against required paths
- **Workflows / references:** F02
- **Test references:** TC-CN04
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-05 — Campus authorization

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN05
- **Actor / service:** Campus IT, NET
- **Functions:** Obtain hosting and firewall-change approval before performing those changes
- **Workflows / references:** F02
- **Test references:** TC-CN05
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-06 — Campus capacity

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN06
- **Actor / service:** NET, test team
- **Functions:** Validate network throughput and Wi-Fi capacity for 150 students with declared test conditions
- **Workflows / references:** F02
- **Test references:** TC-CN06
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-07 — Campus discovery

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN07
- **Actor / service:** Installer, application
- **Functions:** Provide working QR and manual URL access instructions
- **Workflows / references:** F02
- **Test references:** TC-CN07
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-08 — Campus addressing safety

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN08
- **Actor / service:** NET, campus IT
- **Functions:** Avoid IP conflicts with existing campus services
- **Workflows / references:** F02
- **Test references:** TC-CN08
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-09 — Campus offline runtime

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN09
- **Actor / service:** NET, local services
- **Functions:** Host required application components locally and test with WAN disconnected
- **Workflows / references:** F02
- **Test references:** TC-CN09
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-10 — Campus enforcement integration

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** CN10
- **Actor / service:** NET, Policy Manager
- **Functions:** Use approved DNS/gateway controls; verify effects and restoration
- **Workflows / references:** F02, F10, F13
- **Test references:** TC-CN10
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-11 — Portable high-density Wi-Fi

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR01
- **Actor / service:** NET, installer
- **Functions:** Select Wi-Fi 6-or-better equipment and validate real client capacity
- **Workflows / references:** F03
- **Test references:** TC-OR01
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-12 — Portable network identity

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR02
- **Actor / service:** NET, installer
- **Functions:** Configure classroom SSID and password
- **Workflows / references:** F03
- **Test references:** TC-OR02
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-13 — Portable Wi-Fi security

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR03
- **Actor / service:** NET, installer
- **Functions:** Configure compatible WPA2-AES or WPA3
- **Workflows / references:** F03
- **Test references:** TC-OR03
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-14 — Portable address allocation

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR04
- **Actor / service:** NET, DHCP service
- **Functions:** Provide DHCP capacity for students and support devices
- **Workflows / references:** F03
- **Test references:** TC-OR04
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-15 — Portable server discovery

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR05
- **Actor / service:** NET, installer
- **Functions:** Provide a stable server address or local hostname
- **Workflows / references:** F03
- **Test references:** TC-OR05
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-16 — Wired server uplink

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR06
- **Actor / service:** NET, installer
- **Functions:** Use Gigabit Ethernet or faster where possible; record measured exceptions
- **Workflows / references:** F03
- **Test references:** TC-OR06
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-17 — Portable network isolation

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR07
- **Actor / service:** NET, installer
- **Functions:** Permit required server/enforcement access under intended isolation settings
- **Workflows / references:** F03
- **Test references:** TC-OR07
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-18 — Access-point capacity

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR08
- **Actor / service:** NET, test team
- **Functions:** Determine AP count and placement through classroom tests
- **Workflows / references:** F03
- **Test references:** TC-OR08
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-19 — Portable expansion

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR09
- **Actor / service:** NET, installer
- **Functions:** Support additional APs and a wired switch
- **Workflows / references:** F03
- **Test references:** TC-OR09
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-20 — Portable kit

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR10
- **Actor / service:** Installer, equipment owner
- **Functions:** Provide and check power, cables/adapters and carrying equipment
- **Workflows / references:** F03
- **Test references:** TC-OR10
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-21 — Portable offline runtime

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR11
- **Actor / service:** NET, local services
- **Functions:** Run required local services without WAN/internet
- **Workflows / references:** F03
- **Test references:** TC-OR11
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-04-22 — Portable policy automation

- **Priority:** MUST* / proposed classification
- **Requirement / basis:** OR12
- **Actor / service:** NET, Policy Manager
- **Functions:** Change class policies through supported software integration without per-class manual router-rule editing
- **Workflows / references:** F03, F10, F13
- **Test references:** TC-OR12
- **Approval:** Pending confirmation
- **Test result:** Not run

## Area 05 — Diagnostics, verification and recovery — 7 entries

### BF-05-01 — Student reconnection

- **Priority:** MUST
- **Requirement / basis:** S06
- **Actor / service:** Student, Backend, SFU
- **Functions:** Revalidate current admission and recover playback after a temporary interruption
- **Workflows / references:** F12
- **Test references:** TC-S06
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-05-02 — Connection feedback

- **Priority:** MUST
- **Requirement / basis:** S07
- **Actor / service:** Student, application
- **Functions:** Show useful joining, disconnected, waiting, ended and media-error states
- **Workflows / references:** F05, F07, F12, F15
- **Test references:** TC-S07
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-05-03 — Expanded stream diagnostics

- **Priority:** SHOULD
- **Requirement / basis:** T09
- **Actor / service:** Teacher, application
- **Functions:** Display available streaming health and connection diagnostics
- **Workflows / references:** F15
- **Test references:** TC-T09
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-05-04 — Actual enforcement status

- **Priority:** MUST
- **Requirement / basis:** NAC10
- **Actor / service:** Scoped administrator, Backend
- **Functions:** Show desired/active policy separately from verified enforcement, with scope/time and failures
- **Workflows / references:** F10, F13, F14, F15
- **Test references:** TC-NAC10
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-05-05 — Emergency disable/rollback

- **Priority:** MUST
- **Requirement / basis:** NAC12
- **Actor / service:** Scoped SYS/NET, recovery worker
- **Functions:** Safely restore ClassroomCast-managed temporary changes and report the result
- **Workflows / references:** F14, F15
- **Test references:** TC-NAC12
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-05-06 — Temporary expiry

- **Priority:** MUST
- **Requirement / basis:** NAC13
- **Actor / service:** Backend/recovery worker, enforcement service
- **Functions:** Expire temporary rules automatically with durable restart/recovery behavior
- **Workflows / references:** F14, F15
- **Test references:** TC-NAC13
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-05-07 — Basic health and operations

- **Priority:** REQUIRED / source obligation
- **Requirement / basis:** Shared architectural and classroom-administration obligations; no extra original ID
- **Actor / service:** Authorized operator, local services
- **Functions:** Provide local diagnostics, health checks, relevant logs, configuration and recovery procedures
- **Workflows / references:** F15
- **Test references:** TC-RECOVERY, TC-LOCAL
- **Approval:** Pending confirmation
- **Test result:** Not run

## Area 06 — Application administration and security — 8 entries

### BF-06-01 — Policy action audit

- **Priority:** MUST
- **Requirement / basis:** NAC11
- **Actor / service:** Backend; authorized SYS/NET review
- **Functions:** Record administrator actions, timestamps and relevant outcomes without secrets
- **Workflows / references:** F09–F15
- **Test references:** TC-NAC11
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-06-02 — Policy authorization

- **Priority:** MUST
- **Requirement / basis:** NAC16
- **Actor / service:** Backend; scoped SYS/NET
- **Functions:** Restrict policy-management operations to authorized administrators and scopes
- **Workflows / references:** F09, F10, F14, F17
- **Test references:** TC-NAC16
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-06-03 — Secret protection

- **Priority:** MUST
- **Requirement / basis:** NAC17
- **Actor / service:** NET, Backend
- **Functions:** Keep router credentials/API secrets on the server and out of clients, exports and logs
- **Workflows / references:** F02, F03, F09, F10, F15
- **Test references:** TC-NAC17
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-06-04 — Minimal browsing data

- **Priority:** MUST
- **Requirement / basis:** NAC19
- **Actor / service:** Client/data owner, SYS/NET, Backend
- **Functions:** Minimize student browsing-history collection; agree allowed logs, access and retention
- **Workflows / references:** F09–F15; D13
- **Test references:** TC-NAC19
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-06-05 — Classroom authorization

- **Priority:** REQUIRED / source obligation
- **Requirement / basis:** Unnumbered classroom-administration obligation; supports T01/T06 and S03
- **Actor / service:** Backend, SFU
- **Functions:** Prevent unauthorized broadcast control; check owned class and current admission/media grants
- **Workflows / references:** F04–F08, F12, F13; TC-AUTH
- **Test references:** TC-AUTH
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-06-06 — Application account management

- **Priority:** PROPOSED / no source priority
- **Requirement / basis:** Proposed account model, not a separate original numbered feature
- **Actor / service:** SYS
- **Functions:** Provision/deactivate accounts and define recovery
- **Workflows / references:** Role-permission matrix; D01/D14
- **Test references:** TC-AUTH
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-06-07 — Role assignment

- **Priority:** PROPOSED / no source priority
- **Requirement / basis:** Proposed RBAC allocation
- **Actor / service:** SYS; network authority for NET scope
- **Functions:** Explicitly assign/revoke roles; combine multiple roles without automatically granting network scope
- **Workflows / references:** Role-permission matrix; D01/D14/D15
- **Test references:** TC-AUTH
- **Approval:** Pending confirmation
- **Test result:** Not run

### BF-06-08 — Application settings and scoped review

- **Priority:** PROPOSED / no source priority
- **Requirement / basis:** Proposed administration UI/permission details
- **Actor / service:** SYS; limited scoped NET
- **Functions:** Manage permitted app settings; review only authorized audit/health data
- **Workflows / references:** Role-permission matrix; D15
- **Test references:** TC-AUTH
- **Approval:** Pending confirmation
- **Test result:** Not run


