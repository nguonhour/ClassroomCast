# Feedback and decision log

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Existing decision register

All inherited decisions remain Pending. D08's prior audio-pause suggestion is one candidate. D12 must define test conditions for the teacher-specified 50–150 students; the source capacity itself is not a competing-target decision.

| ID | Decision | Proposed position / question to resolve | Accountable decision owner | Due point | Status | Affected behavior |
|---|---|---|---|---|---|---|
| D01 | Account provisioning and multiple roles | SYS + Teacher/Student/NET roles combine only when explicitly assigned; no inherited network scope | Client/supervisor + System Administrator | Before RBAC implementation | Pending | Four-role allocation and account provisioning |
| D02 | Which code-required admission modes are supported/default? | Propose Code admission and Code + teacher approval; both require S02 code entry. Agree default, timeout/cancellation, code expiry and seat reservation. Approval-only without a code requires an explicit scope decision | Client/supervisor + pilot teacher | Before admission implementation | Pending | F05, TC-S02 and TC-ADM01–TC-ADM07 |
| D03 | Student identity and block duration | Choose session identity strength, name/ID use, blocking persistence and honest limitations | Client/supervisor + pilot teacher | Before join/removal implementation | Pending | S08, T06 and reconnect guarantees |
| D04 | What event starts the class policy? | Explicit class Start event, distinct from Create class and Start sharing | Client/supervisor + NET | Before class/policy integration | Pending | NAC05 automation trigger |
| D05 | Continue if enforcement fails? | Normal lesson may allow explicit authorized override; exam may require stopping; choose who decides | Client/supervisor + NET + pilot teacher | Before enforcement demo | Pending | F01 and exam failure behavior |
| D06 | Network scope and simultaneous classes | One active policy lease per approved scope initially; reject conflicts | NET / campus IT + client | Before adapter implementation | Pending | Scope isolation and safe rollback |
| D07 | Default modes, exceptions and subdomains | Specify precedence and adapter-supported domain matching using a declared test set | NET + backend team; client confirms intent | Before policy evaluator tests | Pending | NAC03, NAC04 and NAC08 results |
| D08 | Pause and media-quality semantics | Explicit paused indicator; pause audio too; disclose capture restart/adaptation limitations | Pilot teacher + media team | Before broadcast-control acceptance | Pending | T02/T07 and microphone expectations |
| D09 | Supported OS/browser/source combinations | Publish screen, tab/system audio and microphone compatibility matrix after spike | Media team + client/supervisor | Before media release criteria approved | Pending | T03/T04/S04 tests |
| D10 | Local names, HTTPS trust and renewal | Preprovision trusted endpoints and document offline operation and renewal owner | NET / campus IT + deployment team | Before two-laptop feasibility test | Pending | Secure capture and local connectivity |
| D11 | Disconnect, expiry, retries and missed schedules | Durable expiry/recovery; decide teacher-offline grace period, retry limits and missed-run policy | NET + backend team + client | Before recovery implementation | Pending | NAC06/NAC09/NAC13 and pending states |
| D12 | Capacity and measurable acceptance conditions | Keep supplied 50–150 target; agree physical/simulated evidence and AT01–AT06 numeric proposals | Client/supervisor + NET + test team | Before load-test/acceptance baseline | Pending | CN06/OR capacity, performance and recovery thresholds |
| D13 | Minimal logging, identifiers and retention | Agree fields, access and deletion; minimize raw browsing history | Client/data owner + SYS + NET | Before pilot data collection | Pending | NAC19 and audit/privacy tests |
| D14 | System-administrator recovery and role assignment | Audit role grants, protect last recoverable SYS account, define out-of-band recovery | Client/supervisor + SYS + NET | Before account administration release | Pending | Operational access and privilege governance |
| D15 | Who may approve/apply/restore policy scopes? | SYS edits assigned profiles; NET approves scope; manual apply/restore only with explicit scoped permission | Client/supervisor + network authority | Before policy permissions baseline | Pending | Role-permission matrix and NAC16 |
| D16 | Materials sharing behavior and limits | Define supported presentation/file formats, size, local storage and download controls | Pilot teacher + frontend/backend team | Before T10/S09 commitment | Pending | F16 Should acceptance |
| D17 | Optional participation, history and targeting scope | Choose actual S10 interactions, retained T11 summaries and supported NAC15 scope; confirm W01–W05 | Client/supervisor + pilot teacher + NET | Before extended-scope commitment | Pending | F18 and proposed exclusions |

## 2. New review questions from the latest request

| ID | Decision | Proposed owner / authority | Due gate | Status |
|---|---|---|---|---|
| D18 | Is school Ubuntu server the only deployment, or must portable mode still be delivered? Confirm inventory, access and authorized network scope | Teacher/client + campus IT; Mengkong coordinates | Scope and feasibility gate | Needs Teacher Approval |
| D19 | Confirm or revise previously proposed stack after compatibility/licensing/operational checks; no new stack selected here | Team + infrastructure owner; teacher reviews material impact | Before architecture baseline | Pending Decision |
| D20 | What has actually been completed since Nov 2, and what are remaining personal hours, pilot resources and revised commitments? | All Developers + Hour; teacher approves baseline changes | Next planning meeting | Pending Decision |

## 3. Conflict decisions requiring explicit disposition

C01/D12: The teacher source specifies **50–150 students**. The previously introduced lower range was unsupported and has been withdrawn. D12 remains pending only for test methods, physical versus simulated evidence, media profile, duration and quality thresholds.

C02/D18: school-server context does not automatically remove portable obligations. C03: separate class/publication/policy state dimensions as proposed clarification; confirm with implementation team. See [source review](../sources/review-and-conflicts.md).

## 4. Decision and change record template

Decision ID: ___ · Date: ___ · Question: ___ · Options/evidence: ___ · Chosen wording: ___ · Authority: ___ · Conditions: ___ · Affected requirement/story/test/flow IDs: ___ · Effort/schedule/risk impact: ___ · Approval evidence: ___ · Follow-up owner/due date: ___

## 5. Feedback register template

| Date | Reviewer/role | Artifact/version | Feedback | Action/owner | Decision link | Status |
|---|---|---|---|---|---|---|
| To complete | | | | | | Pending |

Do not change Pending to Confirmed/Approved without evidence. Confirmed source wording is not the same as teacher acceptance.

## 6. D21 - Latest course-site schedule and cutoff reconciliation

**Opened:** 9 November 2026. **Status:** Pending teacher confirmation. Latest user-provided screenshots show preparation November 10-17, design November 18-27, three development sprints November 30-January 13, release January 27 and presentation February 3. Confirm the superseding baseline, working-day/timebox assumptions, actual team capacity and whether the earlier January 25 23:59 description/code/demo edit cutoff requires separate earlier delivery. No approval or deadline extension is implied. HENG NGUON HOUR coordinates; teacher/course authority confirms dates; all members confirm allocations. See [meeting package](../meeting-2026-11-10/README.md). D20 must now reconcile the older November 2 start with the latest site snapshot rather than assume work occurred.
