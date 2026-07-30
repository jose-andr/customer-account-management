# CAM-DQ-003 — Exact mobile duplicate signal

## Document control

| Field | Value |
|---|---|
| Rule ID | CAM-DQ-003 |
| Rule name | Exact mobile duplicate signal |
| Rule group | Person Account duplicate detection |
| Status | Draft — business refinement required |
| Validation level | Partially validated |
| Current phase | Define |
| Priority | First refinement cycle |
| Governed metric status | Not ready |
| Last updated | 30 July 2026 |

## Purpose

Define how an exact mobile-number match may be used to identify potential duplicate Person Accounts for review.

This rule produces a duplicate signal only.

It does not confirm that two or more records represent the same person and must not automatically trigger a merge.

## Business question

Which Person Accounts share the same normalised mobile number, and which of those matches should be reviewed as potential duplicates?

## Decision required

Agree:

1. the eligible Person Account population;
2. the mobile fields included;
3. the mobile normalisation logic;
4. legitimate shared-number scenarios;
5. excluded, invalid or non-usable values;
6. whether results are counted as records, pairs or groups;
7. the relationship between Salesforce, Plauti and Databricks controls;
8. the operational review pathway; and
9. the ownership of review, confirmation and merge decisions.

## Current working definition

> An exact mobile duplicate signal occurs when two or more eligible Person Accounts contain the same normalised mobile number after agreed exclusions and exception rules have been applied.

This is a working definition only.

An exact match is evidence of a shared contact detail, not proof of shared identity.

## Why the rule matters

Repeated mobile numbers across Person Accounts may indicate:

- duplicate account creation;
- incomplete account matching during service delivery;
- inconsistent account maintenance;
- family members sharing one number;
- a parent, guardian, carer or representative acting for another customer;
- a service provider or support worker using one contact number for multiple people;
- recycled mobile numbers;
- placeholder or test values;
- migration or integration defects; or
- legitimate reuse of a mobile number over time.

The rule must support investigation without overstating what the data proves.

## Required terminology

Use these terms consistently:

| Term | Meaning |
|---|---|
| Duplicate signal | A data pattern suggesting that records may require review. |
| Potential duplicate | Two or more records that may represent the same person. |
| Confirmed duplicate | Records reviewed and confirmed as representing the same person. |
| Rejected match | A reviewed signal determined not to be a duplicate. |
| Unresolved match | A signal that has not yet been conclusively assessed. |
| Merge candidate | A confirmed duplicate assessed as potentially safe to merge. |
| Merged | Records combined through an approved operational process. |

Do not call exact mobile matches “duplicates” without operational confirmation.

## Eligible population

### Proposed starting population

Person Accounts that are:

- within the agreed Salesforce account population;
- not identified as test, training or system-generated records;
- not already superseded or excluded under approved logic;
- not deliberately duplicated for an approved operational reason; and
- within the agreed activity, creation or relevance period.

### Population questions

The workshop must determine:

- whether all Person Accounts are included;
- whether inactive or historical accounts are included;
- how merged, deleted or superseded records are treated;
- whether accounts without recent activity remain in scope;
- how deceased-customer records are treated;
- how temporary or incomplete records are treated;
- whether records created by integrations require separate analysis; and
- whether some record types should be analysed independently.

## Mobile fields

The business and technical owners must confirm:

- the primary mobile field;
- any alternate or secondary mobile fields;
- whether general telephone fields are included;
- whether relationship or representative mobile fields are included;
- whether numbers from related objects are in scope;
- which field is authoritative for the rule; and
- how conflicting mobile fields are treated.

Do not combine unrelated telephone fields without documenting the business meaning of each field.

## Mobile normalisation

Exact matching should use an agreed normalised value.

### Candidate normalisation steps

The following steps require technical validation:

1. trim leading and trailing spaces;
2. remove formatting characters such as spaces, brackets and hyphens;
3. convert approved Australian country-code formats to one standard form;
4. treat blank strings as null;
5. exclude values that fail minimum length or format checks;
6. exclude known placeholder and test values;
7. preserve extensions only where operationally meaningful; and
8. preserve the original source value for operational review without storing it in GitHub.

### Candidate Australian standard form

A possible technical standard is:

> Convert valid Australian mobile numbers to a consistent international format such as `+614XXXXXXXX`.

This format is not approved through this page.

The business and technical owners must confirm:

- accepted local and international formats;
- whether only Australian mobile numbers are in scope;
- how international numbers are treated;
- whether leading zeroes are restored or removed;
- how invalid or incomplete values are classified; and
- whether mobile and non-mobile numbers must be separated.

### Normalisation boundaries

Do not automatically:

- infer missing digits;
- correct likely typographical errors;
- convert ambiguous international numbers;
- remove extensions without review;
- treat landline and mobile numbers as equivalent;
- combine multiple numbers into one value; or
- use partial-number matching.

These transformations may create false matches and require separate approval.

## Candidate exclusions

Potential exclusions requiring validation include:

- blank or null values;
- values that are too short or too long;
- known test numbers;
- repeated placeholder digits;
- all-zero values;
- service or switchboard numbers;
- generic organisational numbers;
- numbers belonging to authorised representatives;
- numbers known to be disconnected;
- numbers recorded only for historic or records purposes;
- fax numbers;
- emergency or public service numbers; and
- values that cannot be safely normalised.

Exclusion logic must be explicit, versioned and measurable.

## Legitimate shared-number scenarios

An exact mobile number may legitimately appear across multiple Person Accounts.

Candidate scenarios include:

- family members sharing one mobile number;
- a parent or guardian managing another person’s services;
- carers or authorised representatives;
- customers with accessibility or support needs;
- supported accommodation or community-service arrangements;
- customers without an individual mobile number;
- temporary use of another person’s number;
- recycled mobile numbers;
- migrated historical records; and
- records retained for legal or records obligations.

These scenarios must be considered before any merge or correction activity.

## Recycled-number risk

Mobile numbers may be reassigned by telecommunications providers.

An exact match across records created or active at different times may therefore represent different people.

The review process should consider:

- account creation dates;
- last verified dates;
- last interaction dates;
- known invalidation or bounce indicators;
- whether the number is current on both records; and
- whether the records overlap in time.

A shared number across different periods must not be treated as conclusive identity evidence.

## Rule logic — business expression

The rule should be expressed as:

> Within the eligible Person Account population, group records by the agreed normalised mobile number and identify groups containing two or more distinct Person Account identifiers after approved exclusions have been applied.

The output is a duplicate signal requiring review.

## Signal strength

Exact mobile alone should not be treated as conclusive identity evidence.

Where permitted and appropriate, operational review may consider additional attributes such as:

- name;
- date of birth;
- email address;
- postal address;
- account history;
- linked service activity;
- existing merge history;
- relationship or representative information;
- record creation timing; and
- other approved identity attributes.

The repository must not contain raw customer values or identifiable match examples.

## Salesforce control

### Potential purpose

Salesforce may:

- warn staff when an account with the same mobile number already exists;
- support account-search behaviour before creation;
- prevent selected duplicate-creation scenarios; or
- surface possible matches for operational review.

### Current status

Existing Salesforce or Plauti behaviour must be confirmed before proposing changes.

### Questions

- Does Salesforce already perform a mobile-based duplicate check?
- Is the logic native, custom or Plauti-managed?
- Which record types and creation pathways are covered?
- Does the check run on create, update or both?
- Are integrations and imports included?
- Is the control a warning or a hard block?
- What exceptions are allowed?
- What happens when staff override a warning?
- Are match outcomes recorded?
- How often is the logic reviewed?

Do not create a second control that duplicates existing functionality without a clear reason.

## Plauti relationship

Plauti Duplicate Check may already use mobile-number matching as part of one or more scenarios.

Before reproducing or extending the logic, confirm:

- active Person Account scenarios;
- fields used;
- exact-match and fuzzy-match logic;
- normalisation rules;
- thresholds;
- cross-object matching;
- scheduled jobs;
- real-time behaviour;
- result fields;
- merge permissions;
- exception handling;
- output volumes;
- false-positive patterns; and
- current production configuration.

Databricks should not automatically reproduce Plauti logic.

The tools may serve different purposes:

| Capability | Potential role |
|---|---|
| Plauti | Operational duplicate identification and review support |
| Databricks | Baseline measurement, trend monitoring and root-cause analysis |
| Salesforce | Preventative controls and account-search support |
| Human review | Identity confirmation and merge decision |
| Governance | Standards, ownership and escalation |

## Databricks purpose

Databricks may be used to:

- estimate the scale of exact mobile duplicate signals;
- identify patterns by safe operational dimensions;
- compare signal volumes over time;
- assess likely creation pathways;
- monitor the effect of preventative controls;
- support sampling and validation;
- compare analytical results with Plauti outputs; and
- identify unresolved data-quality issues.

Databricks must not label matches as confirmed duplicates unless review outcomes are available and governed.

## Measurement structures

The result may be represented in several ways.

These measures are not interchangeable.

### Record count

Number of Person Account records that belong to an exact mobile match group.

### Group count

Number of distinct normalised mobile numbers shared by two or more Person Accounts.

### Pair count

Number of unique record-to-record combinations created within match groups.

For a group containing three records:

- record count = 3;
- group count = 1;
- pair count = 3.

The chosen measure must be named explicitly.

## Proposed primary diagnostic

### Metric name

Person Accounts in exact mobile match groups.

### Metric status

Exploratory only — not governed and not slide-safe.

### Unit

Distinct eligible Person Accounts.

### Proposed numerator

Distinct eligible Person Accounts belonging to a normalised mobile group containing two or more distinct Person Account identifiers.

### Proposed denominator

All distinct eligible Person Accounts with a mobile value that meets the agreed minimum inclusion criteria.

### Proposed rate

`Numerator ÷ denominator × 100`

This denominator measures the proportion of assessable accounts with an exact mobile duplicate signal.

It does not measure the proportion of all CRM accounts unless accounts without usable mobile values are intentionally included.

## Supporting diagnostics

Candidate supporting measures include:

- number of exact mobile match groups;
- distribution of group sizes;
- number of records in groups of two;
- number of records in groups of three or more;
- number of signals already reviewed;
- confirmed duplicate rate;
- rejected match rate;
- unresolved match rate;
- number of merge candidates;
- number of completed merges;
- number of signals by account-creation pathway;
- number of signals involving potentially recycled numbers; and
- number of signals by rule version.

Each measure requires compatible grain and explicit definitions.

## Denominator safety

Do not divide:

- match groups by account records;
- pairs by match groups;
- reviewed signals by all CRM accounts;
- confirmed duplicates by records that were never reviewed;
- mobile-match records by all accounts without stating that missing mobile values are included; or
- recent duplicate signals by the total historical account base.

Every rate must use a denominator that represents the population eligible for the numerator.

## Source requirements

Before implementation, confirm:

| Requirement | Status |
|---|---|
| Salesforce source object or governed Databricks table | Open |
| Unique Person Account identifier | Open |
| Primary mobile field | Open |
| Alternate telephone fields | Open |
| Record-type logic | Open |
| Account-status logic | Open |
| Creation date and source | Open |
| Last verified or last updated date | Open |
| Merge or superseded-record indicators | Open |
| Test and system-record exclusions | Open |
| Plauti result fields | Open |
| Review outcome fields | Open |
| Rule refresh frequency | Open |

Do not record raw mobile numbers or record-level extracts in this repository.

## Output structure

A technical output should retain enough information in the governed analytical environment to support review and measurement.

Candidate fields include:

- rule ID;
- rule version;
- execution date;
- Person Account identifier;
- normalised match-key hash or governed equivalent;
- match-group identifier;
- group size;
- source field;
- number-type classification;
- account status;
- creation pathway;
- last verified or updated date;
- review status;
- review outcome;
- exception status; and
- permitted operational metadata.

The use of hashed or masked values must be agreed with technical and governance owners.

## Operational review

Each signal should move through a controlled review pathway.

### Candidate statuses

1. new signal;
2. under review;
3. confirmed duplicate;
4. rejected match;
5. unresolved match;
6. approved exception;
7. merge candidate;
8. merged; and
9. closed without merge.

### Review questions

Operational reviewers may need to determine:

- whether the records represent the same person;
- whether the shared number is legitimate;
- whether the number may have been recycled;
- whether the number is current on both records;
- which record should be retained;
- whether records can be safely merged;
- whether service or transaction history may be affected;
- whether legal, privacy, records or security constraints apply;
- whether related records must be updated;
- whether the source of duplicate creation can be corrected; and
- whether customer contact is appropriate.

No merge should occur solely because the mobile number matches.

## Ownership

| Role | Responsibility | Owner |
|---|---|---|
| Business rule owner | Approves the rule purpose, scope and permitted use | Open |
| Operational owner | Owns signal review and exception handling | Open |
| Merge authority | Approves or performs merges under controlled conditions | Open |
| Technical owner — Salesforce | Owns preventative or in-platform controls | Open |
| Technical owner — Plauti | Owns operational duplicate-check configuration | Open |
| Technical owner — Databricks | Implements and maintains analytical logic | Open |
| Data owner or steward | Confirms data meaning and quality expectations | Open |
| Governance reviewers | Provide privacy, records, security or governance advice | Open |

Ownership must be assigned before the rule is moved to governed use.

## Risks

| Risk | Treatment |
|---|---|
| Exact matches are labelled as confirmed duplicates | Use duplicate-signal terminology throughout. |
| Shared family or representative numbers create false positives | Define exceptions and require human review. |
| Recycled numbers create incorrect identity assumptions | Include time and currency checks in review. |
| Different telephone fields are combined without context | Confirm field meaning and scope before implementation. |
| Normalisation creates incorrect matches | Use conservative logic and document each transformation. |
| Mobile and landline numbers are mixed | Classify and report number types separately. |
| Record, pair and group counts are confused | State the unit and grain with every result. |
| Databricks duplicates existing Plauti functionality | Compare tool purposes and active configurations first. |
| Automated merges cause loss or corruption of history | Prohibit merge decisions based on this rule alone. |
| Operational teams receive an unmanageable queue | Agree prioritisation, ownership and capacity before use. |
| Historical records distort current-state reporting | Agree account status and period logic. |
| Customer information is copied into GitHub | Store only definitions, logic, summaries and caveats. |

## Workshop decision record

| Decision | Outcome | Owner | Date | Status |
|---|---|---|---|---|
| Eligible Person Account population |  |  |  | Open |
| Mobile fields included |  |  |  | Open |
| Normalisation logic |  |  |  | Open |
| Accepted number types |  |  |  | Open |
| Excluded values |  |  |  | Open |
| Legitimate shared-number exceptions |  |  |  | Open |
| Recycled-number treatment |  |  |  | Open |
| Primary reporting unit |  |  |  | Open |
| Measurement period |  |  |  | Open |
| Salesforce control purpose |  |  |  | Open |
| Plauti relationship |  |  |  | Open |
| Databricks diagnostic purpose |  |  |  | Open |
| Operational review pathway |  |  |  | Open |
| Merge authority |  |  |  | Open |
| Business owner |  |  |  | Open |
| Technical owners |  |  |  | Open |
| Governed-use approval |  |  |  | Open |

## Definition of Ready

The rule is ready for governed technical implementation only when:

- the business question is agreed;
- the eligible population is explicit;
- included mobile fields are confirmed;
- accepted number types are defined;
- normalisation logic is documented;
- exclusions and exceptions are approved;
- recycled-number treatment is agreed;
- the reporting unit is explicit;
- source fields and grain are confirmed;
- numerator and denominator are compatible;
- Plauti and Salesforce overlap has been assessed;
- operational review ownership is assigned;
- merge authority and controls are defined;
- test cases include valid matches, false positives, recycled numbers and exceptions;
- privacy, records, security and governance needs have been considered;
- rule versioning is established;
- permitted uses are documented; and
- the decision is recorded in the decision log.

## Current assessment

**Status:** Technically definable but not ready for governed implementation.

**Reason:** Population, mobile fields, normalisation, exceptions, recycled-number treatment, tool boundaries, review ownership and reporting grain remain unresolved.

**Slide-safe wording:** Not available.

**Permitted current use:** Workshop preparation, exploratory profiling and comparison with existing duplicate-check controls only.

## Related repository pages

- `02-define/rules/CAM-DQ-001-minimum-valid-contact-method.md`
- `02-define/rules/CAM-DQ-002-exact-email-duplicate-signal.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `02-define/crm-data-quality-rule-refinement-workshop.md`
- `01-discover/evidence-gaps.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`
