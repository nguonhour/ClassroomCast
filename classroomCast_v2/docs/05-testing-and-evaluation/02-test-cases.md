# Test-case catalogue

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Catalogue authority and execution convention

The 63 criteria below are preserved from the existing requirements acceptance catalogue. They remain **Proposed**; results are **Not run**. Each case needs the detailed environment and evidence record from [strategy](01-testing-strategy.md). Steps are specified as the executable scenarios within each criterion; before running, instantiate named devices, class, domains, credentials and expected values. Numeric conditions refer to AT proposals, not approved commitments.

## 2. Original requirement cases

| Requirement | Story | Test ID | Procedure and expected result |
|---|---|---|---|
| NAC01 | US-NAC01 | TC-NAC01 | In a controlled authorized scope, enable and disable a profile; status and client-path probes show the effective result. Disabled/unreachable integration is not reported as verified. |
| NAC02 | US-NAC02 | TC-NAC02 | For each configured category, predeclare representative denied domains and allowed controls; application produces the expected DNS/gateway results. Record list version and known coverage gaps. |
| NAC03 | US-NAC03 | TC-NAC03 | A custom blocked domain is denied and an allowed domain is permitted through the configured enforcement path; invalid domain syntax is rejected before a network change. |
| NAC04 | US-NAC04 | TC-NAC04 | Run allow-by-default and restricted-by-default profiles against the same declared test set; results match the agreed rule/exception precedence, including subdomain handling under D07. |
| NAC05 | US-NAC05 | TC-NAC05 | Starting an authorized class with an approved profile creates an apply operation and audit outcome; healthy-scope verification meets proposed AT04. Starting from another class/scope cannot apply it. |
| NAC06 | US-NAC06 | TC-NAC06 | After applying a temporary profile, end the class; prior effective rules and allowed/blocked client-path controls are restored within proposed AT05 when reachable. Restoration failures remain visible and retryable. |
| NAC07 | US-NAC07 | TC-NAC07 | Save two named profiles, reload the application/backend and retrieve equivalent rule versions; switching the selected profile does not itself falsely report network enforcement. |
| NAC08 | US-NAC08 | TC-NAC08 | Given a blocked category, add an approved domain exception; that control resolves/connects where upstream permits, while another category domain remains denied. Protect local app/media access throughout. |
| NAC09 | US-NAC09 | TC-NAC09 | Schedule a start/end against a declared timezone and test clock; each executes once per agreed idempotency semantics after restart, rechecks scope approval and records actual result. Missed-run policy awaits D11. |
| NAC10 | US-NAC10 | TC-NAC10 | Compare desired version, adapter read-back and affected-client probe results; UI accurately differentiates saved, applying, verified, degraded, failed and restoration-pending outcomes with timestamps. |
| NAC11 | US-NAC11 | TC-NAC11 | Perform a profile edit, apply, failed apply and restore; each audit record includes actor/service identity, action, scope, time and outcome, with no credentials. |
| NAC12 | US-NAC12 | TC-NAC12 | Apply restrictions then invoke authorized emergency restore; prior policy verifies under proposed AT05. Unauthorized request changes no rules; an unreachable adapter yields a visible unresolved result. |
| NAC13 | US-NAC13 | TC-NAC13 | Apply a rule with declared expiry; close the admin browser and restart the backend before expiry. Recovery executes restoration once safely and verifies it under AT05 or displays pending/failure if unreachable. |
| NAC14 | US-NAC14 | TC-NAC14 | Export and reimport a sample profile; normalized rule content matches, secrets are absent, malformed imports are rejected and applying requires its own authorized operation. |
| NAC15 | US-NAC15 | TC-NAC15 | Where the chosen adapter supports isolated identity/scope, apply a group rule to target A and demonstrate that control B retains its prior policy. Otherwise mark unsupported and record the scope decision. |
| NAC16 | US-NAC16 | TC-NAC16 | Execute the role-permission matrix’s representative allowed and denied operations; Student/Teacher roles alone cannot edit policies or infrastructure, and out-of-scope administrators cannot mutate that scope. |
| NAC17 | US-NAC17 | TC-NAC17 | Inspect built frontend, network responses, profile exports and logs for test secret markers; none appear. Adapter secrets/signing keys are accessible only through protected server configuration. |
| NAC18 | US-NAC18 | TC-NAC18 | Apply the most restrictive agreed profile; a fresh student join, teacher controls, live media, local names and restoration remain functional. Reject an explicit conflicting local-service rule. |
| NAC19 | US-NAC19 | TC-NAC19 | Review app/resolver logging and storage using synthetic browsing events; collect only agreed minimal data, mask/exclude unnecessary raw histories and demonstrate deletion according to D13. |
| NAC20 | US-NAC20 | TC-NAC20 | After provisioning local lists, disable WAN and restart services; profiles/rules remain retrievable and local test-domain policy operations work without remote list fetching. Baseline offline behavior remains required. |
| T01 | US-T01 | TC-T01 | Create 10 concurrent active classes with the same authorized teacher or test teachers; all session IDs and active join codes are distinct. Closed-code join is rejected. |
| T02 | US-T02 | TC-T02 | Run start → pause → resume → stop on the supported setup; both viewers see each agreed state and publication stops after stop. Stopping sharing leaves the class open; pause/audio semantics await D08. |
| T03 | US-T03 | TC-T03 | For every supported capture type (screen/window/tab), publish the teacher-selected source to two viewers; denial/cancellation creates no published capture. Record unsupported browser/source combinations under D09. |
| T04 | US-T04 | TC-T04 | On each agreed OS/browser/source combination, verify shared audio when supported, microphone audio when selected, and no microphone publication when not selected. Record unsupported sources explicitly. |
| T05 | US-T05 | TC-T05 | Join two viewers and disconnect one; roster shows the correct participant count and each current connection state within proposed 5 s after the server detects the event. |
| T06 | US-T06 | TC-T06 | Demonstrate approve, reject, remove and block separately. Removed access closes; blocked rejoin fails for the agreed identity/duration. Repeat cross-class control attempts and verify denial; D02/D03 define guarantees. |
| T07 | US-T07 | TC-T07 | Apply two supported quality profiles; record configured and observed resolution, frame rate and bitrate with adaptation limits. Unsupported input is rejected or reported; do not assert exact network bitrate from settings alone. |
| T08 | US-T08 | TC-T08 | From a second laptop, open the displayed URL and decoded QR destination; both point to the intended local class/join route and the displayed code joins that class. |
| T09 | US-T09 | TC-T09 | During a controlled media fault, diagnostics distinguish connection state, missing/stalled media and available WebRTC statistics; display measurement time and refresh within proposed 5 s. |
| T10 | US-T10 | TC-T10 | Exercise one approved presentation, PDF, image and video sample through the agreed sharing method; admitted viewers can access it and rejected formats show a useful error. D16 defines upload versus media presentation behavior. |
| T11 | US-T11 | TC-T11 | End two owned classes; retained history shows their correct IDs/times and participant counts. Another teacher cannot read them; summaries do not imply video recordings. |
| S01 | US-S01 | TC-S01 | From two test laptops on the selected network, the local URL and QR destination both reach the join page with trusted browser access. Record page-ready time against proposed AT01. |
| S02 | US-S02 | TC-S02 | In both proposed modes, missing, invalid, expired or closed codes are rejected. Code admission permits viewing only after final checks; code + approval keeps a valid request pending until owning-Teacher approval and fresh atomic admission/capacity checks. Wrong guesses follow the agreed rate-limit rule; execute TC-ADM01–TC-ADM07. |
| S03 | US-S03 | TC-S03 | Two admitted viewers receive the selected live screen via the local SFU; non-admitted clients cannot subscribe. Measure physical-viewer playback and target-scale conditions under AT02/AT03. |
| S04 | US-S04 | TC-S04 | On supported audio combinations, each viewer can start playback and adjust/mute its own audio independently; another viewer’s volume and teacher publication are unchanged. |
| S05 | US-S05 | TC-S05 | Enter/exit fullscreen on each supported browser using user interaction; playback continues or any unsupported behavior is explained and recorded. |
| S06 | US-S06 | TC-S06 | Interrupt one viewer’s network for 10 s; it reconnects to the same active class within proposed 15 s of reachability returning in at least 9/10 attempts. Removed/ended sessions never auto-readmit. |
| S07 | US-S07 | TC-S07 | Inject invalid code, full class, denied admission, ended session, network loss and media failure; each produces the correct actionable status without exposing secrets. |
| S08 | US-S08 | TC-S08 | With the feature enabled, enter a valid name/assigned ID; invalid input receives validation feedback and the allowed identifier is associated with the admitted participant. Identity strength and retention await D03/D13. |
| S09 | US-S09 | TC-S09 | An admitted student downloads an allowed sample matching its recorded checksum; download denied when permission is off or admission is revoked; direct URL requests enforce the same checks. |
| S10 | US-S10 | TC-S10 | For each selected interaction (hand/question/poll), an admitted student action reaches the owning teacher; unauthorized or closed-activity submissions are rejected. Specific interaction set awaits D17. |
| CN01 | US-CN01 | TC-CN01 | Campus IT approves server name/address; two campus laptops reach the correct server with trusted access. Preserve approval and configuration evidence. |
| CN02 | US-CN02 | TC-CN02 | From two representative student network locations, verify app/API and media-signaling connectivity; report each separate endpoint and any inaccessible segment. |
| CN03 | US-CN03 | TC-CN03 | Establish real audio/video over the approved configured media path; record actual ports/transports and approved firewall evidence. Signaling-only success does not pass. |
| CN04 | US-CN04 | TC-CN04 | Test the intended SSID/VLAN/isolation settings; students reach only the required server/enforcement paths, and guest restrictions affecting the flow are recorded. |
| CN05 | US-CN05 | TC-CN05 | Record written campus IT authorization for hosting and any required firewall changes before making those changes; absence leaves this criterion pending, not passed. |
| CN06 | US-CN06 | TC-CN06 | Execute staged 50/100/150 subscriber tests and AT02/AT03 on the documented campus setup; identify physical versus simulated clients and whether 150-device Wi-Fi capacity is actually demonstrated. |
| CN07 | US-CN07 | TC-CN07 | Join from a campus laptop by both manual URL and QR destination; network instructions identify the correct campus network and server. |
| CN08 | US-CN08 | TC-CN08 | Campus IT checks reserved/static server addressing against DHCP/IP allocations; conflict checks show no duplicate address before the pilot. |
| CN09 | US-CN09 | TC-CN09 | With images/assets/certificates provisioned, disconnect WAN and use a fresh browser session; class creation, joining and local media work without CDN/cloud requests. |
| CN10 | US-CN10 | TC-CN10 | Within written approved scope, apply an approved profile through the campus DNS/gateway adapter, verify client-path effects, and restore previous rules. Missing integration remains an acceptance gap. |
| OR01 | US-OR01 | TC-OR01 | Record Wi-Fi 6-or-better equipment model/capabilities and staged load results for the intended client density; brochure client count alone is insufficient. |
| OR02 | US-OR02 | TC-OR02 | Configure the intended classroom SSID/password; two student laptops associate and obtain local connectivity without changing per-class infrastructure rules. |
| OR03 | US-OR03 | TC-OR03 | Inspect negotiated Wi-Fi security on the supported clients: WPA2-AES or compatible WPA3 as agreed; record any incompatible devices and resolution. |
| OR04 | US-OR04 | TC-OR04 | DHCP pool/lease configuration supports at least 150 students plus inventoried support devices; test lease assignment and no duplicate allocations using declared physical/simulated conditions. |
| OR05 | US-OR05 | TC-OR05 | Reboot router/server; the configured stable server address/local name still leads students to the intended application and media endpoint. |
| OR06 | US-OR06 | TC-OR06 | Use and record a negotiated Gigabit-or-faster wired server link where possible; if unavailable, record the exception and measured capacity impact for acceptance. |
| OR07 | US-OR07 | TC-OR07 | With intended isolation enabled/configured, two student clients still reach the server, media and approved enforcement paths; document permitted connectivity. |
| OR08 | US-OR08 | TC-OR08 | Test increasing client loads, measure bottlenecks and choose AP count/placement that meets agreed AT02/AT03; repeat after relevant configuration changes. |
| OR09 | US-OR09 | TC-OR09 | Demonstrate adding the supported AP/switch arrangement without address conflicts or loss of class reachability; preserve a topology/configuration record. |
| OR10 | US-OR10 | TC-OR10 | Inventory required power supplies, cables/adapters and transport protection; perform one full setup and power/restart recovery using the portable kit. |
| OR11 | US-OR11 | TC-OR11 | With WAN physically disconnected and local dependencies provisioned, start a fresh class and receive screen/supported audio on two laptops; apply/restore rules against controlled local test domains. |
| OR12 | US-OR12 | TC-OR12 | Apply and restore two class profiles through the supported software adapter with no manual router rule edits between classes; unsupported automation is visibly reported as a gap. |

## 3. Admission edge cases

| Admission test | Proposed pass/fail check | References |
|---|---|---|
| TC-ADM01 | Code admission: valid active code plus available capacity admits; invalid/expired/closed code is rejected | S02, TC-S02, F05 |
| TC-ADM02 | Code + approval: valid code creates pending request with no viewing grant; owning Teacher approval admits only after final checks | T06, TC-T06, F05 |
| TC-ADM03 | Owning Teacher rejection prevents viewing; pending/cancelled/timed-out requests do not obtain media access | T06, TC-T06; timeout policy pending D02 |
| TC-ADM04 | Student, unrelated Teacher, or unscoped administrator cannot approve a request; denied attempt does not change its pending state | NAC16, TC-AUTH, F05/F08 |
| TC-ADM05 | While approval waits, end class / expire code / add block / fill capacity in separate trials; subsequent approval does not bypass final eligibility checks | T06, S02, TC-AUTH |
| TC-ADM06 | Two simultaneous requests compete for the final seat; at most one receives admission/media access under the agreed capacity rule | Classroom limits, S02, TC-S02 |
| TC-ADM07 | A missing join code is rejected in either mode; selecting approval mode does not create a code-free endpoint | S02, TC-S02 |

## 4. Architectural cases

| Criterion/test | Proposed acceptance |
|---|---|
| AC-AUTH / TC-AUTH | Matrix allow/deny and cross-class/scope tests pass; stale/forged/revoked room grants fail; role removal affects new privileged requests; no permission is inferred only from visible UI |
| AC-LOCAL / TC-LOCAL | AT07 confirms local app, API, signaling, SFU, policy storage and required filtering service operation without cloud/CDN runtime dependence |
| AC-SFU / TC-SFU | Documented transport path shows teacher publication to local SFU and per-viewer subscriptions; actual negotiated streams/bitrates and load are recorded |
| AC-RECOVERY / TC-RECOVERY | Execute isolated scenarios TC-FAIL01–TC-FAIL08; health distinguishes network, application, media, trust/name and enforcement faults; unfinished temporary policy operations resume safely; backup/database/config restoration drill documented |
| AC-PRIVACY / TC-PRIVACY | Server secrets absent from clients/exports/logs; retained participant/audit data matches approved minimal collection and deletion rules |

## 5. Isolated failure scenarios



**Offline means WAN unavailable while the required local network, server/services, local naming and trusted access remain operational.** It does not promise uninterrupted broadcasting when Wi-Fi, the server or the SFU fails. Isolate each fault below on an authorized test setup; keep the other dependencies available where the topology permits. If services share a host/process/resolver, document the coupled failure rather than calling it an independent test.

Before every trial, record build/configuration, network mode, topology, physical/simulated client counts, browser/OS, capture source, active profile, current admission and enforcement states. Capture the healthy baseline, fault start, detected outcome, recovery action, retest and final policy state. Restore the test environment before the next case. Repeat applicable cases for both campus and portable modes; campus faults require the authorized operator/test scope.

| Scenario / test | Controlled fault and retained dependencies | Expected behavior during fault | Recovery and observable final state | Requirement / workflow references |
|---|---|---|---|---|
| **FS01 / TC-FAIL01 — WAN disconnected** | Disconnect upstream internet only; LAN, application/backend, SFU, local names/trust and required filtering service stay available | Fresh local joining and ongoing screen/supported-audio viewing work under AT07; public websites may fail independently of policy; no cloud runtime dependency is required | Restore WAN; local class remains usable. Use local controlled domains for offline rule checks; use upstream-connected controls separately to prove selective public-domain enforcement | CN09, OR11, NAC18/NAC20; F02/F03/F06/F10/F15 |
| **FS02 / TC-FAIL02 — One student loses Wi-Fi** | Disconnect one viewer for 10 s while teacher, other viewers and local services remain reachable | Affected viewer shows lost/reconnecting status; it receives no new media during the outage; other viewers continue. Network policy does not change merely because one viewer disconnects | Restore Wi-Fi and revalidate admission; AT06 recovery applies only to a still-authorized active class. Also revoke/end while offline and verify no readmission | S06/S07, T05/T06; F08/F12 |
| **FS03 / TC-FAIL03 — Classroom LAN/AP path fails** | Interrupt the class access-point/LAN path in the controlled scope; server may still be powered | Clients on that path cannot be promised broadcast, new joining or live backend status. No successful new policy verification is claimed from stale data; infrastructure recovery is required | Restore path; recheck names/trust, app, media, admission and current policy before reporting recovered. Restoration/verification stays pending until its required paths are reachable | CN02–CN04, OR07, S07; F02/F03/F12/F15 |
| **FS04 / TC-FAIL04 — Application/backend unavailable** | Stop only application/backend service where separable; leave LAN/SFU/enforcement running | New joins, class controls and fresh authorization fail visibly where a client is still loaded. Existing media may continue or stop according to tested SFU/token behavior; do not promise either. Previously applied rules may remain; unreachable control plane must not be described as restored | Authorized operator restores backend; recover durable sessions/leases, reconcile ended/revoked admission and expired policies, and retest. Document any access-revocation/expiry delay; D11 must settle it before release | NAC06/NAC10/NAC13, S07; F12–F15, TC-RECOVERY |
| **FS05 / TC-FAIL05 — SFU unavailable** | Stop/disconnect only media service; application/backend and network controls remain available | App can show class/participant state while media publication/subscription fails. Display media unavailable rather than global service success. Do not reset network rules solely because the SFU failed | Restore SFU, reauthorize/resubscribe current participants and republish only with valid Teacher permission/capture consent where needed. Retain class identity where safely recoverable; report any unsupported recovery | T02–T05, S03/S04/S07; F05/F06/F12/F15 |
| **FS06 / TC-FAIL06 — Local name resolution fails** | Make required local hostname resolution unavailable without bypassing security; note if DNS filtering shares the fault | Fresh clients may fail before the page loads; existing cached connections may behave differently. Operator instructions identify naming failure; do not assume the app can display its own error page when unreachable | Authorized operator repairs local DNS/name configuration; verify the original trusted hostname, signaling/media and enforcement paths. A raw IP is not a passing substitute unless its secure access was explicitly provisioned | CN01/CN02, OR05, secure-context obligation; F02/F03/F15 |
| **FS07 / TC-FAIL07 — HTTPS trust/certificate fails** | On an isolated test endpoint/client, present expired, untrusted or hostname-mismatched certificate; keep network reachable | Browser may block the app/WSS/capture. Do not tell users to bypass certificate checks and count that as success; use browser/endpoint evidence when app UI cannot load | Repair certificate, hostname, clock or trust provisioning as appropriate; fresh clients access original intended endpoints without warnings and can capture/connect. Do not rely on online renewal during an offline class | Secure-context obligation, CN01/CN09, OR05/OR11; F02/F03/F06/F15; D10 |
| **FS08 / TC-FAIL08 — Enforcement API or filtering service unavailable** | Test adapter management-API loss separately from resolver/gateway failure where possible; app/SFU retained | Report last verified time and current unverified/degraded/pending state. Management-API loss may leave old rules effective; resolver failure may also break naming/public access. Neither proves policy disabled/restored. Preserve local access according to tested topology; expose dependencies honestly | Restore service/path; read back rules, reconcile outstanding apply/expiry/restore tasks and verify affected-client controls. Ending the class still closes app/media access when those services are reachable; network restoration may remain unresolved | NAC01/NAC06/NAC10/NAC12/NAC13/NAC18, CN10/OR12; F10/F13/F14/F15 |

**Fault classification:** FS01 tests the required offline capability. FS02–FS08 test failure detection, truthful state and recovery; they do not introduce a guarantee of uninterrupted playback through failed infrastructure. Numeric detection/recovery limits remain proposed AT targets and D11/D12 decisions. All eight results = **Not run**; requirement approval and client acceptance remain separate.

**Additional cross-cutting acceptance:** AC-FAILURES / TC-FAIL01–TC-FAIL08 requires the isolated fault, expected visible/operational state, recovery evidence and final policy/admission state to be recorded. Use existing CC-002/CC-017 for setup, CC-009 for viewer recovery and CC-020 for integrated fault/recovery checks; add component evidence to CC-005/CC-008/CC-012/CC-015 as relevant. These tests supplement the 63 original requirement test specifications rather than replacing or renumbering them.

## 6. Supplemental workflow race cases — proposed

| Case | Steps / expected result | Trace |
|---|---|---|
| TC-CTRL01 | Start F07 action, then start F13 before SFU reply; late result must not reactivate publication | US-T02; F07/F13 |
| TC-CTRL02 | Repeat same operation ID/intent after completion; return recorded result without second mutation; different intent with same ID is denied | US-T02/US-T06; F07/F08 |
| TC-CTRL03 | Resume after browser source ends; show new capture required and use F06 explicit consent | US-T02/US-T03; F07/F06 |
| TC-CTRL04 | Remove participant while SFU is unreachable; revoke app grants, record media cleanup unresolved and schedule F15 | US-T06; F08/F15 |
| TC-CLOSE01 | Close media successfully while network restore fails; result is Class ended, restoration pending/failed | US-NAC06; F13 |
| TC-CLOSE02 | Fail media closure while network restore succeeds; result remains Class ending, cleanup unresolved | US-NAC06; F13 |
| TC-CLOSE03 | Repeat completed close; return original outcome; incomplete close resumes only unfinished steps using same operation | US-NAC06; F13 |

## 7. Execution template

| Test | Build/environment | Criteria approval | Actual result | Evidence/defect | Reviewer/date |
|---|---|---|---|---|---|
| To select | To record | Pending | Not run | None | Pending |
