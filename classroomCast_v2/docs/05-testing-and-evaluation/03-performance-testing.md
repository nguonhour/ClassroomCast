# Performance and offline testing

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Source capacity and test conditions

The teacher specifies 50–150 students per classroom and CN06 calls for capacity validation for 150. D12 concerns acceptance test conditions and evidence. Lower-load trials cannot replace testing the source target. Record physical clients and simulated subscribers separately.

## 2. Test protocol proposal

1. Record server CPU/RAM/NIC/storage/OS, AP models/count/placement, SSID/VLAN, client OS/browser, SFU/build and source type.
2. Declare media profile, actual negotiated bitrate/layers, test duration and sampling method.
3. Run two-viewer functional sanity first; stage 50/100/150 subscriber trials under source AT03; lower-load trials are exploratory, not a replacement for the source target.
4. Collect per-viewer playback checks, disconnects, freezes, loss and visible timestamp latency; collect server and network utilization.
5. Repeat with actual physical devices where available. A simulator result is server-load evidence only for its declared workload.
6. Save raw samples and failure logs; stop escalating load if unsafe or unstable, investigate and record the limit.

## 3. Candidate metrics

| Test basis | Proposed setup/target | Approval/evidence rule |
|---|---|---|
| AT01 — Local UI | Fresh browser reaches join page within 5 s on a reachable healthy test LAN; 10 trials per supported browser | Timing starts at navigation and ends when code input is interactive; record cold/cache conditions |
| AT02 — Playback quality | Agreed starting profile 720p/15 fps; source-to-display p95 ≤1 s; report received bitrate, freezes, packet loss and per-client results | Proposed threshold needs D12 approval; measure visible source timestamp at source/viewer in a common recording; separate screen content from encoder adaptation |
| AT03 — Capacity/stability | 50/100/150 concurrent subscribers, 30 min each; per-viewer playback active at ≥98% of declared one-minute checks; no open release-blocking defect | Record physical/simulated counts, AP/SSID/topology, OS/browser, source, bitrate, server CPU/RAM/NIC and samples; simulation does not prove 150-laptop Wi-Fi airtime |
| AT04 — Policy apply | Healthy reachable authorized adapter reports verified outcome within 30 s of class-start/apply event in 10 trials | Must include client-path denied/allowed controls and local app/media access; upstream conditions recorded |
| AT05 — Restoration | Prior policy verified within 30 s of end/emergency/expiry trigger in 10 healthy reachable trials | In unreachable/conflicting-state tests, class still closes; durable pending/failure shown within proposed 5 s of detecting failure; safe retry/operator recovery required |
| AT06 — Reconnect | After a 10 s interruption, same-class playback recovers within 15 s of reachability returning in ≥9/10 attempts | Also test class ended and participant revoked while offline; those clients must not regain access |
| AT07 — Offline | Preprovision runtime assets/images, names/cert trust and lists; disconnect WAN and open fresh browser | External public-site failure is not evidence of selective blocking; use controlled local domains for offline rule checks |

## 4. Interpretation

For latency report sample count, percentile calculation, synchronization/measurement method and outliers. For active-playback rate use successful checks divided by scheduled declared checks per viewer; disclose missing observations rather than silently excluding them. Show quality against each load stage, not only a team-wide average that hides failing viewers.

## 5. Report template

Build: ___ · Mode/topology: ___ · Target approved by: ___ · Actual devices/simulators: ___ · Duration: ___ · Profile/bitrate: ___ · Metrics/raw evidence: ___ · Bottleneck: ___ · Limits: ___ · Result/next action: ___

No performance, scale or offline pass is asserted by this document.
