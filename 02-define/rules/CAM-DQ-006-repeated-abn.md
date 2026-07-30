# CAM-DQ-006 — Repeated ABN

## Document control

| Field | Value |
|---|---|
| Rule ID | CAM-DQ-006 |
| Rule name | Repeated ABN |
| Rule group | Organisation Account duplicate detection |
| Status | Draft — business refinement required |
| Validation level | Partially validated |
| Current phase | Define |
| Priority | First refinement cycle |
| Governed metric status | Not ready |
| Last updated | 30 July 2026 |

## Purpose

Define how repeated Australian Business Numbers across Organisation Accounts should be identified, measured and reviewed.

This rule produces an organisation-account duplicate signal.

It does not confirm that repeated records represent the same organisation, establish that the ABN belongs to each account, or automatically authorise merging.

## Business question

Which eligible Organisation Accounts share the same normalised ABN, and which repeated values require review as potential duplicate organisation records?

## Decision required

Agree:

1. the eligible Organisation Account population;
2. the authoritative ABN field;
3. minimum ABN validity requirements;
4. ABN normalisation logic;
5. legitimate repeated-ABN scenarios;
6. whether outputs are counted as records, groups or pairs;
7. the relationship between Salesforce, Plauti and Databricks controls;
8. the operational review pathway; and
9. ownership of review, correction and merge decisions.

## Current working definition

> A repeated ABN signal occurs when two or more eligible Organisation Accounts contain the same normalised ABN after agreed validity, exclusion and exception rules have been applied.

This is a working definition only.

A repeated ABN is strong evidence that records may relate to the same legal or operating entity, but it is not sufficient evidence for an automatic merge.

## Why the rule matters

Repeated ABNs may indicate:

- duplicate Organisation Account creation;
- inconsistent account-search practices;
- separate records created for different services;
- migrated or historical duplicates;
- parent and subsidiary relationships recorded incorrectly;
- legal and trading entities being mixed;
- multiple operating locations under one ABN;
- internal or system-generated records;
- an ABN entered against the wrong organisation;
- placeholder or test values; or
- legitimate operating structures requiring separate CRM accounts.

The rule must distinguish likely duplicate accounts from legitimate organisational relationships.

## Scope

This rule applies to Organisation Accounts with an ABN that meets the agreed minimum inclusion criteria.

It must not be applied to:

- Person Accounts;
- blank ABN values;
- values that cannot be safely normalised;
- known test or placeholder values;
- records outside the agreed organisation-account population; or
- approved exceptions.

## Eligible population

### Proposed starting population

Organisation Accounts that:

- are within the agreed Salesforce account population;
- contain an ABN meeting the agreed minimum inclusion criteria;
- are not test, training or system-generated records;
- are not already merged, superseded or excluded under approved logic;
- are within the agreed status or activity period; and
- do not meet an approved exception.

### Population questions

The workshop must determine:

- whether inactive and historical accounts remain in scope;
- whether merged or superseded records remain visible in analysis;
- whether internal organisational accounts are excluded;
- whether international organisations are excluded;
- whether all Organisation Account record types are included;
- whether separate business units or locations may legitimately share an ABN;
- whether account hierarchy fields should affect the rule;
- whether sole traders require different treatment;
- whether related organisations should be analysed separately; and
- whether an activity or recency threshold is required.

## ABN field and validity dependency

The business and technical owners must confirm:

- the authoritative ABN field;
- whether alternate ABN fields exist;
- whether ABN values are stored consistently;
- whether only structurally valid ABNs are included;
- whether checksum validation is required;
- whether externally verified ABNs are treated differently;
- whether blank and placeholder values are excluded; and
- whether conflicting values exist across fields or systems.

The repeated-ABN rule depends on the business decisions recorded in:

`CAM-DQ-004 — ABN completeness`

Do not include malformed or placeholder ABNs in duplicate analysis unless they are reported as a separate diagnostic category.

## ABN normalisation

Candidate normalisation steps requiring technical validation:

1. trim leading and trailing spaces;
2. remove approved formatting characters;
3. retain digits only where safe;
4. preserve leading zeroes;
5. treat blank strings as null;
6. exclude known test and placeholder values;
7. separate values that fail minimum structural criteria; and
8. retain the original source value in the governed environment for operational review.

Do not store raw ABNs or record-level extracts in GitHub.

## Minimum inclusion criteria

Candidate inclusion levels include:

### Level 1 — Present

The ABN field contains a non-blank value.

### Level 2 — Structurally valid

The normalised value contains 11 digits.

### Level 3 — Checksum-valid

The value passes the approved ABN checksum algorithm.

### Level 4 — Externally verified

The ABN has been validated against an approved source.

The selected level must be explicit.

A repeated malformed ABN may indicate a shared data-entry defect rather than a duplicate organisation.

## Legitimate repeated-ABN scenarios

A repeated ABN may be legitimate where:

- multiple operating locations use separate CRM accounts;
- separate service relationships are intentionally represented by separate records;
- a parent entity and trading division share one ABN;
- a sole trader has multiple service-specific accounts;
- a trust or legal structure is represented through more than one operational account;
- account hierarchy requires separate records;
- one account is retained for historical or records purposes;
- migrated records are retained temporarily;
- internal and external account representations coexist;
- a legal entity operates under multiple trading names; or
- merge is unsafe because records have incompatible relationships or service history.

These scenarios must be understood before classifying records as duplicate organisations.

## Rule logic — business expression

The rule should be expressed as:

> Within the eligible Organisation Account population, group records by the agreed normalised ABN and identify groups containing two or more distinct Organisation Account identifiers after approved exclusions have been applied.

The output is a repeated-ABN signal requiring review.

## Signal strength

Repeated ABN is a stronger organisation-identity signal than repeated organisation name alone.

It should still be assessed with other information such as:

- legal name;
- trading name;
- account type;
- organisation classification;
- address;
- account hierarchy;
- service relationships;
- creation source;
- account status;
- related contacts;
- linked transactions;
- previous merge history; and
- approved external verification results.

No merge should occur solely because the ABN matches.

## Salesforce control

### Potential purpose

Salesforce may:

- warn staff when an account with the same ABN already exists;
- support account search before creation;
- prevent selected duplicate-creation scenarios;
- require review before a repeated ABN is saved; or
- record a legitimate exception.

### Current status

Existing Salesforce and Plauti behaviour must be confirmed before proposing changes.

### Questions

- Does Salesforce currently check for repeated ABNs?
- Is the control native, custom or Plauti-managed?
- Does it run on create, update or both?
- Are integrations and imports included?
- Is the control a warning or hard block?
- Are legitimate repeated-ABN scenarios supported?
- Can staff override the control?
- Are override reasons recorded?
- Does the rule use normalised or raw values?
- Are review outcomes stored?

Do not introduce a hard block until legitimate organisational structures are understood.

## Plauti relationship

Plauti may already use ABN as part of Organisation Account duplicate-detection scenarios.

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
| Human review | Organisation confirmation and merge decision |
| Governance | Standards, ownership and escalation |

## Databricks purpose

Databricks may be used to:

- identify Organisation Accounts in repeated-ABN groups;
- estimate the scale of repeated-ABN signals;
- measure group-size distribution;
- compare results across account-creation pathways;
- identify likely upstream causes;
- compare analytical results with Plauti outputs;
- monitor trends over time;
- support sampling and validation; and
- evaluate the effect of preventative controls.

Databricks must not classify repeated ABNs as confirmed duplicates unless governed review outcomes are available.

## Pilot dashboard input

The initial customer data-quality pilot reported ABN uniqueness of approximately 95.71%.

This result is exploratory.

It must not be interpreted as:

- 4.29% of organisations being confirmed duplicates;
- 4.29% of accounts requiring merge; or
- a governed organisation-account duplicate rate.

The result may be affected by:

- unclear organisation-account eligibility;
- invalid or placeholder ABNs;
- record-level versus group-level counting;
- legitimate shared-ABN structures;
- inactive or historical accounts;
- multiple rule executions;
- unclear denominator logic; and
- different treatment of blanks and excluded records.

The pilot result should be used to refine the rule, not to establish a performance baseline.

## Measurement structures

Repeated ABNs may be counted in several ways.

These units are not interchangeable.

### Record count

Number of Organisation Account records belonging to a repeated-ABN group.

### Group count

Number of distinct normalised ABNs shared by two or more Organisation Accounts.

### Pair count

Number of unique record-to-record combinations within repeated-ABN groups.

For a group containing three records:

- record count = 3;
- group count = 1;
- pair count = 3.

Every output must state the reporting unit.

## Proposed primary diagnostic

### Metric name

Organisation Accounts in repeated-ABN groups.

### Metric status

Exploratory only — not governed and not slide-safe.

### Unit

Distinct eligible Organisation Accounts.

### Proposed numerator

Distinct eligible Organisation Accounts belonging to a normalised ABN group containing two or more distinct Organisation Account identifiers.

### Proposed denominator

All distinct eligible Organisation Accounts with an ABN meeting the agreed minimum inclusion criteria.

### Proposed rate

`Numerator ÷ denominator × 100`

This rate measures the proportion of assessable Organisation Accounts that belong to a repeated-ABN group.

It does not measure the proportion of confirmed duplicate organisations.

## Supporting diagnostics

Candidate supporting measures include:

- repeated-ABN group count;
- Organisation Accounts in repeated-ABN groups;
- distribution of group sizes;
- groups containing active accounts only;
- groups containing active and inactive accounts;
- repeated ABNs by account-creation pathway;
- repeated ABNs by account type;
- repeated ABNs by organisation classification;
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

- repeated-ABN groups by account records;
- duplicate pairs by ABN groups;
- reviewed signals by all Organisation Accounts;
- confirmed duplicates by records never reviewed;
- repeated ABNs by all CRM accounts;
- repeated ABNs by accounts with blank or invalid ABNs; or
- recent repeated-ABN signals by the total historical account base.

The numerator and denominator must use:

- the same Organisation Account population;
- the same period;
- the same ABN inclusion criteria;
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
| Authoritative ABN field | Open |
| ABN validity logic | Open |
| Organisation Account record types | Open |
| Legal and trading name fields | Open |
| Organisation classification | Open |
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

1. repeated checksum-valid ABN;
2. repeated structurally valid ABN;
3. repeated malformed ABN;
4. repeated placeholder value;
5. likely legitimate shared-ABN structure;
6. potential duplicate organisation;
7. confirmed duplicate;
8. rejected match;
9. unresolved match;
10. approved exception;
11. merge candidate;
12. merged; and
13. excluded record.

These categories must not be collapsed where they imply different actions.

## Operational review

Each repeated-ABN signal should move through a controlled review pathway.

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

- whether the records represent the same legal entity;
- whether separate records are operationally required;
- whether the legal and trading names are consistent;
- whether the ABN belongs to each account;
- whether one record is historical or superseded;
- whether account hierarchy explains the repetition;
- which record should be retained;
- whether records can be safely merged;
- whether service, relationship or transaction history may be affected;
- whether legal, privacy, records or security constraints apply;
- whether related records must be updated; and
- whether the creation pathway can be improved.

## Operational response

Possible actions include:

- confirm a legitimate exception;
- correct an incorrectly entered ABN;
- update organisation classification;
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
| Repeated ABNs are labelled as confirmed duplicates | Use duplicate-signal terminology throughout. |
| Legitimate organisational structures are treated as defects | Define exceptions and account-hierarchy rules. |
| Invalid or placeholder ABNs create false groups | Apply minimum validity criteria before matching. |
| Record, group and pair counts are confused | State the unit and grain with every result. |
| ABN ownership is assumed from field presence | Keep field value, structural validity and verification separate. |
| Historical records distort current-state reporting | Agree status and period logic. |
| Databricks duplicates existing Plauti functionality | Compare tool purposes and active configuration first. |
| Automated merges damage relationships or history | Require human review and controlled merge authority. |
| Operational teams receive an unactionable queue | Agree prioritisation, capacity and ownership before use. |
| Raw ABNs are copied into GitHub | Store only definitions, logic, summaries and caveats. |

## Workshop decision record

| Decision | Outcome | Owner | Date | Status |
|---|---|---|---|---|
| Eligible Organisation Account population |  |  |  | Open |
| Authoritative ABN field |  |  |  | Open |
| Minimum ABN inclusion criteria |  |  |  | Open |
| Normalisation logic |  |  |  | Open |
| Excluded and placeholder values |  |  |  | Open |
| Legitimate shared-ABN scenarios |  |  |  | Open |
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
- the authoritative ABN field is confirmed;
- minimum ABN inclusion criteria are documented;
- normalisation logic is agreed;
- exclusions and exceptions are approved;
- account-hierarchy treatment is defined;
- the reporting unit is explicit;
- source fields and grain are confirmed;
- numerator and denominator are compatible;
- Salesforce and Plauti overlap has been assessed;
- operational review ownership is assigned;
- merge authority and controls are defined;
- test cases include duplicates, legitimate shared-ABN structures, invalid values and exceptions;
- privacy, records, security and governance needs have been considered;
- rule versioning is established;
- permitted uses are documented; and
- the decision is recorded in the decision log.

## Current assessment

**Status:** Technically calculated in the pilot but not ready for governed implementation.

**Reason:** ABN inclusion criteria, eligible population, legitimate shared-ABN scenarios, reporting grain, tool boundaries and operational ownership remain unresolved.

**Slide-safe wording:** Not available.

**Permitted current use:** Workshop preparation, exploratory profiling and refinement of the pilot uniqueness rule only.

## Related repository pages

- `01-discover/databricks-customer-data-quality-pilot-input.md`
- `02-define/rules/CAM-DQ-004-abn-completeness.md`
- `02-define/rules/CAM-DQ-005-acn-completeness.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `02-define/crm-data-quality-rule-refinement-workshop.md`
- `01-discover/evidence-gaps.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`
