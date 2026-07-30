# CAM-DQ-001 — Minimum valid contact method

## Document control

| Field | Value |
|---|---|
| Rule ID | CAM-DQ-001 |
| Rule name | Minimum valid contact method |
| Rule group | Person Account contact completeness |
| Status | Draft — business refinement required |
| Validation level | Partially validated |
| Current phase | Define |
| Priority | First refinement cycle |
| Governed metric status | Not ready |
| Last updated | 30 July 2026 |

## Purpose

Define the minimum contact information required for an eligible Person Account to support reliable customer communication and connected customer interactions.

This page separates the business rule from Salesforce controls, Databricks measurement and operational action.

It does not approve a new validation rule, reporting measure or automated remediation process.

## Business question

For which Person Accounts should the organisation expect at least one valid contact method, and what counts as a valid contact method for that population?

## Decision required

Agree:

1. the eligible Person Account population;
2. the accepted contact methods;
3. the validity criteria for each method;
4. legitimate exceptions;
5. whether the rule is preventative, diagnostic or both;
6. what should happen when an account fails the rule; and
7. who owns the rule, remediation process and technical implementation.

## Current working definition

> An eligible Person Account should contain at least one accepted and sufficiently valid contact method unless an approved exception applies.

This is a working definition only.

The following elements remain unresolved:

- eligible population;
- accepted contact methods;
- minimum validity criteria;
- exception categories;
- treatment of inactive or historical accounts;
- treatment of customers who decline contact;
- treatment of inaccessible or unverified contact details; and
- required operational response.

## Why the rule matters

A missing or unusable contact method may:

- prevent service teams from providing updates;
- increase avoidable follow-up effort;
- reduce confidence in customer records;
- contribute to repeated customer contact;
- weaken handovers between channels;
- limit the organisation’s ability to resolve enquiries;
- distort customer account quality reporting; and
- create risks when staff assume that recorded details are current or usable.

A contact detail being present does not necessarily mean that it is valid, current, consented for use or appropriate for a particular communication.

## Eligible population

### Proposed starting population

Person Accounts that are:

- present in the agreed Salesforce account population;
- not identified as test, training or system-generated records;
- not formally excluded through an approved exception;
- within the agreed activity or relevance period; and
- intended to represent a customer who may need to receive service-related communication.

### Population questions

The workshop must determine:

- whether all Person Accounts are included;
- whether inactive or historical accounts are included;
- whether a recent activity period is required;
- how deceased customers are treated;
- how anonymous or identity-limited interactions are treated;
- how records created only for statutory or administrative purposes are treated;
- how test and system records are identified;
- whether merged or superseded records remain in scope; and
- whether different customer or service types require different rules.

## Accepted contact methods

The following are candidates for business validation.

They are not yet approved as interchangeable contact methods.

| Contact method | Candidate status | Questions to resolve |
|---|---|---|
| Email address | Candidate | What syntax, status or verification is required? |
| Mobile telephone | Candidate | What format and usability checks are required? |
| Other telephone | Candidate | Can a landline or alternative number satisfy the rule? |
| Postal address | Unresolved | Does an address count as a contact method or only as location information? |
| Preferred communication channel | Supporting field | Does preference affect whether the underlying detail is valid? |
| Authorised representative details | Unresolved | Can representative details satisfy the customer-account rule? |
| No-contact or declined-contact status | Exception candidate | How must this choice be recorded and reviewed? |

## Contact validity

A value being populated is not sufficient evidence that it is valid.

### Candidate validity dimensions

| Dimension | Description |
|---|---|
| Presence | The field contains a value. |
| Format | The value follows an agreed structural format. |
| Plausibility | The value is not an obvious placeholder, test value or impossible value. |
| Usability | The organisation can reasonably use the method for service communication. |
| Currency | The detail is not known to be outdated or invalid. |
| Consent and preference | Use is consistent with applicable consent, preference and communication rules. |
| Verification | The value has been verified where verification is required. |

The initial rule may use only a subset of these dimensions.

Any simplified logic must be described accurately and must not be labelled as fully valid contact information unless the rule supports that claim.

## Candidate exceptions

Potential exceptions requiring validation include:

- customer has deliberately declined to provide contact information;
- customer has requested no contact through selected methods;
- account is inactive, historical or retained only for records purposes;
- customer is deceased;
- account is a test, training or system record;
- contact occurs only through an authorised representative;
- communication is restricted for legal, safety or privacy reasons;
- the account was created for a transaction that does not require ongoing contact;
- contact information exists in another governed system but is not expected in Salesforce; and
- temporary records awaiting completion or review.

Exceptions must be:

- defined;
- approved;
- identifiable in the source data where possible;
- measurable;
- reviewable; and
- included in the rule version.

## Rule logic — business expression

The rule should be expressed as:

> For the eligible Person Account population, identify accounts that do not contain at least one accepted contact method meeting the agreed minimum validity criteria and that do not have an approved exception.

The business expression must be agreed before detailed technical logic is treated as authoritative.

## Salesforce control

### Potential purpose

Salesforce may prevent selected new or updated Person Accounts from being saved without the agreed minimum contact information.

### Current status

Not confirmed for implementation through this page.

### Questions

- Does an existing Salesforce validation rule already address this scenario?
- Which record types and creation pathways are covered?
- Are integrations, imports or automated processes exempt?
- Would a hard validation rule obstruct legitimate services?
- Should the control apply only at account creation or also at update?
- Can approved exceptions be represented safely?
- Who owns changes to the Salesforce control?
- How will impacts be tested before release?

A Salesforce control should not be proposed until legitimate service and accessibility exceptions are understood.

## Databricks purpose

Databricks may be used to:

- establish an exploratory baseline;
- measure the number and proportion of eligible accounts that fail the agreed rule;
- identify failure patterns by safe operational dimensions;
- monitor trends after improvement activity;
- support root-cause analysis; and
- evaluate whether preventative controls are working.

Databricks should not be treated as the source of the business definition.

## Proposed metric structure

### Metric name

Person Accounts without a minimum valid contact method.

### Metric status

Exploratory only — not governed and not slide-safe.

### Unit

Distinct eligible Person Accounts.

### Proposed numerator

Distinct eligible Person Accounts that:

- do not contain at least one accepted contact method meeting the agreed minimum criteria; and
- do not meet an approved exception.

### Proposed denominator

All distinct eligible Person Accounts after approved population exclusions.

### Proposed rate

`Numerator ÷ denominator × 100`

### Grain

One row or one counted entity per unique Person Account.

### Period

To be agreed.

Possible approaches include:

- current snapshot;
- financial-year-end snapshot;
- monthly snapshot;
- accounts active within an agreed period; or
- accounts created or updated within an agreed period.

The selected period must be explicit because different approaches answer different business questions.

## Denominator safety

The numerator and denominator must use:

- the same Person Account population;
- the same snapshot or activity period;
- the same account identifier;
- the same inclusion and exclusion logic;
- the same rule version; and
- compatible source-table logic.

Do not divide a recent-activity failure count by the total historical Person Account base.

Do not combine account records, contact-point records and customer interactions in one rate without an explicit relationship and compatible grain.

## Source requirements

Before implementation, confirm:

| Requirement | Status |
|---|---|
| Salesforce source object or governed Databricks table | Open |
| Unique Person Account identifier | Open |
| Record-type logic | Open |
| Account-status logic | Open |
| Email fields | Open |
| Mobile and telephone fields | Open |
| Contact preference fields | Open |
| Exception fields or indicators | Open |
| Test and system-record exclusions | Open |
| Activity-date fields | Open |
| Merge or superseded-record treatment | Open |
| Refresh frequency | Open |

Do not record raw customer details or record-level extracts in this repository.

## Failure categories

Where technically feasible, failures should be separated into categories rather than reported as one undifferentiated total.

Candidate categories:

1. no candidate contact field populated;
2. email populated but fails minimum criteria;
3. telephone populated but fails minimum criteria;
4. multiple contact fields populated but none meet minimum criteria;
5. possible exception not consistently recorded;
6. record awaiting review;
7. source or classification issue prevents assessment; and
8. rule cannot be applied because required data is unavailable.

These categories require technical and business validation.

## Operational response

A failed diagnostic rule must have an agreed action pathway.

Possible actions include:

- correct the record during the next legitimate customer interaction;
- assign the record to an operational review queue;
- investigate a recurring upstream creation pathway;
- improve staff guidance;
- improve integration or import controls;
- introduce a preventative Salesforce control;
- record an approved exception; or
- take no action where remediation would be inappropriate or disproportionate.

The rule must not automatically trigger customer contact or record changes without an approved operational process.

## Ownership

| Role | Responsibility | Owner |
|---|---|---|
| Business rule owner | Approves the rule purpose, population and acceptable outcomes | Open |
| Operational owner | Owns review, correction and exception handling | Open |
| Technical owner — Salesforce | Owns preventative or in-platform controls | Open |
| Technical owner — Databricks | Implements and maintains analytical logic | Open |
| Data owner or steward | Confirms data meaning and quality expectations | Open |
| Governance reviewers | Provide privacy, records, security or governance advice where required | Open |

Ownership must be assigned before the rule is moved to governed use.

## Risks

| Risk | Treatment |
|---|---|
| Presence is reported as validity | Name the rule according to the checks it actually performs. |
| Legitimate exceptions are treated as defects | Define and test exception logic before governed reporting. |
| Historical accounts distort the baseline | Agree the population and period before calculation. |
| Different contact fields use inconsistent standards | Record method-specific criteria. |
| Operational teams receive an unactionable failure list | Agree ownership, prioritisation and response pathways. |
| A Salesforce validation rule blocks legitimate service access | Test service, accessibility and exception scenarios first. |
| Customer details are copied into GitHub | Store only definitions, summaries, caveats and decision logic. |
| The metric is used as a customer-growth measure | Label it as an account-quality diagnostic only. |

## Workshop decision record

| Decision | Outcome | Owner | Date | Status |
|---|---|---|---|---|
| Eligible Person Account population |  |  |  | Open |
| Accepted contact methods |  |  |  | Open |
| Minimum validity criteria |  |  |  | Open |
| Approved exceptions |  |  |  | Open |
| Measurement period |  |  |  | Open |
| Salesforce control purpose |  |  |  | Open |
| Databricks diagnostic purpose |  |  |  | Open |
| Operational response |  |  |  | Open |
| Business owner |  |  |  | Open |
| Operational owner |  |  |  | Open |
| Technical owners |  |  |  | Open |
| Governed-use approval |  |  |  | Open |

## Definition of Ready

The rule is ready for governed technical implementation only when:

- the business question is agreed;
- the eligible population is explicit;
- accepted contact methods are agreed;
- validity criteria are documented;
- exceptions are approved;
- source fields and grain are confirmed;
- numerator and denominator are compatible;
- rule ownership is assigned;
- operational action is agreed;
- privacy, records, security and governance needs have been considered;
- test cases include valid, invalid and exception scenarios;
- rule versioning is established;
- permitted uses are documented; and
- the decision is recorded in the decision log.

## Current assessment

**Status:** Technically definable but not ready for governed implementation.

**Reason:** The eligible population, accepted contact methods, validity criteria, exceptions, owners and operational response have not yet been agreed.

**Slide-safe wording:** Not available.

**Permitted current use:** Workshop preparation and exploratory rule refinement only.

## Related repository pages

- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `02-define/crm-data-quality-rule-refinement-workshop.md`
- `02-define/problem-statement.md`
- `01-discover/evidence-gaps.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`
