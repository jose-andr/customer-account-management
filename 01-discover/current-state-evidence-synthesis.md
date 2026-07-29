# Current-state evidence synthesis

Status: Draft  
Owner: José Andrade  
Current stage: Discover  
Last updated: 29 July 2026

## Purpose

This page synthesises current-state evidence from:

`jose-andr/cx-current-state-sop-mapping`

It identifies what the existing repository can currently support, what remains unvalidated and what the evidence implies for Customer Account Management transformation.

This page does not reproduce individual SOPs.

The source repository remains authoritative for detailed current-state operational documentation.

## Executive synthesis

The current-state repository establishes a credible operational scope for Customer Data and Systems Support centred on:

- customer record quality;
- duplicate-record identification;
- customer record cleansing;
- manual de-duplication;
- customer data correction;
- progress tracking;
- data-quality and system escalation; and
- basic CRM data-maintenance support.

However, the detailed evidence base is not yet mature enough to describe these activities as fully validated current practice.

The source repository currently labels the Customer Data and Systems Support area as draft current-state discovery. Its actual-practice summary states that the listed work areas still require officer mapping and validation.

The strongest current conclusion is therefore:

> Customer account quality, duplicate management and CRM data-maintenance work are established areas of operational concern, but the detailed process, frequency, ownership, controls, effort and variation still require validation.

## Source relationship

| Repository | Role |
|---|---|
| `jose-andr/cx-current-state-sop-mapping` | Source of current-state operational evidence |
| `jose-andr/customer-account-management` | Transformation framing, design, decisions and learning |

Use the source repository to understand:

- what work happens today;
- how work is triggered;
- which systems are used;
- where decisions occur;
- where exceptions and workarounds occur;
- what remains undocumented;
- what creates operational friction; and
- what may constrain future connected interactions.

Do not copy detailed SOP content into this repository.

## Current source status

The source repository is:

- a discovery and concept-development repository;
- focused on actual practice rather than aspirational role scope;
- not an approved operational policy library;
- not a customer-data store;
- not a final operating model; and
- still subject to officer validation.

The Customer Data and Systems Support folder is marked:

`Draft current-state discovery`

The current actual-practice summary is marked:

`Draft discovery placeholder`

This means that candidate activities, pain points, controls and risks must remain labelled as reported, proposed or awaiting validation.

## Current operational scope

The source repository identifies the following candidate current work areas:

| Work area | Current evidence status | Customer Account Management relevance |
|---|---|---|
| Customer record quality | Pending officer validation | Establishes account quality as an operational concern |
| Duplicate customer record identification | Pending officer validation | Supports investigation of duplicate creation and detection |
| Customer record cleansing | Pending officer validation | Indicates recurring remediation activity |
| Manual de-duplication | Pending officer validation | Suggests human review and judgement may be required |
| Customer data correction | Pending officer validation | Connects data quality to service reliability |
| CRM data-maintenance support | Pending officer validation | Shows dependency on CRM support processes |
| Data-quality or system escalation | Pending officer validation | Indicates exceptions may cross role or system boundaries |
| Cleansing progress tracking | Pending officer validation | Suggests a need for visibility, continuity and measurement |

These work areas are credible discovery inputs.

They are not yet validated SOPs or stable organisation-wide practices.

## Current-state process signals

The repository structure indicates that current work should be examined through:

- triggers;
- inputs;
- process steps;
- decision points;
- systems and tools;
- handovers;
- exceptions;
- workarounds;
- controls;
- pain points;
- risks; and
- connected-interaction implications.

This provides the right evidence model for Customer Account Management transformation.

The current synthesis should therefore avoid treating duplicate management as only a data-cleaning task.

It should be understood as a service and operating-system problem involving:

- upstream account creation;
- customer identification;
- record comparison;
- staff judgement;
- correction authority;
- privacy and sensitivity;
- system capability;
- escalation;
- progress visibility; and
- recurring root causes.

## Reported pain-point signals

The source repository records the following candidate pain points.

All remain subject to validation.

| ID | Reported pain-point signal | Possible impact | Status |
|---|---|---|---|
| P-001 | Duplicate records may require manual review | Staff effort and fragmented customer context | To validate |
| P-002 | Duplicate-confirmation criteria may not be fully documented | Inconsistent decisions and escalation | To validate |
| P-003 | Records may contain missing or conflicting information | Delay, rework and uncertainty | To validate |
| P-004 | Corrections may depend on officer judgement | Variation and individual knowledge dependency | To validate |
| P-005 | System constraints may create manual workarounds | Effort and traceability risk | To validate |
| P-006 | Cleansing progress may be tracked outside the system of record | Visibility and continuity risk | To validate |
| P-007 | Formal role expectations may not reflect actual practice | Ownership and capability misunderstanding | To validate |
| P-008 | Upstream processes or channels may continue creating duplicates | Recurring quality problems despite remediation | To validate |

## Reported risk signals

The source repository records the following candidate risks.

Likelihood, control reliability and occurrence have not yet been assessed.

| ID | Reported risk signal | Potential impact | Status |
|---|---|---|---|
| R-001 | Two different customers could be incorrectly merged | Data integrity, privacy and customer harm | To validate |
| R-002 | True duplicates could remain unresolved | Fragmented records and inconsistent context | To validate |
| R-003 | Incorrect information could be retained or corrected incorrectly | Service, reporting and data-quality impact | To validate |
| R-004 | Sensitive information could be linked incorrectly | Privacy and information-handling risk | To validate |
| R-005 | Completed cleansing work may not be traceable | Weak auditability and continuity | To validate |
| R-006 | Work may depend on undocumented individual knowledge | Operational continuity risk | To validate |
| R-007 | System access or constraints may prevent correction | Unresolved defects and manual escalation | To validate |
| R-008 | Stakeholders may assume broader reporting capability exists | Misaligned expectations and ownership | To validate |

## Current control signals

The source material suggests that current work may involve controls such as:

- comparing records before deciding they are duplicates;
- checking whether sufficient information exists before correction;
- escalating uncertain or sensitive cases;
- recording completion in a tracker or note;
- applying privacy or sensitivity checks; and
- using human judgement where automated certainty is insufficient.

These are control signals only.

They must not be described as established controls until the officer confirms:

- whether the control occurs;
- when it occurs;
- who performs it;
- what evidence is retained;
- how exceptions are managed; and
- whether the control is reliable.

## Ownership and knowledge signals

The current-state material indicates several possible operating-model issues:

- work may depend on one officer’s knowledge;
- duplicate criteria may not be fully documented;
- correction decisions may require judgement;
- escalation responsibilities may be unclear;
- stakeholder expectations may exceed actual role capacity;
- progress visibility may rely on separate trackers; and
- ownership of recurring upstream causes may sit outside the operational role.

These signals suggest that future transformation should examine both:

1. how account-quality work is performed; and
2. who owns prevention, resolution, standards, controls and improvement.

## Root-cause signal

The source repository explicitly identifies the possibility that upstream processes or channels create duplicate records.

This is an important transformation signal.

It means that success should not be defined only as:

- finding more duplicates;
- merging more records; or
- completing more cleansing activity.

A stronger transformation outcome would reduce the creation and recurrence of account-quality issues at source.

Potential root-cause areas to investigate include:

- account-creation journeys;
- staff-assisted account creation;
- inconsistent matching rules;
- mandatory-field design;
- identity-verification practices;
- system integrations;
- service-specific account structures;
- classification rules;
- customer-detail update processes; and
- unclear ownership between systems and services.

These are investigation areas, not confirmed causes.

## Connected-interaction implications

The current-state evidence suggests the following implications for future connected customer interactions:

| Current-state signal | Transformation implication |
|---|---|
| Duplicate records require review | Customer identity quality must be sufficient to carry context across services |
| Matching criteria may be undocumented | Matching rules require explicit governance and human-review thresholds |
| Information may be missing or conflicting | Account-creation and update pathways may require stronger validation |
| Corrections may depend on judgement | Automation must preserve appropriate human decision points |
| Workarounds may sit outside systems | Future workflows need traceability and visible status |
| Work may depend on individual knowledge | Processes, ownership and escalation need to be maintainable |
| Upstream channels may create duplicates | Prevention must be designed into service and system entry points |
| Role expectations may exceed current capacity | Future capability must distinguish current resources from desired ownership |

## What the source currently supports

The available evidence is sufficient to support the following working conclusions:

### Supported with caveats

- Customer account quality is a relevant operational and transformation concern.
- Duplicate identification and remediation are legitimate discovery areas.
- Manual judgement may be an important part of current work.
- Privacy and data-integrity risk must be considered in duplicate resolution.
- Current system or process constraints may produce workarounds.
- Upstream causes should be investigated rather than assuming cleansing is the full solution.
- Operational practice must be validated before becoming future requirements.

### Not yet supported

The source does not yet safely support claims that:

- all listed activities occur regularly;
- duplicate volumes are materially increasing;
- duplicate management consumes a known amount of staff time;
- controls operate consistently;
- current controls are effective;
- the organisation needs a single master customer record;
- automation is ready or safe;
- a particular team should own Customer Account Management;
- specific CRM changes are required; or
- the listed pain points apply across the organisation.

## Evidence gaps

The following current-state evidence is still required:

### Actual practice

- the top recurring activities;
- triggers and demand sources;
- frequency and volume;
- actual process steps;
- systems and tools;
- decision criteria;
- handovers;
- exception pathways;
- workarounds; and
- completion-recording practices.

### Ownership

- who requests work;
- who approves corrections;
- who decides records are duplicates;
- who manages uncertain cases;
- who owns upstream causes;
- who owns quality standards;
- who receives escalations; and
- who is accountable for improvement.

### Measures

- duplicate records identified;
- duplicates confirmed;
- records corrected;
- records not safely resolvable;
- time per activity;
- backlog and ageing;
- repeat defects;
- source channel or process;
- control failures; and
- customer or service impact.

### Controls

- matching criteria;
- evidence requirements;
- privacy checks;
- sensitive-case handling;
- audit records;
- quality assurance;
- access controls;
- escalation thresholds; and
- reversal or recovery processes.

## Decision implications

The current evidence supports continued Discover and Define work.

It does not yet support selecting a future-state solution.

The next decisions should focus on:

1. which current activities require officer validation first;
2. which pain points most affect customers, staff or risk;
3. which upstream pathways create the greatest recurrence;
4. which account-quality measures are available and governed;
5. which ownership questions block improvement; and
6. what evidence is required before moving into Design.

## Transformation principle

Customer Account Management should address both:

- **remediation** — identifying, correcting and resolving existing account-quality issues; and
- **prevention** — changing upstream practices, rules and systems so avoidable issues are less likely to recur.

Do not optimise remediation activity without investigating why the defects continue to be created.

## Current conclusion

The current-state SOP repository provides a sound discovery structure and a credible set of operational hypotheses.

It does not yet provide a fully validated operational baseline.

The Customer Account Management workstream should therefore use it as:

- a source of candidate practices;
- a source of pain-point and risk hypotheses;
- a guide for officer validation;
- a framework for gathering operational evidence; and
- an input into problem definition.

It should not yet use it as:

- approved policy;
- complete process truth;
- proof of organisation-wide impact;
- a validated control framework; or
- a future-state requirements specification.

## Next action

Validate the highest-priority current-state activity:

`Identify duplicate customer records`

The validation should confirm:

- trigger;
- frequency;
- input information;
- systems used;
- matching criteria;
- decision points;
- escalation thresholds;
- privacy or sensitivity checks;
- completion record;
- recurring pain points;
- upstream source; and
- evidence suitable for baseline measurement.
