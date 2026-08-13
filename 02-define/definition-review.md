# Definition review

Status: Draft
Owner: José Andrade
Last updated: 13 August 2026

## Purpose

Run a focused working-group review to agree what City of Melbourne needs to learn before prioritising Customer Account Management improvements.

The session establishes:

* the questions for the external desktop scan;
* the first opportunities to investigate;
* the viability dimensions that matter;
* the evidence required for prioritisation; and
* the decisions the Define phase must support.

This is not a solution-design workshop.

## North star

> Assess the viability of improvements to Customer Account Management and potential future investment at City of Melbourne, using evidence to support prioritisation and business-case decisions.

## Session decision

By the end of the review, the group should be able to answer:

> What do we need to learn from internal evidence and comparable external practice to decide which Customer Account Management improvements are worth progressing?

## Expected outputs

The session should produce:

1. five to eight agreed desktop-scan questions;
2. three to five relevant organisations or examples to investigate;
3. agreed viability dimensions;
4. two or three priority opportunities for the first assessment;
5. known evidence gaps;
6. owners for the scan;
7. a date for playback; and
8. explicit decisions recorded in the repository.

## Inputs

Review these before the session:

* `01-discover/existing-evidence-inventory.md`
* `01-discover/current-state-evidence-synthesis.md`
* `01-discover/databricks-customer-data-quality-pilot-input.md`
* `02-define/problem-statement.md`
* `02-define/definition-overview.md`
* `02-define/outcomes-and-value.md`
* `02-define/prioritised-opportunities.md`
* `02-define/success-measures.md`
* `04-deliver/initiative-register.md`

The group does not need to review every repository page.

Bring only enough evidence to support the decisions in this session.

## Participants

Minimum working group:

* Customer Focus and Strategy Manager;
* CRM Product Owner;
* Customer Data and Systems Support Officer; and
* project lead.

Invite specialist stakeholders only where their input is necessary for a decision.

Potential later contributors include:

* Privacy;
* Records;
* Data Governance;
* Information Security;
* Salesforce / CRM;
* Databricks / analytics;
* operational service owners; and
* Contact Centre representatives.

## Suggested duration

60–90 minutes.

## Agenda

### 1. Reconfirm the decision — 10 minutes

Review:

* the current problem statement;
* the viability North Star;
* the initial opportunity set; and
* what the Define phase is trying to decide.

Prompt:

> If this work is successful, what investment or prioritisation decision should leaders be better able to make?

Do not begin with technology options.

### 2. Review what we already know — 10 minutes

Use the evidence inventory and initiative register to identify:

* strong evidence;
* reported but unvalidated signals;
* known risks;
* current analytical work;
* missing baselines; and
* unresolved ownership.

Prompt:

> What do we already know well enough that we do not need to rediscover it?

### 3. Define what we need to learn — 20 minutes

Ask the group:

> What are the key questions we would like the desktop scan to answer?

Generate questions first.

Do not begin by selecting organisations.

Group the questions into themes.

## Candidate desktop-scan questions

### Customer identity and account relationships

* How do organisations establish confidence that a customer record represents the correct person?
* How are shared email addresses, mobile numbers and household relationships handled?
* How are customer, organisation, representative and statutory relationships represented?
* What prevents automated linking from creating incorrect relationships?

### Duplicate prevention and resolution

* How do organisations prevent duplicate customer records from being created?
* How are potential duplicates distinguished from confirmed duplicates?
* What requires human review?
* Which merge decisions are automated and which remain controlled?
* How are complex account relationships protected during resolution?

### Customer information management

* How are deceased customers represented and propagated across systems?
* How are customer restrictions, preferences and opt-outs represented?
* How are customer requests for correction, restriction or removal handled?
* How are exceptions managed?

### Authentication

* How do organisations vary authentication according to interaction risk?
* Which account changes require stronger identity checks?
* How are authentication exceptions handled?

### Data quality and operating model

* Who owns customer-account quality?
* Who acts on data-quality failures?
* What quality standards are governed centrally?
* How is recurring remediation converted into upstream prevention?
* How are Salesforce, analytics, duplicate-management tools and human review separated?

### Value and investment

* What evidence was used to justify Customer Account Management investment?
* Which outcomes were measured before and after improvement?
* What improvements required technology investment?
* What improvements were primarily process, governance or operating-model changes?
* What capabilities proved reusable across services?

## Question prioritisation

Do not research every question.

For each candidate question, ask:

| Test               | Question                                                         |
| ------------------ | ---------------------------------------------------------------- |
| Decision relevance | Would the answer change a prioritisation or investment decision? |
| Evidence gap       | Do we genuinely lack this information?                           |
| Transferability    | Is external practice likely to help?                             |
| Urgency            | Does this relate to a current high-priority issue?               |
| Researchability    | Is credible evidence likely to be accessible?                    |

Select approximately five to eight questions for the first scan.

## Agreed desktop-scan questions

Record the final questions here after the session.

|  # | Agreed question | Related opportunity | Why it matters | Owner |
| -: | --------------- | ------------------- | -------------- | ----- |
|  1 |                 |                     |                |       |
|  2 |                 |                     |                |       |
|  3 |                 |                     |                |       |
|  4 |                 |                     |                |       |
|  5 |                 |                     |                |       |
|  6 |                 |                     |                |       |
|  7 |                 |                     |                |       |
|  8 |                 |                     |                |       |

## Select external examples

Only select examples after the questions are agreed.

An organisation is useful when it can provide evidence relevant to one or more agreed questions.

Potential categories include:

* local or state government;
* organisations with complex statutory relationships;
* organisations managing sensitive customer information;
* utilities or service providers with persistent accounts;
* organisations with mature CRM or customer-data practices; and
* organisations that have documented Customer Account Management transformation.

State Trustees has been suggested as an initial example to explore.

Treat it as a research candidate, not a benchmark to copy.

## Example selection criteria

| Criterion              | Question                                                                          |
| ---------------------- | --------------------------------------------------------------------------------- |
| Context similarity     | Does the organisation manage comparable customer or relationship complexity?      |
| Problem relevance      | Has it addressed one of our priority questions?                                   |
| Evidence accessibility | Is credible information available?                                                |
| Practice maturity      | Does the example show an established approach rather than marketing claims alone? |
| Transferability        | Could the learning plausibly inform City of Melbourne?                            |

## Agreed examples

| Organisation / example | Questions it may inform | Why selected                | Evidence source | Owner     |
| ---------------------- | ----------------------- | --------------------------- | --------------- | --------- |
| State Trustees         | To confirm              | Suggested external use case | To identify     | To assign |
|                        |                         |                             |                 |           |
|                        |                         |                             |                 |           |
|                        |                         |                             |                 |           |
|                        |                         |                             |                 |           |

## Confirm viability dimensions

Review the dimensions defined in `02-define/prioritised-opportunities.md`.

Proposed dimensions:

* customer value;
* operational value;
* risk reduction;
* evidence strength;
* strategic fit;
* organisational fit;
* capability readiness;
* complexity;
* dependencies; and
* investment signal.

For each dimension, ask:

> Would this materially influence whether we progress, investigate, invest or park an opportunity?

Remove dimensions that do not improve the decision.

Do not add numerical weighting unless the group agrees it is necessary.

## Agreed viability dimensions

| Dimension            | Keep / change / remove | Reason |
| -------------------- | ---------------------- | ------ |
| Customer value       |                        |        |
| Operational value    |                        |        |
| Risk reduction       |                        |        |
| Evidence strength    |                        |        |
| Strategic fit        |                        |        |
| Organisational fit   |                        |        |
| Capability readiness |                        |        |
| Complexity           |                        |        |
| Dependencies         |                        |        |
| Investment signal    |                        |        |

## Select first opportunities

The initial recommendation is to start with:

1. `CAM-OPP-001` — customer identity and Service Account linking;
2. `CAM-OPP-002` — duplicate prevention and safe resolution; and
3. `CAM-OPP-003` — deceased-customer handling.

These are starting candidates, not predetermined priorities.

Ask:

> Which two or three opportunities would benefit most from external evidence before we make a prioritisation decision?

## Opportunity selection record

| Opportunity                                                 | Include in first assessment? | Reason | Evidence gap |
| ----------------------------------------------------------- | ---------------------------- | ------ | ------------ |
| CAM-OPP-001 — Customer identity and Service Account linking |                              |        |              |
| CAM-OPP-002 — Duplicate prevention and safe resolution      |                              |        |              |
| CAM-OPP-003 — Deceased-customer handling                    |                              |        |              |
| CAM-OPP-004 — Information removal and restriction           |                              |        |              |
| CAM-OPP-005 — Central customer record opt-out               |                              |        |              |
| CAM-OPP-006 — Customer authentication                       |                              |        |              |

## Desktop-scan evidence standard

For each external example, capture:

| Field                | Requirement                            |
| -------------------- | -------------------------------------- |
| Source               | Where the evidence came from           |
| Organisation         | Organisation or use case               |
| Context              | Relevant operating context             |
| Question addressed   | Which agreed question it informs       |
| Practice             | What appears to be done                |
| Evidence of outcome  | What value or result is reported       |
| Evidence strength    | Strong / Moderate / Weak               |
| Transferability      | High / Medium / Low                    |
| Interpretation       | What it may mean for City of Melbourne |
| Caveat               | What cannot be concluded               |
| Opportunity affected | Relevant CAM-OPP ID                    |

Separate:

* source evidence;
* interpretation;
* assumption; and
* recommendation.

## What the scan should not become

Do not turn the activity into:

* an exhaustive market scan;
* a technology comparison;
* a vendor assessment;
* a maturity-model exercise;
* a generic collection of best practices;
* evidence that City of Melbourne must copy another organisation; or
* a business case before the problem and value are sufficiently evidenced.

Stop when there is enough evidence to improve the prioritisation decision.

## Playback format

For each priority opportunity, summarise the scan in one view:

### Opportunity

What are we considering?

### Internal evidence

What do we know about our context?

### External evidence

What relevant practice did we find?

### Transferability

What appears applicable and what does not?

### Viability implication

Does the evidence strengthen, weaken or leave the opportunity unchanged?

### Decision

* Progress
* Investigate further
* Escalate for investment assessment
* Park

### Evidence still required

What is missing before the next decision?

## Decisions to record

At the end of the session, record:

| Decision                       | Outcome | Owner |
| ------------------------------ | ------- | ----- |
| Desktop-scan questions agreed  |         |       |
| External examples selected     |         |       |
| Viability dimensions confirmed |         |       |
| First opportunities selected   |         |       |
| Research owners assigned       |         |       |
| Playback date agreed           |         |       |

Material decisions should also be added to:

`06-decisions/decision-log.md`

## Completion criteria

This Define review is complete when:

* the decision purpose is understood;
* the group agrees what it needs to learn;
* the first scan questions are prioritised;
* external examples are selected intentionally;
* viability dimensions are agreed;
* the first opportunities are selected;
* research ownership is clear; and
* a playback date is agreed.

## Next action

Complete the desktop scan against the agreed questions.

Do not add new repository structure unless conducting the scan demonstrates that the existing Define pages cannot hold the evidence clearly.

## Review notes

<!-- AUTO-REVIEW-NOTES:START -->

| Date | Update | Updated by | Commit |
| ---- | ------ | ---------- | ------ |

<!-- AUTO-REVIEW-NOTES:END -->
