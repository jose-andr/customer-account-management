# CAM-DQ-004 — ABN completeness

## Document control

| Field | Value |
|---|---|
| Rule ID | CAM-DQ-004 |
| Rule name | ABN completeness |
| Rule group | Organisation Account identifier completeness |
| Status | Draft — business refinement required |
| Validation level | Partially validated |
| Current phase | Define |
| Priority | First refinement cycle |
| Governed metric status | Not ready |
| Last updated | 30 July 2026 |

## Purpose

Define when an eligible Organisation Account should contain an Australian Business Number and how missing or unusable ABN values should be identified.

This rule is a completeness diagnostic.

It does not establish that every Organisation Account must have an ABN, confirm that a recorded ABN belongs to the organisation, or approve external verification.

## Business question

Which Organisation Accounts are expected to have an ABN, and what proportion of that eligible population does not contain an ABN meeting the agreed minimum criteria?

## Decision required

Agree:

1. the eligible Organisation Account population;
2. which organisation types require an ABN;
3. legitimate exceptions;
4. minimum ABN presence and format criteria;
5. whether external verification is in scope;
6. the relationship between Salesforce controls and Databricks measurement;
7. the action required when an account fails the rule; and
8. business, operational and technical ownership.

## Current working definition

> An eligible Organisation Account should contain an ABN meeting the agreed minimum criteria unless an approved exception applies.

This is a working definition only.

The business must first determine which Organisation Accounts are expected to have an ABN.

## Why the rule matters

Missing or unusable ABN information may:

- reduce confidence in organisation-account identification;
- make it harder to distinguish organisations with similar names;
- contribute to duplicate account creation;
- weaken account matching across systems;
- create avoidable staff investigation;
- affect reporting by organisation type;
- limit safe comparison with external registers; and
- reduce confidence in customer account quality measures.

An ABN being present does not prove that it is current, valid or associated with the correct organisation.

## Scope

This rule applies to Organisation Accounts only.

It must not be applied to Person Accounts.

The source object, account types and record types must be confirmed before technical implementation.

## Eligible population

### Proposed starting population

Organisation Accounts that:

- are within the agreed Salesforce account population;
- represent an organisation type expected to hold an ABN;
- are not test, training or system-generated records;
- are not merged, superseded or otherwise excluded under approved logic;
- are within the agreed status or activity period; and
- do not meet an approved exception.

### Population questions

The workshop must determine:

- which Organisation Account record types are in scope;
- whether businesses, companies, sole traders and partnerships are treated differently;
- whether government entities are expected to have an ABN;
- whether incorporated associations are expected to have an ABN;
- whether trusts are in scope;
- whether charities and not-for-profit entities are in scope;
- whether informal community groups are excluded;
- whether international organisations are excluded;
- whether inactive or historical accounts remain in scope;
- how internal organisational records are treated;
- how temporary or incomplete accounts are treated; and
- whether an activity or recency threshold is required.

## Organisation-type dependency

ABN completeness cannot be measured safely until organisation classifications are sufficiently reliable.

The rule may depend on fields such as:

- organisation account record type;
- legal entity type;
- customer category;
- business classification;
- jurisdiction;
- country;
- registration type;
- active status; and
- internal or external organisation indicator.

If these classifications are missing or inconsistent, the output should separate:

1. accounts clearly expected to have an ABN;
2. accounts clearly exempt;
3. accounts requiring classification review; and
4. accounts that cannot be assessed.

Do not treat unclassifiable accounts as confirmed ABN failures.

## ABN field

The business and technical owners must confirm:

- the authoritative ABN field;
- whether alternate ABN fields exist;
- whether the value is stored as text or number;
- whether formatting characters are retained;
- whether leading zeroes can be preserved;
- whether legacy or migrated fields are in use;
- whether related objects also hold an ABN; and
- how conflicting values are treated.

Do not combine multiple ABN fields without documenting their meaning and precedence.

## Minimum criteria

The initial rule may include several levels of assessment.

### Level 1 — Presence

The authoritative ABN field contains a non-blank value.

### Level 2 — Structural format

The normalised value contains 11 digits.

### Level 3 — Checksum validity

The value passes the approved ABN checksum algorithm.

### Level 4 — External verification

The value is verified against an approved external source.

These levels are not interchangeable.

A presence measure must not be described as valid ABN coverage.

A structurally valid ABN must not be described as belonging to the organisation unless ownership has been verified.

## ABN normalisation

Candidate normalisation steps requiring technical validation:

1. trim leading and trailing spaces;
2. remove spaces and approved formatting characters;
3. retain digits only where safe;
4. preserve leading zeroes;
5. treat blank strings as null;
6. exclude known placeholder and test values;
7. separate values that cannot be normalised; and
8. retain the original source value in the governed source environment for review.

Do not store raw ABNs or record-level extracts in GitHub.

## Candidate invalid values

Potential invalid or unusable values include:

- blank or null values;
- values containing fewer or more than 11 digits;
- alphabetic characters;
- repeated placeholder digits;
- all-zero values;
- known test values;
- multiple ABNs entered into one field;
- text such as “unknown” or “not applicable”;
- values that fail the approved checksum; and
- values known to be obsolete or incorrect.

The treatment of each category must be documented.

## Candidate exceptions

Potential exceptions requiring validation include:

- organisation type is not expected to hold an ABN;
- international organisation;
- informal or unincorporated group;
- internal organisational account;
- account retained only for records purposes;
- temporary record awaiting verification;
- account created before ABN collection became required;
- customer declined or was unable to provide the information;
- ABN is held in another governed system and is not expected in Salesforce;
- legal, privacy or operational constraint prevents collection; and
- account classification is unresolved.

Exceptions must be explicit, measurable and approved.

## Rule logic — business expression

The rule should be expressed as:

> Within the eligible Organisation Account population expected to hold an ABN, identify accounts where the authoritative ABN field does not meet the agreed minimum criteria and no approved exception applies.

The minimum criteria must be named in every output.

Examples:

- ABN missing;
- ABN present but structurally invalid;
- ABN present and checksum-valid;
- ABN externally verified.

Do not combine these into one undifferentiated measure.

## Salesforce control

### Potential purpose

Salesforce may:

- require an ABN for selected organisation types;
- apply format or checksum validation;
- provide guidance when an ABN is not available;
- support an approved exception value;
- prevent placeholder values; or
- prompt staff to confirm organisation classification.

### Current status

Existing Salesforce validation rules and operational practices must be confirmed before proposing changes.

### Questions

- Is ABN currently mandatory for any record types?
- Which organisation classifications trigger the requirement?
- Does Salesforce validate length, characters or checksum?
- Are integrations and imports subject to the same control?
- Are legacy records exempt?
- Can staff record an approved exception?
- Would a hard validation rule prevent legitimate service access?
- Who owns changes to the control?
- How are failed validations monitored?
- Is ABN verification performed elsewhere?

A hard validation rule should not be implemented until legitimate exceptions are understood.

## Databricks purpose

Databricks may be used to:

- establish an exploratory ABN completeness baseline;
- separate missing, malformed and checksum-invalid values;
- identify accounts that cannot be assessed because organisation type is unclear;
- measure trends over time;
- compare account-creation pathways;
- support root-cause analysis;
- monitor the effect of Salesforce controls; and
- identify records requiring classification or operational review.

Databricks should not become the source of the business definition.

## Proposed primary diagnostic

### Metric name

Eligible Organisation Accounts without an ABN meeting minimum criteria.

### Metric status

Exploratory only — not governed and not slide-safe.

### Unit

Distinct eligible Organisation Accounts.

### Proposed numerator

Distinct eligible Organisation Accounts expected to hold an ABN where:

- the authoritative ABN field does not meet the agreed minimum criteria; and
- no approved exception applies.

### Proposed denominator

All distinct eligible Organisation Accounts expected to hold an ABN after approved exclusions.

### Proposed rate

`Numerator ÷ denominator × 100`

The denominator must exclude organisations not expected to hold an ABN.

## Supporting diagnostics

Candidate supporting measures include:

- accounts with no ABN value;
- accounts with an ABN value of incorrect length;
- accounts containing non-numeric ABN characters;
- accounts failing checksum validation;
- accounts with a structurally valid ABN;
- accounts externally verified;
- accounts with an approved exception;
- accounts requiring organisation-type classification;
- accounts not assessable;
- failures by creation pathway;
- failures by account status;
- failures by organisation type; and
- failures by rule version.

Each measure must state its grain, population and criteria.

## Denominator safety

Do not divide:

- missing ABNs by all CRM accounts;
- Organisation Account failures by a denominator containing Person Accounts;
- checksum failures by accounts with no ABN value;
- externally verified ABNs by accounts never submitted for verification;
- recent account failures by the total historical organisation-account base; or
- ABN failures by organisations not expected to hold an ABN.

The numerator and denominator must use:

- the same Organisation Account population;
- the same period;
- the same account identifier;
- the same classification logic;
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
| Authoritative ABN field | Open |
| Organisation-type classification | Open |
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

1. ABN missing;
2. ABN present but not normalisable;
3. ABN incorrect length;
4. ABN checksum invalid;
5. ABN meets agreed structural criteria;
6. ABN externally verified;
7. approved exception;
8. organisation classification unresolved;
9. account not assessable; and
10. record excluded from the eligible population.

These categories must not be collapsed where they imply different actions.

## Operational response

Possible actions include:

- correct the ABN during the next legitimate interaction;
- request organisation classification review;
- review the account against approved source material;
- update staff guidance;
- improve account-creation controls;
- correct integration or migration logic;
- record an approved exception;
- assign records to a controlled remediation queue;
- perform approved external verification; or
- take no action where remediation is inappropriate.

The rule must not automatically trigger customer contact, external verification or record changes without an approved process.

## External verification

External ABN verification is a future capability unless explicitly approved.

Before using an external source, confirm:

- approved provider or register;
- permitted use;
- privacy and records requirements;
- access and security controls;
- matching criteria;
- verification frequency;
- handling of unavailable or conflicting results;
- ownership;
- cost and operational impact; and
- audit requirements.

A successful register lookup does not by itself confirm that the ABN belongs to the CRM account.

## Ownership

| Role | Responsibility | Owner |
|---|---|---|
| Business rule owner | Approves eligible organisation types and rule purpose | Open |
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
| Every Organisation Account is assumed to require an ABN | Define eligible organisation types first. |
| Presence is described as validity | Name each assessment level accurately. |
| Checksum validity is treated as ownership verification | Keep structural and ownership checks separate. |
| Poor organisation classification distorts the metric | Report unclassifiable accounts separately. |
| Person Accounts enter the denominator | Enforce object and record-type boundaries. |
| International or informal organisations are treated as defects | Define approved exceptions. |
| A hard Salesforce rule blocks legitimate account creation | Test service and exception scenarios first. |
| External data is used without governance | Require approved source, purpose and controls. |
| Operational teams receive an unactionable failure list | Assign ownership and action pathways before use. |
| Raw ABNs are copied into GitHub | Store only definitions, logic, summaries and caveats. |

## Workshop decision record

| Decision | Outcome | Owner | Date | Status |
|---|---|---|---|---|
| Eligible Organisation Account population |  |  |  | Open |
| Organisation types requiring an ABN |  |  |  | Open |
| Authoritative ABN field |  |  |  | Open |
| Minimum assessment level |  |  |  | Open |
| Normalisation logic |  |  |  | Open |
| Invalid and placeholder values |  |  |  | Open |
| Approved exceptions |  |  |  | Open |
| Organisation-classification treatment |  |  |  | Open |
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
- organisation types requiring an ABN are defined;
- the authoritative ABN field is confirmed;
- the minimum assessment level is documented;
- normalisation logic is agreed;
- invalid and placeholder values are defined;
- exceptions are approved;
- organisation-classification gaps are handled explicitly;
- source fields and grain are confirmed;
- numerator and denominator are compatible;
- operational action is agreed;
- ownership is assigned;
- external verification boundaries are documented;
- privacy, records, security and governance needs have been considered;
- test cases include valid, invalid, exempt and unclassifiable accounts;
- rule versioning is established;
- permitted uses are documented; and
- the decision is recorded in the decision log.

## Current assessment

**Status:** Technically definable but not ready for governed implementation.

**Reason:** Eligible organisation types, minimum ABN criteria, exceptions, classification dependencies, ownership and operational response remain unresolved.

**Slide-safe wording:** Not available.

**Permitted current use:** Workshop preparation and exploratory profiling only.

## Related repository pages

- `02-define/rules/CAM-DQ-001-minimum-valid-contact-method.md`
- `02-define/rules/CAM-DQ-002-exact-email-duplicate-signal.md`
- `02-define/rules/CAM-DQ-003-exact-mobile-duplicate-signal.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `02-define/crm-data-quality-rule-refinement-workshop.md`
- `01-discover/evidence-gaps.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`
