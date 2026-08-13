# Success measures

Status: Draft
Owner: José Andrade
Last updated: 13 August 2026

## Purpose

Define how City of Melbourne could evidence whether Customer Account Management improvements are creating meaningful value.

These measures support:

* viability assessment;
* prioritisation;
* controlled testing;
* future business-case development; and
* evaluation of delivered improvements.

This page does not establish approved KPIs or targets.

Measures should only become governed when their:

* business question;
* source;
* population;
* grain;
* numerator;
* denominator;
* exclusions;
* ownership; and
* permitted use

have been agreed.

## North star

> Assess the viability of improvements to Customer Account Management and potential future investment at City of Melbourne, using evidence to support prioritisation and business-case decisions.

## Measurement question

> What evidence would show that a Customer Account Management improvement is valuable enough, viable enough and sufficiently effective to justify further investment or scaling?

## Measurement principles

### 1. Measure outcomes, not activity

Do not treat completion of workshops, documentation or configuration changes as evidence that Customer Account Management improved.

### 2. Link every measure to a decision

A measure should help answer a decision question such as:

* Is the problem material?
* Is an intervention working?
* Should this opportunity progress?
* Is further investment justified?
* Should the approach scale?
* Should the initiative stop?

### 3. Keep grain explicit

Measures based on CRM records must not automatically be described as customer measures.

For example:

> Person Account records failing a rule

is not equivalent to:

> Customers affected.

### 4. Protect denominator integrity

Do not publish percentages unless the eligible population and denominator are explicit and compatible with the numerator.

### 5. Separate diagnostics from governed measures

Exploratory Databricks outputs may support discovery and prioritisation before they are suitable for executive reporting.

### 6. Use caveats visibly

A technically calculated result may still be unsafe for decision-making if:

* the source is incomplete;
* the population is unclear;
* the grain is incompatible;
* exceptions are unresolved;
* the rule is unvalidated; or
* the measure cannot be repeated reliably.

## Outcome-to-measure model

| Outcome area         | What should become better                                               | Possible evidence                                                                              |
| -------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Customer             | More accurate, appropriate and consistent customer-account interactions | Incorrect account-linking incidents, inappropriate communications, validated customer examples |
| Operational          | Less avoidable investigation, rework and manual remediation             | Remediation volumes, handling effort, queue size, repeat support demand                        |
| Risk and governance  | Clearer and more effective customer-data controls                       | Control failures, exceptions, unresolved ownership, incident or audit evidence                 |
| Strategic capability | More reusable and sustainable Customer Account Management capability    | Common standards, adoption, repeatability, cross-service reuse, sustained quality improvement  |

## Measurement maturity

Measures should progress through the following maturity levels.

### Level 1 — Signal

A reported example or diagnostic indicates that a problem may exist.

Suitable for:

* discovery;
* hypothesis formation; and
* prioritisation discussions.

Not suitable for:

* targets;
* performance comparison; or
* investment claims.

### Level 2 — Baseline

The population, source, grain and calculation are sufficiently clear to establish the current state.

Suitable for:

* sizing the problem;
* comparing future change; and
* viability assessment.

### Level 3 — Controlled test measure

A defined intervention can be compared against an agreed baseline or control condition.

Suitable for:

* experiments;
* pilots; and
* Design / Deliver decisions.

### Level 4 — Governed measure

The measure has agreed ownership, definition, quality controls and reporting use.

Suitable for:

* ongoing operational reporting;
* governance;
* targets where appropriate; and
* investment monitoring.

### Level 5 — Outcome measure

Evidence demonstrates sustained customer, operational, risk or strategic improvement.

Suitable for:

* benefits realisation;
* scaling decisions; and
* business-case evaluation.

## Initial success-measure framework

### Customer identity and account linking

#### Decision question

Is customer information being linked to the correct account relationship with sufficient confidence?

#### Possible measures

| Measure                                                     | Intended use                        | Current status       |
| ----------------------------------------------------------- | ----------------------------------- | -------------------- |
| Reported incorrect Service Account linking cases            | Identify problem signals            | Reported evidence    |
| Confirmed incorrect-linking cases after review              | Establish validated impact          | Not yet defined      |
| Incorrect-linking rate within an eligible tested population | Establish scale                     | Not yet safe         |
| Repeat linking corrections                                  | Identify recurring failure          | Not yet defined      |
| Customer-impact examples                                    | Understand consequence and severity | Qualitative evidence |

#### Key caveat

Do not use raw case counts as a rate unless the eligible Service Account linking population is known.

## Duplicate prevention and resolution

#### Decision questions

* How much duplicate creation is occurring?
* Where are duplicates being created?
* How much operational effort is used to resolve them?
* Are preventative controls reducing new duplicate signals?
* Are confirmed duplicates being resolved safely?

#### Possible measures

| Measure                              | Intended use                     | Current status              |
| ------------------------------------ | -------------------------------- | --------------------------- |
| Potential duplicate records          | Diagnostic workload              | Exploratory                 |
| Potential duplicate pairs or groups  | Understand match workload        | Grain requires agreement    |
| Confirmed duplicates                 | Validated problem measure        | Operational review required |
| Rejected matches                     | Understand false-positive burden | Not yet available           |
| Unresolved matches                   | Understand backlog               | Not yet governed            |
| New duplicate signals per period     | Trend detection                  | Rule version required       |
| Duplicate remediation effort         | Operational value baseline       | Not yet measured            |
| Duplicate creation by source pathway | Root-cause analysis              | Exploratory                 |
| Prevention-control failure rate      | Evaluate upstream controls       | Future measure              |

#### Key caveat

Use consistent terminology:

* duplicate signal;
* potential duplicate;
* confirmed duplicate;
* rejected match;
* unresolved match;
* merge candidate; and
* merged.

Do not label all flagged records as duplicates.

## Minimum contact-data quality

#### Decision question

Are eligible Person Account records sufficiently complete for their intended operational use?

#### Possible measures

| Measure                                  | Intended use                | Current status           |
| ---------------------------------------- | --------------------------- | ------------------------ |
| Eligible Person Account records assessed | Denominator                 | Definition required      |
| Records meeting minimum contact rule     | Compliance numerator        | Rule refinement required |
| Records failing minimum contact rule     | Diagnostic failure count    | Exploratory              |
| Approved exceptions                      | Explain legitimate failures | Exception model required |
| Failure rate by source pathway           | Root-cause analysis         | Exploratory              |
| Repeat failure after correction          | Control effectiveness       | Future measure           |

#### Key caveat

A populated field does not automatically represent:

* valid contact information;
* usable contact information;
* consent;
* communication preference; or
* customer reachability.

## Deceased-customer handling

#### Decision question

Is deceased status being handled consistently enough to prevent inappropriate communication and incorrect account relationships?

#### Possible measures

| Measure                                                   | Intended use                | Current status          |
| --------------------------------------------------------- | --------------------------- | ----------------------- |
| Confirmed deceased-status handling issues                 | Problem baseline            | Not yet defined         |
| Inappropriate communications after known deceased status  | Customer/risk outcome       | Evidence required       |
| Records with inconsistent deceased status across systems  | Diagnostic measure          | Source rules required   |
| Time from verified notification to required system update | Operational-control measure | Process not yet defined |
| Exceptions requiring manual intervention                  | Operational burden          | Future measure          |

#### Key caveat

Do not infer deceased status analytically.

The status must come from an approved source and process.

## Customer information restriction and opt-out

#### Decision question

Are approved customer restrictions, preferences and opt-outs applied consistently?

#### Possible measures

| Measure                                  | Intended use        | Current status          |
| ---------------------------------------- | ------------------- | ----------------------- |
| Approved restriction or opt-out requests | Demand signal       | Definition required     |
| Requests requiring manual remediation    | Operational burden  | Not yet measured        |
| Confirmed control failures               | Risk measure        | Not yet defined         |
| Time to apply approved restriction       | Service measure     | Process not yet defined |
| Rework caused by incorrect consolidation | Operational measure | Future measure          |

#### Key caveat

Do not combine:

* deletion;
* correction;
* suppression;
* communication preference;
* consent;
* retention; and
* central-record opt-out

into a single metric unless the business definitions are explicitly aligned.

## Customer authentication

#### Decision question

Are customer-account changes supported by authentication controls proportionate to interaction risk?

#### Possible measures

| Measure                                          | Intended use            | Current status          |
| ------------------------------------------------ | ----------------------- | ----------------------- |
| Interactions requiring authentication            | Population context      | Not defined             |
| Authentication exceptions                        | Control diagnostic      | Not defined             |
| Confirmed incorrect-account updates              | Risk outcome            | Evidence required       |
| Escalations caused by authentication uncertainty | Operational signal      | Not measured            |
| Compliance with agreed authentication pattern    | Future governed measure | Standard required first |

#### Key caveat

Authentication measures should be risk-based.

A single authentication method should not be assumed to apply across every service, channel or transaction.

## Operational value measures

Potential cross-cutting measures include:

| Measure                                   | Value question                                                |
| ----------------------------------------- | ------------------------------------------------------------- |
| Manual remediation volume                 | How much work exists because account quality is poor?         |
| Average remediation effort                | How much staff effort does each issue require?                |
| Repeat remediation                        | Are problems recurring after correction?                      |
| Support demand related to account quality | How much avoidable operational demand is generated?           |
| Escalation volume                         | How often does unclear ownership or process cause escalation? |
| Backlog age                               | Are unresolved account-quality issues accumulating?           |
| Source-process recurrence                 | Are defects continuing to be created upstream?                |

Do not monetise staff effort until:

* the activity is clearly defined;
* the volume is repeatable;
* the time estimate is credible; and
* the costing assumptions are approved.

## Strategic capability measures

Potential measures of reusable capability include:

* proportion of priority rules with assigned business owners;
* proportion of governed measures with complete definitions;
* number of recurring issues with agreed operational pathways;
* adoption of common Customer Account Management patterns;
* number of services reusing approved standards;
* reduction in unowned data-quality queues;
* rule-version consistency across Salesforce and Databricks;
* percentage of priority opportunities with explicit decisions; and
* number of improvements moving from recurring remediation to upstream prevention.

These should be used cautiously.

Documentation completeness is not itself a customer outcome.

## Viability evidence for investment

A future investment case should combine multiple evidence types rather than rely on one headline metric.

### Customer evidence

* severity and frequency of customer impact;
* repeated customer effort;
* inappropriate communication;
* incorrect identity or relationship handling; and
* customer trust implications.

### Operational evidence

* staff effort;
* remediation demand;
* repeated investigation;
* manual workarounds;
* support demand; and
* backlog.

### Risk evidence

* privacy exposure;
* control gaps;
* governance exceptions;
* data-integrity impact; and
* service continuity risk.

### Strategic evidence

* impact across multiple services;
* dependency for CRM or digital uplift;
* reusable capability;
* future connected-interaction readiness; and
* ability to support safer analytics or AI.

### Cost and feasibility evidence

* current capability;
* change complexity;
* implementation dependencies;
* operating cost;
* technology cost;
* ongoing ownership; and
* expected scale of benefit.

## Measure definition template

Before a metric is used for decision-making, record:

| Field             | Definition                                                          |
| ----------------- | ------------------------------------------------------------------- |
| Business question | What decision the metric supports                                   |
| Metric            | Exact measure name                                                  |
| Definition        | Plain-English calculation                                           |
| Numerator         | What is counted above the line                                      |
| Denominator       | Eligible comparison population                                      |
| Source            | Authoritative system or dataset                                     |
| Grain             | Record, interaction, case, person, pair, group or other unit        |
| Filters           | Included and excluded conditions                                    |
| Period            | Reporting timeframe                                                 |
| Rule version      | Logic version where applicable                                      |
| Owner             | Accountable business owner                                          |
| Status            | Exploratory / Baseline / Controlled test / Governed                 |
| Caveat            | Known limitation                                                    |
| Permitted use     | Discovery, operational reporting, executive reporting or evaluation |

## Databricks measurement role

Databricks can support:

* profiling;
* data-quality diagnostics;
* baseline measurement;
* trends;
* segmentation;
* root-cause analysis; and
* controlled evaluation.

Databricks should not independently determine:

* customer identity;
* confirmed duplicates;
* customer consent;
* deceased status;
* legal retention;
* required remediation; or
* business priority.

Those decisions require business and governance ownership.

## Baseline priorities

The first baseline work should focus on measures that materially improve viability decisions.

### Priority 1 — Duplicate scale and operational burden

Establish:

* safe duplicate-signal grain;
* eligible population;
* trend;
* affected account types;
* source pathways; and
* remediation effort.

### Priority 2 — Customer identity and incorrect linking

Establish:

* validated incident count;
* eligible interaction or account population;
* repeat patterns; and
* consequences.

### Priority 3 — Minimum customer-data quality

Establish:

* rule definitions;
* eligible populations;
* failure counts;
* exception treatment; and
* source pathways.

Do not expand the measurement backlog until these measures are sufficiently clear to support decisions.

## Success criteria for the Define phase

Define is successful when leaders can answer:

1. Which Customer Account Management problems are materially important?
2. What evidence supports that conclusion?
3. What value could improvement create?
4. Which measures could establish a credible baseline?
5. Which opportunities appear viable?
6. Which require more evidence?
7. Which justify deeper investment assessment?
8. What would need to be measured during a pilot or intervention?
9. What evidence would support a future business case?
10. What should not progress?

## Current measurement position

At this stage:

* several useful diagnostic signals exist;
* most measures are not yet governed;
* denominators remain unresolved for several important questions;
* duplicate terminology and grain require discipline;
* operational-effort baselines are incomplete;
* no financial benefits are validated;
* no target has been approved; and
* measurement should remain focused on viability and prioritisation.

## Next action

Define the first baseline measures for:

1. duplicate scale and remediation effort;
2. incorrect customer-account linking; and
3. minimum customer-data quality.

For each, confirm:

* business question;
* source;
* grain;
* population;
* numerator;
* denominator;
* caveat;
* owner; and
* permitted use.

Then use those baselines alongside the desktop scan to strengthen the viability assessment in `02-define/prioritised-opportunities.md`.

## Review notes

<!-- AUTO-REVIEW-NOTES:START -->

| Date | Update | Updated by | Commit |
| ---- | ------ | ---------- | ------ |

<!-- AUTO-REVIEW-NOTES:END -->
