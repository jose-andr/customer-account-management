# CAM-DQ-002 — Exact email duplicate signal

## Document control

| Field | Value |
|---|---|
| Rule ID | CAM-DQ-002 |
| Rule name | Exact email duplicate signal |
| Rule group | Person Account duplicate detection |
| Status | Draft — business refinement required |
| Validation level | Partially validated |
| Current phase | Define |
| Priority | First refinement cycle |
| Governed metric status | Not ready |
| Last updated | 30 July 2026 |

## Purpose

Define how an exact email-address match may be used to identify potential duplicate Person Accounts for review.

This rule produces a duplicate signal only.

It does not confirm that two or more records represent the same person and must not automatically trigger a merge.

## Business question

Which Person Accounts share the same normalised email address, and which of those matches should be reviewed as potential duplicates?

## Decision required

Agree:

1. the eligible Person Account population;
2. the email fields included;
3. the email normalisation logic;
4. legitimate shared-email scenarios;
5. excluded or non-usable email values;
6. whether results are counted as records, pairs or groups;
7. the relationship between Salesforce, Plauti and Databricks controls;
8. the operational review pathway; and
9. the ownership of review, confirmation and merge decisions.

## Current working definition

> An exact email duplicate signal occurs when two or more eligible Person Accounts contain the same normalised email address after agreed exclusions and exception rules have been applied.

This is a working definition only.

An exact match is evidence of a shared contact detail, not proof of shared identity.

## Why the rule matters

Repeated email addresses across Person Accounts may indicate:

- duplicate account creation;
- incomplete account matching during service delivery;
- inconsistent account maintenance;
- shared household or family contact details;
- a representative acting for another customer;
- organisational or generic addresses used for multiple people;
- test or placeholder values;
- integration or migration defects; or
- legitimate reuse of an email address over time.

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

Do not call exact email matches “duplicates” without operational confirmation.

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

## Email fields

The business and technical owners must confirm:

- the primary email field;
- any secondary or alternate email fields;
- whether relationship or representative email fields are included;
- whether email fields from related objects are in scope;
- which field is authoritative for the rule; and
- how conflicting email fields are treated.

Do not combine unrelated email fields without documenting the business meaning of each field.

## Email normalisation

Exact matching should use an agreed normalised value.

### Candidate normalisation steps

The following steps require technical validation:

1. convert text to lowercase;
2. remove leading and trailing spaces;
3. remove accidental internal spaces where they are invalid;
4. treat blank strings as null;
5. exclude values that fail minimum syntax checks;
6. exclude known placeholder or test values; and
7. preserve the original source value for operational review without storing it in GitHub.

### Normalisation boundaries

Do not automatically:

- remove dots from email usernames;
- remove plus-addressing suffixes;
- rewrite domains;
- infer typographical corrections;
- treat similar email addresses as equivalent; or
- apply provider-specific rules across all domains.

These transformations may create false matches and require separate approval.

## Candidate exclusions

Potential exclusions requiring validation include:

- blank or null email values;
- invalid email formats;
- known test addresses;
- known placeholder addresses;
- generic organisational mailboxes;
- no-reply addresses;
- system-generated addresses;
- addresses used for anonymised records;
- addresses belonging to authorised representatives;
- addresses recorded only for historic or records purposes; and
- values already known to be unusable.

Exclusion logic must be explicit, versioned and measurable.

## Legitimate shared-email scenarios

An exact email address may legitimately appear across multiple Person Accounts.

Candidate scenarios include:

- family members sharing one email address;
- a parent or guardian managing another person’s services;
- carers or authorised representatives;
- customers with accessibility or support needs;
- shared household addresses;
- customers without an individual email address;
- temporary reuse of a contact address;
- service-specific operational practices;
- migrated historical records; and
- records retained for legal or records obligations.

These scenarios must be considered before any merge or correction activity.

## Rule logic — business expression

The rule should be expressed as:

> Within the eligible Person Account population, group records by the agreed normalised email address and identify groups containing two or more distinct Person Account identifiers after approved exclusions have been applied.

The output is a duplicate signal requiring review.

## Signal strength

Exact email alone should not be treated as conclusive identity evidence.

Where permitted and appropriate, operational review may consider additional attributes such as:

- name;
- date of birth;
- telephone number;
- address;
- account history;
- linked service activity;
- existing merge history;
- relationship or representative information; and
- other approved identity attributes.

The repository must not contain raw customer values or identifiable match examples.

## Salesforce control

### Potential purpose

Salesforce may:

- warn staff when an account with the same email already exists;
- support account-search behaviour before creation;
- prevent selected duplicate-creation scenarios; or
- surface possible matches for operational review.

### Current status

Existing Salesforce or Plauti behaviour must be confirmed before proposing changes.

### Questions

- Does Salesforce already perform an email-based duplicate check?
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

Plauti Duplicate Check may already use email-address matching as part of one or more scenarios.

Before reproducing or extending the logic, confirm:

- active Person Account scenarios;
- fields used;
- exact-match and fuzzy-match logic;
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

The two tools may serve different purposes:

| Capability | Potential role |
|---|---|
| Plauti | Operational duplicate identification and review support |
| Databricks | Baseline measurement, trend monitoring and root-cause analysis |
| Salesforce | Preventative controls and account-search support |
| Human review | Identity confirmation and merge decision |
| Governance | Standards, ownership and escalation |

## Databricks purpose

Databricks may be used to:

- estimate the scale of exact email duplicate signals;
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

Number of Person Account records that belong to an exact email match group.

### Group count

Number of distinct normalised email values shared by two or more Person Accounts.

### Pair count

Number of unique record-to-record combinations created within match groups.

For a group containing three records:

- record count = 3;
- group count = 1;
- pair count = 3.

The chosen measure must be named explicitly.

## Proposed primary diagnostic

### Metric name

Person Accounts in exact email match groups.

### Metric status

Exploratory only — not governed and not slide-safe.

### Unit

Distinct eligible Person Accounts.

### Proposed numerator

Distinct eligible Person Accounts belonging to a normalised email group containing two or more distinct Person Account identifiers.

### Proposed denominator

All distinct eligible Person Accounts with an email value that meets the agreed minimum inclusion criteria.

### Proposed rate

`Numerator ÷ denominator × 100`

This denominator measures the proportion of assessable accounts with an exact email duplicate signal.

It does not measure the proportion of all CRM accounts unless accounts without usable email values are intentionally included.

## Supporting diagnostics

Candidate supporting measures include:

- number of exact email match groups;
- distribution of group sizes;
- number of records in groups of two;
- number of records in groups of three or more;
- number of signals already reviewed;
- confirmed duplicate rate;
- rejected match rate;
- unresolved match rate;
- number of merge candidates;
- number of completed merges;
- number of signals by account-creation pathway; and
- number of signals by rule version.

Each measure requires compatible grain and explicit definitions.

## Denominator safety

Do not divide:

- match groups by account records;
- pairs by match groups;
- reviewed signals by all CRM accounts;
- confirmed duplicates by records that were never reviewed; or
- recent duplicate signals by the total historical account base.

Every rate must use a denominator that represents the population eligible for the numerator.

## Source requirements

Before implementation, confirm:

| Requirement | Status |
|---|---|
| Salesforce source object or governed Databricks table | Open |
| Unique Person Account identifier | Open |
| Primary email field | Open |
| Alternate email fields | Open |
| Record-type logic | Open |
| Account-status logic | Open |
| Creation date and source | Open |
| Merge or superseded-record indicators | Open |
| Test and system-record exclusions | Open |
| Plauti result fields | Open |
| Review outcome fields | Open |
| Rule refresh frequency | Open |

Do not record raw email addresses or record-level extracts in this repository.

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
- account status;
- creation pathway;
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
- whether the shared email is legitimate;
- which record should be retained;
- whether records can be safely merged;
- whether service or transaction history may be affected;
- whether legal, privacy, records or security constraints apply;
- whether related records must be updated;
- whether the source of duplicate creation can be corrected; and
- whether customer contact is appropriate.

No merge should occur solely because the email address matches.

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
| Shared family or representative emails create false positives | Define exceptions and require human review. |
| Different email fields are combined without context | Confirm field meaning and scope before implementation. |
| Normalisation creates incorrect matches | Use conservative logic and document each transformation. |
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
| Email fields included |  |  |  | Open |
| Normalisation logic |  |  |  | Open |
| Excluded values |  |  |  | Open |
| Legitimate shared-email exceptions |  |  |  | Open |
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
- included email fields are confirmed;
- normalisation logic is documented;
- exclusions and exceptions are approved;
- the reporting unit is explicit;
- source fields and grain are confirmed;
- numerator and denominator are compatible;
- Plauti and Salesforce overlap has been assessed;
- operational review ownership is assigned;
- merge authority and controls are defined;
- test cases include valid matches, false positives and exceptions;
- privacy, records, security and governance needs have been considered;
- rule versioning is established;
- permitted uses are documented; and
- the decision is recorded in the decision log.

## Current assessment

**Status:** Technically definable but not ready for governed implementation.

**Reason:** Population, email fields, normalisation, exceptions, tool boundaries, review ownership and reporting grain remain unresolved.

**Slide-safe wording:** Not available.

**Permitted current use:** Workshop preparation, exploratory profiling and comparison with existing duplicate-check controls only.

## Related repository pages

- `02-define/rules/CAM-DQ-001-minimum-valid-contact-method.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `02-define/crm-data-quality-rule-refinement-workshop.md`
- `01-discover/evidence-gaps.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`
- 
