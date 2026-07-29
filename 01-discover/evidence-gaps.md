# Evidence gaps

Status: Draft  
Owner: José Andrade  
Current stage: Discover  
Last updated: 29 July 2026

## Purpose

Track the evidence, unresolved questions and validation activity required before Customer Account Management can move confidently from Define into Design.

This page helps the workstream:

- distinguish evidence from assumptions;
- identify decision-critical gaps;
- avoid premature solution design;
- connect operational discovery with CRM data-quality analysis;
- clarify who needs to validate each issue;
- make evidence limitations visible; and
- stop discovery when the next decision can be made safely.

## Current position

The workstream has enough evidence to support an aligned draft problem statement.

It does not yet have enough validated evidence to:

- confirm the scale of customer account quality problems;
- identify the highest-impact customer and employee use cases;
- establish the main root causes;
- confirm current ownership and controls;
- define safe baseline measures;
- prioritise transformational interventions; or
- select a technology, governance or operating-model response.

The immediate need is targeted validation rather than broad additional discovery.

## Evidence principles

Evidence collection should follow these rules:

1. Collect evidence only where it supports a decision.
2. Prioritise actual practice over intended process.
3. Separate customer, employee, operational, system and governance evidence.
4. Use governed sources for quantitative measures.
5. Preserve uncertainty where evidence is incomplete.
6. Do not retain raw customer or organisational data in this repository.
7. Record proposed solutions separately from problem evidence.
8. Stop discovery when the next decision can be made safely.

## Databricks CRM data-quality work in progress

CRM data-quality rules are currently being developed for checking Salesforce data through Databricks.

This work may provide:

- repeatable CRM account-quality checks;
- governed business-rule definitions;
- scheduled rule execution;
- trendable results;
- evidence of recurring data-quality issues;
- initial account-quality baselines; and
- evidence for prioritising process, system or governance improvements.

The work is still in progress.

It must not yet be treated as:

- a complete CRM data-quality framework;
- a validated Customer Account Management baseline;
- proof of customer impact;
- proof of root cause;
- an approved duplicate-management standard;
- a complete inventory of CRM quality rules; or
- a production reporting capability unless implementation, scheduling and ownership are confirmed.

## Current CRM rule-definition structure

The current rule inventory records:

| Field | Purpose |
|---|---|
| Source | Source system or Databricks data domain |
| Dataset | Table or view containing the measured attribute |
| Attribute | Field or field combination being checked |
| Business description | Plain-English statement of the rule |
| Technical logic | Query, filter, format or comparison used |
| Frequency | Expected execution schedule |
| Contact | Person who supplied the rule |
| Priority | Relative importance |
| Active | Whether the rule is currently enabled |
| Rule ID | Identifier used to track the rule |

The default proposed execution frequency is weekly unless another frequency is agreed.

## Current CRM rule themes

### Person-account completeness

Current checks include:

- person accounts without a primary email;
- secondary email populated while primary email is blank;
- person accounts without a primary mobile;
- secondary phone populated while primary mobile is blank; and
- missing minimum contact information.

### Person-account validity

Current checks include:

- mobile-number length;
- unexpected characters in first or last name;
- future birth dates; and
- incomplete address information.

### Potential person-account duplicates

Current checks use combinations of:

- exact email;
- secondary email;
- exact mobile;
- phone;
- exact name; and
- greater than 90% name similarity.

These results identify potential duplicates only.

They do not confirm that two records relate to the same customer.

### Organisation-account completeness and validity

Current checks include:

- missing ABN;
- missing ACN;
- ABN length;
- proposed ACN length;
- proposed ACN-to-ABN consistency; and
- possible future validation against an authoritative external source.

### Potential organisation duplicates

Current checks include repeated:

- ABN;
- ACN;
- organisation name; and
- trading name.

## Current rule maturity

The rule inventory contains a mixture of:

- active rules;
- proposed rules;
- parked rules;
- incomplete technical logic;
- unresolved field questions;
- rules requiring multiple-field comparison;
- rules requiring external verification;
- business questions not yet converted into complete rules; and
- existing Salesforce validation rules.

Each rule must record both:

1. **Definition status** — whether the business rule is agreed.
2. **Execution status** — whether it is implemented, scheduled and producing reviewed results.

Recommended statuses:

| Status | Meaning |
|---|---|
| Proposed | Business question or possible rule only |
| Definition in progress | Business intent exists but logic, ownership or scope is incomplete |
| Ready for implementation | Business rule, population, grain, filters and expected result are agreed |
| Implemented | Logic has been created in Databricks |
| Scheduled | Rule runs at an agreed frequency |
| Results under review | Results exist but are not yet accepted as governed measures |
| Validated | Rule and results are approved for the stated decision use |
| Parked | Not currently progressing due to a dependency or design issue |
| Retired | No longer required or replaced |

## Next business task: refine the CRM rules

The business must refine the current CRM data-quality rules before Databricks outputs are treated as governed measures.

For each rule, confirm:

- the business question;
- the customer or account population;
- the record grain;
- the fields used;
- the failure condition;
- valid exceptions;
- exclusions;
- numerator;
- denominator where required;
- output unit;
- execution frequency;
- business owner;
- operational action owner;
- technical owner;
- required action when the rule fails;
- caveats;
- privacy or governance implications; and
- whether the rule is ready for implementation.

## Initial rule-refinement priorities

Refine the rules in this order:

1. minimum contact information for active person accounts;
2. exact email duplicate signals;
3. exact mobile duplicate signals;
4. ABN and ACN completeness;
5. ABN and ACN duplicate signals;
6. person-account fuzzy-name matching;
7. organisation-name and trading-name matching;
8. external ABN and ACN verification;
9. remaining format and cross-field consistency rules.

This sequence starts with rules that are easier to explain and test before moving into higher-risk fuzzy matching and external verification.

## Rule-refinement questions

### Person-account contact completeness

Confirm:

- Is an email required for every active person account?
- Is a mobile number required for every active person account?
- Is one valid contact method sufficient?
- What approved exceptions apply?
- Should secondary values be promoted to primary?
- Are inactive accounts included?
- What customer or service impact follows from missing details?

### Person-account field validity

Confirm:

- Are international mobile numbers permitted?
- Which characters are valid in customer names?
- How should hyphens, apostrophes, spaces and diacritics be handled?
- Is address completeness required for every account?
- Which Salesforce validation rules already prevent defects?
- Are historical records expected to comply?

### Potential person-account duplicates

Confirm:

- Is the output measured as records, pairs or duplicate groups?
- Which fields provide enough confidence to create a potential match?
- Is 90% name similarity appropriate?
- How are common names handled?
- How are shared email addresses and phone numbers handled?
- How are families, carers and representatives handled?
- Which matches require human review?
- What makes a duplicate confirmed rather than potential?
- Should each matching scenario have a separate rule ID?

### Organisation-account rules

Confirm:

- Which organisation types require an ABN?
- Which require an ACN?
- Can an organisation legitimately have one but not the other?
- Are inactive organisations included?
- Does a repeated ABN always mean duplicate accounts?
- Can one legal entity have multiple valid account records?
- Can different entities share a trading name?
- How should branches, subsidiaries and departments be represented?
- Which external source is authoritative?
- Is external verification technically and legally approved?

## Metric-safety requirements

A rule result is not automatically a safe business metric.

Before a Databricks result is used for decision-making, record:

- business question;
- rule ID;
- source schema;
- dataset or view;
- attribute or attribute combination;
- record grain;
- population filter;
- numerator;
- denominator;
- exclusions;
- execution date;
- reporting period;
- rule version;
- result;
- known limitations;
- validation owner; and
- permitted decision use.

Potential duplicate matches must not be described as confirmed duplicates.

A count of flagged records must not be mixed with a count of duplicate groups.

Rules using different populations, fields or matching thresholds must not be combined without explicit caveats.

## Priority evidence gaps

| ID | Evidence gap | Why it matters | Current confidence | Priority |
|---|---|---|---|---|
| GAP-001 | Actual duplicate-identification and resolution process | Establishes current practice, effort, controls and failure points | Low | Critical |
| GAP-002 | Business refinement of CRM data-quality rules | Ensures Databricks logic reflects agreed business meaning | In progress | Critical |
| GAP-003 | Databricks CRM rule implementation and governed results | Confirms whether repeatable quality measures and baselines are available | In progress | Critical |
| GAP-004 | Duplicate volume and creation rate | Confirms scale and provides a baseline | Low | Critical |
| GAP-005 | Main sources and causes of duplicate creation | Supports prevention rather than remediation only | Low | Critical |
| GAP-006 | Customer impact by journey or service | Identifies where account problems create the greatest customer effort or harm | Low | High |
| GAP-007 | Employee effort and operational demand | Supports prioritisation and investment decisions | Low | High |
| GAP-008 | Current ownership and decision rights | Identifies accountability gaps and governance needs | Low | High |
| GAP-009 | Account classifications and relationship needs | Tests whether current structures reflect people, organisations and representatives | Low | High |
| GAP-010 | Existing matching rules and controls | Determines whether duplicate decisions are consistent and safe | Partially documented | High |
| GAP-011 | Privacy, records, security and data-governance constraints | Prevents unsafe future-state design | Low | High |
| GAP-012 | Account-quality impact on self-service and connected interactions | Connects operational quality to transformation outcomes | Low | Medium |
| GAP-013 | Current reporting and metric definitions | Determines which outputs are governed and denominator-safe | In progress | Medium |
| GAP-014 | Readiness of systems and integrations | Identifies technical constraints without assuming a solution | Low | Medium |

## Other critical validation questions

### Actual duplicate process

Confirm:

- what triggers duplicate investigation;
- who performs the work;
- how often it occurs;
- what information is reviewed;
- which systems are used;
- how a duplicate is confirmed;
- when records can be merged or corrected;
- when escalation is required;
- what privacy or sensitivity checks apply;
- how completion is recorded;
- what exceptions occur; and
- which steps depend on individual knowledge.

### Duplicate volume and creation rate

Confirm:

- potential duplicates identified;
- duplicates confirmed;
- records resolved;
- records left unresolved;
- backlog and ageing;
- duplicates created by period;
- duplicate rate relative to eligible new accounts;
- recurring defects;
- source dataset;
- record grain; and
- rule version.

Potential duplicates and confirmed duplicates must remain separate measures.

### Root causes

Investigate whether defects originate from:

- customer self-service account creation;
- staff-assisted account creation;
- CRM processes;
- service-specific workflows;
- external systems;
- integrations;
- inconsistent matching rules;
- missing or optional fields;
- inconsistent classifications;
- customer-detail changes;
- organisation-account creation;
- representative or family relationships; or
- historical migration.

### Customer impact

Validate whether account problems contribute to:

- repeated information requests;
- failed account access;
- incorrect communications;
- delayed service;
- fragmented histories;
- incorrect relationship links;
- difficulty updating details;
- inability to track requests or applications;
- repeat contact; or
- reduced trust.

### Employee impact

Confirm:

- staff roles affected;
- volume of work;
- search and validation effort;
- correction and merge effort;
- escalations;
- workarounds;
- repeat handling;
- dependency on individual expertise; and
- impact on service resolution.

### Ownership and decision rights

Confirm who owns:

- customer identity definitions;
- account-creation rules;
- matching criteria;
- duplicate prevention;
- duplicate resolution;
- customer-information standards;
- field definitions;
- account classifications;
- system configuration;
- quality monitoring;
- privacy decisions;
- escalation;
- root-cause correction; and
- transformation prioritisation.

## Initial validation activities

| Activity | Evidence produced | Suggested participants | Priority |
|---|---|---|---|
| CRM data-quality rule-refinement session | Agreed rule definitions, populations, ownership and implementation readiness | Customer Focus and Strategy, CRM Product Owner, Customer Data and Systems Support, Databricks or Data Governance support | Critical |
| Duplicate-record process walkthrough | Actual process, systems, decisions, controls and workarounds | Customer Data and Systems Support Officer | Critical |
| Databricks rule and metric review | Rule status, source, grain, numerator, denominator, outputs and caveats | Databricks or Data Governance support, CRM Product Owner | Critical |
| Duplicate root-cause review | Main creation pathways and recurring causes | CRM Product Owner, operational officer, service owners | Critical |
| Customer-impact evidence review | Priority journeys and de-identified examples | Customer Experience, service owners, frontline teams | High |
| Ownership mapping workshop | Roles, decision rights, gaps and escalation pathways | Manager, CRM Product Owner, governance partners | High |
| Governance constraint review | Privacy, records, security and data requirements | Relevant governance specialists | High |

## Evidence records required

Each activity should produce a safe evidence record containing:

- evidence ID;
- question;
- source;
- collection date;
- participant role;
- summary;
- finding;
- validation status;
- caveat;
- implication;
- related decision; and
- authorised source location.

Use:

`07-templates/evidence-record-template.md`

Do not include identifiable customer information or sensitive operational extracts.

## Evidence-gap backlog

| ID | Next action | Owner | Status |
|---|---|---|---|
| GAP-001 | Complete a walkthrough of duplicate identification and resolution | To assign | Open |
| GAP-002 | Run the first CRM data-quality rule-refinement session | José Andrade | In progress |
| GAP-003 | Confirm which rules are implemented, scheduled or producing results in Databricks | To assign | Open |
| GAP-004 | Confirm available duplicate-account measures and definitions | To assign | Open |
| GAP-005 | Identify the top pathways creating duplicate accounts | To assign | Open |
| GAP-006 | Select three priority customer account use cases | To assign | Open |
| GAP-007 | Estimate operational effort using available evidence | To assign | Open |
| GAP-008 | Map current ownership and escalation responsibilities | To assign | Open |
| GAP-009 | Validate priority account and relationship needs | To assign | Open |
| GAP-010 | Document current matching and correction controls | To assign | Open |
| GAP-011 | Complete governance constraint review | To assign | Open |
| GAP-012 | Test the relationship between account quality and self-service outcomes | To assign | Open |
| GAP-013 | Create a governed CRM metric-definition inventory | To assign | Open |
| GAP-014 | Map systems that create, update or consume customer accounts | To assign | Open |

## Stop conditions for discovery

Discovery should stop expanding when:

- the working problem is sufficiently supported;
- the highest-impact use cases are clear;
- material causes and constraints are understood;
- critical ownership gaps are visible;
- CRM data-quality rules have agreed business definitions;
- safe baseline measures are available;
- major governance risks are known;
- priority opportunities can be compared; and
- the next design decision is explicit.

Lower-priority evidence gaps may remain open where they do not prevent the next decision.

## Current decision

The next business activity is to refine the CRM data-quality rules before treating Databricks outputs as governed evidence.

The first refinement session should focus on:

1. minimum valid contact information for active person accounts;
2. exact email duplicate signals;
3. exact mobile duplicate signals;
4. ABN and ACN completeness requirements;
5. ABN and ACN duplicate signals; and
6. the distinction between potential and confirmed duplicates.

## Next action

Prepare the first CRM data-quality rule-refinement session and complete the business definition for the initial priority rules before requesting further Databricks implementation.
