# Project Status

This file is auto-written by `scripts/phase1_bootstrap.py` and should be updated after each run (IMPLEMENTATION_SPEC §25). The current phase is recorded under `runs/`.

```yaml
current_phase: 4
current_subject: all
status: blocked
knowledge_bank_version: null
unresolved_items: 818
last_run_id: 20260903T094155Z_c04f
next_allowed_phase: 4
```

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

## Phase 4A — Biology Extraction

**Status:** blocked

**Run ID:** `20260903T094153Z_264a`

### Outcome

Phase 4 extraction was executed for biology. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 52 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/biology/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/biology/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-BIO-EXTRACTION.yaml`
- `runs/20260903T094153Z_264a/` — full run log (events, decisions, errors, metrics, artifacts)

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

**Run ID:** `20260903T094153Z_392b`

### Outcome

Phase 4 extraction was executed for physics. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 233 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/physics/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/physics/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-PHY-EXTRACTION.yaml`
- `runs/20260903T094153Z_392b/` — full run log (events, decisions, errors, metrics, artifacts)

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

**Run ID:** `20260903T094154Z_f08a`

### Outcome

Phase 4 extraction was executed for history. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 18 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/history/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/history/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-HIS-EXTRACTION.yaml`
- `runs/20260903T094154Z_f08a/` — full run log (events, decisions, errors, metrics, artifacts)

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

**Run ID:** `20260903T094154Z_0671`

### Outcome

Phase 4 extraction was executed for english. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 100 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/english/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/english/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-ENG-EXTRACTION.yaml`
- `runs/20260903T094154Z_0671/` — full run log (events, decisions, errors, metrics, artifacts)

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

**Run ID:** `20260903T094154Z_85c3`

### Outcome

Phase 4 extraction was executed for ap_mathematics. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 145 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/ap_mathematics/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/ap_mathematics/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-APM-EXTRACTION.yaml`
- `runs/20260903T094154Z_85c3/` — full run log (events, decisions, errors, metrics, artifacts)

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

**Run ID:** `20260903T094155Z_c04f`

### Outcome

Phase 4 extraction was executed for mathematics. The gate check confirmed there is **no acquired corpus**: Phase 3 preserved 0 of 270 sources requiring extraction (all `access_status: inaccessible`, `local_path: null`, `file_hash: null`). The sandbox TLS restriction to Google Drive was re-probed and is still present. With zero preserved originals there were no pages to extract text from, no tables, figures, diagrams, headers/footers, question numbers or mark allocations to preserve, no extraction confidence to record, and no pages to flag for visual verification. No text was invented and no external material was substituted. The run is marked **blocked** (RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was not started.

---

### Deliverables

- `data/raw/mathematics/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report
- `data/extracted/mathematics/` — structural placeholder only (`.gitkeep`); no artifacts
- `review_queue/RQ-P4-MAT-EXTRACTION.yaml`
- `runs/20260903T094155Z_c04f/` — full run log (events, decisions, errors, metrics, artifacts)

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
- Biology: `20260903T094153Z_264a`
- Physics: `20260903T094153Z_392b`
- History: `20260903T094154Z_f08a`
- English: `20260903T094154Z_0671`
- AP Mathematics: `20260903T094154Z_85c3`
- Mathematics: `20260903T094155Z_c04f`

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

**Phase 4 — Extract source content (BLOCKED).** Do NOT re-run Phase 4
until Phase 3 acquisition is resolved: every source must have a preserved
original file (`local_path`) and a verified SHA-256 hash (`file_hash`)
before extraction can proceed. Extraction must not invent, substitute or
simulate source text. Once originals are preserved, re-run Phase 4 per
subject; do not proceed to Phase 5 until extraction is unblocked and
validated.
