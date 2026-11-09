# ClassroomCast documentation index

> **Start here for the meeting tomorrow, 10 November 2026:** [Reviewed meeting package and findings](meeting-2026-11-10/README.md). It uses the latest three-sprint site schedule as a proposal; the older six-sprint documents below are retained as history.

**Version:** 0.1 · **Prepared:** 9 November 2026 · **Status:** Proposed review draft; no teacher approval or product test execution claimed.

## 1. Start here

This is the new review package for **ClassroomCast — Local Network Screen Sharing and Access Control System**, located under classroomCast_v2/docs. The older classroomcast_v1 materials are preserved. This package is documentation only: it does not implement, deploy, submit or approve the project.

1. Read [project overview](01-requirements/01-project-overview.md) and [source conflicts](sources/review-and-conflicts.md).
2. Review the [proposal](02-project-proposal/01-project-proposal.md), [scope](02-project-proposal/02-project-scope.md) and [teacher questions](07-teacher-review/04-open-questions.md).
3. Walk through [roles](01-requirements/06-user-roles-and-permissions.md), [workflows](03-system-analysis-and-design/02-system-workflows.md) and [architecture](03-system-analysis-and-design/01-system-architecture.md).
4. Confirm [acceptance tests](05-testing-and-evaluation/02-test-cases.md), then refine [Scrum work](04-scrum-and-project-management/04-sprint-planning.md).
5. Record actual decisions in [decision log](07-teacher-review/03-feedback-and-decision-log.md); keep [traceability](traceability.md) updated.

## 2. Current review position

63 original requirements, 68 feature entries, 15 use cases, 18 process flows, 26 inherited delivery items and 63 proposed requirement-level stories. Original priorities: 31 Must, 7 Should, 3 Could and 22 unlabeled deployment obligations. No implementation progress, product test result or teacher acceptance is inferred.

**Resolve first:** test conditions for the specified 50–150 students; equipment and authorization for both deployment modes; admission/failure rules; team availability and the latest three-sprint schedule. Use the meeting package for the latest schedule proposal.

## 3. Document index


### 01-requirements

- [ClassroomCast project overview](01-requirements/01-project-overview.md)
- [Problem statement and objectives](01-requirements/02-problem-statement-and-objectives.md)
- [Software requirements specification](01-requirements/03-software-requirements-specification.md)
- [Functional requirements and deployment obligations](01-requirements/04-functional-requirements.md)
- [Non-functional requirements](01-requirements/05-non-functional-requirements.md)
- [User roles and permissions](01-requirements/06-user-roles-and-permissions.md)
- [Business rules](01-requirements/07-business-rules.md)
- [Use-case catalogue](01-requirements/08-use-cases.md)

### 02-project-proposal

- [Project proposal](02-project-proposal/01-project-proposal.md)
- [Project scope](02-project-proposal/02-project-scope.md)
- [Objectives and expected outcomes](02-project-proposal/03-project-objectives-and-expected-outcomes.md)
- [Feasibility study](02-project-proposal/04-feasibility-study.md)
- [Timeline and milestones](02-project-proposal/05-project-timeline-and-milestones.md)
- [Risks and mitigation](02-project-proposal/06-risks-and-mitigation.md)

### 03-system-analysis-and-design

- [System architecture](03-system-analysis-and-design/01-system-architecture.md)
- [System workflows F01–F18](03-system-analysis-and-design/02-system-workflows.md)
- [Role-to-use-case diagram](03-system-analysis-and-design/03-use-case-diagram.md)
- [Conceptual database design](03-system-analysis-and-design/04-database-design.md)
- [API and event design](03-system-analysis-and-design/05-api-design.md)
- [Security design](03-system-analysis-and-design/06-security-design.md)
- [Infrastructure and deployment design](03-system-analysis-and-design/07-infrastructure-design.md)
- [UI and UX design](03-system-analysis-and-design/08-ui-ux-design.md)

### 04-scrum-and-project-management

- [Scrum plan](04-scrum-and-project-management/01-scrum-plan.md)
- [Product backlog](04-scrum-and-project-management/02-product-backlog.md)
- [User stories and acceptance criteria](04-scrum-and-project-management/03-user-stories.md)
- [Sprint planning](04-scrum-and-project-management/04-sprint-planning.md)
- [Team roles and responsibilities](04-scrum-and-project-management/05-team-roles-and-responsibilities.md)
- [Definition of Ready and Definition of Done](04-scrum-and-project-management/06-definition-of-done.md)
- [Meeting and review templates](04-scrum-and-project-management/07-meeting-and-review-template.md)

### 05-testing-and-evaluation

- [Testing strategy](05-testing-and-evaluation/01-testing-strategy.md)
- [Test-case catalogue](05-testing-and-evaluation/02-test-cases.md)
- [Performance and offline testing](05-testing-and-evaluation/03-performance-testing.md)
- [Security testing](05-testing-and-evaluation/04-security-testing.md)
- [User acceptance testing](05-testing-and-evaluation/05-user-acceptance-testing.md)

### 06-final-documentation

- [Final academic report outline](06-final-documentation/01-final-report-outline.md)
- [Technical documentation and handover plan](06-final-documentation/02-technical-documentation.md)
- [User manual outline](06-final-documentation/03-user-manual-outline.md)
- [Presentation outline](06-final-documentation/04-presentation-outline.md)

### 07-teacher-review

- [Teacher review meeting agenda](07-teacher-review/01-teacher-meeting-agenda.md)
- [Teacher approval checklist](07-teacher-review/02-teacher-approval-checklist.md)
- [Feedback and decision log](07-teacher-review/03-feedback-and-decision-log.md)
- [Open questions for user and teacher](07-teacher-review/04-open-questions.md)

### sources

- [Supplied specification — preserved source snapshot](sources/supplied-specification.md)
- [Source review and unresolved conflicts](sources/review-and-conflicts.md)
- [Source inventory and preservation manifest](sources/source-manifest.md)

## 4. Validation and sources

See [traceability](traceability.md) and [validation report](VALIDATION.md). Relative links to older documents depend on preserving sibling classroomcast_v1. The copied specification is evidence; the requirements register is the organized review baseline. Generated images are not used as a substitute for checked Mermaid source. All diagrams remain proposed design views.

## 5. Next meeting

Bring the proposal, scope, flow overview, acceptance targets and checklist to the teacher. Record named decision owners and approval evidence; inventory the actual school server and network with IT. Then reforecast the sprint backlog and execute the approved feasibility experiments. The final-report documents are outlines until real implementation and evaluation evidence exists.

## Eight supporting submission documents

[Open the submission index](submission-2026-11-10/README.md). Capacity corrected to the teacher-specified 50–150; full catalogue and inherited flows included. Draft readiness is separate from approval and test execution.
