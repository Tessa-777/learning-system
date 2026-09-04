# Grade 11 Adaptive Socratic Tutor

## System Specification

**Version:** 1.1.0
**Status:** Authoritative system definition
**Scope:** Grade 11 Biology, Physics, History, English, AP Mathematics, and Mathematics

> **v1.1.0 revision.** §16 (completion definition) and new §17 (corpus
> sufficiency and the fidelity ladder) replace the v1.0.0 assumption that the
> source corpus must be acquired exhaustively. The corpus is now a
> **form-stratified saturation sample** governed by
> [`CORPUS_SUFFICIENCY_POLICY.md`](CORPUS_SUFFICIENCY_POLICY.md). Nothing else
> in this specification changed: the two-layer separation (§2), the source-of-truth
> hierarchy (§5), provenance (§14) and immutability (§13) all still apply
> unchanged to the smaller corpus.

---

## 1. Purpose

Build an adaptive Socratic tutoring system for a Grade 11 student whose subjects are:

* Biology
* Physics
* History
* English
* AP Mathematics
* Mathematics

The system must be grounded in the student's actual curriculum and assessment environment.

Its source of truth is built from:

1. the school's official curriculum/reference material available through the St Benedict's Online Resource Centre (ORC)
2. the school's Grade 11 past papers available through the ORC
3. the corresponding marking memoranda, rubrics, and marking guidance where available
4. other assessment material explicitly associated with those official sources

The system must first build a structured knowledge bank describing **what students are expected to understand and demonstrate when answering questions**.

Only after that knowledge bank has been created and validated should the adaptive tutor be built on top of it.

---

# 2. Core architectural principle

The system has two fundamentally different knowledge layers.

## 2.1 Curriculum / assessment knowledge

This is the relatively stable source of truth.

It answers:

> What does this school, in this subject and grade, expect a student to understand and demonstrate?

It contains:

* curriculum topics
* question families
* question types
* assessment operations
* required knowledge
* prerequisite knowledge
* required reasoning
* required procedures
* evidence of understanding
* marking requirements
* common breakdowns
* misconceptions
* diagnostic strategies
* source provenance

This layer is built offline from source material.

The tutor must not independently redefine these requirements during tutoring.

---

## 2.2 Student knowledge

This is the adaptive layer.

It answers:

> What does this particular student appear to understand right now?

It contains evidence such as:

* demonstrated understanding
* partial understanding
* misconceptions
* recurring breakdowns
* successful explanations
* prerequisite gaps
* question-interpretation problems
* method-selection problems
* reasoning problems

This layer changes through interaction.

---

## 2.3 Separation rule

The following separation is mandatory:

```text
CURRICULUM / ASSESSMENT KNOWLEDGE
                    |
                    | read
                    v
              TUTOR ENGINE
                    |
                    | reads + updates
                    v
              STUDENT MODEL
```

The tutor may update the Student Model.

The tutor may not silently modify the Curriculum / Assessment Knowledge Bank.

Any change to the knowledge bank must happen through a new ingestion, analysis, validation, and versioning process.

---

# 3. Educational objective

The tutor is not primarily an answer-generation system.

Its primary objective is to help the student reach independent understanding.

A successful interaction should result in the student being able to explain, as appropriate to the subject:

* what the question requires
* what knowledge is relevant
* why that knowledge is relevant
* what approach or method is appropriate
* why that approach is appropriate
* how the reasoning works
* why the resulting answer is justified

Correctly producing an answer without being able to explain the reasoning is not sufficient evidence of understanding.

---

# 4. Two modes of learning

The system supports two related but distinct modes.

## 4.1 Question Understanding Mode

Purpose:

> Teach the student how to recognise and understand the different kinds of questions their subjects ask.

This mode uses the question taxonomy and understanding models in the knowledge bank.

It should help the student discover:

* what kinds of questions occur
* what the wording is asking them to do
* what each question type requires
* what knowledge they need
* what reasoning they need
* what evidence a good answer requires

The tutor should not simply announce:

> "This is a cause-and-effect question."

when the pedagogical goal is to help the student learn to recognise that themselves.

The tutor should use questioning to help the student arrive at that recognition.

---

## 4.2 Work-Through Mode

Purpose:

> Help the student understand a real question or piece of work they are currently dealing with.

The student may provide:

* homework
* a textbook question
* a past-paper question
* a test question
* an essay prompt
* working they have already attempted
* an explanation of what they think is happening

The tutor retrieves the corresponding assessment knowledge and uses Socratic questioning to diagnose understanding.

The tutor should progressively determine:

* whether the student understands the question
* whether they know the prerequisite knowledge
* whether they understand the relevant concept
* whether they can select an appropriate method
* whether they can execute the method
* whether they can explain their reasoning
* whether they can verify or evaluate their answer

---

# 5. Source-of-truth hierarchy

Sources must be treated according to the following hierarchy.

## Tier 1 — Authoritative source evidence

Examples:

* official ORC curriculum/reference material
* official school past papers
* official memoranda
* official rubrics
* official marking guidance

These establish what the assessment actually requires.

## Tier 2 — Structured analytical interpretation

Examples:

* grouping repeated questions into a question family
* identifying common prerequisite knowledge
* modelling the reasoning required by a question type
* identifying the structure of a marking scheme

These are derived from Tier 1 evidence.

## Tier 3 — Pedagogical inference

Examples:

* likely misconception patterns
* suggested diagnostic questions
* likely distinctions between different student failure modes

These may be useful but must never be represented as though they were directly stated by the source.

Every Tier 2 and Tier 3 object must retain provenance to the source evidence from which it was derived.

---

# 6. Subjects

The initial system scope is exactly six subjects:

```text
biology
physics
history
english
ap_mathematics
mathematics
```

Each subject must have:

* its own source corpus
* its own curriculum mapping
* its own question taxonomy
* its own understanding models
* its own breakdown models
* its own diagnostic knowledge
* its own validation report

The architecture should be shared across subjects, but the knowledge itself must remain subject-specific.

---

# 7. Subject-specific reasoning

The system must not assume that the same concept of "understanding" applies identically across every subject.

Examples of dimensions that may matter:

## Mathematics

* question interpretation
* mathematical object recognition
* prerequisite knowledge
* method selection
* symbolic manipulation
* procedural execution
* mathematical reasoning
* proof
* verification
* interpretation

## AP Mathematics

Use the same structural approach as Mathematics while deriving the actual content, methods, representations, reasoning demands, and assessment patterns from the AP Mathematics corpus used by the student.

Do not import a generic AP syllabus into the system unless it is explicitly part of the student's authoritative source set.

## Physics

Potential dimensions include:

* physical interpretation
* model selection
* principle recognition
* representation
* equation selection
* assumptions
* calculation
* units
* interpretation
* physical reasonableness

## Biology

Potential dimensions include:

* factual recall
* terminology
* process understanding
* mechanism
* cause/effect
* application
* data interpretation
* experimental reasoning
* comparison
* evaluation

## History

Potential dimensions include:

* chronology
* context
* causation
* consequence
* significance
* comparison
* evidence
* source analysis
* argument
* judgement
* evaluation

## English

Potential dimensions include:

* comprehension
* interpretation
* inference
* textual evidence
* language analysis
* structural analysis
* comparison
* argument
* evaluation
* written communication

These are analytical dimensions only. The final subject taxonomies must be derived and validated from the actual curriculum and assessment corpus.

---

# 8. Question model

Every assessment unit must be represented as more than an answer.

A question record should be able to reference:

```text
subject
grade
topic
subtopic
question family
question type
assessment operation
marks
required knowledge
required prerequisites
required reasoning
required method
evidence of understanding
marking criteria
common breakdowns
diagnostic questions
source evidence
```

---

# 9. Understanding model

The central conceptual entity in the knowledge bank is the Understanding Model.

An Understanding Model describes what a student must understand in order to successfully complete a recurring kind of assessment task.

A model may contain:

```text
identity
definition
subject
grade
topic
question family
assessment operations
required knowledge
prerequisites
required reasoning
required procedure
evidence of understanding
marking requirements
common breakdowns
misconceptions
diagnostic dimensions
diagnostic questions
source references
confidence
validation state
version
```

The purpose of the model is not to provide an answer to a question.

Its purpose is to describe the underlying competence being assessed.

---

# 10. Breakdown model

Each Understanding Model must represent plausible ways a student's understanding can fail.

Breakdowns may occur at different stages, for example:

```text
question interpretation
        ↓
prerequisite knowledge
        ↓
conceptual understanding
        ↓
strategy / method selection
        ↓
execution
        ↓
reasoning
        ↓
explanation
        ↓
verification / evaluation
```

Not every question requires every stage.

The knowledge bank must specify which stages apply to each model.

A breakdown must contain enough information for the tutor to distinguish it from other plausible breakdowns.

---

# 11. Diagnostic model

A diagnostic question is a question asked by the tutor for the purpose of determining what the student understands.

It is not necessarily an exam question.

Each diagnostic should identify:

* what it is trying to determine
* which understanding model it belongs to
* which breakdowns it helps distinguish
* what kinds of responses provide evidence
* source or rationale for its existence

Diagnostic questions must be designed to minimise leading the student toward the answer.

---

# 12. Socratic tutoring rules

The tutor must behave according to these principles.

## 12.1 Do not prematurely reveal the target

The tutor may internally know that a question requires a particular skill.

That does not mean it should immediately tell the student.

Instead it should probe the student's understanding.

## 12.2 Ask one useful question at a time

The tutor should generally ask a single next question that reduces uncertainty about the student's understanding.

## 12.3 Adapt to evidence

The tutor should choose its next question using the student's actual response.

## 12.4 Distinguish types of failure

The tutor should attempt to distinguish:

* not understanding the wording
* missing prerequisite knowledge
* conceptual misunderstanding
* incorrect method selection
* procedural failure
* reasoning failure
* explanation failure
* verification failure

## 12.5 Prefer student explanation over tutor explanation

The tutor should help the student construct and articulate the understanding.

## 12.6 Do not turn every interaction into an exam

The objective is understanding, not simply scoring.

---

# 13. Knowledge-bank immutability

The tutor reads a specific version of the knowledge bank.

Example:

```text
mathematics@1.0.0
physics@1.0.0
```

A new source corpus must produce a new knowledge-bank version after validation.

The tutor must never silently overwrite an existing validated version.

---

# 14. Provenance requirement

Every substantive knowledge-bank assertion must be traceable.

The minimum provenance chain is:

```text
knowledge item
    ↓
understanding model
    ↓
question family
    ↓
question(s)
    ↓
memo / rubric evidence
    ↓
source document
    ↓
ORC source
```

A knowledge item without traceable evidence must be marked unresolved or unvalidated.

---

# 15. Auditability

Every ingestion and analysis run must produce:

* run ID
* timestamps
* source inventory
* artifacts produced
* decisions made
* assumptions
* failures
* retries
* validation results
* unresolved items
* final status
* Git commit if available

The purpose is to make the entire build reproducible and inspectable.

---

# 16. Completion definition

The overall system is complete only when:

1. all six subjects have been processed
2. each subject has a validated source corpus, where *validated* means the
   corpus has passed the saturation test in §17.3 — not that it is exhaustive
3. each subject has a question taxonomy
4. each subject has Understanding Models
5. each subject has breakdown models
6. each subject has diagnostic knowledge
7. provenance exists throughout the knowledge graph
8. the database has been built and validated
9. the tutor can retrieve the correct assessment knowledge
10. the tutor can adapt questioning based on Student Model evidence
11. the evaluation suite passes
12. all runs and decisions are traceable

The system is not considered complete merely because an LLM can answer the student's homework questions.

---

# 17. Corpus sufficiency and the fidelity ladder

## 17.1 Why the corpus is sampled, not exhaustive

The knowledge bank's primary objects are question families (§8, Phase 8) and
Understanding Models (§9). §9 states that an Understanding Model describes *"the
underlying competence being assessed"* — not topic content. A taxonomy is
therefore a **compression** of a corpus, and acquiring every discovered document
to feed a compression step spends effort on exactly the redundancy the
compression removes.

What determines which question families a paper can contain is its **assessment
form** — who set it, which paper number it is, and which sitting it belongs to —
not its topics and not its year. The corpus itself demonstrates this: the
November 2018 Mathematics Paper 2 prints its own topic/mark table, the November
2022 Physics paper labels its own question families in its question headings, and
the November 2017 History paper declares its own three-section structure.

Sampling is therefore stratified on form. The full design, the evidence, the
memorandum-pairing rules and the known gaps are in
[`CORPUS_SUFFICIENCY_POLICY.md`](CORPUS_SUFFICIENCY_POLICY.md), which is
authoritative for Phases 3 and 4.

## 17.2 Fidelity ladder for acquired evidence

Not every acquired document arrives at the same fidelity. Each must record which
rung it occupies, and no document may be represented as occupying a higher rung
than it does.

```text
Rung A — original bytes preserved
    The file itself is stored under data/raw/<subject>/ with a SHA-256 hash of
    the original. Fully satisfies Phase 3. Diagrams, graphs and layout survive.

Rung B — faithful transcription, original not held
    Text obtained through a proxy or converter, with the original URL and
    source_id recorded and a hash of the transcription. Question wording,
    numbering and mark allocations survive; diagrams, graphs and geometric
    figures degrade or are lost.

Rung C — metadata only
    The source is known to exist but its content was never obtained. May be
    cited for provenance. May NOT be used as evidence for any question family,
    marking requirement or Understanding Model.
```

Rung B is acceptable for building question families and Understanding Models
because those depend on wording, command verbs, mark allocation and answer
structure — all of which survive transcription.

Rung B is **not** acceptable, on its own, for any question whose meaning depends
on a diagram, graph, geometric figure, circuit, table image or source-booklet
visual. Such questions must carry `requires_visual_verification: true` and must
not be used to assert marking requirements until either the original is supplied
(Rung A) or a human has verified the visual. This discharges the Phase 4 rule
*"Do not discard diagrams that may carry meaning."*

## 17.3 Saturation test

Sufficiency is decided empirically, not asserted:

> Order a subject's acquired papers by acquisition sequence. If the final third
> yields no question family, no assessment operation and no marking structure
> that the first two thirds did not already contain, the corpus is saturated for
> taxonomy purposes. If it does yield new families, acquisition continues —
> targeted at the strata that produced them, never by reverting to blanket
> acquisition.

Each Phase 13 validation report must state, per subject: `papers_in_sample`,
`question_families_identified`, `families_first_observed_in_final_third`,
`strata_left_unsampled`, and `families_supported_by_single_exemplar`. A subject
may not be marked validated while `families_first_observed_in_final_third > 0`.

## 17.4 What sampling does not license

* It does not make the sample a coverage of the Grade 11 syllabus. Work-Through
  Mode (§4.2) will encounter questions on topics no selected paper touches.
  Those must be recorded as knowledge-bank gaps, never answered as though they
  were grounded in the bank.
* It does not weaken provenance (§14). Every selected document keeps its
  `source_id`, source URL and ORC subject page.
* It does not permit substituting external material for missing ORC sources
  (`AGENTS.md` rule 3).
* It does not permit inferring marking criteria for a paper whose memorandum was
  never acquired (`AGENTS.md` rule 8). Such papers stay unresolved.
