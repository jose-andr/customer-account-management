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

Test the assumptions attached to the first CRM rule-refinement workshop and update each assumption immediately after the relevant decision is made.
