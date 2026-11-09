# Product backlog

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Epics and estimate policy

Epics correspond to the six product areas. CC-001/018/021/022 also cover cross-cutting discovery, acceptance and handover. Existing CC IDs and source order are preserved. Each CC item is a broad delivery slice to split before commitment; proposed story points below are discussion seeds, not team estimates or a forecast. Do not total these points with per-requirement story sizes.

## 2. Ordered delivery backlog

| CC ID | Delivery slice | Priority | Proposed SP | Sprint candidate | Lead proposed | Source requirements |
|---|---|---|---|---|---|---|
| CC-001 | Confirm scope capacity hardware and network authorization | Must | 3 | 1 | HENG NGUON HOUR | Project constraints |
| CC-002 | Provision local application SFU and trusted HTTPS | Must | 8 | 1 | CHANTHA MENGKONG | CN01 CN02 CN03 CN04 CN05 CN07 CN08 CN09 OR02 OR03 OR04 OR05 OR06 OR07 OR10 OR11 |
| CC-003 | Create class and validate admission credentials | Must | 5 | 1 | BUN SENGLEANG | T01 T08 S01 S02 |
| CC-004 | Build teacher start screen with joining information | Must | 3 | 1 | HAK SENGKEA | T01 T08 |
| CC-005 | Publish and subscribe through local SFU | Must | 8 | 1 | HONG DYHENGMESA | T03 S03 |
| CC-006 | Build student join and basic playback UI | Must | 5 | 1 | HENG NGUON HOUR | S01 S02 S03 S07 |
| CC-007 | Authorize classroom controls and participant actions | Must | 8 | 2 | BUN SENGLEANG | T05 T06 NAC16 |
| CC-008 | Add screen audio microphone and broadcast controls | Must | 5 | 2 | HONG DYHENGMESA | T02 T03 T04 T07 |
| CC-009 | Add student fullscreen volume and reconnect | Must | 5 | 2 | HENG NGUON HOUR | S04 S05 S06 S07 |
| CC-010 | Integrate teacher roster and sharing controls | Must | 5 | 2 | HAK SENGKEA | T02 T05 T06 T07 |
| CC-011 | Store and validate profiles categories rules and exceptions | Must | 8 | 3 | HONG DYHENGMESA | NAC02 NAC03 NAC04 NAC07 NAC08 NAC18 |
| CC-012 | Implement authorized enforcement adapter | Must | 8 | 3 | CHANTHA MENGKONG | NAC01 NAC10 NAC17 CN10 OR12 |
| CC-013 | Build policy editor and actual enforcement status | Must | 5 | 3 | HAK SENGKEA | NAC01 NAC02 NAC03 NAC04 NAC07 NAC08 NAC10 |
| CC-014 | Apply policies on class lifecycle with audit | Must | 8 | 3 | HONG DYHENGMESA | NAC05 NAC06 NAC11 NAC16 NAC19 |
| CC-015 | Implement durable expiry emergency restoration and recovery | Must | 8 | 4 | CHANTHA MENGKONG | NAC06 NAC12 NAC13 NAC18 |
| CC-016 | Verify policy effects and permission failures | Must | 5 | 4 | HENG NGUON HOUR | NAC01 NAC02 NAC03 NAC04 NAC05 NAC06 NAC08 NAC10 NAC11 NAC12 NAC13 NAC16 NAC17 NAC18 NAC19 |
| CC-017 | Validate both deployment modes and offline runtime | Must | 8 | 4 | CHANTHA MENGKONG | CN01 CN02 CN03 CN04 CN05 CN07 CN08 CN09 CN10 OR02 OR03 OR04 OR05 OR06 OR07 OR10 OR11 OR12 |
| CC-018 | Complete Must traceability and acceptance gap review | Must | 5 | 4 | HENG NGUON HOUR | T01 T02 T03 T04 T05 T06 T07 T08 S01 S02 S03 S04 S05 S06 S07 NAC01 NAC02 NAC03 NAC04 NAC05 NAC06 NAC07 NAC08 NAC10 NAC11 NAC12 NAC13 NAC16 NAC17 NAC18 NAC19 |
| CC-019 | Measure 50 and 150 subscriber capacity | Must | 8 | 5 | CHANTHA MENGKONG | CN06 OR01 OR08 OR09 |
| CC-020 | Run security offline rollback and restore drills | Must | 8 | 5 | HENG NGUON HOUR | NAC06 NAC10 NAC12 NAC13 NAC16 NAC17 NAC18 NAC19 CN09 OR11 |
| CC-021 | Run physical pilot and obtain acceptance decisions | Must | 5 | 6 | HENG NGUON HOUR | Release acceptance |
| CC-022 | Finish guides demonstration and submission | Must | 5 | 6 | HENG NGUON HOUR | Project handover |
| CC-023 | Add health diagnostics and reusable offline category maintenance | Should | 5 | After Must forecast | HONG DYHENGMESA | T09 NAC20 |
| CC-024 | Add schedules and policy import export | Should | 8 | After Must forecast | HONG DYHENGMESA | NAC09 NAC14 |
| CC-025 | Add permitted materials and optional student identifiers | Should | 8 | After Must forecast | HENG NGUON HOUR | T10 S08 S09 |
| CC-026 | Explore history participation tools and per-group policies | Could | 8 | Future release | HENG NGUON HOUR | T11 S10 NAC15 |

## 3. Acceptance and dependencies

| CC ID | Acceptance from existing backlog | Dependency |
|---|---|---|
| CC-001 | Roster roles and actual calendars recorded; hardware inventory and campus integration decision path recorded | Scope and feasible authorized environment |
| CC-002 | Two laptops reach trusted app and media endpoints; installation dependencies are listed | Scope and feasible authorized environment |
| CC-003 | Teacher creates session; active join code is unique; invalid and expired codes fail | Scope and feasible authorized environment |
| CC-004 | Teacher displays working local URL QR and join code | Scope and feasible authorized environment |
| CC-005 | Teacher-selected screen is visible on two browser viewers using local SFU | Scope and feasible authorized environment |
| CC-006 | Student joins valid class and sees playback or a useful connection error | Scope and feasible authorized environment |
| CC-007 | Teacher sees roster and admits rejects removes or blocks; unauthorized control and blocked rejoin fail | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-008 | Start stop pause resume and media settings pass supported-browser checks; audio source limitations recorded | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-009 | Playback controls work; interrupted connection recovers under agreed criterion; ended class remains closed | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-010 | UI reflects actual session state and results of authorized controls | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-011 | Versioned profiles cover both default modes and exceptions; protected local services remain reachable | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-012 | Adapter applies versioned rules and reads back state; credentials stay server-side; unsupported scope is explicit | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-013 | Administrator can configure profile and distinguish saved desired applying verified degraded and failed states | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-014 | Authorized class start/end invokes scope lease and restoration; audit excludes unnecessary browsing history | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-015 | End expiry emergency action and restart restore safely; conflicts and unreachable adapters stay visibly unresolved | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-016 | Client-path probes confirm block allow and local access; failure and bypass limitations are documented | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-017 | Same build works with mode-specific config; campus authorization recorded; new browser session works without WAN | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-018 | Each Must has an evidence case and named reviewer; missing or failing criteria remain open | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-019 | Report physical and simulated counts separately; bitrate loss delay CPU NIC and AP conditions recorded; unresolved capacity gap escalated | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-020 | Role failures service restarts external-rule conflicts WAN outage and backup restoration have recorded results | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-021 | Pilot device count results feedback and lecturer decisions recorded; open blockers resolved or explicit scope decision obtained | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-022 | Source/demo links build version runbooks acceptance evidence and operator handover ready by 22 Jan | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-023 | Dashboard shows useful metrics; versioned local lists can be refreshed before offline classes | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-024 | Schedules survive restart and timezone checks; exports exclude secrets and imports validate rules | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-025 | Allowed files and identifiers follow session permissions and retention rules | Relevant earlier classroom, media or policy slice plus current decisions |
| CC-026 | Each feature is separately refined and depends on demonstrated capacity and supported enforcement scope | Relevant earlier classroom, media or policy slice plus current decisions |

## 4. Backlog status and sources

Every item is Proposed / implementation Not assessed. Original WBS and CSV remain [BACKLOG.csv](../../../classroomcast_v1/BACKLOG.csv) and [PROJECT-PLAN.md](../../../classroomcast_v1/PROJECT-PLAN.md). See [stories](03-user-stories.md) and [traceability](../traceability.md) for detailed acceptance links. A delivery item can cover several requirements; test coverage is not proof of implementation.
