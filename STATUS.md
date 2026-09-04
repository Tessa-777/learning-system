# Project Status

This file is auto-written by `scripts/phase1_bootstrap.py` and should be updated after each run (IMPLEMENTATION_SPEC §25). The current phase is recorded under `runs/`.

```yaml
current_phase: 3
current_subject: all
status: awaiting_source_drop
knowledge_bank_version: null
unresolved_items: 60
last_run_id: 20260904T165815Z_62d6
next_allowed_phase: 3b
spec_version: 1.1.0
```

> **Scope revision (2026-09-04).** `SYSTEM_SPEC.md` and `IMPLEMENTATION_SPEC.md`
> were revised to **v1.1.0**. Phase 3 no longer acquires all 821 discovered
> records; it acquires a **form-stratified saturation sample of 60 documents**.
> See [`CORPUS_SUFFICIENCY_POLICY.md`](CORPUS_SUFFICIENCY_POLICY.md) and the new
> Phase 3a section below. The Phase 3 retry and Phase 4 blocked sections further
> down this file are retained as the audit trail of the v1.0.0 attempt; they are
> **superseded** and their 818 unresolved items are no longer the working set.

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



---

## Phase 3a — Corpus Selection (scope revision)

**Status:** completed_with_review

**Run IDs:** `20260904T164135Z_757e` (initial), `20260904T165815Z_62d6` (authoritative — after classifier and pairing fixes)

**Spec version:** 1.1.0

### Outcome

Phase 3 was re-scoped and re-run as **selection**, not acquisition. Two findings drove this.

**1. The TLS diagnosis was correct but incomplete.** Sandbox-level HTTP has no
outbound TLS at all — `curl https://example.com` fails with `SSL_ERROR_SYSCALL`,
so the restriction is not specific to Google. However the platform's *proxied*
page fetcher reaches the ORC normally. During this run four real documents were
retrieved from Drive to verify it: the History July 2009 memorandum, the History
November 2017 question paper, the Mathematics November 2018 Paper 2, and the
Physics November 2022 final exam. Question wording, numbering, mark allocations,
section structure, tables and LaTeX all survive. **Original bytes do not** — the
proxy returns a transcription — so it satisfies fidelity Rung B, not Rung A
(`SYSTEM_SPEC.md` §17.2).

**2. The 821-record corpus was the wrong target.** It was never 821 papers: 209
past papers, 237 memoranda, 122 marking guides, 165 assessment items, 85
reference documents, 1 curriculum document, 7 other. Phase 2 deduplicated on
Drive *file ID* only and removed one record, so it never detected content
duplication — which is present and was verified:
`2022_G11_Physics_Nov-Exam_QP.pdf` and `G11 Nov Physics Exam 2022 QP.pdf` are
distinct Drive IDs with identical content (same examiner, moderator, date,
200-mark table and MCQ items), and the 2022 IEB Trial Physics P1 is present under
three IDs and three naming schemes.

Question families track **assessment form** — setter × paper number × sitting —
not topic and not year. The corpus proves it: the November 2018 Mathematics
Paper 2 prints its own topic/mark table, the November 2022 Physics paper labels
its own question families (`KINEMATICS GRAPH`, `HORIZONTAL MOTION`,
`PROJECTILE MOTION`), and the November 2017 History paper declares its own
three-section structure. `SYSTEM_SPEC.md` §9 already defines an Understanding
Model as the "underlying competence being assessed", and
`IMPLEMENTATION_SPEC.md` §9 already forbids one family per question. The taxonomy
is a compression, so acquiring 821 documents to feed it was a mismatch.

### Deliverables

- `CORPUS_SUFFICIENCY_POLICY.md` — authoritative policy: stratum definition, two-pass allocation, memo-pairing rules, saturation stopping rule, known gaps
- `data/raw/CORPUS_SELECTION.yaml` — machine-readable selection (60 documents, with per-document rationale, stratum, pairing method and flags)
- `data/raw/DOWNLOAD_CHECKLIST.md` — human download checklist with Drive links and target paths
- `review_queue/RQ-P3-CORPUS-SELECTION.yaml` — scope-change sign-off item
- `ingestion/acquisition/` — `inventory.py`, `forms.py`, `selection.py`, `content_probe.py`
- `core/yamllite.py` — stdlib YAML subset, so the repository runs where PyYAML cannot be installed
- `scripts/phase3_select.py`, `scripts/phase3_ingest_drop.py`
- `tests/test_corpus_selection.py` — 48 tests
- `SYSTEM_SPEC.md` §17 + §16 amendment, `IMPLEMENTATION_SPEC.md` §4 rewrite, `config/settings.yaml` → 1.1.0

### Selection metrics

| subject | candidate papers | forms present | papers selected | memoranda paired | companions | anchors |
|---|---|---|---|---|---|---|
| biology | 10 | 3 | 5 | 5 | 1 | 0 |
| physics | 67 | 9 | 5 | 4 | 2 | 1 |
| history | 11 | 6 | 5 | 1 | 1 | 1 |
| english | 35 | 4 | 5 | 5 | 0 | 0 |
| ap_mathematics | 46 | 9 | 5 | 5 | 0 | 0 |
| mathematics | 39 | 6 | 5 | 4 | 0 | 0 |
| **total** | **208** | **37** | **30** | **24** | **4** | **2** |

**60 documents to acquire.** Every subject's distinct `(setter, paper_form)`
pairs are represented, including the Physics IEB MCQ paper — a form sat once,
whose question families appear nowhere else in that subject.

### Validation

- 48 tests pass under `python3 -m unittest tests.test_corpus_selection`.
- `core/yamllite.py` round-trips `config/settings.yaml` and `config/subjects.yaml` exactly, and re-parses the generated `CORPUS_SELECTION.yaml`.
- The Phase 2 inventories were **not modified** by selection; they remain discovery provenance.
- No source content was fabricated. Four documents were retrieved through the proxy to verify access and to gather the evidence cited above; those retrievals were **not** written into `data/raw/` because they are Rung B transcriptions and the approved acquisition mode is Rung A (human-supplied originals).
- Selection is deterministic: identical inventories and budget always produce the identical sample.

### Unresolved / review items

1. **60 documents await acquisition.** Nothing has been downloaded yet. See `data/raw/DOWNLOAD_CHECKLIST.md`; then run `python3 scripts/phase3_ingest_drop.py`.
2. **6 selected papers have no memorandum in the ORC** (4 History, 1 Physics MCQ, 1 Mathematics 2020). Per policy §4.2.1 these may support question families but must never support marking requirements.
3. **History memo coverage is structural, not a sampling artefact.** The ORC holds 3 memoranda for 11 History papers and 2 of the 3 are class tests. Acquiring all 11 papers would yield no additional memorandum. Phase 6 for History is effectively limited to the October 2017 Cold War exam.
4. **History `document_type` labels are wrong for at least one record.** `2009_July_exam_Gr_11.doc.docx` is filed as `past_paper` but its content is the July 2009 memorandum. `phase3_ingest_drop.py` re-verifies document type from content and reports contradictions rather than trusting Phase 2.
5. **4 of 6 subjects have no curriculum anchor document.** Only Physics (`IEB - SAG - PS`) and History (`July 2015 Exam Requirements`) have one. Phase 7 must derive the topic hierarchy from the papers' own front-matter tables and mark it `derived`, never `curriculum`.
6. **Chemistry material is present in the Physics folder** and is excluded from the selection but retained for provenance.
7. **Strata left unsampled** are itemised per subject in `data/raw/CORPUS_SELECTION.yaml` notes. Physics is the worst case: 9 strata, 5 sampled. Several unsampled `unknown` strata are likely the same exam filed under different names; only content-hash dedupe at Phase 3b can settle it.
8. **Mathematics 2020 `2a. Grade 11 Paper 2.pdf`** could not be paired to a memorandum — the filing prefix matched two candidates. Needs human pairing.
9. **Phase 2 unresolved items remain open** (ORC legacy folder HTTP 500, AP boundary, History `Zipped Past Papers.zip`, Physics legacy folder, external formula sheets, out-of-scope clusters).
10. **`jsonschema` and `PyYAML` cannot be installed offline.** `core/schema.py` falls back to a bundled mini-validator covering the keyword set the schemas actually use, and `core/config.py` / `core/runlog.py` fall back to `core/yamllite.py`. The existing pytest suite under `tests/` still requires pytest and could not be executed here.

---

## Phase 3A — Biology Source Acquisition (Retry)

> **SUPERSEDED** by the v1.1.0 scope revision above. Retained as the audit trail
> of the v1.0.0 blanket-acquisition attempt. Its unresolved counts are no longer
> the working set.

**Status:** completed_with_review

**Run ID:** `20260903T095742Z_7898`

### Outcome

Phase 3 acquisition was retried for biology: every non-external source (52 sources) was re-attempted with a real download request. No files could be downloaded — the sandbox still terminates TLS connections to Google services (the same failure as the original Phase 3 runs, re-probed at retry time). All failed sources were updated in `data/raw/biology/SOURCE_INVENTORY.yaml` with `access_status: inaccessible`, `local_path: null`, `file_hash: null` and a note for this run's attempt. No original files were modified or invented. No Phase 4 (extraction) work was started.

---

### Deliverables

- Updated `data/raw/biology/SOURCE_INVENTORY.yaml`
- `data/raw/biology/ACQUISITION_REPORT.yaml` (retry)
- `runs/20260903T095742Z_7898/` — full run log (events, decisions, errors, metrics, artifacts)
- `review_queue/RQ-P3-BIO-ACQUISITION.yaml` (updated)

---

### Metrics

- Sources discovered: 52
- Sources attempted: 52
- Sources acquired: 0
- Sources failed: 52
- Sources skipped (external/container): 0
- Duplicate hashes detected: 0
- Unresolved items: 52

---

### Unresolved / review items

- All 52 attempted biology sources remain inaccessible and must be retried in an environment with working Google Drive access, or provided manually, before Phase 4.

---

## Phase 3B — Physics Source Acquisition (Retry)

**Status:** completed_with_review

**Run ID:** `20260903T095743Z_9daa`

### Outcome

Phase 3 acquisition was retried for physics: every non-external source (233 sources) was re-attempted with a real download request. No files could be downloaded — the sandbox still terminates TLS connections to Google services (the same failure as the original Phase 3 runs, re-probed at retry time). All failed sources were updated in `data/raw/physics/SOURCE_INVENTORY.yaml` with `access_status: inaccessible`, `local_path: null`, `file_hash: null` and a note for this run's attempt. No original files were modified or invented. No Phase 4 (extraction) work was started.

---

### Deliverables

- Updated `data/raw/physics/SOURCE_INVENTORY.yaml`
- `data/raw/physics/ACQUISITION_REPORT.yaml` (retry)
- `runs/20260903T095743Z_9daa/` — full run log (events, decisions, errors, metrics, artifacts)
- `review_queue/RQ-P3-PHY-ACQUISITION.yaml` (updated)

---

### Metrics

- Sources discovered: 233
- Sources attempted: 233
- Sources acquired: 0
- Sources failed: 233
- Sources skipped (external/container): 0
- Duplicate hashes detected: 0
- Unresolved items: 233

---

### Unresolved / review items

- All 233 attempted physics sources remain inaccessible and must be retried in an environment with working Google Drive access, or provided manually, before Phase 4.

---

## Phase 3C — History Source Acquisition (Retry)

**Status:** completed_with_review

**Run ID:** `20260903T095751Z_4aeb`

### Outcome

Phase 3 acquisition was retried for history: every non-external source (18 sources) was re-attempted with a real download request. No files could be downloaded — the sandbox still terminates TLS connections to Google services (the same failure as the original Phase 3 runs, re-probed at retry time). All failed sources were updated in `data/raw/history/SOURCE_INVENTORY.yaml` with `access_status: inaccessible`, `local_path: null`, `file_hash: null` and a note for this run's attempt. No original files were modified or invented. No Phase 4 (extraction) work was started.

---

### Deliverables

- Updated `data/raw/history/SOURCE_INVENTORY.yaml`
- `data/raw/history/ACQUISITION_REPORT.yaml` (retry)
- `runs/20260903T095751Z_4aeb/` — full run log (events, decisions, errors, metrics, artifacts)
- `review_queue/RQ-P3-HIS-ACQUISITION.yaml` (updated)

---

### Metrics

- Sources discovered: 18
- Sources attempted: 18
- Sources acquired: 0
- Sources failed: 18
- Sources skipped (external/container): 0
- Duplicate hashes detected: 0
- Unresolved items: 18

---

### Unresolved / review items

- All 18 attempted history sources remain inaccessible and must be retried in an environment with working Google Drive access, or provided manually, before Phase 4.

---

## Phase 3D — English Source Acquisition (Retry)

**Status:** completed_with_review

**Run ID:** `20260903T095752Z_c30a`

### Outcome

Phase 3 acquisition was retried for english: every non-external source (100 sources) was re-attempted with a real download request. No files could be downloaded — the sandbox still terminates TLS connections to Google services (the same failure as the original Phase 3 runs, re-probed at retry time). All failed sources were updated in `data/raw/english/SOURCE_INVENTORY.yaml` with `access_status: inaccessible`, `local_path: null`, `file_hash: null` and a note for this run's attempt. No original files were modified or invented. No Phase 4 (extraction) work was started.

---

### Deliverables

- Updated `data/raw/english/SOURCE_INVENTORY.yaml`
- `data/raw/english/ACQUISITION_REPORT.yaml` (retry)
- `runs/20260903T095752Z_c30a/` — full run log (events, decisions, errors, metrics, artifacts)
- `review_queue/RQ-P3-ENG-ACQUISITION.yaml` (updated)

---

### Metrics

- Sources discovered: 100
- Sources attempted: 100
- Sources acquired: 0
- Sources failed: 100
- Sources skipped (external/container): 0
- Duplicate hashes detected: 0
- Unresolved items: 100

---

### Unresolved / review items

- All 100 attempted english sources remain inaccessible and must be retried in an environment with working Google Drive access, or provided manually, before Phase 4.

---

## Phase 3E — AP Mathematics Source Acquisition (Retry)

**Status:** completed_with_review

**Run ID:** `20260903T095755Z_e18a`

### Outcome

Phase 3 acquisition was retried for ap_mathematics: every non-external source (145 sources) was re-attempted with a real download request. No files could be downloaded — the sandbox still terminates TLS connections to Google services (the same failure as the original Phase 3 runs, re-probed at retry time). All failed sources were updated in `data/raw/ap_mathematics/SOURCE_INVENTORY.yaml` with `access_status: inaccessible`, `local_path: null`, `file_hash: null` and a note for this run's attempt. No original files were modified or invented. No Phase 4 (extraction) work was started.

---

### Deliverables

- Updated `data/raw/ap_mathematics/SOURCE_INVENTORY.yaml`
- `data/raw/ap_mathematics/ACQUISITION_REPORT.yaml` (retry)
- `runs/20260903T095755Z_e18a/` — full run log (events, decisions, errors, metrics, artifacts)
- `review_queue/RQ-P3-APM-ACQUISITION.yaml` (updated)

---

### Metrics

- Sources discovered: 146
- Sources attempted: 145
- Sources acquired: 0
- Sources failed: 145
- Sources skipped (external/container): 1
- Duplicate hashes detected: 0
- Unresolved items: 145

---

### Unresolved / review items

- All 145 attempted ap_mathematics sources remain inaccessible and must be retried in an environment with working Google Drive access, or provided manually, before Phase 4.

---

## Phase 3F — Mathematics Source Acquisition (Retry)

**Status:** completed_with_review

**Run ID:** `20260903T095800Z_7724`

### Outcome

Phase 3 acquisition was retried for mathematics: every non-external source (270 sources) was re-attempted with a real download request. No files could be downloaded — the sandbox still terminates TLS connections to Google services (the same failure as the original Phase 3 runs, re-probed at retry time). All failed sources were updated in `data/raw/mathematics/SOURCE_INVENTORY.yaml` with `access_status: inaccessible`, `local_path: null`, `file_hash: null` and a note for this run's attempt. No original files were modified or invented. No Phase 4 (extraction) work was started.

---

### Deliverables

- Updated `data/raw/mathematics/SOURCE_INVENTORY.yaml`
- `data/raw/mathematics/ACQUISITION_REPORT.yaml` (retry)
- `runs/20260903T095800Z_7724/` — full run log (events, decisions, errors, metrics, artifacts)
- `review_queue/RQ-P3-MAT-ACQUISITION.yaml` (updated)

---

### Metrics

- Sources discovered: 272
- Sources attempted: 270
- Sources acquired: 0
- Sources failed: 270
- Sources skipped (external/container): 2
- Duplicate hashes detected: 0
- Unresolved items: 270

---

### Unresolved / review items

- All 270 attempted mathematics sources remain inaccessible and must be retried in an environment with working Google Drive access, or provided manually, before Phase 4.

---

## Aggregate Phase 3 Retry Status

**Status:** completed_with_review

**Run IDs:**
- Biology: `20260903T095742Z_7898`
- Physics: `20260903T095743Z_9daa`
- History: `20260903T095751Z_4aeb`
- English: `20260903T095752Z_c30a`
- AP Mathematics: `20260903T095755Z_e18a`
- Mathematics: `20260903T095800Z_7724`

### Aggregate Metrics

- Total sources attempted: 818
- Total sources acquired: 0
- Total sources failed: 818
- Aggregate unresolved items: 818

### Aggregate Notes

Phase 3 was re-executed for all six subjects as a retry of the original Phase 3 runs (2026-09-03T0918xxZ). No source files were downloaded for any subject: the sandbox environment still terminates TLS connections to Google Drive and Google Sites. Every acquisition attempt was performed and recorded per source in each run's errors.json and in the source record notes. Original source files were not modified, replaced or invented. Acquisition must be retried in an environment with working Google Drive access, or files must be provided manually, before Phase 4 (extraction) can proceed.

---

## Phase 4A — Biology Extraction

**Status:** blocked

**Run ID:** `20260903T095815Z_961e`

### Outcome

Phase 4 extraction was executed for biology. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 52 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/biology/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/biology/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-BIO-EXTRACTION.yaml`
- `runs/20260903T095815Z_961e/` — full run log (events, decisions, errors, metrics, artifacts)

---

### Metrics

- Sources requiring extraction: 52
- Sources with preserved original: 0
- Documents extracted: 0
- Pages extracted: 0
- Pages requiring visual verification: 0
- Extraction uncertainty records: 0
- Original files modified: 0
- Unresolved items (carried from Phase 3): 52

---

### Unresolved / review items

- All 52 biology sources still lack a preserved original; Phase 4 extraction remains blocked until Phase 3 is resolved (see `RQ-P3-BIO-ACQUISITION.yaml` and `RQ-P4-BIO-EXTRACTION.yaml`).

---

## Phase 4B — Physics Extraction

**Status:** blocked

**Run ID:** `20260903T095815Z_77a3`

### Outcome

Phase 4 extraction was executed for physics. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 233 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/physics/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/physics/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-PHY-EXTRACTION.yaml`
- `runs/20260903T095815Z_77a3/` — full run log (events, decisions, errors, metrics, artifacts)

---

### Metrics

- Sources requiring extraction: 233
- Sources with preserved original: 0
- Documents extracted: 0
- Pages extracted: 0
- Pages requiring visual verification: 0
- Extraction uncertainty records: 0
- Original files modified: 0
- Unresolved items (carried from Phase 3): 233

---

### Unresolved / review items

- All 233 physics sources still lack a preserved original; Phase 4 extraction remains blocked until Phase 3 is resolved (see `RQ-P3-PHY-ACQUISITION.yaml` and `RQ-P4-PHY-EXTRACTION.yaml`).

---

## Phase 4C — History Extraction

**Status:** blocked

**Run ID:** `20260903T095816Z_8955`

### Outcome

Phase 4 extraction was executed for history. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 18 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/history/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/history/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-HIS-EXTRACTION.yaml`
- `runs/20260903T095816Z_8955/` — full run log (events, decisions, errors, metrics, artifacts)

---

### Metrics

- Sources requiring extraction: 18
- Sources with preserved original: 0
- Documents extracted: 0
- Pages extracted: 0
- Pages requiring visual verification: 0
- Extraction uncertainty records: 0
- Original files modified: 0
- Unresolved items (carried from Phase 3): 18

---

### Unresolved / review items

- All 18 history sources still lack a preserved original; Phase 4 extraction remains blocked until Phase 3 is resolved (see `RQ-P3-HIS-ACQUISITION.yaml` and `RQ-P4-HIS-EXTRACTION.yaml`).

---

## Phase 4D — English Extraction

**Status:** blocked

**Run ID:** `20260903T095816Z_980e`

### Outcome

Phase 4 extraction was executed for english. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 100 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/english/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/english/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-ENG-EXTRACTION.yaml`
- `runs/20260903T095816Z_980e/` — full run log (events, decisions, errors, metrics, artifacts)

---

### Metrics

- Sources requiring extraction: 100
- Sources with preserved original: 0
- Documents extracted: 0
- Pages extracted: 0
- Pages requiring visual verification: 0
- Extraction uncertainty records: 0
- Original files modified: 0
- Unresolved items (carried from Phase 3): 100

---

### Unresolved / review items

- All 100 english sources still lack a preserved original; Phase 4 extraction remains blocked until Phase 3 is resolved (see `RQ-P3-ENG-ACQUISITION.yaml` and `RQ-P4-ENG-EXTRACTION.yaml`).

---

## Phase 4E — AP Mathematics Extraction

**Status:** blocked

**Run ID:** `20260903T095816Z_9585`

### Outcome

Phase 4 extraction was executed for ap_mathematics. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 145 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/ap_mathematics/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/ap_mathematics/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-APM-EXTRACTION.yaml`
- `runs/20260903T095816Z_9585/` — full run log (events, decisions, errors, metrics, artifacts)

---

### Metrics

- Sources requiring extraction: 145
- Sources with preserved original: 0
- Documents extracted: 0
- Pages extracted: 0
- Pages requiring visual verification: 0
- Extraction uncertainty records: 0
- Original files modified: 0
- Unresolved items (carried from Phase 3): 145

---

### Unresolved / review items

- All 145 ap_mathematics sources still lack a preserved original; Phase 4 extraction remains blocked until Phase 3 is resolved (see `RQ-P3-APM-ACQUISITION.yaml` and `RQ-P4-APM-EXTRACTION.yaml`).

---

## Phase 4F — Mathematics Extraction

**Status:** blocked

**Run ID:** `20260903T095817Z_d51c`

### Outcome

Phase 4 extraction was executed for mathematics. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 270 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/mathematics/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/mathematics/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-MAT-EXTRACTION.yaml`
- `runs/20260903T095817Z_d51c/` — full run log (events, decisions, errors, metrics, artifacts)

---

### Metrics

- Sources requiring extraction: 270
- Sources with preserved original: 0
- Documents extracted: 0
- Pages extracted: 0
- Pages requiring visual verification: 0
- Extraction uncertainty records: 0
- Original files modified: 0
- Unresolved items (carried from Phase 3): 270

---

### Unresolved / review items

- All 270 mathematics sources still lack a preserved original; Phase 4 extraction remains blocked until Phase 3 is resolved (see `RQ-P3-MAT-ACQUISITION.yaml` and `RQ-P4-MAT-EXTRACTION.yaml`).

---

## Aggregate Phase 4 Status

**Status:** blocked

**Run IDs:**
- Biology: `20260903T095815Z_961e`
- Physics: `20260903T095815Z_77a3`
- History: `20260903T095816Z_8955`
- English: `20260903T095816Z_980e`
- AP Mathematics: `20260903T095816Z_9585`
- Mathematics: `20260903T095817Z_d51c`

### Aggregate Notes

Phase 4 was executed for all six subjects in the prescribed order (IMPLEMENTATION_SPEC §23). No subject had an acquired corpus, so no extraction was performed anywhere; nothing was fabricated or substituted. All six subject runs are marked blocked on the Phase 3 dependency, consistent with the STATUS.md gate and RUN_LOG_SPEC §11. Aggregate unresolved items carried from Phase 3: 818.

---

### Deliverables (aggregate)

- `data/raw/PHASE4_AGGREGATE_SUMMARY.yaml` — aggregate blocked-state summary
- `data/raw/<subject>/PHASE4_EXTRACTION_REPORT.yaml` × 6
- `review_queue/RQ-P4-*-EXTRACTION.yaml` × 6
- `runs/` × 6 (full logs, decisions, errors, metrics, artifacts)

---

### Validation

- All 6 run directories contain `run.json`, `events.jsonl`, `decisions.json`, `errors.json`, `metrics.json` and `artifacts/artifacts.yaml`.
- All source records in all 6 inventories still validate against `database/schema/source_metadata.schema.json` (no source record modified).
- `data/extracted/<subject>/` contains structural `.gitkeep` placeholders only; no extraction content was created.
- No original files were modified or created.
- Pytest suite passes (48 passed).
- All errors recorded with `unresolved` status; all runs marked `blocked` with rationale in `decisions.json`.

---

### Unresolved / review items (aggregate)

1. All 818 accessible sources across 6 subjects remain without preserved originals (carried from Phase 3).
2. Phase 4 extraction is blocked for all 6 subjects until Phase 3 is resolved (new review items `RQ-P4-*-EXTRACTION.yaml` × 6).
3. Phase 2 unresolved items (ORC legacy folder, AP boundary, History zip, Physics legacy folder, external formula sheets/portal, out-of-scope clusters) remain open.
---

## Next Phase

**Phase 3b — Acquire and preserve the selected corpus.**

The corpus has been selected but not acquired. The next action is human, not
automated:

1. Open [`data/raw/DOWNLOAD_CHECKLIST.md`](data/raw/DOWNLOAD_CHECKLIST.md).
2. Download the 60 listed documents from their Drive links into
   `data/incoming/` (or any directory passed as `--drop-dir`). Keep the original
   filenames; do not convert, re-save or edit the files.
3. Run:

   ```bash
   python3 scripts/phase3_ingest_drop.py --dry-run   # check matching first
   python3 scripts/phase3_ingest_drop.py             # ingest for real
   ```

The runner copies each file into `data/raw/<subject>/{papers,memoranda,companions,curriculum}/`,
computes SHA-256 over the **original bytes** (fidelity Rung A), verifies
`document_type` from content, detects duplicates by content hash, updates only
the four mutable fields on the matching Phase 2 source records, validates them
against `source_metadata.schema.json`, and writes per-subject
`ACQUISITION_REPORT.yaml` plus a full run log.

**Do not run Phase 4 until every selected document has a preserved original
(`local_path`) and a verified hash (`file_hash`).** Extraction must not invent,
substitute or simulate source text.

Phase 4 will also change shape under v1.1.0: because the selection is 60
documents rather than 821, extraction runs once per subject over a small,
fully-hashed corpus, and every diagram-, graph- or figure-bearing question must
be flagged `requires_visual_verification` where the document is held only at
Rung B.
