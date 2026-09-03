# Grade 11 Adaptive Socratic Tutor

An adaptive Socratic tutoring system for a Grade 11 student whose subjects are
Biology, Physics, History, English, AP Mathematics and Mathematics.

The system is grounded in the student's actual curriculum and assessment
environment. Its source of truth is built from the school's official material
available through the St Benedict's Online Resource Centre (ORC): curriculum /
reference material, Grade 11 past papers, the corresponding marking memoranda,
rubrics and marking guidance.

The project first builds a structured knowledge bank describing **what
students are expected to understand and demonstrate when answering questions**.
Only after that knowledge bank is created and validated is the adaptive tutor
built on top of it.

> **Status:** see [`STATUS.md`](STATUS.md).

---

## Specification Documents

| Document | Purpose |
|---|---|
| [`SYSTEM_SPEC.md`](SYSTEM_SPEC.md) | Authoritative system definition and architecture. |
| [`IMPLEMENTATION_SPEC.md`](IMPLEMENTATION_SPEC.md) | Phased implementation plan (one phase at a time). |
| [`AGENTS.md`](AGENTS.md) | Absolute rules every execution must follow. |
| [`RUN_LOG_SPEC.md`](RUN_LOG_SPEC.md) | Run, decision and error logging requirements. |

## Repository Layout

```text
/
├── SYSTEM_SPEC.md
├── IMPLEMENTATION_SPEC.md
├── AGENTS.md
├── RUN_LOG_SPEC.md
├── README.md
├── STATUS.md
│
├── config/            # base project + subject configuration
├── core/              # shared infrastructure (ids, config, runlog, schema)
├── data/              # raw sources, extracted text, structured questions, validated
├── knowledge/         # subject-specific knowledge bank
├── database/          # schema, migrations, seed, knowledge.db
├── ingestion/         # acquisition, extraction, segmentation, classification, analysis, validation
├── tutor/             # core engine, prompts, per-subject agents
├── student_model/     # mutable student-understanding layer
├── tests/             # test suite
├── scripts/           # runnable phase drivers (e.g. phase1_bootstrap.py)
├── runs/              # per-run audit logs (RUN_LOG_SPEC)
└── review_queue/      # human-review items (RUN_LOG_SPEC)
```

## Install

The build dependencies are documented in [`requirements.txt`](requirements.txt).
Because system Python may be externally managed (PEP 668), use a virtual
environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the Phase 1 bootstrap

Phase 1 (Repository Bootstrap) sets up the structure, schemas, logging
framework and documentation. To execute it and record a fresh run:

```bash
source .venv/bin/activate
python scripts/phase1_bootstrap.py
```

This creates a new run under `runs/`, validates the schemas against example
instances, runs the test suite and updates the status. Each invocation records a
new run ID.

## Run the tests

```bash
source .venv/bin/activate
python -m pytest
```

## Phase model

The implementation is executed one phase at a time. Do **not** continue into a
later phase automatically. The exact next phase is recorded in
[`STATUS.md`](STATUS.md).

* Phase 1 — Repository bootstrap
* Phase 2 — ORC source discovery
* Phase 3 — Acquire and preserve the source corpus
* Phase 4 — Extract source content
* Phase 5 — Segment assessment questions
* Phase 6 — Align questions with memoranda
* Phase 7 — Curriculum mapping
* Phase 8 — Discover question taxonomy
* Phase 9 — Build Understanding Models
* Phase 10 — Build the breakdown model
* Phase 11 — Build diagnostic question bank
* Phase 12 — Build the knowledge graph
* Phase 13 — Subject validation
* Phase 14 — Freeze knowledge-bank version
* Phase 15 — Build database
* Phase 16 — Build Student Model
* Phase 17 — Build common Tutor Engine
* Phase 18 — Build subject agents
* Phase 19 — Build evaluation suite
* Phase 20 — End-to-end integration
* Phase 21 — Final audit

## Design principles

The tutor is not primarily an answer-generation system; it helps the student
reach independent understanding through Socratic questioning. Two knowledge
layers are kept strictly separate (SYSTEM_SPEC §2):

* **Curriculum / assessment knowledge** — the stable source of truth, built
  offline and immutable per version.
* **Student knowledge** — the adaptive layer, updated through interaction.

Every substantive knowledge assertion must be traceable to source evidence.
