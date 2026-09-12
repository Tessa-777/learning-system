# Project Status

This file is auto-written by `scripts/phase1_bootstrap.py` and should be updated after each run (IMPLEMENTATION_SPEC §25). The current phase is recorded under `runs/`.

```yaml
current_phase: 4-11 (biology Pass 1 + Pass 2; Phase 7 not run)
current_subject: biology
status: completed_with_review
knowledge_bank_version: null
unresolved_items: 19 # current biology run only; earlier subject queues remain open
last_run_id: 20260912T032614Z_139d
next_allowed_phase: biology review/acquisition and Phase 7 mapping; no automatic phase continuation
```

> **Corrections to earlier entries in this file.** The Phase 3 aggregate below states that
> "No Phase 4 artifacts exist" and that Phase 4 must not start until all 818 sources are
> downloaded. Both are now out of date for physics: `data/organized/` holds 163 source files
> that are tracked in git, including the 25 physics PDFs used by the run recorded below, and
> `data/extracted/` holds real Pass 1 output. `data/raw/physics/SOURCE_INVENTORY.yaml` still
> lists all 233 ORC sources as `inaccessible` with `local_path: null`, which no longer
> describes the organized copies — that inventory has not been reconciled
> (`UNRES-PHY-025`).

---

## Phase 1 — Repository Bootstrap

**Status:** completed

**Run ID:** `20260903T075532Z_0796`

### Outcome

Phase 1 acceptance criteria passed: structure present, schemas validate, a test run was created, decisions were logged, tests passed.

The objective was to establish the repository structure, configuration, schemas, logging framework and basic documentation. No curriculum material was collected or analysed.

---

## Phase 2 — ORC Source Discovery

**Status:** completed_with_review

**Run ID:** `20260903T090314Z_25ba`

### Outcome

Authoritative source inventories were built for all six Grade 11 subjects from St Benedict's Online Resource Centre (`https://sites.google.com/stbenedicts.co.za/orc`). 821 schema-valid source records were recorded across 6 subject inventories plus 4 physics container (folder) records; 3 external sources marked `external`; 36 records marked out-of-scope (chemistry / Grade 12) for provenance only.

No source files were downloaded or altered. No educational content was analysed. Discovery did not continue into Phase 3.

### Deliverables

- `data/raw/CORPUS_MANIFEST.yaml` — corpus manifest (totals, per-subject summary, unresolved sources, review items)
- `data/raw/<subject>/SOURCE_INVENTORY.yaml` × 6 — biology (52), physics (233 + 4 containers), history (18), english (100), ap_mathematics (146), mathematics (272)

### Validation

- 821 / 821 source records validate against `database/schema/source_metadata.schema.json` (0 failures).
- 821 unique `source_id`s; 0 duplicates.
- Live Drive re-verification: all Maths file IDs (2016–2026), English past-paper/file IDs and AP Maths file IDs resolved against live Drive listings; no missing file-level entries; 1 physics duplicate file ID deduped; 2 Maths + 1 AP external URLs recorded as `external`.
- Run log, decisions, errors, metrics and artifact manifest written.

### Unresolved / review items (6)

1. Legacy `Grade 11 work` Drive folder `1-fySqm2KyqUZcGdjElhHbgzhhN5DBA0y` — unlistable (HTTP 500), subject attribution unconfirmed.
2. AP Mathematics has no dedicated ORC page — FS Maths Grade 11 Drive used; boundary to be confirmed.
3. History `Zipped Past Papers.zip` — contents not expanded in Phase 2.
4. Physics legacy `ORC Matric 2020 (Current Grade 11)` folder — children not surveyed.
5. External formula sheets (stithian.com) and Mindbourne portal — grade applicability not stated.
6. Out-of-scope discovery clusters (chemistry, Grade 12 Film Contextual Tests, AP P2 Info Booklet) — retained for provenance; must not be used without review.

---

## Phase 3A — Biology Source Acquisition

**Status:** completed_with_review

**Run ID:** `20260903T091841Z_9448`

**Subject:** biology

### Outcome

Phase 3 acquisition was executed for Biology. All 52 accessible authoritative sources identified in Phase 2 were attempted. No files could be downloaded from the Google Drive URLs due to sandbox TLS/SSL connection termination. All 52 sources were updated in `data/raw/biology/SOURCE_INVENTORY.yaml` with `access_status: inaccessible`, `local_path: null`, `file_hash: null`, and detailed failure notes. No original files were modified or invented. No duplicate file hashes were detected (no files acquired).

### Deliverables

- Updated `data/raw/biology/SOURCE_INVENTORY.yaml`
- `data/raw/biology/ACQUISITION_REPORT.yaml`
- `runs/20260903T091841Z_9448/` — full run log (events, decisions, errors, metrics, artifacts)
- `review_queue/RQ-P3-BIO-ACQUISITION.yaml`

### Metrics

- Sources discovered: 52
- Sources accessible before: 52
- Sources acquired: 0
- Sources failed: 52
- Sources external: 0
- Sources inaccessible after: 52
- Duplicate hashes detected: 0
- Unresolved items: 52

### Unresolved / review items

- All 52 Biology sources remain inaccessible and must be retried in an environment with working Google Drive access, or files must be provided manually before Phase 4.

---

## Phase 3B — Physics Source Acquisition

**Status:** completed_with_review

**Run ID:** `20260903T091842Z_c0f7`

**Subject:** physics

### Outcome

Phase 3 acquisition was executed for Physics. All 233 accessible authoritative sources (plus 4 container folders) identified in Phase 2 were attempted. No files could be downloaded from the Google Drive URLs due to sandbox TLS/SSL connection termination. All 233 sources were updated in `data/raw/physics/SOURCE_INVENTORY.yaml` with `access_status: inaccessible` and failure notes. The 4 container folders (including the out-of-scope `IeBT P2-Chemistry folder`) remain noted but were not expanded or downloaded.

### Deliverables

- Updated `data/raw/physics/SOURCE_INVENTORY.yaml`
- `data/raw/physics/ACQUISITION_REPORT.yaml`
- `runs/20260903T091842Z_c0f7/` — full run log
- `review_queue/RQ-P3-PHY-ACQUISITION.yaml`

### Metrics

- Sources discovered: 233 (+ 4 containers)
- Sources accessible before: 233
- Sources acquired: 0
- Sources failed: 233
- Sources external: 0
- Sources inaccessible after: 233
- Duplicate hashes detected: 0
- Unresolved items: 233

### Unresolved / review items

- All 233 Physics sources remain inaccessible; container folder contents must be inspected manually; must be retried before Phase 4.

---

## Phase 3C — History Source Acquisition

**Status:** completed_with_review

**Run ID:** `20260903T091848Z_81f2`

**Subject:** history

### Outcome

Phase 3 acquisition was executed for History. All 18 accessible authoritative sources identified in Phase 2 were attempted. No files could be downloaded due to sandbox TLS/SSL restriction. All 18 sources updated to `access_status: inaccessible`. Note: the `Zipped Past Papers.zip` identified in Phase 2 remains unexpanded; it must be expanded and inspected if obtained.

### Deliverables

- Updated `data/raw/history/SOURCE_INVENTORY.yaml`
- `data/raw/history/ACQUISITION_REPORT.yaml`
- `runs/20260903T091848Z_81f2/` — full run log
- `review_queue/RQ-P3-HIS-ACQUISITION.yaml`

### Metrics

- Sources discovered: 18
- Sources accessible before: 18
- Sources acquired: 0
- Sources failed: 18
- Sources external: 0
- Sources inaccessible after: 18
- Unresolved items: 18

### Unresolved / review items

- All 18 History sources remain inaccessible; zip file contents must be expanded upon acquisition; must be retried before Phase 4.

---

## Phase 3D — English Source Acquisition

**Status:** completed_with_review

**Run ID:** `20260903T091848Z_827b`

**Subject:** english

### Outcome

Phase 3 acquisition was executed for English. All 100 accessible authoritative sources identified in Phase 2 were attempted. No files could be downloaded due to sandbox TLS/SSL restriction. All 100 sources updated to `access_status: inaccessible`. No original files were modified.

### Deliverables

- Updated `data/raw/english/SOURCE_INVENTORY.yaml`
- `data/raw/english/ACQUISITION_REPORT.yaml`
- `runs/20260903T091848Z_827b/` — full run log
- `review_queue/RQ-P3-ENG-ACQUISITION.yaml`

### Metrics

- Sources discovered: 100
- Sources accessible before: 100
- Sources acquired: 0
- Sources failed: 100
- Sources external: 0
- Sources inaccessible after: 100
- Unresolved items: 100

### Unresolved / review items

- All 100 English sources remain inaccessible; must be retried before Phase 4.

---

## Phase 3E — AP Mathematics Source Acquisition

**Status:** completed_with_review

**Run ID:** `20260903T091851Z_b250`

**Subject:** ap_mathematics

### Outcome

Phase 3 acquisition was executed for AP Mathematics. 145 accessible authoritative sources were attempted (1 external source excluded); no files could be downloaded due to sandbox TLS/SSL restriction. All 145 sources updated to `access_status: inaccessible`. The 1 external source (`stithian.com` formula sheet) remains marked `external` and requires grade-applicability verification before use.

### Deliverables

- Updated `data/raw/ap_mathematics/SOURCE_INVENTORY.yaml`
- `data/raw/ap_mathematics/ACQUISITION_REPORT.yaml`
- `runs/20260903T091851Z_b250/` — full run log
- `review_queue/RQ-P3-APM-ACQUISITION.yaml`

### Metrics

- Sources discovered: 146
- Sources accessible before: 145
- Sources acquired: 0
- Sources failed: 145
- Sources external: 1
- Sources inaccessible after: 145
- Unresolved items: 145

### Unresolved / review items

- All 145 AP Mathematics sources remain inaccessible; external formula sheet applicability must be confirmed; AP Mathematics source boundary (FS Maths Grade 11 Drive) must be verified; must be retried before Phase 4.

---

## Phase 3F — Mathematics Source Acquisition

**Status:** completed_with_review

**Run ID:** `20260903T091854Z_8c5d`

**Subject:** mathematics

### Outcome

Phase 3 acquisition was executed for Mathematics. 270 accessible authoritative sources were attempted (2 external sources excluded); no files could be downloaded due to sandbox TLS/SSL restriction. All 270 sources updated to `access_status: inaccessible`. The 2 external sources (`stithian.com`, Mindbourne portal) remain marked `external` and require grade-applicability verification.

### Deliverables

- Updated `data/raw/mathematics/SOURCE_INVENTORY.yaml`
- `data/raw/mathematics/ACQUISITION_REPORT.yaml`
- `runs/20260903T091854Z_8c5d/` — full run log
- `review_queue/RQ-P3-MAT-ACQUISITION.yaml`

### Metrics

- Sources discovered: 272
- Sources accessible before: 270
- Sources acquired: 0
- Sources failed: 270
- Sources external: 2
- Sources inaccessible after: 270
- Unresolved items: 270

### Unresolved / review items

- All 270 Mathematics sources remain inaccessible; external sources must be verified; source inventory completeness must be confirmed; must be retried before Phase 4.

---

## Aggregate Phase 3 Status

**Status:** completed_with_review

**Run IDs:**

- Biology: `20260903T091841Z_9448`
- Physics: `20260903T091842Z_c0f7`
- History: `20260903T091848Z_81f2`
- English: `20260903T091848Z_827b`
- AP Mathematics: `20260903T091851Z_b250`
- Mathematics: `20260903T091854Z_8c5d`

### Aggregate Metrics

- Total sources discovered: 821
- Total sources accessible before Phase 3: 818 (52 + 233 + 18 + 100 + 145 + 270)
- Total sources acquired: 0
- Total sources failed: 818
- Total external sources (not downloaded): 3 (1 AP + 2 Math)
- Total duplicate file hashes detected: 0
- Aggregate unresolved items: 818

### Aggregate Notes

No source files were downloaded for any subject because the sandbox environment terminates TLS connections to Google Drive (`drive.google.com`). Every acquisition attempt was properly attempted, documented, and recorded. Original source files from Phase 2 were not modified, replaced, or overwritten. No Phase 4 (extraction) work was started. The acquisition must be retried in an environment with working Google Drive access, or files must be provided manually, before Phase 4 can proceed.

### Deliverables (aggregate)

- `data/raw/PHASE3_AGGREGATE_SUMMARY.yaml`
- Updated `data/raw/<subject>/SOURCE_INVENTORY.yaml` × 6
- `data/raw/<subject>/ACQUISITION_REPORT.yaml` × 6
- `runs/` directories × 6 (full logs, decisions, errors, metrics, artifacts)
- `review_queue/RQ-P3-*-ACQUISITION.yaml` × 6

### Validation

- All 6 run directories contain `run.json`, `events.jsonl`, `decisions.json`, `errors.json`, `metrics.json`, and `artifacts/artifacts.yaml`.
- All 6 source inventories validate against the `source_metadata.schema.json` schema (updated fields: `access_status`, `local_path`, `file_hash`, `notes`).
- No fabricated source files exist in `data/raw/<subject>/` (only `.gitkeep`, updated `SOURCE_INVENTORY.yaml`, and new `ACQUISITION_REPORT.yaml`).
- No original source files were modified or overwritten.
- All errors are recorded with `unresolved` status.
- All decisions document the acquisition strategy and its failure.
- No Phase 4 artifacts exist (no `data/extracted/` content created).

### Unresolved / review items (aggregate: 818 + 6 previous)

1-6. Previous Phase 2 unresolved items (see above) remain open.
7. All 818 accessible sources across 6 subjects remain inaccessible and must be retried or provided manually before Phase 4.
8. Container folders (Physics: 4) require manual inspection when acquisition is retried.
9. External sources (AP: 1, Math: 2) require grade-applicability verification.
10. History `Zipped Past Papers.zip` must be expanded and inspected upon acquisition.

---

## Physics Two-Pass — Phases 4, 5, 6, 8, 9, 10, 11

**Status:** completed_with_review

**Run ID:** `20260911T210957Z_edb5`

**Subject:** physics

### Outcome

Pass 1 was re-run for physics and Pass 2 (cross-paper synthesis, `TWO_PASS_PROMPTS.md`) was
executed on the resulting batch. 238 question records were extracted from 4 question papers and
their verified memoranda, and compressed into 16 question families, 16 Understanding Models, 48
breakdown models, 44 diagnostic questions and 28 unresolved items. Every emitted object validates
against `database/schema/*.schema.json` (124 checked, 0 failures). The saturation report does
**not** declare physics saturated. Full narrative: `knowledge/physics/PASS2_REPORT.md`.

The inherited `data/extracted/physics_pass1.json` was a stub (one record per paper, every content
field `"unresolved"`); it was rebuilt from the tracked PDFs in `data/organized/physics`. Only the
physics records in `data/extracted/all_subjects_pass1.json` changed (15 → 238); the other five
subjects' records are byte-identical.

### Deliverables

- `data/extracted/physics_pass1.json`, `data/extracted/pass1/physics/*.json` — Pass 1 batch
- `knowledge/physics/{question_families,understanding_models,breakdown_models,diagnostic_questions,unresolved_items,saturation_report,_PASS2_SUMMARY}.json, plus `pass2_output.json` (the same content as the single five-array object the prompt specifies)`
- `knowledge/physics/PASS2_REPORT.md` — narrative and saturation verdict
- `ingestion/extraction/physics_pass1_evidence_{2019,2021,2023,2025}.py` — Pass 1 evidence tables
- `ingestion/analysis/physics_pass2_{families,models,unresolved}.py` — Pass 2 analysis
- `scripts/build_physics_pass1.py`, `scripts/build_physics_pass2.py`, `scripts/run_physics_pass2.py`
- `tests/test_physics_pass2.py` — 8 tests executing both builders and re-checking the artifacts
- `review_queue/RQ-P4-PHY-PASS2.yaml` — 28 items, each with issue, affected entity, evidence,
  possible resolutions and a recommended review

### Metrics

- Files in the organized physics sample: 25 (13 question papers, 11 memoranda)
- Papers processed: 4 (2019 mid-year, 2021 Nov, 2023 mid-year, 2025 Nov); not processed: 9
- Questions extracted: 238; classified into a family: 224; unclassified: 14
- Memo alignment rate: 1.00 (all pairs verified from printed headers); 2025 memo marks disagree
  with the paper (125 vs 135) — `UNRES-PHY-002`
- Curriculum mapping rate: null — Phase 7 not run, no curriculum document in the sample
- Records requiring visual verification: 197 of 238
- Question families 16 (13 high / 3 medium confidence); models 16 (all `unvalidated`, `0.1.0-draft`)
- Breakdowns 48; diagnostics 44; unresolved items 28; validation failures 0
- Saturation: papers_in_sample 4, families 16, families first observed in the final third 1,
  strata left unsampled 5, families supported by a single exemplar 0 → **not saturated**

### Unresolved / review items (28, all in `review_queue/RQ-P4-PHY-PASS2.yaml`)

Highlights: 10 paper/memo contradictions (one of which changes the correct answer,
`UNRES-PHY-005`); 9 of 13 question papers not extracted (`UNRES-PHY-017`); electrostatics,
electromagnetism, mechanical waves and momentum are thin or absent (`UNRES-PHY-018`); no
curriculum document (`UNRES-PHY-020`); 14 records unassigned (`UNRES-PHY-021`); 1 family rests
on one paper (`UNRES-PHY-022`); 7 breakdowns rest on a single record (`UNRES-PHY-023`, tagged
`single_exemplar`); the Phase 3 inventory does not reflect `data/organized/` (`UNRES-PHY-025`).

---

## Next Phase

**Physics:** Phase 12 (knowledge graph) and Phase 13 (subject validation) are the natural next
steps, but Phase 7 (curriculum mapping) is still owed for physics and blocks a real curriculum
mapping rate. Extracting the 9 remaining paired physics papers and re-running Pass 2 is the
cheapest way to reduce the 28 unresolved items and to test saturation again.

**Other subjects:** still at Phase 3. Their Pass 1 files remain stubs generated by
`scripts/complete_subject_pass1.py` with no question content, so Pass 2 must not be run on them
until they are rebuilt the way physics was.



<!-- BIOLOGY_PASS2_START -->
## Biology Two-Pass — 2026-09-12

**Status:** completed_with_review · **Run:** `20260912T032614Z_139d`

275 question records from five verified pairs (50 + 50 + 150 + 40 + 200 = 490 marks).
9 families, 9 Understanding Models, 18 breakdowns and 18 diagnostics; 54 objects schema-valid.
46 records classified; 229 deliberately unassigned. 19 review items.
All models are `unvalidated`, `0.1.0-draft`; curriculum coverage remains unknown.

**Not saturated:** one family first observed in the final third of the new batch.
The 2022 year-end pair is rejected (160 allocated versus 170 printed); eight papers lack
local memoranda. The microorganisms ambiguity was resolved from content, not dates.
Visual-dependent records are excluded from synthesis, not silently counted as support.

Full report: `knowledge/biology/BIOLOGY_REPORT.md`.
Entry point: `python scripts/run_biology_pass2.py`; tests: `python -m pytest`.
Review queue: `review_queue/RQ-P4-BIO-PASS2.yaml`.

This supersedes the historical statement above that all non-physics subjects still have
stub Pass 1 records. Physics and the other subjects were not rebuilt or changed.
Only biology entries in the all-subject aggregate were replaced. No later phase was run.
<!-- BIOLOGY_PASS2_END -->
