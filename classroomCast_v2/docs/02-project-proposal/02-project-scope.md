# Project scope

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Release scope

Retain all supplied Must capabilities, the individually unlabeled campus/portable obligations and shared architectural requirements. Source scope includes local screen/audio broadcasting, class admission and control, policy administration/apply/verification/restoration, offline operation, diagnostics and authorized network setup. The teacher-specified capacity is 50–150 students. D12 concerns test conditions and evidence.

## 2. Demonstrable MVP versus full release

An early feasibility increment is one teacher and two laptops using trusted local access, valid joining and SFU playback, plus a separate authorized policy apply/restore spike. It is an early demonstration, not acceptance of the full required release. The second gate integrates permissions, supported audio, reconnection, policy state and safe recovery. Scaling and both modes must later be measured or explicitly changed through approval.

## 3. Lower-priority work

Should: richer diagnostics, materials, optional identification/downloads, scheduling/import-export/local list maintenance. Could: history, participation and supported group targeting. Global offline obligations remain required even though extra list-management convenience has a Should label. Optional features still require authorization and tests if delivered.

## 4. Proposed exclusions — needs agreement

| ID | Proposed exclusion | Boundary |
|---|---|---|
| W01 | Custom SFU implementation | Reuse a tested local SFU and integrate its controls |
| W02 | Mandatory native student app | Preserve browser-only participation |
| W03 | Recording/archive of classroom video | History summaries do not imply recordings |
| W04 | LMS/ERP integration | No integration requirement supplied |
| W05 | Remote control or capture of student screens | Roster monitoring concerns participation/connectivity |

## 5. Change control

For every requested scope change record source IDs, new wording, justification, dependency, affected tests, hours/cash/schedule impact and approving authority. Do not remove Must requirements merely to fit a sprint. See [decision log](../07-teacher-review/03-feedback-and-decision-log.md).
