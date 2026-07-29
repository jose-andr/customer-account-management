# Problem statement

Status: Aligned draft  
Owner: José Andrade  
Current stage: Define  
Last updated: 29 July 2026

## Aligned draft problem statement

The City of Melbourne cannot reliably identify a single, accurate view of each customer due to duplicated accounts, inconsistent classifications and fragmented customer information across systems.

This creates avoidable effort for staff, reduces confidence in customer records and can contribute to inconsistent or fragmented customer experiences.

## Validation status

This problem statement has been aligned in draft between:

- the Customer Focus and Strategy Manager;
- the CRM Product Owner; and
- the Customer Data and Systems Support Officer.

It is suitable as the current working problem statement.

It is not yet:

- validated across all relevant business areas;
- supported by a complete organisation-wide evidence base;
- formally endorsed as policy;
- an approved technology requirement; or
- confirmation that a single technical master record is the required solution.

## Problem context

The initial discovery identified recurring signals that:

- duplicate accounts create avoidable friction;
- the current account model may not reflect the full customer relationship;
- customer information is captured differently across systems;
- statutory, non-statutory and organisation accounts are classified and managed differently;
- staff may need to search, validate or reconcile records manually;
- customers may need to repeat information;
- customers may hold multiple accounts across different services or systems;
- ownership of customer accounts and information may be unclear;
- some customer relationships, such as families, representatives, minors and organisations, are not consistently represented; and
- account quality directly affects staff confidence in service delivery.

These remain working evidence signals until their scale, frequency and impact are validated.

## Who experiences the problem

### Customers

Customers may experience:

- repeated requests for information;
- inconsistent communications;
- difficulty updating or managing their details;
- fragmented account or service histories;
- unclear relationships between accounts, permits, requests and payments;
- reduced confidence that the organisation recognises their circumstances; and
- additional effort when using multiple services.

### Employees

Employees may experience:

- difficulty locating the correct customer record;
- uncertainty about whether records relate to the same person or organisation;
- manual duplicate investigation and correction;
- repeated validation and reconciliation work;
- unclear ownership and escalation pathways;
- inconsistent business rules;
- limited confidence in account data; and
- difficulty supporting customers across multiple services.

### The organisation

The organisation may experience:

- avoidable operational effort;
- inconsistent reporting;
- weak confidence in customer counts and classifications;
- recurring data-quality remediation;
- increased privacy, records and service risks;
- reduced readiness for connected customer interactions;
- increased complexity in CRM, digital and integration changes; and
- reduced ability to evaluate customer outcomes across services.

## Problem boundaries

The current problem statement focuses on:

- known customers;
- customer accounts;
- customer identity and classification;
- duplicate and inconsistent records;
- customer information linked to accounts;
- account creation and update processes;
- staff confidence in customer records;
- relationships between customers, services, permits, requests and payments; and
- the operational and service impacts of unreliable account information.

The wider topic of customer data management includes:

- anonymous interactions;
- website behaviour;
- customer analytics;
- segmentation;
- personalisation;
- consent and preferences;
- off-platform behaviour; and
- broader enterprise data management.

These areas are adjacent but are not automatically included in the initial Customer Account Management problem scope.

## Supporting evidence

Initial supporting evidence includes:

- reported duplicate-account handling;
- manual record investigation and merging;
- customer records spread across multiple systems;
- inconsistent field and classification practices;
- reported difficulty identifying the correct customer;
- reported uncertainty about account ownership;
- reported limitations in representing organisations, families, minors and representatives;
- manual transfer or correction of account-linked information;
- workshop-generated customer and employee use cases; and
- current-state Customer Data and Systems Support SOP evidence.

The current-state operational repository is:

`jose-andr/cx-current-state-sop-mapping`

That repository remains the source for detailed current operational practice.

This repository should reference, not duplicate, that evidence.

## Evidence gaps

The following still require further validation:

- the volume and rate of duplicate accounts;
- the main causes of duplicate creation;
- which systems and processes create the greatest risk;
- the proportion of records affected by inconsistent classification;
- the amount of staff time spent searching, correcting and reconciling records;
- the customer effort caused by account fragmentation;
- the services most affected;
- the frequency of incorrect or inconsistent communications;
- the level of reporting impact;
- the privacy, records and security implications;
- differences between statutory, non-statutory and organisation accounts;
- the effect on self-service completion;
- the effect on service resolution and repeat contact; and
- the organisational cost of maintaining the current state.

## Assumptions

The current problem framing includes the following assumptions:

| ID | Assumption | Status |
|---|---|---|
| ASM-001 | Duplicate and inconsistent accounts materially affect customer and employee experience | Partially validated |
| ASM-002 | Current classifications do not adequately represent all customer relationships | Reported |
| ASM-003 | Fragmented customer information increases manual operational effort | Partially validated |
| ASM-004 | Improving account quality would support more connected customer interactions | Future signal |
| ASM-005 | Some account problems are caused by upstream process and system design rather than isolated data-cleaning issues | Reported |
| ASM-006 | Greater consistency in customer information practices would improve service confidence | Future signal |

## Proposed solutions that are not yet confirmed

The following ideas appeared during discovery but must remain outside the problem statement until separately evaluated:

- creating a master customer ID;
- creating a single physical customer record;
- implementing new duplicate-detection technology;
- introducing a dedicated customer-account function;
- changing CRM account structures;
- creating organisation-wide customer-information standards;
- establishing new governance bodies;
- automating record merging;
- introducing family or representative accounts;
- creating new organisation-account models; and
- consolidating customer information across all systems.

These are potential responses, not validated requirements.

## Problem statement test

The problem statement should remain:

- broad enough to allow multiple design responses;
- specific enough to guide further evidence collection;
- neutral about technology;
- separate from proposed organisational structures;
- grounded in customer, employee and operational impacts;
- clear about current uncertainty; and
- safe to use in stakeholder alignment discussions.

## Current decision

Use the aligned draft problem statement as the working definition for continued Discover and Define activity.

Do not progress it as an approved enterprise requirement until:

- supporting evidence is consolidated;
- the scope is reviewed with relevant stakeholders;
- key assumptions are tested;
- problem impacts are prioritised; and
- adjacent customer-data topics are explicitly included or excluded.

## Next action

Validate the problem statement against:

1. current-state SOP evidence;
2. customer and employee use cases;
3. available account-quality measures;
4. affected service owners; and
5. privacy, records, security and data-governance perspectives.
