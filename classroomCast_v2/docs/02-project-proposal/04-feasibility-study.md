# Feasibility study

> **9 November planning update:** Latest user-provided site screenshots show three development sprints starting November 30, different task allocations, and release/presentation dates through February 3. Earlier dates/allocations below are historical proposals, not the current meeting commitment. Use the [November 10 meeting package](../meeting-2026-11-10/README.md) to review the new baseline and January 25 editing-cutoff question. Approval remains pending.

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Current conclusion

Feasibility is **unproven**. The architecture is a plausible proposal based on local services and reuse, but no delivered benchmarks or approved campus integration establish success.

## 2. Feasibility experiments

| Spike | Setup and procedure | Pass evidence | Failure response / owner |
|---|---|---|---|
| SP01 trusted offline access | Provision approved name/cert; fresh browsers on two laptops; remove WAN | Capture and app/media connections without trust bypass | Resolve trust with NET; Mengkong |
| SP02 SFU publication | One teacher, two viewers; screen and supported audio; zero-viewer start | Authorized publish/subscribe and observed media; supported matrix | Check transport/source compatibility; Dyhengmesa |
| SP03 enforcement | Isolated authorized scope; preserve baseline; apply test profile | Read-back plus denied/allowed/local-path controls; prior policy restored | Unsupported scope stays unavailable; Mengkong/Mesa |
| SP04 resilience | Interrupt backend/SFU/enforcement independently; replay pending operation | Truthful separate status, no stale admission or unsafe restore | Open defects and recovery decision; Sengleang/Hour |
| SP05 staged capacity | Document hardware/APs; increase subscriptions and physical clients | Resource/quality results at each agreed stage | Resolve D12 or equipment need; Mengkong |

## 3. Operational and schedule feasibility

Confirm server access, Ubuntu version, resources, existing workloads, network owner, maintenance windows and pilot devices. Permission to host does not authorize DNS/firewall modification. Six-sprint dates are inherited planning dates; November 9 reforecast is required. Scope/hours cannot be validated from diagram completion alone.

## 4. Economic feasibility

Reuse existing proposed SFU/filtering components and inventory borrowed resources first. Costs and licenses for selected versions must be checked before adoption. Record quotes only if procurement is needed; do not present unknown expenses as zero. The 480-hour planning envelope is effort, not a monetary budget.

## 5. Gate result template

For each spike record hypothesis, authorization, configuration, observations, pass/fail against agreed criteria, limitations, decision and reviewer. All five spikes are **Not run in this package**. Proceed with full implementation commitments only after the relevant dependency is evidenced or explicitly accepted as a risk.
