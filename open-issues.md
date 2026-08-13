# Open issues

Source status: Stakeholder-owned
Repository treatment: Preserved source artefact
Publishing position: Repository root
Publishing rule: Preserve stakeholder-authored content; do not automatically rewrite or restructure
Owner: To be confirmed
Last updated: 3 August 2026

> This page preserves the stakeholder-created Customer Account Management issue register for ownership and provenance. Changes to the substantive issue content should be agreed with the page owner.

## 1.1. Purpose

Track reported Customer Account Management issues that may require further discovery, definition, design or delivery.

This register preserves the priorities and evidence supplied in the working Customer Account Management table.

An item appearing in this register does not confirm:

* the reported cause;
* the scale or frequency of the issue;
* an approved solution;
* an agreed delivery commitment;
* a confirmed privacy breach;
* a technology requirement; or
* an accountable business owner.

## 1.2. Status model

| Status              | Meaning                                                           |
| ------------------- | ----------------------------------------------------------------- |
| Reported            | Issue has been raised but not yet validated                       |
| Discovery required  | Current state, evidence and affected processes need investigation |
| Definition required | The problem, scope, rules or ownership need agreement             |
| Design required     | A response or operating pattern needs to be developed             |
| Delivery ready      | Scope, ownership, controls and measures are sufficiently defined  |
| Parked              | Not currently progressing                                         |
| Closed              | No further action required                                        |

## 1.3. Priority summary

| Priority | Number of items |
| -------- | --------------: |
| High     |               4 |
| Medium   |               2 |
| Total    |               6 |

## 1.4. Initiative backlog

| Rank | Priority | Initiative                                                      | Issue raised  | Evidence reference                                     | Current status      |
| ---: | -------- | --------------------------------------------------------------- | ------------- | ------------------------------------------------------ | ------------------- |
|    1 | High     | Service Accounts linking to an incorrect Person Account         | 5 March 2026  | Two reported email examples dated March and June 2026  | Discovery required  |
|    2 | High     | Merge restrictions across statutory and non-statutory customers | April 2025    | #291605, #291629 and related duplicate-management work | Discovery required  |
|    3 | High     | Marking a customer as deceased                                  | 26 March 2025 | SR#290875                                              | Discovery required  |
|    4 | High     | Customer requests to remove or restrict CRM details             | Not recorded  | No reference recorded                                  | Definition required |
|    5 | Medium   | Customers who opt out of a central customer record              | Not recorded  | No reference recorded                                  | Discovery required  |
|    6 | Medium   | Customer authentication before updating details                 | Not recorded  | No reference recorded                                  | Definition required |

## 1.5. CAM-INIT-001 — Service Accounts linking to an incorrect Person Account

### 1.5.1. Priority

High — rank 1

### 1.5.2. Issue raised

5 March 2026

### 1.5.3. Reported issue

Service Accounts may be linked to an incorrect Person Account.

The reported scenario occurs where multiple Person Accounts share the same email address and mobile number. The service may be linked to the earliest-created Person Account even where the first name differs.

### 1.5.4. Evidence reference

Two reported email examples dated:

* 5 March 2026; and
* 12 June 2026.

Personal names and email content remain in the organisational system of record and are not reproduced in this repository.

### 1.5.5. Reported reasoning

Shared contact information may be treated as sufficient for automated account linking even when other identity information differs.

The current evidence does not yet confirm:

* the exact matching logic;
* whether the behaviour applies to every Service Account workflow;
* which system performs the linking;
* how frequently it occurs;
* whether first name is used in matching;
* whether the affected records are potential or confirmed duplicates; or
* whether the behaviour remains active.

### 1.5.6. Reported risks

* A customer may see another person's name on their Service Account.
* A Service Account may be linked to a partner's Person Account.
* A Service Account may be linked to a deceased person's account.
* Customer information may be exposed to the wrong person.
* Customer identity and account relationships may become unreliable.
* Staff may need to investigate and correct linked records manually.

These are reported risks. Any privacy incident must be assessed through the approved organisational process.

### 1.5.7. Proposed next steps

1. Confirm the system and workflow responsible for linking Service Accounts.
2. Document the current matching fields and precedence rules.
3. Validate the reported scenarios using de-identified test cases.
4. Confirm whether name differences affect matching.
5. Identify the current correction and escalation process.
6. Determine whether preventative, warning or review controls are appropriate.
7. Assign a business owner and technical owner.

### 1.5.8. Current status

Discovery required

## 1.6. CAM-INIT-002 — Merge restrictions across statutory and non-statutory customers

### 1.6.1. Priority

High — rank 2

### 1.6.2. Issue raised

April 2025

### 1.6.3. Evidence reference

* #291605 — Plauti issue logged, 2 April 2025
* #291629 — duplicate statutory and non-statutory accounts, 2 April 2025
* related work concerning duplicate detection and merge configuration

The source table refers to additional duplicate-management work, but the identifiers were not preserved clearly enough in the uploaded CSV to record them reliably.

### 1.6.4. Reported issue

Plauti may not allow statutory customers to be merged with non-statutory customers where a Service Account relationship exists.

This may contribute to duplicate Person Accounts remaining unresolved in Salesforce.

### 1.6.5. Reported reasoning

Restrictions in the current duplicate-management process may prevent staff from resolving account records that represent the same customer but have different account types or service relationships.

The current evidence does not yet confirm:

* the current production Plauti configuration;
* the precise merge restriction;
* whether the restriction is intentional;
* the number of affected records;
* the risks associated with allowing these merges;
* which account should survive;
* which relationships must be preserved; or
* whether a merge is always the correct resolution.

### 1.6.6. Reported risks

* Customer interactions and history may be spread across several records.
* Staff may miss relevant information when managing enquiries.
* Customers may receive inconsistent communications.
* Integrations may reference different customer records.
* Cases, requests or notifications may be linked to the wrong record.
* Staff may spend additional time finding the correct account.
* Manual checks may be required before creating or updating customers.
* Duplicate management and cleansing effort may increase.

### 1.6.7. Proposed next steps

1. Validate the current Plauti configuration in production.
2. Confirm which statutory and non-statutory account combinations cannot be merged.
3. Measure affected records using a denominator-safe method.
4. Document relationship, integration and recordkeeping constraints.
5. Define valid merge, non-merge and exception scenarios.
6. Confirm merge permissions, review controls and reversal arrangements.
7. Assign operational and technical owners.

### 1.6.8. Current status

Discovery required

## 1.7. CAM-INIT-003 — Marking a customer as deceased

### 1.7.1. Priority

High — rank 3

### 1.7.2. Issue raised

26 March 2025

### 1.7.3. Evidence reference

SR#290875

### 1.7.4. Reported issue

The organisation needs a consistent way to record that a customer is deceased so that inappropriate contact, surveys and account linking do not continue.

For statutory customers, evidence may be recorded in Pathway, but the status may not flow into Salesforce.

### 1.7.5. Reported reasoning

The absence of a consistent end-to-end process may cause deceased-customer information to be recorded differently across systems.

The current evidence does not yet confirm:

* the authoritative source;
* the approved evidence requirement;
* which teams may update the status;
* whether Salesforce has an appropriate field;
* how the status should affect communications;
* how related Service Accounts should be handled;
* privacy and records requirements; or
* whether integrations can propagate the status safely.

### 1.7.6. Reported risks

* Correspondence or surveys may be sent to a deceased person.
* Service Accounts may be linked to a deceased person's record.
* Customer records may remain inconsistent across systems.
* Staff may repeat checks or data entry.
* Customer service may be distressing or inappropriate.
* Data integrity, governance and reputational risks may increase.

### 1.7.7. Proposed next steps

1. Map the current process across Pathway, Salesforce and operational teams.
2. Confirm the authoritative source for deceased status.
3. Clarify evidence, access, privacy and records requirements.
4. Define the minimum Salesforce status and handling rules.
5. Identify affected communications, surveys, cases and Service Accounts.
6. Define exception and correction processes.
7. Assign business, operational and technical owners.

### 1.7.8. Current status

Discovery required

## 1.8. CAM-INIT-004 — Customer requests to remove or restrict CRM details

### 1.8.1. Priority

High — rank 4

### 1.8.2. Issue raised

Not recorded

### 1.8.3. Evidence reference

No reference was included in the source table.

### 1.8.4. Reported issue

Customers may ask for their personal information to be removed, corrected or no longer used.

The organisation needs a clear way to assess and action these requests while meeting legal, operational, privacy, records and retention obligations.

### 1.8.5. Reported reasoning

Customer requests should be managed so that information remains accurate, necessary, appropriately used and protected.

A request to remove information must not be interpreted as an automatic deletion requirement. The permissible response depends on applicable legislation, policy, recordkeeping obligations, service needs and approved organisational guidance.

### 1.8.6. Reported risks

* Continued unwanted contact
* Inaccurate or unnecessary personal information
* Unauthorised use or disclosure
* Privacy or compliance concerns
* Reputational damage
* Reduced customer trust
* Inconsistent treatment of customer requests

### 1.8.7. Proposed next steps

1. Confirm the applicable privacy, legal and records requirements.
2. Distinguish correction, deletion, restriction, suppression and communication-preference requests.
3. Map the current request and approval process.
4. Define decision ownership and escalation.
5. Identify system and integration impacts.
6. Define how actions and reasons are recorded.
7. Establish customer-facing response standards.

### 1.8.8. Current status

Definition required

## 1.9. CAM-INIT-005 — Customers who opt out of a central customer record

### 1.9.1. Priority

Medium — rank 5

### 1.9.2. Issue raised

Not recorded

### 1.9.3. Evidence reference

No reference was included in the source table.

### 1.9.4. Reported issue

Some customers may not want their information stored or shared through a central customer record.

The current process may rely on manual report monitoring and staff intervention to identify and de-link cases associated with opted-out accounts.

Opt-out notes may not be visible to Customer Experience Officers during case creation.

### 1.9.5. Reported reasoning

Customer preferences and applicable privacy requirements must be respected while maintaining lawful and operationally necessary records.

The current evidence does not yet confirm:

* the approved meaning of opt-out;
* whether customers may opt out of every relevant use;
* which systems and processes are affected;
* where the preference is recorded;
* how staff see the preference;
* which cases must be de-linked;
* how exceptions are handled; or
* who owns monitoring.

### 1.9.6. Reported risks

* Records may continue to be consolidated contrary to an approved preference.
* Staff may not see relevant opt-out information.
* Manual monitoring may miss affected records.
* Customer data may be used or shared inconsistently.
* Privacy, compliance and customer-experience impacts may occur.
* Data integrity may deteriorate through repeated linking and de-linking.

### 1.9.7. Proposed next steps

1. Confirm the approved definition and scope of central-record opt-out.
2. Map the current process and report monitoring.
3. Identify where the preference is recorded and displayed.
4. Confirm which workflows create or consolidate records.
5. Define permitted exceptions and retention requirements.
6. Assess whether staff need an in-workflow warning or control.
7. Assign an accountable owner for monitoring and remediation.

### 1.9.8. Current status

Discovery required

## 1.10. CAM-INIT-006 — Customer authentication before updating details

### 1.10.1. Priority

Medium — rank 6

### 1.10.2. Issue raised

Not recorded

### 1.10.3. Evidence reference

No reference was included in the source table.

### 1.10.4. Reported issue

Staff need to confirm that they are interacting with the correct customer before accessing or changing customer information.

A consistent authentication approach has not yet been documented in this register.

### 1.10.5. Reported reasoning

Authentication helps prevent unauthorised access and changes while protecting customer privacy and data integrity.

Authentication requirements may differ by channel, service, transaction risk and information sensitivity. A single method should not be assumed to be suitable for every interaction.

### 1.10.6. Reported risks

* Updates may be made to the wrong account.
* Information may be disclosed to an unauthorised person.
* Customer complaints may increase.
* Data integrity may be reduced.
* Fraudulent access may become more likely.
* Customers may be identified incorrectly.
* Staff may apply inconsistent authentication practices.

### 1.10.7. Proposed next steps

1. Document current authentication practices by channel and interaction type.
2. Identify existing organisational standards and controls.
3. Classify interactions by risk and information sensitivity.
4. Define minimum evidence for common scenarios.
5. Document exception and escalation pathways.
6. Confirm how authentication outcomes are recorded.
7. Assign policy, operational and technical owners.

### 1.10.8. Current status

Definition required

## 1.11. Cross-initiative dependencies

| Dependency                                      | Relevant initiatives                                                 |
| ----------------------------------------------- | -------------------------------------------------------------------- |
| Person Account matching and identity logic      | CAM-INIT-001, CAM-INIT-002, CAM-INIT-006                             |
| Service Account relationships                   | CAM-INIT-001, CAM-INIT-002, CAM-INIT-003                             |
| Plauti configuration                            | CAM-INIT-002                                                         |
| Pathway and Salesforce integration              | CAM-INIT-003                                                         |
| Privacy and records guidance                    | CAM-INIT-001, CAM-INIT-003, CAM-INIT-004, CAM-INIT-005, CAM-INIT-006 |
| Customer preferences and communication controls | CAM-INIT-003, CAM-INIT-004, CAM-INIT-005                             |
| Staff procedures and training                   | All initiatives                                                      |
| Databricks diagnostic analysis                  | CAM-INIT-001, CAM-INIT-002 and selected supporting measures          |

## 1.12. Databricks pilot relationship

The Databricks customer-data-quality pilot may help investigate:

* potential duplicate-account patterns;
* Person Accounts sharing email and mobile values;
* account-type combinations;
* records linked through selected service relationships;
* data completeness;
* source-system patterns; and
* quality trends over time.

Databricks outputs must not independently determine:

* customer identity;
* confirmed duplicate status;
* whether records should be merged;
* whether a privacy breach occurred;
* deceased status;
* customer consent;
* authentication success; or
* whether personal information should be deleted.

The pilot input is documented in:

`01-discover/databricks-customer-data-quality-pilot-input.md`

## 1.13. Delivery readiness requirements

Before an initiative becomes delivery ready, confirm:

| Requirement          | Expected evidence                                                     |
| -------------------- | --------------------------------------------------------------------- |
| Business question    | The decision or outcome is explicit                                   |
| Current state        | Actual processes, systems and controls are documented                 |
| Evidence             | Reported examples are validated and safely summarised                 |
| Scope                | Included and excluded scenarios are clear                             |
| Ownership            | Business, operational and technical owners are assigned               |
| Governance           | Privacy, records, security and legal input is obtained where required |
| Solution neutrality  | The problem is defined before a solution is selected                  |
| Measures             | Baseline, grain, numerator, denominator and caveats are agreed        |
| Test approach        | Safe test cases and acceptance criteria are documented                |
| Operational response | Review, remediation and escalation pathways are defined               |
| Decision             | Proceed, test, park or close is recorded                              |

## 1.14. Decisions required

| Decision                                                     | Owner          | Status |
| ------------------------------------------------------------ | -------------- | ------ |
| Confirm the accountable owner for each initiative            | To be assigned | Open   |
| Validate the reported issue and current-state behaviour      | To be assigned | Open   |
| Confirm which initiatives require formal privacy assessment  | To be assigned | Open   |
| Select the first controlled investigation                    | To be assigned | Open   |
| Confirm which issues are suitable for Databricks diagnostics | To be assigned | Open   |
| Agree the threshold for progression into design              | To be assigned | Open   |

## 1.15. Recommended first investigation

Start with:

**CAM-INIT-001 — Service Accounts linking to an incorrect Person Account**

This initiative has:

* the highest stated priority;
* recent reported examples;
* a direct customer-identity concern;
* potential privacy impact;
* a relationship to duplicate and matching logic; and
* a clear need for controlled technical and operational validation.

The first investigation should establish the actual linking behaviour before proposing a technical change.

## 1.16. Source and privacy note

This register was derived from the supplied Customer Account Management table.

Raw emails, personal names, customer records and case details must remain in approved organisational systems of record.

Only de-identified references, summaries, caveats and decision logic should be retained in this repository.

## 1.17. Review notes

| Date       | Update                                                         | Updated by   | Commit    |
| ---------- | -------------------------------------------------------------- | ------------ | --------- |
| 2026-08-03 | 04-deliver/initiative-register.md edited online with Bitbucket | Jose Andrade | `a7def31` |
| 2026-08-03 | 04-deliver/initiative-register.md edited online with Bitbucket | Jose Andrade | `125f01c` |
| 2026-08-03 | 04-deliver/initiative-register.md edited online with Bitbucket | Jose Andrade | `a20ff3e` |
| 2026-07-29 | Add Customer Account Management 4D repository scaffold         | Jose Andrade | `397d0cf` |
