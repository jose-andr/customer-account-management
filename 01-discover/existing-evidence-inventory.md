# Existing evidence inventory

Status: Draft  
Owner: José Andrade  
Current stage: Discover  
Last updated: 29 July 2026

## Purpose

This page records the evidence and source material currently available for Customer Account Management.

It helps the workstream:

- avoid losing earlier work;
- distinguish evidence from interpretation and ambition;
- identify the authoritative source for each topic;
- avoid duplicating current-state documentation;
- assess what can be used now;
- identify evidence gaps; and
- support traceable problem-definition and design decisions.

This inventory records sources and their decision relevance.

It does not reproduce raw organisational material.

## Evidence handling rules

For each source, record:

- what the source contains;
- what it can safely support;
- its validation status;
- its limitations;
- where the authoritative version is held; and
- how it should be used in this repository.

Use the following evidence labels:

| Label | Meaning |
|---|---|
| Source material | Original document, repository, workshop output or system record |
| Reported evidence | Information provided by participants but not independently validated |
| Partially validated | Supported by more than one source or stakeholder, but not fully confirmed |
| Validated evidence | Confirmed through the required operational, data or governance review |
| Interpretation | Meaning derived from available evidence |
| Future signal | Possible future need, capability or solution |
| Decision | An authorised choice with recorded rationale |

## Current source inventory

| Source ID | Source | Type | Primary content | Current status | Authoritative location | Intended use |
|---|---|---|---|---|---|---|
| SRC-001 | `jose-andr/cx-current-state-sop-mapping` | GitHub repository | Current Customer Data and Systems Support operating practices, systems, decisions, workarounds, pain points and exceptions | Active input; validation varies by file | GitHub | Current-state operational evidence |
| SRC-002 | Customer Account Management brief, scope and activity plan — March 2026 | Discovery planning document | Initial central question, discovery ambition, sprint activities, stakeholder notes and early operational examples | Reported / draft | Organisational source file | Understand original intent and planned discovery activity |
| SRC-003 | Customer Account Management — April 2026 | Workshop and discovery output | Point-of-view statements, How Might We questions, problem-definition canvases, scope ideas, impact statements, future outcomes and proposed interventions | Mixed: aligned draft, reported evidence and future signals | Organisational source file | Recover workshop outputs and distinguish evidence from proposed solutions |
| SRC-004 | Customer Account Management — April 2026 problem statement | Consolidated problem-framing output | Reduced set of problem statements, impacts, scope, governance needs and intended outcomes | Aligned draft with unresolved elements | Organisational source file | Support the current working problem statement |
| SRC-005 | Customer Account Management discovery discussions | Stakeholder input | Alignment between the Customer Focus and Strategy Manager, CRM Product Owner and Customer Data and Systems Support Officer | Aligned draft | Meeting notes and working material | Confirm current problem-framing status |
| SRC-006 | CRM operational records and account-quality reporting | Organisational systems and reports | Duplicate accounts, account corrections, classifications, quality measures and operational activity | Not yet inventoried | CRM, reporting and authorised systems of record | Quantitative validation and baselining |
| SRC-007 | Customer and employee examples | Workshop and operational examples | Account creation issues, duplicate records, transfer activity, relationship-management gaps and repeated information | Reported; requires de-identification and validation | Organisational systems of record | Illustrate problem patterns without retaining identifiable cases |
| SRC-008 | Customer Account Management problem statement in this repository | Repository artefact | Current aligned draft problem statement, assumptions, boundaries, evidence gaps and proposed solutions excluded from the problem definition | Aligned draft | `02-define/problem-statement.md` | Working definition for continued Discover and Define activity |
| SRC-009 | Customer Account Management purpose and scope in this repository | Repository artefact | Workstream purpose, boundaries, intended outcomes and relationship to current-state SOP mapping | Aligned draft | `00-project-control/purpose-and-scope.md` | Control scope and prevent unplanned expansion |

## Source assessments

### SRC-001 — Current-state SOP mapping repository

Repository:

`jose-andr/cx-current-state-sop-mapping`

#### What it contains

The repository documents actual or reported current Customer Data and Systems Support practices, including:

- duplicate-account investigation and management;
- customer-record corrections;
- CRM support activities;
- systems and tools;
- decisions and handovers;
- exception pathways;
- manual workarounds;
- operational pain points;
- current controls; and
- unresolved questions.

#### What it can support

This source can support:

- understanding how account problems are currently handled;
- identifying operational effort and recurring workarounds;
- identifying decision points and ownership gaps;
- tracing account-quality issues to current processes;
- validating employee pain points;
- identifying transformation constraints; and
- establishing current-state patterns for future comparison.

#### Limitations

- individual files may have different validation statuses;
- reported practice must not be treated as organisation-wide practice;
- the repository focuses on current operations, not future-state design;
- it may not contain quantitative evidence of volume, frequency or cost; and
- it should not be copied into this repository.

#### Use rule

Reference the relevant file, finding and validation status.

Do not reproduce the SOP content.

---

### SRC-002 — March 2026 brief, scope and activity plan

#### What it contains

The March material establishes the initial central question:

> What problem are we trying to solve?

It also records an intended discovery programme covering:

- problem and opportunity definition;
- customer account-management use cases;
- current-state mapping;
- organisational context;
- Salesforce account-management practice;
- data cleansing;
- desired outcomes;
- roadmap development;
- sharing and feedback; and
- customer and employee pain points.

#### What it can support

This source can support:

- understanding the original discovery intent;
- identifying activities that were planned;
- recovering early stakeholder questions;
- identifying operational examples for validation; and
- comparing planned outputs with work actually completed.

#### Limitations

- the activity plan represents intention, not completed work;
- several items are workshop prompts rather than findings;
- stakeholder notes may be incomplete;
- proposed dates and sprint plans are historical;
- some examples may contain sensitive operational context; and
- ambition must not be recorded as a delivered outcome.

#### Use rule

Use this source to reconstruct the discovery plan and identify gaps.

Do not treat planned activities as completed evidence.

---

### SRC-003 — April 2026 workshop and discovery output

#### What it contains

The April material includes:

- point-of-view statements;
- How Might We questions;
- problem-definition canvases;
- customer and staff impact statements;
- scope proposals;
- success ideas;
- governance concepts;
- technology ideas;
- customer identity concepts;
- operating-model ideas; and
- wider customer-data framing.

The material includes a draft problem statement focused on the organisation’s inability to reliably identify a single, accurate view of each customer due to duplicated accounts, inconsistent classifications and the absence of a common identifier across systems.

#### What it can support

This source can support:

- recovering stakeholder-generated problem signals;
- identifying customer, employee and organisational impacts;
- recording potential opportunity areas;
- identifying assumptions;
- identifying solution bias;
- tracing the evolution of the problem statement; and
- understanding where Customer Account Management and wider Customer Data Management were being conflated.

#### Limitations

The material combines:

- evidence;
- participant opinion;
- assumptions;
- draft wording;
- proposed outcomes;
- possible measures;
- technology ideas; and
- future-state solutions.

It must therefore be decomposed before use.

Statements such as the need for:

- a master customer ID;
- a single customer view;
- dedicated roles;
- new governance;
- account standards; or
- duplicate-detection technology

must remain future signals until evaluated.

#### Use rule

Extract individual findings and label each as:

- reported evidence;
- assumption;
- interpretation;
- future signal; or
- aligned draft.

Do not transfer the workshop canvas as one validated artefact.

---

### SRC-004 — April 2026 consolidated problem statement

#### What it contains

The consolidated material narrows the earlier workshop outputs towards:

- inconsistent customer-information practices;
- unclear ownership;
- operational effort;
- poor service confidence;
- privacy and security concerns;
- reduced self-service capability;
- difficulty personalising interactions;
- transformation constraints; and
- the potential need for standards, roles and governance.

#### What it can support

This source can support:

- the current working problem statement;
- initial scope boundaries;
- impact categories;
- assumptions requiring validation;
- stakeholder-alignment history; and
- candidate outcome areas.

#### Limitations

- it still includes proposed responses alongside the problem;
- not all wording has been validated organisation-wide;
- outcome statements are not yet supported by baselines;
- governance and ownership proposals are not approved; and
- wider customer-data issues remain mixed with account-management issues.

#### Use rule

Use the source to support the aligned draft problem definition.

Separate problem, impact, scope, outcome and solution content before transferring it into repository artefacts.

## Current evidence by decision question

| Decision question | Available evidence | Current confidence | Gap |
|---|---|---|---|
| Is there a material Customer Account Management problem? | Workshop outputs, stakeholder alignment and current-state SOP signals | Medium | Consolidated evidence and quantitative scale |
| What is the core problem? | Aligned draft problem statement | Medium | Wider stakeholder and operational validation |
| Who is affected? | Customer, employee and organisational impact statements | Low to medium | Direct customer evidence and broader employee validation |
| What causes the problem? | Duplicate creation, inconsistent classifications, fragmented systems and unclear practices are reported | Low | Root-cause analysis |
| Which services are most affected? | Isolated examples exist | Low | Prioritised service and journey evidence |
| What is the scale of duplication? | Account-quality activity is known to exist | Low | Governed duplicate-account measures |
| What is the operational cost? | Manual effort and cleansing are reported | Low | Time, demand and cost baselines |
| What is the customer impact? | Repetition, fragmented interactions and inconsistent communications are reported | Low | Direct research and service-level evidence |
| What should be designed? | Multiple future signals exist | Low | Validated requirements and prioritised opportunities |
| What should be delivered first? | No agreed implementation priority | Low | Define-stage prioritisation |

## Existing evidence themes

The current material contains evidence or signals across the following themes:

### Customer identity and classification

- difficulty establishing whether records relate to the same customer;
- inconsistent treatment of statutory, non-statutory and organisational customers;
- incomplete representation of relationships;
- uncertainty about the meaning of a customer account; and
- inconsistent classifications across systems.

### Duplicate accounts

- duplicate creation;
- manual investigation;
- manual reconciliation;
- merge or correction activity;
- repeated customer information; and
- uncertainty about prevention controls.

### Account ownership

- uncertainty about who owns the customer;
- uncertainty about who owns an account;
- uncertainty about who owns linked services, permits or records;
- fragmented responsibility; and
- incomplete governance rules.

### Customer effort

- repeated explanations;
- difficulty updating information;
- fragmented histories;
- inconsistent communications;
- failed or delayed account interactions; and
- reduced self-service confidence.

### Employee effort

- searching;
- validating;
- reconciling;
- correcting;
- escalating;
- manually transferring linked information; and
- interpreting inconsistent business rules.

### Transformation readiness

- dependence on reliable customer records;
- dependence on consistent service information;
- risks to CRM and digital change;
- integration complexity;
- unclear minimum information needs; and
- limited confidence in customer measures.

## Evidence not yet available

The current repository does not yet contain validated evidence for:

- organisation-wide duplicate-account volume;
- duplicate-account creation rate;
- duplicate root causes by channel, system or process;
- account-quality trends;
- customer effort caused by account fragmentation;
- employee time spent on account corrections;
- repeat-contact impacts;
- self-service failure caused by account issues;
- incorrect communication rates;
- statutory and non-statutory classification accuracy;
- organisation-account quality;
- privacy or security incident patterns;
- cost of current-state account management;
- value of proposed interventions; or
- baseline measures for future evaluation.

## Evidence collection priorities

The next evidence activity should prioritise:

1. current-state SOP synthesis;
2. governed account-quality measures;
3. duplicate root-cause analysis;
4. high-impact customer and employee use cases;
5. affected service-owner validation;
6. privacy, records, security and data-governance review;
7. current ownership and decision-right mapping; and
8. baseline measures suitable for future evaluation.

## Privacy and source boundaries

Do not add the following to this repository:

- raw CRM exports;
- customer names;
- account identifiers;
- identifiable case details;
- unredacted screenshots;
- customer contact information;
- credentials;
- sensitive operational extracts; or
- copies of controlled organisational documents.

Use:

- safe summaries;
- redacted or synthetic examples;
- aggregated measures;
- repository references;
- file names;
- section references;
- evidence status;
- caveats; and
- decision relevance.

## Next action

## Additional evidence — Databricks customer data-quality pilot

### Evidence summary

| Field | Detail |
|---|---|
| Evidence item | Initial customer data-quality pilot |
| Evidence type | Exploratory analytical output |
| Source platform | Databricks data-quality framework |
| Presentation layer | Power BI Report Server |
| Source tables shown | `vwaccount`, `vwcontact` |
| Test date shown | 19 June 2026 |
| Validation status | Partially validated |
| Governed metric status | Not ready |
| Current use | Business-rule refinement input |
| Repository summary | `databricks-customer-data-quality-pilot-input.md` |

### What the evidence contains

The pilot includes technical checks across selected Account and Contact attributes covering:

- completeness;
- format or reference validity;
- uniqueness;
- similarity or potential-duplicate detection; and
- an aggregate rule-pass result.

Visible attributes and rule themes include:

- email completeness and format;
- mobile completeness and format;
- email and mobile similarity;
- ABN completeness or validity;
- ACN completeness or validity;
- repeated ABN;
- repeated ACN;
- name validity;
- name uniqueness;
- trading-name uniqueness;
- secondary email checks; and
- customer-number uniqueness.

### Preliminary dashboard results

The screenshots reviewed showed:

| Measure | Reported result |
|---|---:|
| Aggregate rule-pass rate | Approximately 95.9% |
| Completeness | Approximately 99.9% |
| Validity | Approximately 94.1% |
| Uniqueness | Approximately 95.2% |
| ABN validity | Approximately 81.80% |
| ACN validity | Approximately 56.59% |
| Email uniqueness | Approximately 86.02% |
| ABN uniqueness | Approximately 95.71% |
| ACN uniqueness | Approximately 90.77% |

These results remain exploratory.

They must not be interpreted as governed customer data-quality, accuracy or confirmed duplicate rates.

### Evidence value

The pilot provides useful evidence that:

- technical customer data-quality checks can be executed;
- Account and Contact attributes are included;
- selected rule failures are visible;
- duplicate and similarity diagnostics are already being tested;
- potential material quality issues exist;
- rule definitions require stronger business input;
- eligible populations require refinement;
- numerator and denominator definitions require validation;
- rule taxonomy requires review; and
- operational ownership and response pathways remain unresolved.

### Evidence limitations

The pilot does not yet confirm:

- what `records tested` represents;
- whether the grain is account, contact, attribute or rule execution;
- why different dashboard views show different tested totals;
- whether blanks are included in validity and uniqueness results;
- whether Account and Contact populations can be combined;
- whether rule results are weighted equally;
- whether repeated values are counted as records, groups or pairs;
- whether similarity thresholds align with business meaning;
- whether Salesforce and Plauti controls overlap with the Databricks rules;
- whether valid exceptions are excluded;
- whether inactive, merged or superseded records are included;
- whether failed records can be acted on safely; or
- whether any measure is suitable for executive reporting.

### Page-total discrepancy

The reviewed dashboard views showed different tested totals:

| Dashboard view | Records tested |
|---|---:|
| Full Records | 8,929,330 |
| All Attributes | 8,521,688 |
| Difference | 407,642 |

The difference requires technical reconciliation before the dashboard is used as a governed reporting source.

### Permitted use

The evidence may currently be used to:

- refine business-rule definitions;
- prepare workshops;
- identify calculation and denominator questions;
- compare technical logic with business intent;
- validate source fields;
- improve rule names and taxonomy;
- prioritise further investigation; and
- support decisions about Salesforce, Plauti and Databricks responsibilities.

The evidence must not currently be used to:

- claim that customer data quality is approximately 95.9%;
- report confirmed duplicate volumes;
- compare business units or teams;
- establish quality targets;
- approve automated record changes;
- evaluate staff performance;
- trigger customer-level decisions; or
- provide governed executive measures.

### Related priority rules

This evidence informs:

- `CAM-DQ-001 — Minimum valid contact method`;
- `CAM-DQ-002 — Exact email duplicate signal`;
- `CAM-DQ-003 — Exact mobile duplicate signal`;
- `CAM-DQ-004 — ABN completeness`;
- `CAM-DQ-005 — ACN completeness`;
- `CAM-DQ-006 — Repeated ABN`; and
- `CAM-DQ-007 — Repeated ACN`.

### Source boundary

The source screenshots and record-level data remain in approved organisational systems.

The repository should retain only:

- aggregate observations;
- rule names;
- field names;
- interpretation;
- caveats;
- refinement questions;
- source references; and
- decision logic.

Do not store:

- customer records;
- email addresses;
- telephone numbers;
- ABNs or ACNs tied to identifiable records;
- Salesforce record identifiers;
- failed-record extracts;
- unredacted screenshots;
- credentials; or
- sensitive operational data.

### Current evidence assessment

| Assessment | Status |
|---|---|
| Evidence available | Yes |
| Technical execution visible | Yes |
| Technical logic fully validated | No |
| Business definitions approved | No |
| Population and grain confirmed | No |
| Dashboard totals reconciled | No |
| Operational response agreed | No |
| Governed measures approved | No |
| Slide-safe wording available | No |
