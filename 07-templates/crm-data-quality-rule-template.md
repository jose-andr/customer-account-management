# CRM data-quality rule template

## How to use this template

Use this template when a proposed CRM data-quality rule needs a decision-ready business definition.

Create a separate rule page only when:

- a clear business question exists;
- the rule is relevant to a current decision or operating need;
- the source field or data pattern is known;
- the rule is sufficiently distinct from existing rules; and
- documenting it will support refinement, implementation or governance.

Do not create a rule page only because a technical check is possible.

Replace all instructional text and placeholders before moving the rule beyond draft status.

## Document control

| Field | Value |
|---|---|
| Rule ID | `CAM-DQ-###` |
| Rule name | `[Plain-English rule name]` |
| Rule group | `[Rule family]` |
| Business-rule status | Draft — business refinement required |
| Evidence-validation status | `[Observed / Partially validated / Validated for exploratory use / Governed evidence]` |
| Technical status | `[Not started / In development / Implemented / Scheduled / Results under review / Technically validated]` |
| Operational-readiness status | `[Not assessed / Response undefined / Response in design / Operational pathway agreed / Operationally validated / Operational use approved]` |
| Governed-use status | `[Not ready / Exploratory only / Governed for diagnostic use / Governed for operational review / Governed for preventative control / Approved for reporting]` |
| Metric-readiness status | `[Not applicable / Technically calculated / Definition incomplete / Calculation under validation / Diagnostic-ready / Operationally ready / Reporting-ready / Not safe]` |
| Current phase | Define |
| Priority | `[Critical / High / Medium / Low]` |
| Last updated | `[DD Month YYYY]` |

## Purpose

Define:

- what the rule is intended to identify;
- which records are eligible;
- what counts as a pass, failure or exception;
- how the result should be measured;
- which system or process should act on it;
- who owns the rule; and
- what uses are currently permitted.

This page does not approve technical implementation, operational action or reporting unless the relevant statuses explicitly state that approval.

## Business question

> `[State the decision-relevant business question the rule is intended to answer.]`

A strong business question should identify:

- the entity or population;
- the condition being assessed;
- the decision or operational need; and
- the intended interpretation.

Avoid starting with the technical test.

## Decision required

Agree:

1. `[eligible population]`;
2. `[included source fields]`;
3. `[minimum criteria or matching logic]`;
4. `[exclusions]`;
5. `[legitimate exceptions]`;
6. `[grain and reporting unit]`;
7. `[numerator and denominator, where applicable]`;
8. `[Salesforce, Plauti and Databricks responsibilities]`;
9. `[operational response]`;
10. `[ownership]`; and
11. `[permitted use]`.

## Current working definition

> `[Write the simplest accurate business expression of the rule.]`

This is a working definition until the business-rule status changes to:

`Business definition agreed`

## Why the rule matters

Explain the decision or service impact.

Possible impacts include:

- customer communication;
- customer effort;
- staff rework;
- account matching;
- duplicate prevention;
- operational handover;
- reporting confidence;
- legal-entity identification;
- service continuity;
- privacy, records or security risk; and
- readiness for connected customer interactions.

Do not overstate consequences that have not been evidenced.

## Scope

### Included

- `[Included object, record type, account type or entity]`
- `[Included activity or time period]`
- `[Included fields or relationships]`

### Excluded

- `[Excluded object or record type]`
- `[Test, training or system records]`
- `[Merged or superseded records, where applicable]`
- `[Other approved exclusions]`

## Eligible population

### Proposed population

`[Describe the records that should be eligible to pass or fail the rule.]`

### Population questions

Confirm:

- which source object is authoritative;
- which record and account types are included;
- how active, inactive and historical records are treated;
- how merged and superseded records are treated;
- whether an activity or snapshot period is required;
- how test, training and system records are excluded;
- whether integrations or imports require separate treatment;
- which classifications determine eligibility; and
- how records that cannot be classified are reported.

Do not treat unclassifiable records as confirmed failures unless explicitly approved.

## Source fields

| Field | Purpose | Status |
|---|---|---|
| `[Source field]` | `[Business meaning]` | Open |
| `[Supporting field]` | `[Business meaning]` | Open |
| `[Exception field]` | `[Business meaning]` | Open |
| `[Status or date field]` | `[Business meaning]` | Open |

Confirm:

- the authoritative source table or object;
- field definitions;
- field precedence;
- null and blank handling;
- legacy fields;
- related-object fields;
- refresh frequency; and
- conflicting values.

## Rule criteria

Describe the assessment levels clearly.

Possible levels include:

### Presence

`[The field contains a value.]`

### Structural or format validity

`[The value meets the agreed structural criteria.]`

### Reference validity

`[The value appears in an approved reference set.]`

### Verification

`[The value has been confirmed through an approved process or source.]`

### Uniqueness or duplicate signal

`[The value is repeated or similar across eligible records.]`

These levels are not interchangeable.

Use names that accurately describe what the rule tests.

## Normalisation

Where matching or formatting is required, document each approved transformation.

Candidate steps:

1. trim leading and trailing spaces;
2. standardise case where relevant;
3. remove approved formatting characters;
4. treat blank strings as null;
5. preserve significant leading zeroes;
6. exclude known test or placeholder values;
7. separate values that cannot be safely normalised; and
8. retain the original source value in the governed environment for review.

Do not add inferred corrections or provider-specific transformations without explicit approval.

## Failure categories

Separate failures where they imply different causes or actions.

| Failure category | Definition | Proposed action |
|---|---|---|
| `[Missing]` | `[Definition]` | `[Action]` |
| `[Malformed]` | `[Definition]` | `[Action]` |
| `[Invalid]` | `[Definition]` | `[Action]` |
| `[Duplicate signal]` | `[Definition]` | `[Action]` |
| `[Unclassifiable]` | `[Definition]` | `[Action]` |
| `[Not assessable]` | `[Definition]` | `[Action]` |

Do not collapse materially different failure types into one measure.

## Candidate exclusions

Potential exclusions include:

- test, training or system-generated records;
- invalid source values;
- placeholder values;
- merged or superseded records;
- records outside the agreed period;
- entity types not subject to the rule;
- temporary or incomplete records;
- internal records;
- records retained only for historical or records purposes; and
- records that cannot be safely assessed.

Each exclusion must be:

- defined;
- approved;
- technically identifiable where possible;
- measurable; and
- versioned.

## Candidate exceptions

Potential exceptions include:

- approved customer preference;
- representative, guardian or carer arrangement;
- legitimate shared contact information;
- valid multi-account organisational structure;
- entity not required to hold the relevant identifier;
- legal, privacy, safety or operational restriction;
- approved temporary condition;
- historical record retained for a valid reason; or
- other documented business exception.

Exceptions must not be hidden inside technical logic.

Record:

- the exception definition;
- approval owner;
- identification method;
- review date or expiry where relevant; and
- reporting treatment.

## Rule logic — business expression

> Within `[eligible population]`, identify `[records, groups or pairs]` where `[failure condition]` after `[exclusions and exception treatment]`.

The business expression must be agreed before detailed technical logic is treated as authoritative.

## Technical expression

Record the approved technical interpretation only after technical review.

| Field | Value |
|---|---|
| Source table or object | `[Source]` |
| Entity identifier | `[Identifier]` |
| Included fields | `[Fields]` |
| Filters | `[Filters]` |
| Normalisation | `[Logic]` |
| Threshold | `[Threshold or not applicable]` |
| Rule version | `[Version]` |
| Execution frequency | `[Frequency]` |
| Output table or location | `[Governed location]` |

Do not place credentials, raw extracts or customer-level values in this repository.

## Salesforce role

### Potential purpose

Salesforce may:

- prevent selected defects;
- provide a warning;
- require selected information;
- support account search;
- record an approved exception; or
- surface a potential duplicate for review.

### Questions

- Does a control already exist?
- Is it native, custom or managed through Plauti?
- Does it run on create, update or both?
- Are integrations and imports included?
- Is it a warning or hard block?
- What legitimate exceptions exist?
- Can staff override it?
- Are overrides recorded?
- Who owns the control?
- What operational impacts could it create?

Do not recommend a hard block until legitimate service and exception scenarios are understood.

## Plauti role

Complete this section only where duplicate detection is relevant.

Confirm:

- active scenarios;
- fields used;
- exact and fuzzy logic;
- thresholds;
- normalisation;
- record types;
- cross-object checks;
- real-time and scheduled behaviour;
- output fields;
- review statuses;
- merge permissions;
- override behaviour;
- false-positive patterns; and
- current production configuration.

Databricks should not automatically reproduce Plauti logic.

## Databricks role

Databricks may support:

- exploratory profiling;
- baseline measurement;
- trend monitoring;
- root-cause analysis;
- comparison of creation pathways;
- sampling;
- technical-rule validation;
- monitoring of preventative controls; and
- controlled diagnostic outputs.

Databricks does not define the business rule.

## Power BI role

Power BI may present approved:

- rule-level diagnostics;
- trends;
- failure categories;
- reviewed outcomes;
- operational workload; and
- governed measures.

Power BI must not turn an exploratory technical result into an approved business metric.

## Measurement structure

### Metric name

`[Plain-English metric name]`

### Metric status

`[Technically calculated / Definition incomplete / Calculation under validation / Diagnostic-ready / Operationally ready / Reporting-ready / Not safe]`

### Unit

`[Distinct accounts / contacts / records / groups / pairs / rule executions]`

### Numerator

`[Define exactly what is counted as failure or signal.]`

### Denominator

`[Define the complete eligible population able to pass or fail.]`

### Rate

`Numerator ÷ denominator × 100`

Remove this formula where a rate is not decision-relevant.

### Period

`[Snapshot date, activity period, creation period or execution period]`

### Filters

- `[Filter]`
- `[Filter]`

### Rule version

`[Version]`

## Denominator safety

The numerator and denominator must use:

- the same entity population;
- the same grain;
- the same identifier;
- the same period;
- the same inclusion and exclusion logic;
- the same exception treatment;
- the same rule version; and
- compatible source logic.

Do not divide:

- groups by records;
- pairs by groups;
- reviewed signals by records never reviewed;
- recent failures by a total historical population;
- Account results by Contact populations; or
- failures by entities not expected to meet the rule.

State plainly when the result is technically calculated but not decision-safe.

## Supporting diagnostics

Possible supporting diagnostics include:

- count by failure category;
- distribution of group size;
- result by account or record type;
- result by creation pathway;
- result by active status;
- result by source;
- reviewed signal count;
- confirmed outcome rate;
- rejected-match rate;
- unresolved count;
- approved exception count;
- remediation count;
- trend by rule version; and
- upstream root-cause patterns.

Each diagnostic requires its own explicit grain and denominator.

## Operational response

For each failure or signal, decide whether the response is:

- correction during the next legitimate interaction;
- operational review;
- controlled remediation;
- upstream process improvement;
- Salesforce prevention;
- Plauti duplicate review;
- Databricks monitoring only;
- governance escalation;
- approved exception; or
- no action.

The rule must not create an operational queue until ownership, capacity and prioritisation are agreed.

## Operational statuses

Use where review is required:

1. new signal;
2. under review;
3. confirmed issue;
4. rejected signal;
5. unresolved;
6. approved exception;
7. remediation candidate;
8. remediated; and
9. closed without action.

For duplicate rules, use the repository duplicate terminology:

- duplicate signal;
- potential duplicate;
- confirmed duplicate;
- rejected match;
- unresolved match;
- approved exception;
- merge candidate; and
- merged.

## Ownership

| Role | Responsibility | Owner |
|---|---|---|
| Business rule owner | Approves purpose, population, logic and permitted use | Open |
| Operational owner | Owns review, correction and exception handling | Open |
| Technical owner — Salesforce | Owns preventative or in-platform controls | Open |
| Technical owner — Plauti | Owns duplicate-check configuration where applicable | Open / Not applicable |
| Technical owner — Databricks | Implements and maintains analytical logic | Open |
| Reporting owner | Maintains approved presentation and wording | Open |
| Data owner or steward | Confirms data meaning and quality expectations | Open |
| Merge authority | Approves merges where applicable | Open / Not applicable |
| Governance reviewers | Provide privacy, records, security or governance advice | Open |

Ownership must be assigned before governed operational use.

## Risks

| Risk | Treatment |
|---|---|
| `[Risk]` | `[Treatment]` |
| `[Risk]` | `[Treatment]` |
| `[Risk]` | `[Treatment]` |

Always consider:

- unsafe population;
- incompatible denominator;
- false positives;
- false negatives;
- operational capacity;
- duplicated tool logic;
- inappropriate automated action;
- privacy and sensitive-data exposure;
- misleading reporting; and
- unversioned rule changes.

## Test cases

Use de-identified or synthetic examples.

Include:

| Test type | Expected outcome |
|---|---|
| Clear pass | `[Expected result]` |
| Clear failure | `[Expected result]` |
| Approved exception | `[Expected result]` |
| Boundary case | `[Expected result]` |
| Invalid source value | `[Expected result]` |
| Unclassifiable record | `[Expected result]` |
| Historical or inactive record | `[Expected result]` |
| Integration-created record | `[Expected result]` |

For duplicate rules, include:

- confirmed duplicate;
- legitimate shared value;
- rejected match;
- unresolved match; and
- safe merge and unsafe merge examples.

## Workshop decision record

| Decision | Outcome | Owner | Date | Status |
|---|---|---|---|---|
| Business question |  |  |  | Open |
| Eligible population |  |  |  | Open |
| Source fields |  |  |  | Open |
| Rule criteria |  |  |  | Open |
| Normalisation |  |  |  | Open |
| Exclusions |  |  |  | Open |
| Exceptions |  |  |  | Open |
| Grain and reporting unit |  |  |  | Open |
| Numerator |  |  |  | Open |
| Denominator |  |  |  | Open |
| Period and filters |  |  |  | Open |
| Salesforce role |  |  |  | Open |
| Plauti role |  |  |  | Open / Not applicable |
| Databricks role |  |  |  | Open |
| Operational response |  |  |  | Open |
| Ownership |  |  |  | Open |
| Governed-use status |  |  |  | Open |
| Reporting approval |  |  |  | Open |

## Definition of Ready

The rule is ready for governed technical implementation only when:

- the business question is agreed;
- the eligible population is explicit;
- source fields are confirmed;
- minimum rule criteria are documented;
- normalisation is agreed;
- exclusions and exceptions are approved;
- grain and reporting unit are explicit;
- numerator and denominator are compatible;
- the reporting period is explicit;
- Salesforce and Plauti overlap has been assessed;
- technical logic can be tested;
- operational response is agreed;
- ownership is assigned;
- privacy, records, security and governance needs have been considered;
- test cases cover passes, failures and exceptions;
- rule versioning is established;
- permitted use is documented; and
- the decision is recorded in the decision log.

## Current assessment

**Business-rule status:** Draft — business refinement required.

**Technical status:** `[Status]`

**Operational-readiness status:** `[Status]`

**Governed-use status:** Not ready.

**Metric-readiness status:** `[Status or not applicable]`

**Reason:** `[State the unresolved decisions plainly.]`

**Permitted current use:** `[For example: workshop preparation and exploratory profiling only.]`

**Slide-safe wording:** Not available.

## Related repository pages

- `../crm-data-quality-rule-register.md`
- `../crm-data-quality-rule-refinement-index.md`
- `../crm-data-quality-rule-refinement.md`
- `../crm-data-quality-rule-refinement-workshop.md`
- `../../01-discover/databricks-customer-data-quality-pilot-input.md`
- `../../00-project-control/status-and-validation-model.md`
- `../../00-project-control/assumptions-log.md`
- `../../00-project-control/risk-register.md`
- `../../06-decisions/decision-log.md`
