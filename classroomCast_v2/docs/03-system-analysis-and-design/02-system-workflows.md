# System workflows F01–F18

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Diagram authority and reading order

These are compact **proposed process overviews**, not executable code or proof that every concurrency path has been implemented. The original detailed Mermaid remains in [REQUIREMENTS-AND-ACTIVITIES.md](../../../classroomcast_v1/REQUIREMENTS-AND-ACTIVITIES.md) and the corrected F01 source in [board/row-3/F01-CLASSROOM-LIFECYCLE.mmd](../../../classroomcast_v1/board/row-3/F01-CLASSROOM-LIFECYCLE.mmd). The business rules in this package capture the later reviewed separation of authorization, stale operations, closure and restoration. Do not reproduce a generated image as an exact rendering unless generated from the checked code.

Suggested board review order: F01 → F05 → F06 → F10 → F13 → F08 → F07 → F12 → F15 → F14, then F04/F09/F11, deployment F02/F03 and selected F16–F18. This is a documentation review order, **not** mandatory runtime execution.

Green = Must; yellow = Should; gray = Could; red = proposed Won't; white = context/decision. CN/OR steps use proposed Must* classification. Exceptions remain mandatory when an optional capability is selected.


## 2. F01 — Entire classroom lifecycle

**Trigger / actor:** Prepared classroom; operator and teacher.  
**References:** F04/F05/F06/F08/F10/F13; D05.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Check local readiness"]
 N1["Create class F04"]
 N2["Authorize start"]
 N3["Evaluate approved policy using F10"]
 N4["Open class with actual policy status"]
 N5["Handle joining broadcasting and roster events"]
 N6["Authorize end and execute F13"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> N6
 N6 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5,N6 capability;
```

**Exception and recovery:** Unverified restrictions require the D05 agreed rule; aborted startup restores owned changes. Individual rejected joins do not end class.

**Postcondition / next action:** Class ended only after access/media closure verified; restoration is separate; F15 handles unresolved cleanup.


## 3. F02 — Prepare campus deployment

**Trigger / actor:** Authorized campus installer; before class.  
**References:** CN01–CN10; D10/D12/D18.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Confirm IT authorization"]
 N1["Inventory server network and trust"]
 N2["Provision approved endpoints and media paths"]
 N3["Test joining media offline operation and enforcement scope"]
 N4["Record campus readiness"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4 capability;
```

**Exception and recovery:** Missing permission, trust or media reachability prevents readiness; fix and retest.

**Postcondition / next action:** Prepared campus environment for F01; retain measured capacity and unverified integration gaps.


## 4. F03 — Prepare portable deployment

**Trigger / actor:** Authorized portable installer; before class.  
**References:** OR01–OR12; D12/D18.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Inventory kit and scope"]
 N1["Configure SSID security DHCP and stable server name"]
 N2["Provision local services and trust"]
 N3["Test isolation media policy and WAN disconnected operation"]
 N4["Measure capacity and record readiness"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4 capability;
```

**Exception and recovery:** Insufficient AP capacity or unsupported adapter stays a documented gap; no per-class manual router-edit workaround counted as automation.

**Postcondition / next action:** Prepared portable environment for F01; equipment and recovery record retained.


## 5. F04 — Create classroom

**Trigger / actor:** Teacher requests new classroom.  
**References:** T01/T08; D04.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Authenticate teacher"]
 N1["Create unique session and active join code"]
 N2["Display local URL QR and code"]
 N3["Await explicit Start class event"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3 capability;
```

**Exception and recovery:** Unauthorized request creates no class; conflicting active code is regenerated safely.

**Postcondition / next action:** Created class; policy application and screen capture have not automatically happened.


## 6. F05 — Student joining and admission

**Trigger / actor:** Student opens local URL on classroom network.  
**References:** S01/S02/S07/T05/T06; D02/D03.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Enter required code and optional agreed identifier"]
 N1["Validate class code block and capacity"]
 N2["Apply agreed admission mode"]
 N3["Reauthorize teacher decision if required"]
 N4["Atomically recheck and allocate seat"]
 N5["Issue current subscriber grant"]
 N6["Receive available media or wait"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> N6
 N6 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5,N6 capability;
```

**Exception and recovery:** Pending/rejected/full/closed requests have no viewing grant. Recheck capacity at commit; rejected unauthorized teacher action does not reject the student.

**Postcondition / next action:** Admitted waiting or viewing; F12 reconnects, F08 manages access, F13 ends class.


## 7. F06 — Start screen and audio broadcasting

**Trigger / actor:** Authorized teacher starts or retries publication.  
**References:** T02/T03/T04/T07/S03/S04; D09.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Select supported source and request browser consent"]
 N1["Obtain selected tracks"]
 N2["Validate teacher class and publishing authority"]
 N3["Issue scoped publication grant"]
 N4["SFU validates and accepts publication"]
 N5["Record actual media availability"]
 N6["Notify admitted viewers"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> N6
 N6 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5,N6 capability;
```

**Exception and recovery:** Capture refusal produces no publication. Missing optional mic must not be reported as captured. Service/authorization failure stays not publishing; release captured tracks when denied.

**Postcondition / next action:** Broadcast available even with zero viewers; F07 controls publication; F13 closes class.


## 8. F07 — Pause resume and stop broadcasting

**Trigger / actor:** Teacher controls current publication.  
**References:** T02/T07/S03/S04/S05; D08.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Authorize action and check class state"]
 N1["Bind operation ID to requester class publication and action"]
 N2["Return recorded result or resume unfinished work"]
 N3["Validate current publication before SFU mutation"]
 N4["Apply selected pause resume or stop"]
 N5["Recheck operation version on response"]
 N6["Record confirmed or unresolved state"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> N6
 N6 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5,N6 capability;
```

**Exception and recovery:** Closure takes precedence via F13; stale publication response cannot mutate new stream. Resume with ended capture goes to F06; failures route F12/F15.

**Postcondition / next action:** Pause/resume/stop leave admission intact. Stop ends publication, not class. D08 pause/audio semantics remain pending.


## 9. F08 — Participant management

**Trigger / actor:** Teacher opens roster and selects an action.  
**References:** T05/T06; D02/D03.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Authorize roster access"]
 N1["Reauthorize modifying action and bind operation identity"]
 N2["Validate target and current request state"]
 N3["Atomically approve or reject pending request or revoke removed blocked access"]
 N4["For removal or block terminate target subscriptions"]
 N5["Record result and return roster"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5 capability;
```

**Exception and recovery:** Approve rechecks final seat; rejected action changes nothing. SFU failure means removal recorded but media cleanup unresolved; schedule F15.

**Postcondition / next action:** Class stays open and teacher publication continues. Approved student continues F05; display names are not durable block identities.


## 10. F09 — Create or edit restriction profile

**Trigger / actor:** Scoped SYS or NET edits configuration.  
**References:** NAC02/03/04/07/08/16/17/18; D07/D15.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Authorize profile scope"]
 N1["Edit category domain default mode and exceptions"]
 N2["Validate syntax precedence and protected paths"]
 N3["Save versioned profile"]
 N4["Display saved status"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4 capability;
```

**Exception and recovery:** Invalid or out-of-scope edit is denied; no network mutation from save.

**Postcondition / next action:** Saved profile eligible for separately authorized F10 application.


## 11. F10 — Apply and verify restrictions

**Trigger / actor:** Authorized manual request or approved class-start automation.  
**References:** NAC01/05/10/11/16/17/18/19; D05/D06/D07/D15.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Check authorization and scope"]
 N1["Validate approved profile integration and local service safety"]
 N2["Preserve baseline and durable operation"]
 N3["Apply via supported adapter"]
 N4["Read back effective rules"]
 N5["Test affected client denied allowed and local paths"]
 N6["Record verified scope and time"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> N6
 N6 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5,N6 capability;
```

**Exception and recovery:** Rejected/partial/unknown result requires inspect/reconcile. Restore owned changes if needed; verified restoration or unresolved recovery is recorded.

**Postcondition / next action:** Return actual result to F01; F10 does not decide whether class may continue under D05.


## 12. F11 — Public website request

**Trigger / actor:** Student device requests an external domain.  
**References:** NAC02/03/04/08/18; D07.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Request domain over supported enforcement path"]
 N1["Evaluate current effective policy and exceptions"]
 N2["Deny matching restricted request or allow permitted resolution"]
 N3["Record only agreed minimal operational evidence"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3 capability;
```

**Exception and recovery:** Alternate DNS/VPN/direct IP may bypass domain-only controls; WAN outage is not proof of selective denial.

**Postcondition / next action:** Local classroom remains available; show restrictions only for tested supported scope.


## 13. F12 — Connection loss and reconnection

**Trigger / actor:** Student or teacher media connection is interrupted.  
**References:** S06/S07; D11.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Detect and show connection interruption"]
 N1["Classify reachable services"]
 N2["Retry under agreed policy"]
 N3["Recheck class admission and current authority"]
 N4["Refresh permitted credentials"]
 N5["Reconnect to current publication"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5 capability;
```

**Exception and recovery:** Ended class or revoked admission denies reconnect; lost capture requires explicit F06 consent. Persistent service failure routes F15.

**Postcondition / next action:** Same authorized class resumes or waiting/unresolved/denied status is shown; no automatic re-admission.


## 14. F13 — End class and restore policy

**Trigger / actor:** Teacher requests End class.  
**References:** NAC06/10/11; D11.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Authorize end request"]
 N1["Return completed operation or resume unfinished steps"]
 N2["Mark Ending close admissions and revoke grants"]
 N3["Execute media closure and owned policy restoration tracks"]
 N4["Record both track outcomes"]
 N5["Verify application and media closure"]
 N6["Select final class and restoration result"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> N6
 N6 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5,N6 capability;
```

**Exception and recovery:** Unauthorized request leaves class unchanged. Closure unverified means Class ending; verified closure can coexist with pending restoration. Conflicting external network changes require reconciliation.

**Postcondition / next action:** Class ended with restoration not required verified or pending; otherwise Class ending cleanup unresolved. F15 continues recovery.


## 15. F14 — Temporary expiry and emergency disable

**Trigger / actor:** Durable expiry trigger or scoped authorized emergency action.  
**References:** NAC12/NAC13; D11/D15.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Find expired operation or authorize emergency request"]
 N1["Load original operation and owned policy baseline"]
 N2["Reconcile current scope and external changes"]
 N3["Restore owned temporary changes"]
 N4["Verify read back and affected client paths"]
 N5["Record restored or unresolved state"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5 capability;
```

**Exception and recovery:** Unreachable or conflicting state is persistent unresolved recovery, not disabled/restored; repeated trigger is idempotent.

**Postcondition / next action:** Return status to active classroom/operator; F15 handles unresolved recovery; emergency policy action does not itself end class.


## 16. F15 — Diagnostics and recovery

**Trigger / actor:** Authorized operator or durable unresolved operation.  
**References:** Shared operational obligations; T09 Should; D11.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Authorize diagnostics scope"]
 N1["Identify failed network trust application media or enforcement component"]
 N2["Inspect operation and observed state"]
 N3["Plan authorized safe recovery"]
 N4["Resume unfinished work"]
 N5["Reverify affected behavior"]
 N6["Record evidence and notify operator"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> N5
 N5 --> N6
 N6 --> DONE(["Record outcome and next action"])
 classDef capability fill:#dcfce7,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4,N5,N6 capability;
```

**Exception and recovery:** Never replay completed mutation or overwrite unrelated network changes; persistent fault remains unresolved and visible.

**Postcondition / next action:** Return verified result to originating flow or durable unresolved record with next operator action.


## 17. F16 — Share and download materials

**Trigger / actor:** Teacher shares approved materials; admitted student requests them.  
**References:** T10/S09 Should; D16.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Authorize class and sharing permission"]
 N1["Validate agreed file type size and storage model"]
 N2["Make permitted material available"]
 N3["Recheck admission and download permission"]
 N4["Deliver material and record result"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> DONE(["Record outcome and next action"])
 classDef capability fill:#fff2b3,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4 capability;
```

**Exception and recovery:** Reject forbidden type/size or revoked access; direct file route cannot bypass authorization.

**Postcondition / next action:** Material accessed or clear denial; class remains open; content handling details await D16.


## 18. F17 — Schedules and configuration transfer

**Trigger / actor:** Scoped administrator manages policy tools.  
**References:** NAC09/14/20 Should; D11.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Authorize scope"]
 N1["Validate schedule timezone or imported rules"]
 N2["Save versioned configuration without secrets"]
 N3["At approved trigger recheck authority and execute F10 or F14"]
 N4["Record actual result"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> DONE(["Record outcome and next action"])
 classDef capability fill:#fff2b3,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4 capability;
```

**Exception and recovery:** Malformed import changes nothing; missed schedule/retry behavior needs D11. Required offline runtime remains mandatory.

**Postcondition / next action:** Configuration saved or scheduled operation recorded; applying and verification remain separate.


## 19. F18 — Optional participation history and group policy

**Trigger / actor:** Actor uses an explicitly selected optional feature.  
**References:** S10/T11/NAC15 Could; D17.

```mermaid
flowchart TB
 START(["Start"]) --> N0
 N0["Check selected feature and current actor permission"]
 N1["Branch to admitted participation owned history or authorized supported group policy"]
 N2["Validate activity ownership or target isolation"]
 N3["Process requested optional action"]
 N4["Return scoped result"]
 N0 --> N1
 N1 --> N2
 N2 --> N3
 N3 --> N4
 N4 --> DONE(["Record outcome and next action"])
 classDef capability fill:#e5e7eb,stroke:#52735e,color:#111;
 class N0,N1,N2,N3,N4 capability;
```

**Exception and recovery:** Unselected feature is not required; unauthorized submissions/history access denied; unsupported group identity cannot be claimed enforced.

**Postcondition / next action:** Return to class or admin view; no implied recording or remote student monitoring.


## 20. Mandatory branch diagrams for high-risk transitions

The overviews above show the principal sequence; the following diamonds define essential branching that must not be lost in a presentation.

```mermaid
flowchart TB
 A["F13 authorized end request"] --> B["Close admissions and revoke grants"]
 B --> C["Complete or record unresolved media closure"]
 B --> D["Restore owned policy or record not required or unresolved"]
 C --> E["Wait for both recorded outcomes"]
 D --> E
 E --> F{"Application and media closure verified?"}
 F -->|No| G["Class ending - cleanup unresolved - F15"]
 F -->|Yes| H{"Restoration status?"}
 H -->|Not required| I["Class ended - no temporary changes"]
 H -->|Verified| J["Class ended - prior policy restored"]
 H -->|Pending or failed| K["Class ended - restoration unresolved - F15"]
```

```mermaid
flowchart TB
 A["F07 control request"] --> B{"Authorized for action?"}
 B -->|No| C["Deny without changing publication"]
 B -->|Yes| D{"Class ending or ended?"}
 D -->|Yes| E["Disable controls - F13 takes precedence"]
 D -->|No| F{"Operation and publication current?"}
 F -->|No| G["Reject stale or mismatched request"]
 F -->|Yes| H["Execute or resume only unfinished action"]
 H --> I{"Current state still valid on response?"}
 I -->|No| J["Record stale outcome - do not revive old publication"]
 I -->|Yes| K{"Actual result verified?"}
 K -->|Yes| L["Record confirmed publication state"]
 K -->|No| M["Record unresolved - F12 or F15"]
```
