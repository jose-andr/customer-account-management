# CRM data-quality rule register

Status: In progress  
Owner: José Andrade  
Current stage: Define  
Last updated: 30 July 2026

## Purpose

This register tracks the business refinement, ownership, technical alignment and implementation readiness of CRM data-quality rules.

It is used to:

- convert rule ideas into clear business definitions;
- distinguish Salesforce, Plauti, Databricks and operational-review responsibilities;
- assign ownership;
- identify valid exceptions;
- define safe measures;
- record unresolved questions;
- prioritise implementation;
- link detailed rule definitions;
- distinguish technical execution from governed use; and
- approve, refine, validate, park, reject or supersede rules.

The detailed working rule inventory remains in Confluence:

[Salesforce Data Quality Rules](https://jira-cityofmelbourne.atlassian.net/wiki/spaces/DP/pages/527597570/Salesforce+Data+Quality+Rules)

This register records decision-relevant refinement outcomes rather than duplicating the full Confluence rule table.

## Source boundaries

| Source | Purpose |
|---|---|
| Salesforce Data Quality Rules Confluence page | Current working rule inventory and technical details |
| Plauti Duplicate Check Configuration | Existing operational duplicate-detection configuration |
| Databricks data-quality pilot | Exploratory rule execution, profiling and diagnostic outputs |
| Power BI data-quality dashboard | Presentation of pilot outputs |
| `cx-current-state-sop-mapping` | Current duplicate-review and remediation practices |
| Individual rule pages in `02-define/rules/` | Detailed business definitions, caveats and decision records |
| This register | Rule portfolio status, ownership, decisions and implementation readiness |

## Current position

The first seven priority rule-definition pages have been created.

The initial Databricks customer data-quality pilot has also demonstrated that selected completeness, validity, similarity and uniqueness checks can be technically executed.

This does not mean that:

- the business definitions are approved;
- the Databricks implementation matches the intended business logic;
- the pilot dashboard results are governed;
- eligible populations and denominators are confirmed;
- operational remediation is ready;
- duplicate signals are confirmed duplicates; or
- the measures are suitable for executive reporting.

The seven priority rules remain in business refinement.

## Databricks pilot evidence

The initial Databricks and Power BI customer data-quality pilot is an exploratory evidence input.

Related evidence page:

`../01-discover/databricks-customer-data-quality-pilot-input.md`

The pilot may be used to:

- identify rules requiring refinement;
- validate source fields and technical logic;
- test population, grain and denominator assumptions;
- review rule taxonomy;
- compare Databricks and Plauti responsibilities;
- prepare refinement workshops; and
- identify candidate diagnostic priorities.

The pilot must not currently be used to:

- claim that overall customer data quality is approximately 95.9%;
- report confirmed duplicate rates;
- establish performance targets;
- compare teams or services;
- approve automated merges;
- make customer-level decisions; or
- present governed executive measures.

## Pilot calculation issues

The pilot requires further validation because:

- the Full Records and All Attributes views show different tested totals;
- the meaning of `records tested` is not yet confirmed;
- Account and Contact rule executions may use different grains;
- completeness, validity and uniqueness may use different eligible populations;
- duplicate and similarity rules may be classified under validity;
- blank and excluded-record treatment is unclear;
- multiple rules may test the same record;
- high-volume rules may dominate the overall result; and
- rule versions and execution timing are not yet visible.

The overall pilot pass rate is therefore exploratory and not decision-safe.

## Status definitions

### Definition status

| Status | Meaning |
|---|---|
| Proposed | Initial rule or business question |
| In refinement | Business meaning, scope, exceptions or ownership are incomplete |
| In review | Business and technical owners are actively reviewing the definition |
| Business definition agreed | Population, purpose, logic and exceptions are agreed |
| Ready for implementation | Business definition is complete and approved for technical implementation |
| Parked | Not currently progressing |
| Rejected | Reviewed and not required |
| Superseded | Replaced by another rule |
| Retired | No longer required |

### Execution status

| Status | Meaning |
|---|---|
| Not started | No technical implementation has begun |
| In development | Logic is being created |
| Implemented | Logic exists but is not necessarily scheduled |
| Scheduled | Rule runs at an agreed frequency |
| Results under review | Results exist but are not yet validated or governed |
| Validated | Logic and outputs are approved for the stated use |
| Failed | Rule cannot currently run reliably |
| Retired | Rule is no longer active |

### Governed-use status

| Status | Meaning |
|---|---|
| Not ready | Rule is not approved for governed use |
| Exploratory only | Rule may support profiling and refinement |
| Governed for diagnostic use | Rule is approved for controlled monitoring |
| Governed for operational use | Rule is approved to support operational action |
| Approved for reporting | Rule definition, calculation and wording are approved for reporting |
| Superseded | Governed use has moved to another rule |
| Retired | Rule is no longer used |

Technical execution alone does not change definition or governed-use status.

## Priority rule register

| Rule ID | Rule name | Primary control | Quality category | Definition status | Execution status | Governed-use status | Priority | Business owner |
|---|---|---|---|---|---|---|---|---|
| CAM-DQ-001 | Minimum valid contact method | Salesforce / Databricks | Completeness and usability | In refinement | Pilot relationship to validate | Not ready | Critical | To confirm |
| CAM-DQ-002 | Exact email duplicate signal | Plauti / Databricks | Duplicate signal | In refinement | Results under review | Not ready | Critical | To confirm |
| CAM-DQ-003 | Exact mobile duplicate signal | Plauti / Databricks | Duplicate signal | In refinement | Results under review | Not ready | Critical | To confirm |
| CAM-DQ-004 | ABN completeness | Salesforce / Databricks | Identifier completeness | In refinement | Results under review | Not ready | High | To confirm |
| CAM-DQ-005 | ACN completeness | Salesforce / Databricks | Identifier completeness | In refinement | Results under review | Not ready | High | To confirm |
| CAM-DQ-006 | Repeated ABN | Plauti / Databricks | Duplicate signal | In refinement | Results under review | Not ready | High | To confirm |
| CAM-DQ-007 | Repeated ACN | Plauti / Databricks | Duplicate signal | In refinement | Results under review | Not ready | High | To confirm |
| CAM-DQ-008 | Person name similarity duplicate signal | Plauti / Databricks | Duplicate signal | Proposed | To confirm | Not ready | Medium | To confirm |
| CAM-DQ-009 | Organisation name duplicate signal | Plauti / Databricks | Duplicate signal | Proposed | To confirm | Not ready | Medium | To confirm |
| CAM-DQ-010 | Trading name duplicate signal | Plauti / Databricks | Duplicate signal | Proposed | To confirm | Not ready | Medium | To confirm |
| CAM-DQ-011 | Primary mobile format | Salesforce / Databricks | Format validity | Proposed | Results under review | Not ready | Medium | To confirm |
| CAM-DQ-012 | Person name character validity | Salesforce / Databricks | Format validity | Proposed | Results under review | Not ready | Medium | To confirm |

## Detailed rule definitions

### Person Account rules

- `rules/CAM-DQ-001-minimum-valid-contact-method.md`
- `rules/CAM-DQ-002-exact-email-duplicate-signal.md`
- `rules/CAM-DQ-003-exact-mobile-duplicate-signal.md`

### Organisation Account rules

- `rules/CAM-DQ-004-abn-completeness.md`
- `rules/CAM-DQ-005-acn-completeness.md`
- `rules/CAM-DQ-006-repeated-abn.md`
- `rules/CAM-DQ-007-repeated-acn.md`

## Pilot-to-rule mapping

| Pilot rule or attribute | Related business rule | Refinement issue |
|---|---|---|
| Email completeness | CAM-DQ-001 | A populated email field is not equivalent to a usable contact method |
| MobilePhone completeness | CAM-DQ-001 | A populated mobile field is not equivalent to a usable contact method |
| Email uniqueness | CAM-DQ-002 | Repeated email is a duplicate signal, not proof of duplicate identity |
| Email similarity threshold `1` | CAM-DQ-002 | Confirm whether this represents exact matching after normalisation |
| Email similarity threshold `0.9` | Future refinement | Define similarity method, threshold meaning and permitted use |
| MobilePhone similarity threshold `1` | CAM-DQ-003 | Confirm whether this represents exact matching after normalisation |
| MobilePhone similarity threshold `0.9` | Future refinement | Define similarity method, threshold meaning and permitted use |
| ABN validity | CAM-DQ-004 | Define eligible organisation types and separate completeness from validity |
| ACN validity | CAM-DQ-005 | Restrict the denominator to entities expected to hold an ACN |
| ABN uniqueness | CAM-DQ-006 | Confirm whether the output counts records, groups or pairs |
| ACN uniqueness | CAM-DQ-007 | Confirm legal-entity eligibility and legitimate multi-account structures |
| Name uniqueness | Future refinement | High false-positive risk without identity and matching context |
| Account Trading Name uniqueness | Future refinement | Repeated trading names may be legitimate |
| Secondary email rules | Future refinement | Confirm field purpose, population and relationship to primary contact rules |
| FirstName and LastName validity | Future refinement | Define accepted characters, international-name handling and operational value |

## CAM-DQ-001 — Minimum valid contact method

Detailed definition:

`rules/CAM-DQ-001-minimum-valid-contact-method.md`

### Business question

For which Person Accounts should the organisation expect at least one valid contact method, and what counts as a valid contact method for that population?

### Working business rule

An eligible Person Account should contain at least one accepted contact method meeting the agreed minimum validity criteria unless an approved exception applies.

### Decisions required

- Which Person Accounts are eligible?
- Is one contact method sufficient?
- Which contact methods qualify?
- What validity criteria apply to each method?
- Does postal address count as a contact method?
- How are representatives or carers handled?
- Which inactive or historical accounts are excluded?
- How are deceased customers treated?
- What approved exceptions apply?
- What action follows a failed result?
- Who owns the rule and remediation pathway?

### Working definition

| Field | Current position |
|---|---|
| Account type | Person Account |
| Population | Eligible Person Accounts — to define |
| Grain | One row per Person Account |
| Candidate attributes | Primary email, secondary email, mobile, phone and postal address |
| Failure condition | No accepted contact method meets the agreed minimum criteria |
| Exclusions | To define |
| Exceptions | To define |
| Numerator | Eligible Person Accounts with no accepted valid contact method |
| Denominator | All eligible Person Accounts after approved exclusions |
| Output unit | Count and percentage |
| Primary control | Salesforce prevention and Databricks monitoring |
| Action on failure | To define |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |
| Governed-use status | Not ready |

### Pilot relationship

The pilot reports very high email and mobile completeness.

These results may measure field presence only.

They must not be interpreted as usable contact coverage until format, currency, consent, verification, exceptions and account eligibility are agreed.

## CAM-DQ-002 — Exact email duplicate signal

Detailed definition:

`rules/CAM-DQ-002-exact-email-duplicate-signal.md`

### Business question

Which eligible Person Accounts share the same normalised email address, and which matches should be reviewed as potential duplicates?

### Working business rule

Two or more eligible Person Accounts containing the same normalised email address should be flagged as potential duplicates after agreed exclusions and exception rules are applied.

Matching name or other identity attributes may strengthen or weaken the signal during review.

They are not mandatory parts of the initial exact-email signal unless explicitly approved.

### Decisions required

- Which email fields are included?
- How is email normalised?
- Which invalid, test or placeholder values are excluded?
- How are shared household email addresses handled?
- How are representatives, guardians or carers handled?
- Are inactive accounts included?
- Is the output counted as records, pairs or duplicate groups?
- Does the logic align with current Plauti scenarios?
- What review outcome confirms or rejects a duplicate?
- Who owns operational review and merge decisions?

### Working definition

| Field | Current position |
|---|---|
| Account type | Person Account |
| Population | Eligible Person Accounts with an included email value |
| Grain | To confirm: records, pairs or duplicate groups |
| Attribute | Normalised email address |
| Supporting evidence | Name, date of birth, mobile, address and account history where approved |
| Failure condition | Same normalised email across two or more eligible Person Accounts |
| Exclusions | Invalid, test, placeholder and approved shared-contact scenarios |
| Numerator | To define according to selected reporting unit |
| Denominator | Required only where a rate is reported |
| Output unit | Records, groups or pairs — to confirm |
| Primary control | Plauti detection and Databricks monitoring |
| Action on failure | Operational review |
| Business owner | To confirm |
| Operational owner | Customer Data and Systems Support — to confirm |
| Technical owner | To confirm |
| Definition status | In refinement |
| Governed-use status | Not ready |

### Pilot relationship

The pilot reports email uniqueness of approximately 86.02%.

This must not be interpreted as a confirmed duplicate rate.

The pilot logic, normalisation, grain, denominator, similarity thresholds and overlap with Plauti remain to be validated.

## CAM-DQ-003 — Exact mobile duplicate signal

Detailed definition:

`rules/CAM-DQ-003-exact-mobile-duplicate-signal.md`

### Business question

Which eligible Person Accounts share the same normalised mobile number, and which matches should be reviewed as potential duplicates?

### Working business rule

Two or more eligible Person Accounts containing the same normalised mobile number should be flagged as potential duplicates after agreed exclusions and exception rules are applied.

Matching name or other identity attributes may strengthen or weaken the signal during review.

They are not mandatory parts of the initial exact-mobile signal unless explicitly approved.

### Decisions required

- Which mobile and telephone fields are included?
- How are numbers normalised?
- Are international numbers included?
- How are shared family numbers handled?
- How are carers, guardians or representatives handled?
- How are recycled mobile numbers treated?
- Are landline and mobile fields compared?
- Are inactive accounts included?
- Is the output counted as records, pairs or duplicate groups?
- Does the rule align with the current Plauti scenario?
- Who owns operational review and merge decisions?

### Working definition

| Field | Current position |
|---|---|
| Account type | Person Account |
| Population | Eligible Person Accounts with an included mobile value |
| Grain | To confirm: records, pairs or duplicate groups |
| Attribute | Normalised mobile number |
| Supporting evidence | Name, date of birth, email, address, account history and timing where approved |
| Failure condition | Same normalised mobile across two or more eligible Person Accounts |
| Exclusions | Invalid, test, placeholder and approved shared-number scenarios |
| Numerator | To define according to selected reporting unit |
| Denominator | Required only where a rate is reported |
| Output unit | Records, groups or pairs — to confirm |
| Primary control | Plauti detection and Databricks monitoring |
| Action on failure | Operational review |
| Business owner | To confirm |
| Operational owner | Customer Data and Systems Support — to confirm |
| Technical owner | To confirm |
| Definition status | In refinement |
| Governed-use status | Not ready |

### Pilot relationship

The pilot includes mobile similarity rules with thresholds of `0.9` and `1`.

The business meaning of those thresholds, the normalisation logic and the reporting grain remain to be confirmed.

A mobile match is a duplicate signal only.

## CAM-DQ-004 — ABN completeness

Detailed definition:

`rules/CAM-DQ-004-abn-completeness.md`

### Business question

Which Organisation Accounts are expected to have an ABN, and what proportion of that eligible population does not contain an ABN meeting the agreed minimum criteria?

### Working business rule

An eligible Organisation Account should contain an ABN meeting the agreed minimum criteria when its organisation type requires one, unless an approved exception applies.

### Decisions required

- Which Organisation Account types require an ABN?
- Which entity types are exempt?
- Are government, community, international or informal entities excluded?
- Are inactive or historical accounts excluded?
- Is the minimum test presence, structural format, checksum validity or external verification?
- How are unclassifiable accounts treated?
- Is a blank ABN a defect or approved exception?
- Who owns correction and classification review?

### Working definition

| Field | Current position |
|---|---|
| Account type | Organisation Account |
| Population | Eligible Organisation Accounts expected to hold an ABN |
| Grain | One row per Organisation Account |
| Attribute | Authoritative ABN field — to confirm |
| Failure condition | ABN does not meet the agreed minimum criteria |
| Exclusions | Organisation types not expected to hold an ABN |
| Exceptions | To define |
| Numerator | Eligible accounts without an ABN meeting minimum criteria |
| Denominator | All eligible Organisation Accounts expected to hold an ABN |
| Output unit | Count and percentage |
| Primary control | Salesforce prevention and Databricks monitoring |
| Action on failure | Review, classification and correction |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |
| Governed-use status | Not ready |

### Pilot relationship

The pilot reports ABN validity of approximately 81.80%.

This result must not be interpreted until the eligible population, minimum assessment level, treatment of blanks, exceptions and organisation classifications are agreed.

## CAM-DQ-005 — ACN completeness

Detailed definition:

`rules/CAM-DQ-005-acn-completeness.md`

### Business question

Which Organisation Accounts are expected to have an ACN, and what proportion of that eligible population does not contain an ACN meeting the agreed minimum criteria?

### Working business rule

An eligible Organisation Account representing an entity expected to hold an ACN should contain an ACN meeting the agreed minimum criteria unless an approved exception applies.

### Decisions required

- Which legal entity types require an ACN?
- Which entities do not have an ACN?
- How are sole traders, partnerships, trusts, government entities and international organisations treated?
- Is an ABN sufficient for some account types?
- Are inactive, deregistered or historical accounts excluded?
- Is the minimum test presence, structural format, checksum validity or external verification?
- How are ABNs entered in the ACN field treated?
- Who validates legal entity classification?
- Who corrects missing or invalid values?

### Working definition

| Field | Current position |
|---|---|
| Account type | Organisation Account |
| Population | Eligible Organisation Accounts expected to hold an ACN |
| Grain | One row per Organisation Account |
| Attribute | Authoritative ACN field — to confirm |
| Failure condition | ACN does not meet the agreed minimum criteria |
| Exclusions | Entity types not expected to hold an ACN |
| Exceptions | To define |
| Numerator | Eligible accounts without an ACN meeting minimum criteria |
| Denominator | All eligible Organisation Accounts expected to hold an ACN |
| Output unit | Count and percentage |
| Primary control | Salesforce prevention and Databricks monitoring |
| Action on failure | Review, classification and correction |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |
| Governed-use status | Not ready |

### Pilot relationship

The pilot reports ACN validity of approximately 56.59%.

This must not be interpreted as the proportion of companies with invalid ACNs.

The eligible company population, assessment level, blank treatment, classification logic and denominator remain unresolved.

## CAM-DQ-006 — Repeated ABN

Detailed definition:

`rules/CAM-DQ-006-repeated-abn.md`

### Business question

Which eligible Organisation Accounts share the same normalised ABN, and which repeated values require review as potential duplicate organisation records?

### Working business rule

Two or more eligible Organisation Accounts sharing the same normalised ABN should be flagged for review after agreed validity, exclusion and exception rules are applied.

### Decisions required

- What minimum ABN validity level is required before matching?
- Can one ABN legitimately relate to multiple CRM accounts?
- Can branches, locations or service relationships justify separate accounts?
- Are inactive or historical records included?
- How are merged or superseded records treated?
- Is the output counted as records, pairs or duplicate groups?
- Should legal or trading name be used as supporting evidence?
- Does the rule align with Plauti?
- Who reviews, confirms and authorises merges?

### Working definition

| Field | Current position |
|---|---|
| Account type | Organisation Account |
| Population | Eligible Organisation Accounts with an ABN meeting minimum inclusion criteria |
| Grain | To confirm: records, pairs or duplicate groups |
| Attribute | Normalised ABN |
| Supporting evidence | Legal name, trading name, classification, hierarchy, address and account history |
| Failure condition | Same normalised ABN across multiple eligible Organisation Accounts |
| Exclusions | Invalid identifiers and approved multi-account structures |
| Numerator | To define according to selected reporting unit |
| Denominator | Required only where a rate is reported |
| Output unit | Records, groups or pairs — to confirm |
| Primary control | Plauti detection and Databricks monitoring |
| Action on failure | Operational and business review |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |
| Governed-use status | Not ready |

### Pilot relationship

The pilot reports ABN uniqueness of approximately 95.71%.

This does not mean that the remaining records are confirmed duplicate organisations or merge candidates.

The grain, denominator, validity threshold and legitimate shared-ABN structures remain to be confirmed.

## CAM-DQ-007 — Repeated ACN

Detailed definition:

`rules/CAM-DQ-007-repeated-acn.md`

### Business question

Which eligible Organisation Accounts share the same normalised ACN, and which repeated values require review as potential duplicate company records?

### Working business rule

Two or more eligible Organisation Accounts sharing the same normalised ACN should be flagged for review after agreed validity, exclusion and exception rules are applied.

### Decisions required

- Which legal entity types enter the population?
- What minimum ACN validity level is required before matching?
- Can a company legitimately have multiple CRM accounts?
- Can branches, locations or service relationships justify separate accounts?
- Are inactive, deregistered or historical records included?
- How are probable ABNs entered in the ACN field treated?
- Is the output counted as records, pairs or duplicate groups?
- Should legal name or ABN be used as supporting evidence?
- Does the rule align with Plauti?
- Who reviews, confirms and authorises merges?

### Working definition

| Field | Current position |
|---|---|
| Account type | Organisation Account |
| Population | Eligible Organisation Accounts expected to hold an ACN and containing an ACN meeting minimum inclusion criteria |
| Grain | To confirm: records, pairs or duplicate groups |
| Attribute | Normalised ACN |
| Supporting evidence | Legal name, ABN, classification, hierarchy, address and account history |
| Failure condition | Same normalised ACN across multiple eligible Organisation Accounts |
| Exclusions | Invalid identifiers and approved multi-account structures |
| Numerator | To define according to selected reporting unit |
| Denominator | Required only where a rate is reported |
| Output unit | Records, groups or pairs — to confirm |
| Primary control | Plauti detection and Databricks monitoring |
| Action on failure | Operational and business review |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |
| Governed-use status | Not ready |

### Pilot relationship

The pilot reports ACN uniqueness of approximately 90.77%.

This does not mean that the remaining records are confirmed duplicate companies or merge candidates.

Legal entity eligibility, identifier validity, reporting grain, denominator and legitimate multi-account structures remain to be confirmed.

## Lower-priority rule backlog

| Rule ID | Rule | Primary unresolved issue | Status |
|---|---|---|---|
| CAM-DQ-008 | Person name similarity duplicate signal | Appropriate threshold, international names and false-positive risk | Proposed |
| CAM-DQ-009 | Organisation name duplicate signal | Name normalisation and valid multi-account structures | Proposed |
| CAM-DQ-010 | Trading name duplicate signal | Shared trading names and legal-entity relationships | Proposed |
| CAM-DQ-011 | Primary mobile format | International-number support and minimum validity logic | Proposed |
| CAM-DQ-012 | Person name character validity | Valid punctuation, diacritics and international-name handling | Proposed |

The following pilot checks also remain outside the first priority cycle:

- secondary email completeness;
- secondary email similarity;
- personal email uniqueness;
- phone similarity;
- customer number uniqueness;
- first-name format;
- last-name format;
- name uniqueness; and
- trading-name uniqueness.

These should not progress until repeated use shows that they are decision-relevant and the first refinement cycle establishes a workable pattern.

## Shared refinement decisions

Before any rule moves beyond business refinement, confirm the following.

### Business definition

- business question;
- intended decision or operational use;
- eligible population;
- approved exclusions;
- legitimate exceptions;
- minimum rule criteria; and
- failure categories.

### Metric structure

- source object or governed table;
- source field;
- entity grain;
- numerator;
- denominator;
- period;
- filters;
- rule version;
- calculation frequency; and
- result unit.

### Technical alignment

- current Databricks logic;
- current Salesforce control;
- current Plauti configuration where relevant;
- normalisation logic;
- rule thresholds;
- output structure;
- page filters;
- blank and exclusion handling; and
- reconciliation with the pilot dashboard.

### Operating model

- business rule owner;
- operational owner;
- technical owner;
- review or remediation pathway;
- exception authority;
- merge authority where applicable;
- escalation pathway; and
- operational capacity.

### Permitted use

Each rule must be explicitly approved for one or more of the following:

- exploratory profiling;
- diagnostic monitoring;
- operational review;
- preventative control;
- remediation prioritisation;
- governed reporting; or
- executive communication.

Approval for one use does not imply approval for every use.

## Tool responsibilities

| Capability | Intended role |
|---|---|
| Salesforce validation and duplicate controls | Prevent selected defects and support account search |
| Plauti Duplicate Check | Identify potential duplicates and support operational review |
| Databricks | Measure quality, monitor trends and support root-cause analysis |
| Power BI | Present approved analytical outputs and diagnostics |
| Human review | Confirm identity, assess exceptions and approve corrective action |
| Governance | Define standards, ownership, permitted use and escalation |

Databricks should not automatically reproduce Plauti logic.

Power BI should not present exploratory technical results as governed measures without approved business definitions.

## Duplicate terminology

Use:

- duplicate signal;
- potential duplicate;
- confirmed duplicate;
- rejected match;
- unresolved match;
- approved exception;
- merge candidate; and
- merged.

Do not call records duplicates solely because they share:

- an email address;
- a mobile number;
- an ABN;
- an ACN;
- a name; or
- a trading name.

## Numerator and denominator safety

Every governed rate must use:

- the same eligible population;
- the same entity grain;
- the same account or contact identifier;
- the same period;
- the same inclusion and exclusion logic;
- the same exception treatment;
- the same rule version; and
- compatible numerator and denominator definitions.

Do not combine:

- account records with contact records;
- duplicate groups with record counts;
- duplicate pairs with group counts;
- recent failures with a total historical population;
- reviewed signals with records that were never reviewed; or
- identifier failures with entities not expected to hold the identifier.

A result may be technically calculated but still unsafe for decision-making or presentation.

## Workshop decision table

Use this table during the refinement session.

| Rule ID | Business definition agreed | Population agreed | Grain agreed | Exceptions agreed | Owner assigned | Technical logic checked | Plauti alignment checked | Decision |
|---|---|---|---|---|---|---|---|---|
| CAM-DQ-001 | No | No | Yes | No | No | No | Not applicable | In refinement |
| CAM-DQ-002 | No | No | No | No | No | No | No | In refinement |
| CAM-DQ-003 | No | No | No | No | No | No | No | In refinement |
| CAM-DQ-004 | No | No | Yes | No | No | No | Not applicable | In refinement |
| CAM-DQ-005 | No | No | Yes | No | No | No | Not applicable | In refinement |
| CAM-DQ-006 | No | No | No | No | No | No | No | In refinement |
| CAM-DQ-007 | No | No | No | No | No | No | No | In refinement |

## Decision outcomes

Use one of the following outcomes for each rule:

| Decision | Meaning |
|---|---|
| Approve | Business definition is ready for the stated next stage |
| Refine | More business definition is required |
| Validate | Current technical configuration or evidence must be checked |
| Govern for diagnostic use | Approved for controlled monitoring |
| Govern for operational use | Approved to support operational action |
| Approve for reporting | Definition, calculation and wording are approved |
| Park | Not currently progressing |
| Reject | Rule is not required |
| Supersede | Another rule replaces it |
| Retire | Rule is no longer required |

## Status progression

Each rule should progress through:

1. Proposed;
2. In refinement;
3. In review;
4. Business definition agreed;
5. Ready for implementation;
6. Technical logic validated;
7. Operational pathway agreed;
8. Governed for diagnostic use;
9. Governed for operational use, where applicable;
10. Approved for reporting, where applicable; or
11. Superseded or retired.

Technical execution alone does not move a rule through this sequence.

## First refinement-cycle scope

The first refinement session will focus on:

1. CAM-DQ-001 — Minimum valid contact method;
2. CAM-DQ-002 — Exact email duplicate signal;
3. CAM-DQ-003 — Exact mobile duplicate signal;
4. CAM-DQ-004 — ABN completeness;
5. CAM-DQ-005 — ACN completeness;
6. CAM-DQ-006 — Repeated ABN; and
7. CAM-DQ-007 — Repeated ACN.

## First refinement-cycle completion criteria

The first refinement cycle is complete when:

- all seven business questions have been reviewed;
- eligible populations are explicit;
- source fields and grain are confirmed;
- numerator and denominator definitions are compatible;
- exceptions are approved;
- current Databricks logic has been compared with the agreed definitions;
- Salesforce, Plauti and Databricks responsibilities are explicit;
- operational actions and owners are assigned;
- rule versions are recorded;
- decision-log entries are updated;
- each rule has an explicit permitted use; and
- approved dashboard wording and caveats are available where reporting is permitted.

## Current register assessment

| Assessment | Status |
|---|---|
| Priority rules identified | Complete |
| Detailed draft rule pages | Complete |
| Databricks pilot evidence recorded | Complete |
| Pilot-to-rule mapping recorded | Complete |
| Business definitions approved | Not complete |
| Pilot calculation model reconciled | Not complete |
| Databricks logic validated against business intent | Not complete |
| Plauti alignment checked | Not complete |
| Operational owners assigned | Not complete |
| Remediation pathways agreed | Not complete |
| Governed metrics approved | Not complete |
| Slide-safe wording approved | Not complete |

## Current decision

No rule should be approved for governed reporting or operational use until:

- the business definition is agreed;
- the population and grain are explicit;
- valid exceptions are documented;
- ownership is assigned;
- Salesforce and Plauti alignment is checked where relevant;
- the operational action is clear;
- numerator and denominator definitions are compatible;
- the technical logic has been tested against the business definition;
- the result has been reviewed; and
- permitted use is recorded.

## Next action

Use this register and the individual rule pages in the first business-refinement workshop.

Begin with:

`CAM-DQ-001 — Minimum valid contact method`

Update the workshop decision table, relevant rule page and decision log immediately after each rule decision.

## Related control pages

- `crm-data-quality-rule-refinement-index.md`
- `crm-data-quality-rule-refinement.md`
- `crm-data-quality-rule-refinement-workshop.md`
- `../01-discover/databricks-customer-data-quality-pilot-input.md`
- `../00-project-control/status-and-validation-model.md`
- `../00-project-control/risk-register.md`
- `../06-decisions/decision-log.md`
