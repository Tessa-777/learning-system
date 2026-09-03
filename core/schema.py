"""JSON Schema validation for the data models.

Provides a thin wrapper around ``jsonschema`` that loads the schema documents
shipped under ``database/schema/`` and validates data documents against them.

The four core schemas required by Phase 1 are:
    source_metadata, question, knowledge_model (understanding model), validation.

Additional schemas (question_family, breakdown, diagnostic) are also shipped so
later phases share one consistent schema directory.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - defensive
    raise RuntimeError(
        "jsonschema is required. Install dependencies with `pip install -r requirements.txt`."
    ) from exc


class SchemaError(RuntimeError):
    """Raised when a schema document cannot be loaded or is itself invalid."""


@dataclass
class SchemaValidationResult:
    """Outcome of validating a document against a schema."""

    valid: bool
    errors: list[str] = field(default_factory=list)
    schema_id: str | None = None

    def summary(self) -> str:
        if self.valid:
            return f"[OK] '{self.schema_id}': valid"
        return f"[FAIL] '{self.schema_id}': {len(self.errors)} error(s): " + "; ".join(
            self.errors[:5]
        )


class SchemaValidator:
    """Loads schema documents and validates data against them."""

    def __init__(self, schema_dir: Path | str):
        self.schema_dir = Path(schema_dir)
        self._schemas: dict[str, Any] = {}

    def load(self, name: str) -> Any:
        """Load (and cache) a schema by filename.

        Returns the parsed JSON Schema document.
        """
        if name in self._schemas:
            return self._schemas[name]
        path = self.schema_dir / name
        if not path.exists():
            raise SchemaError(f"Schema file not found: {path}")
        try:
            with path.open("r", encoding="utf-8") as fh:
                schema = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            raise SchemaError(f"Could not read schema {path}: {exc}") from exc
        # A schema document must itself be an object declaring $schema.
        if not isinstance(schema, dict):
            raise SchemaError(f"Schema {path} must be a JSON object")
        self._schemas[name] = schema
        return schema

    def all_names(self) -> list[str]:
        return sorted(p.name for p in self.schema_dir.glob("*.schema.json"))

    def validate(self, name: str, document: Mapping[str, Any]) -> SchemaValidationResult:
        """Validate ``document`` against the schema named ``name``."""
        schema = self.load(name)
        validator_class = jsonschema.validators.validator_for(schema)
        validator_class.check_schema(schema)
        validator = validator_class(schema)
        errors = sorted(
            validator.iter_errors(document), key=lambda e: list(e.absolute_path)
        )
        return SchemaValidationResult(
            valid=len(errors) == 0,
            errors=[self._format_error(e) for e in errors],
            schema_id=schema.get("$id", name),
        )

    def validate_all(self, name: str, documents: Iterable[Mapping[str, Any]]) -> list[SchemaValidationResult]:
        return [self.validate(name, doc) for doc in documents]

    @staticmethod
    def _format_error(error: Any) -> str:
        path = "/".join(str(p) for p in error.absolute_path) or "<root>"
        return f"{path}: {error.message}"
