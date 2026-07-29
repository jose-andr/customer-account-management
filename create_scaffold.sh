#!/usr/bin/env bash

set -euo pipefail

# Customer Account Management repository scaffold
# Run from the root of:
# jose-andr/customer-account-management

EXPECTED_REPO="customer-account-management"

CURRENT_REPO="$(basename "$(git rev-parse --show-toplevel)")"

if [[ "$CURRENT_REPO" != "$EXPECTED_REPO" ]]; then
  echo "Error: run this script from the $EXPECTED_REPO repository."
  echo "Current repository: $CURRENT_REPO"
  exit 1
fi

cd "$(git rev-parse --show-toplevel)"

echo "Updating the local main branch..."
git pull --ff-only origin main

echo "Creating repository folders..."

mkdir -p \
  00-project-control \
  01-discover/research \
  02-define \
  03-design/prototypes-and-tests \
  04-deliver/implementation-plans \
  04-deliver/change-and-adoption \
  04-deliver/handover-and-controls \
  04-deliver/delivery-reviews \
  05-evaluation-and-learning \
  06-decisions/records \
  07-templates \
  references

create_page() {
  local path="$1"
  local title="$2"
  local purpose="$3"

  if [[ -e "$path" ]]; then
    echo "Skipping existing file: $path"
    return
  fi

  cat > "$path" <<EOF
# $title

Status: Draft  
Owner: José Andrade  
Last updated: 29 July 2026

## Purpose

$purpose

## Current position

Not yet documented.

## Evidence

No evidence recorded yet.

## Decisions

No decisions recorded yet.

## Open questions

- What needs to be confirmed?
- Who needs to be involved?
- What evidence is still required?

## Next action

Define the smallest useful next step.
EOF

  echo "Created: $path"
}

echo "Creating project-control pages..."

create_page \
  "00-project-control/repository-structure.md" \
  "Repository structure" \
  "Define how the Customer Account Management repository is organised and how the 4D activity model is used."

create_page \
  "00-project-control/purpose-and-scope.md" \
  "Purpose and scope" \
  "Define the purpose, boundaries, intended outcomes and exclusions for the Customer Account Management workstream."

create_page \
  "00-project-control/ways-of-working.md" \
  "Ways of working" \
  "Define how evidence, decisions, delivery activity and stakeholder input will be managed."

create_page \
  "00-project-control/status-and-validation-model.md" \
  "Status and validation model" \
  "Define the status labels used to distinguish draft, reported, aligned, validated and superseded content."

create_page \
  "00-project-control/stakeholder-map.md" \
  "Stakeholder map" \
  "Record the people, roles and groups involved in Customer Account Management."

create_page \
  "00-project-control/assumptions-log.md" \
  "Assumptions log" \
  "Track assumptions that require evidence, validation or a decision."

create_page \
  "00-project-control/risk-register.md" \
  "Risk register" \
  "Track risks, impacts, controls, owners and mitigation actions."

create_page \
  "00-project-control/glossary.md" \
  "Glossary" \
  "Define key Customer Account Management, CRM, customer data and service-design terms."

echo "Creating Discover pages..."

create_page \
  "01-discover/discovery-overview.md" \
  "Discover overview" \
  "Summarise the discovery purpose, current status, evidence sources, findings and gaps."

create_page \
  "01-discover/existing-evidence-inventory.md" \
  "Existing evidence inventory" \
  "Record existing research, workshop outputs, repositories, documents and operational evidence."

create_page \
  "01-discover/customer-needs-and-pain-points.md" \
  "Customer needs and pain points" \
  "Document de-identified customer needs, pain points, use cases and experience impacts."

create_page \
  "01-discover/employee-needs-and-pain-points.md" \
  "Employee needs and pain points" \
  "Document staff tasks, pain points, workarounds and information needs."

create_page \
  "01-discover/operational-and-system-context.md" \
  "Operational and system context" \
  "Describe the current operational environment, systems, dependencies and constraints."

create_page \
  "01-discover/current-state-evidence-synthesis.md" \
  "Current-state evidence synthesis" \
  "Synthesise current-state evidence without duplicating the source SOP repository."

create_page \
  "01-discover/evidence-gaps.md" \
  "Evidence gaps" \
  "Track missing evidence, unresolved questions and validation needs."

echo "Creating Define pages..."

create_page \
  "02-define/definition-overview.md" \
  "Define overview" \
  "Summarise the current problem framing, scope, outcomes, principles and decisions."

create_page \
  "02-define/problem-statement.md" \
  "Problem statement" \
  "Record the aligned draft Customer Account Management problem statement and its evidence basis."

create_page \
  "02-define/problem-boundaries.md" \
  "Problem boundaries" \
  "Define what is included, excluded and adjacent to the Customer Account Management problem."

create_page \
  "02-define/outcomes-and-value.md" \
  "Outcomes and value" \
  "Define intended customer, employee, operational and organisational outcomes."

create_page \
  "02-define/design-principles.md" \
  "Design principles" \
  "Define the principles that future Customer Account Management options must satisfy."

create_page \
  "02-define/success-measures.md" \
  "Success measures" \
  "Define baseline, outcome and diagnostic measures with clear caveats."

create_page \
  "02-define/prioritised-opportunities.md" \
  "Prioritised opportunities" \
  "Record and prioritise transformation opportunities supported by discovery evidence."

create_page \
  "02-define/definition-review.md" \
  "Definition review" \
  "Record whether the problem, scope, outcomes and measures are ready to move into design."

echo "Creating Design pages..."

create_page \
  "03-design/design-overview.md" \
  "Design overview" \
  "Summarise future-state design activity, options, tests and decisions."

create_page \
  "03-design/future-state-concepts.md" \
  "Future-state concepts" \
  "Record future-state concepts as options until they are tested and approved."

create_page \
  "03-design/customer-account-model.md" \
  "Customer account model" \
  "Define and test possible customer identity, relationship and account lifecycle models."

create_page \
  "03-design/operating-model-options.md" \
  "Operating model options" \
  "Compare possible ownership, service, capability and operating-model arrangements."

create_page \
  "03-design/governance-options.md" \
  "Governance options" \
  "Compare possible decision rights, standards, controls and ownership models."

create_page \
  "03-design/service-and-process-patterns.md" \
  "Service and process patterns" \
  "Document reusable account-management and customer-information design patterns."

create_page \
  "03-design/design-review.md" \
  "Design review" \
  "Assess whether proposed designs are desirable, feasible, viable and ready for delivery."

echo "Creating Deliver pages..."

create_page \
  "04-deliver/delivery-overview.md" \
  "Deliver overview" \
  "Summarise active implementation, pilot, change and handover activity."

create_page \
  "04-deliver/initiative-register.md" \
  "Initiative register" \
  "Track initiatives contributing to Customer Account Management transformation."

create_page \
  "04-deliver/experiment-register.md" \
  "Experiment register" \
  "Track pilots and experiments, including hypotheses, measures, results and decisions."

echo "Creating evaluation and learning pages..."

create_page \
  "05-evaluation-and-learning/evaluation-overview.md" \
  "Evaluation overview" \
  "Define how outcomes, unintended consequences and learning will be evaluated."

create_page \
  "05-evaluation-and-learning/baseline-measures.md" \
  "Baseline measures" \
  "Record validated baselines and caveats before interventions begin."

create_page \
  "05-evaluation-and-learning/outcome-reviews.md" \
  "Outcome reviews" \
  "Record observed results and decisions to scale, revise, pause or stop."

create_page \
  "05-evaluation-and-learning/lessons-learned.md" \
  "Lessons learned" \
  "Capture reusable lessons from discovery, design, delivery and evaluation."

create_page \
  "05-evaluation-and-learning/iteration-backlog.md" \
  "Iteration backlog" \
  "Track evidence-based improvements for future work."

create_page \
  "05-evaluation-and-learning/reusable-patterns.md" \
  "Reusable patterns" \
  "Record validated patterns that can be applied across future services and initiatives."

echo "Creating decision log..."

if [[ ! -e "06-decisions/decision-log.md" ]]; then
  cat > "06-decisions/decision-log.md" <<'EOF'
# Decision log

| ID | Date | Decision | Rationale | Evidence | Owner | Status |
|---|---|---|---|---|---|---|
| DEC-001 | 29 July 2026 | Use a 4D structure for the repository | Supports traceable discovery, definition, design, delivery and learning | Initial project direction | José Andrade | Draft |
EOF

  echo "Created: 06-decisions/decision-log.md"
else
  echo "Skipping existing file: 06-decisions/decision-log.md"
fi

echo "Creating templates..."

if [[ ! -e "07-templates/discover-template.md" ]]; then
  cat > "07-templates/discover-template.md" <<'EOF'
# Discover: [Activity name]

Status: Draft  
Owner:  
Date:

## Question

What are we trying to understand?

## Evidence

## Findings

## Assumptions

## Evidence gaps

## Implications

## Next decision
EOF
fi

if [[ ! -e "07-templates/define-template.md" ]]; then
  cat > "07-templates/define-template.md" <<'EOF'
# Define: [Activity name]

Status: Draft  
Owner:  
Date:

## Problem

## Who is affected

## Evidence

## Scope

## Out of scope

## Intended outcomes

## Success measures

## Open questions

## Definition decision
EOF
fi

if [[ ! -e "07-templates/design-template.md" ]]; then
  cat > "07-templates/design-template.md" <<'EOF'
# Design: [Concept name]

Status: Draft  
Owner:  
Date:

## Opportunity

## Concept

## Evidence used

## Customer value

## Employee value

## Operational value

## Risks and constraints

## Test approach

## Decision
EOF
fi

if [[ ! -e "07-templates/deliver-template.md" ]]; then
  cat > "07-templates/deliver-template.md" <<'EOF'
# Deliver: [Initiative name]

Status: Draft  
Owner:  
Date:

## Change being delivered

## Problem addressed

## Intended outcome

## Scope

## Delivery approach

## Measures

## Risks

## Handover

## Outcome
EOF
fi

if [[ ! -e "07-templates/evidence-record-template.md" ]]; then
  cat > "07-templates/evidence-record-template.md" <<'EOF'
# Evidence record: [Title]

Status: Draft  
Evidence type:  
Source:  
Date collected:  
Recorded by:

## Summary

## Relevant finding

## Caveats

## Interpretation

## Decision relevance

## Source location
EOF
fi

if [[ ! -e "07-templates/problem-statement-template.md" ]]; then
  cat > "07-templates/problem-statement-template.md" <<'EOF'
# Problem statement

Status: Draft

## Problem

[Who] needs [need] because [evidence-based insight].

## Impact

## Evidence

## Scope

## Out of scope

## Assumptions

## Validation status
EOF
fi

if [[ ! -e "07-templates/decision-record-template.md" ]]; then
  cat > "07-templates/decision-record-template.md" <<'EOF'
# Decision: [Title]

Decision ID:  
Status: Draft  
Date:  
Owner:

## Decision

## Context

## Options considered

## Evidence

## Rationale

## Consequences

## Follow-up actions
EOF
fi

if [[ ! -e "07-templates/experiment-template.md" ]]; then
  cat > "07-templates/experiment-template.md" <<'EOF'
# Experiment: [Title]

Status: Draft  
Owner:  
Start date:  
End date:

## Hypothesis

## Change being tested

## Participants or context

## Measures

## Baseline

## Result

## Caveats

## Decision

Scale / Revise / Pause / Stop
EOF
fi

if [[ ! -e "07-templates/outcome-review-template.md" ]]; then
  cat > "07-templates/outcome-review-template.md" <<'EOF'
# Outcome review: [Initiative]

Status: Draft  
Review date:  
Owner:

## Original problem

## Intended outcome

## Baseline

## Change delivered

## Evidence collected

## Observed outcome

## Unintended consequences

## Caveats

## Decision

Scale / Revise / Pause / Stop

## Reusable learning
EOF
fi

echo "Creating reference pages..."

if [[ ! -e "references/source-register.md" ]]; then
  cat > "references/source-register.md" <<'EOF'
# Source register

| Source ID | Source | Type | Purpose | System of record | Status |
|---|---|---|---|---|---|
| SRC-001 | `jose-andr/cx-current-state-sop-mapping` | GitHub repository | Current-state operational evidence | GitHub | Active input |
EOF
fi

if [[ ! -e "references/related-repositories.md" ]]; then
  cat > "references/related-repositories.md" <<'EOF'
# Related repositories

## `jose-andr/cx-current-state-sop-mapping`

### Purpose

Documents actual current Customer Data and Systems Support operational practices.

### Relationship

This repository is an evidence input to Customer Account Management discovery and definition work.

### Boundary

Do not duplicate current-state SOP content.

Reference the relevant source file, finding or validation status.
EOF
fi

echo "Preserving empty working folders..."

touch \
  01-discover/research/.gitkeep \
  03-design/prototypes-and-tests/.gitkeep \
  04-deliver/implementation-plans/.gitkeep \
  04-deliver/change-and-adoption/.gitkeep \
  04-deliver/handover-and-controls/.gitkeep \
  04-deliver/delivery-reviews/.gitkeep \
  06-decisions/records/.gitkeep

echo
echo "Reviewing generated changes..."
git status --short

if git diff --quiet && git diff --cached --quiet && [[ -z "$(git ls-files --others --exclude-standard)" ]]; then
  echo "No new changes were created."
  exit 0
fi

git add .

git commit -m "Add Customer Account Management 4D repository scaffold"

git push origin HEAD:main

echo
echo "Repository scaffold created and pushed successfully."