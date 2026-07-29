# CRM data-quality rule refinement

Status: In progress  
Owner: José Andrade  
Current stage: Define  
Last updated: 29 July 2026

## Purpose

This page supports the business refinement of Salesforce CRM data-quality rules before they are implemented, scheduled or reported through Databricks.

The refinement activity will ensure each rule is:

- tied to a clear business question;
- defined in plain language;
- scoped to the correct customer population;
- technically implementable;
- safe to interpret;
- owned by an appropriate business role;
- prioritised according to customer, operational and risk impact; and
- suitable for trend reporting or operational action.

The current rule inventory is a starting point.

It contains a mixture of:

- agreed business concerns;
- draft rules;
- active checks;
- parked rules;
- incomplete technical logic;
- unresolved field questions;
- proposed future checks; and
- existing Salesforce validation rules.

These must be refined before the outputs are treated as governed measures.

## Refinement objective

The immediate objective is to produce a prioritised set of business-approved CRM data-quality rules for Databricks.

Each refined rule should answer:

1. What business problem does this rule detect?
2. Which records should be assessed?
3. What condition represents a failure?
4. What condition is acceptable?
5. What action should follow a failed result?
6. Who owns the rule?
7. How frequently should it run?
8. How should the result be interpreted?
9. What caveats apply?
10. Is the result suitable for reporting, operational review or both?

## Business refinement principles

### Decision first

Every rule must support a business decision or operational action.

Do not retain a rule only because the field is available.

### Business meaning before SQL

Agree the business definition before finalising technical logic.

The technical query should implement the rule, not define it.

### Correct population

Each rule must clearly state the records it applies to.

Examples include:

- active person accounts;
- all person accounts;
- active organisation accounts;
- organisation accounts with an ABN;
- accounts created during a reporting period;
- accounts assessed by a specific matching rule.

### Denominator safety

Where a percentage or rate is required, define the denominator explicitly.

The numerator and denominator must use:

- the same population;
- the same reporting period;
- compatible filters;
- the same record grain; and
- the same rule version.

### Potential is not confirmed

Records identified by matching logic are potential duplicates.

They must not be labelled as confirmed duplicates until reviewed through the agreed operational process.

### Prevention and remediation

Rules should distinguish between:

- defects prevented by Salesforce validation;
- defects detected after creation;
- records requiring operational remediation; and
- patterns indicating an upstream process or system issue.

### Human in the loop

Rules may identify possible issues.

Humans remain responsible for decisions involving:

- record merging;
- identity confirmation;
- sensitive data;
- conflicting evidence;
- customer relationships; and
- privacy or records implications.

## Required fields for each rule

| Field | Required definition |
|---|---|
| Rule ID | Stable identifier |
| Rule name | Short business-readable name |
| Business question | The decision question the rule supports |
| Business description | Plain-English statement of expected data quality |
| Quality dimension | Completeness, validity, uniqueness, consistency, accuracy or timeliness |
| Customer/account type | Person, organisation or other defined population |
| Source | Salesforce or relevant source domain |
| Dataset | Databricks table or view |
| Grain | One row per account, contact, duplicate group or other unit |
| Attributes | Fields assessed by the rule |
| Population filter | Records included in the assessment |
| Failure condition | Logic that causes the record to fail |
| Exclusions | Records intentionally excluded |
| Numerator | Count of failing records or groups |
| Denominator | Eligible population where a rate is required |
| Output unit | Records, accounts, groups, percentage or rate |
| Frequency | Daily, weekly, monthly or other agreed schedule |
| Priority | Business priority |
| Severity | Consequence of failure |
| Business owner | Role accountable for the rule |
| Operational owner | Role responsible for reviewing or acting on results |
| Technical owner | Role responsible for implementation and maintenance |
| Action on failure | Review, correct, monitor, escalate or investigate |
| Target or threshold | Expected tolerance, where agreed |
| Caveats | Known limitations |
| Definition status | Current refinement status |
| Execution status | Current implementation status |

## Quality dimensions

Use one primary quality dimension for each rule.

| Dimension | Meaning |
|---|---|
| Completeness | Required information is populated |
| Validity | Information follows an agreed format or domain rule |
| Uniqueness | Records are not duplicated according to the stated rule |
| Consistency | Related fields or records do not conflict |
| Accuracy | Information reflects an authoritative or verified source |
| Timeliness | Information is current or updated within the required period |

A rule may relate to more than one dimension, but one should be nominated as primary.

## Rule refinement workflow

### Step 1 — Group the current rules

Group existing rules into:

- person-account completeness;
- person-account validity;
- person-account duplicate signals;
- organisation-account completeness;
- organisation-account validity;
- organisation-account duplicate signals;
- cross-field consistency;
- external verification;
- case and work-order quality; and
- existing Salesforce preventative controls.

Customer Account Management should initially prioritise account and customer-identity rules.

Case and work-order rules should remain separate unless they directly support the Customer Account Management problem.

### Step 2 — Confirm the business question

Rewrite each rule as a decision-relevant question.

Example:

Current wording:

> How many person accounts do not contain an email?

Refined business question:

> What proportion of active person accounts do not have a primary email address, and does this limit account communication or self-service?

### Step 3 — Confirm the population

Agree:

- account type;
- active or inactive status;
- record type;
- date range;
- required exclusions;
- test or system records;
- deceased customers;
- historical records; and
- records subject to legal or operational exceptions.

### Step 4 — Confirm the business rule

State what good data looks like.

Example:

> An active person account should contain at least one usable contact method unless an approved exception applies.

This may be more appropriate than treating every missing email as a defect.

### Step 5 — Confirm the technical rule

Work with the technical owner to confirm:

- source table or view;
- field names;
- joins;
- null handling;
- whitespace handling;
- case sensitivity;
- formatting;
- matching thresholds;
- duplicate grouping logic;
- exclusions; and
- expected output.

### Step 6 — Confirm actionability

For every failed result, determine:

- whether a person should review it;
- whether it can be corrected safely;
- whether it should be monitored only;
- whether it indicates an upstream defect;
- whether it should be escalated; and
- whether the result is useful enough to justify running the rule.

### Step 7 — Confirm ownership

Assign:

- business owner;
- operational action owner;
- technical implementation owner; and
- governance or escalation owner where required.

Do not activate a rule without an owner for its results.

### Step 8 — Set priority

Prioritise rules using:

- customer impact;
- privacy or security risk;
- operational effort;
- regulatory or records impact;
- effect on connected interactions;
- volume;
- recurrence;
- ease of remediation; and
- readiness for implementation.

### Step 9 — Test the rule

Test against a controlled sample or approved aggregate output.

Confirm:

- the result matches the business definition;
- expected records are included;
- false positives are understood;
- false negatives are considered;
- the rule can be explained;
- the output unit is clear; and
- the result leads to an action or decision.

### Step 10 — Approve for implementation

A rule is ready for Databricks when:

- the business question is agreed;
- population and exclusions are explicit;
- the failure condition is testable;
- ownership is assigned;
- caveats are documented;
- the expected action is clear;
- the output unit is defined; and
- the rule has been approved by the relevant business owner.

## Initial rule groups for refinement

### Group 1 — Person-account contact completeness

Current rules include:

- no primary email;
- secondary email populated but primary email blank;
- no primary mobile;
- secondary phone populated but primary mobile blank; and
- minimum contact information missing.

Questions to resolve:

- Is an email mandatory for every person account?
- Is a mobile number mandatory for every person account?
- Is one valid contact method sufficient?
- Are there approved exceptions?
- Should secondary fields be promoted to primary?
- Are inactive accounts included?
- What customer or service impact follows from missing details?

### Group 2 — Person-account field validity

Current rules include:

- mobile number length;
- special characters in names;
- future birth date; and
- incomplete address information.

Questions to resolve:

- Are international mobile numbers permitted?
- Which characters are valid in personal names?
- How should hyphens, apostrophes, spaces and diacritics be handled?
- Is address completeness required for every customer?
- Which validation rules already prevent these defects in Salesforce?
- Are historical records expected to comply?

### Group 3 — Potential person-account duplicates

Current rules include combinations of:

- exact email;
- secondary email;
- exact mobile;
- phone;
- exact name; and
- greater than 90% name similarity.

Questions to resolve:

- What is the unit of output: records, pairs or duplicate groups?
- Which fields provide sufficient matching confidence?
- Is 90% name similarity appropriate?
- How are common names handled?
- How are shared email addresses or phone numbers handled?
- How are families, carers and representatives handled?
- Which matches require human review?
- What makes a duplicate confirmed rather than potential?
- Should each matching scenario have a separate rule ID?

### Group 4 — Organisation-account completeness and validity

Current rules include:

- missing ABN;
- missing ACN;
- ABN length;
- proposed ACN length;
- ACN comparison with the final nine digits of ABN; and
- proposed external verification.

Questions to resolve:

- Which organisation types require an ABN?
- Which organisation types require an ACN?
- Can an account legitimately have one but not the other?
- Are inactive organisations included?
- Which external source is authoritative?
- What should happen when Salesforce and the authoritative source differ?
- Is external verification technically and legally approved?

### Group 5 — Potential organisation duplicates

Current rules include repeated:

- ABN;
- ACN;
- organisation name; and
- trading name.

Questions to resolve:

- Does the same ABN always indicate a duplicate?
- Can one legal entity have multiple valid account records?
- Can multiple entities share a trading name?
- Should names be normalised before comparison?
- How should branches, subsidiaries and departments be represented?
- What relationship model is required instead of merging some records?

## Initial business review order

Refine the rules in this order:

1. person-account contact completeness;
2. exact person-account email duplicates;
3. exact person-account mobile duplicates;
4. organisation ABN and ACN completeness;
5. organisation ABN and ACN duplicates;
6. person-account fuzzy-name matching;
7. organisation-name and trading-name duplicates;
8. external ABN and ACN verification;
9. remaining format and cross-field consistency rules.

This order begins with rules that are easier to explain and test before moving into higher-risk fuzzy matching and external verification.

## Rule-refinement register

| Rule group | Business owner | Technical support | Status | Next action |
|---|---|---|---|---|
| Person-account contact completeness | To confirm | Databricks / CRM | Open | Agree minimum valid contact requirement |
| Person-account field validity | To confirm | Databricks / CRM | Open | Confirm accepted phone and name formats |
| Person-account duplicate signals | To confirm | Databricks / CRM | Open | Define potential versus confirmed duplicate |
| Organisation-account completeness | To confirm | Databricks / CRM | Open | Confirm when ABN and ACN are required |
| Organisation-account validity | To confirm | Databricks / CRM | Open | Confirm format and external verification rules |
| Organisation-account duplicate signals | To confirm | Databricks / CRM | Open | Confirm legal-entity and relationship rules |
| Case and work-order rules | Outside initial account focus | Databricks / CRM | Parked | Review separately with service owners |

## Definition-of-ready checklist

A rule is ready for technical implementation when all answers are yes.

| Check | Yes / No |
|---|---|
| Is the business question clear? | |
| Is the rule linked to a decision or action? | |
| Is the customer or account population explicit? | |
| Is the record grain explicit? | |
| Is the failure condition agreed? | |
| Are exclusions documented? | |
| Are numerator and denominator defined where required? | |
| Is the output unit clear? | |
| Is the business owner assigned? | |
| Is the action owner assigned? | |
| Are privacy and governance implications understood? | |
| Have false positives and false negatives been considered? | |
| Are caveats documented? | |
| Has the rule been tested on safe data or aggregate outputs? | |
| Has the business owner approved implementation? | |

## Outputs from the refinement activity

The business refinement should produce:

- a prioritised CRM data-quality rule register;
- agreed business definitions;
- confirmed populations and exclusions;
- approved rule ownership;
- clear technical implementation requirements;
- agreed execution frequency;
- safe measure definitions;
- operational response expectations;
- a list of parked or rejected rules; and
- a decision on which rules enter the first Databricks implementation cycle.

## Current decision

The business will refine and approve the CRM data-quality rules before treating Databricks outputs as governed measures.

The first refinement session should focus on:

1. minimum contact information for active person accounts;
2. exact email duplicate rules;
3. exact mobile duplicate rules;
4. ABN and ACN requirements; and
5. the distinction between potential and confirmed duplicates.

## Next action

Schedule a business rule-refinement session with:

- Customer Focus and Strategy;
- CRM Product Ownership;
- Customer Data and Systems Support;
- Databricks or Data Governance technical support; and
- Privacy or Data Governance representatives where required.

Use the session to complete the Definition-of-ready checklist for the first five rule areas.
