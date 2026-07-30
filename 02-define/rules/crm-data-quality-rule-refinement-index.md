# CRM data-quality rule refinement index

## Document control

| Field | Value |
|---|---|
| Status | Draft — business refinement required |
| Current phase | Define |
| Scope | First customer account data-quality refinement cycle |
| Governed metric status | Not ready |
| Last updated | 30 July 2026 |

## Purpose

Provide a single control page for the first customer account data-quality rule-refinement cycle.

This page:

- links the initial Databricks pilot evidence to the business-rule definitions;
- shows the current status of each priority rule;
- identifies common decisions required across the rule set;
- separates technical execution from governed business use; and
- provides a clear sequence for workshop refinement and approval.

Detailed rule logic remains in the individual rule pages.

## Current position

The initial Databricks customer data-quality pilot has demonstrated that a set of completeness, validity and uniqueness checks can be technically executed.

The pilot has not yet established:

- governed business definitions;
- approved eligible populations;
- compatible denominators;
- confirmed duplicate volumes;
- agreed operational responses;
- assigned rule ownership; or
- slide-safe performance measures.

The seven priority rules are therefore recorded as draft business definitions for refinement.

## Evidence input

| Evidence | Status | Permitted use |
|---|---|---|
| Initial Databricks and Power BI customer data-quality pilot | Partially validated | Rule refinement, denominator review, taxonomy review and workshop preparation |

Related page:

- `01-discover/databricks-customer-data-quality-pilot-input.md`

The pilot should not currently be used to claim that overall customer data quality is approximately 95.9%.

## Priority rule set

| Rule ID | Rule | Account type | Primary purpose | Current status |
|---|---|---|---|---|
| CAM-DQ-001 | Minimum valid contact method | Person Account | Contact completeness and usability | Draft — business refinement required |
| CAM-DQ-002 | Exact email duplicate signal | Person Account | Potential duplicate identification | Draft — business refinement required |
| CAM-DQ-003 | Exact mobile duplicate signal | Person Account | Potential duplicate identification | Draft — business refinement required |
| CAM-DQ-004 | ABN completeness | Organisation Account | Identifier completeness | Draft — business refinement required |
| CAM-DQ-005 | ACN completeness | Organisation Account | Identifier completeness | Draft — business refinement required |
| CAM-DQ-006 | Repeated ABN | Organisation Account | Potential duplicate identification | Draft — business refinement required |
| CAM-DQ-007 | Repeated ACN | Organisation Account | Potential duplicate identification | Draft — business refinement required |

## Rule pages

### Person Account rules

- `02-define/rules/CAM-DQ-001-minimum-valid-contact-method.md`
- `02-define/rules/CAM-DQ-002-exact-email-duplicate-signal.md`
- `02-define/rules/CAM-DQ-003-exact-mobile-duplicate-signal.md`

### Organisation Account rules

- `02-define/rules/CAM-DQ-004-abn-completeness.md`
- `02-define/rules/CAM-DQ-005-acn-completeness.md`
- `02-define/rules/CAM-DQ-006-repeated-abn.md`
- `02-define/rules/CAM-DQ-007-repeated-acn.md`

## Common refinement decisions

The following decisions affect multiple rules and should be resolved consistently.

### Population

Confirm:

- eligible Salesforce objects;
- included record types;
- active, inactive and historical-record treatment;
- merged and superseded-record treatment;
- test, training and system-record exclusions;
- activity or snapshot period;
- treatment of incomplete records; and
- treatment of records created through integrations or imports.

### Grain

Confirm whether each result represents:

- distinct accounts;
- distinct contacts;
- attribute evaluations;
- duplicate groups;
- duplicate pairs;
- rule executions; or
- record-rule combinations.

Every output must state its grain.

### Numerator and denominator

Confirm:

- the population eligible to pass or fail;
- whether blank values are included;
- whether exceptions are removed from the denominator;
- whether rule failures are mutually exclusive;
- whether multiple executions of one record are counted;
- whether account and contact populations are combined; and
- whether the same period and rule version apply to both numerator and denominator.

### Rule taxonomy

Use distinct categories for:

- completeness;
- format validity;
- reference validity;
- verification;
- uniqueness;
- duplicate signals;
- timeliness;
- accuracy; and
- consistency.

Do not classify similarity or potential-duplicate checks as ordinary validity checks without an explicit rationale.

### Exceptions

Each rule must identify:

- legitimate exceptions;
- how an exception is recorded;
- who approves exceptions;
- whether exceptions are measurable;
- when exceptions expire or require review; and
- whether an exception remains in or is removed from reporting.

### Operational response

For every failed rule, confirm whether the expected response is:

- correction during the next legitimate interaction;
- operational review;
- controlled remediation;
- upstream process improvement;
- Salesforce prevention;
- Plauti duplicate review;
- Databricks monitoring;
- governance escalation;
- approved exception; or
- no action.

A rule should not create an operational queue until ownership and capacity are agreed.

### Ownership

Each governed rule requires:

- business rule owner;
- operational owner;
- Salesforce technical owner where applicable;
- Plauti owner where applicable;
- Databricks technical owner;
- data owner or steward;
- merge authority for duplicate rules; and
- governance reviewers where required.

## Tool boundaries

| Capability | Intended role |
|---|---|
| Salesforce validation and duplicate controls | Prevent selected defects and support account search |
| Plauti Duplicate Check | Identify potential duplicates and support operational review |
| Databricks | Measure quality, monitor trends and support root-cause analysis |
| Power BI | Present approved analytical outputs and diagnostics |
| Human review | Confirm identity, determine exceptions and approve corrective action |
| Governance | Define standards, ownership, permitted use and escalation |

Databricks should not automatically reproduce Plauti logic.

Power BI should not turn exploratory technical outputs into governed metrics without approved definitions.

## Duplicate-rule language

Use:

- duplicate signal;
- potential duplicate;
- confirmed duplicate;
- rejected match;
- unresolved match;
- merge candidate; and
- merged.

Do not describe repeated email, mobile, ABN or ACN values as confirmed duplicates without review.

## Pilot findings requiring refinement

| Pilot observation | Refinement implication |
|---|---|
| Overall quality shown as approximately 95.9% | Reconcile grain, weighting and page totals before reporting |
| Different dashboard pages show different tested totals | Confirm filters, aggregation and refresh logic |
| Email and mobile completeness are very high | Confirm whether completeness means only non-blank values |
| ACN validity is approximately 56.59% | Rebuild the denominator around eligible company entities |
| ABN validity is approximately 81.80% | Separate missing, malformed, checksum-invalid and exempt records |
| Email uniqueness is approximately 86.02% | Treat as a duplicate signal, not a confirmed duplicate rate |
| ACN uniqueness is approximately 90.77% | Confirm legal-entity eligibility and reporting unit |
| ABN uniqueness is approximately 95.71% | Identify legitimate shared-ABN structures |
| Similarity checks appear under validity | Review the rule taxonomy |
| Account and contact tests appear in one dashboard | Confirm whether populations and grains are compatible |

## Refinement sequence

### Step 1 — Confirm the pilot calculation model

Confirm:

- what `records tested` means;
- the calculation grain;
- the source-table relationships;
- page-level filters;
- blank and exclusion handling;
- rule execution timing;
- threshold meaning;
- result weighting; and
- rule versioning.

### Step 2 — Refine Person Account rules

Work through:

1. CAM-DQ-001 — Minimum valid contact method;
2. CAM-DQ-002 — Exact email duplicate signal; and
3. CAM-DQ-003 — Exact mobile duplicate signal.

Resolve contact-method validity before interpreting completeness or duplicate outputs.

### Step 3 — Refine Organisation Account eligibility

Before interpreting ABN or ACN outputs, agree:

- organisation and legal-entity classifications;
- entities expected to hold an ABN;
- entities expected to hold an ACN;
- exempt organisation types;
- international-entity treatment; and
- unresolved-classification treatment.

### Step 4 — Refine identifier completeness rules

Work through:

1. CAM-DQ-004 — ABN completeness; and
2. CAM-DQ-005 — ACN completeness.

Keep presence, structural validity, checksum validity and external verification separate.

### Step 5 — Refine repeated-identifier rules

Work through:

1. CAM-DQ-006 — Repeated ABN; and
2. CAM-DQ-007 — Repeated ACN.

Confirm whether results are represented as records, groups or pairs.

### Step 6 — Confirm tool and action pathways

For each rule, decide:

- whether Salesforce should prevent the issue;
- whether Plauti should support operational review;
- whether Databricks should monitor the issue;
- whether Power BI should display the result;
- whether human confirmation is required; and
- what action follows a failure.

### Step 7 — Record decisions

After refinement:

- update the relevant rule page;
- update the rule register;
- record material decisions in the decision log;
- assign owners;
- record the rule version;
- confirm permitted use; and
- update governed metric status.

## Status progression

Each rule should progress through:

1. Draft — business refinement required;
2. In review;
3. Business definition agreed;
4. Technical logic validated;
5. Operational pathway agreed;
6. Governed for diagnostic use;
7. Governed for operational use, where applicable;
8. Approved for reporting, where applicable; or
9. Superseded or retired.

Technical execution alone does not move a rule to governed status.

## Definition of completion for the first refinement cycle

The first refinement cycle is complete when:

- all seven business questions have been reviewed;
- eligible populations are explicit;
- source fields and grain are confirmed;
- numerator and denominator definitions are compatible;
- exceptions are approved;
- tool boundaries are agreed;
- operational actions are documented;
- business, operational and technical owners are assigned;
- rule versions are recorded;
- pilot logic has been compared with the agreed definitions;
- material decisions are in the decision log; and
- each rule has an explicit permitted use.

## Current assessment

**Priority rule pages complete:** Yes.

**Pilot evidence recorded:** Yes.

**Business refinement complete:** No.

**Technical logic validated against business intent:** No.

**Operational ownership assigned:** No.

**Governed metrics available:** No.

**Slide-safe measures available:** No.

## Related repository pages

- `01-discover/databricks-customer-data-quality-pilot-input.md`
- `01-discover/evidence-gaps.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `02-define/crm-data-quality-rule-refinement-workshop.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`
