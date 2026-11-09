# Supplied specification — preserved source snapshot

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Provenance

Verbatim body from the supplied ClassroomCast specification attachment. Historical requirements evidence; technology recommendations and numeric targets are not proof of feasibility or approval.

## 2. Original text

ClassroomCast
Project name: ClassroomCast — Local Network Screen Sharing and Access Control System

The key update is that network blocking must be managed at the software level, through the ClassroomCast administrator dashboard and backend policy manager, rather than requiring teachers to configure router settings manually.

The system will support both the existing campus network and a teacher-owned router, with the same application and administration interface.
1. Project overview

Classroom broadcasting

Teachers share their screens, presentations, supported system audio, microphone audio, and classroom media with students in real time.




Classroom management

Teachers create classes, generate QR codes and join codes, monitor students, and control participation.




Software-managed network access control

Administrators configure website restrictions, including AI websites and coding agents, using policy profiles and a supported local enforcement service.




Network administration and diagnostics

Manage the two deployment modes, monitor connectivity, check enforcement status, and recover from network configuration problems.



Target environment
- One teacher and 50–150 students per classroom.
- Students use laptops with a supported web browser; no student application installation is required.
- The system operates on a local network without requiring internet access during class.
- Two network modes: existing campus Wi-Fi/LAN or a dedicated teacher-owned router.
- One shared software platform for both modes.
2. Software-level network blocking — updated requirement
The administrator must be able to manage public internet restrictions directly from the ClassroomCast dashboard.

Important technical distinction: The blocking interface and policy management can be implemented entirely in software. However, blocking websites on student laptops requires an enforcement component, such as a local DNS filtering service or an authorized gateway/firewall integration. A normal website alone cannot reliably block other websites across devices.

The recommended design is a local policy manager integrated with a DNS filtering service, with optional router or firewall adapters for stronger enforcement.
2.1 Administrator features
ID	Requirement	Priority
NAC01	Enable or disable network restrictions for a class	Must
NAC02	Block website categories, including AI and coding agents	Must
NAC03	Block or allow individual domains	Must
NAC04	Support allow-by-default and restricted-by-default policies	Must
NAC05	Automatically apply policies when a class starts	Must
NAC06	Restore the previous policy when a class ends	Must
NAC07	Save reusable policy profiles	Must
NAC08	Add allowlist exceptions for approved websites	Must
NAC09	Schedule restrictions by date and time	Should
NAC10	Display active policy and actual enforcement status	Must
NAC11	Record administrator actions and timestamps	Must
NAC12	Provide an emergency disable and rollback function	Must
NAC13	Support temporary rules with automatic expiry	Must
NAC14	Import and export policy configurations	Should
NAC15	Apply different policies to student groups or devices where supported	Could
NAC16	Restrict policy management to authorized administrators	Must
NAC17	Keep router credentials and API secrets on the server	Must
NAC18	Prevent restrictions from breaking ClassroomCast itself	Must
NAC19	Minimize student browsing-history collection	Must
NAC20	Support locally stored rules for offline operation	Should

2.2 Website categories
The administrator should be able to select categories, search for domains, add custom domains, and define exceptions.
Example: Exam Mode
Illustrative policy configuration, not an active network restriction.
[x] AI websites and assistants
[x] AI coding agents and cloud IDEs
[x] Social media and public messaging
[x] Online gaming
[ ] Video and music streaming
[ ] Custom administrator-defined categories

Selected categories: 4

This is a preview of the desired interface. It does not apply restrictions to the current network.
Use selected categories for specification
Additional category groups:
- AI services: generative AI chat, AI search, writing, and image-generation websites.
- Developer services: cloud coding agents, AI programming assistants, online IDEs, and selected code-hosting services.
- Communication: social networks and public messaging services.
- Entertainment: streaming platforms, online games, and selected download sites.
- Custom rules: administrator-defined categories and individual domains.
The system should support profile presets such as Normal Class, Programming Lab, and Exam Mode. Programming Lab, for example, could block selected AI assistants while allowing approved documentation, programming references, and course resources.
2.3 How the software-level blocking works
ClassroomCast Admin Dashboard

Manage categories, domains, profiles, schedules, and exceptions

Backend Policy Manager

Validate permissions, store policies, apply session rules, and log changes

Network Enforcement Service

Local DNS filter first; optional supported router/firewall integration

Student laptops

Access approved public websites while configured restrictions are enforced


Implementation requirements:
1. Administrators create and save policies through the web interface.
2. The backend validates the policy and sends it to the configured enforcement service.
3. The enforcement service applies domain rules and returns a success or failure result.
4. The dashboard shows both the configured policy and the verified enforcement health.
5. When a class ends, temporary rules expire and the previous network policy is restored.
6. Local ClassroomCast traffic must remain available even when internet access is restricted.
7. All application assets, policy rules, and required local services must remain usable without internet access.
Limitations to account for: DNS filtering can be bypassed through VPNs, alternate DNS resolvers, encrypted DNS, or direct IP connections unless additional controls are configured. Blocking a website's main domain may not cover all associated services. Locally installed coding agents may also operate without accessing a blocked website. Stronger control may require gateway enforcement and, where appropriate, managed-device policies.

For campus network mode, the system must only apply network restrictions with authorization from campus IT. The application must not attempt to bypass campus network controls.
3. Classroom broadcasting requirements
3.1 Teacher dashboard
ID	Requirement	Priority
T01	Create a classroom with a unique session ID and join code	Must
T02	Start, stop, pause, and resume broadcasting	Must
T03	Share an entire screen, window, or browser tab where supported	Must
T04	Share supported system audio and optional microphone audio	Must
T05	View connected students and their connection status	Must
T06	Approve, reject, remove, and block participants	Must
T07	Configure resolution, frame rate, and bitrate	Must
T08	Display the classroom URL, join code, and QR code	Must
T09	Display streaming health and connection diagnostics	Should
T10	Share presentation files, PDFs, images, and videos	Should
T11	Display session history and participant counts	Could

3.2 Student interface
ID	Requirement	Priority
S01	Join through a local URL or QR code	Must
S02	Enter a classroom join code	Must
S03	Watch the teacher's screen in real time	Must
S04	Play supported shared audio with volume control	Must
S05	View the broadcast in fullscreen	Must
S06	Reconnect after temporary network interruptions	Must
S07	Show connection status and useful errors	Must
S08	Enter a student name or assigned student ID	Should
S09	Download teacher-provided materials when permitted	Should
S10	Raise a hand, submit questions, or answer polls	Could

3.3 Classroom administration
- Manage classroom sessions, join codes, and participant limits.
- Prevent unauthorized users from controlling broadcasts.
- End a session and disconnect all participants.
- Provide clear network connection instructions.
- Provide a local diagnostic page.
- Integrate classroom start/end events with network access policies.
- Ensure network restrictions cannot block the classroom's local server or media connections.
4. Deployment mode A — Existing campus network
The system must operate on the institution's existing Wi-Fi and LAN infrastructure.
ClassroomCast local server

Web application + signaling + SFU + policy manager

Campus LAN / Wi-Fi

Existing access points, switches, routing and authorized network controls

50–150 student laptops

Browser-based classroom access


Campus network requirements
ID	Requirement
CN01	Use an approved local server address or hostname.
CN02	Verify student devices can reach the application and signaling services.
CN03	Confirm required WebRTC media traffic is permitted.
CN04	Verify Wi-Fi client isolation and guest-network restrictions.
CN05	Obtain campus IT approval for hosting and firewall changes.
CN06	Validate Wi-Fi capacity and network throughput for 150 students.
CN07	Provide QR-code and manual URL discovery.
CN08	Avoid IP address conflicts with existing campus services.
CN09	Host required application components locally for offline operation.
CN10	Integrate network restrictions with campus-approved DNS or gateway controls.

Recommended deployment: Use a dedicated server connected to the campus LAN via Ethernet. Campus IT controls the underlying network, while authorized ClassroomCast administrators manage supported policies through the software dashboard.

The software must clearly indicate if campus IT has not enabled or authorized network enforcement.
5. Deployment mode B — Teacher-owned router
This mode creates an independent classroom network that can be transported between classrooms.
Teacher laptop or mini-PC

ClassroomCast server + SFU + policy manager

Dedicated Wi-Fi access points

DHCP + local connectivity + approved DNS enforcement

50–150 student laptops

Classroom SSID + QR code + browser


Router and hardware requirements
ID	Requirement
OR01	Business-class Wi-Fi 6 or better equipment suitable for high client density.
OR02	Configurable classroom SSID and Wi-Fi password.
OR03	WPA2-AES or WPA3 security where compatible.
OR04	DHCP capacity for all students and support devices.
OR05	Stable server IP address or local hostname.
OR06	Wired Gigabit Ethernet or faster connection to the server where possible.
OR07	Appropriate client isolation settings that permit access to the server and approved enforcement services.
OR08	One or more access points based on classroom capacity testing.
OR09	Support for additional access points and a wired switch.
OR10	Portable power, cables, and carrying equipment.
OR11	Fully functional local services without WAN or internet access.
OR12	Local software-based policy management without requiring manual rule changes for each class.

Suggested setup defaults
These are examples, not fixed addresses.
- Router LAN: 192.168.50.1
- Classroom server: 192.168.50.10
- Student DHCP pool: 192.168.50.50–192.168.50.240
- Classroom SSID: ClassroomCast
- Join method: local URL, QR code, and classroom code.
The server should run the local DNS filtering service or integrate with a supported local gateway. The software should configure policies through a documented API wherever possible, with a manual-configuration warning if the equipment does not support automation.
6. Shared software architecture
Component	Recommended technology	Responsibility
Frontend	React + Vite + TypeScript	Teacher, student, and administrator interfaces
Screen capture	Browser Screen Capture API	Capture teacher-selected content
Media transport	WebRTC	Real-time audio/video delivery
Signaling	Node.js + Socket.IO or WebSocket	Establish media connections
Media server	mediasoup or LiveKit SFU	Distribute one teacher stream to many students
Backend API	Node.js, optionally NestJS	Sessions, permissions, policy management
Database	SQLite initially; PostgreSQL if needed	Users, policies, settings, audit records
Network enforcement	Local DNS filtering service, such as AdGuard Home or Pi-hole	Apply domain-level allow/block rules
Enforcement adapters	Supported DNS, router, or firewall APIs	Apply and verify network policies
Reverse proxy	Caddy or Nginx	Serve the application and configure local HTTPS
Deployment	Docker Compose or native services	Run components locally
Monitoring	WebRTC statistics and server metrics	Measure health and performance

Architectural requirements
- Use a Selective Forwarding Unit (SFU) rather than direct teacher-to-student mesh as the default production architecture for 50–150 students.
- Keep the web interface, signaling server, SFU, policy manager, and required filtering services available locally.
- Keep network credentials and API secrets on the server, never in browser code.
- Separate the application policy configuration from the actual enforcement status.
- Provide health checks, logs, configuration files, and recovery procedures.
- Support local HTTPS or another browser-supported secure-context arrangement for screen and microphone capture
