# CAM-DQ-005 — ACN completeness

## Document control

| Field | Value |
|---|---|
| Rule ID | CAM-DQ-005 |
| Rule name | ACN completeness |
| Rule group | Organisation Account identifier completeness |
| Status | Draft — business refinement required |
| Validation level | Partially validated |
| Current phase | Define |
| Priority | First refinement cycle |
| Governed metric status | Not ready |
| Last updated | 30 July 2026 |

## Purpose

Define when an eligible Organisation Account should contain an Australian Company Number and how missing or unusable ACN values should be identified.

This rule is a completeness diagnostic.

It does not establish that every Organisation Account must have an ACN, confirm that a recorded ACN belongs to the organisation, or approve external verification.

## Business question

Which Organisation Accounts are expected to have an ACN, and what proportion of that eligible population does not contain an ACN meeting the agreed minimum criteria?

## Decision required

Agree:

1. the eligible Organisation Account population;
2. which organisation types require an ACN;
3. legitimate exceptions;
4. minimum ACN presence and format criteria;
5. whether external verification is in scope;
6. the relationship between Salesforce controls and Databricks measurement;
7. the action required when an account fails the rule; and
8. business, operational and technical ownership.

## Current working definition

> An eligible Organisation Account representing an Australian company should contain an ACN meeting the agreed minimum criteria unless an approved exception applies.

This is a working definition only.

The business must first determine which Organisation Accounts represent entities expected to hold an ACN.

## Why the rule matters

Missing or unusable ACN information may:

- reduce confidence in company-account identification;
- make it harder to distinguish companies with similar names;
- contribute to duplicate account creation;
- weaken account matching across systems;
- create avoidable staff investigation;
- affect reporting by legal entity type;
- limit safe comparison with external registers; and
- reduce confidence in customer account quality measures.

An ACN being present does not prove that it is current, valid or associated with the correct company.

## Scope

This rule applies only to Organisation Accounts representing entities expected to hold an ACN.

It must not be applied to:

- Person Accounts;
- sole traders;
- partnerships;
- trusts without a company structure;
- incorporated associations that do not hold an ACN;
- government entities that do not hold an ACN;
- informal community groups;
- international organisations without an Australian company registration; or
- other entity types not expected to hold an ACN.

The source object, account types and record types must be confirmed before implementation.

## Eligible population

### Proposed starting population

Organisation Accounts that:

- are within the agreed Salesforce account population;
- are classified as an Australian company or another entity type expected to hold an ACN;
- are not test, training or system-generated records;
- are not merged, superseded or excluded under approved logic;
- are within the agreed status or activity period; and
- do not meet an approved exception.

### Population questions

The workshop must determine:

- which Organisation Account record types are in scope;
- which legal entity types require an ACN;
- whether proprietary and public companies are treated differently;
- whether registered Australian bodies with an ARBN are excluded or handled separately;
- whether subsidiaries and related entities require separate records;
- whether inactive, deregistered or historical companies remain in scope;
- how internal organisational records are treated;
- how temporary or incomplete accounts are treated;
- how international companies are classified;
- whether an activity or recency threshold is required; and
- whether company classification is sufficiently reliable for reporting.

## Organisation-type dependency

ACN completeness cannot be measured safely until legal-entity classifications are sufficiently reliable.

The rule may depend on fields such as:

- Organisation Account record type;
- legal entity type;
- company or business classification;
- registration type;
- jurisdiction;
- country;
- active status;
- internal or external organisation indicator; and
- Australian company indicator.

If classifications are incomplete or inconsistent, outputs should separate:

1. accounts clearly expected to have an ACN;
2. accounts clearly exempt;
3. accounts requiring classification review; and
4. accounts that cannot be assessed.

Do not treat unclassifiable accounts as confirmed ACN failures.

## ACN field

The business and technical owners must confirm:

- the authoritative ACN field;
- whether alternate ACN fields exist;
- whether the value is stored as text or number;
- whether formatting characters are retained;
- whether leading zeroes can be preserved;
- whether legacy or migrated fields remain in use;
- whether related objects also hold an ACN; and
- how conflicting values are treated.

Do not combine multiple ACN fields without documenting their meaning and precedence.

## Minimum criteria

The initial rule may include several levels of assessment.

### Level 1 — Presence

The authoritative ACN field contains a non-blank value.

### Level 2 — Structural format

The normalised value contains nine digits.

### Level 3 — Checksum validity

The value passes the approved ACN checksum algorithm.

### Level 4 — External verification

The value is verified against an approved external source.

These levels are not interchangeable.

A presence measure must not be described as valid ACN coverage.

A structurally valid ACN must not be described as belonging to the company unless ownership has been verified.

## ACN normalisation

Candidate normalisation steps requiring technical validation:

1. trim leading and trailing spaces;
2. remove spaces and approved formatting characters;
3. retain digits only where safe;
4. preserve leading zeroes;
5. treat blank strings as null;
6. exclude known placeholder and test values;
7. separate values that cannot be normalised; and
8. retain the original source value in the governed source environment for review.

Do not store raw ACNs or record-level extracts in GitHub.

## Candidate invalid values

Potential invalid or unusable values include:

- blank or null values;
- values containing fewer or more than nine digits;
- alphabetic characters;
- repeated placeholder digits;
- all-zero values;
- known test values;
- multiple ACNs entered into one field;
- text such as “unknown” or “not applicable”;
- ABNs incorrectly entered into the ACN field;
- values that fail the approved checksum; and
- values known to be obsolete or incorrect.

The treatment of each category must be documented.

## Candidate exceptions

Potential exceptions requiring validation include:

- the organisation is not an Australian company;
- sole trader;
- partnership;
- trust;
- incorporated association without an ACN;
- government entity;
- informal or unincorporated group;
- international organisation;
- registered Australian body using an ARBN rather than an ACN;
- internal organisational account;
- account retained only for records purposes;
- temporary record awaiting classification or verification;
- company has been deregistered;
- ACN is held in another governed system and is not expected in Salesforce;
- legal or operational constraint prevents collection; and
- account classification is unresolved.

Exceptions must be explicit, measurable and approved.

## Rule logic — business expression

The rule should be expressed as:

> Within the eligible Organisation Account population expected to hold an ACN, identify accounts where the authoritative ACN field does not meet the agreed minimum criteria and no approved exception applies.

The minimum criteria must be named in every output.

Examples:

- ACN missing;
- ACN present but structurally invalid;
- ACN present and checksum-valid;
- ACN externally verified.

Do not combine these into one undifferentiated measure.

## Relationship between ABN and ACN

ABN and ACN are related but not interchangeable.

The rule-refinement process must confirm:

- whether the organisation type should hold an ACN;
- whether the organisation should also hold an ABN;
- whether the ABN contains the ACN as part of its structure;
- whether values entered in the wrong field can be detected;
- whether one identifier may be present while the other is legitimately absent; and
- whether cross-field checks are useful and safe.

Do not infer a missing ACN from an ABN without approved technical and business logic.

Do not treat all ABN holders as companies.

## Salesforce control

### Potential purpose

Salesforce may:

- require an ACN for selected company record types;
- apply format or checksum validation;
- provide guidance when an ACN is not applicable;
- support an approved exception value;
- prevent placeholder values;
- detect likely ABNs entered in the ACN field; or
- prompt staff to confirm legal-entity classification.

### Current status

Existing Salesforce validation rules and operational practices must be confirmed before proposing changes.

### Questions

- Is ACN currently mandatory for any record types?
- Which legal-entity classifications trigger the requirement?
- Does Salesforce validate length, characters or checksum?
- Does Salesforce detect ABNs entered into the ACN field?
- Are integrations and imports subject to the same control?
- Are legacy records exempt?
- Can staff record an approved exception?
- Would a hard validation rule prevent legitimate service access?
- Who owns changes to the control?
- Is company verification performed elsewhere?

A hard validation rule should not be implemented until legitimate exceptions are understood.

## Databricks purpose

Databricks may be used to:

- establish an exploratory ACN completeness baseline;
- separate missing, malformed and checksum-invalid values;
- identify likely ABNs entered in the ACN field;
- identify accounts that cannot be assessed because legal-entity type is unclear;
- measure trends over time;
- compare account-creation pathways;
- support root-cause analysis;
- monitor the effect of Salesforce controls; and
- identify records requiring classification or operational review.

Databricks should not become the source of the business definition.

## Pilot dashboard input

The initial customer data-quality pilot reported an ACN validity result of approximately 56.59%.

This result is exploratory and must not be interpreted as evidence that 43.41% of companies have invalid ACNs.

The result may include:

- organisation types not expected to hold an ACN;
- missing ACNs;
- incorrectly classified accounts;
- historical or inactive records;
- blank values included in validity;
- ABNs entered into ACN fields;
- accounts outside the intended company population; and
- rule executions using an unclear denominator.

The pilot result should be used to refine the business population and failure categories before governed reporting.

## Proposed primary diagnostic

### Metric name

Eligible Organisation Accounts without an ACN meeting minimum criteria.

### Metric status

Exploratory only — not governed and not slide-safe.

### Unit

Distinct eligible Organisation Accounts.

### Proposed numerator

Distinct eligible Organisation Accounts expected to hold an ACN where:

- the authoritative ACN field does not meet the agreed minimum criteria; and
- no approved exception applies.

### Proposed denominator

All distinct eligible Organisation Accounts expected to hold an ACN after approved exclusions.

### Proposed rate

`Numerator ÷ denominator × 100`

The denominator must exclude organisation types not expected to hold an ACN.

## Supporting diagnostics

Candidate supporting measures include:

- accounts with no ACN value;
- accounts with an ACN value of incorrect length;
- accounts containing non-numeric ACN characters;
- accounts failing checksum validation;
- accounts containing a likely ABN in the ACN field;
- accounts with a structurally valid ACN;
- accounts externally verified;
- accounts with an approved exception;
- accounts requiring legal-entity classification;
- accounts not assessable;
- failures by creation pathway;
- failures by account status;
- failures by legal entity type; and
- failures by rule version.

Each measure must state its grain, population and criteria.

## Denominator safety

Do not divide:

- missing ACNs by all CRM accounts;
- Organisation Account failures by a denominator containing Person Accounts;
- ACN failures by all ABN holders;
- checksum failures by accounts with no ACN value;
- externally verified ACNs by accounts never submitted for verification;
- recent account failures by the total historical organisation-account base; or
- ACN failures by organisations not expected to hold an ACN.

The numerator and denominator must use:

- the same Organisation Account population;
- the same period;
- the same account identifier;
- the same legal-entity classification logic;
- the same exclusions;
- the same minimum criteria; and
- the same rule version.

## Source requirements

Before implementation, confirm:

| Requirement | Status |
|---|---|
| Salesforce source object or governed Databricks table | Open |
| Unique Organisation Account identifier | Open |
| Organisation Account record types | Open |
| Authoritative ACN field | Open |
| Legal-entity classification | Open |
| ABN field for cross-checking | Open |
| Country or jurisdiction field | Open |
| Account-status logic | Open |
| Creation date and source | Open |
| Merge or superseded-record indicators | Open |
| Test and system-record exclusions | Open |
| Exception field or indicator | Open |
| External verification result, if applicable | Open |
| Refresh frequency | Open |

## Output categories

A governed analytical output should separate:

1. ACN missing;
2. ACN present but not normalisable;
3. ACN incorrect length;
4. ACN checksum invalid;
5. probable ABN entered in ACN field;
6. ACN meets agreed structural criteria;
7. ACN externally verified;
8. approved exception;
9. legal-entity classification unresolved;
10. account not assessable; and
11. record excluded from the eligible population.

These categories must not be collapsed where they imply different actions.

## Operational response

Possible actions include:

- correct the ACN during the next legitimate interaction;
- request legal-entity classification review;
- review the account against approved source material;
- move a probable ABN to the correct field through a controlled process;
- update staff guidance;
- improve account-creation controls;
- correct integration or migration logic;
- record an approved exception;
- assign records to a controlled remediation queue;
- perform approved external verification; or
- take no action where remediation is inappropriate.

The rule must not automatically trigger customer contact, external verification or record changes without an approved process.

## External verification

External ACN verification is a future capability unless explicitly approved.

Before using an external source, confirm:

- approved provider or register;
- permitted use;
- privacy and records requirements;
- access and security controls;
- matching criteria;
- verification frequency;
- handling of deregistered companies;
- handling of unavailable or conflicting results;
- ownership;
- cost and operational impact; and
- audit requirements.

A successful register lookup does not by itself confirm that the ACN belongs to the CRM account.

## Ownership

| Role | Responsibility | Owner |
|---|---|---|
| Business rule owner | Approves eligible company types and rule purpose | Open |
| Operational owner | Owns classification review and correction pathways | Open |
| Technical owner — Salesforce | Owns preventative or in-platform controls | Open |
| Technical owner — Databricks | Implements and maintains analytical logic | Open |
| Data owner or steward | Confirms field meaning and quality expectations | Open |
| External verification owner | Owns approved verification process, if introduced | Open |
| Governance reviewers | Provide privacy, records, security or governance advice | Open |

Ownership must be assigned before governed use.

## Risks

| Risk | Treatment |
|---|---|
| Every Organisation Account is assumed to require an ACN | Define eligible legal entity types first. |
| The pilot result is treated as a company failure rate | Rebuild the denominator around eligible companies. |
| Presence is described as validity | Name each assessment level accurately. |
| Checksum validity is treated as ownership verification | Keep structural and ownership checks separate. |
| Poor legal-entity classification distorts the metric | Report unclassifiable accounts separately. |
| ABNs entered in the ACN field are treated as ordinary failures | Create a distinct failure category. |
| Person Accounts enter the denominator | Enforce object and record-type boundaries. |
| Non-company entities are treated as defects | Define approved exceptions. |
| A hard Salesforce rule blocks legitimate account creation | Test service and exception scenarios first. |
| External data is used without governance | Require an approved source, purpose and controls. |
| Operational teams receive an unactionable failure list | Assign ownership and action pathways before use. |
| Raw ACNs are copied into GitHub | Store only definitions, logic, summaries and caveats. |

## Workshop decision record

| Decision | Outcome | Owner | Date | Status |
|---|---|---|---|---|
| Eligible Organisation Account population |  |  |  | Open |
| Legal entity types requiring an ACN |  |  |  | Open |
| Authoritative ACN field |  |  |  | Open |
| Minimum assessment level |  |  |  | Open |
| Normalisation logic |  |  |  | Open |
| Invalid and placeholder values |  |  |  | Open |
| ABN-to-ACN cross-field logic |  |  |  | Open |
| Approved exceptions |  |  |  | Open |
| Legal-entity classification treatment |  |  |  | Open |
| Measurement period |  |  |  | Open |
| Salesforce control purpose |  |  |  | Open |
| Databricks diagnostic purpose |  |  |  | Open |
| External verification scope |  |  |  | Open |
| Operational response |  |  |  | Open |
| Business owner |  |  |  | Open |
| Operational owner |  |  |  | Open |
| Technical owners |  |  |  | Open |
| Governed-use approval |  |  |  | Open |

## Definition of Ready

The rule is ready for governed technical implementation only when:

- the business question is agreed;
- the eligible Organisation Account population is explicit;
- legal entity types requiring an ACN are defined;
- the authoritative ACN field is confirmed;
- the minimum assessment level is documented;
- normalisation logic is agreed;
- invalid and placeholder values are defined;
- ABN-to-ACN cross-field treatment is agreed;
- exceptions are approved;
- classification gaps are handled explicitly;
- source fields and grain are confirmed;
- numerator and denominator are compatible;
- operational action is agreed;
- ownership is assigned;
- external verification boundaries are documented;
- privacy, records, security and governance needs have been considered;
- test cases include valid, invalid, exempt, misclassified and unclassifiable accounts;
- rule versioning is established;
- permitted uses are documented; and
- the decision is recorded in the decision log.

## Current assessment

**Status:** Technically calculated in the pilot but not ready for governed implementation.

**Reason:** Eligible company types, minimum ACN criteria, classification dependencies, denominator, exceptions, ownership and operational response remain unresolved.

**Slide-safe wording:** Not available.

**Permitted current use:** Workshop preparation, exploratory profiling and refinement of the pilot rule only.

## Related repository pages

- `01-discover/databricks-customer-data-quality-pilot-input.md`
- `02-define/rules/CAM-DQ-004-abn-completeness.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `02-define/crm-data-quality-rule-refinement-workshop.md`
- `01-discover/evidence-gaps.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`
