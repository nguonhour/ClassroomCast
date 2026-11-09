# User stories and acceptance criteria

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Story status and granularity

These are 63 proposed requirement-level story candidates, with IDs US-{source requirement}. Deployment obligations are technical/enabler stories; split large candidates in refinement. Five supporting feature cards are covered through relevant CC work and architecture tests rather than invented source requirement IDs. Every candidate is Proposed; every acceptance test is Not run. Estimates are discussion seeds, not approved team velocity. Story estimates and CC estimates are alternative granularities and must not be added together.

## 2. Story catalogue and acceptance criteria

### US-NAC01 — Enable or disable network restrictions for a class

As a scoped policy administrator, I need the capability “enable or disable network restrictions for a class”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** NAC01 → F01 F10 / UC06 → CC-012, CC-013, CC-016, CC-018 → TC-NAC01.
- **Acceptance:** In a controlled authorized scope, enable and disable a profile; status and client-path probes show the effective result. Disabled/unreachable integration is not reported as verified.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC02 — Block website categories, including AI and coding agents

As a scoped policy administrator, I need the capability “block website categories, including AI and coding agents”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC02 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-016, CC-018 → TC-NAC02.
- **Acceptance:** For each configured category, predeclare representative denied domains and allowed controls; application produces the expected DNS/gateway results. Record list version and known coverage gaps.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC03 — Block or allow individual domains

As a scoped policy administrator, I need the capability “block or allow individual domains”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC03 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-016, CC-018 → TC-NAC03.
- **Acceptance:** A custom blocked domain is denied and an allowed domain is permitted through the configured enforcement path; invalid domain syntax is rejected before a network change.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC04 — Support allow-by-default and restricted-by-default policies

As a scoped policy administrator, I need the capability “support allow-by-default and restricted-by-default policies”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC04 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-016, CC-018 → TC-NAC04.
- **Acceptance:** Run allow-by-default and restricted-by-default profiles against the same declared test set; results match the agreed rule/exception precedence, including subdomain handling under D07.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC05 — Automatically apply policies when a class starts

As a scoped policy administrator, I need the capability “automatically apply policies when a class starts”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** NAC05 → F01 F10 / UC06 → CC-014, CC-016, CC-018 → TC-NAC05.
- **Acceptance:** Starting an authorized class with an approved profile creates an apply operation and audit outcome; healthy-scope verification meets proposed AT04. Starting from another class/scope cannot apply it.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC06 — Restore the previous policy when a class ends

As a scoped policy administrator, I need the capability “restore the previous policy when a class ends”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 8 points, to refine.
- **Trace:** NAC06 → F13 F14 / UC08 UC09 → CC-014, CC-015, CC-016, CC-018, CC-020 → TC-NAC06.
- **Acceptance:** After applying a temporary profile, end the class; prior effective rules and allowed/blocked client-path controls are restored within proposed AT05 when reachable. Restoration failures remain visible and retryable.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC07 — Save reusable policy profiles

As a scoped policy administrator, I need the capability “save reusable policy profiles”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC07 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-018 → TC-NAC07.
- **Acceptance:** Save two named profiles, reload the application/backend and retrieve equivalent rule versions; switching the selected profile does not itself falsely report network enforcement.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC08 — Add allowlist exceptions for approved websites

As a scoped policy administrator, I need the capability “add allowlist exceptions for approved websites”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC08 → F09 F10 F11 / UC05 UC06 → CC-011, CC-013, CC-016, CC-018 → TC-NAC08.
- **Acceptance:** Given a blocked category, add an approved domain exception; that control resolves/connects where upstream permits, while another category domain remains denied. Protect local app/media access throughout.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC09 — Schedule restrictions by date and time

As a scoped policy administrator, I need the capability “schedule restrictions by date and time”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** NAC09 → F17 / UC12 → CC-024 → TC-NAC09.
- **Acceptance:** Schedule a start/end against a declared timezone and test clock; each executes once per agreed idempotency semantics after restart, rechecks scope approval and records actual result. Missed-run policy awaits D11.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC10 — Display active policy and actual enforcement status

As a scoped policy administrator, I need the capability “display active policy and actual enforcement status”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC10 → F10 F13 F14 F15 / UC06 UC08 UC09 UC10 → CC-012, CC-013, CC-016, CC-018, CC-020 → TC-NAC10.
- **Acceptance:** Compare desired version, adapter read-back and affected-client probe results; UI accurately differentiates saved, applying, verified, degraded, failed and restoration-pending outcomes with timestamps.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC11 — Record administrator actions and timestamps

As a scoped policy administrator, I need the capability “record administrator actions and timestamps”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC11 → F10 F13 F14 F15 / UC06 UC08 UC09 UC10 → CC-014, CC-016, CC-018 → TC-NAC11.
- **Acceptance:** Perform a profile edit, apply, failed apply and restore; each audit record includes actor/service identity, action, scope, time and outcome, with no credentials.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC12 — Provide an emergency disable and rollback function

As a scoped policy administrator, I need the capability “provide an emergency disable and rollback function”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC12 → F14 F15 / UC09 UC10 → CC-015, CC-016, CC-018, CC-020 → TC-NAC12.
- **Acceptance:** Apply restrictions then invoke authorized emergency restore; prior policy verifies under proposed AT05. Unauthorized request changes no rules; an unreachable adapter yields a visible unresolved result.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC13 — Support temporary rules with automatic expiry

As a scoped policy administrator, I need the capability “support temporary rules with automatic expiry”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 8 points, to refine.
- **Trace:** NAC13 → F14 F15 / UC09 UC10 → CC-015, CC-016, CC-018, CC-020 → TC-NAC13.
- **Acceptance:** Apply a rule with declared expiry; close the admin browser and restart the backend before expiry. Recovery executes restoration once safely and verifies it under AT05 or displays pending/failure if unreachable.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC14 — Import and export policy configurations

As a scoped policy administrator, I need the capability “import and export policy configurations”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** NAC14 → F17 / UC12 → CC-024 → TC-NAC14.
- **Acceptance:** Export and reimport a sample profile; normalized rule content matches, secrets are absent, malformed imports are rejected and applying requires its own authorized operation.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC15 — Apply different policies to student groups or devices where supported

As a scoped policy administrator, I need the capability “apply different policies to student groups or devices where supported”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Could; **proposed size:** 8 points, to refine.
- **Trace:** NAC15 → F18 / UC13 → CC-026 → TC-NAC15.
- **Acceptance:** Where the chosen adapter supports isolated identity/scope, apply a group rule to target A and demonstrate that control B retains its prior policy. Otherwise mark unsupported and record the scope decision.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC16 — Restrict policy management to authorized administrators

As a scoped policy administrator, I need the capability “restrict policy management to authorized administrators”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC16 → F09 F10 F13 F14 F15 / UC05 UC06 UC08 UC09 UC10 → CC-007, CC-014, CC-016, CC-018, CC-020 → TC-NAC16.
- **Acceptance:** Execute the role-permission matrix’s representative allowed and denied operations; Student/Teacher roles alone cannot edit policies or infrastructure, and out-of-scope administrators cannot mutate that scope.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC17 — Keep router credentials and API secrets on the server

As a scoped policy administrator, I need the capability “keep router credentials and API secrets on the server”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC17 → F09 F10 F13 F14 F15 / UC05 UC06 UC08 UC09 UC10 → CC-012, CC-016, CC-018, CC-020 → TC-NAC17.
- **Acceptance:** Inspect built frontend, network responses, profile exports and logs for test secret markers; none appear. Adapter secrets/signing keys are accessible only through protected server configuration.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC18 — Prevent restrictions from breaking ClassroomCast itself

As a scoped policy administrator, I need the capability “prevent restrictions from breaking ClassroomCast itself”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC18 → F09 F10 F13 F14 F15 / UC05 UC06 UC08 UC09 UC10 → CC-011, CC-015, CC-016, CC-018, CC-020 → TC-NAC18.
- **Acceptance:** Apply the most restrictive agreed profile; a fresh student join, teacher controls, live media, local names and restoration remain functional. Reject an explicit conflicting local-service rule.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC19 — Minimize student browsing-history collection

As a scoped policy administrator, I need the capability “minimize student browsing-history collection”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** NAC19 → F09 F10 F13 F14 F15 / UC05 UC06 UC08 UC09 UC10 → CC-014, CC-016, CC-018, CC-020 → TC-NAC19.
- **Acceptance:** Review app/resolver logging and storage using synthetic browsing events; collect only agreed minimal data, mask/exclude unnecessary raw histories and demonstrate deletion according to D13.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-NAC20 — Support locally stored rules for offline operation

As a scoped policy administrator, I need the capability “support locally stored rules for offline operation”, so that I can manage supported restrictions safely and observe their actual effect.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** NAC20 → F03 F17 / UC12 UC15 → CC-023 → TC-NAC20.
- **Acceptance:** After provisioning local lists, disable WAN and restart services; profiles/rules remain retrievable and local test-domain policy operations work without remote list fetching. Baseline offline behavior remains required.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T01 — Create a classroom with a unique session ID and join code

As a teacher, I need the capability “create a classroom with a unique session ID and join code”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T01 → F04 F05 / UC01 UC02 → CC-003, CC-004, CC-018 → TC-T01.
- **Acceptance:** Create 10 concurrent active classes with the same authorized teacher or test teachers; all session IDs and active join codes are distinct. Closed-code join is rejected.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T02 — Start, stop, pause, and resume broadcasting

As a teacher, I need the capability “start, stop, pause, and resume broadcasting”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** T02 → F06 F07 / UC03 → CC-008, CC-010, CC-018 → TC-T02.
- **Acceptance:** Run start → pause → resume → stop on the supported setup; both viewers see each agreed state and publication stops after stop. Stopping sharing leaves the class open; pause/audio semantics await D08.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T03 — Share an entire screen, window, or browser tab where supported

As a teacher, I need the capability “share an entire screen, window, or browser tab where supported”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T03 → F06 F07 / UC03 → CC-005, CC-008, CC-018 → TC-T03.
- **Acceptance:** For every supported capture type (screen/window/tab), publish the teacher-selected source to two viewers; denial/cancellation creates no published capture. Record unsupported browser/source combinations under D09.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T04 — Share supported system audio and optional microphone audio

As a teacher, I need the capability “share supported system audio and optional microphone audio”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** T04 → F06 F07 / UC03 → CC-008, CC-018 → TC-T04.
- **Acceptance:** On each agreed OS/browser/source combination, verify shared audio when supported, microphone audio when selected, and no microphone publication when not selected. Record unsupported sources explicitly.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T05 — View connected students and their connection status

As a teacher, I need the capability “view connected students and their connection status”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T05 → F05 F08 / UC02 UC04 → CC-007, CC-010, CC-018 → TC-T05.
- **Acceptance:** Join two viewers and disconnect one; roster shows the correct participant count and each current connection state within proposed 5 s after the server detects the event.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T06 — Approve, reject, remove, and block participants

As a teacher, I need the capability “approve, reject, remove, and block participants”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** T06 → F05 F08 / UC02 UC04 → CC-007, CC-010, CC-018 → TC-T06.
- **Acceptance:** Demonstrate approve, reject, remove and block separately. Removed access closes; blocked rejoin fails for the agreed identity/duration. Repeat cross-class control attempts and verify denial; D02/D03 define guarantees.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T07 — Configure resolution, frame rate, and bitrate

As a teacher, I need the capability “configure resolution, frame rate, and bitrate”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T07 → F06 F07 / UC03 → CC-008, CC-010, CC-018 → TC-T07.
- **Acceptance:** Apply two supported quality profiles; record configured and observed resolution, frame rate and bitrate with adaptation limits. Unsupported input is rejected or reported; do not assert exact network bitrate from settings alone.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T08 — Display the classroom URL, join code, and QR code

As a teacher, I need the capability “display the classroom URL, join code, and QR code”, so that I can operate an owned classroom.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** T08 → F04 F05 / UC01 UC02 → CC-003, CC-004, CC-018 → TC-T08.
- **Acceptance:** From a second laptop, open the displayed URL and decoded QR destination; both point to the intended local class/join route and the displayed code joins that class.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T09 — Display streaming health and connection diagnostics

As a teacher, I need the capability “display streaming health and connection diagnostics”, so that I can operate an owned classroom.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** T09 → F15 / UC10 → CC-023 → TC-T09.
- **Acceptance:** During a controlled media fault, diagnostics distinguish connection state, missing/stalled media and available WebRTC statistics; display measurement time and refresh within proposed 5 s.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T10 — Share presentation files, PDFs, images, and videos

As a teacher, I need the capability “share presentation files, PDFs, images, and videos”, so that I can operate an owned classroom.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** T10 → F16 / UC11 → CC-025 → TC-T10.
- **Acceptance:** Exercise one approved presentation, PDF, image and video sample through the agreed sharing method; admitted viewers can access it and rejected formats show a useful error. D16 defines upload versus media presentation behavior.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-T11 — Display session history and participant counts

As a teacher, I need the capability “display session history and participant counts”, so that I can operate an owned classroom.

- **Priority:** Could; **proposed size:** 3 points, to refine.
- **Trace:** T11 → F18 / UC13 → CC-026 → TC-T11.
- **Acceptance:** End two owned classes; retained history shows their correct IDs/times and participant counts. Another teacher cannot read them; summaries do not imply video recordings.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S01 — Join through a local URL or QR code

As a student, I need the capability “join through a local URL or QR code”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S01 → F05 / UC02 → CC-003, CC-006, CC-018 → TC-S01.
- **Acceptance:** From two test laptops on the selected network, the local URL and QR destination both reach the join page with trusted browser access. Record page-ready time against proposed AT01.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S02 — Enter a classroom join code

As a student, I need the capability “enter a classroom join code”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S02 → F05 / UC02 → CC-003, CC-006, CC-018 → TC-S02.
- **Acceptance:** In both proposed modes, missing, invalid, expired or closed codes are rejected. Code admission permits viewing only after final checks; code + approval keeps a valid request pending until owning-Teacher approval and fresh atomic admission/capacity checks. Wrong guesses follow the agreed rate-limit rule; execute TC-ADM01–TC-ADM07.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S03 — Watch the teacher's screen in real time

As a student, I need the capability “watch the teacher's screen in real time”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S03 → F06 F07 / UC03 → CC-005, CC-006, CC-018 → TC-S03.
- **Acceptance:** Two admitted viewers receive the selected live screen via the local SFU; non-admitted clients cannot subscribe. Measure physical-viewer playback and target-scale conditions under AT02/AT03.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S04 — Play supported shared audio with volume control

As a student, I need the capability “play supported shared audio with volume control”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S04 → F06 F07 / UC03 → CC-009, CC-018 → TC-S04.
- **Acceptance:** On supported audio combinations, each viewer can start playback and adjust/mute its own audio independently; another viewer’s volume and teacher publication are unchanged.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S05 — View the broadcast in fullscreen

As a student, I need the capability “view the broadcast in fullscreen”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S05 → F06 F07 / UC03 → CC-009, CC-018 → TC-S05.
- **Acceptance:** Enter/exit fullscreen on each supported browser using user interaction; playback continues or any unsupported behavior is explained and recorded.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S06 — Reconnect after temporary network interruptions

As a student, I need the capability “reconnect after temporary network interruptions”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 5 points, to refine.
- **Trace:** S06 → F12 / UC07 → CC-009, CC-018 → TC-S06.
- **Acceptance:** Interrupt one viewer’s network for 10 s; it reconnects to the same active class within proposed 15 s of reachability returning in at least 9/10 attempts. Removed/ended sessions never auto-readmit.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S07 — Show connection status and useful errors

As a student, I need the capability “show connection status and useful errors”, so that I can participate in an authorized local class.

- **Priority:** Must; **proposed size:** 3 points, to refine.
- **Trace:** S07 → F05 F07 F12 F15 / UC02 UC03 UC07 UC10 → CC-006, CC-009, CC-018 → TC-S07.
- **Acceptance:** Inject invalid code, full class, denied admission, ended session, network loss and media failure; each produces the correct actionable status without exposing secrets.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S08 — Enter a student name or assigned student ID

As a student, I need the capability “enter a student name or assigned student ID”, so that I can participate in an authorized local class.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** S08 → F05 / UC02 → CC-025 → TC-S08.
- **Acceptance:** With the feature enabled, enter a valid name/assigned ID; invalid input receives validation feedback and the allowed identifier is associated with the admitted participant. Identity strength and retention await D03/D13.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S09 — Download teacher-provided materials when permitted

As a student, I need the capability “download teacher-provided materials when permitted”, so that I can participate in an authorized local class.

- **Priority:** Should; **proposed size:** 3 points, to refine.
- **Trace:** S09 → F16 / UC11 → CC-025 → TC-S09.
- **Acceptance:** An admitted student downloads an allowed sample matching its recorded checksum; download denied when permission is off or admission is revoked; direct URL requests enforce the same checks.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-S10 — Raise a hand, submit questions, or answer polls

As a student, I need the capability “raise a hand, submit questions, or answer polls”, so that I can participate in an authorized local class.

- **Priority:** Could; **proposed size:** 3 points, to refine.
- **Trace:** S10 → F18 / UC13 → CC-026 → TC-S10.
- **Acceptance:** For each selected interaction (hand/question/poll), an admitted student action reaches the owning teacher; unauthorized or closed-activity submissions are rejected. Specific interaction set awaits D17.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN01 — Use an approved local server address or hostname

As a authorized network installer, I need the capability “use an approved local server address or hostname”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN01 → F02 / UC14 → CC-002, CC-017 → TC-CN01.
- **Acceptance:** Campus IT approves server name/address; two campus laptops reach the correct server with trusted access. Preserve approval and configuration evidence.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN02 — Verify student devices can reach the application and signaling services

As a authorized network installer, I need the capability “verify student devices can reach the application and signaling services”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN02 → F02 / UC14 → CC-002, CC-017 → TC-CN02.
- **Acceptance:** From two representative student network locations, verify app/API and media-signaling connectivity; report each separate endpoint and any inaccessible segment.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN03 — Confirm required WebRTC media traffic is permitted

As a authorized network installer, I need the capability “confirm required WebRTC media traffic is permitted”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN03 → F02 / UC14 → CC-002, CC-017 → TC-CN03.
- **Acceptance:** Establish real audio/video over the approved configured media path; record actual ports/transports and approved firewall evidence. Signaling-only success does not pass.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN04 — Verify Wi-Fi client isolation and guest-network restrictions

As a authorized network installer, I need the capability “verify Wi-Fi client isolation and guest-network restrictions”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN04 → F02 / UC14 → CC-002, CC-017 → TC-CN04.
- **Acceptance:** Test the intended SSID/VLAN/isolation settings; students reach only the required server/enforcement paths, and guest restrictions affecting the flow are recorded.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN05 — Obtain campus IT approval for hosting and firewall changes

As a authorized network installer, I need the capability “obtain campus IT approval for hosting and firewall changes”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN05 → F02 / UC14 → CC-002, CC-017 → TC-CN05.
- **Acceptance:** Record written campus IT authorization for hosting and any required firewall changes before making those changes; absence leaves this criterion pending, not passed.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN06 — Validate Wi-Fi capacity and network throughput for 150 students

As a authorized network installer, I need the capability “validate Wi-Fi capacity and network throughput for 150 students”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 8 points, to refine.
- **Trace:** CN06 → F02 / UC14 → CC-019 → TC-CN06.
- **Acceptance:** Execute staged 50/100/150 subscriber tests and AT02/AT03 on the documented campus setup; identify physical versus simulated clients and whether 150-device Wi-Fi capacity is actually demonstrated.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN07 — Provide QR-code and manual URL discovery

As a authorized network installer, I need the capability “provide QR-code and manual URL discovery”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN07 → F02 / UC14 → CC-002, CC-017 → TC-CN07.
- **Acceptance:** Join from a campus laptop by both manual URL and QR destination; network instructions identify the correct campus network and server.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN08 — Avoid IP address conflicts with existing campus services

As a authorized network installer, I need the capability “avoid IP address conflicts with existing campus services”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN08 → F02 / UC14 → CC-002, CC-017 → TC-CN08.
- **Acceptance:** Campus IT checks reserved/static server addressing against DHCP/IP allocations; conflict checks show no duplicate address before the pilot.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN09 — Host required application components locally for offline operation

As a authorized network installer, I need the capability “host required application components locally for offline operation”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** CN09 → F02 / UC14 → CC-002, CC-017, CC-020 → TC-CN09.
- **Acceptance:** With images/assets/certificates provisioned, disconnect WAN and use a fresh browser session; class creation, joining and local media work without CDN/cloud requests.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-CN10 — Integrate network restrictions with campus-approved DNS or gateway controls

As a authorized network installer, I need the capability “integrate network restrictions with campus-approved DNS or gateway controls”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 5 points, to refine.
- **Trace:** CN10 → F02 / UC14 → CC-012, CC-017 → TC-CN10.
- **Acceptance:** Within written approved scope, apply an approved profile through the campus DNS/gateway adapter, verify client-path effects, and restore previous rules. Missing integration remains an acceptance gap.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR01 — Business-class Wi-Fi 6 or better equipment suitable for high client density

As a authorized network installer, I need the capability “business-class Wi-Fi 6 or better equipment suitable for high client density”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR01 → F03 / UC15 → CC-019 → TC-OR01.
- **Acceptance:** Record Wi-Fi 6-or-better equipment model/capabilities and staged load results for the intended client density; brochure client count alone is insufficient.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR02 — Configurable classroom SSID and Wi-Fi password

As a authorized network installer, I need the capability “configurable classroom SSID and Wi-Fi password”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR02 → F03 / UC15 → CC-002, CC-017 → TC-OR02.
- **Acceptance:** Configure the intended classroom SSID/password; two student laptops associate and obtain local connectivity without changing per-class infrastructure rules.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR03 — WPA2-AES or WPA3 security where compatible

As a authorized network installer, I need the capability “wPA2-AES or WPA3 security where compatible”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR03 → F03 / UC15 → CC-002, CC-017 → TC-OR03.
- **Acceptance:** Inspect negotiated Wi-Fi security on the supported clients: WPA2-AES or compatible WPA3 as agreed; record any incompatible devices and resolution.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR04 — DHCP capacity for all students and support devices

As a authorized network installer, I need the capability “dHCP capacity for all students and support devices”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR04 → F03 / UC15 → CC-002, CC-017 → TC-OR04.
- **Acceptance:** DHCP pool/lease configuration supports at least 150 students plus inventoried support devices; test lease assignment and no duplicate allocations using declared physical/simulated conditions.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR05 — Stable server IP address or local hostname

As a authorized network installer, I need the capability “stable server IP address or local hostname”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR05 → F03 / UC15 → CC-002, CC-017 → TC-OR05.
- **Acceptance:** Reboot router/server; the configured stable server address/local name still leads students to the intended application and media endpoint.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR06 — Wired Gigabit Ethernet or faster connection to the server where possible

As a authorized network installer, I need the capability “wired Gigabit Ethernet or faster connection to the server where possible”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR06 → F03 / UC15 → CC-002, CC-017 → TC-OR06.
- **Acceptance:** Use and record a negotiated Gigabit-or-faster wired server link where possible; if unavailable, record the exception and measured capacity impact for acceptance.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR07 — Appropriate client isolation settings that permit access to the server and approved enforcement services

As a authorized network installer, I need the capability “appropriate client isolation settings that permit access to the server and approved enforcement services”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR07 → F03 / UC15 → CC-002, CC-017 → TC-OR07.
- **Acceptance:** With intended isolation enabled/configured, two student clients still reach the server, media and approved enforcement paths; document permitted connectivity.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR08 — One or more access points based on classroom capacity testing

As a authorized network installer, I need the capability “one or more access points based on classroom capacity testing”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 8 points, to refine.
- **Trace:** OR08 → F03 / UC15 → CC-019 → TC-OR08.
- **Acceptance:** Test increasing client loads, measure bottlenecks and choose AP count/placement that meets agreed AT02/AT03; repeat after relevant configuration changes.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR09 — Support for additional access points and a wired switch

As a authorized network installer, I need the capability “support for additional access points and a wired switch”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR09 → F03 / UC15 → CC-019 → TC-OR09.
- **Acceptance:** Demonstrate adding the supported AP/switch arrangement without address conflicts or loss of class reachability; preserve a topology/configuration record.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR10 — Portable power, cables, and carrying equipment

As a authorized network installer, I need the capability “portable power, cables, and carrying equipment”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR10 → F03 / UC15 → CC-002, CC-017 → TC-OR10.
- **Acceptance:** Inventory required power supplies, cables/adapters and transport protection; perform one full setup and power/restart recovery using the portable kit.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR11 — Fully functional local services without WAN or internet access

As a authorized network installer, I need the capability “fully functional local services without WAN or internet access”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 3 points, to refine.
- **Trace:** OR11 → F03 / UC15 → CC-002, CC-017, CC-020 → TC-OR11.
- **Acceptance:** With WAN physically disconnected and local dependencies provisioned, start a fresh class and receive screen/supported audio on two laptops; apply/restore rules against controlled local test domains.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.

### US-OR12 — Local software-based policy management without requiring manual rule changes for each class

As a authorized network installer, I need the capability “local software-based policy management without requiring manual rule changes for each class”, so that I can provide a tested local deployment.

- **Priority:** Unlabeled / proposed Must*; **proposed size:** 5 points, to refine.
- **Trace:** OR12 → F03 / UC15 → CC-012, CC-017 → TC-OR12.
- **Acceptance:** Apply and restore two class profiles through the supported software adapter with no manual router rule edits between classes; unsupported automation is visibly reported as a gap.
- **Dependencies:** agreed role/scope and supported deployment; relevant decisions in the decision register.
