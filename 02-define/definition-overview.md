# Define overview

Status: Draft
Owner: José Andrade
Last updated: 13 August 2026

## Purpose

Define which Customer Account Management improvements are sufficiently valuable, viable and evidence-supported to progress into design, testing or a future investment case.

The Define phase converts discovery evidence into clearer decision options.

It does not assume that:

* a single customer record is the required solution;
* additional technology investment is required;
* Databricks, Salesforce, Plauti or another platform is the answer;
* every identified issue should progress;
* practices used by other organisations are directly transferable; or
* a business case has already been established.

## North star — viability

The current North Star for Define is:

> Assess the viability of improvements to Customer Account Management and potential future investment at City of Melbourne, using evidence to support prioritisation and business-case decisions.

For this work, viability means understanding whether an improvement is:

* addressing a meaningful customer or operational problem;
* supported by credible evidence;
* strategically relevant;
* achievable within organisational constraints;
* proportionate to the risk or opportunity;
* dependent on capabilities that already exist or require investment;
* likely to create sufficient value to justify further work; and
* suitable to progress into design, experimentation or business-case development.

Viability is not a financial business case by itself.

The purpose of this phase is to create enough evidence to decide where deeper investment analysis is warranted.

## Current position

Discovery has identified recurring Customer Account Management issues including:

* duplicate and fragmented customer records;
* customer identity and account-linking concerns;
* inconsistent customer-data quality;
* unresolved account-management processes;
* governance and ownership gaps;
* manual remediation effort; and
* risks created by inconsistent customer information across systems.

The repository also contains emerging Databricks data-quality work and a prioritised initiative backlog.

The next Define task is to assess these issues against external practice and organisational context so that prioritisation is based on more than internal pain points alone.

## Define decision

The central decision is:

> Which Customer Account Management improvements should City of Melbourne investigate or invest in next, based on customer value, operational value, risk reduction, strategic fit and evidence of viable practice?

Supporting decisions include:

1. Which problems are important enough to justify further investment?
2. Which capabilities appear necessary regardless of technology?
3. Which capabilities already exist and need improvement rather than replacement?
4. Which opportunities should move into Design?
5. Which opportunities require additional evidence before progressing?
6. Which opportunities should be parked?
7. Where might a future business case be justified?

## Define activity — Customer Account Management desktop scan

### Purpose

Conduct a focused desktop scan of comparable Customer Account Management practices to help the working group understand what good practice can look like and use that evidence to support prioritisation decisions.

The scan is not intended to produce a generic best-practice report.

It should answer specific questions relevant to City of Melbourne decisions.

### Step 1 — agree the questions

Before researching external examples, the working group should agree:

> What are the most important things we need to learn from other organisations to make better Customer Account Management prioritisation decisions?

Initial question areas are below.

| Question area        | What we want to learn                                                                                             | Why it matters                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Customer identity    | How do organisations establish and maintain confidence that records relate to the correct person or organisation? | Supports decisions about account linking, authentication and duplicate management |
| Account model        | How are individual, organisation, household, representative or statutory relationships handled?                   | Helps test whether current account structures support customer needs              |
| Duplicate prevention | What controls reduce duplicate creation upstream?                                                                 | Distinguishes prevention from downstream cleansing                                |
| Duplicate resolution | How are potential duplicates reviewed, confirmed and safely resolved?                                             | Supports operating-model and control decisions                                    |
| Customer preferences | How are contact preferences, restrictions, opt-outs and special handling represented?                             | Supports privacy-safe and consistent account management                           |
| Deceased customers   | How do organisations manage deceased status across systems and communications?                                    | Tests approaches to a known high-risk issue                                       |
| Data quality         | Which customer-data standards are monitored and who acts when records fail?                                       | Supports Databricks and operational-control decisions                             |
| Ownership            | Who owns customer-account quality and the ongoing improvement backlog?                                            | Tests operating-model viability                                                   |
| Governance           | How are privacy, records, security and data ownership translated into operational rules?                          | Identifies capabilities needed beyond technology                                  |
| Measures             | How do organisations demonstrate that account-management improvements create value?                               | Supports prioritisation and future business cases                                 |
| Investment           | What capabilities required dedicated investment versus process or governance improvement?                         | Helps distinguish improvement from transformation                                 |

The working group should refine this list before the scan begins.

## Scan approach

Use a small number of relevant examples rather than attempting an exhaustive benchmark.

Potential examples may include:

* government organisations;
* organisations managing complex statutory and non-statutory customer relationships;
* organisations with high privacy or identity requirements;
* utilities or service providers with persistent customer-account relationships; and
* organisations with mature customer-master or CRM practices.

State Trustees has been suggested as one potential use case for investigation.

Its relevance should be assessed against the agreed questions rather than assumed.

## Evidence capture

For each external example, record:

| Field                         | What to capture                                    |
| ----------------------------- | -------------------------------------------------- |
| Organisation                  | Organisation or published example                  |
| Context                       | Why the example may be relevant                    |
| Customer-account problem      | Problem the organisation was addressing            |
| Practice or capability        | What it does                                       |
| Operating ownership           | Who appears responsible                            |
| Technology role               | What technology enables the practice               |
| Governance role               | Relevant controls or standards                     |
| Evidence of value             | Reported benefit or outcome                        |
| Evidence strength             | Published evidence, reported practice or inference |
| Transferability               | High / Medium / Low                                |
| City of Melbourne implication | What the example suggests for this work            |
| Caveat                        | What cannot safely be concluded                    |

Do not copy raw organisational data or copyrighted source material into the repository.

Record summaries, references, interpretation and caveats.

## Viability assessment

External practices should not automatically become recommendations.

Each potential improvement should ultimately be assessed against:

| Dimension            | Question                                                                               |
| -------------------- | -------------------------------------------------------------------------------------- |
| Customer value       | Would this materially improve customer experience, trust, continuity or accessibility? |
| Operational value    | Would this reduce avoidable effort, rework or uncertainty?                             |
| Risk reduction       | Would this materially reduce privacy, data, service or governance risk?                |
| Evidence             | Is the underlying problem sufficiently supported?                                      |
| Strategic fit        | Does it support the intended Customer Account Management direction?                    |
| Organisational fit   | Can it work within City of Melbourne's operating environment?                          |
| Capability readiness | Do the required people, processes, governance and technology exist?                    |
| Complexity           | How difficult would it be to introduce safely?                                         |
| Dependency           | What other decisions or capabilities are required first?                               |
| Investment signal    | Does the opportunity appear significant enough to justify deeper investment analysis?  |

Do not create a numerical score until the working group agrees that weighting the dimensions would improve the decision.

## Expected output

The Define activity should produce a short evidence-based position for each priority opportunity:

**Progress**

Evidence and viability are sufficient to move into Design or controlled testing.

**Investigate further**

The opportunity appears important but requires additional evidence before a design or investment decision.

**Park**

Current evidence or viability does not justify further work at this stage.

**Escalate for investment assessment**

The opportunity may require material organisational investment and has enough evidence to justify deeper business-case analysis.

## Relationship to repository pages

Use existing pages rather than create parallel documentation.

* `01-discover/existing-evidence-inventory.md` — internal evidence already available
* `01-discover/databricks-customer-data-quality-pilot-input.md` — analytical evidence and diagnostic questions
* `02-define/problem-statement.md` — agreed problem framing
* `02-define/outcomes-and-value.md` — value expected from improvement
* `02-define/prioritised-opportunities.md` — opportunities and viability decisions
* `02-define/success-measures.md` — evidence required to demonstrate value
* `04-deliver/initiative-register.md` — reported initiatives and delivery backlog

The desktop scan should inform these pages rather than become a separate strategy document unless repeated use shows that a dedicated evidence artefact is necessary.

## Evidence status

Current external benchmark evidence: Not yet gathered.

Current viability assessment: Not yet completed.

Current investment recommendation: None.

## Open questions

* Which three to five questions are most important for the first desktop scan?
* Which organisations provide genuinely comparable examples?
* What evidence would materially change a prioritisation decision?
* Which current initiatives should be assessed first?
* Which viability dimensions should be treated as mandatory?
* What threshold would justify deeper business-case work?
* Who needs to participate in the prioritisation decision?

## Next action

Run a short working-group session to agree the key questions for the desktop scan before collecting external examples.

The output of that session should be:

1. an agreed set of research questions;
2. three to five priority organisations or examples to investigate;
3. agreed viability dimensions;
4. the first Customer Account Management opportunities to assess; and
5. ownership for completing the scan.

## Review notes

<!-- AUTO-REVIEW-NOTES:START -->

| Date | Update | Updated by | Commit |
| ---- | ------ | ---------- | ------ |

<!-- AUTO-REVIEW-NOTES:END -->
