# CRM data-quality rule refinement

Status: In progress  
Owner: José Andrade  
Current stage: Define  
Last updated: 29 July 2026

## Purpose

This page supports the business refinement of CRM data-quality rules before they are implemented, scheduled or used as governed measures.

The refinement activity must align:

- Salesforce validation rules;
- Plauti duplicate-detection scenarios;
- Databricks analytical data-quality rules;
- operational duplicate-review practices;
- business ownership;
- customer and employee impacts; and
- governance requirements.

The objective is not to create more rules.

The objective is to create a smaller, clearer and decision-relevant set of rules that work together as one controlled account-quality system.

## Source material

Use the following sources together during business-rule refinement.

Each source has a different role.

No single source is sufficient to approve a business rule, governed metric or operational control.

### Salesforce data-quality rule inventory

The current working rule inventory is maintained in Confluence:

[Salesforce Data Quality Rules](https://jira-cityofmelbourne.atlassian.net/wiki/spaces/DP/pages/527597570/Salesforce+Data+Quality+Rules)

This page remains the working source of truth for:

- current rule IDs;
- draft business descriptions;
- technical logic;
- rule priorities;
- active and parked status;
- source fields;
- implementation notes;
- contacts; and
- ongoing rule changes.

The Confluence inventory does not by itself establish that a rule has:

- an approved business definition;
- an agreed eligible population;
- a safe numerator and denominator;
- an operational owner;
- a governed permitted use; or
- reporting approval.

### Databricks customer data-quality pilot

Use:

`../01-discover/databricks-customer-data-quality-pilot-input.md`

This page records the initial Databricks rule execution and Power BI dashboard as exploratory evidence.

Use the pilot to examine:

- rules already tested;
- source tables shown;
- visible attributes and rule types;
- similarity thresholds;
- preliminary rule-pass results;
- page-total discrepancies;
- possible grain and denominator issues;
- rule-taxonomy issues;
- Account and Contact population compatibility;
- candidate technical defects; and
- questions requiring business or technical validation.

The pilot may be used for:

- business-rule refinement;
- workshop preparation;
- technical-logic review;
- source-field validation;
- denominator investigation;
- pilot-to-rule comparison; and
- prioritisation of further analysis.

The pilot must not currently be used to:

- claim an overall governed customer data-quality score;
- report confirmed duplicate rates;
- establish performance targets;
- compare teams or services;
- approve automated remediation;
- make customer-level decisions; or
- present executive measures without further validation.

The displayed aggregate rule-pass rate of approximately 95.9% remains exploratory.

### Detailed priority-rule definitions

Use the following pages as the primary business-definition artefacts for the first refinement cycle.

#### Person Account rules

- `rules/CAM-DQ-001-minimum-valid-contact-method.md`
- `rules/CAM-DQ-002-exact-email-duplicate-signal.md`
- `rules/CAM-DQ-003-exact-mobile-duplicate-signal.md`

#### Organisation Account rules

- `rules/CAM-DQ-004-abn-completeness.md`
- `rules/CAM-DQ-005-acn-completeness.md`
- `rules/CAM-DQ-006-repeated-abn.md`
- `rules/CAM-DQ-007-repeated-acn.md`

Each detailed rule page records:

- business question;
- purpose;
- current working definition;
- eligible-population questions;
- candidate exclusions;
- legitimate exceptions;
- proposed numerator and denominator;
- grain and output-unit questions;
- Salesforce, Plauti and Databricks responsibilities;
- operational-response requirements;
- ownership gaps;
- risks;
- Definition of Ready;
- current permitted use; and
- workshop decisions.

These pages are draft refinement artefacts.

They are not approved business rules.

### CRM data-quality rule register

Use:

`crm-data-quality-rule-register.md`

The register is the portfolio-level control page for:

- rule status;
- priority;
- detailed rule links;
- pilot-to-rule mapping;
- technical-execution status;
- governed-use status;
- shared refinement decisions;
- workshop decisions;
- ownership; and
- first-cycle completion criteria.

Update the register after each material rule decision.

Do not duplicate the complete rule definition in the register.

### CRM data-quality rule refinement index

Use:

`crm-data-quality-rule-refinement-index.md`

The index provides:

- the first-cycle rule set;
- common population decisions;
- shared grain and denominator requirements;
- rule-taxonomy guidance;
- duplicate terminology;
- tool boundaries;
- pilot findings requiring refinement;
- refinement sequence; and
- definition of completion.

Use the index to keep decisions consistent across the seven individual rules.

### Plauti duplicate-check configuration

The existing Plauti configuration is documented in Confluence:

`Plauti Duplicate Check Configuration`

The documented configuration includes:

- Person Account duplicate detection;
- Organisation Account duplicate detection;
- matching scenarios;
- record-type applicability;
- cross-object configuration;
- duplicate result fields;
- merge permissions;
- scheduled jobs; and
- fields presented during duplicate review.

The current production configuration still requires validation.

Confirm:

- active scenarios;
- fields used;
- exact and fuzzy matching logic;
- normalisation;
- thresholds;
- cross-object behaviour;
- real-time and scheduled checks;
- result fields;
- review statuses;
- merge permissions;
- override behaviour;
- exception handling;
- output volumes; and
- false-positive patterns.

Do not assume that Databricks should reproduce Plauti logic.

The tools may support different purposes.

### Salesforce controls

Confirm current Salesforce validation, matching and duplicate-management behaviour before proposing new controls.

For each rule, identify:

- current validation rules;
- current duplicate rules;
- account-search prompts;
- warning or blocking behaviour;
- create and update coverage;
- integration and import coverage;
- override permissions;
- exception handling;
- known operational impacts; and
- current ownership.

Do not recommend a new validation or duplicate rule until the existing control and legitimate exceptions are understood.

### Current-state operational evidence

Detailed current operational practice remains in:

`jose-andr/cx-current-state-sop-mapping`

Use that repository to validate:

- how account search currently occurs;
- how potential duplicates are identified;
- how records are reviewed;
- how merge decisions are made;
- which exceptions occur;
- what workarounds exist;
- where decisions are recorded;
- what risks staff manage;
- where individual knowledge is required;
- how corrections are made; and
- how issues are escalated.

The current-state repository documents actual or reported operational practice.

Do not replace current-state evidence with proposed role scope, future governance or aspirational operating-model assumptions.

### Supporting repository pages

Use where relevant:

- `../01-discover/evidence-gaps.md`
- `../01-discover/current-state-evidence-synthesis.md`
- `../01-discover/existing-evidence-inventory.md`
- `../00-project-control/assumptions-log.md`
- `../00-project-control/risk-register.md`
- `../00-project-control/status-and-validation-model.md`
- `crm-data-quality-rule-refinement-workshop.md`
- `../06-decisions/decision-log.md`

### Source hierarchy

Use the following hierarchy for refinement decisions:

| Decision need | Primary source |
|---|---|
| Current technical rule inventory | Salesforce Data Quality Rules Confluence page |
| Initial analytical results | Databricks pilot evidence and governed analytical environment |
| Current Salesforce control | Live Salesforce configuration |
| Current duplicate configuration | Live Plauti configuration |
| Current operational practice | Current-state SOP repository and operational representatives |
| Draft business definition | Individual rule page |
| Rule portfolio status | CRM data-quality rule register |
| Shared refinement standards | CRM data-quality rule refinement index |
| Approved project decision | Decision log |
| Original customer or operational data | Approved organisational system of record |

Where sources conflict:

1. record the contradiction;
2. do not resolve it through assumption;
3. assign a validation owner;
4. identify the required evidence;
5. keep the rule in refinement or validation status;
6. update the relevant risk or assumption where necessary; and
7. update the rule page only after the source has been confirmed.

### Evidence handling

Do not bring raw customer records into GitHub or the general workshop pack.

Use:

- aggregate results;
- field names;
- rule descriptions;
- de-identified examples;
- synthetic examples;
- masked values;
- safe screenshots;
- controlled demonstrations in approved systems; and
- source references.

Do not place the following in GitHub:

- customer names;
- customer email addresses;
- telephone numbers;
- ABNs or ACNs tied to identifiable records;
- CRM record identifiers;
- failed-record extracts;
- unredacted screenshots;
- credentials;
- access tokens; or
- sensitive operational data.## Control-system model

CRM account quality currently involves several different controls.

| Control | Primary purpose |
|---|---|
| Salesforce validation rules | Prevent invalid or incomplete data from being entered |
| Plauti Duplicate Check | Identify potential duplicate records and support operational review |
| Databricks data-quality rules | Measure account-quality conditions, trends and recurring patterns |
| Operational review | Confirm identity, assess risk and decide whether action is safe |
| Governance and ownership | Define standards, accountabilities, thresholds and escalation |
| Root-cause improvement | Reduce the processes and system behaviours creating defects |

These controls should complement each other.

They should not be treated as interchangeable.

## Refinement objective

The immediate objective is to produce a prioritised set of business-approved CRM data-quality rules.

Each refined rule must answer:

1. What business problem does the rule detect?
2. Which control should own the issue?
3. Which records are assessed?
4. What condition represents failure?
5. What valid exceptions apply?
6. What action follows a failed result?
7. Who owns the rule and its outcomes?
8. How often should the rule run?
9. How should the result be interpreted?
10. What caveats or risks apply?

## Rule types

Each rule should be assigned one primary type.

| Rule type | Purpose |
|---|---|
| Preventative | Stops invalid data being created or saved |
| Detective | Identifies an issue after creation |
| Monitoring | Tracks quality or trends over time |
| Investigative | Supports root-cause analysis |
| Operational | Creates a review or remediation action |
| Governance | Tests compliance with an approved standard |

A single business issue may require more than one rule type.

For example:

- Salesforce may prevent an invalid format;
- Plauti may identify a potential duplicate;
- Databricks may monitor duplicate signals over time; and
- an officer may determine whether two records should be merged.

## Required rule definition

Each rule must include:

| Field | Required definition |
|---|---|
| Rule ID | Stable identifier |
| Rule name | Short business-readable name |
| Business question | Decision or action supported |
| Business description | Plain-English quality expectation |
| Rule type | Preventative, detective, monitoring, investigative, operational or governance |
| Quality dimension | Completeness, validity, uniqueness, consistency, accuracy or timeliness |
| Account type | Person, organisation or another defined population |
| Source | Salesforce or relevant source domain |
| Dataset | Databricks table or view where applicable |
| Grain | Account, record, pair, group or another unit |
| Attributes | Fields assessed |
| Population filter | Eligible records |
| Failure condition | Logic that causes failure |
| Valid exceptions | Accepted conditions that should not fail |
| Exclusions | Records intentionally omitted |
| Numerator | Failing records or groups |
| Denominator | Eligible population where a rate is used |
| Output unit | Records, pairs, groups, percentage or rate |
| Frequency | Execution schedule |
| Priority | Business importance |
| Severity | Consequence of failure |
| Business owner | Accountable for the rule |
| Operational owner | Responsible for action |
| Technical owner | Responsible for implementation |
| Action on failure | Review, correct, monitor, escalate or investigate |
| Threshold | Tolerance where agreed |
| Caveats | Known limitations |
| Definition status | Business refinement status |
| Execution status | Technical implementation status |

## Rule statuses

### Definition status

| Status | Meaning |
|---|---|
| Proposed | Initial business question or idea |
| In refinement | Business meaning, scope or ownership is incomplete |
| Ready for implementation | Business definition is complete and approved |
| Parked | Not progressing due to dependency or low value |
| Rejected | Reviewed and not required |
| Superseded | Replaced by another rule |

### Execution status

| Status | Meaning |
|---|---|
| Not started | No implementation work has begun |
| In development | Logic is being created |
| Implemented | Logic exists but may not be scheduled |
| Scheduled | Rule runs at an agreed frequency |
| Results under review | Outputs exist but are not governed |
| Validated | Rule and outputs are approved for the stated use |
| Failed | Rule cannot currently execute reliably |
| Retired | Rule is no longer active |

## Initial refinement scope

The first refinement cycle should focus on Customer Account Management rules only.

### Included

- Person Account contact completeness;
- Person Account field validity;
- potential Person Account duplicates;
- organisation-account completeness;
- organisation identifier validity;
- potential organisation duplicates;
- matching and merge controls; and
- account-quality monitoring.

### Parked for separate review

- case-description quality;
- case subject requirements;
- work-order subject requirements;
- knowledge-article attachment;
- call-recording attachment;
- location-description quality;
- work-order-to-enquiry matching; and
- other service-specific case controls.

These may be important CRM quality issues, but they are not all Customer Account Management rules.

## Initial rule groups

### 1. Person Account contact completeness

Current rule signals include:

- no primary email;
- secondary email populated while primary email is blank;
- no primary mobile;
- secondary phone populated while primary mobile is blank; and
- no usable contact method.

Business decisions required:

- Is an email mandatory?
- Is a mobile number mandatory?
- Is one valid contact method sufficient?
- Which account types require particular contact methods?
- What valid exceptions apply?
- Should inactive accounts be included?
- Should secondary values be promoted or reported only?
- What action follows a failed result?

### 2. Person Account field validity

Current rule signals include:

- mobile-number length;
- unexpected name characters;
- future birth dates; and
- incomplete address information.

Business decisions required:

- Are international phone numbers supported?
- Which characters are valid in names?
- How are apostrophes, hyphens, spaces and diacritics handled?
- When is an address mandatory?
- Which defects are already prevented in Salesforce?
- Should historical records be assessed against current standards?

### 3. Potential Person Account duplicates

Current rule signals include combinations of:

- exact email;
- secondary email;
- exact mobile;
- phone;
- exact name; and
- greater than 90% name similarity.

Business decisions required:

- Is the output a record, pair or duplicate group?
- Which matching fields provide sufficient confidence?
- Is 90% name similarity appropriate?
- How are common names handled?
- How are shared contact details handled?
- How are families, representatives and carers handled?
- Which results require human review?
- What makes a duplicate confirmed?
- How do proposed Databricks rules differ from Plauti scenarios?

### 4. Organisation-account completeness

Current rule signals include:

- missing ABN;
- missing ACN;
- missing organisation name; and
- missing trading name where relevant.

Business decisions required:

- Which organisation types require an ABN?
- Which require an ACN?
- Can one identifier be sufficient?
- Are inactive organisations included?
- Are branches, departments or informal groups treated differently?
- What action follows missing information?

### 5. Organisation-account validity

Current rule signals include:

- ABN length;
- ACN length;
- ACN-to-ABN consistency; and
- external verification.

Business decisions required:

- Which source is authoritative?
- Is external verification approved?
- How often should verification occur?
- What happens when Salesforce and the source differ?
- Are format rules enough without external verification?
- Who owns correction?

### 6. Potential organisation duplicates

Current rule signals include repeated:

- ABN;
- ACN;
- organisation name; and
- trading name.

Business decisions required:

- Does a repeated ABN always mean a duplicate?
- Can one legal entity have multiple valid accounts?
- Can multiple entities share a trading name?
- How should names be normalised?
- How are branches and subsidiaries represented?
- When should accounts be related rather than merged?

## Plauti-to-Databricks comparison

Each duplicate rule must be compared with current Plauti behaviour.

| Rule area | Plauti configuration | Databricks purpose | Business decision |
|---|---|---|---|
| Exact email and exact name | To validate | Monitor or independently detect | Confirm whether duplicate logic is intentionally repeated |
| Exact email and similar name | To validate | Measure potential duplicates | Confirm similarity threshold |
| Exact mobile and exact name | To validate | Monitor potential duplicate patterns | Confirm shared-number exceptions |
| Exact mobile and similar name | To validate | Investigate possible duplicates | Confirm acceptable false positives |
| Repeated ABN | To validate | Monitor organisation duplicate signals | Confirm whether repeated ABN is always invalid |
| Repeated ACN | To validate | Monitor organisation duplicate signals | Confirm legal-entity rules |
| Repeated organisation name | To validate | Investigate possible duplicates | Confirm normalisation |
| Repeated trading name | To validate | Investigate possible duplicates | Confirm acceptable shared names |

## Refinement workflow

### Step 1 — Confirm the business question

Rewrite each rule as a decision-relevant question.

Example:

Current wording:

> How many person accounts do not contain an email?

Refined wording:

> What proportion of active Person Accounts have no usable email address, and which customer interactions are affected?

### Step 2 — Identify the correct control

Decide whether the issue should be handled through:

- Salesforce prevention;
- Plauti detection;
- Databricks monitoring;
- operational review;
- governance;
- root-cause improvement; or
- a combination.

### Step 3 — Confirm the population

Agree:

- account type;
- active or inactive status;
- record type;
- reporting period;
- exclusions;
- test records;
- historical records; and
- approved exceptions.

### Step 4 — Confirm the grain

State whether the rule produces:

- one row per account;
- one row per failed field;
- one row per matched pair;
- one row per duplicate group; or
- another clearly defined unit.

### Step 5 — Confirm good data

State the expected business condition in plain language.

Example:

> An active Person Account should contain at least one usable contact method unless an approved exception applies.

### Step 6 — Confirm technical logic

Confirm:

- source table or view;
- field names;
- joins;
- null handling;
- whitespace handling;
- case sensitivity;
- normalisation;
- similarity thresholds;
- grouping logic; and
- exclusions.

### Step 7 — Confirm actionability

For each failure, decide whether the response is:

- correct the record;
- review the potential duplicate;
- monitor the trend;
- investigate the source;
- escalate a risk;
- change an upstream process; or
- take no action.

Do not implement rules that create results with no owner or action.

### Step 8 — Assign ownership

Confirm:

- business owner;
- operational action owner;
- technical owner;
- governance owner where required; and
- escalation pathway.

### Step 9 — Test and review

Test the rule using safe data or approved aggregate outputs.

Review:

- expected matches;
- false positives;
- possible false negatives;
- edge cases;
- explainability;
- output grain;
- operational effort; and
- privacy implications.

### Step 10 — Approve or park

The business owner should decide whether the rule is:

- ready for implementation;
- returned for refinement;
- parked;
- rejected; or
- superseded.

## Metric-safety rules

A Databricks output is not automatically a governed measure.

Before use, record:

- business question;
- rule version;
- source;
- dataset;
- grain;
- population;
- numerator;
- denominator;
- exclusions;
- reporting period;
- execution date;
- result;
- caveats;
- validation owner; and
- permitted use.

Potential duplicate matches must not be described as confirmed duplicates.

Flagged records must not be mixed with matched pairs or duplicate groups.

Rules using different populations or thresholds must not be combined without explicit caveats.

## Definition of ready

A rule is ready for technical implementation when:

| Check | Complete |
|---|---|
| Business question is clear | |
| Control purpose is agreed | |
| Account population is explicit | |
| Grain is explicit | |
| Failure condition is agreed | |
| Valid exceptions are documented | |
| Exclusions are documented | |
| Numerator and denominator are defined | |
| Output unit is clear | |
| Business owner is assigned | |
| Operational owner is assigned | |
| Technical owner is assigned | |
| Action on failure is clear | |
| Privacy and governance implications are understood | |
| False positives have been considered | |
| False negatives have been considered | |
| Rule has been tested | |
| Business owner has approved implementation | |

## First refinement workshop

The first workshop should focus on:

1. minimum valid contact information for active Person Accounts;
2. exact email duplicate signals;
3. exact mobile duplicate signals;
4. ABN and ACN completeness;
5. ABN and ACN duplicate signals; and
6. potential versus confirmed duplicates.

Suggested participants:

- Customer Focus and Strategy;
- CRM Product Owner;
- Customer Data and Systems Support Officer;
- Databricks or Data Governance technical support;
- Privacy or Data Governance representative where required; and
- operational users who review or merge duplicate records.

## Required workshop outputs

The session should produce:

- refined business definitions;
- agreed populations;
- agreed grain;
- valid exceptions;
- ownership;
- intended control type;
- action on failure;
- implementation priority;
- Plauti alignment;
- unresolved questions; and
- a decision for each rule.

## Current decision

The business will refine and approve CRM data-quality rules before Databricks outputs are treated as governed evidence.

Databricks rules must be designed in relation to:

- Salesforce preventative controls;
- Plauti duplicate detection;
- operational human review;
- governance requirements; and
- root-cause improvement.

## Next action

Prepare the first six priority rules using the Definition of Ready checklist and bring them to the business refinement workshop.
