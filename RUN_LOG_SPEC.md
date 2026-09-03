# Run and Decision Logging Specification

**Version:** 1.0.0

---

# 1. Purpose

Every autonomous execution must leave an auditable record.

The repository must allow a future reader to determine:

* what the agent did
* when it did it
* what sources it used
* what artifacts it created
* what decisions it made
* what failed
* what was unresolved
* what version of the knowledge bank resulted

---

# 2. Run directory

Every execution receives a unique run ID.

Example:

```text
runs/
  2026-09-03T084100Z_a91f/
```

Each run contains:

```text
run.json
events.jsonl
decisions.json
errors.json
metrics.json
artifacts/
```

---

# 3. run.json

Minimum fields:

```yaml
run_id:
started_at:
completed_at:
phase:
subject:
spec_version:
implementation_spec_version:
agent_version:
model:
model_provider:
git_commit_before:
git_commit_after:
status:
```

---

# 4. events.jsonl

Record significant execution events.

Examples:

```text
SOURCE_DISCOVERED
SOURCE_ACQUIRED
SOURCE_SKIPPED
SOURCE_DUPLICATE
EXTRACTION_STARTED
EXTRACTION_COMPLETED
EXTRACTION_UNCERTAIN
QUESTION_SEGMENTED
MEMO_ALIGNED
QUESTION_CLASSIFIED
QUESTION_UNCLASSIFIED
UNDERSTANDING_MODEL_CREATED
BREAKDOWN_CREATED
DIAGNOSTIC_CREATED
VALIDATION_STARTED
VALIDATION_FAILED
REVIEW_REQUIRED
VERSION_FROZEN
TEST_STARTED
TEST_FAILED
TEST_PASSED
```

Each event should contain:

```json
{
  "timestamp": "...",
  "event": "...",
  "subject": "...",
  "entity_id": "...",
  "message": "...",
  "metadata": {}
}
```

---

# 5. Decision log

Every important analytical decision goes into:

```text
decisions.json
```

Each decision should contain:

```json
{
  "decision_id": "DEC-0042",
  "timestamp": "...",
  "phase": 8,
  "subject": "biology",
  "decision_type": "question_family_merge",
  "context": "...",
  "evidence": [
    "BIO-2024-T2-Q3.1",
    "BIO-2025-T1-Q5.2"
  ],
  "alternatives": [
    "keep separate",
    "merge"
  ],
  "selected": "merge",
  "rationale": "...",
  "confidence": "high",
  "requires_review": false
}
```

---

# 6. Errors

All significant errors must be recorded in:

```text
errors.json
```

Record:

```text
timestamp
phase
subject
error_type
message
affected_artifact
retry_attempts
resolution
status
```

---

# 7. Metrics

Every phase should produce machine-readable metrics.

Examples:

```yaml
papers_discovered:
papers_acquired:
papers_processed:
questions_extracted:
questions_classified:
questions_unclassified:
memo_alignment_rate:
curriculum_mapping_rate:
understanding_models:
breakdowns:
diagnostics:
unresolved_items:
validation_failures:
```

---

# 8. Artifact manifest

Every run should record the artifacts it created or modified.

Example:

```yaml
artifact_id:
path:
type:
created_or_modified:
source_run:
content_hash:
```

---

# 9. Provenance

Every derived knowledge artifact must be traceable through IDs.

Example:

```text
UNDERSTANDING-MATH-014
        ↓
QUESTION-FAMILY-MATH-007
        ↓
MATH-2025-T2-Q4.2
        ↓
MATH-2025-T2-MEMO-Q4.2
        ↓
SOURCE-ORC-MATH-2025-T2-01
```

---

# 10. Human review queue

Create:

```text
review_queue/
```

Use it whenever the system encounters:

* inaccessible source
* ambiguous extraction
* uncertain question segmentation
* uncertain memo alignment
* disputed question classification
* uncertain curriculum mapping
* low-confidence Understanding Model
* conflicting source evidence

Each item must state:

```text
issue
affected entity
evidence
possible resolutions
recommended review
```

---

# 11. Run completion

A run may be marked:

```text
completed
completed_with_review
blocked
failed
```

`completed` means the phase's acceptance criteria passed.

`completed_with_review` means the phase completed but has explicitly recorded unresolved review items.

`blocked` means the next work cannot responsibly continue without resolving a dependency.

`failed` means the phase could not complete.

Never use `completed` simply because the code ran without crashing.
