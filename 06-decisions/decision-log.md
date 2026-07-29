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
