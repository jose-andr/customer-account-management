# CRM data-quality rule refinement workshop

Status: Draft  
Owner: José Andrade  
Current stage: Define  
Last updated: 29 July 2026

## Purpose

This workshop will refine the first priority CRM data-quality rules so they are clear enough for business approval and technical implementation.

The workshop will align:

- business meaning;
- Salesforce preventative controls;
- Plauti duplicate-detection behaviour;
- Databricks analytical checks;
- operational review;
- ownership;
- exceptions;
- actions; and
- reporting use.

The objective is not to review every current rule.

The objective is to make decisions on a small set of priority rules.

## Source material

Use the following sources during the workshop.

Each source has a different role.

Do not treat any one source as sufficient evidence for approving a business rule.

### Salesforce data-quality rule inventory

[Salesforce Data Quality Rules](https://jira-cityofmelbourne.atlassian.net/wiki/spaces/DP/pages/527597570/Salesforce+Data+Quality+Rules)

This remains the working source of truth for:

- current rule IDs;
- draft technical logic;
- active and parked status;
- source fields;
- implementation notes;
- unresolved technical questions; and
- named contacts where recorded.

The Confluence inventory does not by itself establish that a rule has an approved business definition or governed reporting use.

### Databricks customer data-quality pilot

Use:

`01-discover/databricks-customer-data-quality-pilot-input.md`

This page records the initial Databricks rule execution and Power BI dashboard as exploratory evidence.

Use it to examine:

- rules already tested;
- source tables shown in the pilot;
- visible rule names and thresholds;
- preliminary rule-pass results;
- page-total discrepancies;
- possible grain and denominator issues;
- rule-taxonomy issues;
- compatibility between account and contact results; and
- questions requiring technical validation.

The pilot may support rule refinement.

It must not currently be used to:

- claim an overall governed customer data-quality score;
- report confirmed duplicate rates;
- establish performance targets;
- approve automated remediation;
- compare teams or services; or
- present executive measures without further validation.

The displayed aggregate pass rate of approximately 95.9% remains exploratory.

### Detailed rule definitions

Use the following pages as the primary working definitions for the first refinement cycle:

#### Person Account rules

- `02-define/rules/CAM-DQ-001-minimum-valid-contact-method.md`
- `02-define/rules/CAM-DQ-002-exact-email-duplicate-signal.md`
- `02-define/rules/CAM-DQ-003-exact-mobile-duplicate-signal.md`

#### Organisation Account rules

- `02-define/rules/CAM-DQ-004-abn-completeness.md`
- `02-define/rules/CAM-DQ-005-acn-completeness.md`
- `02-define/rules/CAM-DQ-006-repeated-abn.md`
- `02-define/rules/CAM-DQ-007-repeated-acn.md`

Each rule page records:

- the business question;
- current working definition;
- eligible-population questions;
- candidate exclusions and exceptions;
- proposed numerator and denominator;
- grain and output-unit questions;
- Salesforce, Plauti and Databricks responsibilities;
- operational-response requirements;
- ownership gaps;
- risks;
- Definition of Ready; and
- workshop decisions.

The pages are draft refinement artefacts.

They are not approved business rules.

### CRM data-quality rule register

Use:

`02-define/crm-data-quality-rule-register.md`

The register is the portfolio-level control page for:

- rule status;
- priority;
- pilot-to-rule mapping;
- detailed rule links;
- shared refinement decisions;
- technical-execution status;
- governed-use status;
- workshop decisions; and
- completion criteria.

Update the register immediately after the workshop.

Do not duplicate all rule-level detail in the register.

### CRM data-quality rule refinement index

Use:

`02-define/crm-data-quality-rule-refinement-index.md`

The index provides:

- the overall refinement sequence;
- common population and grain decisions;
- shared denominator-safety rules;
- tool boundaries;
- duplicate terminology;
- pilot findings requiring refinement; and
- the definition of completion for the first cycle.

Use it to prevent inconsistent decisions across individual rules.

### Plauti configuration

Use:

`Plauti Duplicate Check Configuration`

Confirm the current production position rather than relying only on historical documentation.

Use this source to validate:

- active duplicate scenarios;
- matching fields;
- exact and fuzzy logic;
- thresholds;
- record types;
- cross-object behaviour;
- real-time and scheduled checks;
- result fields;
- review outcomes;
- merge permissions;
- override behaviour;
- exception handling; and
- scheduled duplicate jobs.

The Plauti configuration may overlap with Databricks rules, but the tools do not necessarily serve the same purpose.

Do not assume Databricks should reproduce Plauti logic.

### Salesforce controls

Confirm existing Salesforce validation, matching and duplicate-management behaviour.

For each rule, identify:

- current validation rules;
- current duplicate rules;
- account-search prompts;
- warning or blocking behaviour;
- create and update coverage;
- integration and import coverage;
- override permissions;
- exception handling;
- existing ownership; and
- known operational impacts.

Do not recommend a new Salesforce control until the existing control position and valid exceptions are understood.

### Current-state operations

Use:

`jose-andr/cx-current-state-sop-mapping`

to validate how the following currently occur:

- account search;
- duplicate identification;
- duplicate review;
- record correction;
- merge assessment;
- merge execution;
- escalation;
- exception handling;
- audit activity; and
- root-cause improvement.

The current-state repository documents actual or reported operational practice.

Do not replace current-state evidence with proposed role scope or future operating-model assumptions.

### Supporting repository pages

Use where relevant:

- `01-discover/evidence-gaps.md`
- `01-discover/current-state-evidence-synthesis.md`
- `01-discover/existing-evidence-inventory.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`

### Source hierarchy for workshop decisions

Use the following hierarchy:

| Decision need | Primary source |
|---|---|
| Current technical rule inventory | Salesforce Data Quality Rules Confluence page |
| Initial analytical results | Databricks pilot evidence page and governed source environment |
| Current duplicate configuration | Live Salesforce and Plauti configuration |
| Current operational practice | `cx-current-state-sop-mapping` and operational representatives |
| Draft business definition | Individual rule page |
| Portfolio status | CRM data-quality rule register |
| Shared refinement standards | CRM data-quality rule refinement index |
| Approved project decision | Decision log |
| Original customer or operational data | Approved organisational system of record |

Where sources conflict:

1. record the contradiction;
2. do not resolve it through assumption;
3. assign a validation owner;
4. record the required evidence;
5. keep the rule in refinement or validation status; and
6. update the rule page after the source has been confirmed.

### Evidence handling

Do not bring raw customer records into the repository or workshop pack.

Use:

- aggregate results;
- field names;
- rule descriptions;
- de-identified examples;
- synthetic examples;
- masked values;
- screenshots without customer information; and
- controlled access to source systems where record-level review is necessary.

Do not place the following in GitHub:

- customer names;
- email addresses;
- telephone numbers;
- ABNs or ACNs tied to identifiable accounts;
- CRM record IDs;
- failed-record extracts;
- unredacted dashboard screenshots;
- credentials; or
- sensitive operational data.

## Workshop outcome

By the end of the workshop, each selected rule should have one recorded decision:

- Approve;
- Refine;
- Validate;
- Park;
- Reject; or
- Supersede.

A rule should only be approved when:

- the business question is clear;
- the population is explicit;
- the record grain is explicit;
- the failure condition is agreed;
- valid exceptions are documented;
- ownership is assigned;
- action on failure is clear;
- Plauti alignment is understood where relevant;
- caveats are documented; and
- the intended Databricks use is clear.

## Participants

Required:

- Customer Focus and Strategy;
- CRM Product Owner;
- Customer Data and Systems Support Officer;
- Databricks or Data Governance technical representative; and
- workshop facilitator.

Invite where relevant:

- Privacy;
- Records;
- Information Security;
- service owners;
- frontline operational representatives;
- Salesforce administrator; and
- analytics or reporting support.

## Roles in the workshop

| Role | Responsibility |
|---|---|
| Business owner | Confirms the purpose and acceptable business rule |
| Operational representative | Explains current practice, exceptions and actionability |
| CRM Product Owner | Confirms Salesforce and Plauti behaviour |
| Databricks or Data Governance representative | Confirms technical feasibility and output design |
| Governance representative | Identifies privacy, records, security or ownership constraints |
| Facilitator | Keeps the group focused on decisions and records unresolved items |

## Workshop scope

### Rules for this session

| Rule ID | Rule |
|---|---|
| CAM-DQ-001 | Minimum valid contact method |
| CAM-DQ-002 | Exact email duplicate signal |
| CAM-DQ-003 | Exact mobile duplicate signal |
| CAM-DQ-004 | Organisation ABN completeness |
| CAM-DQ-005 | Organisation ACN completeness |
| CAM-DQ-006 | Repeated ABN duplicate signal |
| CAM-DQ-007 | Repeated ACN duplicate signal |

### Out of scope for this session

- fuzzy-name matching;
- organisation-name matching;
- trading-name matching;
- external ABN or ACN verification;
- case-quality rules;
- work-order rules;
- knowledge-article rules;
- call-recording rules;
- full future-state account model;
- technology procurement; and
- organisation-wide governance design.

These may be considered in later refinement sessions.

## Preparation

### Facilitator preparation

Before the workshop:

- confirm the current Confluence rule inventory;
- identify the current Plauti scenario for each duplicate rule;
- prepare the seven priority rules in the rule register;
- identify existing Salesforce validation rules;
- confirm known account populations;
- note unresolved field-name questions;
- prepare a visible decision log; and
- confirm where approved outputs will be recorded.

### Participant preparation

Participants should review:

- the relevant Confluence rule entries;
- the current Plauti configuration;
- the priority rule register;
- known operational exceptions;
- current remediation activity; and
- any available aggregate rule results.

Do not bring raw customer records into the workshop materials.

Use de-identified or synthetic examples where examples are required.

## Proposed agenda

| Time | Activity | Output |
|---:|---|---|
| 5 minutes | Purpose, scope and decision rules | Shared understanding |
| 10 minutes | Current control-system overview | Salesforce, Plauti, Databricks and operational roles clarified |
| 15 minutes | CAM-DQ-001 — contact completeness | Refined definition and decision |
| 15 minutes | CAM-DQ-002 and CAM-DQ-003 — exact duplicate signals | Refined definitions and decisions |
| 15 minutes | CAM-DQ-004 and CAM-DQ-005 — ABN and ACN completeness | Refined definitions and decisions |
| 15 minutes | CAM-DQ-006 and CAM-DQ-007 — repeated identifiers | Refined definitions and decisions |
| 10 minutes | Ownership, actions and technical readiness | Owners and next steps |
| 5 minutes | Confirm decisions and unresolved questions | Agreed workshop record |

Total duration:

`85 minutes`

If only 60 minutes is available, split the activity into:

1. Person Account rules; and
2. organisation-account rules.

## Decision sequence for each rule

For each rule, work through the questions below in order.

### 1. Business question

What decision or action should this rule support?

Do not begin with the SQL or field name.

### 2. Business expectation

What should good data look like?

State this in plain language.

### 3. Population

Which records should be assessed?

Confirm:

- account type;
- active or inactive status;
- record type;
- date range;
- historical records;
- test records; and
- exclusions.

### 4. Grain

What does one result row represent?

Choose one:

- account;
- failed field;
- matched pair;
- duplicate group; or
- another explicit unit.

### 5. Failure condition

What specific condition causes the rule to fail?

### 6. Valid exceptions

Which records may legitimately fail the apparent rule?

### 7. Existing controls

Does Salesforce already prevent the issue?

Does Plauti already detect it?

Is operational review already required?

### 8. Databricks purpose

Is the Databricks rule intended to:

- monitor;
- detect;
- validate Plauti coverage;
- measure trends;
- support root-cause analysis;
- identify an operational queue; or
- test compliance with an agreed standard?

### 9. Action on failure

What happens when the rule produces a result?

Choose one or more:

- correct;
- review;
- merge assessment;
- monitor;
- investigate;
- escalate;
- change an upstream process; or
- no action.

### 10. Ownership

Confirm:

- business owner;
- operational action owner;
- technical owner; and
- escalation owner.

### 11. Caveats

What must a reader know before interpreting the result?

### 12. Decision

Record:

- Approve;
- Refine;
- Validate;
- Park;
- Reject; or
- Supersede.

## Rule worksheet

Complete one worksheet for each rule.

### Rule identification

| Field | Workshop response |
|---|---|
| Rule ID | |
| Rule name | |
| Current Confluence rule ID | |
| Current Plauti scenario | |
| Current Salesforce validation rule | |

### Business definition

| Field | Workshop response |
|---|---|
| Business question | |
| Business expectation | |
| Primary quality dimension | |
| Primary rule type | |
| Business value | |
| Customer impact | |
| Employee impact | |
| Risk impact | |

### Population and logic

| Field | Workshop response |
|---|---|
| Account type | |
| Eligible population | |
| Grain | |
| Attributes | |
| Failure condition | |
| Valid exceptions | |
| Exclusions | |
| Numerator | |
| Denominator | |
| Output unit | |
| Frequency | |

### Control relationship

| Field | Workshop response |
|---|---|
| Salesforce role | |
| Plauti role | |
| Databricks role | |
| Operational review role | |
| Governance role | |
| Root-cause improvement role | |

### Ownership and action

| Field | Workshop response |
|---|---|
| Business owner | |
| Operational action owner | |
| Technical owner | |
| Escalation owner | |
| Action on failure | |
| Target or threshold | |
| Caveats | |

### Decision

| Field | Workshop response |
|---|---|
| Decision | |
| Decision rationale | |
| Definition status | |
| Execution status | |
| Follow-up action | |
| Action owner | |
| Due date | |

## Rule-specific prompts

### CAM-DQ-001 — Minimum valid contact method

Ask:

- Is one valid contact method sufficient?
- Which contact methods qualify?
- Is postal address sufficient?
- Is email required for online account use?
- Are service-specific requirements different?
- Which exceptions are legitimate?
- Should secondary contact details count?
- What action should follow a failed result?

### CAM-DQ-002 — Exact email duplicate signal

Ask:

- Is email normalised before comparison?
- Are primary and secondary email fields compared?
- How are shared household emails handled?
- How are representatives or carers handled?
- Is exact name matching required?
- Is the result a pair or duplicate group?
- Does Plauti already detect the same condition?
- What confirms a true duplicate?

### CAM-DQ-003 — Exact mobile duplicate signal

Ask:

- How is the mobile number normalised?
- Are international formats supported?
- Are phone and mobile fields compared?
- How are shared family numbers handled?
- Is exact name matching required?
- Does Plauti already detect the same condition?
- What confirms a true duplicate?

### CAM-DQ-004 — Organisation ABN completeness

Ask:

- Which organisation types require an ABN?
- Which organisation types are legitimate exceptions?
- Are inactive accounts included?
- Is a blank ABN preventable in Salesforce?
- Who is responsible for correction?
- Is the rule useful without entity-type accuracy?

### CAM-DQ-005 — Organisation ACN completeness

Ask:

- Which legal entity types require an ACN?
- Is an ABN sufficient for some organisations?
- Are government and community organisations excluded?
- Who validates legal entity type?
- Who is responsible for correction?

### CAM-DQ-006 — Repeated ABN duplicate signal

Ask:

- Does repeated ABN always indicate a duplicate?
- Can one legal entity have multiple valid accounts?
- How are branches or service relationships handled?
- Should organisation name also be compared?
- Does Plauti already detect this?
- Is the result a pair or duplicate group?

### CAM-DQ-007 — Repeated ACN duplicate signal

Ask:

- Does repeated ACN always indicate a duplicate?
- Can valid multiple-account structures exist?
- Should organisation name also be compared?
- Does Plauti already detect this?
- Is human review mandatory?
- What confirms a true duplicate?

## Workshop decision record

| Rule ID | Decision | Business owner | Operational owner | Definition status | Next action |
|---|---|---|---|---|---|
| CAM-DQ-001 | | | | | |
| CAM-DQ-002 | | | | | |
| CAM-DQ-003 | | | | | |
| CAM-DQ-004 | | | | | |
| CAM-DQ-005 | | | | | |
| CAM-DQ-006 | | | | | |
| CAM-DQ-007 | | | | | |

## Unresolved questions

| ID | Question | Decision blocked | Owner | Due date | Status |
|---|---|---|---|---|---|
| Q-001 | | | | | Open |

## Risks and caveats

During the workshop, preserve the following distinctions:

- potential duplicate is not confirmed duplicate;
- a flagged record is not the same as a duplicate group;
- completeness does not prove accuracy;
- valid format does not prove authoritative identity;
- Plauti detection does not prove a merge should occur;
- Databricks monitoring does not replace operational review;
- current Salesforce validation does not guarantee historical data compliance;
- a technical result without an action owner is not decision-ready; and
- a rule should not be approved only because it is easy to implement.

## Required outputs after the workshop

Update:

- `02-define/crm-data-quality-rule-register.md`;
- `01-discover/evidence-gaps.md`;
- the Confluence Salesforce Data Quality Rules page;
- the decision log where a material decision was made; and
- Databricks implementation requirements for approved rules.

Do not update technical logic in isolation from the agreed business definition.

## Workshop completion criteria

The workshop is complete when:

- every priority rule has a recorded decision;
- approved rules have a business owner;
- approved rules have an action owner;
- populations and grains are explicit;
- valid exceptions are recorded;
- Plauti alignment is understood for duplicate rules;
- Databricks purpose is explicit;
- unresolved questions have owners; and
- the next implementation or validation action is clear.

## Next action

Confirm workshop participants and pre-populate the seven rule worksheets using the current Confluence and Plauti documentation.
