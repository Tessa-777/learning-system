"""Run and decision logging framework.

Implements RUN_LOG_SPEC. Each execution receives a unique run ID and a
directory under ``runs/`` containing:

    runs/<run_id>/
        run.json
        events.jsonl
        decisions.json
        errors.json
        metrics.json
        artifacts/
            artifacts.yaml

The logger is designed to be written-to during a phase and then finalized once
the phase completes. It is intentionally independent of any particular phase
logic so later ingestion phases can reuse it unchanged.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from . import ids

try:
    import yaml
except ImportError as exc:  # pragma: no cover - defensive
    raise RuntimeError(
        "PyYAML is required. Install dependencies with `pip install -r requirements.txt`."
    ) from exc


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _json_default(value: Any) -> Any:
    """Return a JSON-serialisable representation of ``value``."""
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, datetime):
        return value.isoformat()
    if hasattr(value, "to_dict") and callable(value.to_dict):
        return value.to_dict()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serialisable")


def git_commit_sha() -> str | None:
    """Return the current short Git commit SHA, or ``None`` if not in a repo."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
            cwd=str(Path(__file__).resolve().parent.parent),
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None
    return None


def sha256_file(path: Path) -> str:
    """SHA-256 content hash of a file."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


class RunLogger:
    """Creates and manages a single run directory and its log files."""

    def __init__(
        self,
        runs_dir: Path | str,
        *,
        run_id: str | None = None,
        phase: int | str | None = None,
        subject: str | None = None,
        spec_version: str = "1.0.0",
        implementation_spec_version: str = "1.0.0",
        agent_version: str = "unknown",
        model: str = "unknown",
        model_provider: str = "unknown",
    ) -> None:
        self.runs_dir = Path(runs_dir)
        self.run_id = run_id or ids.make_run_id()
        self.run_dir = self.runs_dir / self.run_id
        self.phase = phase
        self.subject = subject
        self.spec_version = spec_version
        self.implementation_spec_version = implementation_spec_version
        self.agent_version = agent_version
        self.model = model
        self.model_provider = model_provider

        self._events: list[dict[str, Any]] = []
        self._decisions: list[dict[str, Any]] = []
        self._errors: list[dict[str, Any]] = []
        self._metrics: dict[str, Any] = {}
        self._artifacts: list[dict[str, Any]] = []
        self._started_at: str | None = None
        self._completed_at: str | None = None
        self._git_commit_before: str | None = None
        self._git_commit_after: str | None = None
        self._artifacts_manifest_path: Path | None = None

    # -- lifecycle ---------------------------------------------------------
    def start(self) -> str:
        """Create the run directory and record the run start.

        Returns the run ID.
        """
        self.run_dir.mkdir(parents=True, exist_ok=True)
        (self.run_dir / "artifacts").mkdir(parents=True, exist_ok=True)
        self._started_at = _utcnow_iso()
        self._git_commit_before = git_commit_sha()
        self._write_run_manifest()
        return self.run_id

    def complete(self, status: str, *, unresolved_items: int = 0) -> None:
        """Finalise the run: set status, write all files, record end time.

        ``status`` should be one of ``completed``, ``completed_with_review``,
        ``blocked`` or ``failed`` (RUN_LOG_SPEC §11).
        """
        self._completed_at = _utcnow_iso()
        self._git_commit_after = git_commit_sha()
        if "unresolved_items" not in self._metrics:
            self._metrics["unresolved_items"] = unresolved_items
        self.flush()
        self._write_run_manifest(status=status)

    def flush(self) -> None:
        """Persist all in-memory log buffers to disk (idempotent)."""
        self.run_dir.mkdir(parents=True, exist_ok=True)
        (self.run_dir / "artifacts").mkdir(parents=True, exist_ok=True)
        self._write_events()
        self._write_decisions()
        self._write_errors()
        self._write_metrics()
        self._write_artifacts()

    # -- event logging -----------------------------------------------------
    def log_event(
        self,
        event: str,
        *,
        subject: str | None = None,
        entity_id: str | None = None,
        message: str | None = None,
        metadata: Mapping[str, Any] | None = None,
        phase: int | str | None = None,
    ) -> dict[str, Any]:
        """Append a single structured event to ``events.jsonl``."""
        record = {
            "timestamp": _utcnow_iso(),
            "event": event,
            "subject": subject if subject is not None else self.subject,
            "entity_id": entity_id,
            "message": message,
            "metadata": dict(metadata or {}),
        }
        if phase is not None:
            record["phase"] = phase
        self._events.append(record)
        return record

    # -- decision logging --------------------------------------------------
    def log_decision(
        self,
        *,
        decision_id: str,
        phase: int | str | None = None,
        subject: str | None = None,
        decision_type: str,
        context: str,
        evidence: Iterable[str] | None = None,
        alternatives: Iterable[str] | None = None,
        selected: str,
        rationale: str,
        confidence: str = "medium",
        requires_review: bool = False,
    ) -> dict[str, Any]:
        """Append a structured decision to ``decisions.json``."""
        record = {
            "decision_id": decision_id,
            "timestamp": _utcnow_iso(),
            "phase": phase if phase is not None else self.phase,
            "subject": subject if subject is not None else self.subject,
            "decision_type": decision_type,
            "context": context,
            "evidence": list(evidence or []),
            "alternatives": list(alternatives or []),
            "selected": selected,
            "rationale": rationale,
            "confidence": confidence,
            "requires_review": bool(requires_review),
        }
        self._decisions.append(record)
        return record

    # -- error logging -----------------------------------------------------
    def log_error(
        self,
        *,
        phase: int | str | None = None,
        subject: str | None = None,
        error_type: str,
        message: str,
        affected_artifact: str | None = None,
        retry_attempts: int = 0,
        resolution: str | None = None,
        status: str = "unresolved",
    ) -> dict[str, Any]:
        """Append a structured error record to ``errors.json``."""
        record = {
            "timestamp": _utcnow_iso(),
            "phase": phase if phase is not None else self.phase,
            "subject": subject if subject is not None else self.subject,
            "error_type": error_type,
            "message": message,
            "affected_artifact": affected_artifact,
            "retry_attempts": retry_attempts,
            "resolution": resolution,
            "status": status,
        }
        self._errors.append(record)
        return record

    # -- metrics -----------------------------------------------------------
    def set_metric(self, key: str, value: Any) -> None:
        self._metrics[key] = value

    def set_metrics(self, metrics: Mapping[str, Any]) -> None:
        self._metrics.update(metrics)

    # -- artifact manifest -------------------------------------------------
    def record_artifact(
        self,
        path: Path | str,
        *,
        type: str | None = None,
        description: str | None = None,
        content_hash: str | None = None,
    ) -> dict[str, Any]:
        """Record an artifact created or modified by this run."""
        p = Path(path)
        record: dict[str, Any] = {
            "artifact_id": self._next_artifact_id(),
            "path": str(p),
            "type": type or _guess_type(p),
            "created_or_modified": _utcnow_iso(),
            "source_run": self.run_id,
            "content_hash": content_hash or (
                None if p.is_dir() else (sha256_file(p) if p.exists() else None)
            ),
        }
        if description:
            record["description"] = description
        self._artifacts.append(record)
        return record

    def _next_artifact_id(self) -> str:
        return f"ART-{len(self._artifacts) + 1:04d}"

    # -- write helpers -----------------------------------------------------
    def _run_manifest(self, status: str | None = None) -> dict[str, Any]:
        manifest = {
            "run_id": self.run_id,
            "started_at": self._started_at,
            "completed_at": self._completed_at,
            "phase": self.phase,
            "subject": self.subject,
            "spec_version": self.spec_version,
            "implementation_spec_version": self.implementation_spec_version,
            "agent_version": self.agent_version,
            "model": self.model,
            "model_provider": self.model_provider,
            "git_commit_before": self._git_commit_before,
            "git_commit_after": self._git_commit_after,
            "status": status or "in_progress",
        }
        return manifest

    def _write_run_manifest(self, status: str | None = None) -> None:
        path = self.run_dir / "run.json"
        with path.open("w", encoding="utf-8") as fh:
            json.dump(self._run_manifest(status), fh, indent=2, default=_json_default)
            fh.write("\n")

    def _write_events(self) -> None:
        path = self.run_dir / "events.jsonl"
        with path.open("w", encoding="utf-8") as fh:
            for record in self._events:
                fh.write(json.dumps(record, default=_json_default) + "\n")

    def _write_decisions(self) -> None:
        path = self.run_dir / "decisions.json"
        self._write_json_list(path, self._decisions)

    def _write_errors(self) -> None:
        path = self.run_dir / "errors.json"
        self._write_json_list(path, self._errors)

    def _write_json_list(self, path: Path, items: Iterable[Mapping[str, Any]]) -> None:
        with path.open("w", encoding="utf-8") as fh:
            json.dump(list(items), fh, indent=2, default=_json_default)
            fh.write("\n")

    def _write_metrics(self) -> None:
        path = self.run_dir / "metrics.json"
        with path.open("w", encoding="utf-8") as fh:
            json.dump(self._metrics, fh, indent=2, default=_json_default)
            fh.write("\n")

    def _write_artifacts(self) -> None:
        path = self.run_dir / "artifacts" / "artifacts.yaml"
        with path.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(list(self._artifacts), fh, sort_keys=False)
        self._artifacts_manifest_path = path


def _guess_type(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".yaml", ".yml"}:
        return "yaml"
    if suffix in {".json", ".jsonl"}:
        return "json"
    if suffix in {".sql", ".db", ".sqlite", ".sqlite3"}:
        return "database"
    if suffix in {".md"}:
        return "markdown"
    if suffix == ".py":
        return "python"
    if path.is_dir():
        return "directory"
    return "file"


def default_schema_paths(config: Any = None) -> dict[str, str]:
    """Return a mapping of schema kind -> configured filename.

    Kept here for consumers that need the schema filenames without a full
    Config object. When ``config`` is provided its ``schema`` block is used.
    """
    if config is not None:
        return dict(config.schema)
    return {
        "source_metadata": "source_metadata.schema.json",
        "question": "question.schema.json",
        "question_family": "question_family.schema.json",
        "understanding_model": "understanding_model.schema.json",
        "breakdown": "breakdown.schema.json",
        "diagnostic": "diagnostic.schema.json",
        "validation": "validation.schema.json",
    }
