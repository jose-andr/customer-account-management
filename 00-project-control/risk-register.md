# Risk register

Status: Active  
Owner: José Andrade  
Current stage: Discover → Define  
Last updated: 29 July 2026

## Purpose

Record risks that could affect Customer Account Management decisions, CRM data-quality refinement, Databricks implementation or future transformation activity.

This register helps the workstream:

- distinguish evidence gaps from delivery risks;
- make potential customer and operational harm visible;
- assign risk ownership;
- identify controls and mitigations;
- prevent premature technical implementation;
- preserve governance constraints; and
- escalate material issues before they become embedded.

This register is a working decision-support artefact.

It does not replace formal organisational risk, privacy, security, records or project-management systems.

## Risk status

| Status | Meaning |
|---|---|
| Open | Risk has been identified and requires action |
| Monitoring | Risk is being watched but no immediate action is required |
| Mitigating | Agreed mitigation activity is underway |
| Escalated | Risk requires formal decision or governance review |
| Accepted | Risk has been consciously accepted by the authorised owner |
| Closed | Risk is no longer active |
| Superseded | Replaced by a more precise risk |

## Risk rating

Use a simple working rating:

| Rating | Meaning |
|---|---|
| Low | Limited consequence or unlikely to affect the next decision |
| Medium | Could materially affect quality, effort or delivery |
| High | Could cause significant customer, operational, governance or decision harm |
| Critical | Could create serious privacy, identity, service or organisational harm |

Formal organisational risk frameworks take precedence where required.

## Active risks

| ID | Risk | Potential impact | Rating | Owner | Status |
|---|---|---|---|---|---|
| RSK-001 | Potential duplicates may be interpreted as confirmed duplicates | Incorrect reporting, unsafe merge decisions and overstated problem scale | High | CRM Product Owner | Open |
| RSK-002 | Two different customers may be incorrectly merged | Privacy harm, data loss, service disruption and customer harm | Critical | To confirm | Open |
| RSK-003 | Databricks rules may be implemented before business definitions are agreed | Technically correct but misleading outputs | High | José Andrade | Mitigating |
| RSK-004 | Databricks rules may duplicate Plauti without a clear purpose | Duplicate effort, conflicting results and unclear ownership | Medium | CRM Product Owner | Open |
| RSK-005 | Rule populations, grain or denominators may be inconsistent | Unsafe trend reporting and misleading percentages | High | Databricks or Data Governance representative | Open |
| RSK-006 | CRM rule results may have no operational action owner | Unmanaged queues, unresolved defects and low trust in reporting | High | To confirm | Open |
| RSK-007 | Existing Plauti documentation may not reflect current production configuration | Incorrect rule comparisons and false assumptions about current controls | High | CRM Product Owner | Open |
| RSK-008 | Existing Salesforce Data Quality Rules may not reflect the latest working inventory | Decisions may be based on outdated or incomplete rules | Medium | José Andrade | Open |
| RSK-009 | Missing contact information may be treated as a defect where valid exceptions exist | Exclusion, inappropriate remediation and distorted quality measures | High | Business rule owner | Open |
| RSK-010 | Shared contact details may generate false duplicate signals | High review effort and risk of incorrect identity decisions | High | CRM Product Owner | Open |
| RSK-011 | Repeated ABN or ACN may be treated as proof of duplicate organisations | Valid organisation relationships may be removed or merged incorrectly | High | To confirm | Open |
| RSK-012 | Fuzzy-name matching may create excessive false positives | Operational burden and reduced trust in the rules | High | CRM Product Owner | Open |
| RSK-013 | CRM data-quality outputs may be interpreted as proof of customer impact | Weak evidence may be overstated in strategic decisions | Medium | José Andrade | Open |
| RSK-014 | Current operational practice may depend on undocumented individual knowledge | Continuity risk, inconsistency and slow onboarding | High | Customer Data and Systems Support Officer | Open |
| RSK-015 | Upstream duplicate causes may remain unresolved while remediation activity increases | Ongoing recurrence and growing operational effort | High | To confirm | Open |
| RSK-016 | Privacy, records or security requirements may be considered too late | Rework, blocked implementation or unsafe design | Critical | Governance owners | Open |
| RSK-017 | Rule priorities may be driven by ease of implementation rather than business value | Low-value reporting and delayed improvement | Medium | José Andrade | Mitigating |
| RSK-018 | Customer Account Management may expand into broader customer-data strategy without clear scope | Diluted focus, duplicated work and unclear ownership | Medium | Customer Focus and Strategy Manager | Monitoring |
| RSK-019 | GitHub may duplicate operational Confluence or system-of-record content | Conflicting sources and maintenance burden | Medium | José Andrade | Mitigating |
| RSK-020 | Raw or identifiable customer data may be copied into the repository | Privacy, security and records breach | Critical | José Andrade | Open |
| RSK-021 | Current rule results may be presented before validation | Misleading executive reporting and premature decisions | High | Business rule owner | Open |
| RSK-022 | Historical records may be measured against current standards without caveat | Inflated failure rates and unfair interpretation | Medium | Business rule owner | Open |
| RSK-023 | A rule may be approved without a clear action on failure | Results accumulate without improvement | High | Business rule owner | Open |
| RSK-024 | Different systems may use incompatible customer definitions | Conflicting measures and unclear account relationships | High | To confirm | Open |
| RSK-025 | Service-specific exceptions may be ignored in organisation-wide rules | Poor fit, incorrect remediation and stakeholder resistance | High | Service owners | Open |

## Critical risks

### RSK-002 — Incorrect merge

**Risk**

Two different customers may be incorrectly merged.

**Possible causes**

- insufficient matching evidence;
- over-reliance on email or phone;
- shared household contact details;
- common names;
- inaccurate fuzzy matching;
- incomplete operational review;
- inappropriate automation;
- unclear merge authority; or
- pressure to reduce duplicate counts.

**Potential consequences**

- customer information linked to the wrong person;
- sensitive information exposure;
- loss of valid records;
- incorrect service history;
- incorrect communications;
- service interruption;
- complaint or incident;
- difficult reversal; and
- loss of customer trust.

**Required controls**

- potential and confirmed duplicate status kept separate;
- human review before merge;
- documented merge criteria;
- authorised merge permissions;
- high-risk scenarios escalated;
- traceable merge decision;
- recovery or reversal process;
- privacy and records review; and
- quality assurance.

**Next action**

Validate the actual merge decision process, permissions and recovery controls.

---

### RSK-016 — Governance considered too late

**Risk**

Privacy, records, security or data-governance requirements may be considered after rules or workflows have already been designed.

**Possible consequences**

- rework;
- blocked deployment;
- unsafe matching or data linkage;
- inappropriate access;
- insufficient audit evidence;
- unclear ownership;
- unauthorised external verification; and
- loss of stakeholder confidence.

**Required controls**

- governance review triggered by rule type and data use;
- privacy and records input for identity and merge rules;
- security review for access or platform changes;
- data-owner confirmation;
- documented permitted use;
- approved escalation pathway; and
- no automated merge without explicit approval.

**Next action**

Identify which first-cycle rules require Privacy, Records, Security or Data Governance review.

---

### RSK-020 — Sensitive information in GitHub

**Risk**

Raw organisational or customer-identifiable information may be copied into this repository.

**Potential consequences**

- privacy breach;
- unauthorised access;
- records-management failure;
- data leakage;
- repository removal or restriction; and
- loss of trust.

**Required controls**

Do not store:

- customer names;
- contact details;
- account identifiers;
- identifiable case information;
- raw CRM extracts;
- screenshots containing sensitive data;
- credentials;
- access tokens; or
- controlled organisational records.

Use:

- de-identified summaries;
- synthetic examples;
- aggregate outputs;
- source links;
- field names;
- caveats; and
- decision records.

**Next action**

Keep all future evidence records privacy-safe and link to authorised source locations rather than copying source data.

## CRM rule-specific risks

### Contact-completeness rules

| Risk | Control |
|---|---|
| Email or mobile treated as mandatory for every customer | Confirm service need and valid exceptions |
| Secondary contact details ignored | Define whether secondary values qualify |
| Postal-only customers treated as invalid | Confirm accepted contact modes |
| Inactive or historical accounts inflate failure rates | Define population and exclusions |
| Completeness presented as accuracy | State that populated data may still be incorrect |

### Person duplicate rules

| Risk | Control |
|---|---|
| Shared household email creates false positives | Define shared-contact exceptions |
| Shared mobile number creates false positives | Require contextual review |
| Common names inflate matches | Test rule performance |
| Pair counts are confused with duplicate groups | Define grain explicitly |
| Potential duplicates are reported as confirmed | Use controlled terminology |
| Databricks and Plauti produce conflicting results | Compare logic and intended purpose |

### Organisation rules

| Risk | Control |
|---|---|
| ABN or ACN treated as mandatory for every organisation | Define eligible entity types |
| Repeated identifier treated as automatic duplicate | Review valid multiple-account relationships |
| Branches and subsidiaries are merged incorrectly | Define organisation relationship model |
| External source used without approval | Confirm legal, technical and governance authority |
| Trading names treated as unique identifiers | Treat as supporting evidence only |

## Measurement risks

| Risk | Example | Required response |
|---|---|---|
| Wrong denominator | Missing-email rate divided by all CRM records instead of eligible Person Accounts | Define eligible population |
| Mixed grain | Flagged records combined with duplicate groups | Report separately |
| Mixed rule versions | Trend compares different matching thresholds | Version and caveat results |
| Mixed time periods | Current failures compared with lifetime account creation | Align period |
| Historical bias | Old accounts assessed using new standards | Separate historical and current cohorts |
| Incomplete coverage | Only selected Salesforce record types assessed | State coverage |
| Potential treated as confirmed | Match output described as duplicate count | Use “potential duplicate” |
| Completeness treated as accuracy | Populated email assumed valid | Separate completeness and validity |

## Operational risks

| ID | Operational risk | Mitigation |
|---|---|---|
| OPS-001 | Rule outputs create more work than the team can review | Estimate volume before scheduling |
| OPS-002 | Results are not prioritised | Add severity and action rules |
| OPS-003 | Duplicate candidates remain unresolved | Track outcome and ageing |
| OPS-004 | Review relies on one officer | Document process and decision criteria |
| OPS-005 | Merge permissions are too broad or too narrow | Validate role and permission model |
| OPS-006 | Work is tracked outside the system of record | Confirm traceable completion method |
| OPS-007 | Root causes are not fed back to product or service owners | Add escalation and improvement loop |
| OPS-008 | False positives reduce trust in the framework | Review precision and adjust thresholds |

## Risk controls required before rule approval

A rule should not be approved unless:

- business meaning is agreed;
- population is explicit;
- grain is explicit;
- valid exceptions are documented;
- existing Salesforce and Plauti controls are understood;
- action on failure is clear;
- ownership is assigned;
- privacy and governance implications are considered;
- false-positive and false-negative risks are reviewed;
- technical logic has been tested;
- results are explainable; and
- permitted use is recorded.

## Risk escalation triggers

Escalate a risk when:

- customer identity may be incorrectly changed;
- sensitive information could be linked incorrectly;
- automated merge or correction is proposed;
- a rule uses external identity data;
- results are intended for executive or formal reporting;
- no business owner can be identified;
- conflicting system definitions cannot be reconciled;
- rule outputs exceed operational review capacity;
- a production control appears not to be functioning; or
- a privacy, records or security concern remains unresolved.

## Risk actions

| Action ID | Related risk | Action | Owner | Status |
|---|---|---|---|---|
| ACT-001 | RSK-001, RSK-002 | Define and use duplicate-status terminology | José Andrade | In progress |
| ACT-002 | RSK-003 | Complete business refinement before technical approval | José Andrade | In progress |
| ACT-003 | RSK-004, RSK-007 | Validate current Plauti production configuration | CRM Product Owner | Open |
| ACT-004 | RSK-005 | Confirm grain, numerator and denominator for first rules | Databricks or Data Governance representative | Open |
| ACT-005 | RSK-006, RSK-023 | Assign business and operational action owners | Customer Focus and Strategy Manager | Open |
| ACT-006 | RSK-009 | Define valid contact-method requirements and exceptions | To confirm | Open |
| ACT-007 | RSK-010, RSK-012 | Test false positives for duplicate rules | CRM Product Owner | Open |
| ACT-008 | RSK-011 | Validate organisation identifier and relationship rules | To confirm | Open |
| ACT-009 | RSK-014 | Complete operational duplicate-process walkthrough | Customer Data and Systems Support Officer | Open |
| ACT-010 | RSK-015 | Identify upstream duplicate-creation pathways | CRM Product Owner | Open |
| ACT-011 | RSK-016 | Identify governance review requirements | José Andrade | Open |
| ACT-012 | RSK-020 | Maintain privacy-safe repository handling | José Andrade | Active |
| ACT-013 | RSK-021 | Prevent use of results until validation status is explicit | Business rule owner | Open |
| ACT-014 | RSK-024 | Map customer definitions across relevant systems | To assign | Open |

## Current risk position

The highest current risks are:

1. incorrect customer or organisation merges;
2. technically implemented rules with incomplete business meaning;
3. misleading metrics caused by incompatible populations or grains;
4. unclear ownership of rule outcomes;
5. outdated assumptions about Plauti or Salesforce controls;
6. delayed privacy, records, security or governance review; and
7. raw or identifiable data entering the repository.

These risks should be reduced before the workstream moves from rule refinement into governed reporting or future-state design.

## Next action

Review the critical and high-rated risks during the first CRM data-quality refinement workshop and assign owners for all open mitigation actions.
