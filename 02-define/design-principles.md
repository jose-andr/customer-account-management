# Design principles

Status: Draft
Owner: José Andrade
Last updated: 13 August 2026

## Purpose

Define the principles that future Customer Account Management options must satisfy before they progress into design, testing or investment assessment.

These principles help the working group compare options consistently.

They are not detailed solution requirements.

## North star

> Assess the viability of improvements to Customer Account Management and potential future investment at City of Melbourne, using evidence to support prioritisation and business-case decisions.

## How to use these principles

Use the principles when:

* assessing external examples;
* framing potential options;
* comparing process, governance and technology responses;
* deciding whether an opportunity should progress;
* preparing controlled experiments;
* evaluating future investment options; and
* identifying reasons to reject an option.

A proposed option does not need to be perfect against every principle.

Material conflicts must be explicit and resolved before progression.

## Principle 1 — Protect customer identity

Customer Account Management should increase confidence that information and services are associated with the correct customer or authorised relationship.

Options should:

* avoid relying on one weak identity signal;
* distinguish identity from contact-data similarity;
* support appropriate verification;
* account for shared contact information;
* protect complex account relationships; and
* require human review where automated confidence is insufficient.

### Viability test

> Does this option increase identity confidence without creating unacceptable false matches or customer harm?

## Principle 2 — Prevent problems upstream where practical

Recurring data-quality defects should be reduced at source rather than managed indefinitely through downstream cleansing.

Options should consider:

* where defects originate;
* whether prevention is possible;
* whether prevention would block legitimate service activity;
* whether warnings are safer than hard controls;
* how exceptions are handled; and
* whether remediation effort can be reduced over time.

### Viability test

> Does this option reduce recurring defects, or does it mainly create another downstream remediation process?

## Principle 3 — Keep human judgement where consequences are material

Automation should support review and decision-making rather than replace human judgement where:

* identity is uncertain;
* merging could remove or combine important information;
* customer relationships are complex;
* sensitive statuses are involved;
* privacy consequences may occur; or
* exceptions require contextual understanding.

### Viability test

> Is the level of automation proportionate to the consequence of being wrong?

## Principle 4 — Separate signals from decisions

Analytical or system outputs should be labelled according to what they actually establish.

For example:

* a duplicate signal is not a confirmed duplicate;
* a matching field is not confirmed identity;
* a rule failure is not automatically an invalid customer;
* a populated field is not automatically usable contact information; and
* an analytical anomaly is not automatically a remediation instruction.

### Viability test

> Does the option preserve the distinction between detection, review, decision and action?

## Principle 5 — Support complex customer relationships

Customer Account Management should accommodate legitimate complexity rather than force every customer into a simple one-person-to-one-record model.

Relevant complexity may include:

* statutory and non-statutory relationships;
* Service Accounts;
* representatives;
* organisations;
* shared contact information;
* historical records;
* restricted records;
* deceased customers; and
* other approved exceptions.

### Viability test

> Can the option handle legitimate exceptions without driving staff toward workarounds or false data?

## Principle 6 — Design privacy and records controls into operations

Privacy, records, security and information-management requirements should be translated into usable operational controls.

Options should make clear:

* who can perform an action;
* what evidence is required;
* what must be retained;
* what may be changed;
* what requires escalation;
* where exceptions are recorded; and
* who owns the decision.

### Viability test

> Can staff apply the required control consistently during real service delivery?

## Principle 7 — Make ownership explicit

Every ongoing Customer Account Management capability should have clear ownership.

Options should identify:

* business owner;
* operational owner;
* technical owner;
* data steward where relevant;
* governance decision-maker;
* exception owner; and
* escalation pathway.

### Viability test

> If this option creates a rule, alert or backlog tomorrow, is it clear who will act on it?

## Principle 8 — Use existing capability before adding technology

Existing Salesforce, Plauti, Databricks, integration, governance and operational capabilities should be understood before additional technology is proposed.

An option should explain:

* what already exists;
* why it is insufficient;
* whether configuration or process improvement is enough;
* what capability gap remains; and
* why further investment is proportionate.

### Viability test

> Is additional technology solving a demonstrated capability gap rather than compensating for unclear process or ownership?

## Principle 9 — Make data quality actionable

Data-quality measurement should lead to a defined operational or strategic response.

A useful measure should clarify:

* what is being measured;
* why it matters;
* who owns the result;
* what action may follow;
* what exceptions exist; and
* whether the measure is diagnostic or governed.

### Viability test

> If the measure deteriorates, do we know what decision or action follows?

## Principle 10 — Keep measures decision-safe

Metrics must preserve:

* source;
* grain;
* eligible population;
* numerator;
* denominator;
* filters;
* rule version;
* caveats; and
* permitted use.

Do not describe record-level quality as customer-level quality without evidence.

### Viability test

> Could a leader interpret this measure correctly without being misled about what was counted?

## Principle 11 — Design for sustainable operations

A viable option must consider what happens after implementation.

Assess:

* ongoing monitoring;
* workload;
* support requirements;
* rule maintenance;
* exception handling;
* training;
* governance;
* reporting; and
* continuous improvement.

### Viability test

> Can the organisation operate this capability sustainably, or does it create an unowned long-term burden?

## Principle 12 — Improve the system, not only individual records

Customer Account Management should move progressively from correction toward understanding why defects occur.

Options should support:

* root-cause analysis;
* recurring-pattern identification;
* source-process improvement;
* feedback into upstream services;
* prevention; and
* evaluation of whether defects return.

### Viability test

> Does the option improve the conditions that create the issue, or only repair individual records after failure?

## Principle 13 — Preserve customer access and service continuity

Controls should not make it unnecessarily difficult for customers or staff to complete legitimate service interactions.

Hard validation, identity checks and account controls should be proportionate to:

* customer risk;
* transaction risk;
* information sensitivity;
* available evidence; and
* service context.

### Viability test

> Does the control reduce risk without creating disproportionate customer effort, exclusion or operational workaround?

## Principle 14 — Create reusable capability

Where practical, improvements should create patterns that can be reused across Customer Account Management rather than isolated fixes for one service.

Potential reusable capabilities include:

* identity patterns;
* account-relationship rules;
* data-quality standards;
* exception models;
* stewardship patterns;
* measurement definitions;
* escalation pathways; and
* governance controls.

### Viability test

> Can this capability be reused across relevant services without forcing inappropriate standardisation?

## Principle 15 — Evidence before investment

Material investment should follow evidence that:

* the problem is real;
* its scale or consequence is meaningful;
* expected value is clear;
* existing capability is insufficient;
* feasible options exist;
* constraints are understood; and
* success can be measured.

### Viability test

> Is there enough evidence to justify spending more time or money on this option?

## Option review template

Use this table when comparing future options.

| Principle                           | Meets | Partially meets | Does not meet | Evidence / implication |
| ----------------------------------- | ----- | --------------- | ------------- | ---------------------- |
| Protect customer identity           |       |                 |               |                        |
| Prevent problems upstream           |       |                 |               |                        |
| Keep human judgement where material |       |                 |               |                        |
| Separate signals from decisions     |       |                 |               |                        |
| Support complex relationships       |       |                 |               |                        |
| Embed privacy and records controls  |       |                 |               |                        |
| Make ownership explicit             |       |                 |               |                        |
| Use existing capability first       |       |                 |               |                        |
| Make data quality actionable        |       |                 |               |                        |
| Keep measures decision-safe         |       |                 |               |                        |
| Design for sustainable operations   |       |                 |               |                        |
| Improve root causes                 |       |                 |               |                        |
| Preserve customer access            |       |                 |               |                        |
| Create reusable capability          |       |                 |               |                        |
| Evidence before investment          |       |                 |               |                        |

## Material principle conflicts

An option should not progress without explicit review where it:

* increases risk of incorrect customer identification;
* enables uncontrolled merging;
* removes necessary human review;
* weakens privacy or records controls;
* creates an unowned operational backlog;
* depends on misleading metrics;
* blocks legitimate customer interactions without an exception pathway;
* requires material investment without sufficient evidence; or
* creates a local solution that materially conflicts with broader organisational capability.

## Relationship to viability assessment

These principles answer:

> What must a credible option be able to do?

`02-define/prioritised-opportunities.md` answers:

> Which opportunities appear worth pursuing?

`02-define/outcomes-and-value.md` answers:

> What value should they create?

`02-define/success-measures.md` answers:

> How would we know whether that value was created?

`02-define/problem-boundaries.md` answers:

> What constraints must the option operate within?

Together, these provide the decision basis for moving from Define into Design.

## Current principle decision

At this stage:

* no technology option is preferred;
* no automated merge model is approved;
* identity and duplicate decisions remain human-controlled where consequences are material;
* existing capability should be understood before new investment;
* operational ownership is required for viability;
* customer access and legitimate exceptions must be protected;
* data-quality outputs must remain decision-safe; and
* material investment requires stronger evidence than reported pain points alone.

## Next action

Use these principles during the desktop scan and the first option-framing activity.

Record where external examples:

* reinforce a principle;
* challenge a principle;
* expose a missing principle; or
* demonstrate a relevant trade-off.

Only amend the principles where repeated evidence shows that a change would improve decision quality.

## Review notes

<!-- AUTO-REVIEW-NOTES:START -->

| Date | Update | Updated by | Commit |
| ---- | ------ | ---------- | ------ |

<!-- AUTO-REVIEW-NOTES:END -->
