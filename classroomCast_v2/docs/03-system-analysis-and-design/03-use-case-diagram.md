# Role-to-use-case diagram

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Interpretation

This Mermaid flowchart is an actor-goal map, not a claim of formal UML use-case notation. Human roles are external to the application; automation is an internal mechanism. The optional abstract User parent conveys common access only and grants no inherited permissions. UC identifiers match the canonical catalogue.

```mermaid
flowchart LR
 U["User - abstract grouping only"] -.-> T["Teacher"]
 U -.-> S["Student"]
 U -.-> A["System Administrator"]
 U -.-> N["IT Network Administrator"]
 subgraph CC["ClassroomCast application and local integrations"]
 C1["UC01 Create classroom"]
 C2["UC02 Admission"]
 C3["UC03 Publish and receive media"]
 C4["UC04 Participant management"]
 C5["UC05 Profiles"]
 C6["UC06 Apply and verify policy"]
 C7["UC07 Reconnect"]
 C8["UC08 End class and restore"]
 C9["UC09 Emergency and expiry recovery"]
 C10["UC10 Diagnostics"]
 C11["UC11 Materials - Should"]
 C12["UC12 Policy tools - Should"]
 C13["UC13 Optional participation history targeting"]
 C14["UC14 Campus deployment"]
 C15["UC15 Portable deployment"]
 end
 T --> C1 & C2 & C3 & C4 & C8 & C11 & C13
 S --> C2 & C3 & C7 & C11 & C13
 A --> C5 & C6 & C9 & C10 & C12 & C13
 N --> C5 & C6 & C9 & C10 & C12 & C13 & C14 & C15
```

## 2. Permission caveats

Every edge is subject to the [permission matrix](../01-requirements/06-user-roles-and-permissions.md). SYS/NET policy actions require assigned scope; diagnostic access is limited. Optional group targeting requires supported network identity. Teacher approval concerns only owned classes. No edge grants SYS/NET classroom media access. Automatic expiry and approved class-start policy actions act under recorded authority.
