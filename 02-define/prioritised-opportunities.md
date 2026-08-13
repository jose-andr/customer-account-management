# Prioritised opportunities

Status: Draft
Owner: José Andrade
Last updated: 13 August 2026

## Purpose

Assess and prioritise Customer Account Management improvement opportunities using evidence, organisational context and viability.

This page is the decision record for determining which opportunities should:

* progress into Design;
* receive further investigation;
* be considered for deeper investment assessment;
* remain parked; or
* be closed.

Priority does not imply that a solution has been approved.

## North star

> Assess the viability of improvements to Customer Account Management and potential future investment at City of Melbourne, using evidence to support prioritisation and business-case decisions.

## Decision question

> Which Customer Account Management improvements are sufficiently valuable, viable and evidence-supported to justify further design, testing or investment analysis?

## Evidence inputs

Prioritisation should draw from:

* current-state discovery;
* existing evidence inventory;
* Customer Account Management initiative register;
* Databricks customer-data-quality pilot evidence;
* CRM and Plauti configuration evidence;
* stakeholder knowledge;
* customer and operational examples;
* applicable governance guidance; and
* external desktop-scan evidence.

Relevant repository pages include:

* `01-discover/existing-evidence-inventory.md`
* `01-discover/current-state-evidence-synthesis.md`
* `01-discover/databricks-customer-data-quality-pilot-input.md`
* `02-define/problem-statement.md`
* `02-define/definition-overview.md`
* `02-define/outcomes-and-value.md`
* `04-deliver/initiative-register.md`

## Viability dimensions

Assess each opportunity against the following dimensions.

| Dimension            | Assessment question                                                                    |
| -------------------- | -------------------------------------------------------------------------------------- |
| Customer value       | Would this materially improve customer experience, trust, continuity or accessibility? |
| Operational value    | Would this reduce avoidable effort, rework, manual investigation or uncertainty?       |
| Risk reduction       | Would this materially reduce privacy, data, service, governance or reputational risk?  |
| Evidence strength    | Is the underlying problem sufficiently supported by evidence?                          |
| Strategic fit        | Does this support the intended Customer Account Management direction?                  |
| Organisational fit   | Can the improvement work within City of Melbourne's operating environment?             |
| Capability readiness | Are the required people, process, governance and technology capabilities available?    |
| Complexity           | How difficult would the improvement be to introduce safely?                            |
| Dependencies         | What other decisions, controls or capabilities must exist first?                       |
| Investment signal    | Is the opportunity significant enough to justify deeper investment analysis?           |

## Assessment scale

Use qualitative judgement rather than a weighted numerical score at this stage.

| Rating   | Meaning                                                    |
| -------- | ---------------------------------------------------------- |
| Strong   | Current evidence supports progression                      |
| Moderate | Opportunity appears credible but material questions remain |
| Weak     | Evidence or viability is currently insufficient            |
| Unknown  | Additional investigation is required                       |

Do not aggregate these ratings into a single score unless the working group agrees that weighting would improve the decision.

## Decision outcomes

Each opportunity should receive one of four outcomes.

### Progress

Evidence and viability are sufficient to move into Design or controlled testing.

### Investigate further

The opportunity appears important but requires additional evidence before progression.

### Escalate for investment assessment

The opportunity appears strategically important and may require material investment. Evidence is sufficient to justify deeper business-case analysis.

### Park

Current evidence or viability does not justify further work at this stage.

## Initial opportunity set

The initial opportunity set is derived from the Customer Account Management initiative register and current discovery evidence.

| ID          | Opportunity                                                                 | Current priority | Current decision    | Confidence |
| ----------- | --------------------------------------------------------------------------- | ---------------- | ------------------- | ---------- |
| CAM-OPP-001 | Improve customer identity and Service Account linking                       | High             | Investigate further | Moderate   |
| CAM-OPP-002 | Improve duplicate prevention and safe resolution                            | High             | Investigate further | Moderate   |
| CAM-OPP-003 | Establish consistent deceased-customer handling                             | High             | Investigate further | Moderate   |
| CAM-OPP-004 | Establish clear handling for customer data removal and restriction requests | High             | Investigate further | Low        |
| CAM-OPP-005 | Improve central customer record opt-out handling                            | Medium           | Investigate further | Low        |
| CAM-OPP-006 | Establish proportionate customer authentication standards                   | Medium           | Investigate further | Low        |

No opportunity is currently approved for implementation.

## CAM-OPP-001 — Improve customer identity and Service Account linking

### Problem signal

Service Accounts may be linked to an incorrect Person Account where shared contact information is treated as sufficient identity evidence.

### Potential value

* reduce incorrect account relationships;
* reduce privacy exposure;
* improve customer confidence;
* improve customer-history continuity;
* reduce manual correction effort; and
* improve confidence in downstream CRM use.

### Current viability assessment

| Dimension            | Rating   | Current interpretation                                                    |
| -------------------- | -------- | ------------------------------------------------------------------------- |
| Customer value       | Strong   | Incorrect identity can directly affect customer trust and experience      |
| Operational value    | Moderate | Better linking may reduce investigation and correction effort             |
| Risk reduction       | Strong   | Potential privacy and identity risk is material                           |
| Evidence strength    | Moderate | Reported examples exist but scale and system behaviour require validation |
| Strategic fit        | Strong   | Directly supports reliable customer-account management                    |
| Organisational fit   | Unknown  | Current matching and integration constraints need investigation           |
| Capability readiness | Unknown  | Required controls and ownership are not yet confirmed                     |
| Complexity           | Unknown  | May span CRM, Service Account and integration logic                       |
| Dependencies         | Moderate | Depends on identity, matching and account-model decisions                 |
| Investment signal    | Moderate | May justify further investment if scale and systemic cause are confirmed  |

### Current decision

**Investigate further**

### Evidence needed next

* current matching logic;
* system responsible for linking;
* frequency and affected population;
* de-identified test scenarios;
* current correction pathway; and
* viable external approaches to identity and account linking.

## CAM-OPP-002 — Improve duplicate prevention and safe resolution

### Problem signal

Duplicate accounts remain a recurring data-quality and operational issue, and current merge controls may not safely support all account relationships.

### Potential value

* reduce fragmented customer history;
* reduce staff search and remediation effort;
* improve integration reliability;
* improve customer communication consistency; and
* improve confidence in CRM information.

### Current viability assessment

| Dimension            | Rating   | Current interpretation                                                                   |
| -------------------- | -------- | ---------------------------------------------------------------------------------------- |
| Customer value       | Moderate | Fragmentation can cause inconsistent interactions                                        |
| Operational value    | Strong   | Duplicate management creates recurring manual effort                                     |
| Risk reduction       | Strong   | Unsafe merges and unresolved duplicates both create risk                                 |
| Evidence strength    | Moderate | Existing issues and rule work support the problem, but validated scale is still required |
| Strategic fit        | Strong   | Core Customer Account Management capability                                              |
| Organisational fit   | Moderate | Existing Salesforce, Plauti and Databricks capabilities provide a starting point         |
| Capability readiness | Moderate | Some controls exist but ownership and operating rules remain incomplete                  |
| Complexity           | Strong   | Complex relationships and merge consequences require careful handling                    |
| Dependencies         | Strong   | Account model, identity rules, governance and operational review are dependencies        |
| Investment signal    | Moderate | May justify investment if prevention and remediation volumes support the case            |

### Current decision

**Investigate further**

### Evidence needed next

* active Plauti configuration;
* duplicate volumes and trends;
* false-positive and false-negative evidence;
* affected account combinations;
* upstream duplicate-creation pathways;
* current remediation effort; and
* external duplicate-prevention and stewardship practices.

## CAM-OPP-003 — Establish consistent deceased-customer handling

### Problem signal

Deceased status may be managed inconsistently across systems and customer communications.

### Potential value

* prevent inappropriate contact;
* reduce distress to customers and families;
* improve information consistency;
* reduce manual reconciliation;
* improve governance; and
* reduce reputational risk.

### Current viability assessment

| Dimension            | Rating          | Current interpretation                                                            |
| -------------------- | --------------- | --------------------------------------------------------------------------------- |
| Customer value       | Strong          | Incorrect contact can create direct customer harm                                 |
| Operational value    | Moderate        | Consistent status could reduce repeated manual handling                           |
| Risk reduction       | Strong          | Material customer, governance and reputational implications                       |
| Evidence strength    | Moderate        | A reported issue exists but the full current-state process needs validation       |
| Strategic fit        | Strong          | Supports trusted customer information                                             |
| Organisational fit   | Unknown         | Pathway, Salesforce and process ownership need clarification                      |
| Capability readiness | Unknown         | Source-of-truth and control requirements remain unresolved                        |
| Complexity           | Moderate        | Cross-system propagation and governance may be required                           |
| Dependencies         | Strong          | Requires authoritative source and handling rules                                  |
| Investment signal    | Low to Moderate | May be primarily process and integration improvement rather than major investment |

### Current decision

**Investigate further**

### Evidence needed next

* authoritative source;
* current Pathway and Salesforce process;
* affected communications;
* governance requirements;
* ownership;
* integration feasibility; and
* comparable organisational practice.

## CAM-OPP-004 — Establish clear handling for customer data removal and restriction requests

### Problem signal

A consistent operational pathway for customer requests to remove, restrict, correct or suppress personal information is not yet documented.

### Potential value

* improve privacy handling;
* reduce inconsistent staff decisions;
* improve customer trust;
* clarify retention constraints; and
* create clearer escalation and governance pathways.

### Current viability assessment

Current evidence is insufficient for a confident assessment.

The first requirement is to distinguish:

* correction;
* deletion;
* restriction;
* suppression;
* contact preference;
* consent;
* retention; and
* legal or recordkeeping obligations.

### Current decision

**Investigate further**

### Evidence needed next

* approved privacy and records guidance;
* current operational process;
* decision ownership;
* existing system capabilities;
* request volumes; and
* valid exceptions.

## CAM-OPP-005 — Improve central customer record opt-out handling

### Problem signal

Opt-out handling may rely on manual monitoring and may not be visible at the point of customer interaction.

### Potential value

* improve customer preference handling;
* reduce manual monitoring;
* reduce unintended consolidation;
* improve frontline visibility; and
* improve consistency.

### Current viability assessment

Current evidence remains limited.

The organisation first needs an agreed definition of what central-record opt-out means operationally.

### Current decision

**Investigate further**

### Evidence needed next

* approved opt-out definition;
* current process;
* affected systems;
* volumes;
* staff visibility requirements;
* permitted exceptions; and
* governance ownership.

## CAM-OPP-006 — Establish proportionate customer authentication standards

### Problem signal

A consistent approach to confirming customer identity before accessing or changing information has not yet been defined for this workstream.

### Potential value

* reduce unauthorised access or change;
* improve customer trust;
* improve staff consistency;
* support safer customer-account maintenance; and
* reduce incorrect identification.

### Current viability assessment

Authentication requirements are likely to vary by:

* channel;
* transaction;
* information sensitivity;
* risk level; and
* service context.

A single authentication method should therefore not be assumed.

### Current decision

**Investigate further**

### Evidence needed next

* current practices by channel;
* existing organisational standards;
* high-risk interaction types;
* operational pain points;
* governance requirements; and
* external risk-based authentication patterns.

## Desktop scan connection

The desktop scan should be used to test these opportunities rather than generate unrelated best-practice findings.

For each opportunity, ask:

1. How do comparable organisations address this problem?
2. Which capabilities appear consistently important?
3. What is handled through process or governance rather than technology?
4. What evidence of value is available?
5. What organisational conditions are required?
6. What appears transferable to City of Melbourne?
7. What should not be inferred from the example?

## Priority desktop-scan questions

The first scan should focus on:

1. How do organisations establish confidence in customer identity and account relationships?
2. How do they prevent and safely resolve duplicate customer records?
3. How is customer-data quality owned and governed operationally?
4. How are sensitive customer statuses and preferences represented across systems?
5. What measures are used to demonstrate the value of Customer Account Management improvements?
6. Which capabilities required material investment and which were achieved through operating-model or process changes?

## Investment signals

The Define phase should identify investment signals rather than prematurely create a business case.

An opportunity may warrant deeper investment assessment where there is evidence of:

* material customer harm or risk;
* recurring operational effort;
* significant data-quality impact;
* cross-system dependency;
* inadequate existing capability;
* inability to address the issue through modest process improvement;
* measurable benefit from change; and
* strategic relevance beyond a single isolated issue.

## Prioritisation workshop

After the desktop scan, use a working session to review each opportunity against the viability dimensions.

For each opportunity, record:

| Field                | Decision                                                                   |
| -------------------- | -------------------------------------------------------------------------- |
| Evidence strength    | Strong / Moderate / Weak / Unknown                                         |
| Customer value       | Strong / Moderate / Weak / Unknown                                         |
| Operational value    | Strong / Moderate / Weak / Unknown                                         |
| Risk reduction       | Strong / Moderate / Weak / Unknown                                         |
| Organisational fit   | Strong / Moderate / Weak / Unknown                                         |
| Capability readiness | Strong / Moderate / Weak / Unknown                                         |
| Investment signal    | Strong / Moderate / Weak / Unknown                                         |
| Decision             | Progress / Investigate further / Escalate for investment assessment / Park |
| Rationale            | Why this decision was made                                                 |
| Owner                | Who owns the next action                                                   |
| Evidence gap         | What still needs to be learned                                             |

## Current prioritisation position

At this stage:

* no opportunity is approved for implementation;
* no opportunity has been escalated into a formal business case;
* CAM-OPP-001 and CAM-OPP-002 currently have the strongest combination of customer, operational and risk signals;
* CAM-OPP-003 has a strong customer and governance signal but requires current-state validation;
* CAM-OPP-004 to CAM-OPP-006 require clearer policy, process and evidence before confident prioritisation; and
* the desktop scan should test rather than confirm these initial interpretations.

## Next action

Agree the first desktop-scan questions and assess a small number of relevant external examples against CAM-OPP-001, CAM-OPP-002 and CAM-OPP-003.

Use the findings to update this page with the first explicit **Progress / Investigate further / Escalate / Park** decisions.

## Review notes

<!-- AUTO-REVIEW-NOTES:START -->

| Date | Update | Updated by | Commit |
| ---- | ------ | ---------- | ------ |

<!-- AUTO-REVIEW-NOTES:END -->
