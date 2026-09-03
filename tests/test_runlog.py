"""Tests for the run / decision logging framework (RUN_LOG_SPEC)."""

import json

import pytest
from pathlib import Path

from core.runlog import RunLogger, git_commit_sha


def _new_logger(tmp_path) -> RunLogger:
    return RunLogger(
        tmp_path,
        run_id="2026-09-03T084100Z_a91f",
        phase=1,
        subject=None,
        spec_version="1.0.0",
        implementation_spec_version="1.0.0",
        agent_version="1.0.0",
        model="test-model",
        model_provider="test-provider",
    )


def test_run_directory_created_on_start(tmp_path):
    logger = _new_logger(tmp_path)
    run_id = logger.start()
    assert run_id == "2026-09-03T084100Z_a91f"
    assert (tmp_path / run_id / "run.json").exists()
    assert (tmp_path / run_id / "artifacts").is_dir()


def test_run_manifest_fields(tmp_path):
    logger = _new_logger(tmp_path)
    logger.start()
    manifest = json.loads((tmp_path / logger.run_id / "run.json").read_text())
    for field in [
        "run_id",
        "started_at",
        "completed_at",
        "phase",
        "subject",
        "spec_version",
        "implementation_spec_version",
        "agent_version",
        "model",
        "model_provider",
        "git_commit_before",
        "git_commit_after",
        "status",
    ]:
        assert field in manifest, field
    assert manifest["status"] == "in_progress"


def test_event_written_to_events_jsonl(tmp_path):
    logger = _new_logger(tmp_path)
    logger.start()
    logger.log_event(
        "TEST_STARTED",
        subject="mathematics",
        entity_id="DEC-0001",
        message="A test event",
        metadata={"key": "value"},
    )
    logger.complete("completed")
    events = (tmp_path / logger.run_id / "events.jsonl").read_text().strip().splitlines()
    record = json.loads(events[0])
    assert record["event"] == "TEST_STARTED"
    assert record["subject"] == "mathematics"
    assert record["entity_id"] == "DEC-0001"
    assert record["metadata"] == {"key": "value"}
    assert "timestamp" in record


def test_decision_logged(tmp_path):
    logger = _new_logger(tmp_path)
    logger.start()
    logger.log_decision(
        decision_id="DEC-0042",
        decision_type="question_family_merge",
        context="Merging two families",
        evidence=["BIO-2024-T2-Q3.1", "BIO-2025-T1-Q5.2"],
        alternatives=["keep separate", "merge"],
        selected="merge",
        rationale="Same underlying competence.",
        confidence="high",
        requires_review=False,
    )
    logger.complete("completed")
    decisions = json.loads((tmp_path / logger.run_id / "decisions.json").read_text())
    assert len(decisions) == 1
    d = decisions[0]
    assert d["decision_id"] == "DEC-0042"
    assert d["selected"] == "merge"
    assert d["confidence"] == "high"


def test_error_and_metrics_written(tmp_path):
    logger = _new_logger(tmp_path)
    logger.start()
    logger.log_error(
        error_type="acquisition_failed",
        message="Could not download source",
        affected_artifact="SOURCE-X",
        status="unresolved",
    )
    logger.set_metric("questions_extracted", 12)
    logger.complete("completed_with_review", unresolved_items=1)
    errors = json.loads((tmp_path / logger.run_id / "errors.json").read_text())
    metrics = json.loads((tmp_path / logger.run_id / "metrics.json").read_text())
    assert errors[0]["error_type"] == "acquisition_failed"
    assert errors[0]["status"] == "unresolved"
    assert metrics["questions_extracted"] == 12
    assert metrics["unresolved_items"] == 1


def test_artifact_and_manifest_hashed(tmp_path):
    logger = _new_logger(tmp_path)
    logger.start()
    artifact = tmp_path / "sample.txt"
    artifact.write_text("hello world")
    logger.record_artifact(artifact, type="text", description="a sample artifact")
    logger.complete("completed")
    manifest = (tmp_path / logger.run_id / "artifacts" / "artifacts.yaml").read_text()
    assert "sample.txt" in manifest
    assert logger._artifacts[0]["content_hash"] is not None


def test_last_event_represents_final_status(tmp_path):
    logger = _new_logger(tmp_path)
    logger.start()
    logger.complete("blocked")
    manifest = json.loads((tmp_path / logger.run_id / "run.json").read_text())
    assert manifest["status"] == "blocked"
    assert manifest["completed_at"] is not None


def test_flush_is_idempotent(tmp_path):
    logger = _new_logger(tmp_path)
    logger.start()
    logger.log_event("TEST_STARTED")
    logger.flush()
    logger.flush()
    lines = (tmp_path / logger.run_id / "events.jsonl").read_text().strip().splitlines()
    assert len(lines) == 1


def test_git_commit_sha_available():
    # Function runs within a git repo (this checkout), returns a short SHA or None.
    sha = git_commit_sha()
    assert sha is None or sha
