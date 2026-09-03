"""A small convenience context that binds config, run logger and schema validator.

This is the shared object later phases will use to start a run, log events and
decisions, validate produced data against the schemas, and finalise the run.
It deliberately contains no curriculum logic.
"""

from __future__ import annotations

from pathlib import Path

from core.config import Config, REPO_ROOT
from core.runlog import RunLogger
from core.schema import SchemaValidationResult, SchemaValidator


class RunContext:
    """Bundle of the Phase 1 infrastructure for one execution."""

    def __init__(
        self,
        config: Config | None = None,
        *,
        run_id: str | None = None,
        phase: int | str | None = None,
        subject: str | None = None,
    ) -> None:
        self.config = config or Config.load()
        real_path = self.config.resolve_path(self.config.paths["runs_dir"])
        agent = self.config.agents
        self.logger = RunLogger(
            real_path,
            run_id=run_id,
            phase=phase,
            subject=subject,
            spec_version=self.config.specs["system_spec_version"],
            implementation_spec_version=self.config.specs["implementation_spec_version"],
            agent_version=agent.get("agent_version", "unknown"),
            model=agent.get("model", "unknown"),
            model_provider=agent.get("model_provider", "unknown"),
        )
        self.validator = SchemaValidator(self.config.schema_dir())

    def start(self) -> str:
        """Begin the run and return the run ID."""
        return self.logger.start()

    def complete(self, status: str, *, unresolved_items: int = 0) -> None:
        self.logger.complete(status, unresolved_items=unresolved_items)

    # Convenience forwarding -------------------------------------------------
    def log_event(self, *args, **kwargs):
        return self.logger.log_event(*args, **kwargs)

    def log_decision(self, *args, **kwargs):
        return self.logger.log_decision(*args, **kwargs)

    def log_error(self, *args, **kwargs):
        return self.logger.log_error(*args, **kwargs)

    def set_metric(self, *args, **kwargs):
        return self.logger.set_metric(*args, **kwargs)

    def set_metrics(self, *args, **kwargs):
        return self.logger.set_metrics(*args, **kwargs)

    def record_artifact(self, *args, **kwargs):
        return self.logger.record_artifact(*args, **kwargs)

    def validate(self, schema_name: str, document: dict) -> SchemaValidationResult:
        return self.validator.validate(schema_name, document)
