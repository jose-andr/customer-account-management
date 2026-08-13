# Constraints and boundaries

Status: Draft
Owner: José Andrade
Last updated: 13 August 2026

## Purpose

Define the boundaries and constraints that must be considered when assessing the viability of Customer Account Management improvements.

These constraints are not reasons to avoid change.

They ensure that opportunities are assessed against the actual organisational environment rather than an unconstrained future-state concept.

## North star

> Assess the viability of improvements to Customer Account Management and potential future investment at City of Melbourne, using evidence to support prioritisation and business-case decisions.

## Boundary principle

A viable improvement must work across four conditions:

1. it addresses a meaningful customer, operational or risk problem;
2. it can operate within applicable organisational controls;
3. its dependencies and implementation complexity are understood; and
4. the expected value is proportionate to the effort and investment required.

## In scope

The Define phase may consider improvements to:

* customer identity and account relationships;
* duplicate prevention;
* duplicate identification and safe resolution;
* Customer Account data quality;
* Service Account and Person Account relationships;
* customer contact-data quality;
* sensitive customer statuses;
* customer preferences and restrictions;
* customer authentication for account maintenance;
* CRM data-quality rules;
* operational review and remediation;
* customer-data stewardship;
* ownership and governance;
* source-process improvement;
* analytics and monitoring;
* relevant Salesforce controls;
* relevant Plauti controls;
* relevant Databricks diagnostics;
* integration dependencies;
* operating-model capability; and
* evidence required for future investment decisions.

## Out of scope for current Define activity

The current phase does not approve or design:

* a replacement CRM;
* a master customer platform;
* a new enterprise customer-data platform;
* a universal customer identifier;
* automated account merging;
* organisation-wide identity management;
* technology procurement;
* a full enterprise data-governance operating model;
* wholesale redesign of every customer-facing service;
* migration of raw customer information into the repository;
* automated remediation without human oversight; or
* a formal financial business case before the value and viability evidence is sufficient.

These may become future options if evidence supports them.

## Solution neutrality

The work should define the required capability before selecting the implementation.

For example:

| Need                                | Do not automatically translate it into      |
| ----------------------------------- | ------------------------------------------- |
| Better customer identity confidence | One master customer ID                      |
| Fewer duplicates                    | Automated merging                           |
| Better duplicate prevention         | More cleansing                              |
| Better data quality                 | More Databricks rules                       |
| Better account relationships        | CRM replacement                             |
| Clearer governance                  | More policy documents                       |
| Better customer continuity          | One central record for every interaction    |
| Better authentication               | One authentication method for every service |

Potential responses may combine:

* process improvement;
* service design;
* governance;
* operating model;
* staff capability;
* CRM configuration;
* data-quality controls;
* analytics;
* integration;
* automation; and
* technology investment.

## Customer boundary

Customer Account Management should support customer experience without assuming that every customer:

* has an online account;
* uses digital channels;
* provides the same contact information;
* has a simple one-person-to-one-account relationship;
* can be represented safely through standard rules;
* wants the same type of interaction;
* can satisfy the same authentication pattern; or
* should have every interaction consolidated into one view.

Assisted and exception pathways must remain possible where required.

## Account-model boundary

A Salesforce Person Account record should not automatically be treated as equivalent to a unique customer.

Possible complexities include:

* multiple records associated with one person;
* shared contact details;
* statutory and non-statutory account relationships;
* representatives;
* organisations;
* household relationships;
* historical records;
* Service Accounts;
* restricted records; and
* potential duplicates.

Any analytical or design decision must state the account grain explicitly.

## Identity boundary

Customer identity cannot be established safely from a single data-quality signal alone.

For example:

* shared email does not prove identity;
* shared mobile does not prove identity;
* matching names do not prove identity;
* duplicate signals do not prove duplicate status; and
* account creation order does not establish which record is authoritative.

Identity decisions may require:

* multiple attributes;
* contextual information;
* operational verification;
* system rules;
* approved evidence; and
* human review.

## Duplicate-management boundary

Use the following terms consistently:

* duplicate signal;
* potential duplicate;
* confirmed duplicate;
* rejected match;
* unresolved match;
* merge candidate; and
* merged.

A potential duplicate should not automatically become a merge candidate.

A merge candidate should not automatically be merged.

Any future merge approach must consider:

* customer identity;
* account relationships;
* statutory requirements;
* linked services;
* records obligations;
* integration behaviour;
* permissions;
* reversal controls; and
* consequences of an incorrect merge.

## Privacy and records boundary

Customer Account Management improvements must operate within approved privacy, records and information-management requirements.

The repository should record:

* decision logic;
* summaries;
* field names;
* evidence references;
* caveats;
* assumptions;
* governance questions; and
* approved rules.

It must not store:

* customer personal information;
* raw CRM extracts;
* unredacted operational examples;
* credentials;
* security information;
* uncontrolled screenshots; or
* sensitive records belonging in organisational systems of record.

Where a privacy or records interpretation is required, obtain the appropriate organisational advice rather than embedding an unvalidated interpretation as a project requirement.

## Governance boundary

The project can identify governance needs but should not invent organisation-wide policy.

Define should clarify:

* what decision needs ownership;
* what standard is required;
* who may approve it;
* what operational control is needed;
* where exceptions are recorded; and
* how issues are escalated.

Formal governance decisions remain with the relevant organisational authority.

## Technology boundary

Technology is an enabler, not the starting definition of the problem.

### Salesforce

May support:

* account records;
* validation;
* workflow;
* customer relationships;
* operational controls; and
* customer-service activity.

Do not assume Salesforce configuration alone can resolve every Customer Account Management problem.

### Plauti

May support:

* duplicate signals;
* duplicate review;
* matching scenarios; and
* controlled merge activity.

Do not treat Plauti output as confirmation that two records represent the same customer without the required review.

### Databricks

May support:

* profiling;
* diagnostics;
* data-quality rules;
* baselines;
* trends;
* segmentation; and
* root-cause analysis.

Databricks should not independently determine:

* customer identity;
* confirmed duplicate status;
* merge decisions;
* customer consent;
* deceased status;
* privacy obligations; or
* required remediation.

### Other technology

Future technology options should only be assessed when a defined capability gap cannot be addressed adequately through existing capability, process, governance or modest configuration improvement.

## Analytics boundary

A calculated result is not automatically a decision-safe metric.

Before a result is treated as governed evidence, confirm:

* business question;
* source;
* grain;
* eligible population;
* numerator;
* denominator;
* filters;
* exclusions;
* exception treatment;
* rule version;
* ownership;
* caveats; and
* permitted use.

Do not describe account-record metrics as customer metrics unless the relationship has been validated.

## Operating-model boundary

A technology control without an operating response may create an unmanaged queue rather than an improvement.

For any proposed control, clarify:

* who owns the rule;
* who monitors failures;
* who reviews exceptions;
* who corrects records;
* who investigates root cause;
* who approves changes;
* who measures effectiveness; and
* who escalates unresolved risk.

Operating ownership is part of viability.

## Delivery boundary

Define should not produce detailed implementation plans before an opportunity has passed a viability decision.

Progression should follow:

```text
Evidence
→ Problem definition
→ Value hypothesis
→ Viability assessment
→ Prioritisation decision
→ Design / controlled test
→ Delivery decision
→ Implementation
→ Evaluation
```

Skipping directly from a reported issue to implementation increases the risk of solving the wrong problem.

## Investment boundary

The current work may identify an investment signal.

It does not yet establish:

* investment amount;
* procurement approach;
* financial benefit;
* return on investment;
* implementation cost;
* funding source; or
* approved business case.

An opportunity should only escalate toward business-case development when there is enough evidence to explain:

1. the material problem;
2. who or what is affected;
3. the current baseline;
4. expected value;
5. why current capability is insufficient;
6. feasible response options;
7. major constraints and dependencies;
8. likely implementation complexity; and
9. how success would be measured.

## Desktop-scan boundary

External research should inform decisions, not create requirements by imitation.

For each external example, distinguish:

* what the organisation actually did;
* why it did it;
* evidence of outcomes;
* contextual differences;
* what appears transferable;
* what remains uncertain; and
* what City of Melbourne should investigate further.

Do not conclude that a practice is viable locally simply because another organisation uses it.

## Constraint register

Use this table during viability assessment.

| Constraint                                      | Why it matters                                                           | Opportunities affected                | Evidence status                               | Decision implication                                   |
| ----------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------- | --------------------------------------------- | ------------------------------------------------------ |
| Complex Person Account relationships            | One record may not represent one unique customer                         | CAM-OPP-001, CAM-OPP-002              | Known complexity; further validation required | Identity and duplicate logic require controlled review |
| Service Account relationships                   | Incorrect linking may create customer and privacy impact                 | CAM-OPP-001, CAM-OPP-002, CAM-OPP-003 | Reported evidence                             | Validate linking and relationship behaviour            |
| Statutory and non-statutory account differences | Merge and account handling may have different constraints                | CAM-OPP-002                           | Reported evidence                             | Do not assume common merge rules                       |
| Current Plauti configuration                    | Existing controls may enable or constrain options                        | CAM-OPP-002                           | Requires production validation                | Assess current capability before investment            |
| Current Salesforce controls                     | Existing validation and workflow may already address part of the problem | Multiple                              | Partially known                               | Confirm before proposing new capability                |
| Databricks rule maturity                        | Diagnostics may not yet be governed                                      | Multiple                              | Work in progress                              | Use exploratory results with caveats                   |
| Privacy requirements                            | Some options may require specialist review                               | Multiple                              | Depends on issue                              | Include governance review before progression           |
| Records requirements                            | Deletion, merge and status changes may have retention implications       | CAM-OPP-002, CAM-OPP-003, CAM-OPP-004 | Requires specialist input                     | Do not encode assumptions                              |
| Operational ownership                           | Controls require ongoing action                                          | All                                   | Ownership gaps remain                         | Ownership is a viability criterion                     |
| Baseline evidence                               | Scale and effort are not yet quantified consistently                     | All                                   | Incomplete                                    | Limit investment claims until baselines improve        |

## Viability stop conditions

An opportunity should not progress into Design or investment assessment when:

* the underlying problem remains unsupported;
* the affected population cannot be described;
* the proposed value is unclear;
* a major governance constraint is unresolved;
* no accountable owner exists;
* the intervention would create unacceptable customer risk;
* the required capability already exists but has not been tested;
* the measurement approach cannot distinguish improvement from activity;
* a simpler response has not been considered; or
* additional research is unlikely to change the decision.

## Viability progression conditions

An opportunity may progress when:

* the problem is sufficiently evidenced;
* the customer, operational or risk value is explicit;
* material constraints are understood;
* relevant external evidence has been considered where useful;
* the opportunity fits organisational context;
* ownership can be established;
* feasible response options exist;
* success can be measured; and
* further design or investment analysis is proportionate to the opportunity.

## Current boundary decision

At this stage:

* the project remains solution-neutral;
* existing capability should be understood before additional investment is proposed;
* analytics remain diagnostic until definitions are governed;
* customer identity and duplicate status require appropriate human and operational controls;
* governance requirements should be confirmed rather than inferred;
* operating ownership is part of viability;
* external examples should inform rather than dictate the response; and
* financial business-case development is premature until stronger baseline and viability evidence exists.

## Next action

Use these boundaries during the desktop scan and first viability assessment.

For each priority opportunity, identify:

1. the material constraints;
2. which constraints are confirmed;
3. which require specialist validation;
4. whether existing capability can address the problem;
5. whether the constraints materially weaken or strengthen viability; and
6. whether the opportunity should Progress, Investigate further, Escalate for investment assessment or Park.

## Review notes

<!-- AUTO-REVIEW-NOTES:START -->

| Date | Update | Updated by | Commit |
| ---- | ------ | ---------- | ------ |

<!-- AUTO-REVIEW-NOTES:END -->
