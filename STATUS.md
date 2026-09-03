# Project Status

This file is auto-written by `scripts/phase1_bootstrap.py` and should be updated after each run (IMPLEMENTATION_SPEC §25). The current phase is recorded under `runs/`.

```yaml
current_phase: 3
current_subject: all
status: completed_with_review
knowledge_bank_version: null
unresolved_items: 818
last_run_id: 20260903T101928Z_b2a6
next_allowed_phase: 4
```

---

## Phase 3 re-run — this session (2026-09-03)

Phase 3 (source acquisition) for all six subjects was **re-executed in this session**
against the Phase 2 inventories (which were first restored to their Phase 2
`accessible` state so every source was genuinely re-attempted). Every accessible
authoritative source identified in Phase 2 (818 across six subjects) was attempted;
each Google Drive download failed because the sandbox terminates outbound TLS
connections (`TLS/SSL connection has been closed (EOF)`), including to generic
hosts such as `example.com`. Only `github.com` (git) is reachable.

Results were identical in kind to the earlier recorded runs, but produced a fresh
set of run IDs for this session:

- Biology: `20260903T101915Z_c3ac`
- Physics: `20260903T101916Z_175a`
- History: `20260903T101922Z_4f46`
- English: `20260903T101922Z_8ca2`
- AP Mathematics: `20260903T101925Z_8989`
- Mathematics: `20260903T101928Z_b2a6`

No source files were downloaded, no original files were modified or invented, and
no duplicate hashes were detected (no files acquired). No Phase 4 (extraction) work
was started. The earlier Phase 3 run directories remain under `runs/` as history.

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

**Run ID:** `20260903T101915Z_c3ac`

**Subject:** biology

### Outcome

Phase 3 acquisition was executed for Biology. All 52 accessible authoritative sources identified in Phase 2 were attempted. No files could be downloaded from the Google Drive URLs due to sandbox TLS/SSL connection termination. All 52 sources were updated in `data/raw/biology/SOURCE_INVENTORY.yaml` with `access_status: inaccessible`, `local_path: null`, `file_hash: null`, and detailed failure notes. No original files were modified or invented. No duplicate file hashes were detected (no files acquired).

### Deliverables

- Updated `data/raw/biology/SOURCE_INVENTORY.yaml`
- `data/raw/biology/ACQUISITION_REPORT.yaml`
- `runs/20260903T101915Z_c3ac/` — full run log (events, decisions, errors, metrics, artifacts)
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

**Run ID:** `20260903T101916Z_175a`

**Subject:** physics

### Outcome

Phase 3 acquisition was executed for Physics. All 233 accessible authoritative sources (plus 4 container folders) identified in Phase 2 were attempted. No files could be downloaded from the Google Drive URLs due to sandbox TLS/SSL connection termination. All 233 sources were updated in `data/raw/physics/SOURCE_INVENTORY.yaml` with `access_status: inaccessible` and failure notes. The 4 container folders (including the out-of-scope `IeBT P2-Chemistry folder`) remain noted but were not expanded or downloaded.

### Deliverables

- Updated `data/raw/physics/SOURCE_INVENTORY.yaml`
- `data/raw/physics/ACQUISITION_REPORT.yaml`
- `runs/20260903T101916Z_175a/` — full run log
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

**Run ID:** `20260903T101922Z_4f46`

**Subject:** history

### Outcome

Phase 3 acquisition was executed for History. All 18 accessible authoritative sources identified in Phase 2 were attempted. No files could be downloaded due to sandbox TLS/SSL restriction. All 18 sources updated to `access_status: inaccessible`. Note: the `Zipped Past Papers.zip` identified in Phase 2 remains unexpanded; it must be expanded and inspected if obtained.

### Deliverables

- Updated `data/raw/history/SOURCE_INVENTORY.yaml`
- `data/raw/history/ACQUISITION_REPORT.yaml`
- `runs/20260903T101922Z_4f46/` — full run log
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

**Run ID:** `20260903T101922Z_8ca2`

**Subject:** english

### Outcome

Phase 3 acquisition was executed for English. All 100 accessible authoritative sources identified in Phase 2 were attempted. No files could be downloaded due to sandbox TLS/SSL restriction. All 100 sources updated to `access_status: inaccessible`. No original files were modified.

### Deliverables

- Updated `data/raw/english/SOURCE_INVENTORY.yaml`
- `data/raw/english/ACQUISITION_REPORT.yaml`
- `runs/20260903T101922Z_8ca2/` — full run log
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

**Run ID:** `20260903T101925Z_8989`

**Subject:** ap_mathematics

### Outcome

Phase 3 acquisition was executed for AP Mathematics. 145 accessible authoritative sources were attempted (1 external source excluded); no files could be downloaded due to sandbox TLS/SSL restriction. All 145 sources updated to `access_status: inaccessible`. The 1 external source (`stithian.com` formula sheet) remains marked `external` and requires grade-applicability verification before use.

### Deliverables

- Updated `data/raw/ap_mathematics/SOURCE_INVENTORY.yaml`
- `data/raw/ap_mathematics/ACQUISITION_REPORT.yaml`
- `runs/20260903T101925Z_8989/` — full run log
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

**Run ID:** `20260903T101928Z_b2a6`

**Subject:** mathematics

### Outcome

Phase 3 acquisition was executed for Mathematics. 270 accessible authoritative sources were attempted (2 external sources excluded); no files could be downloaded due to sandbox TLS/SSL restriction. All 270 sources updated to `access_status: inaccessible`. The 2 external sources (`stithian.com`, Mindbourne portal) remain marked `external` and require grade-applicability verification.

### Deliverables

- Updated `data/raw/mathematics/SOURCE_INVENTORY.yaml`
- `data/raw/mathematics/ACQUISITION_REPORT.yaml`
- `runs/20260903T101928Z_b2a6/` — full run log
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

- Biology: `20260903T101915Z_c3ac`
- Physics: `20260903T101916Z_175a`
- History: `20260903T101922Z_4f46`
- English: `20260903T101922Z_8ca2`
- AP Mathematics: `20260903T101925Z_8989`
- Mathematics: `20260903T101928Z_b2a6`

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

## Next Phase

**Phase 4 — Extract source content.** Do NOT start Phase 4 until Phase 3 acquisition failures are resolved for all six subjects. Every source must have a preserved original file (`local_path`) and a verified SHA-256 hash (`file_hash`) before extraction can proceed responsibly.
