# Use-case catalogue

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. System boundary and catalogue

A use case is an actor goal, not a function count or mandatory runtime sequence. Preserve these UC IDs across the board, stories and tests.

| Use case | Primary actor | Goal / activities |
|---|---|---|
| UC01 | Teacher | Create class and publish joining information — F04 |
| UC02 | Student, Teacher for approval | Request and obtain admission — F05 |
| UC03 | Teacher, admitted Student | Publish/receive media and playback controls — F06/F07 |
| UC04 | Teacher | Manage roster and participant access — F08 |
| UC05 | SYS/NET with policy permission | Create/maintain profiles and exceptions — F09 |
| UC06 | SYS/NET or authorized class automation | Apply and verify supported restrictions — F10/F11 |
| UC07 | Student | Recover class connection — F12 |
| UC08 | Teacher and backend automation | End class, revoke access and restore policy — F13 |
| UC09 | SYS/NET or expiry automation | Emergency/expiry recovery — F14 |
| UC10 | Authorized operator | Diagnose/recover local services — F15 |
| UC11 | Teacher, admitted Student | Share/access permitted materials — F16 |
| UC12 | SYS/NET with policy permission | Schedule/import/export/local lists — F17 |
| UC13 | Teacher, Student, scoped policy administrator | Optional participation, history or group policy — F18 |
| UC14 | Authorized campus installer/NET | Prepare and verify campus deployment — F02 |
| UC15 | Authorized portable installer/NET | Prepare and verify portable deployment — F03 |

## 2. Use-case detail convention

For each goal use its linked F workflow for trigger, preconditions, success path, alternate path and final state. Shared preconditions are authorized role/resource scope and required services; exceptions must preserve truthful state. UC02 requires valid code and current eligibility; UC03 requires publisher authority and current subscriber admission; UC06 requires approved network scope; UC08 requires end authority before mutation. UC11–UC13 include lower-priority capabilities and do not silently become Must work.

## 3. Example — UC02 Request and obtain admission

Trigger: student opens local join page. Preconditions: correct network and trusted endpoint; active class. Student enters code and optional agreed identifier. Backend validates code, class, block and capacity; if approval mode applies, wait without viewing rights. Owning teacher decision is reauthorized. Final atomic checks allocate a seat and issue permitted subscription credentials. Pending, rejected, expired, full or revoked requests receive no viewing grant. Postcondition: admitted/waiting or admitted/viewing, or a clear non-admitted result. F05 and TC-S02/TC-ADM01–07 specify acceptance.

## 4. Administration coverage

Account provisioning, role assignment and app settings are supporting proposals in Area 06. Keep them explicit in permissions/design; do not renumber UC01–UC15 to disguise them as source-defined use cases. Their scope needs D01/D14 approval.
