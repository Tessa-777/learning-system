# Physics — Two-pass run report (Pass 1 + Pass 2)

Subject: physics · grade 11
Phases executed: 4 (extract), 5 (segment), 6 (align with memoranda), 8 (taxonomy), 9 (Understanding Models), 10 (breakdown model), 11 (diagnostic bank). Phase 7 (curriculum mapping) was **not** run — see §5.
Specs: `TWO_PASS_PROMPTS.md` (Pass 2), `SYSTEM_SPEC.md` v1.0.0, `IMPLEMENTATION_SPEC.md` v1.0.0
Entry point: `python scripts/run_physics_pass2.py`
Run log: the newest run under `runs/` (id also in `STATUS.md` → `last_run_id`) · review queue: `review_queue/RQ-P4-PHY-PASS2.yaml`

---

## 1. What was run

| Step | Input | Output |
|---|---|---|
| Pass 1 (re-run) | 4 question papers + their memoranda in `data/organized/physics/` | `data/extracted/physics_pass1.json` (238 records), `data/extracted/pass1/physics/*.json` |
| Pass 2 | that Pass 1 batch | `knowledge/physics/{question_families,understanding_models,breakdown_models,diagnostic_questions,unresolved_items,saturation_report,_PASS2_SUMMARY}.json` |

Both builders are pure stdlib + `jsonschema` + `pypdf`; no knowledge object was hand-written
into the output files. `tests/test_physics_pass2.py` executes both builders and re-checks the
committed artifacts against the same rules.

---

## 2. Pass 1 result

`data/organized/physics/` holds **25 files**: 15 named as question papers (14 distinct papers —
the 2020 paper ships as both `.pdf` and `.docx`), of which one (`PS11- P1-Physics - IeBT - MCQ -
2024.pdf`) is actually a memorandum (`UNRES-PHY-016`), giving **13 question papers** and 11
memoranda.

**4 papers were processed**, one per available year:

| paper | date | records | marks sum = printed total | memo pairing |
|---|---|---|---|---|
| PHY-2019-MY | 22 July 2019 | 60 | 165 = 165 | verified |
| PHY-2021-NOV | 15 Nov 2021 | 71 | 200 = 200 | verified |
| PHY-2023-MY | 18 July 2023 | 60 | 165 = 165 | verified |
| PHY-2025-NOV | 03 Nov 2025 | 47 | 135 = 135 | verified |

**238 question records**, each with real stem text, the memo's answer, the memo's marking
breakdown and rubric, a topic tag, and a verified SHA-256 for both its source PDF and its
memorandum (all 8 documents checked against the files on disk).

**9 question papers were not processed** (`UNRES-PHY-017`): 2020 Nov, Sept 2021 (no memo in the
sample), July 2022 (no memo), Nov 2022, Nov 2023, Mid-Year 2024, Mid-Year 2025 (no memo), Nov
2024, IeBT 2025 (memo is image-only). Pass 1 without a memorandum produces no marking notes,
and Pass 2 depends on them.

### Why Pass 1 had to be re-run

The committed `data/extracted/physics_pass1.json` held **one record per paper** with
`question_text`, `marks`, `memo_answer` and `topic_guess` all set to the literal string
`"unresolved"`, produced by `scripts/complete_subject_pass1.py`. Pass 2 would have had nothing
to cite. The PDFs are tracked in git and have a clean text layer, so the Phase 3 blocker
recorded in `STATUS.md` ("Google Drive downloads fail") does not apply to the organized corpus.
Only the physics records in `data/extracted/all_subjects_pass1.json` changed (15 → 238); the
other five subjects' records are byte-identical.

### Paper/memo pairing was verified, not trusted

`sample_manifest.json` pairs four physics papers with a memorandum from a **different sitting**
(`UNRES-PHY-015`). `verify_alignment()` compares paper with memo on printed header date, total
marks and examiner; only matching pairs were used, and every processed record carries
`memo_alignment.verified_by = "printed header DATE/MARKS/EXAMINER comparison"`.

### Provenance chain back to Phase 2

Every record also carries `orc_source_id` and `orc_memo_source_id`, resolved by title against
`data/raw/physics/SOURCE_INVENTORY.yaml` (a missing match is a hard build error). All 238 records
resolve, so the chain required by RUN_LOG_SPEC §9 is complete:

```
UNDERSTANDING-PHY-001
  → QUESTION-FAMILY-PHY-001
    → physics_2019_internal_paper1_june_q2.1.1  (37 such records across 4 papers)
      → SOURCE-ORC-PHY-2019-133 (paper) / SOURCE-ORC-PHY-2019-132 (memo)
```

| paper | ORC source_id | memo ORC source_id |
|---|---|---|
| PHY-2019-MY | SOURCE-ORC-PHY-2019-133 | SOURCE-ORC-PHY-2019-132 |
| PHY-2021-NOV | SOURCE-ORC-PHY-2021-138 | SOURCE-ORC-PHY-2021-137 |
| PHY-2023-MY | SOURCE-ORC-PHY-2023-146 | SOURCE-ORC-PHY-2023-145 |
| PHY-2025-NOV | SOURCE-ORC-PHY-2025-155 | SOURCE-ORC-PHY-2025-154 |

The Phase 3 inventory itself still records these as `inaccessible` with `local_path: null`, which
no longer describes the tracked files in `data/organized/` (`UNRES-PHY-025`).

---

## 3. Pass 2 result

| | count |
|---|---|
| question families | 16 |
| understanding models | 16 (one per family) |
| breakdown models | 48 |
| diagnostic questions | 44 (2–3 per model) |
| unresolved items | 28 |
| records assigned to a family | 224 / 238 |
| objects validated against `database/schema/*.schema.json` | 124, **0 failures** |

### Families

| id | family | members | papers | marks | confidence |
|---|---|---|---|---|---|
| PHY-001 | State a physics term to the memo's two-part definition | 37 | 4 | 1-2 | high |
| PHY-002 | Substitute into a data-sheet equation and carry the answer through | 37 | 4 | 2-5 | high |
| PHY-003 | Read and interpret a motion graph (value, interval, gradient, area) | 13 | 4 | 1-4 | high |
| PHY-004 | Construct a graph representation from a description or another graph | 9 | 4 | 3-5 | high |
| PHY-005 | Draw a labelled force diagram (free-body or vector addition) | 11 | 4 | 2-5 | high |
| PHY-006 | Apply Newton's second law to a system of connected bodies | 5 | 3 | 2-6 | high |
| PHY-007 | Resolve a force acting at an angle into components | 5 | 3 | 2-6 | high |
| PHY-008 | Predict a qualitative change, then justify it with a named relationship | 22 | 4 | 1-4 | high |
| PHY-009 | Analyse a resistor network (reduce, then apply Ohm / power / emf) | 17 | 4 | 2-5 | high |
| PHY-010 | Investigation: hypothesise, plot data, find the gradient and its physical meaning | 15 | 3 | 1-7 | high |
| PHY-011 | Photon and energy-level quantisation calculations | 10 | 3 | 1-4 | high |
| PHY-012 | Multiple-choice single-step concept application | 25 | 3 | 2-2 | high |
| PHY-013 | Identify the Newton's-third-law partner of a named force | 3 | 3 | 1-2 | medium |
| PHY-014 | Conservation of momentum and impulse-momentum in a collision | 3 | 1 | 2-6 | medium |
| PHY-015 | Explain a physical situation in words using a named principle | 9 | 3 | 1-4 | high |
| PHY-016 | Distinguish scalar from vector descriptions of the same motion | 3 | 2 | 2-4 | medium |

Rules the builder enforces and the test suite re-checks:

* **Membership is a partition** — no record belongs to two families; 14 records that fit no
  family are reported unassigned (`UNRES-PHY-021`) rather than force-fitted.
* **≥2 members per family**; `families_supported_by_single_exemplar` is 0.
* **Confidence is computed, never authored**: `high` requires ≥4 members across ≥3 papers,
  otherwise `medium`; it can never be `high` on one paper's evidence. 13 high / 3 medium.
* **No family mixes disciplines** — every member of every family is tagged `discipline: Physics`
  (the Pass 2 Physical Science note); there is no Chemistry content in this batch.
* **`typical_marks_range`** is preserved per family in `_PASS2_SUMMARY.json`
  (`families[].marks_range`) because `question_family.schema.json` sets
  `additionalProperties: false` and has no such field — see §6.

`PHY-014` (momentum/impulse) is the only family resting on one paper: momentum appears **only**
in the 2025 November paper, because the 2021 Mid-Year sitting that would have carried it is not
in the sample (`UNRES-PHY-017`).

### Understanding Models

One per family with the full §9 field list plus `provenance` (AGENTS.md rule 6). All 16 carry
`validation_state: "unvalidated"` and `version: "0.1.0-draft"`; `confidence` mirrors its family.

### Breakdown models

48 breakdowns over **7 of the 9 permitted stages**: concept 12, execution 10, explanation 7,
reasoning 7, strategy 5, interpretation 4, prerequisite 3. No `verification` or `other`
breakdown is evidenced in this batch — none is asserted. Each carries `observable_signals`,
`possible_confusions` and `source_basis` citing the Pass 1 records it came from; 41 cite ≥2
records and **7 cite one** (`BREAKDOWN-PHY-010-A`, `-011-C`, `-013-B`, `-014-A/-B/-C`,
`-016-B`) — all 7 are listed in `UNRES-PHY-023`, tagged `single_exemplar`.

The marking-pattern grounding is real: 4 records across 3 papers carry memo marking notes of
the form "Formula, substitution, answer" (2019 Q2.2.2, 2019 Q7.5.2, 2021 Q6.2.2, 2023 Q2.2),
and 2019 Q2.1.4 records "Separate formula mark awarded before substitution".

### Diagnostic questions

44 diagnostics, 2–3 per model (12 models have 3, 4 have 2). Each names its model, the breakdown
it targets, the breakdowns it distinguishes between, the evidence a correct response gives, and
conditional follow-ups. None states the answer.

---

## 4. Saturation report

```
papers_in_sample                          4
question_families_identified              16
families_first_observed_in_final_third    1     (QUESTION-FAMILY-PHY-014)
strata_left_unsampled                     5
families_supported_by_single_exemplar     0
```

**Not saturated.** The prompt's rule is explicit: a subject cannot be declared saturated while
`families_first_observed_in_final_third > 0`. Acquisition order used: 2019-MY → 2021-NOV →
2023-MY → 2025-NOV, split into thirds `[2019-MY] [2021-NOV, 2023-MY] [2025-NOV]`; PHY-014's
members all come from the final third. Three further reasons are recorded:

1. 4 papers where 8–15 are recommended.
2. 5 strata left unsampled, verbatim from the report: `exam_board=IEB` (both IeBT items are
   unusable), `exam_board=NSC`, `exam_period=prelim`, `paper_type=paper2`, and the 9
   unextracted papers.
3. Four recurring patterns meet the member minimum but rest on 2 papers, so they were **not**
   promoted (`DEC-P4-006`, stricter than the letter of the spec — see §6):

   | candidate | pattern | members | papers | evidence |
   |---|---|---|---|---|
   | A | static-friction threshold on an incline (μ = tan θ) | 5 | 2 | 2019 Q5.6, Q5.7; 2023 Q7.2.2–7.2.4 |
   | B | work-energy theorem used instead of kinematics | 5 | 2 | 2021 Q6.2.1/6.2.2/6.2.4; 2025 Q2.6, Q4.6 |
   | C | symbolic "in terms of" with no numerical data | 2 | 2 | 2019 Q2.3; 2023 Q2.7 |
   | E | "prove / show that" with the target printed | 3 | 2 | 2023 Q6.3; 2025 Q2.4, Q3.4 |

   A and B are the first to promote once a third paper is extracted.

---

## 5. Honest limits — what this run does **not** establish

* **Coverage is partial.** 9 of 13 question papers were not processed; topics present only in
  those papers appear in no family here.
* **No curriculum mapping.** No Grade 11 Physical Sciences curriculum or ATP document is in the
  organized sample, so Phase 7 could not run and `curriculum_mapping_rate` is `null`
  (`UNRES-PHY-020`).
* **Topic coverage gaps.** Electrostatics appears in exactly one item (2025 Q6.2, one paper) so
  no family exists for it; electromagnetism appears nowhere; Waves/Sound/Light appears only as
  photons and energy levels; momentum only in 2025 (`UNRES-PHY-018`).
* **197 of 238 records are flagged `requires_visual_verification`** — their meaning depends on a
  circuit diagram, motion graph, apparatus drawing or energy-level diagram that exists only as
  an image. Every record is nonetheless `fidelity_rung: A`, because the **text layer itself** is
  clean and the stems, marks and memo answers were read directly; the diagrams were not
  inspected (`UNRES-PHY-011`).
* **The §17.2 visual cap did not fire on any family.** That cap applies only where members are
  *both* below Rung A *and* visually unverified, and no record here is below Rung A — so the 13
  high-confidence families keep their rating. The exposure is recorded instead as
  `visual_verification_members` per family in `_PASS2_SUMMARY.json`, and `UNRES-PHY-011` now
  derives its `affected` list from the evidence: **14 of 16 families** have over half their
  members image-dependent (PHY-003/004/005/006/007/009/016 at 100%, PHY-002 35/37, PHY-008 21/22,
  PHY-010 14/15, PHY-015 8/9, PHY-011 8/10, PHY-001 22/37, PHY-012 13/25). Only PHY-013 (1/3)
  and PHY-014 (0/3) do not.
* **14 records are unassigned** (`UNRES-PHY-021`), including the four candidate patterns above.
* **10 memo contradictions are unresolved**, of which one changes the correct answer: 2025 memo
  6.2.1 marks "Positive" while all three accepted reasonings in 6.2.2 conclude Q2 is negative
  (`UNRES-PHY-005`). The 2025 memo header also says 125 marks against the paper's 135
  (`UNRES-PHY-002`), and 47 records carry `memo_alignment.marks_match: false` for that reason.
* **One stratum is unrepresented in every processed paper**: all four are internally set
  (`exam_board = internal`), and the 2025 paper has no multiple-choice section, so PHY-012 rests
  on 2019/2021/2023 only (`UNRES-PHY-019`).
* **All 16 models are `unvalidated`.** Nothing here has been validated against student
  responses; that is Phase 13.

---

## 6. Deviations from the Pass 2 prompt, and why

| Deviation | Reason |
|---|---|
| Family fields named `source_evidence` / `definition` instead of `member_source_ids` / `distinguishing_features`; `typical_marks_range` moved to `_PASS2_SUMMARY.json` | `database/schema/question_family.schema.json` sets `additionalProperties: false` and has no such fields. The persisted object must validate against the repository schema (IMPLEMENTATION_SPEC Phase 8). Recorded as `DEC-P4-005`. |
| 4 candidate families with ≥2 members were deferred to `unresolved_items` instead of being promoted | Their `marking_requirements` could not be generalised from two sittings. All four remain in `unresolved_items.json` with their evidence, so nothing is hidden and promotion is a one-line change in `ingestion/analysis/physics_pass2_families.py`. Recorded as `DEC-P4-006`. |
| `confidence` requires 3+ papers for `high`, not just 4+ members | The prompt forbids `high` when all support comes from one paper; requiring 3 papers is the conservative reading and is computed, so it is auditable. Recorded as `DEC-P4-003`. |
| `target_breakdown` is filled from `distinguishes[0]` when the analysis left it empty | A diagnostic must name the breakdown it targets; deriving it mechanically keeps the object schema-valid without inventing a target. |

---

## 7. Reproducing this

```
python scripts/run_physics_pass2.py   # Pass 1 + Pass 2 + run log + review queue
python -m pytest                      # 56 tests, 8 of them over this output
```

`pypdf` is required by the Pass 1 builder and is listed in `requirements.txt`.
