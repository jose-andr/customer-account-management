# Assumptions log

Status: Active  
Owner: José Andrade  
Current stage: Discover → Define  
Last updated: 29 July 2026

## Purpose

Record assumptions that affect Customer Account Management decisions.

This log helps the workstream:

- separate evidence from belief;
- identify what still needs validation;
- avoid premature solution design;
- assign validation actions;
- preserve contradictory evidence;
- make decision risk visible; and
- retire assumptions when evidence is sufficient.

An assumption is not a finding, requirement or decision.

## Status definitions

| Status | Meaning |
|---|---|
| Open | Not yet tested |
| In validation | Evidence collection is underway |
| Partially supported | Some evidence exists, but confidence is limited |
| Supported | Sufficiently supported for the stated decision |
| Rejected | Evidence does not support the assumption |
| Superseded | Replaced by a more precise assumption or decision |
| Parked | Not currently important to the next decision |

## Confidence definitions

| Confidence | Meaning |
|---|---|
| Low | Based mainly on isolated examples, opinion or incomplete evidence |
| Medium | Supported by multiple sources or partial validation |
| High | Supported by reliable evidence and appropriate stakeholder review |

## Active assumptions

| ID | Assumption | Decision affected | Current confidence | Status | Validation owner |
|---|---|---|---|---|---|
| ASM-001 | Duplicate and inconsistent customer accounts materially affect customer experience | Problem priority and design focus | Low | In validation | To assign |
| ASM-002 | Duplicate and inconsistent accounts create material employee effort | Investment and operational prioritisation | Medium | Partially supported | Customer Data and Systems Support Officer |
| ASM-003 | The current account model does not adequately represent all customer relationships | Future account model | Low | Open | To assign |
| ASM-004 | Upstream processes and systems continue to create avoidable duplicate accounts | Prevention priorities | Medium | Partially supported | CRM Product Owner |
| ASM-005 | Improving CRM account quality will support more connected customer interactions | Transformation value | Low | Open | José Andrade |
| ASM-006 | Current duplicate-detection and merge practices depend on undocumented individual knowledge | Capability and continuity risk | Medium | Partially supported | Customer Data and Systems Support Officer |
| ASM-007 | Existing Plauti configuration does not fully meet current business needs | Plauti refinement and Databricks scope | Low | Open | CRM Product Owner |
| ASM-008 | Databricks quality rules can provide a reliable CRM quality baseline | Measurement and reporting | Low | In validation | Databricks or Data Governance representative |
| ASM-009 | Databricks should not reproduce Plauti logic unless there is a distinct monitoring or analytical purpose | Control design | Medium | Partially supported | José Andrade |
| ASM-010 | Potential duplicate results can be converted into safe trend measures | Metric design | Low | Open | Analytics or Data Governance support |
| ASM-011 | Active Person Accounts should contain at least one usable contact method | Contact-completeness rule | Low | In validation | To assign |
| ASM-012 | A missing primary email is always a data-quality defect | Email-completeness rule | Low | Open | To assign |
| ASM-013 | A missing primary mobile is always a data-quality defect | Mobile-completeness rule | Low | Open | To assign |
| ASM-014 | Exact name and email matches provide a sufficiently useful duplicate signal | Person duplicate rule | Medium | In validation | CRM Product Owner |
| ASM-015 | Exact name and mobile matches provide a sufficiently useful duplicate signal | Person duplicate rule | Medium | In validation | CRM Product Owner |
| ASM-016 | A repeated ABN usually indicates duplicate organisation accounts | Organisation duplicate rule | Low | Open | To assign |
| ASM-017 | A repeated ACN usually indicates duplicate organisation accounts | Organisation duplicate rule | Low | Open | To assign |
| ASM-018 | All active organisation accounts should contain an ABN | Organisation completeness rule | Low | Open | To assign |
| ASM-019 | All active organisation accounts should contain an ACN | Organisation completeness rule | Low | Open | To assign |
| ASM-020 | Name similarity above 90% is an appropriate Person Account duplicate threshold | Fuzzy matching | Low | Open | CRM Product Owner |
| ASM-021 | The Salesforce Data Quality Rules Confluence page reflects the latest working rule inventory | Source reliability | Medium | In validation | José Andrade |
| ASM-022 | The documented Plauti configuration reflects the current production setup | Control validation | Low | Open | CRM Product Owner |
| ASM-023 | Current Salesforce validation rules prevent selected new defects but do not address historical records | Prevention and remediation split | Medium | Partially supported | Salesforce administrator |
| ASM-024 | Current account-quality measures can be made denominator-safe | Reporting readiness | Low | In validation | Analytics or Data Governance support |
| ASM-025 | The first rule-refinement cycle should focus on Person Account contact quality and exact duplicate signals before fuzzy matching | Delivery sequencing | Medium | Supported | José Andrade |

## Assumption details

### ASM-001 — Customer impact

**Assumption**

Duplicate and inconsistent customer accounts materially affect customer experience.

**Current signals**

Reported impacts include:

- repeated requests for information;
- fragmented service histories;
- difficulty accessing or updating accounts;
- inconsistent communications;
- additional effort across services; and
- reduced confidence that the organisation recognises the customer.

**Evidence required**

- de-identified customer examples;
- complaints or feedback themes;
- account-related contact reasons;
- failed account journeys;
- repeat-contact evidence; and
- evidence from priority services.

**Decision rule**

Treat as supported when there is sufficient evidence that account-quality issues create material customer effort, risk or service failure in priority journeys.

---

### ASM-002 — Employee effort

**Assumption**

Duplicate and inconsistent accounts create material employee effort.

**Current signals**

Reported activities include:

- searching;
- comparing records;
- validating identity;
- correcting information;
- assessing potential duplicates;
- escalating uncertain cases;
- recording completion; and
- managing work outside the primary system.

**Evidence required**

- validated process walkthrough;
- activity volume;
- handling time;
- backlog;
- escalation frequency;
- workarounds; and
- repeat handling.

**Decision rule**

Treat as supported when actual-practice evidence confirms recurring effort of sufficient scale or consequence to justify improvement.

---

### ASM-004 — Upstream duplicate creation

**Assumption**

Upstream processes and systems continue to create avoidable duplicate accounts.

**Possible causes**

- customer self-service account creation;
- staff-assisted account creation;
- inconsistent matching;
- optional fields;
- integration behaviour;
- service-specific account structures;
- account classification;
- historical migration; and
- customer-detail update processes.

**Evidence required**

- account creation source;
- account creation date;
- duplicate rule output;
- service or channel source;
- repeat defects;
- technical process review; and
- operational validation.

**Decision rule**

Treat as supported when recurring duplicate patterns can be linked to identifiable creation pathways or system behaviours.

---

### ASM-008 — Databricks baseline capability

**Assumption**

Databricks quality rules can provide a reliable CRM account-quality baseline.

**Conditions**

This requires:

- agreed business definitions;
- stable rule IDs;
- validated source datasets;
- explicit record grain;
- correct population filters;
- numerator and denominator definitions;
- version control;
- scheduled execution;
- reviewed outputs;
- ownership; and
- known caveats.

**Evidence required**

- technical rule inventory;
- implementation status;
- execution results;
- test evidence;
- data reconciliation;
- rule owner review; and
- metric approval.

**Decision rule**

Treat as supported only when the selected rules produce repeatable and reviewed results suitable for the stated decision use.

---

### ASM-011 — Minimum contact method

**Assumption**

An active Person Account should contain at least one usable contact method.

**Questions**

- What qualifies as usable?
- Is postal address sufficient?
- Is email required for online services?
- Is mobile required for selected services?
- Are service-specific rules required?
- What exceptions apply?
- Are inactive, deceased or historical accounts excluded?

**Evidence required**

- current business rules;
- service requirements;
- Salesforce validations;
- operational exceptions;
- customer communication needs;
- privacy constraints; and
- service-owner input.

**Decision rule**

Treat as supported when the required contact methods and valid exceptions are agreed by the appropriate business owner.

---

### ASM-014 and ASM-015 — Exact duplicate signals

**Assumption**

Exact name plus shared email or mobile provides a useful Person Account duplicate signal.

**Risks**

- shared household contact details;
- carers and representatives;
- family accounts;
- common names;
- reused phone numbers;
- data-entry variation;
- historical contact information; and
- legitimate multiple records.

**Evidence required**

- current Plauti configuration;
- sample results;
- confirmed and rejected matches;
- false-positive review;
- operational decision criteria; and
- output-grain confirmation.

**Decision rule**

Treat as supported when the rule identifies a useful review population with acceptable false positives and a clear operational action.

---

### ASM-016 and ASM-017 — Repeated organisation identifiers

**Assumption**

Repeated ABN or ACN values usually indicate duplicate organisation accounts.

**Risks**

A repeated identifier may represent:

- duplicate accounts;
- branches;
- departments;
- different service relationships;
- historical records;
- inactive accounts;
- account-model limitations; or
- intentional multiple-account structures.

**Evidence required**

- organisation-account use cases;
- legal-entity model;
- current account structures;
- confirmed duplicate examples;
- service-owner input;
- Plauti behaviour; and
- operational review outcomes.

**Decision rule**

Treat as supported only when the organisation model clearly distinguishes invalid duplication from legitimate multiple-account relationships.

---

### ASM-020 — Fuzzy-name threshold

**Assumption**

A name similarity threshold above 90% is appropriate for duplicate detection.

**Risks**

- common names;
- short names;
- punctuation;
- cultural naming conventions;
- transliteration;
- abbreviations;
- typographical variation;
- false positives; and
- false negatives.

**Evidence required**

- rule-performance testing;
- threshold comparison;
- sample review;
- precision and recall where available;
- operational effort;
- Plauti configuration; and
- privacy-risk assessment.

**Decision rule**

Do not support this assumption until multiple thresholds have been tested and operational reviewers accept the resulting workload and risk.

## Assumptions requiring immediate validation

Prioritise:

1. ASM-011 — minimum valid contact method;
2. ASM-014 — exact email duplicate signal;
3. ASM-015 — exact mobile duplicate signal;
4. ASM-016 — repeated ABN;
5. ASM-017 — repeated ACN;
6. ASM-021 — currency of the Confluence rule inventory;
7. ASM-022 — currency of the Plauti production configuration; and
8. ASM-024 — denominator-safe reporting readiness.

These assumptions directly affect the first CRM rule-refinement cycle.

## Validation methods

| Method | Suitable use |
|---|---|
| Operational walkthrough | Confirm actual tasks, judgement and exceptions |
| Configuration review | Confirm Salesforce and Plauti behaviour |
| Rule-result review | Assess output grain, scale and false positives |
| Governed metric review | Confirm source, population, numerator and denominator |
| Service-owner interview | Confirm service needs and legitimate exceptions |
| Governance review | Confirm privacy, records, security and ownership constraints |
| De-identified case reconstruction | Understand complex account and relationship scenarios |
| Decision workshop | Approve, reject, park or refine an assumption |

## Validation record

When an assumption is tested, record:

- assumption ID;
- validation question;
- evidence source;
- evidence status;
- finding;
- caveat;
- confidence change;
- decision impact;
- owner;
- date; and
- resulting status.

Use:

`07-templates/evidence-record-template.md`

## Assumptions that must not become implicit requirements

Do not assume that the work requires:

- one physical customer record;
- a master customer ID;
- automated merging;
- replacement of Plauti;
- replication of Plauti logic in Databricks;
- mandatory email for every customer;
- mandatory mobile for every customer;
- mandatory ABN or ACN for every organisation;
- one account per legal entity;
- a new governance body;
- a new organisational function; or
- a particular technology solution.

These remain possible design responses or future signals until supported by evidence and an explicit decision.

## Review cadence

Review this log:

- before each rule-refinement workshop;
- after material evidence is collected;
- before a rule is approved for implementation;
- before Databricks results are used in decision-making;
- before moving from Define into Design; and
- when a decision changes the problem or scope.

## Next action

## Additional assumptions — Databricks customer data-quality pilot

### Assumption status

The following assumptions were exposed by the initial Databricks and Power BI customer data-quality pilot.

They are not approved business rules, metric definitions or operating requirements.

Each assumption must be:

- validated;
- refined;
- rejected;
- converted into a recorded decision; or
- retained as an explicitly open assumption.

## Pilot calculation assumptions

| Assumption ID | Assumption | Current status | Validation required | Owner |
|---|---|---|---|---|
| CAM-ASM-011 | `Records tested` represents a consistent and decision-relevant unit across the dashboard | Open | Confirm whether the unit is accounts, contacts, attributes, rule executions, pairs, groups or record-rule combinations | Databricks technical owner — to confirm |
| CAM-ASM-012 | The Full Records and All Attributes pages use compatible filters and calculation logic | Open | Reconcile the difference between the displayed tested totals | Databricks and Power BI technical owners — to confirm |
| CAM-ASM-013 | Account and Contact results can be combined into one overall quality score | Open | Confirm compatible grain, weighting, population and business meaning | Analytics owner and data steward — to confirm |
| CAM-ASM-014 | Each rule execution contributes appropriately to the aggregate score | Open | Confirm weighting and whether high-volume rules dominate the result | Analytics owner — to confirm |
| CAM-ASM-015 | All rules shown in the dashboard were executed against the same source snapshot or reporting period | Open | Confirm execution dates, source refreshes and rule-run timing | Databricks technical owner — to confirm |
| CAM-ASM-016 | Blank, excluded and not-applicable records are handled consistently across rules | Open | Document treatment for each rule and dashboard aggregation | Databricks technical owner and business rule owners — to confirm |
| CAM-ASM-017 | The approximate 95.9% pass rate represents customer data quality in a meaningful way | Rejected for current use | Reconsider only after grain, weighting, populations and dimensions are governed | Business rule owner and analytics owner — to confirm |

## Contact-quality assumptions

| Assumption ID | Assumption | Current status | Validation required | Owner |
|---|---|---|---|---|
| CAM-ASM-018 | A populated email field represents a usable contact method | Open | Validate format, currency, ownership, consent, preference and exceptions | CAM-DQ-001 business owner — to confirm |
| CAM-ASM-019 | A populated mobile field represents a usable contact method | Open | Validate format, currency, ownership, number type, consent and exceptions | CAM-DQ-001 business owner — to confirm |
| CAM-ASM-020 | One valid email or mobile number is sufficient for every eligible Person Account | Open | Confirm accepted contact methods and service-specific needs | CAM-DQ-001 business owner — to confirm |
| CAM-ASM-021 | Secondary contact fields have the same business purpose and quality expectations as primary fields | Open | Confirm field meaning, ownership, permitted use and precedence | CRM Product Owner and data steward — to confirm |
| CAM-ASM-022 | Contact completeness can be evaluated without considering account activity or relevance | Open | Define active, inactive, historical and temporary-record treatment | CAM-DQ-001 business owner — to confirm |

## Duplicate-signal assumptions

| Assumption ID | Assumption | Current status | Validation required | Owner |
|---|---|---|---|---|
| CAM-ASM-023 | A similarity threshold of `1` represents an exact business-relevant match | Open | Confirm algorithm, preprocessing and comparison output | Databricks technical owner — to confirm |
| CAM-ASM-024 | A similarity threshold of `0.9` represents a useful potential-duplicate signal | Open | Test precision, false positives, false negatives and operational value | Databricks technical owner and operational owner — to confirm |
| CAM-ASM-025 | Repeated email addresses usually indicate duplicate Person Accounts | Open | Review shared households, carers, guardians, representatives and service arrangements | CAM-DQ-002 business and operational owners — to confirm |
| CAM-ASM-026 | Repeated mobile numbers usually indicate duplicate Person Accounts | Open | Review shared numbers, representatives, recycled numbers and timing | CAM-DQ-003 business and operational owners — to confirm |
| CAM-ASM-027 | Matching name should be mandatory for exact email or mobile duplicate signals | Open | Decide whether name is required logic or supporting review evidence | CAM-DQ-002 and CAM-DQ-003 business owners — to confirm |
| CAM-ASM-028 | Databricks duplicate rules should reproduce active Plauti scenarios | Rejected for current use | Define each tool’s purpose before deciding whether logic should align | CRM Product Owner, Plauti owner and Databricks owner — to confirm |
| CAM-ASM-029 | A duplicate signal can create a merge candidate without human confirmation | Rejected | Preserve operational review and controlled merge authority | Operational owner and merge authority — to confirm |

## Organisation-identifier assumptions

| Assumption ID | Assumption | Current status | Validation required | Owner |
|---|---|---|---|---|
| CAM-ASM-030 | Every active Organisation Account should contain an ABN | Open | Define eligible organisation types and approved exceptions | CAM-DQ-004 business owner — to confirm |
| CAM-ASM-031 | Every active Organisation Account should contain an ACN | Rejected for current use | Restrict eligibility to entities expected to hold an ACN | CAM-DQ-005 business owner — to confirm |
| CAM-ASM-032 | ABN and ACN presence is sufficient evidence of identifier validity | Rejected for current use | Separate presence, format, checksum and external verification | CAM-DQ-004 and CAM-DQ-005 business owners — to confirm |
| CAM-ASM-033 | A checksum-valid ABN or ACN belongs to the Organisation Account on which it is recorded | Open | Define whether and how ownership is verified | Data steward and governance reviewers — to confirm |
| CAM-ASM-034 | Organisation classifications are sufficiently reliable to define ABN and ACN denominators | Open | Profile record types, legal entity classifications and unresolved values | Data steward and Databricks technical owner — to confirm |
| CAM-ASM-035 | Blank identifier fields and invalid identifier values should be treated as one failure category | Rejected for current use | Separate missing, malformed, checksum-invalid, exempt and unclassifiable records | CAM-DQ-004 and CAM-DQ-005 business owners — to confirm |
| CAM-ASM-036 | An ABN entered into an ACN field can be detected and corrected automatically | Open | Validate detection reliability, correction controls and operational approval | CRM Product Owner and technical owner — to confirm |

## Repeated-identifier assumptions

| Assumption ID | Assumption | Current status | Validation required | Owner |
|---|---|---|---|---|
| CAM-ASM-037 | One ABN should map to one Organisation Account | Open | Review branches, locations, trading structures, service relationships and historical accounts | CAM-DQ-006 business owner — to confirm |
| CAM-ASM-038 | One ACN should map to one Organisation Account | Open | Review multiple operational accounts, branches, service relationships and retained history | CAM-DQ-007 business owner — to confirm |
| CAM-ASM-039 | Every repeated ABN represents a potential duplicate requiring the same review priority | Open | Define signal categories and prioritisation logic | CAM-DQ-006 operational owner — to confirm |
| CAM-ASM-040 | Every repeated ACN represents a potential duplicate requiring the same review priority | Open | Define signal categories and prioritisation logic | CAM-DQ-007 operational owner — to confirm |
| CAM-ASM-041 | Duplicate groups, duplicate pairs and records in duplicate groups can be used interchangeably | Rejected | Require every output to state its grain and reporting unit | Analytics owner — to confirm |
| CAM-ASM-042 | Inactive or historical accounts should remain in repeated-identifier reporting | Open | Define reporting purpose and account-status treatment | Business rule owners — to confirm |

## Operating-model assumptions

| Assumption ID | Assumption | Current status | Validation required | Owner |
|---|---|---|---|---|
| CAM-ASM-043 | A rule failure will have an available operational owner | Open | Assign owners and confirm responsibility before operational use | Customer Focus and CRM leadership — to confirm |
| CAM-ASM-044 | Operational teams have capacity to review pilot failure outputs | Open | Estimate volumes, review effort, service standards and backlog capacity | Operational owner — to confirm |
| CAM-ASM-045 | Every detected failure should create a remediation action | Rejected for current use | Define diagnostic-only, next-interaction, exception and no-action pathways | Business and operational owners — to confirm |
| CAM-ASM-046 | A Databricks result can be used operationally once the technical logic runs successfully | Rejected | Require business definition, validation, ownership and operational readiness | Business rule owner and governance — to confirm |
| CAM-ASM-047 | Power BI is the source of truth for rule definitions | Rejected | Keep rule definitions in governed business and technical sources; use Power BI as a presentation layer | Repository owner and analytics owner |
| CAM-ASM-048 | Current review outcomes are recorded consistently enough to evaluate rule precision | Open | Confirm review-status and outcome data in Salesforce, Plauti or another governed source | Operational owner and Plauti owner — to confirm |

## Reporting assumptions

| Assumption ID | Assumption | Current status | Validation required | Owner |
|---|---|---|---|---|
| CAM-ASM-049 | A high aggregate pass rate indicates low operational risk | Open | Assess rule importance, failure severity and affected journeys separately | Business rule owner — to confirm |
| CAM-ASM-050 | All quality dimensions should be combined into one headline score | Open | Decide whether dimension-level reporting provides safer decision support | Analytics owner and data governance — to confirm |
| CAM-ASM-051 | Completeness, validity and uniqueness scores are directly comparable | Open | Confirm populations, grains, rule counts and weighting | Analytics owner — to confirm |
| CAM-ASM-052 | Pilot results can be compared over time without explicit rule versioning | Rejected | Require version, source snapshot, population and threshold metadata | Databricks technical owner — to confirm |
| CAM-ASM-053 | Pilot results are suitable for executive communication with caveats alone | Rejected for current use | Complete metric governance and approve slide-safe wording first | Business rule owner and governance — to confirm |

## Validation approach

For each assumption:

1. identify the authoritative source;
2. confirm the responsible owner;
3. gather safe and proportionate evidence;
4. record whether the assumption is validated, refined or rejected;
5. update the relevant rule page;
6. update the rule register;
7. record material decisions in the decision log;
8. update risks where the result changes exposure; and
9. record the permitted use of the resulting rule or metric.

## Priority assumptions for the first workshop

Resolve these assumptions first:

1. CAM-ASM-011 — meaning of `records tested`;
2. CAM-ASM-012 — compatibility of dashboard-page totals;
3. CAM-ASM-018 — email presence versus usability;
4. CAM-ASM-019 — mobile presence versus usability;
5. CAM-ASM-023 — meaning of similarity threshold `1`;
6. CAM-ASM-024 — meaning and usefulness of threshold `0.9`;
7. CAM-ASM-030 — Organisation Account eligibility for ABN;
8. CAM-ASM-031 — Organisation Account eligibility for ACN;
9. CAM-ASM-037 — whether one ABN should map to one account;
10. CAM-ASM-038 — whether one ACN should map to one account;
11. CAM-ASM-043 — operational ownership; and
12. CAM-ASM-044 — operational review capacity.

## Related pages

- `risk-register.md`
- `status-and-validation-model.md`
- `../01-discover/databricks-customer-data-quality-pilot-input.md`
- `../01-discover/evidence-gaps.md`
- `../02-define/crm-data-quality-rule-register.md`
- `../02-define/crm-data-quality-rule-refinement-index.md`
- `../02-define/crm-data-quality-rule-refinement-workshop.md`
- `../02-define/rules/`
- `../06-decisions/decision-log.md`
