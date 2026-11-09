# Infrastructure and deployment design

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Intended host and missing inventory

Latest user context specifies an existing school server on Ubuntu/Linux. Confirm actual OS/version, CPU, RAM, storage, NIC, virtualization/container permissions, existing workloads, admin contact, maintenance window and backup location. No hardware minimum or successful installation is established here.

## 2. Network modes

| Mode | Preparation | Evidence |
|---|---|---|
| Campus | Approved hostname/address, client trust, server/media paths, isolation, DNS/gateway scope | CN01–CN10; written IT approval and client-path tests |
| Portable | Suitable router/APs, SSID/security, DHCP, stable host, wired uplink where possible, power and local runtime | OR01–OR12; measured setup and WAN-off tests |

Portable inclusion remains in source scope until D18 approves a change. Use the same application with mode-specific configuration; teachers should not edit router rules per class.

## 3. Deployment checklist proposal

1. Confirm authority and inventory; record baseline configuration.
2. Select and pin reviewed component versions after feasibility; document licenses and dependencies.
3. Provision local application, backend, database, SFU, required enforcement integration and trusted endpoints.
4. Preload assets/images/rule lists and necessary name/certificate trust for offline use.
5. Verify app, signaling and actual media paths separately; approved firewall rules depend on chosen configuration.
6. Exercise authorized policy apply/verify/restore in an isolated scope before classroom use.
7. Record restart/recovery, backup and operational ownership; verify a fresh-browser WAN-off class.

These are planned steps, not runnable installation commands. Exact ports, domains, subnets, resource reservations and trust method are **Pending Decision**; no guessed production values are supplied.

## 4. Capacity model

An SFU reduces teacher upload fan-out but server egress still scales with subscriptions. Existing example: 1.5 Mbps per viewer ×150 ≈225 Mbps before overhead. This is arithmetic, not a benchmark or selected quality setting. Measure actual bitrates, CPU/RAM/NIC, AP airtime and physical client behavior; resolve D12 before acceptance.

## 5. Operations

Keep component health separate: LAN/name/trust, app/database, SFU/media, enforcement API and effective rules. A service can be reachable while its desired policy is not effective. Document restart order, configuration restore, safe rollback, certificate renewal and equipment return under named operators before handover.
