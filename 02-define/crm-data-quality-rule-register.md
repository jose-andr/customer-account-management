# CRM data-quality rule register

Status: In progress  
Owner: José Andrade  
Current stage: Define  
Last updated: 29 July 2026

## Purpose

This register tracks the business refinement, ownership and implementation readiness of CRM data-quality rules.

It is used to:

- convert rule ideas into clear business definitions;
- distinguish Salesforce, Plauti and Databricks responsibilities;
- assign ownership;
- identify valid exceptions;
- define safe measures;
- record unresolved questions;
- prioritise implementation; and
- approve, park or reject rules.

The detailed working rule inventory remains in Confluence:

[Salesforce Data Quality Rules](https://jira-cityofmelbourne.atlassian.net/wiki/spaces/DP/pages/527597570/Salesforce+Data+Quality+Rules)

This register records decision-relevant refinement outcomes rather than duplicating the full Confluence rule table.

## Source boundaries

| Source | Purpose |
|---|---|
| Salesforce Data Quality Rules Confluence page | Current working rule inventory and technical details |
| Plauti Duplicate Check Configuration | Existing operational duplicate-detection configuration |
| `cx-current-state-sop-mapping` | Current duplicate-review and remediation practices |
| This register | Business definitions, ownership, decisions and implementation readiness |

## Status definitions

### Definition status

| Status | Meaning |
|---|---|
| Proposed | Initial rule or business question |
| In refinement | Business meaning, scope or ownership is incomplete |
| Ready for implementation | Business definition is agreed and complete |
| Parked | Not currently progressing |
| Rejected | Reviewed and not required |
| Superseded | Replaced by another rule |

### Execution status

| Status | Meaning |
|---|---|
| Not started | No technical implementation has begun |
| In development | Logic is being created |
| Implemented | Logic exists but is not necessarily scheduled |
| Scheduled | Rule runs at an agreed frequency |
| Results under review | Results exist but are not yet governed |
| Validated | Rule and outputs are approved for the stated use |
| Failed | Rule cannot currently run reliably |
| Retired | Rule is no longer active |

## Priority rule register

| Rule ID | Rule name | Primary control | Quality dimension | Definition status | Execution status | Priority | Business owner |
|---|---|---|---|---|---|---|---|
| CAM-DQ-001 | Minimum valid contact method | Salesforce / Databricks | Completeness | In refinement | To confirm | Critical | To confirm |
| CAM-DQ-002 | Exact email duplicate signal | Plauti / Databricks | Uniqueness | In refinement | To confirm | Critical | To confirm |
| CAM-DQ-003 | Exact mobile duplicate signal | Plauti / Databricks | Uniqueness | In refinement | To confirm | Critical | To confirm |
| CAM-DQ-004 | Organisation ABN completeness | Salesforce / Databricks | Completeness | In refinement | To confirm | High | To confirm |
| CAM-DQ-005 | Organisation ACN completeness | Salesforce / Databricks | Completeness | In refinement | To confirm | High | To confirm |
| CAM-DQ-006 | Repeated ABN duplicate signal | Plauti / Databricks | Uniqueness | In refinement | To confirm | High | To confirm |
| CAM-DQ-007 | Repeated ACN duplicate signal | Plauti / Databricks | Uniqueness | In refinement | To confirm | High | To confirm |
| CAM-DQ-008 | Person name similarity duplicate signal | Plauti / Databricks | Uniqueness | Proposed | To confirm | Medium | To confirm |
| CAM-DQ-009 | Organisation name duplicate signal | Plauti / Databricks | Uniqueness | Proposed | To confirm | Medium | To confirm |
| CAM-DQ-010 | Trading name duplicate signal | Plauti / Databricks | Uniqueness | Proposed | To confirm | Medium | To confirm |
| CAM-DQ-011 | Primary mobile format | Salesforce / Databricks | Validity | Proposed | To confirm | Medium | To confirm |
| CAM-DQ-012 | Person name character validity | Salesforce / Databricks | Validity | Proposed | To confirm | Medium | To confirm |

## CAM-DQ-001 — Minimum valid contact method

### Business question

What proportion of active Person Accounts do not have a usable contact method, and what customer or service interactions are affected?

### Working business rule

An active Person Account should contain at least one usable contact method unless an approved exception applies.

### Decisions required

- Is one contact method sufficient?
- Which contact methods qualify?
- Is email required for selected services?
- Is mobile required for selected services?
- Are postal-only customers valid?
- Which inactive or historical accounts are excluded?
- Are deceased customers excluded?
- What approved exceptions apply?
- What action follows a failed result?

### Working definition

| Field | Current position |
|---|---|
| Account type | Person Account |
| Population | Active Person Accounts |
| Grain | One row per account |
| Attributes | Primary email, secondary email, primary mobile, phone, address |
| Failure condition | No usable contact method |
| Exclusions | To define |
| Numerator | Active Person Accounts with no usable contact method |
| Denominator | All eligible active Person Accounts |
| Output unit | Count and percentage |
| Primary control | Salesforce prevention and Databricks monitoring |
| Action on failure | To define |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |

## CAM-DQ-002 — Exact email duplicate signal

### Business question

How many eligible Person Accounts share the same email address and exact name, and how many are confirmed as duplicates after operational review?

### Working business rule

Two or more Person Accounts with the same normalised email address and exact normalised name should be flagged as potential duplicates.

### Decisions required

- Which email field is primary?
- Should secondary email be included?
- How is email normalised?
- How are shared household email addresses handled?
- How are representatives or carers handled?
- Are inactive accounts included?
- Is the output a pair or duplicate group?
- Does this align with the current Plauti scenario?
- What review outcome makes a duplicate confirmed?

### Working definition

| Field | Current position |
|---|---|
| Account type | Person Account |
| Population | Eligible Person Accounts |
| Grain | Duplicate group |
| Attributes | Name and email |
| Failure condition | Same normalised email and exact normalised name |
| Exclusions | Shared or approved contact arrangements to define |
| Numerator | Potential duplicate groups |
| Denominator | Not required for count; required if a rate is reported |
| Output unit | Duplicate groups |
| Primary control | Plauti detection and Databricks monitoring |
| Action on failure | Operational review |
| Business owner | To confirm |
| Operational owner | Customer Data and Systems Support — to confirm |
| Technical owner | To confirm |
| Definition status | In refinement |

## CAM-DQ-003 — Exact mobile duplicate signal

### Business question

How many eligible Person Accounts share the same mobile number and exact name, and how many are confirmed as duplicates?

### Working business rule

Two or more Person Accounts with the same normalised mobile number and exact normalised name should be flagged as potential duplicates.

### Decisions required

- How are phone numbers normalised?
- Are international numbers included?
- How are shared family numbers handled?
- How are carers or representatives handled?
- Are landline and mobile fields compared?
- Are inactive accounts included?
- Is the output a pair or duplicate group?
- Does the rule match the current Plauti scenario?

### Working definition

| Field | Current position |
|---|---|
| Account type | Person Account |
| Population | Eligible Person Accounts |
| Grain | Duplicate group |
| Attributes | Name and mobile number |
| Failure condition | Same normalised mobile and exact normalised name |
| Exclusions | Shared or approved contact arrangements to define |
| Numerator | Potential duplicate groups |
| Denominator | Not required for count; required if a rate is reported |
| Output unit | Duplicate groups |
| Primary control | Plauti detection and Databricks monitoring |
| Action on failure | Operational review |
| Business owner | To confirm |
| Operational owner | Customer Data and Systems Support — to confirm |
| Technical owner | To confirm |
| Definition status | In refinement |

## CAM-DQ-004 — Organisation ABN completeness

### Business question

What proportion of eligible active organisation accounts do not contain an ABN where an ABN is required?

### Working business rule

An active organisation account should contain an ABN when its organisation type requires one.

### Decisions required

- Which account types require an ABN?
- Can an organisation legitimately operate without one?
- Are government, community or informal entities excluded?
- Are inactive accounts excluded?
- Is a blank ABN a defect or an exception?
- Who is responsible for correction?

### Working definition

| Field | Current position |
|---|---|
| Account type | Organisation |
| Population | Active organisation accounts requiring an ABN |
| Grain | One row per account |
| Attribute | ABN |
| Failure condition | ABN is blank |
| Exclusions | Organisation types not requiring an ABN |
| Numerator | Eligible accounts without ABN |
| Denominator | All eligible organisation accounts |
| Output unit | Count and percentage |
| Primary control | Salesforce prevention and Databricks monitoring |
| Action on failure | Review and correction |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |

## CAM-DQ-005 — Organisation ACN completeness

### Business question

What proportion of eligible active organisation accounts do not contain an ACN where an ACN is required?

### Working business rule

An active organisation account should contain an ACN when its legal entity type requires one.

### Decisions required

- Which organisation types require an ACN?
- Is an ABN sufficient for some accounts?
- Which entities do not have an ACN?
- Are inactive accounts excluded?
- Who validates the organisation type?
- Who corrects missing values?

### Working definition

| Field | Current position |
|---|---|
| Account type | Organisation |
| Population | Active organisation accounts requiring an ACN |
| Grain | One row per account |
| Attribute | ACN |
| Failure condition | ACN is blank |
| Exclusions | Entity types not requiring an ACN |
| Numerator | Eligible accounts without ACN |
| Denominator | All eligible organisation accounts |
| Output unit | Count and percentage |
| Primary control | Salesforce prevention and Databricks monitoring |
| Action on failure | Review and correction |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |

## CAM-DQ-006 — Repeated ABN duplicate signal

### Business question

How many organisation accounts share the same ABN, and which represent true duplicates rather than valid multiple-account relationships?

### Working business rule

Two or more eligible organisation accounts sharing the same normalised ABN should be flagged for review.

### Decisions required

- Does one ABN always represent one valid organisation account?
- Can branches or service relationships justify multiple accounts?
- Are inactive records included?
- How are historical or superseded records handled?
- Is the output a pair or duplicate group?
- Should matching organisation name also be required?
- Does this align with Plauti?

### Working definition

| Field | Current position |
|---|---|
| Account type | Organisation |
| Population | Organisation accounts with a populated ABN |
| Grain | Duplicate group |
| Attribute | ABN |
| Failure condition | Same normalised ABN across multiple eligible accounts |
| Exclusions | Valid multi-account structures to define |
| Numerator | Potential duplicate groups |
| Denominator | Not required for count; required if a rate is reported |
| Output unit | Duplicate groups |
| Primary control | Plauti detection and Databricks monitoring |
| Action on failure | Operational and business review |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |

## CAM-DQ-007 — Repeated ACN duplicate signal

### Business question

How many organisation accounts share the same ACN, and which represent true duplicates?

### Working business rule

Two or more eligible organisation accounts sharing the same normalised ACN should be flagged for review.

### Decisions required

- Does one ACN always represent one valid organisation account?
- Can valid multiple-account structures exist?
- Are inactive records included?
- Should organisation name also be compared?
- Is the output a pair or group?
- Does this align with Plauti?

### Working definition

| Field | Current position |
|---|---|
| Account type | Organisation |
| Population | Organisation accounts with a populated ACN |
| Grain | Duplicate group |
| Attribute | ACN |
| Failure condition | Same normalised ACN across multiple eligible accounts |
| Exclusions | Valid multi-account structures to define |
| Numerator | Potential duplicate groups |
| Denominator | Not required for count; required if a rate is reported |
| Output unit | Duplicate groups |
| Primary control | Plauti detection and Databricks monitoring |
| Action on failure | Operational and business review |
| Business owner | To confirm |
| Operational owner | To confirm |
| Technical owner | To confirm |
| Definition status | In refinement |

## Lower-priority rule backlog

| Rule ID | Rule | Primary unresolved issue | Status |
|---|---|---|---|
| CAM-DQ-008 | Person name similarity duplicate signal | Appropriate threshold and false-positive risk | Proposed |
| CAM-DQ-009 | Organisation name duplicate signal | Name normalisation and valid multi-account structures | Proposed |
| CAM-DQ-010 | Trading name duplicate signal | Shared trading names and legal-entity relationships | Proposed |
| CAM-DQ-011 | Primary mobile format | International-number support | Proposed |
| CAM-DQ-012 | Person name character validity | Valid punctuation and diacritics | Proposed |

## Workshop decision table

Use this table during the refinement session.

| Rule ID | Business definition agreed | Population agreed | Grain agreed | Exceptions agreed | Owner assigned | Plauti alignment checked | Decision |
|---|---|---|---|---|---|---|---|
| CAM-DQ-001 | No | No | Yes | No | No | Not applicable | In refinement |
| CAM-DQ-002 | No | No | No | No | No | No | In refinement |
| CAM-DQ-003 | No | No | No | No | No | No | In refinement |
| CAM-DQ-004 | No | No | Yes | No | No | Not applicable | In refinement |
| CAM-DQ-005 | No | No | Yes | No | No | Not applicable | In refinement |
| CAM-DQ-006 | No | No | No | No | No | No | In refinement |
| CAM-DQ-007 | No | No | No | No | No | No | In refinement |

## Decision outcomes

Use one of the following outcomes for each rule:

| Decision | Meaning |
|---|---|
| Approve | Ready for implementation |
| Refine | More business definition is required |
| Validate | Current configuration or evidence must be checked |
| Park | Not currently progressing |
| Reject | Rule is not required |
| Supersede | Another rule replaces it |

## Current decision

The first refinement session will focus on:

1. CAM-DQ-001 — Minimum valid contact method;
2. CAM-DQ-002 — Exact email duplicate signal;
3. CAM-DQ-003 — Exact mobile duplicate signal;
4. CAM-DQ-004 — Organisation ABN completeness;
5. CAM-DQ-005 — Organisation ACN completeness;
6. CAM-DQ-006 — Repeated ABN duplicate signal; and
7. CAM-DQ-007 — Repeated ACN duplicate signal.

No rule should be approved for governed reporting until:

- the business definition is agreed;
- the population and grain are explicit;
- valid exceptions are documented;
- ownership is assigned;
- Plauti alignment is checked where relevant;
- the operational action is clear; and
- the result has been tested and reviewed.

## Next action

Use this register in the first business refinement workshop and update the decision table immediately after the session.
