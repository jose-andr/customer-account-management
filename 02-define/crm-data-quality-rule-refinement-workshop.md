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

Use the following sources during the workshop:

### Salesforce data-quality rule inventory

[Salesforce Data Quality Rules](https://jira-cityofmelbourne.atlassian.net/wiki/spaces/DP/pages/527597570/Salesforce+Data+Quality+Rules)

This remains the working source of truth for:

- current rule IDs;
- rule descriptions;
- technical logic;
- active and parked status;
- contacts; and
- implementation notes.

### Plauti configuration

`Plauti Duplicate Check Configuration`

Use this source to confirm:

- existing duplicate scenarios;
- matching fields;
- record types;
- cross-object behaviour;
- merge permissions;
- result fields; and
- scheduled duplicate jobs.

### Repository working pages

- `01-discover/evidence-gaps.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `01-discover/current-state-evidence-synthesis.md`

### Current-state operations

Use:

`jose-andr/cx-current-state-sop-mapping`

to validate how duplicate review, correction, escalation and merge decisions currently occur.

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
