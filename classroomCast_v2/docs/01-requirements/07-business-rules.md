# Business rules

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Proposed rules derived from existing requirements and reviewed workflows

| Rule | Required behavior / proposed mechanism | References |
|---|---|---|
| BR01 | Authorization checks action, class ownership, network scope and current state; default deny | NAC16, TC-AUTH |
| BR02 | Join code required; a valid code does not imply admission, identity or media grant | S02, D02/D03 |
| BR03 | Final admission and seat allocation are atomic; recheck pending state, block, code, capacity and class state | F05/F08, TC-ADM05/06 |
| BR04 | Publishing may start with zero viewers; current admitted viewers alone receive media | F06, S03 |
| BR05 | Pause/stop sharing does not end a classroom or revoke student admission | T02, F07 |
| BR06 | Operation IDs bind requester, class, target/publication and action; same completed request returns recorded outcome; unfinished requests resume remaining work | F07/F08/F13 |
| BR07 | Recheck authorization/state and publication version before SFU mutation and when responses arrive; stale responses cannot revive closed or replaced publications | F07/F12/F13 |
| BR08 | Remove/block revoke grants and prevent refresh; verify actual media denial separately; unknown cleanup schedules recovery | T06, F08/F15 |
| BR09 | Saved profile, accepted apply request and verified enforcement are separate states | NAC07/NAC10, F09/F10 |
| BR10 | Preserve prior policy and operation record before changes; restore only owned changes and reconcile conflicts | NAC06/NAC12/NAC13 |
| BR11 | A class is ended only when admission/grant closure and media termination or effective denial are verified; policy restoration is a separate result | F13 |
| BR12 | Expiry survives browser close and backend restart; unreachable services produce persistent unresolved status | F14/F15, D11 |
| BR13 | Local classroom paths remain protected; domain filtering does not imply universal device control | NAC18, F11 |
| BR14 | Evidence distinguishes configured/requested from observed/verified state | NAC10; all recovery flows |

## 2. Proposed state dimensions

| Dimension | Candidate states | Important distinction |
|---|---|---|
| Classroom | Created, Open, Ending, Ended | Paused media does not close class |
| Participant | Pending, Admitted, Rejected, Removed, Blocked | Connection loss is not removal |
| Publication | Not publishing, Publishing, Broadcasting, Paused, Stopping, Stopped, Unresolved | New capture after source ends requires browser consent via F06 |
| Policy operation | Not applied, Applying, Verified, Degraded, Restoring, Restored, Unresolved | Record scope, version, evidence and time |

These names are design proposals, not established database enums. Each transition needs validation, durable outcome and appropriate notification. Final D08/D11 choices can refine them.

## 3. Closure outcome selection

First check application/media closure. If unverified: **Class ending — cleanup unresolved**, regardless of policy result. If verified: report **Class ended** plus restoration **not required**, **verified**, or **pending/failed**. Never label an unknown restore as not required. An unauthorized end request leaves class and publication unchanged.
