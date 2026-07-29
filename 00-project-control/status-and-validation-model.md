# Status and validation model

Status: Active  
Owner: José Andrade  
Current stage: Discover → Define  
Last updated: 29 July 2026

## Purpose

Define the status labels used across the Customer Account Management repository.

This model helps the workstream:

- distinguish evidence from interpretation;
- separate stakeholder alignment from formal approval;
- show whether current-state practice has been validated;
- prevent proposed solutions becoming implicit requirements;
- distinguish business rule approval from technical implementation;
- make uncertainty visible; and
- support traceable decisions.

A status describes the maturity or validation of an artefact.

It does not replace the source, evidence or decision rationale.

## Core content types

Repository content should identify which type of statement is being recorded.

| Content type | Meaning |
|---|---|
| Source material | Original document, repository, system record, workshop output or approved organisational source |
| Evidence | Information supported by an identified source |
| Reported practice | What a participant says currently occurs |
| Validated practice | Current practice confirmed to the required operational level |
| Assumption | A belief that still requires testing |
| Interpretation | Meaning derived from available evidence |
| Future signal | A possible future need, capability or direction |
| Recommendation | A proposed response supported by available evidence |
| Decision | An authorised choice with recorded rationale |
| Action | Work agreed for completion |
| Outcome | An observed result after an intervention |
| Requirement | An explicitly approved need that a future response must satisfy |

Do not record an assumption, interpretation, future signal or recommendation as a requirement without an explicit decision.

## Repository-wide status model

| Status | Meaning | Suitable use |
|---|---|---|
| Draft | Initial content is being developed | Early pages, working notes and first versions |
| Open | An issue, question or gap has not been resolved | Evidence gaps, actions, risks and decisions |
| Reported | Information was supplied by a participant but not independently confirmed | Current-state interviews and workshop findings |
| Partially validated | Some supporting evidence exists, but important uncertainty remains | Findings supported by more than one source |
| Aligned draft | Key participants agree the content is suitable for continued work | Problem statements, scope and early definitions |
| In review | Content is ready for review by the required stakeholders | Rules, findings, recommendations and designs |
| Validated | Evidence or practice has been checked to the level required for its intended use | Current-state findings and metric definitions |
| Endorsed | An authorised stakeholder or group agrees the content may guide the workstream | Scope, principles and recommendations |
| Approved | An authorised decision has been made and implementation may proceed | Requirements, rules, designs and controls |
| Implemented | The agreed change or technical logic exists | Databricks rules, Salesforce controls and process changes |
| Scheduled | An implemented control runs on an agreed schedule | Databricks rules, Plauti jobs and reports |
| Results under review | Outputs exist but are not yet accepted for governed use | New rules and pilot reporting |
| Operational | The change is active in normal service and has an owner | Embedded controls and processes |
| Superseded | Replaced by a later artefact, rule or decision | Historical versions |
| Rejected | Reviewed and explicitly not progressed | Rules, options and assumptions |
| Parked | Not progressing now but may be reconsidered | Lower-priority rules or ideas |
| Retired | Previously active but no longer used | Rules, controls and measures |
| Archived | Retained for history but no longer active | Closed working material |

## Evidence validation levels

Use the following levels for findings and current-state evidence.

### Level 0 — Unrecorded

The evidence has not yet been collected.

Use:

`Open`

### Level 1 — Reported

The evidence has been supplied by one participant or source.

Use:

`Reported`

This is suitable for:

- discovery;
- identifying questions;
- recording pain-point signals;
- generating assumptions; and
- planning validation.

It is not sufficient for:

- organisation-wide claims;
- formal requirements;
- controlled measures; or
- high-risk design decisions.

### Level 2 — Partially validated

The evidence has been supported by:

- more than one participant;
- more than one source;
- a limited process walkthrough;
- a partial configuration review; or
- a preliminary quantitative result.

Use:

`Partially validated`

This may support:

- working problem framing;
- prioritisation for further discovery;
- initial design hypotheses; and
- contained experiments.

### Level 3 — Validated for decision

The evidence has been checked to the level required for a specific decision.

Use:

`Validated`

Validation may include:

- operational walkthrough;
- source-system confirmation;
- configuration review;
- governed metric review;
- stakeholder approval;
- privacy, records or security review; and
- reconciliation against an authoritative source.

Validated does not necessarily mean universally true.

The intended decision use must remain explicit.

### Level 4 — Endorsed or approved

The evidence, definition, rule, recommendation or design has been formally accepted by the authorised owner.

Use:

- `Endorsed` for strategic direction or working guidance;
- `Approved` where implementation or formal adoption may proceed.

## Alignment is not approval

Use `Aligned draft` when key participants agree that content is suitable for continued work.

Examples:

- working problem statement;
- initial scope;
- early design principles;
- draft outcome model.

`Aligned draft` does not mean:

- formally approved;
- organisation-wide;
- validated by all affected services;
- approved policy;
- approved technology requirement; or
- ready for implementation.

## Current-state practice statuses

Use these statuses in current-state discovery.

| Status | Meaning |
|---|---|
| Reported | Participant says this practice occurs |
| Partially validated | Some steps, systems or participants have been checked |
| Validated | The practice has been confirmed to the required level |
| Rejected | The reported practice was not supported |
| Future signal | The item describes a possible future practice rather than current activity |
| Out of scope | The practice is not part of the current discovery boundary |

When documenting current state:

- map actual work, not position descriptions;
- preserve exceptions and workarounds;
- state which role provided the evidence;
- distinguish normal practice from rare cases;
- avoid converting proposed improvements into current requirements; and
- retain unresolved contradictions.

## Assumption statuses

| Status | Meaning |
|---|---|
| Open | Not yet tested |
| In validation | Evidence collection is underway |
| Partially supported | Some evidence supports the assumption |
| Supported | Sufficiently supported for the stated decision |
| Rejected | Evidence does not support the assumption |
| Superseded | Replaced by a more precise assumption or decision |
| Parked | Not currently important to the next decision |

An assumption should not remain `Supported` indefinitely where it has become an approved rule, requirement or decision.

Update the relevant artefact and supersede the assumption.

## Decision statuses

| Status | Meaning |
|---|---|
| Proposed | Decision has been raised but not agreed |
| Agreed | Decision is active for the current workstream |
| Conditional | Decision applies subject to stated validation or dependency |
| Superseded | Replaced by a later decision |
| Rejected | Considered and not adopted |

Every conditional decision should record:

- the condition;
- evidence required;
- owner;
- review point; and
- consequence if the condition is not met.

## Risk statuses

| Status | Meaning |
|---|---|
| Open | Risk requires attention |
| Monitoring | Risk is being watched |
| Mitigating | Treatment is underway |
| Escalated | Formal review or decision is required |
| Accepted | Authorised owner has accepted the risk |
| Closed | Risk is no longer active |
| Superseded | Replaced by a more precise risk |

## CRM rule definition statuses

Business definition and technical execution must be tracked separately.

### Definition status

| Status | Meaning |
|---|---|
| Proposed | Initial rule or business question |
| In refinement | Business meaning, population, exceptions or ownership is incomplete |
| Ready for implementation | Business definition is complete and approved |
| Parked | Not currently progressing |
| Rejected | Reviewed and not required |
| Superseded | Replaced by another rule |

### Execution status

| Status | Meaning |
|---|---|
| Not started | No technical implementation has begun |
| In development | Logic is being created |
| Implemented | Logic exists but is not necessarily scheduled |
| Scheduled | Rule runs at an agreed frequency |
| Results under review | Outputs exist but are not governed |
| Validated | Logic and outputs are approved for the stated use |
| Failed | Rule cannot currently execute reliably |
| Retired | Rule is no longer active |

A rule can be technically implemented while its business definition remains incomplete.

That rule must not be treated as governed.

## CRM rule readiness gates

A CRM data-quality rule moves through the following gates.

### Gate 1 — Proposed

Minimum:

- initial business question;
- known source or field; and
- reason the rule may be useful.

### Gate 2 — In refinement

Minimum:

- working business description;
- proposed population;
- proposed grain;
- unresolved questions visible; and
- owner being identified.

### Gate 3 — Ready for implementation

Required:

- business question agreed;
- population explicit;
- grain explicit;
- failure condition agreed;
- valid exceptions documented;
- exclusions documented;
- numerator and denominator defined where required;
- output unit clear;
- business owner assigned;
- operational owner assigned;
- technical owner assigned;
- action on failure clear;
- privacy and governance implications reviewed; and
- business owner approval recorded.

### Gate 4 — Implemented

Required:

- technical logic created;
- source and field names confirmed;
- rule version recorded;
- test execution completed; and
- technical owner identified.

### Gate 5 — Results under review

Required:

- outputs available;
- expected and unexpected results reviewed;
- false positives assessed;
- possible false negatives considered;
- grain confirmed;
- reconciliation completed where required; and
- caveats documented.

### Gate 6 — Validated for use

Required:

- business owner accepts the result;
- operational owner accepts the action process;
- metric definition is safe;
- permitted use is documented;
- reporting language is approved; and
- review cadence is agreed.

### Gate 7 — Operational

Required:

- rule is scheduled;
- output is monitored;
- failures are acted on;
- ownership is maintained;
- changes are version-controlled; and
- performance is periodically reviewed.

## Metric validation statuses

Use these statuses for Databricks and CRM measures.

| Status | Meaning |
|---|---|
| Exploratory | Output is being used for investigation only |
| Technically calculated | Query has produced a result, but business safety is not confirmed |
| Definition under review | Numerator, denominator, grain or population is being checked |
| Validated for analysis | Safe for the stated analytical purpose |
| Slide-safe | Definition, caveats and wording are suitable for presentation |
| Governed | Approved for repeatable organisational reporting |
| Retired | Measure is no longer used |

Use the following warning where appropriate:

> This is technically calculated but not decision-safe because the business definition, population, grain or denominator has not been validated.

## Duplicate terminology

Use these labels consistently.

| Term | Meaning |
|---|---|
| Duplicate signal | A condition suggesting records may be related |
| Potential duplicate | Records, pairs or groups flagged by a matching rule |
| Confirmed duplicate | Records reviewed and determined to represent the same customer or organisation |
| Rejected match | Potential duplicate reviewed and determined not to be a duplicate |
| Unresolved match | Potential duplicate that cannot yet be confirmed or rejected |
| Merge candidate | Confirmed duplicate being assessed for merge |
| Merged | Records combined through an authorised process |

Do not use `duplicate count` where the measure is actually:

- flagged records;
- matched pairs;
- duplicate groups;
- potential duplicates; or
- confirmed duplicates.

## Confidence rating

Where useful, add a confidence rating alongside status.

| Confidence | Meaning |
|---|---|
| Low | Based mainly on incomplete, isolated or untested evidence |
| Medium | Supported by multiple sources or partial validation |
| High | Supported by reliable evidence and appropriate review |

Status and confidence are different.

Example:

`Status: Partially validated`  
`Confidence: Medium`

## Required metadata

Major repository artefacts should include:

```text
Status:
Owner:
Current stage:
Last updated:
