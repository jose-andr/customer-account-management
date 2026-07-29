# Stakeholder map

Status: Draft  
Owner: José Andrade  
Current stage: Discover → Define  
Last updated: 29 July 2026

## Purpose

Identify the roles involved in Customer Account Management and clarify how they contribute to:

- problem validation;
- CRM data-quality rule refinement;
- current-state evidence;
- ownership decisions;
- technical implementation;
- operational action;
- governance;
- prioritisation; and
- future transformation design.

This map records working stakeholder roles.

It does not establish formal organisational accountabilities.

## Core working group

| Stakeholder role | Current contribution | Decisions or inputs needed | Engagement level |
|---|---|---|---|
| Customer Focus and Strategy Manager | Sponsor, problem alignment and strategic direction | Confirm scope, priorities, intended outcomes and escalation | Core |
| José Andrade | Workstream lead, repository owner and workshop facilitator | Coordinate evidence, rule refinement, decisions and next actions | Core |
| CRM Product Owner | Salesforce and Plauti product context | Confirm current configuration, constraints, roadmap and product ownership | Core |
| Customer Data and Systems Support Officer | Current operational practice and duplicate-management experience | Validate actual process, pain points, controls, exceptions and actionability | Core |
| Databricks or Data Governance technical representative | Data-quality framework and rule implementation | Confirm source, grain, technical feasibility, execution and reporting | Core |

## Governance and assurance stakeholders

| Stakeholder role | Contribution required | Engage when |
|---|---|---|
| Data Governance | Data ownership, stewardship, rule governance and measure acceptance | Refining ownership, standards and governed reporting |
| Privacy | Privacy implications of matching, merging and customer-information use | Rules involve identity, sensitive information or cross-system linkage |
| Records Management | Record integrity, retention and traceability | Changes affect account merging, correction or evidentiary records |
| Information Security | Access, control and platform security | Rules or workflows expose sensitive data or change permissions |
| Legal | Legal-entity interpretation and regulatory constraints | ABN, ACN, representation or statutory issues require advice |
| Enterprise Architecture | System relationships and future-state alignment | Design options affect multiple platforms or integrations |

## Operational stakeholders

| Stakeholder role | Evidence or input required | Engagement purpose |
|---|---|---|
| Customer Data and Systems Support team | Actual activities, workload, decision criteria and exceptions | Validate current-state account-quality work |
| Contact Centre | Customer-identification issues, repeated information and service impact | Validate frontline employee and customer impacts |
| Service owners | Service-specific account requirements and consequences | Confirm priority use cases and legitimate exceptions |
| Frontline operational staff | Practical account use, workarounds and escalation | Test whether proposed rules are actionable |
| Salesforce administrators | Validation rules, permissions, fields and Plauti configuration | Confirm current system behaviour |
| Analytics and reporting support | Measures, populations, denominators and trend reporting | Confirm metric safety and reporting feasibility |

## Customer and experience stakeholders

| Stakeholder role or source | Contribution required | Engagement approach |
|---|---|---|
| Voice of Customer or CX research | Existing evidence of repetition, failed access and fragmented interactions | Use de-identified themes and summaries |
| Customers using account-based services | Needs, pain points and acceptable outcomes | Targeted research only where evidence gaps remain |
| Customers using assisted channels | Account-identification and continuity issues | Use service-level evidence and safe examples |
| Accessibility and inclusion representatives | Risks created by mandatory fields or channel assumptions | Review contact and identity requirements |
| Community and business representatives | Organisation-account and relationship needs | Engage for priority organisation use cases |

## Stakeholder responsibilities by activity

| Activity | Lead | Required contributors | Consult where needed |
|---|---|---|---|
| Working problem statement | José Andrade | Manager, CRM Product Owner, Customer Data and Systems Support Officer | Service owners, governance stakeholders |
| Current-state duplicate-process validation | Customer Data and Systems Support Officer | José Andrade | CRM Product Owner |
| CRM rule refinement | José Andrade | CRM Product Owner, operational officer, Databricks or Data Governance representative | Privacy, service owners, Salesforce administrator |
| Plauti configuration validation | CRM Product Owner | Salesforce administrator | Operational duplicate reviewers |
| Databricks rule implementation | Databricks or Data Governance technical representative | CRM Product Owner, business rule owner | Analytics and security |
| Rule-result review | Business owner | Operational action owner, technical owner | Governance stakeholders |
| Duplicate confirmation and merge decision | Authorised operational role | CRM or system support | Privacy or escalation owner |
| Root-cause investigation | To confirm | CRM Product Owner, service owner, operational staff | Architecture and Digital |
| Transformation prioritisation | Customer Focus and Strategy Manager | José Andrade, CRM Product Owner | Service owners and governance |
| Future-state design | José Andrade | Core working group | Customers, staff and enabling teams |

## CRM rule ownership model

Each data-quality rule requires separate ownership roles.

| Ownership role | Responsibility |
|---|---|
| Business owner | Approves the rule’s purpose, definition, priority and permitted use |
| Data owner | Accountable for the source data domain and quality expectations |
| Data steward | Supports definition, monitoring, issue coordination and metadata |
| Operational action owner | Reviews failures and coordinates correction or escalation |
| Technical owner | Implements, schedules and maintains rule logic |
| Product owner | Confirms Salesforce and Plauti behaviour and manages product impacts |
| Governance owner | Confirms standards, thresholds and escalation where required |
| Decision owner | Decides whether the rule is approved, parked, rejected or superseded |

One person may hold multiple roles, but the responsibilities must remain explicit.

## Initial ownership gaps

| ID | Ownership question | Current position | Priority |
|---|---|---|---|
| OWN-001 | Who owns the business definition for Person Account contact completeness? | Open | Critical |
| OWN-002 | Who owns Person Account duplicate rules? | Open | Critical |
| OWN-003 | Who owns organisation-account ABN and ACN requirements? | Open | High |
| OWN-004 | Who reviews and acts on Databricks rule failures? | Open | Critical |
| OWN-005 | Who approves duplicate matching thresholds? | Open | Critical |
| OWN-006 | Who owns alignment between Plauti and Databricks rules? | Open | High |
| OWN-007 | Who owns upstream duplicate prevention? | Open | Critical |
| OWN-008 | Who is authorised to confirm and merge duplicate records? | Partially documented | Critical |
| OWN-009 | Who owns account-quality measures and reporting? | Open | High |
| OWN-010 | Who approves privacy, records and security controls? | Existing governance roles to confirm | High |

## Engagement principles

### Bring stakeholders in for a decision

Each engagement should have a clear purpose, such as:

- validate current practice;
- define a business rule;
- confirm an exception;
- assign ownership;
- approve a measure;
- identify a governance constraint; or
- decide whether work progresses.

Avoid broad consultation without a specific decision need.

### Separate operational and strategic authority

Operational expertise confirms what currently happens.

Strategic or governance authority confirms what should be adopted, prioritised or controlled.

Do not treat operational participation as formal approval.

### Use role names in the repository

Prefer role names rather than individual names unless:

- the person is the agreed owner;
- the action requires personal accountability; or
- the decision record needs a named approver.

### Protect customer information

Stakeholder engagement should use:

- de-identified summaries;
- synthetic examples;
- aggregate results;
- safe process walkthroughs; and
- authorised systems of record.

Do not add identifiable customer cases to this repository.

## Initial engagement sequence

### 1. Core rule-refinement group

Confirm participation from:

- Customer Focus and Strategy;
- CRM Product Ownership;
- Customer Data and Systems Support;
- Databricks or Data Governance technical support; and
- José Andrade as facilitator.

### 2. Plauti and Salesforce validation

Confirm:

- current production configuration;
- active scenarios;
- matching thresholds;
- record-type coverage;
- scheduled jobs;
- permissions; and
- existing validation controls.

### 3. Governance review

Engage Privacy, Records, Information Security and Data Governance where rules involve:

- identity matching;
- record merging;
- sensitive information;
- cross-system linkage;
- external verification;
- access changes; or
- automated action.

### 4. Service-owner validation

Engage service owners after the first rule definitions are clearer to confirm:

- legitimate exceptions;
- priority journeys;
- operational consequences;
- customer impact; and
- whether the rule supports a meaningful action.

## Stakeholder engagement register

| ID | Stakeholder role | Engagement purpose | Owner | Status | Next action |
|---|---|---|---|---|---|
| STK-001 | Customer Focus and Strategy Manager | Confirm scope, sponsorship and decision authority | José Andrade | Active | Confirm first workshop outcome expectations |
| STK-002 | CRM Product Owner | Validate Plauti and Salesforce controls | José Andrade | Active | Confirm current production configuration |
| STK-003 | Customer Data and Systems Support Officer | Validate duplicate process and operational action | José Andrade | Active | Schedule process walkthrough |
| STK-004 | Databricks or Data Governance technical representative | Confirm rule implementation and result status | José Andrade | To confirm | Identify technical participant |
| STK-005 | Data Governance | Confirm rule ownership and governed measure requirements | José Andrade | To engage | Include in refinement workshop |
| STK-006 | Privacy | Review identity and duplicate-rule risks | José Andrade | As required | Identify rules requiring review |
| STK-007 | Salesforce administrator | Confirm fields, validation rules and Plauti configuration | CRM Product Owner | To engage | Validate configuration evidence |
| STK-008 | Priority service owners | Confirm account requirements and exceptions | To assign | Later | Select after initial rules are refined |
| STK-009 | Analytics or reporting support | Validate metric definitions and reporting approach | To assign | Later | Engage before governed reporting |

## Current decision

Use a small core working group to refine the first CRM data-quality rules.

Bring additional governance, technical and service stakeholders into the work when a specific rule, risk or decision requires their expertise.

Do not seek broad endorsement before the initial rule definitions, populations and ownership questions are clear.

## Next action

Confirm the business owner, operational action owner and technical owner for:

1. minimum valid contact method;
2. exact email duplicate signal;
3. exact mobile duplicate signal;
4. ABN completeness;
5. ACN completeness;
6. repeated ABN; and
7. repeated ACN.
