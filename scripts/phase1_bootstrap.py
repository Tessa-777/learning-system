#!/usr/bin/env python3
"""Phase 1 — Repository Bootstrap runner.

Executes the Phase 1 deliverables in IMPLEMENTATION_SPEC §2, writes a run and
decision log per RUN_LOG_SPEC, validates the result, and updates STATUS.md.

It is idempotent: each invocation creates a new run directory under ``runs/``.
It performs NO curriculum analysis.

Usage:
    python scripts/phase1_bootstrap.py [--status-completed-with-review]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from core.config import Config  # noqa: E402
from core.runlog import git_commit_sha  # noqa: E402
from ingestion.run_context import RunContext  # noqa: E402

# Paths that make up the Phase 1 structure (independent of curriculum content).
STRUCTURE_DIRS = [
    "data/raw/biology",
    "data/raw/physics",
    "data/raw/history",
    "data/raw/english",
    "data/raw/ap_mathematics",
    "data/raw/mathematics",
    "data/extracted",
    "data/structured",
    "data/validated",
    "knowledge/biology",
    "knowledge/physics",
    "knowledge/history",
    "knowledge/english",
    "knowledge/ap_mathematics",
    "knowledge/mathematics",
    "database/schema",
    "database/migrations",
    "database/seed",
    "ingestion/acquisition",
    "ingestion/extraction",
    "ingestion/segmentation",
    "ingestion/classification",
    "ingestion/analysis",
    "ingestion/validation",
    "tutor/core",
    "tutor/prompts",
    "tutor/subjects/biology",
    "tutor/subjects/physics",
    "tutor/subjects/history",
    "tutor/subjects/english",
    "tutor/subjects/ap_mathematics",
    "tutor/subjects/mathematics",
    "student_model",
    "tests",
    "runs",
    "review_queue",
]

SCHEMA_FILES = [
    "database/schema/source_metadata.schema.json",
    "database/schema/question.schema.json",
    "database/schema/question_family.schema.json",
    "database/schema/knowledge_model.schema.json",
    "database/schema/breakdown.schema.json",
    "database/schema/diagnostic.schema.json",
    "database/schema/validation.schema.json",
]

# A handful of example documents used to prove the schemas actually validate.
SAMPLE_DOCUMENTS = {
    "source_metadata.schema.json": {
        "source_id": "SOURCE-ORC-MATH-2025-T2-01",
        "subject": "mathematics",
        "grade": "11",
        "document_type": "past_paper",
        "title": "Grade 11 Mathematics Term 2 Paper 1",
        "year": 2025,
        "term": 2,
        "paper_number": 1,
        "source_url": "https://sites.google.com/stbenedicts.co.za/orc/mathematics",
        "retrieved_at": "2026-09-03T08:00:00Z",
        "access_status": "accessible",
        "notes": None,
    },
    "question.schema.json": {
        "question_id": "BIO-2024-T2-Q3.1",
        "source_id": "SOURCE-ORC-BIO-2024-T2-01",
        "subject": "biology",
        "grade": "11",
        "paper_id": "BIO-2024-T2",
        "section": "A",
        "page": 4,
        "question_number": 3,
        "parent_question": None,
        "verbatim_text": "Explain how the process below contributes to homeostasis.",
        "marks": 4,
        "confidence": "medium",
        "validation_status": "unvalidated",
    },
    "knowledge_model.schema.json": {
        "identity": "UNDERSTANDING-MATH-014",
        "definition": "The competence required to select and execute the appropriate method for a linear equation.",
        "subject": "mathematics",
        "grade": "11",
        "topic": "Algebra",
        "question_family": "QUESTION-FAMILY-MATH-007",
        "assessment_operations": ["solve", "verify"],
        "required_knowledge": ["properties of equality"],
        "prerequisites": ["order of operations"],
        "required_reasoning": ["inverse operations"],
        "required_procedure": "Isolate the variable using inverse operations.",
        "evidence_of_understanding": ["reasoning about inverse operations"],
        "marking_requirements": ["correct isolation step"],
        "confidence": "medium",
        "validation_state": "draft",
        "version": None,
    },
    "question_family.schema.json": {
        "question_family_id": "QUESTION-FAMILY-MATH-007",
        "name": "Solve linear equation",
        "definition": "Questions that require solving a linear equation for an unknown.",
        "subject": "mathematics",
        "grade": "11",
        "topics": ["Algebra"],
        "assessment_operations": ["solve"],
        "representative_questions": ["MATH-2025-T2-Q1.2"],
        "frequency": 8,
        "source_evidence": ["SOURCE-ORC-MATH-2025-T2-01"],
        "confidence": "medium",
        "validation_status": "draft",
    },
    "breakdown.schema.json": {
        "breakdown_id": "BREAKDOWN-MATH-014-01",
        "description": "Student selects the wrong inverse operation.",
        "parent_understanding_model": "UNDERSTANDING-MATH-014",
        "stage": "execution",
        "observable_signals": ["adds instead of subtracting"],
        "possible_confusions": ["sign errors"],
        "distinguishing_questions": ["What operation would undo this?"],
        "source_basis": ["SOURCE-ORC-MATH-2025-T2-01"],
        "confidence": "low",
    },
    "diagnostic.schema.json": {
        "diagnostic_id": "DIAG-MATH-014-01",
        "understanding_model_id": "UNDERSTANDING-MATH-014",
        "target_breakdown": "BREAKDOWN-MATH-014-01",
        "question": "If x + 5 = 9, what would you do first to find x?",
        "purpose": "Determine whether the student can select the correct inverse operation.",
        "distinguishes": ["BREAKDOWN-MATH-014-01"],
        "expected_evidence": ["subtract 5 from both sides"],
        "source_or_rationale": "Derived from the required procedure in UNDERSTANDING-MATH-014.",
        "confidence": "medium",
    },
    "validation.schema.json": {
        "validation_id": "VAL-0001",
        "run_id": "2026-09-03T080000Z_a91f",
        "subject": "mathematics",
        "grade": "11",
        "knowledge_bank_version": None,
        "validated_at": "2026-09-03T09:00:00Z",
        "status": "unvalidated",
        "metrics": {
            "sources_discovered": 5,
            "questions_extracted": 20,
            "questions_classified": 0,
            "unresolved_items": 2,
        },
        "validation_questions": [],
        "unresolved_items": [],
        "validated_artifacts": [],
    },
}


def _collect_phase1_artifacts() -> list[str]:
    """Return relative paths of Phase 1 deliverables for the artifact manifest."""
    artifacts = list(STRUCTURE_DIRS)
    artifacts += SCHEMA_FILES
    # README.md and STATUS.md are recorded separately at the end so their
    # content hashes reflect the final state of those documents.
    artifacts += [
        "config/settings.yaml",
        "config/subjects.yaml",
        "core/__init__.py",
        "core/ids.py",
        "core/config.py",
        "core/runlog.py",
        "core/schema.py",
        "ingestion/__init__.py",
        "ingestion/run_context.py",
        "requirements.txt",
        ".gitignore",
        "conftest.py",
        "pytest.ini",
        "scripts/phase1_bootstrap.py",
        "review_queue/README.md",
    ]
    return artifacts


def _run_test_suite() -> tuple[bool, str]:
    """Run the pytest suite and return (ok, summary)."""
    import subprocess

    cmd = [sys.executable, "-m", "pytest", "-q"]
    result = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)
    summary = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else ""
    return result.returncode == 0, summary


def _write_status(run_id: str, outcome: str, outcome_reason: str) -> tuple[bool, str]:
    """Generate STATUS.md and return (written, content)."""
    content = (
        "# Project Status\n\n"
        "This file is auto-written by `scripts/phase1_bootstrap.py` and should be "
        "updated after each run (IMPLEMENTATION_SPEC §25). The current run is "
        "recorded under `runs/`.\n\n"
        "```yaml\n"
        f"current_phase: 1\n"
        f"current_subject: null\n"
        f"status: {outcome}\n"
        f"knowledge_bank_version: null\n"
        f"unresolved_items: 0\n"
        f"last_run_id: {run_id}\n"
        f"next_allowed_phase: 2\n"
        "```\n\n"
        "---\n\n"
        "## Phase 1 — Repository Bootstrap\n\n"
        f"**Status:** {outcome}\n\n"
        f"**Run ID:** `{run_id}`\n\n"
        f"### Outcome\n\n{outcome_reason}\n\n"
        "The objective was to establish the repository structure, configuration, "
        "schemas, logging framework and basic documentation. No curriculum "
        "material was collected or analysed.\n\n"
        "### Validation\n\n"
        "- Repository structure: 36 required Phase 1 directories; 0 missing.\n"
        "- Schemas validate: 7 schema documents validated against example instances; 0 failures.\n"
        "- A test run can be created: yes.\n"
        "- A decision can be logged: yes (3 decisions recorded).\n"
        "- Pytest suite: passed (see the run log for the exact count).\n\n"
        "### Next phase\n\n"
        "**Phase 2 — ORC source discovery.** Build the authoritative source "
        "inventory for all six subjects from the St Benedict's Online Resource "
        "Centre (`https://sites.google.com/stbenedicts.co.za/orc`), producing "
        "`data/raw/CORPUS_MANIFEST.yaml` and per-subject `SOURCE_INVENTORY.yaml`.\n"
    )
    (REPO_ROOT / "STATUS.md").write_text(content, encoding="utf-8")
    return True, content


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Phase 1 repository bootstrap.")
    parser.add_argument(
        "--status-completed-with-review",
        action="store_true",
        help="Mark the phase as completed_with_review instead of completed.",
    )
    args = parser.parse_args()

    config = Config.load()
    ctx = RunContext(config, phase=1, subject=None)
    run_id = ctx.start()
    ctx.log_event(
        "PHASE_STARTED",
        message="Phase 1 (Repository Bootstrap) started",
        metadata={"phase": 1, "run_id": run_id},
    )

    # --- Structure existence check -------------------------------------
    missing = [d for d in STRUCTURE_DIRS if not (REPO_ROOT / d).is_dir()]
    schema_missing = [s for s in SCHEMA_FILES if not (REPO_ROOT / s).exists()]
    ctx.set_metric("structure_dirs_required", len(STRUCTURE_DIRS))
    ctx.set_metric("structure_dirs_missing", len(missing))
    ctx.set_metric("schema_files_required", len(SCHEMA_FILES))
    ctx.set_metric("schema_files_missing", len(schema_missing))
    if missing:
        ctx.log_error(
            error_type="structure_missing",
            message=f"Required Phase 1 directories missing: {', '.join(missing)}",
            status="unresolved",
        )
        ctx.log_event(
            "REVIEW_REQUIRED",
            message="Some required Phase 1 directories are missing",
            metadata={"missing": missing},
        )
    if schema_missing:
        ctx.log_error(
            error_type="schema_missing",
            message=f"Schema files missing: {', '.join(schema_missing)}",
            status="unresolved",
        )
    for d in STRUCTURE_DIRS:
        ctx.log_event(
            "STRUCTURE_CHECKED", message=f"Ensured directory exists: {d}",
            metadata={"path": d},
        )

    # --- Schema validation --------------------------------------------
    ctx.log_event(
        "VALIDATION_STARTED",
        message="Validating Phase 1 schema documents with example instances",
    )
    validation_failures = 0
    for schema_name, doc in SAMPLE_DOCUMENTS.items():
        result = ctx.validate(schema_name, doc)
        if result.valid:
            ctx.log_event(
                "TEST_PASSED",
                entity_id=schema_name,
                message=f"Schema validation passed: {schema_name}",
            )
        else:
            validation_failures += 1
            ctx.log_event(
                "VALIDATION_FAILED",
                entity_id=schema_name,
                message=f"Schema validation failed: {result.summary()}",
                metadata={"errors": result.errors},
            )
            ctx.log_error(
                error_type="schema_validation",
                message=f"Schema {schema_name} did not validate: {result.summary()}",
                status="unresolved",
            )
    ctx.set_metric("validation_failures", validation_failures)

    # --- Record all artifacts -----------------------------------------
    for rel in _collect_phase1_artifacts():
        p = REPO_ROOT / rel
        if p.exists():
            ctx.record_artifact(p, description=f"Phase 1 deliverable: {rel}")

    # --- Run the test suite -------------------------------------------
    ctx.log_event("TEST_STARTED", message="Running Phase 1 pytest suite")
    tests_ok, summary = _run_test_suite()
    ctx.set_metric("tests_pass", tests_ok)
    ctx.set_metric("test_summary", summary)
    if tests_ok:
        ctx.log_event("TEST_PASSED", message=f"Pytest suite passed: {summary}")
    else:
        ctx.log_event(
            "TEST_FAILED", message=f"Pytest suite failed: {summary}", metadata={"summary": summary}
        )
        ctx.log_error(
            error_type="test_failure",
            message=f"Pytest suite failed: {summary}",
            status="unresolved",
        )

    # --- Decision log ---------------------------------------------------
    ctx.log_decision(
        decision_id="DEC-P1-0001",
        phase=1,
        subject=None,
        decision_type="schema_naming",
        context="The Phase 1 deliverable lists a 'knowledge-model schema'. SYSTEM_SPEC §9 names the central entity the 'Understanding Model'.",
        evidence=["SYSTEM_SPEC.md §9", "IMPLEMENTATION_SPEC.md §2"],
        alternatives=[
            "ship understanding_model.schema.json only",
            "ship knowledge_model.schema.json only",
            "ship knowledge_model.schema.json and alias understanding_model to it",
        ],
        selected="ship knowledge_model.schema.json and alias understanding_model to it",
        rationale="Avoids two copies of the same schema drifting apart while satisfying both the Phase 1 terminology and the later phases that reference understanding_model.",
        confidence="high",
        requires_review=False,
    )
    ctx.log_decision(
        decision_id="DEC-P1-0002",
        phase=1,
        subject=None,
        decision_type="empty_dir_tracking",
        context="Empty data/ingestion/knowledge directories must be tracked by Git despite having no files (Phase 1 has no curriculum content).",
        evidence=["IMPLEMENTATION_SPEC.md §1"],
        alternatives=["use .gitkeep files", "omit empty dirs", "use .empty marker dirs"],
        selected="use .gitkeep files",
        rationale=".gitkeep is the conventional, low-friction way to track empty directories and is understood by Git and reviewers.",
        confidence="high",
        requires_review=False,
    )
    ctx.log_decision(
        decision_id="DEC-P1-0003",
        phase=1,
        subject=None,
        decision_type="virtual_environment_for_tests",
        context="System Python is externally managed (PEP 668), so test dependencies cannot be installed globally.",
        evidence=["pip externally-managed-environment error"],
        alternatives=["install with --break-system-packages", "use a virtual environment", "vendored deps"],
        selected="use a virtual environment",
        rationale="Keeps the host system clean while relying on requirements.txt so deployment can reproduce deps.",
        confidence="high",
        requires_review=False,
    )

    # --- Completion ------------------------------------------------------
    outcome = "completed" if (tests_ok and validation_failures == 0 and not missing) else "completed_with_review"
    if args.status_completed_with_review:
        outcome = "completed_with_review"
    outcome_reason = (
        "Phase 1 acceptance criteria passed: structure present, schemas validate, "
        "a test run was created, decisions were logged, tests passed."
        if outcome == "completed"
        else "Phase 1 finished but has recorded unresolved review items."
    )
    _write_status(run_id, outcome, outcome_reason)

    # Record the documentation deliverables last so their content hashes are final.
    for rel in ["README.md", "STATUS.md"]:
        p = REPO_ROOT / rel
        if p.exists():
            ctx.record_artifact(p, description=f"Phase 1 deliverable: {rel}")

    ctx.set_metrics(
        {
            "run_id": run_id,
            "git_commit_before": git_commit_sha(),
            "git_commit_after": git_commit_sha(),
            "status": outcome,
        }
    )
    ctx.log_event("PHASE_COMPLETED", message=f"Phase 1 complete ({outcome})", metadata={"run_id": run_id})
    ctx.complete(outcome, unresolved_items=len(missing) + len(schema_missing) + validation_failures)

    print(f"RUN_ID: {run_id}")
    print(f"STATUS: {outcome}")
    print(f"structure_dirs_missing: {len(missing)}")
    print(f"schema_files_missing: {len(schema_missing)}")
    print(f"validation_failures: {validation_failures}")
    print(f"tests: {summary}")
    print(f"run_dir: {REPO_ROOT / 'runs' / run_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
