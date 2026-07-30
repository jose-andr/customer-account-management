# CAM-DQ-007 — Repeated ACN

## Document control

| Field | Value |
|---|---|
| Rule ID | CAM-DQ-007 |
| Rule name | Repeated ACN |
| Rule group | Organisation Account duplicate detection |
| Status | Draft — business refinement required |
| Validation level | Partially validated |
| Current phase | Define |
| Priority | First refinement cycle |
| Governed metric status | Not ready |
| Last updated | 30 July 2026 |

## Purpose

Define how repeated Australian Company Numbers across Organisation Accounts should be identified, measured and reviewed.

This rule produces a company-account duplicate signal.

It does not confirm that repeated records represent the same operational account, establish that the ACN belongs to each account, or automatically authorise merging.

## Business question

Which eligible Organisation Accounts share the same normalised ACN, and which repeated values require review as potential duplicate company records?

## Decision required

Agree:

1. the eligible Organisation Account population;
2. the legal entity types expected to hold an ACN;
3. the authoritative ACN field;
4. minimum ACN validity requirements;
5. ACN normalisation logic;
6. legitimate repeated-ACN scenarios;
7. whether outputs are counted as records, groups or pairs;
8. the relationship between Salesforce, Plauti and Databricks controls;
9. the operational review pathway; and
10. ownership of review, correction and merge decisions.

## Current working definition

> A repeated ACN signal occurs when two or more eligible Organisation Accounts contain the same normalised ACN after agreed validity, exclusion and exception rules have been applied.

This is a working definition only.

A repeated ACN is a strong company-identity signal, but it is not sufficient evidence for an automatic merge.

## Why the rule matters

Repeated ACNs may indicate:

- duplicate Organisation Account creation;
- inconsistent account-search practices;
- separate records created for different services;
- migrated or historical duplicates;
- one company represented through multiple operational accounts;
- legal entity and trading-name records being mixed;
- parent, subsidiary or branch relationships recorded incorrectly;
- an ACN entered against the wrong organisation;
- placeholder or test values;
- ABNs entered incorrectly in the ACN field; or
- legitimate account structures requiring separate CRM records.

The rule must distinguish likely duplicate company records from legitimate operational or organisational structures.

## Scope

This rule applies only to Organisation Accounts:

- representing entities expected to hold an ACN;
- containing an ACN that meets the agreed minimum inclusion criteria; and
- within the approved analytical population.

It must not be applied to:

- Person Accounts;
- sole traders;
- partnerships;
- trusts without a company structure;
- incorporated associations without an ACN;
- government entities not expected to hold an ACN;
- international organisations without an Australian company registration;
- blank ACN values;
- values that cannot be safely normalised;
- known test or placeholder values; or
- approved exceptions.

## Eligible population

### Proposed starting population

Organisation Accounts that:

- are within the agreed Salesforce account population;
- are classified as an Australian company or another entity expected to hold an ACN;
- contain an ACN meeting the agreed minimum inclusion criteria;
- are not test, training or system-generated records;
- are not already merged, superseded or excluded under approved logic;
- are within the agreed status or activity period; and
- do not meet an approved exception.

### Population questions

The workshop must determine:

- which Organisation Account record types are in scope;
- which legal entity types are expected to hold an ACN;
- whether inactive, deregistered or historical companies remain in scope;
- whether merged or superseded records remain visible in analysis;
- whether subsidiaries require separate CRM accounts;
- whether multiple service relationships may justify separate accounts;
- whether account hierarchy fields should affect the rule;
- whether branches or business units may share a company identity;
- how registered Australian bodies using an ARBN are treated;
- whether internal organisational accounts are excluded; and
- whether an activity or recency threshold is required.

## ACN field and validity dependency

The business and technical owners must confirm:

- the authoritative ACN field;
- whether alternate ACN fields exist;
- whether ACN values are stored consistently;
- whether only structurally valid ACNs are included;
- whether checksum validation is required;
- whether externally verified ACNs are treated differently;
- whether blank and placeholder values are excluded;
- whether probable ABNs in the ACN field are excluded; and
- whether conflicting values exist across fields or systems.

The repeated-ACN rule depends on the business decisions recorded in:

`CAM-DQ-005 — ACN completeness`

Do not include malformed, placeholder or misclassified identifiers in duplicate analysis unless they are reported as separate diagnostic categories.

## ACN normalisation

Candidate normalisation steps requiring technical validation:

1. trim leading and trailing spaces;
2. remove approved formatting characters;
3. retain digits only where safe;
4. preserve leading zeroes;
5. treat blank strings as null;
6. exclude known test and placeholder values;
7. separate values that fail minimum structural criteria;
8. identify probable ABNs entered in the ACN field; and
9. retain the original source value in the governed environment for operational review.

Do not store raw ACNs or record-level extracts in GitHub.

## Minimum inclusion criteria

Candidate inclusion levels include:

### Level 1 — Present

The ACN field contains a non-blank value.

### Level 2 — Structurally valid

The normalised value contains nine digits.

### Level 3 — Checksum-valid

The value passes the approved ACN checksum algorithm.

### Level 4 — Externally verified

The ACN has been validated against an approved source.

The selected level must be explicit.

A repeated malformed ACN may indicate a shared data-entry defect rather than a duplicate company.

## Legitimate repeated-ACN scenarios

A repeated ACN may be legitimate where:

- one company has multiple operational accounts;
- different services intentionally maintain separate account records;
- a company and one of its trading-name records coexist;
- separate branches or locations use distinct CRM accounts;
- one account is retained for historical or records purposes;
- migrated records are retained temporarily;
- account hierarchy requires separate records;
- a company has multiple customer relationships that cannot yet be consolidated;
- internal and external account representations coexist; or
- merge is unsafe because records have incompatible relationships, permissions or service history.

These scenarios must be understood before classifying records as duplicate companies.

## Rule logic — business expression

The rule should be expressed as:

> Within the eligible Organisation Account population, group records by the agreed normalised ACN and identify groups containing two or more distinct Organisation Account identifiers after approved exclusions have been applied.

The output is a repeated-ACN signal requiring review.

## Signal strength

Repeated ACN is a stronger company-identity signal than repeated legal name or trading name alone.

It should still be assessed with other information such as:

- legal name;
- trading name;
- ABN;
- legal entity classification;
- address;
- account hierarchy;
- service relationships;
- account status;
- creation source;
- linked contacts;
- linked transactions;
- previous merge history;
- company registration status; and
- approved external verification results.

No merge should occur solely because the ACN matches.

## Relationship between ACN and ABN

ACN and ABN are related but not interchangeable.

The review process should determine:

- whether the entity is expected to hold both identifiers;
- whether the same ACN is associated with compatible ABNs;
- whether an ABN has been entered into the ACN field;
- whether one account contains only an ACN and another only an ABN;
- whether cross-field matching strengthens or weakens the duplicate signal; and
- whether inconsistent identifiers indicate a data-entry or classification issue.

Do not infer company identity from partial identifier relationships without approved logic.

## Salesforce control

### Potential purpose

Salesforce may:

- warn staff when an account with the same ACN already exists;
- support account search before creation;
- prevent selected duplicate-creation scenarios;
- require review before a repeated ACN is saved;
- detect probable ABNs entered in the ACN field; or
- record a legitimate exception.

### Current status

Existing Salesforce and Plauti behaviour must be confirmed before proposing changes.

### Questions

- Does Salesforce currently check for repeated ACNs?
- Is the control native, custom or Plauti-managed?
- Does it run on create, update or both?
- Are integrations and imports included?
- Is the control a warning or hard block?
- Are legitimate repeated-ACN scenarios supported?
- Can staff override the control?
- Are override reasons recorded?
- Does the rule use normalised or raw values?
- Are review outcomes stored?

Do not introduce a hard block until legitimate company-account structures are understood.

## Plauti relationship

Plauti may already use ACN as part of Organisation Account duplicate-detection scenarios.

Before reproducing or extending the logic, confirm:

- active Account scenarios;
- fields used;
- exact and fuzzy matching logic;
- thresholds;
- cross-object checks;
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
| Salesforce | Preventative controls and account-search support |
| Plauti | Operational duplicate identification and merge support |
| Databricks | Baseline measurement, trend monitoring and root-cause analysis |
| Human review | Company confirmation and merge decision |
| Governance | Standards, ownership and escalation |

## Databricks purpose

Databricks may be used to:

- identify Organisation Accounts in repeated-ACN groups;
- estimate the scale of repeated-ACN signals;
- measure group-size distribution;
- compare results across account-creation pathways;
- identify likely upstream causes;
- compare analytical results with Plauti outputs;
- monitor trends over time;
- support sampling and validation; and
- evaluate the effect of preventative controls.

Databricks must not classify repeated ACNs as confirmed duplicates unless governed review outcomes are available.

## Pilot dashboard input

The initial customer data-quality pilot reported ACN uniqueness of approximately 90.77%.

This result is exploratory.

It must not be interpreted as:

- 9.23% of companies being confirmed duplicates;
- 9.23% of accounts requiring merge; or
- a governed company-account duplicate rate.

The result may be affected by:

- organisation types not expected to hold an ACN;
- invalid or placeholder ACNs;
- ABNs entered in the ACN field;
- record-level versus group-level counting;
- legitimate multi-account company structures;
- inactive or historical accounts;
- multiple rule executions;
- unclear denominator logic; and
- different treatment of blanks and excluded records.

The pilot result should be used to refine the rule, not to establish a performance baseline.

## Measurement structures

Repeated ACNs may be counted in several ways.

These units are not interchangeable.

### Record count

Number of Organisation Account records belonging to a repeated-ACN group.

### Group count

Number of distinct normalised ACNs shared by two or more Organisation Accounts.

### Pair count

Number of unique record-to-record combinations within repeated-ACN groups.

For a group containing three records:

- record count = 3;
- group count = 1;
- pair count = 3.

Every output must state the reporting unit.

## Proposed primary diagnostic

### Metric name

Organisation Accounts in repeated-ACN groups.

### Metric status

Exploratory only — not governed and not slide-safe.

### Unit

Distinct eligible Organisation Accounts.

### Proposed numerator

Distinct eligible Organisation Accounts belonging to a normalised ACN group containing two or more distinct Organisation Account identifiers.

### Proposed denominator

All distinct eligible Organisation Accounts with an ACN meeting the agreed minimum inclusion criteria.

### Proposed rate

`Numerator ÷ denominator × 100`

This rate measures the proportion of assessable Organisation Accounts that belong to a repeated-ACN group.

It does not measure the proportion of confirmed duplicate companies.

## Supporting diagnostics

Candidate supporting measures include:

- repeated-ACN group count;
- Organisation Accounts in repeated-ACN groups;
- distribution of group sizes;
- groups containing active accounts only;
- groups containing active and inactive accounts;
- repeated ACNs by creation pathway;
- repeated ACNs by account type;
- repeated ACNs by legal entity classification;
- groups with matching ABNs;
- groups with conflicting ABNs;
- groups with consistent legal names;
- groups with conflicting legal names;
- reviewed signals;
- confirmed duplicates;
- rejected matches;
- unresolved matches;
- approved exceptions;
- merge candidates;
- completed merges; and
- results by rule version.

Each measure must state its grain, denominator and permitted use.

## Denominator safety

Do not divide:

- repeated-ACN groups by account records;
- duplicate pairs by ACN groups;
- reviewed signals by all Organisation Accounts;
- confirmed duplicates by records never reviewed;
- repeated ACNs by all CRM accounts;
- repeated ACNs by accounts with blank or invalid ACNs;
- repeated ACNs by organisations not expected to hold an ACN; or
- recent repeated-ACN signals by the total historical account base.

The numerator and denominator must use:

- the same Organisation Account population;
- the same period;
- the same ACN inclusion criteria;
- the same legal entity classification;
- the same account identifier;
- the same exclusions;
- the same rule version; and
- compatible grain.

## Source requirements

Before implementation, confirm:

| Requirement | Status |
|---|---|
| Salesforce source object or governed Databricks table | Open |
| Unique Organisation Account identifier | Open |
| Authoritative ACN field | Open |
| ACN validity logic | Open |
| Authoritative ABN field | Open |
| Organisation Account record types | Open |
| Legal and trading name fields | Open |
| Legal entity classification | Open |
| Account hierarchy fields | Open |
| Account status | Open |
| Creation date and source | Open |
| Merge or superseded-record indicators | Open |
| Test and system-record exclusions | Open |
| Plauti result fields | Open |
| Review outcome fields | Open |
| Rule refresh frequency | Open |

## Output categories

A governed analytical output should distinguish:

1. repeated checksum-valid ACN;
2. repeated structurally valid ACN;
3. repeated malformed ACN;
4. repeated placeholder value;
5. probable ABN entered in the ACN field;
6. likely legitimate multi-account company structure;
7. potential duplicate company;
8. confirmed duplicate;
9. rejected match;
10. unresolved match;
11. approved exception;
12. merge candidate;
13. merged; and
14. excluded record.

These categories must not be collapsed where they imply different actions.

## Operational review

Each repeated-ACN signal should move through a controlled review pathway.

### Candidate statuses

1. new signal;
2. under review;
3. potential duplicate;
4. confirmed duplicate;
5. rejected match;
6. unresolved match;
7. approved exception;
8. merge candidate;
9. merged; and
10. closed without merge.

### Review questions

Operational reviewers may need to determine:

- whether the records represent the same registered company;
- whether separate records are operationally required;
- whether legal and trading names are consistent;
- whether ABN values are compatible;
- whether the ACN belongs to each account;
- whether one account is historical or superseded;
- whether account hierarchy explains the repetition;
- which record should be retained;
- whether records can be safely merged;
- whether service, relationship or transaction history may be affected;
- whether legal, privacy, records or security constraints apply;
- whether related records must be updated; and
- whether the account-creation pathway can be improved.

## Operational response

Possible actions include:

- confirm a legitimate exception;
- correct an incorrectly entered ACN;
- move a probable ABN to the correct field through a controlled process;
- update legal entity classification;
- link accounts through an approved hierarchy;
- merge confirmed duplicate records;
- retain separate records with documented rationale;
- improve account-search guidance;
- improve Salesforce duplicate controls;
- correct integration or migration logic;
- assign records to a controlled review queue; or
- take no action where remediation is inappropriate.

The rule must not automatically trigger merges or customer contact.

## Ownership

| Role | Responsibility | Owner |
|---|---|---|
| Business rule owner | Approves purpose, scope and permitted use | Open |
| Operational owner | Owns review and exception handling | Open |
| Merge authority | Approves or performs controlled merges | Open |
| Technical owner — Salesforce | Owns preventative and in-platform controls | Open |
| Technical owner — Plauti | Owns duplicate-check configuration | Open |
| Technical owner — Databricks | Implements and maintains analytical logic | Open |
| Data owner or steward | Confirms field meaning and quality expectations | Open |
| Governance reviewers | Provide privacy, records, security or governance advice | Open |

Ownership must be assigned before governed use.

## Risks

| Risk | Treatment |
|---|---|
| Repeated ACNs are labelled as confirmed duplicates | Use duplicate-signal terminology throughout. |
| Organisations not expected to hold an ACN enter the population | Apply legal entity eligibility before matching. |
| Legitimate company structures are treated as defects | Define exceptions and account-hierarchy rules. |
| Invalid or placeholder ACNs create false groups | Apply minimum validity criteria before matching. |
| ABNs entered in the ACN field distort results | Identify and report cross-field errors separately. |
| Record, group and pair counts are confused | State the unit and grain with every result. |
| ACN ownership is assumed from field presence | Keep field value, structural validity and verification separate. |
| Historical records distort current-state reporting | Agree status and period logic. |
| Databricks duplicates existing Plauti functionality | Compare tool purposes and active configuration first. |
| Automated merges damage relationships or history | Require human review and controlled merge authority. |
| Operational teams receive an unactionable queue | Agree prioritisation, capacity and ownership before use. |
| Raw ACNs are copied into GitHub | Store only definitions, logic, summaries and caveats. |

## Workshop decision record

| Decision | Outcome | Owner | Date | Status |
|---|---|---|---|---|
| Eligible Organisation Account population |  |  |  | Open |
| Legal entity types requiring an ACN |  |  |  | Open |
| Authoritative ACN field |  |  |  | Open |
| Minimum ACN inclusion criteria |  |  |  | Open |
| Normalisation logic |  |  |  | Open |
| Excluded and placeholder values |  |  |  | Open |
| ABN-to-ACN cross-field treatment |  |  |  | Open |
| Legitimate repeated-ACN scenarios |  |  |  | Open |
| Account hierarchy treatment |  |  |  | Open |
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
- the eligible Organisation Account population is explicit;
- legal entity types expected to hold an ACN are defined;
- the authoritative ACN field is confirmed;
- minimum ACN inclusion criteria are documented;
- normalisation logic is agreed;
- exclusions and exceptions are approved;
- ABN-to-ACN cross-field treatment is defined;
- account-hierarchy treatment is defined;
- the reporting unit is explicit;
- source fields and grain are confirmed;
- numerator and denominator are compatible;
- Salesforce and Plauti overlap has been assessed;
- operational review ownership is assigned;
- merge authority and controls are defined;
- test cases include duplicate companies, legitimate multi-account structures, invalid values, cross-field errors and exceptions;
- privacy, records, security and governance needs have been considered;
- rule versioning is established;
- permitted uses are documented; and
- the decision is recorded in the decision log.

## Current assessment

**Status:** Technically calculated in the pilot but not ready for governed implementation.

**Reason:** ACN eligibility, inclusion criteria, legal entity classification, legitimate repeated-ACN scenarios, reporting grain, tool boundaries and operational ownership remain unresolved.

**Slide-safe wording:** Not available.

**Permitted current use:** Workshop preparation, exploratory profiling and refinement of the pilot uniqueness rule only.

## Related repository pages

- `01-discover/databricks-customer-data-quality-pilot-input.md`
- `02-define/rules/CAM-DQ-004-abn-completeness.md`
- `02-define/rules/CAM-DQ-005-acn-completeness.md`
- `02-define/rules/CAM-DQ-006-repeated-abn.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `02-define/crm-data-quality-rule-refinement-workshop.md`
- `01-discover/evidence-gaps.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`
