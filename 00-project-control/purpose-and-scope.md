# Purpose and scope

Status: Aligned draft  
Owner: José Andrade  
Current stage: Discover → Define  
Last updated: 29 July 2026

## Purpose

Customer Account Management is a transformation workstream focused on improving how customer accounts and customer information support reliable, connected and lower-effort customer interactions.

The workstream provides a structured way to:

- understand current account-management problems;
- connect customer, employee, operational and system evidence;
- align stakeholders around a shared problem definition;
- identify transformation opportunities;
- design and test future approaches;
- document decisions and their rationale;
- evaluate whether changes improve outcomes; and
- retain reusable learning for future iterations.

The repository supports decision-making and transformation activity.

It is not an operational system of record, customer-data repository, approved policy library or replacement for organisational delivery tools.

## Initial objective

The initial objective is to establish a practical 4D Human-Centred Design structure for the workstream:

1. Discover
2. Define
3. Design
4. Deliver

The structure will be used to document existing activity, preserve evidence, identify gaps and support iterative transformational change.

The immediate focus is to:

- record the discovery work already completed;
- distinguish aligned outputs from unvalidated ambition;
- preserve the aligned draft problem definition;
- connect the work to current-state operational evidence;
- identify missing discovery and definition activity; and
- create a traceable basis for future design and delivery decisions.

## Current position

The original discovery activity included broad ambitions covering:

- problem alignment;
- customer use cases and pain points;
- employee use cases and pain points;
- current-state account-management practices;
- organisational and system context;
- business impacts;
- good-practice research;
- success measures;
- future outcomes; and
- a roadmap for improvement.

Not all intended discovery outcomes were completed.

The most dependable output currently available is an aligned draft problem definition developed between:

- the Customer Focus and Strategy Manager;
- the CRM Product Owner; and
- the Customer Data and Systems Support Officer.

Other workshop outputs, proposed solutions, success measures and future-state ideas remain discovery evidence, assumptions or future signals until separately validated.

## Working problem area

The current problem area includes evidence that:

- customer records may be duplicated or inconsistent;
- staff may not be able to confidently identify the correct customer record;
- the current account model may not reflect the full customer relationship;
- fragmented customer information can increase manual effort;
- customers may need to repeat information;
- inconsistent account practices can affect service confidence;
- ownership and governance responsibilities may be unclear; and
- transformation initiatives may be constrained by weak customer-information foundations.

These are working problem signals.

They must not be treated as confirmed organisation-wide findings unless supported by evidence and appropriate validation.

## In scope

The initial workstream includes:

### Customer account experience

- account creation;
- customer identification;
- account access;
- contact-detail maintenance;
- duplicate-account prevention and resolution;
- customer relationship representation;
- account-linked service interactions;
- account continuity across services; and
- customer trust in account information.

### Employee experience

- finding and identifying customer records;
- assessing record reliability;
- updating customer information;
- resolving duplicate or inconsistent records;
- understanding account ownership;
- managing exceptions and workarounds;
- supporting customer enquiries; and
- using account information during service delivery.

### Operational practices

- current customer-account processes;
- account lifecycle events;
- account-quality routines;
- manual correction and cleansing activity;
- ownership and escalation pathways;
- business rules;
- exception handling;
- controls;
- handovers; and
- recurring operational pain points.

### Systems and information

- CRM customer-account structures;
- customer identifiers;
- systems that create or update customer information;
- system dependencies;
- integration-related account issues;
- customer-data quality rules;
- relevant field definitions;
- account classification;
- relationship models; and
- minimum information required for connected interactions.

### Governance and transformation

- roles and responsibilities;
- decision rights;
- ownership models;
- account-management standards;
- privacy, records, security and data-governance dependencies;
- future operating-model options;
- transformation priorities;
- success measures;
- pilots and experiments; and
- evaluation and learning.

## Out of scope

The initial workstream does not include:

- storing raw customer or account data in GitHub;
- replacing CRM, Databricks, Power BI, SharePoint, Jira or other organisational systems of record;
- redesigning every customer-facing service;
- defining a complete enterprise customer-data strategy;
- selecting or procuring technology without validated requirements;
- creating organisation-wide policy without authorised governance;
- assuming a master customer identifier is the required solution;
- treating proposed governance arrangements as approved;
- documenting identifiable customer cases;
- duplicating current-state SOP documentation; or
- committing to implementation before the problem, scope and evidence are sufficiently defined.

## Adjacent areas

The following areas are related but broader than the initial Customer Account Management scope:

- customer data management across known and anonymous interactions;
- customer analytics and segmentation;
- personalisation;
- channel strategy;
- connected customer interactions;
- service information architecture;
- knowledge management;
- digital identity;
- master data management;
- enterprise data governance;
- consent and preference management;
- customer communications; and
- artificial intelligence using customer information.

These areas may become dependencies, evidence sources or future transformation streams.

They should not be absorbed into this repository unless repeated work demonstrates a genuine need.

## Relationship to current-state SOP mapping

The repository:

`jose-andr/cx-current-state-sop-mapping`

is an input to this workstream.

It documents actual current Customer Data and Systems Support operational practices, including:

- duplicate management;
- record correction;
- systems and tools;
- operational decisions;
- exception pathways;
- manual workarounds;
- pain points; and
- current controls.

This repository must reference that evidence rather than reproduce it.

### Repository boundary

| Repository | Purpose |
|---|---|
| `cx-current-state-sop-mapping` | Document actual current operational practice |
| `customer-account-management` | Use evidence to frame, design, test and evaluate transformational change |

## Intended outcomes

The workstream aims to support:

### Customer outcomes

- less repetition;
- clearer account interactions;
- more reliable customer information;
- fewer avoidable account problems;
- improved continuity across services; and
- increased confidence that customer information is handled appropriately.

### Employee outcomes

- greater confidence in customer records;
- reduced manual reconciliation;
- clearer ownership and escalation;
- fewer recurring workarounds;
- more consistent account-management practices; and
- better support for resolving customer needs.

### Operational outcomes

- reduced duplicate creation;
- improved account quality;
- clearer account lifecycle practices;
- more consistent data capture and update rules;
- visible ownership and controls;
- improved root-cause analysis; and
- stronger readiness for connected interactions.

### Organisational outcomes

- better evidence for investment and prioritisation;
- reduced transformation risk;
- clearer decision-making;
- reusable account-management standards;
- stronger customer-information foundations; and
- improved alignment between customer experience, CRM, data and service delivery.

## Success conditions

The workstream will be considered ready to move from Define into Design when:

- the problem statement has been reviewed and validated at the required level;
- customer and employee impacts are supported by sufficient evidence;
- current-state operational evidence has been synthesised;
- scope and exclusions are clear;
- key assumptions are visible;
- ownership and stakeholder roles are understood;
- outcome measures are defined safely;
- priority opportunities are agreed; and
- the next design decisions are explicit.

## Evidence and status rules

Repository content must distinguish:

- Evidence
- Reported practice
- Validated practice
- Assumption
- Interpretation
- Future signal
- Recommendation
- Decision
- Action
- Outcome

An aligned draft is suitable for continued work.

It is not the same as formal endorsement, approved policy or validated organisation-wide evidence.

## Privacy and information boundaries

Do not store:

- customer names;
- contact details;
- account identifiers;
- identifiable case information;
- raw CRM exports;
- raw organisational datasets;
- credentials;
- sensitive screenshots; or
- controlled operational records.

Store only:

- de-identified summaries;
- synthetic examples;
- aggregated findings;
- source references;
- field and system names where safe;
- process descriptions;
- caveats;
- decisions;
- reusable patterns; and
- transformation learning.

## Next action

Record the aligned draft problem statement and separate:

- validated wording;
- supporting evidence;
- assumptions;
- unresolved scope questions; and
- proposed solutions that must remain outside the problem definition.
