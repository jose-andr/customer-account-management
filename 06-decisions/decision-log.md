# Decision log

Status: Active  
Owner: José Andrade  
Last updated: 29 July 2026

## Purpose

Record material decisions affecting the Customer Account Management workstream.

Use this log for decisions that change:

- scope;
- evidence use;
- ownership;
- design direction;
- rule interpretation;
- implementation readiness; or
- the relationship between systems and repositories.

Detailed rationale may be recorded in a separate decision record under:

`06-decisions/records/`

## Decision status

| Status | Meaning |
|---|---|
| Proposed | Decision has been raised but not agreed |
| Agreed | Decision is active for the current workstream |
| Conditional | Decision applies subject to stated validation or dependency |
| Superseded | Replaced by a later decision |
| Rejected | Considered and not adopted |

## Decisions

| ID | Date | Decision | Rationale | Evidence or source | Owner | Status |
|---|---|---|---|---|---|---|
| DEC-001 | 29 July 2026 | Use a 4D structure for the Customer Account Management repository | Provides a traceable structure for Discover, Define, Design, Deliver and iterative learning | Initial workstream direction | José Andrade | Agreed |
| DEC-002 | 29 July 2026 | Treat `jose-andr/cx-current-state-sop-mapping` as an input rather than duplicating its content | Keeps current-state operational evidence separate from transformation framing and future design | Repository boundary defined in `00-project-control/purpose-and-scope.md` | José Andrade | Agreed |
| DEC-003 | 29 July 2026 | Use the aligned draft problem statement as the current working definition | Preserves stakeholder alignment while keeping unresolved evidence and scope questions visible | Customer Account Management April 2026 problem-framing material | José Andrade | Conditional |
| DEC-004 | 29 July 2026 | Treat current CRM data-quality rules as work in progress until business definitions, ownership and results are validated | The existing inventory contains active, proposed, parked and incomplete rules | Salesforce Data Quality Rules Confluence page | José Andrade | Agreed |
| DEC-005 | 29 July 2026 | Keep the Salesforce Data Quality Rules Confluence page as the working source of truth for the detailed rule inventory | Prevents the GitHub repository from becoming a duplicate operational rule table | [Salesforce Data Quality Rules](https://jira-cityofmelbourne.atlassian.net/wiki/spaces/DP/pages/527597570/Salesforce+Data+Quality+Rules) | José Andrade | Agreed |
| DEC-006 | 29 July 2026 | Use this repository to record rule-refinement outcomes, evidence gaps, caveats, ownership and implementation readiness | GitHub is being used for transformation logic and decision traceability, not detailed operational configuration | `01-discover/evidence-gaps.md` and `02-define/crm-data-quality-rule-refinement.md` | José Andrade | Agreed |
| DEC-007 | 29 July 2026 | Refine CRM data-quality rules as a business activity before treating Databricks outputs as governed measures | Technical implementation must follow agreed business meaning, population, grain, exceptions and actionability | CRM rule-refinement workstream | José Andrade | Agreed |
| DEC-008 | 29 July 2026 | Distinguish potential duplicates from confirmed duplicates | Analytical or Plauti matching signals do not establish customer identity or justify merging without review | Plauti configuration and current duplicate-rule inventory | José Andrade | Agreed |
| DEC-009 | 29 July 2026 | Treat Salesforce validation rules, Plauti, Databricks and operational review as separate but connected controls | Each capability serves a different role in prevention, detection, monitoring and human decision-making | `02-define/crm-data-quality-rule-refinement.md` | José Andrade | Agreed |
| DEC-010 | 29 July 2026 | Do not assume Databricks should reproduce Plauti matching logic | Duplicate analytical controls require an explicit purpose such as monitoring, coverage validation, trend analysis or root-cause investigation | Plauti and Databricks comparison | José Andrade | Agreed |
| DEC-011 | 29 July 2026 | Prioritise a small first group of Customer Account Management rules for refinement | A contained first cycle is more practical than attempting to refine the full CRM quality inventory | `02-define/crm-data-quality-rule-register.md` | José Andrade | Agreed |
| DEC-012 | 29 July 2026 | Park case, work-order, knowledge, call-recording and other service-specific quality rules from the first Customer Account Management refinement cycle | These may be legitimate CRM-quality concerns but are not all customer-account rules | Initial refinement scope | José Andrade | Agreed |

## Conditions attached to decisions

### DEC-003 — Working problem statement

The aligned draft problem statement remains conditional until:

- supporting evidence is consolidated;
- affected stakeholders review the scope;
- key assumptions are tested;
- customer and employee impacts are better evidenced; and
- adjacent customer-data topics are explicitly included or excluded.

### DEC-004 — Rule maturity

A CRM data-quality rule must not be treated as governed until:

- the business question is agreed;
- the population is explicit;
- the grain is explicit;
- valid exceptions are documented;
- ownership is assigned;
- the technical logic has been tested;
- outputs have been reviewed; and
- the permitted decision use is recorded.

### DEC-008 — Duplicate status

Use these terms consistently:

| Term | Meaning |
|---|---|
| Duplicate signal | A condition suggesting records may be related |
| Potential duplicate | Records, pairs or groups flagged by a matching rule |
| Confirmed duplicate | Records reviewed and determined to represent the same customer or organisation |
| Rejected match | Potential duplicate reviewed and determined not to be a duplicate |
| Unresolved match | Potential duplicate that cannot yet be confirmed or rejected |

### DEC-009 — Control roles

| Control | Agreed role |
|---|---|
| Salesforce validation rules | Prevent selected invalid or incomplete data from being saved |
| Plauti Duplicate Check | Identify potential duplicates and support operational review |
| Databricks data-quality rules | Measure quality conditions, monitor trends and support analysis |
| Operational review | Confirm identity, assess risk and decide whether corrective action is safe |
| Governance | Define standards, ownership, thresholds and escalation |
| Root-cause improvement | Reduce defects created by upstream process or system design |
## Additional decisions — first CRM data-quality rule-refinement cycle

### CAM-DEC-013 — Use the Databricks customer data-quality pilot as a refinement input

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-013 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Use the initial Databricks and Power BI customer data-quality pilot as exploratory evidence for refining business-rule definitions, populations, denominators, grain, taxonomy and operational responses. |
| Rationale | The pilot demonstrates that technical checks can be executed and reveals useful diagnostic signals, but the underlying business definitions and calculation bases are not yet sufficiently validated for governed reporting. |
| Implication | Pilot results may inform workshops, technical validation and rule prioritisation. They must not be treated as approved customer data-quality measures. |
| Related files | `01-discover/databricks-customer-data-quality-pilot-input.md`; `02-define/crm-data-quality-rule-refinement-index.md` |

### CAM-DEC-014 — Do not use the 95.9% pilot result as a governed customer data-quality score

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-014 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Do not describe the pilot’s approximate 95.9% aggregate pass rate as the organisation’s customer data-quality, accuracy or reliability score. |
| Rationale | The dashboard combines different rules and potentially different account, contact, attribute and rule-execution populations. Page-level tested totals are also not yet reconciled. |
| Implication | Any communication of the result must label it as an exploratory aggregate rule-pass rate and include its unresolved grain, weighting and denominator caveats. |
| Related files | `01-discover/databricks-customer-data-quality-pilot-input.md` |

### CAM-DEC-015 — Reconcile the pilot calculation model before approving reporting use

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-015 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Require reconciliation of the pilot calculation model before any rule or overall result is approved for operational or executive reporting. |
| Rationale | The Full Records and All Attributes views show different tested totals, and the meaning of `records tested` has not been confirmed. |
| Implication | Technical validation must confirm source tables, grain, page filters, blank handling, exclusions, rule timing, thresholds, aggregation and rule versioning. |
| Related files | `01-discover/databricks-customer-data-quality-pilot-input.md`; `02-define/crm-data-quality-rule-refinement-index.md` |

### CAM-DEC-016 — Separate completeness, validity, verification, uniqueness and duplicate signals

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-016 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Use distinct rule categories for completeness, format validity, reference validity, verification, uniqueness and duplicate signals. |
| Rationale | The pilot currently places some similarity and duplicate-detection checks under validity, which may cause potential matches to be interpreted as invalid records. |
| Implication | The business-rule taxonomy and Power BI presentation should be refined before governed use. Similarity checks must be labelled as duplicate or potential-match signals where appropriate. |
| Related files | `01-discover/databricks-customer-data-quality-pilot-input.md`; `02-define/crm-data-quality-rule-refinement-index.md` |

### CAM-DEC-017 — Establish seven rules as the first business-refinement set

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-017 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Use the following seven rules as the first contained business-refinement set: minimum valid contact method, exact email duplicate signal, exact mobile duplicate signal, ABN completeness, ACN completeness, repeated ABN and repeated ACN. |
| Rationale | These rules cover the highest-priority contact, identifier and duplicate-quality questions already represented in the pilot and existing rule inventory. |
| Implication | Lower-priority name, trading-name, secondary-contact, fuzzy-match and external-verification rules remain in the backlog until the first cycle clarifies the operating pattern. |
| Related files | `02-define/crm-data-quality-rule-refinement-index.md`; `02-define/crm-data-quality-rule-register.md` |

### CAM-DEC-018 — Keep all seven priority rules in draft status

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-018 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Keep all seven priority rules at `Draft — business refinement required` until their populations, logic, exceptions, owners and permitted uses are agreed. |
| Rationale | Technical execution in Databricks does not establish that the corresponding business rule is valid, operationally actionable or approved. |
| Implication | No rule should move to governed status solely because a dashboard result exists. |
| Related files | `02-define/rules/`; `00-project-control/status-and-validation-model.md` |

### CAM-DEC-019 — Define minimum valid contact method separately from field completeness

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-019 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Treat minimum valid contact method as a business rule that may combine multiple accepted contact methods, rather than equating it with a populated email or mobile field. |
| Rationale | A populated value may be malformed, outdated, unusable, unverified or inappropriate for contact. Customers may also legitimately use different accepted methods. |
| Implication | Email and mobile completeness results must not be presented as usable customer-contact coverage until validity and exception logic are agreed. |
| Related files | `02-define/rules/CAM-DQ-001-minimum-valid-contact-method.md` |

### CAM-DEC-020 — Treat exact email and mobile matches as duplicate signals only

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-020 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Treat exact email and exact mobile matches as potential duplicate signals requiring review, not as proof of duplicate identity. |
| Rationale | Contact details may legitimately be shared by families, households, carers, representatives or supported customers. Mobile numbers may also be recycled. |
| Implication | No account merge or customer-level action may be triggered solely by an exact email or mobile match. |
| Related files | `02-define/rules/CAM-DQ-002-exact-email-duplicate-signal.md`; `02-define/rules/CAM-DQ-003-exact-mobile-duplicate-signal.md` |

### CAM-DEC-021 — Define ABN and ACN eligibility before interpreting completeness

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-021 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Define which Organisation Account and legal entity types are expected to hold an ABN or ACN before calculating governed completeness rates. |
| Rationale | Not every organisation requires both identifiers. Using all Organisation Accounts as the denominator would overstate failure and create misleading comparisons. |
| Implication | Missing, malformed, checksum-invalid, exempt, unclassifiable and externally verified records must be separated where they imply different decisions or actions. |
| Related files | `02-define/rules/CAM-DQ-004-abn-completeness.md`; `02-define/rules/CAM-DQ-005-acn-completeness.md` |

### CAM-DEC-022 — Treat repeated ABN and ACN values as review signals

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-022 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Treat repeated ABN and ACN values as organisation-account review signals rather than confirmed duplicate organisations or automatic merge candidates. |
| Rationale | One legal entity may legitimately have multiple operational accounts, locations, service relationships, trading names or historical records. |
| Implication | Outputs must state whether they count records, groups or pairs and must use controlled human review before confirmation or merge. |
| Related files | `02-define/rules/CAM-DQ-006-repeated-abn.md`; `02-define/rules/CAM-DQ-007-repeated-acn.md` |

### CAM-DEC-023 — Require compatible numerator and denominator definitions

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-023 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Require every governed rate to use a numerator and denominator with the same population, grain, period, exclusions and rule version. |
| Rationale | Combining incompatible activity bases or grains produces technically calculated but misleading results. |
| Implication | Each rule must record its business question, source, grain, eligible population, numerator, denominator, filters, period and caveats before reporting approval. |
| Related files | `02-define/crm-data-quality-rule-refinement-index.md`; `00-project-control/status-and-validation-model.md` |

### CAM-DEC-024 — Require an operational response before governed rule use

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-024 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Do not approve a rule for governed operational use until the expected response, owner, capacity, exception process and escalation pathway are agreed. |
| Rationale | A technically valid failure list can create unmanaged queues, inappropriate customer contact or unsafe record changes when no operating process exists. |
| Implication | Rules may remain diagnostic even after technical validation. Operational use requires separate approval. |
| Related files | `02-define/crm-data-quality-rule-refinement-index.md`; `02-define/crm-data-quality-rule-refinement-workshop.md` |

### CAM-DEC-025 — Preserve distinct tool responsibilities

| Field | Detail |
|---|---|
| Decision ID | CAM-DEC-025 |
| Status | Agreed for current project use |
| Date | 30 July 2026 |
| Decision | Preserve distinct responsibilities for Salesforce, Plauti, Databricks, Power BI, human review and governance. |
| Rationale | The tools support different stages of prevention, detection, monitoring, presentation, confirmation and decision-making. Duplicating logic without a defined purpose increases inconsistency and operational risk. |
| Implication | Databricks should not automatically reproduce Plauti logic, and Power BI should not present exploratory technical results as governed measures. |
| Related files | `02-define/crm-data-quality-rule-refinement-index.md`; `01-discover/evidence-gaps.md` |
## Open decisions

| ID | Decision required | Evidence needed | Owner | Status |
|---|---|---|---|---|
| ODEC-001 | What constitutes the minimum valid contact method for an active Person Account? | Service needs, current account rules and valid exceptions | To confirm | Open |
| ODEC-002 | What output grain should be used for duplicate reporting: records, pairs or groups? | Plauti behaviour, operational workflow and reporting need | To confirm | Open |
| ODEC-003 | Which Plauti scenarios are currently active in production? | Current configuration and job validation | CRM Product Owner | Open |
| ODEC-004 | Which Databricks rules are implemented, scheduled or producing reviewed results? | Technical implementation review | Databricks or Data Governance support | Open |
| ODEC-005 | Which organisation types require an ABN or ACN? | Business and legal entity definitions | To confirm | Open |
| ODEC-006 | Who owns the business definition and operational action for each rule? | Role and ownership review | To confirm | Open |
| ODEC-007 | Which first rules are ready to move into Databricks implementation? | Completed refinement workshop and Definition of Ready checks | Workshop participants | Open |

## Next decision point

After the first CRM data-quality rule-refinement workshop, update this log with:

- approved rules;
- parked or rejected rules;
- assigned owners;
- confirmed Plauti relationships;
- agreed metric definitions; and
- implementation decisions.
