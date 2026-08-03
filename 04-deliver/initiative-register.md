# Initiative register

Status: Draft  
Owner: José Andrade  
Last updated: 3 August 2026

## Purpose

Track prioritised Customer Account Management initiatives that may progress from evidence and problem definition into investigation, design, testing or delivery.

This register supports prioritisation and visibility.

It does not confirm that an initiative:

- has been approved;
- has funding or delivery capacity;
- has an agreed technical solution;
- represents a validated root cause; or
- is ready for implementation.

## Current position

Six initial backlog items have been derived from reported customer-account and CRM issues.

The items remain working inputs and require validation with relevant business, operational, privacy, governance and technical owners before delivery decisions are made.

## Delivery backlog

| Priority | Initiative | Current issue | Customer or operational risk | Proposed next step | Status |
|---|---|---|---|---|---|
| High | Correct service-account linking | Service accounts may be linked to the wrong Person Account where identifying fields are shared or insufficiently differentiated. | Incorrect identity display, fragmented history and potential privacy impact. | Confirm current matching logic, affected scenarios, ownership and safe test cases. | Discovery required |
| High | Statutory and non-statutory duplicate resolution | Existing duplicate-management controls may not support safe merging across selected account types and service-account relationships. | Fragmented interactions, inconsistent communication, additional staff effort and integration risk. | Validate current Plauti configuration, merge restrictions, volumes and exception pathways. | Discovery required |
| High | Deceased-customer management | Deceased status may not flow consistently between source systems and Salesforce. | Inappropriate correspondence, surveys or account linking; reduced data integrity and reputational risk. | Map the current end-to-end process, identify the authoritative source and define safe handling requirements. | Discovery required |
| High | Customer information removal and restriction requests | Processes for correcting, restricting or removing customer information are not yet represented as one clear operational pathway. | Privacy non-compliance, unwanted contact, inaccurate records and loss of trust. | Confirm applicable obligations, retention constraints, decision ownership and operational workflow. | Definition required |
| Medium | Central customer record opt-out | Opt-out handling may rely on manual monitoring and may not be visible during case creation. | Customer preferences may be overridden, creating privacy, data-integrity and customer-experience risks. | Validate the current opt-out process, visibility gaps, controls and exception handling. | Discovery required |
| Medium | Customer authentication before record updates | A consistent authentication standard for updating customer information has not yet been confirmed. | Unauthorised changes, incorrect identification, complaints and compromised data integrity. | Document existing authentication practices and define where common or service-specific standards are required. | Discovery required |

## Prioritisation principles

Backlog priority should consider:

1. potential customer harm;
2. privacy, records and governance risk;
3. frequency and scale;
4. operational effort;
5. dependency on customer-data quality;
6. feasibility of safe investigation;
7. evidence strength; and
8. readiness of accountable owners.

Priority does not indicate that a solution has already been selected.

## Databricks pilot relationship

The Databricks customer-data-quality pilot may provide diagnostic evidence for selected backlog items, particularly:

- duplicate-account signals;
- contact-data completeness;
- account-type patterns;
- data-quality trends; and
- potential upstream creation pathways.

Databricks outputs must not be treated as confirmation of identity, duplicate status, privacy breach or required remediation without business and operational review.

The pilot input is recorded in:

`01-discover/databricks-customer-data-quality-pilot-input.md`

## Backlog decision fields

Before an initiative progresses into active delivery, record:

| Field | Requirement |
|---|---|
| Business question | The decision or outcome the initiative must support |
| Evidence | Validated evidence and known limitations |
| Owner | Accountable business or operational owner |
| Scope | Included and excluded processes, accounts or services |
| Dependencies | Systems, governance, data and stakeholder dependencies |
| Risk | Customer, privacy, operational and technical risks |
| Success measure | How improvement will be assessed |
| Delivery decision | Investigate, design, test, deliver, park or close |

## Current decisions

- Use the register as the controlled delivery backlog.
- Keep reported issues separate from validated root causes.
- Do not assume that Databricks, Salesforce validation, Plauti or automated merging is the solution.
- Prioritise safe investigation before implementation.
- Keep sensitive records and raw operational extracts in their organisational systems of record.

## Open questions

- Which backlog items have confirmed business owners?
- Which issues have validated volumes or recurrence evidence?
- Which items require Privacy, Records, Security or Data Governance review?
- Which current Salesforce or Plauti controls already address part of the issue?
- Which items are suitable for the initial Databricks pilot?
- What constitutes sufficient evidence to move an item into design?
- Which initiative should become the first controlled delivery experiment?

## Next action

Validate the first three high-priority items with the CRM Product Owner, operational representatives and relevant governance partners, then record whether each should proceed, remain in discovery or be parked.

## Review notes

<!-- AUTO-REVIEW-NOTES:START -->

| Date | Update | Updated by | Commit |
|---|---|---|---|

<!-- AUTO-REVIEW-NOTES:END -->