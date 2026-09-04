# Grade 11 Adaptive Socratic Tutor

## Implementation Specification

**Version:** 1.1.0
**Execution model:** One phase at a time
**Required reading:** `SYSTEM_SPEC.md`, `AGENTS.md`, `RUN_LOG_SPEC.md`, `CORPUS_SUFFICIENCY_POLICY.md`

> **v1.1.0 revision.** §4 (Phase 3) is rewritten: acquisition is now a
> **form-stratified saturation sample** rather than blanket collection of every
> discovered source, and it is split into *selection* (3a) and *acquisition*
> (3b). §23 records that all six subjects may be processed in one run when
> explicitly requested. The authoritative rationale, evidence and known gaps are
> in [`CORPUS_SUFFICIENCY_POLICY.md`](CORPUS_SUFFICIENCY_POLICY.md).

---

# 0. Execution rule

This specification is divided into phases.

The agent must execute **only the phase explicitly requested by the user**.

A phase may create prerequisites for later phases.

The agent must not automatically continue into a later phase.

At the end of a phase:

1. validate its own work
2. write all artifacts to the repository
3. write the run log
4. write the decision log
5. update status
6. report completion and unresolved issues
7. stop

---

# 1. Target repository structure

The final repository should contain approximately:

```text
/
├── SYSTEM_SPEC.md
├── IMPLEMENTATION_SPEC.md
├── AGENTS.md
├── RUN_LOG_SPEC.md
├── README.md
├── STATUS.md
│
├── data/
│   ├── raw/
│   │   ├── biology/
│   │   ├── physics/
│   │   ├── history/
│   │   ├── english/
│   │   ├── ap_mathematics/
│   │   └── mathematics/
│   │
│   ├── extracted/
│   ├── structured/
│   └── validated/
│
├── knowledge/
│   ├── biology/
│   ├── physics/
│   ├── history/
│   ├── english/
│   ├── ap_mathematics/
│   └── mathematics/
│
├── database/
│   ├── schema/
│   ├── migrations/
│   ├── seed/
│   └── knowledge.db
│
├── ingestion/
│   ├── acquisition/
│   ├── extraction/
│   ├── segmentation/
│   ├── classification/
│   ├── analysis/
│   └── validation/
│
├── tutor/
│   ├── core/
│   ├── prompts/
│   └── subjects/
│       ├── biology/
│       ├── physics/
│       ├── history/
│       ├── english/
│       ├── ap_mathematics/
│       └── mathematics/
│
├── student_model/
│
├── tests/
│
└── runs/
```

The implementation may add directories where necessary, but must not discard required provenance or raw source material.

---

# 2. Phase 1 — Repository bootstrap

## Objective

Establish the repository structure, configuration, schemas, logging framework and basic documentation.

## Tasks

Create:

* directory structure
* `README.md`
* `STATUS.md`
* base configuration
* run logging framework
* decision logging framework
* source metadata schema
* question schema
* knowledge-model schema
* validation schema
* tests for schemas

Do not collect or analyse curriculum material yet.

## Deliverables

```text
README.md
STATUS.md
database/schema/
ingestion/
tests/
runs/
```

## Validation

Confirm that:

* repository structure exists
* schemas validate
* a test run can be created
* a decision can be logged
* all files are committed if Git is available

## Hard rules

* Do not analyse source material.
* Do not invent curriculum content.
* Do not create fabricated subject knowledge.
* Do not proceed to Phase 2 automatically.

---

# 3. Phase 2 — ORC source discovery

## Objective

Build the authoritative source inventory for all six subjects.

Subjects:

```text
biology
physics
history
english
ap_mathematics
mathematics
```

Primary source:

St Benedict's Online Resource Centre.

Base source:

`https://sites.google.com/stbenedicts.co.za/orc`

## Tasks

For each subject:

1. locate the ORC subject page
2. inspect its embedded resources
3. identify Grade 11 material
4. identify past papers
5. identify memoranda
6. identify rubrics / marking guides
7. identify curriculum / syllabus references
8. identify relevant supporting assessment material
9. record all discovered sources
10. distinguish accessible sources from inaccessible sources

Do not analyse the educational content yet.

## Deliverable

Create:

```text
data/raw/CORPUS_MANIFEST.yaml
```

and subject inventories under:

```text
data/raw/<subject>/SOURCE_INVENTORY.yaml
```

## Each source record must include

```yaml
source_id:
subject:
grade:
document_type:
title:
year:
term:
paper_number:
source_url:
retrieved_at:
access_status:
local_path:
file_hash:
notes:
```

## Hard rules

* ORC is the primary source boundary.
* Do not silently substitute another curriculum.
* External sources may be used only to resolve technical access problems or explicitly authorised gaps.
* Every external source must be marked as external.
* Do not claim the corpus is complete unless the inventory supports that claim.
* Do not infer missing papers.
* Record unavailable resources explicitly.

---

# 4. Phase 3 — Select, acquire and preserve the source corpus

Governed by [`CORPUS_SUFFICIENCY_POLICY.md`](CORPUS_SUFFICIENCY_POLICY.md), which
is authoritative for this phase and for Phase 4.

## Objective (v1.1.0)

Acquire the **minimum authoritative corpus that saturates the question taxonomy
and the Understanding Models** — not the maximum corpus that covers the syllabus.

This replaces the v1.0.0 objective ("download/copy every accessible
authoritative source identified in Phase 2", 821 records). The change is
recorded as decision `DEC-P3-SEL-001` and requires human sign-off via
`review_queue/RQ-P3-CORPUS-SELECTION.yaml`.

Phase 3 is split in two.

## Phase 3a — Select the corpus

Determine *which* documents to acquire, before acquiring any.

### Tasks

1. read the six Phase 2 inventories (read-only; they are discovery provenance)
2. classify every past paper into an assessment-form stratum
   `setter × paper_form × session`, deriving `paper_form` per
   *(subject, setter)* pair from the corpus rather than assuming it
3. exclude out-of-scope records (other subjects, other grades, Chemistry held in
   the Physical Sciences folder)
4. allocate the per-subject budget in two passes — coverage (one exemplar per
   stratum), then depth (a second, older exemplar for the largest strata)
5. pair every selected paper with its memorandum / marking guide, treating memo
   availability as a *ranking* criterion
6. attach companion documents without which the paper cannot be answered
   (source booklets, data sheets, diagram booklets, answer sheets)
7. attach authoritative curriculum anchors where the ORC holds any
8. record every stratum left unsampled, with justification

### Deliverables

```text
data/raw/CORPUS_SELECTION.yaml
data/raw/DOWNLOAD_CHECKLIST.md
review_queue/RQ-P3-CORPUS-SELECTION.yaml
```

### Driver

```bash
python3 scripts/phase3_select.py
```

Deterministic: the same inventories and budget always produce the same sample.

## Phase 3b — Acquire and preserve

### Tasks

For each document in the selection:

1. acquire the file, recording which **fidelity rung** it occupies
   (`SYSTEM_SPEC.md` §17.2: A = original bytes, B = faithful transcription,
   C = metadata only)
2. preserve the original filename
3. calculate a cryptographic hash — of the original bytes at Rung A, of the
   transcription at Rung B, and record which
4. store it under the appropriate subject directory
5. record metadata against the existing `source_id`
6. detect duplicates **by content hash, not by file ID** — Phase 2 deduplicated
   on Drive file ID only, and the same paper is demonstrably present under
   multiple IDs and multiple naming schemes
7. verify `document_type` **from content**, not from Phase 2 metadata — at least
   one record labelled `past_paper` is in fact a memorandum
8. identify unreadable or corrupt files
9. flag every diagram-, graph- or figure-bearing question as
   `requires_visual_verification` when held only at Rung B

### Deliverable

```text
data/raw/<subject>/papers/
data/raw/<subject>/memoranda/
data/raw/<subject>/companions/
data/raw/<subject>/curriculum/
data/raw/<subject>/ACQUISITION_REPORT.yaml
```

plus updated source manifests for the selected `source_id`s only.

### Driver

```bash
python3 scripts/phase3_ingest_drop.py            # ingest locally supplied files
python3 scripts/phase3_ingest_drop.py --dry-run  # report what would be matched
```

## Hard rules

* Never modify the original source files.
* Never replace an original with extracted text.
* Never silently overwrite a source.
* Preserve hashes, and state what was hashed.
* Preserve source URLs.
* Record failures.
* If a source cannot be acquired, mark it unresolved rather than pretending it
  was acquired.
* **New (v1.1.0):** never represent a Rung B transcription as a preserved
  original, and never let a Rung C record support a question family or a marking
  requirement.
* **New (v1.1.0):** never widen the selection silently. Adding papers beyond the
  approved selection requires a new decision record and an updated
  `CORPUS_SELECTION.yaml`.
* **New (v1.1.0):** the sample size is a budget, not a claim of sufficiency.
  Sufficiency is decided by the saturation test at Phase 8 and Phase 13
  (`SYSTEM_SPEC.md` §17.3).

---

# 5. Phase 4 — Extract source content

## Objective

Convert raw assessment documents into machine-readable representations while retaining the originals.

## Tasks

For every paper and memorandum:

1. extract text
2. retain page numbers
3. preserve tables
4. identify figures and diagrams
5. detect headers/footers
6. preserve question numbering
7. preserve mark allocations
8. record extraction confidence
9. identify pages requiring visual verification

## Deliverables

```text
data/extracted/<subject>/
```

Each extracted artifact must reference its source ID.

## Hard rules

* Do not invent missing text.
* Do not silently correct source wording.
* Do not discard diagrams that may carry meaning.
* Mark uncertain extraction.
* Visually verify ambiguous pages where necessary.

---

# 6. Phase 5 — Segment assessment questions

## Objective

Turn each question paper into structured assessment units.

## Required hierarchy

```text
paper
  section
    question
      subquestion
        component
```

A question record should retain:

```text
question_id
source_id
page
question_number
parent_question
verbatim_text
marks
associated_figure
associated_table
```

## Deliverables

```text
data/structured/<subject>/questions/
```

## Validation

The agent must report:

* number of papers processed
* number of questions
* number of subquestions
* number of segmentation uncertainties

## Hard rules

* Never rewrite the source question as the canonical text.
* Store the original extracted wording.
* Keep question boundaries traceable.
* Do not classify questions yet beyond basic structural metadata.

---

# 7. Phase 6 — Align questions with memoranda

## Objective

Map each assessment unit to its marking evidence.

## Tasks

For each question:

1. identify the corresponding memorandum item
2. match question/subquestion numbering
3. extract mark allocations
4. identify required steps/evidence
5. record alternative accepted responses where stated
6. record partial-credit rules where available

## Deliverable

Every question should have a memo relationship where a corresponding memo exists.

## Hard rules

* Do not infer marking criteria when the memo is available.
* Preserve exact source provenance.
* Distinguish explicit marking requirements from analytical interpretation.
* Mark unmatched questions for review.

---

# 8. Phase 7 — Curriculum mapping

## Objective

Map assessment questions to the Grade 11 curriculum/topic structure.

## Tasks

For each subject:

1. identify the official curriculum/topic structure
2. create topic hierarchy
3. map questions to topics/subtopics
4. record curriculum source
5. record uncertain mappings
6. identify assessment areas not covered by the current corpus

## Deliverables

```text
knowledge/<subject>/curriculum/
```

## Hard rules

* Curriculum hierarchy must come from authoritative source material.
* Do not create topics solely because they appear convenient.
* Any interpretation beyond the source must be marked derived.
* Do not assume that a paper's topic labels are the official curriculum hierarchy.

---

# 9. Phase 8 — Discover question taxonomy

## Objective

Identify recurring types of assessment questions.

This phase must be performed separately for each subject.

## Tasks

Analyse the complete structured corpus and identify:

* recurring question families
* recurring assessment operations
* recurring wording patterns
* recurring answer structures
* recurring reasoning demands
* recurring mark structures

Cluster questions that assess essentially the same underlying competence even when wording differs.

## Deliverables

```text
knowledge/<subject>/question_families/
knowledge/<subject>/question_taxonomy.yaml
```

Each question family must contain:

```yaml
question_family_id:
name:
definition:
subject:
grade:
topics:
assessment_operations:
representative_questions:
frequency:
source_evidence:
confidence:
validation_status:
```

## Hard rules

* Do not create one family for every individual question.
* Do not force unrelated questions into a family.
* Do not use generic educational taxonomies as authoritative.
* Taxonomy must be evidence-led.
* Preserve examples from multiple papers when available.

---

# 10. Phase 9 — Build Understanding Models

## Objective

Determine what a student actually needs to understand to successfully answer each question family.

This is the core knowledge-engineering phase.

## For every question family identify

### Required knowledge

What facts, concepts, definitions, rules, relationships, or content must the student know?

### Prerequisites

What must be understood beforehand?

### Question interpretation

What does the wording require the student to determine?

### Strategy

How does the student decide what approach is appropriate?

### Reasoning

What logical, mathematical, scientific, textual, historical, or analytical reasoning is required?

### Procedure

What operations must be performed?

### Explanation

What should the student be able to articulate?

### Verification / evaluation

How should the student check, interpret, justify, or evaluate the result?

### Evidence of understanding

What would convince us that the student genuinely understands rather than merely reproducing a procedure?

## Deliverable

```text
knowledge/<subject>/understanding_models/
```

## Hard rules

* Every model must link to source evidence.
* Do not confuse the memo answer with the underlying understanding.
* Do not assume that procedural success proves conceptual understanding.
* Separate explicit source requirements from derived pedagogical interpretation.

---

# 11. Phase 10 — Build the breakdown model

## Objective

Model the ways student understanding may fail for every Understanding Model.

## Required analysis

For each model determine plausible failure points:

```text
interpretation
prerequisite
concept
strategy
execution
reasoning
explanation
verification
```

For every breakdown define:

```text
breakdown_id
description
parent_understanding_model
observable_signals
possible_confusions
distinguishing_questions
source_basis
confidence
```

## Deliverable

```text
knowledge/<subject>/breakdowns/
```

## Hard rules

* A breakdown is not a diagnosis of the actual student.
* Do not claim that a student has a breakdown until interaction evidence exists.
* Distinguish "possible breakdown" from "observed breakdown."
* Avoid unsupported psychological explanations.

---

# 12. Phase 11 — Build diagnostic question bank

## Objective

Create Socratic diagnostic questions capable of distinguishing possible breakdowns.

## Each diagnostic needs

```text
diagnostic_id
understanding_model_id
target_breakdown
question
purpose
distinguishes
expected_evidence
follow_up_conditions
source_or_rationale
```

## Requirements

Diagnostic questions should:

* be open where appropriate
* expose the student's reasoning
* minimise leading
* distinguish competing explanations
* permit adaptive follow-up
* avoid giving away the target answer

## Hard rules

* Do not encode exam answers as diagnostic questions.
* Do not make every diagnostic question identical in form.
* Do not explicitly tell the student what the system is testing unless the tutoring policy requires it.
* Diagnostics must be tied to a known understanding model.

---

# 13. Phase 12 — Build the knowledge graph

## Objective

Create explicit relationships among the knowledge-bank entities.

Required relationships include:

```text
subject
  ↓
topic
  ↓
question_family
  ↓
understanding_model
  ↓
prerequisite
  ↓
breakdown
  ↓
diagnostic
```

and:

```text
question
  ↓
question_family
  ↓
understanding_model
```

and:

```text
question
  ↓
memorandum
  ↓
marking_criterion
```

and:

```text
knowledge_item
  ↓
source
```

## Deliverables

Human-readable knowledge files plus database representation.

---

# 14. Phase 13 — Subject validation

## Objective

Validate the complete knowledge bank against the source corpus.

Perform independently for:

1. Biology
2. Physics
3. History
4. English
5. AP Mathematics
6. Mathematics

## Required metrics

At minimum:

```text
sources discovered
sources acquired
papers processed
questions extracted
questions classified
questions unclassified
memo alignment
curriculum coverage
question-family coverage
understanding-model coverage
breakdown coverage
diagnostic coverage
unresolved items
```

## Required validation questions

* Can every question be classified?
* Can every classification be explained?
* Is the curriculum mapping defensible?
* Does the Understanding Model reflect the memo?
* Are source references present?
* Are derived conclusions distinguished from source facts?
* Are breakdowns represented?
* Are diagnostics capable of distinguishing them?

## Deliverable

```text
knowledge/<subject>/VALIDATION_REPORT.md
```

## Hard rules

A subject must not be marked validated merely because the extraction pipeline completed.

Unresolved or ambiguous cases must remain visible.

---

# 15. Phase 14 — Freeze knowledge-bank version

## Objective

Create an immutable, versioned assessment knowledge bank.

Example:

```text
knowledge/
  mathematics/
    v1.0.0/
  ap_mathematics/
    v1.0.0/
  physics/
    v1.0.0/
  biology/
    v1.0.0/
  history/
    v1.0.0/
  english/
    v1.0.0/
```

The exact version number should be determined from the repository's versioning policy.

## Deliverables

* version manifest
* checksum manifest
* validation report
* source manifest
* database seed
* Git commit

## Hard rules

* Never silently mutate an approved version.
* Any change requires a new version.
* Record exactly what changed between versions.

---

# 16. Phase 15 — Build database

## Objective

Create the queryable knowledge database.

Recommended initial implementation:

```text
SQLite
```

The schema should represent at least:

```text
subjects
curricula
sources
documents
papers
questions
question_families
topics
skills
understanding_models
prerequisites
breakdowns
diagnostics
marking_criteria
question_skill_links
question_understanding_links
understanding_prerequisite_links
understanding_breakdown_links
diagnostic_breakdown_links
provenance
validation_records
knowledge_versions
```

## Deliverables

```text
database/schema/
database/migrations/
database/seed/
database/knowledge.db
```

## Validation

Test:

* insertion
* retrieval
* provenance traversal
* question-to-understanding lookup
* understanding-to-breakdown lookup
* breakdown-to-diagnostic lookup
* version isolation

## Hard rules

* Database content must be reproducible from repository artifacts.
* Do not put undocumented knowledge directly into the database.
* The database must not become the only copy of important knowledge.

---

# 17. Phase 16 — Build Student Model

## Objective

Create the mutable student-understanding layer.

Represent evidence rather than simplistic labels.

A student's state may include:

```text
strong evidence
developing
uncertain
breakdown suspected
breakdown observed
mastered
```

But each state must be backed by interaction evidence.

## Deliverables

```text
student_model/
```

## Hard rules

* Never permanently label the student based on one response unless explicitly designed and justified.
* Store evidence.
* Distinguish tutor inference from observed student statements.
* Keep student data separate from curriculum truth.

---

# 18. Phase 17 — Build common Tutor Engine

## Objective

Build the common agent logic that retrieves the assessment knowledge and adapts its questioning to the student's evidence.

The engine should receive:

```text
subject
question
student response
student state
knowledge_bank_version
```

It should retrieve:

```text
question family
understanding model
prerequisites
breakdowns
diagnostics
marking criteria
```

It should then select the next useful question.

## Hard rules

* The tutor must remain grounded in the selected knowledge-bank version.
* The tutor must not create new curriculum requirements.
* The tutor must not expose internal diagnostic labels unnecessarily.
* The tutor should prefer student reasoning over direct explanation.

---

# 19. Phase 18 — Build subject agents

Implement:

```text
biology
physics
history
english
ap_mathematics
mathematics
```

Each subject agent should primarily provide:

* subject-specific terminology
* disciplinary reasoning conventions
* subject-specific interaction policy
* knowledge-bank retrieval
* formatting/notation rules
* subject-specific tutor behaviour

The subject agent should not duplicate the entire knowledge bank in prompts.

---

# 20. Phase 19 — Build evaluation suite

## Objective

Test the system as a learning system rather than simply an LLM application.

Tests must cover:

### Grounding

Does the tutor use the correct knowledge-bank version?

### Classification

Does a question retrieve the appropriate question family?

### Understanding

Does the tutor retrieve the correct Understanding Model?

### Diagnosis

Does it distinguish plausible breakdowns?

### Socratic behaviour

Does it ask rather than immediately tell?

### Adaptation

Does the next question respond to the student's previous answer?

### Non-leading behaviour

Does it avoid unnecessarily revealing the target competency?

### Provenance

Can the origin of an assessment requirement be traced?

### Immutability

Can the tutor modify the curriculum knowledge bank?

It must not.

---

# 21. Phase 20 — End-to-end integration

Run representative scenarios for all six subjects.

Each scenario should demonstrate:

```text
real question
    ↓
question classification
    ↓
understanding-model retrieval
    ↓
diagnostic questioning
    ↓
student response
    ↓
breakdown inference
    ↓
adaptive next question
    ↓
student explanation
    ↓
student-model update
```

Create:

```text
tests/end_to_end/
```

and an overall report.

---

# 22. Phase 21 — Final audit

Before declaring the project complete, inspect:

```text
source completeness
provenance completeness
taxonomy consistency
understanding-model consistency
breakdown consistency
diagnostic coverage
database integrity
versioning
test results
run logs
decision logs
```

Create:

```text
FINAL_AUDIT.md
```

The audit must clearly state:

* what was completed
* what remains unresolved
* what sources were inaccessible
* what assumptions were made
* what requires human review
* exact knowledge-bank versions used by the tutor

---

# 23. Subject execution order

When executing the knowledge-building phases, use this order:

```text
1. Biology
2. Physics
3. History
4. English
5. AP Mathematics
6. Mathematics
```

Do not attempt to process all six subjects in one phase run unless explicitly requested.

Each subject should reach validation before moving to the next.

> **v1.1.0 note.** Phase 3a (corpus selection) is executed for all six subjects
> in a single run, because the selection must be balanced across subjects before
> any acquisition budget is committed. The all-six selection was explicitly
> requested. Phases 5 onward still follow the per-subject order above.

---

# 24. Stop conditions

Stop the current phase when:

* its deliverables are complete
* validation has run
* unresolved issues are logged
* the run is recorded
* status is updated

Do not continue automatically.

---

# 25. Phase status format

Update `STATUS.md` after every run.

Example:

```yaml
current_phase: 6
current_subject: biology
status: completed
knowledge_bank_version: null
unresolved_items: 12
last_run_id: ...
next_allowed_phase: 7
```

The system must make it obvious which phase should be run next.
