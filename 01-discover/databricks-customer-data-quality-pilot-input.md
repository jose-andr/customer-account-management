# Databricks customer data-quality pilot input

## Document control

| Field | Value |
|---|---|
| Evidence item | Initial customer data-quality pilot dashboard |
| Evidence type | Exploratory analytical output |
| Source platform | Databricks data-quality outputs presented through Power BI Report Server |
| Source tables shown | `vwaccount`, `vwcontact` |
| Dashboard test date shown | 19 June 2026 |
| Evidence recorded | 30 July 2026 |
| Validation status | Partially validated |
| Governed metric status | Not ready |
| Current use | Business-rule refinement input |

## Purpose

Record the initial customer data-quality pilot as an input to the refinement of business rules for customer account and contact quality checks.

The pilot provides useful evidence about:

- rules currently being tested;
- attributes included in the pilot;
- preliminary rule-pass results;
- possible denominator and grain issues;
- differences between business-rule intent and technical-rule implementation; and
- questions that must be resolved before outputs are used as governed measures.

This page does not approve the dashboard metrics, business rules or technical implementation.

## Source description

The pilot is presented through the Power BI Report Server under:

`Data Platform and Governance → Data Quality Pilot - Customer`

The screenshots reviewed include:

1. `Data Quality: Full Records`;
2. `Data Quality: All Attributes`; and
3. the rule inventory view.

The dashboard identifies the customer source tables as:

- `vwaccount`;
- `vwcontact`.

The underlying analytical logic is understood to originate from the Databricks data-quality pilot.

## Privacy and source boundary

The screenshots and underlying customer-level records must remain in approved organisational systems.

Do not copy into GitHub:

- customer records;
- email addresses;
- telephone numbers;
- ABNs or ACNs;
- record identifiers;
- failed-record extracts;
- screenshots containing sensitive operational data; or
- other identifiable source-system information.

This repository stores only:

- summaries;
- observed aggregate results;
- rule names;
- interpretation;
- caveats;
- refinement questions; and
- decision logic.

## Dashboard-level observations

### Full Records view

The dashboard displayed:

| Measure | Reported result |
|---|---:|
| Total records passed | 8,562,223 |
| Total records tested | 8,929,330 |
| Percent records passed | 95.89% |
| Complete records | 99.9% |
| Valid records | 94.1% |
| Unique records | 95.2% |

Timeliness, accuracy and consistency were labelled as not included in the report.

### All Attributes view

The dashboard displayed:

| Measure | Reported result |
|---|---:|
| Date tested | 19 June 2026 |
| Total records tested | 8,521,688 |
| Overall data quality | 95.9% |
| Completeness | 99.9% |
| Validity | 94.1% |
| Uniqueness | 95.2% |

Timeliness was blank.

Accuracy and consistency were labelled as not included in the report.

## Page-total discrepancy

The two dashboard views showed different totals:

| View | Total records tested |
|---|---:|
| Full Records | 8,929,330 |
| All Attributes | 8,521,688 |
| Difference | 407,642 |

This difference must be explained before either figure is used in reporting.

Possible causes requiring validation include:

- different filters;
- different rule populations;
- different treatment of excluded records;
- different refresh timing;
- record-level versus attribute-level calculation;
- different source-table coverage;
- hidden slicers;
- failed or incomplete rule executions; or
- differences in aggregation logic.

## Attribute-level observations

The following results were visible in the dashboard screenshots.

### Completeness

| Attribute | Reported result | Interpretation status |
|---|---:|---|
| Email | 99.78% | Definition required |
| MobilePhone | 100.00% | Definition required |

These results must not yet be interpreted as evidence that customers have usable contact methods.

A completeness rule may only establish that a field contains a value.

It may not establish:

- valid format;
- currency;
- consent;
- ownership;
- usability;
- verification; or
- suitability for a particular communication.

### Validity

| Attribute | Reported result | Interpretation status |
|---|---:|---|
| ACN | 56.59% | Material diagnostic signal |
| ABN | 81.80% | Material diagnostic signal |
| FirstName | 82.81% | Material diagnostic signal |
| MobilePhone | 96.04% | Exploratory |
| Email | 97.72% | Exploratory |
| LastName | 99.64% | Exploratory |
| Email Secondary | 99.72% | Exploratory |

The ACN and ABN results require eligible-population rules before they can be interpreted safely.

For example:

- not every organisation is expected to have an ACN;
- not every organisation may be expected to have an ABN;
- missing values may be included in validity;
- exempt organisation types may be included;
- records may be inactive, historical or unclassifiable; and
- a structurally valid identifier is not necessarily verified as belonging to the organisation.

### Uniqueness

| Attribute | Reported result | Interpretation status |
|---|---:|---|
| Email | 86.02% | Duplicate signal only |
| Name | 89.08% | High false-positive risk |
| ACN | 90.77% | Eligibility and grouping rules required |
| ABN | 95.71% | Eligibility and grouping rules required |
| Account Trading Name | 97.02% | Classification and exception rules required |
| Email Secondary | 99.93% | Duplicate signal only |
| Customer Number | 100.00% | Technical interpretation required |
| Personal Email | 100.00% | Technical interpretation required |

A uniqueness failure is not automatically a confirmed duplicate.

Depending on the attribute, repeated values may indicate:

- duplicate account creation;
- legitimate shared contact information;
- parent, guardian or representative relationships;
- family or household contact arrangements;
- generic organisational details;
- recycled telephone numbers;
- shared business identifiers;
- trading-name reuse;
- historical records;
- test or placeholder values; or
- source-system defects.

## Rule inventory observed

The rule inventory showed the following dimensions and rule types.

### Account attributes

| Dimension | Attribute | Rule type | Source |
|---|---|---|---|
| Uniqueness | `ABN__c` | `is_unique` | `vwaccount` |
| Validity | `ABN__c` | `in_list` | `vwaccount` |
| Validity | `ABN__c` | `is_valid_format` | `vwaccount` |
| Uniqueness | `Account_Trading_Name__c` | `is_unique` | `vwaccount` |
| Uniqueness | `ACN__c` | `is_unique` | `vwaccount` |
| Validity | `ACN__c` | `in_list` | `vwaccount` |
| Validity | `ACN__c` | `is_valid_format` | `vwaccount` |
| Uniqueness | `Customer_Number__c` | `is_unique` | `vwaccount` |
| Uniqueness | `Name` | `is_unique` | `vwaccount` |

### Contact attributes

| Dimension | Attribute | Rule type | Rule detail | Source |
|---|---|---|---|---|
| Completeness | `Email` | `is_complete` |  | `vwcontact` |
| Completeness | `Email` | `is_complete_secondary` |  | `vwcontact` |
| Uniqueness | `Email` | `is_unique` |  | `vwcontact` |
| Validity | `Email` | `is_similar_duplicate` | `0.9` | `vwcontact` |
| Validity | `Email` | `is_similar_duplicate` | `1` | `vwcontact` |
| Validity | `Email` | `is_valid_format` |  | `vwcontact` |
| Uniqueness | `Email_Secondary__c` | `is_unique` |  | `vwcontact` |
| Validity | `Email_Secondary__c` | `is_similar_duplicate` | `0.9` | `vwcontact` |
| Validity | `FirstName` | `is_valid_format` |  | `vwcontact` |
| Validity | `LastName` | `is_valid_format` |  | `vwcontact` |
| Completeness | `MobilePhone` | `is_complete` |  | `vwcontact` |
| Completeness | `MobilePhone` | `is_complete_secondary` |  | `vwcontact` |
| Validity | `MobilePhone` | `is_similar_duplicate` | `0.9` | `vwcontact` |
| Validity | `MobilePhone` | `is_similar_duplicate` | `1` | `vwcontact` |
| Validity | `MobilePhone` | `is_valid_format` |  | `vwcontact` |
| Uniqueness | `Personal_Email__c` | `is_unique` |  | `vwcontact` |
| Validity | `Phone` | `is_similar_duplicate` | `0.9` | `vwcontact` |

The list above reflects what was visible in the dashboard.

It must be validated against the underlying rule configuration before being treated as complete.

## Business-rule refinement implications

The pilot confirms that technical rules have been drafted or executed before all business definitions have been fully resolved.

The pilot should therefore be used to refine each rule across the following fields:

| Refinement field | Question |
|---|---|
| Business question | What decision or operational problem is the rule intended to support? |
| Source | Which governed table and source field does the rule use? |
| Grain | Is the rule evaluated per account, contact, attribute, pair, group or rule execution? |
| Eligible population | Which records should be assessed? |
| Exclusions | Which records must be excluded? |
| Numerator | What exactly counts as a failure? |
| Denominator | Which records were eligible to pass or fail? |
| Rule logic | What technical test is applied? |
| Rule threshold | What does a threshold such as `0.9` or `1` represent? |
| Failure category | Does failure mean missing, malformed, repeated, similar or unverified? |
| Exception | Which legitimate cases should not be treated as defects? |
| Action | What should happen after a failure is detected? |
| Ownership | Who owns the definition, implementation and response? |
| Permitted use | Is the result exploratory, operational, governed or suitable for reporting? |

## Dimension-classification issue

The dashboard places `is_similar_duplicate` rules under the validity dimension.

This classification should be reviewed.

Similarity and duplicate-detection rules are more naturally interpreted as:

- duplicate signals;
- uniqueness diagnostics;
- record-linkage diagnostics; or
- potential-match rules.

Placing them under validity may cause stakeholders to interpret a potential match as an invalid record.

A final taxonomy should distinguish:

- completeness;
- format validity;
- reference validity;
- uniqueness;
- duplicate signals;
- timeliness;
- accuracy;
- consistency; and
- verification.

## Record-count and grain issue

The dashboard uses the term `records tested`, but the displayed total may represent:

- distinct accounts;
- distinct contacts;
- attribute evaluations;
- rule executions;
- record-rule combinations;
- duplicate pairs;
- duplicate groups; or
- a combination of several grains.

This must be confirmed before calculating or presenting an overall pass rate.

A total number of rule executions must not be described as the number of customer records unless the grain supports that interpretation.

## Overall score issue

The overall data-quality score of approximately 95.9% is not currently decision-safe.

The score may be influenced by:

- different eligible populations for each rule;
- repeated testing of the same record across multiple attributes;
- high-volume rules dominating the result;
- missing dimensions;
- unequal rule importance;
- duplicate rules with multiple thresholds;
- different account and contact populations;
- blank-value treatment;
- excluded records; and
- unreconciled page totals.

The overall score should not be used as evidence that customer data is 95.9% accurate or reliable.

## Current interpretation

The pilot demonstrates that:

- customer data-quality rules can be technically executed;
- the initial rule set covers completeness, validity and uniqueness;
- account and contact attributes are both included;
- potentially material quality issues are visible;
- duplicate-related diagnostics are already being tested;
- ABN and ACN rules require stronger business-population definitions;
- rule-level outputs are more useful than the overall score at this stage; and
- business-rule refinement is required before governed use.

The pilot does not yet demonstrate:

- a governed customer data-quality baseline;
- confirmed duplicate volumes;
- organisation-wide account accuracy;
- verified ABN or ACN ownership;
- usable customer contact coverage;
- compatibility between all rule denominators;
- operational readiness to remediate failures; or
- approval for executive reporting.

## Questions for the rule-refinement workshop

### Dashboard and measurement

- What does `records tested` mean?
- Why do the dashboard pages show different tested totals?
- Is the overall score weighted by rule volume?
- Are account and contact rule executions combined?
- How are failed, skipped and not-applicable tests treated?
- Are blank values included in validity and uniqueness denominators?
- What snapshot or activity period was used?
- Were all rules executed at the same time?
- How are rule versions recorded?

### Completeness

- Does `is_complete` mean non-null only?
- What does `is_complete_secondary` test?
- Are blank strings and placeholder values treated as complete?
- Does email completeness require only the email field?
- Does mobile completeness require only the mobile field?
- How should multiple accepted contact methods be combined?
- What legitimate exceptions apply?

### Validity

- What does `in_list` mean for ABN and ACN?
- What does `is_valid_format` test for each attribute?
- Does ABN or ACN validation include checksum logic?
- Are missing values included as invalid?
- Which organisation types are eligible for each identifier rule?
- What name characters are considered valid?
- How are international names and numbers treated?

### Duplicate signals and uniqueness

- Does `is_unique` count records, values, pairs or groups?
- What does `is_similar_duplicate` compare?
- What do thresholds `0.9` and `1` mean?
- Does threshold `1` represent exact matching?
- Are fields normalised before comparison?
- Are comparisons performed within or across objects?
- Are shared family, household or representative contact details excluded?
- How are confirmed and rejected matches recorded?
- How do these rules overlap with Plauti Duplicate Check?

### Operational response

- Who reviews failures?
- Which failures should create an operational queue?
- Which failures should be corrected during the next customer interaction?
- Which failures indicate upstream process defects?
- Which rules should be preventative in Salesforce?
- Which rules should remain diagnostic in Databricks?
- Which rules require human confirmation?
- What capacity exists to act on the outputs?

## Rule-specific use

This evidence should inform refinement of:

- `CAM-DQ-001 — Minimum valid contact method`;
- `CAM-DQ-002 — Exact email duplicate signal`;
- `CAM-DQ-003 — Exact mobile duplicate signal`;
- `CAM-DQ-004 — ABN completeness`;
- `CAM-DQ-005 — ACN completeness`;
- `CAM-DQ-006 — Repeated ABN`;
- `CAM-DQ-007 — Repeated ACN`; and
- future name, trading-name, secondary-contact and format rules.

The dashboard should not replace the rule-level business definition.

## Evidence status

**Evidence available:** Yes.

**Technical execution confirmed:** Partially.

**Business definition confirmed:** No.

**Population and denominator confirmed:** No.

**Operational response confirmed:** No.

**Governed measure approved:** No.

**Slide-safe:** No.

## Permitted use

The dashboard may currently be used to:

- identify rules requiring business refinement;
- prepare refinement workshops;
- test denominator and grain questions;
- compare technical implementation with business intent;
- identify candidate diagnostic priorities;
- improve rule naming and taxonomy; and
- plan validation with technical and operational owners.

It must not currently be used to:

- claim that customer data quality is 95.9%;
- report confirmed duplicate rates;
- compare teams or services;
- establish performance targets;
- assess employee performance;
- prioritise automated record merges;
- make customer-level decisions; or
- present governed executive metrics.

## Related repository pages

- `01-discover/evidence-gaps.md`
- `01-discover/existing-evidence-inventory.md`
- `02-define/crm-data-quality-rule-refinement.md`
- `02-define/crm-data-quality-rule-register.md`
- `02-define/crm-data-quality-rule-refinement-workshop.md`
- `02-define/rules/CAM-DQ-001-minimum-valid-contact-method.md`
- `02-define/rules/CAM-DQ-002-exact-email-duplicate-signal.md`
- `02-define/rules/CAM-DQ-003-exact-mobile-duplicate-signal.md`
- `02-define/rules/CAM-DQ-004-abn-completeness.md`
- `00-project-control/status-and-validation-model.md`
- `00-project-control/risk-register.md`
- `06-decisions/decision-log.md`
