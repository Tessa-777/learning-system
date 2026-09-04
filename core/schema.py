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

    JSONSCHEMA_BACKEND = "jsonschema"
except ImportError:  # pragma: no cover - restricted/offline environments
    # jsonschema cannot be installed where pip has no network. Fall back to the
    # bundled mini-validator below, which implements exactly the keyword set the
    # schemas in database/schema/ actually use: type, required, properties,
    # additionalProperties, enum, pattern, items.
    jsonschema = None
    JSONSCHEMA_BACKEND = "mini"


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
        if JSONSCHEMA_BACKEND == "jsonschema":
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
        errors = []
        _mini_validate(schema, document, "", errors)
        return SchemaValidationResult(
            valid=not errors,
            errors=errors,
            schema_id=schema.get("$id", name),
        )

    def validate_all(self, name: str, documents: Iterable[Mapping[str, Any]]) -> list[SchemaValidationResult]:
        return [self.validate(name, doc) for doc in documents]

    @staticmethod
    def _format_error(error: Any) -> str:
        path = "/".join(str(p) for p in error.absolute_path) or "<root>"
        return f"{path}: {error.message}"


# --------------------------------------------------------------------------
# Standard-library fallback validator
# --------------------------------------------------------------------------
#
# Implements only the keywords used by database/schema/*.schema.json.
# `format` is treated as an annotation (jsonschema does not enforce it by
# default either). Unknown keywords are ignored, matching JSON Schema
# semantics where unrecognised keywords are annotations.

_TYPE_MAP = {
    "object": dict,
    "array": list,
    "string": str,
    "integer": int,
    "number": (int, float),
    "boolean": bool,
    "null": type(None),
}


def _mini_check_type(expected: Any, value: Any) -> bool:
    names = expected if isinstance(expected, list) else [expected]
    for name in names:
        py = _TYPE_MAP.get(name)
        if py is None:
            return True  # unknown type keyword: do not fail closed
        if name == "integer" and isinstance(value, bool):
            continue
        if name == "number" and isinstance(value, bool):
            continue
        if isinstance(value, py):
            return True
    return False


def _mini_validate(schema: Any, instance: Any, path: str, errors: list) -> None:
    if not isinstance(schema, dict):
        return
    where = path or "<root>"

    if "type" in schema and not _mini_check_type(schema["type"], instance):
        errors.append(
            f"{where}: {instance!r} is not of type {schema['type']!r}"
        )
        return

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{where}: {instance!r} is not one of {schema['enum']!r}")

    if isinstance(instance, str) and "pattern" in schema:
        import re as _re

        if _re.search(schema["pattern"], instance) is None:
            errors.append(
                f"{where}: {instance!r} does not match {schema['pattern']!r}"
            )

    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{where}: {key!r} is a required property")
        props = schema.get("properties", {})
        additional = schema.get("additionalProperties", True)
        for key, value in instance.items():
            if key in props:
                _mini_validate(props[key], value, f"{path}/{key}", errors)
            elif additional is False:
                errors.append(
                    f"{path}/{key}: additional property {key!r} is not allowed"
                )
            elif isinstance(additional, dict):
                _mini_validate(additional, value, f"{path}/{key}", errors)

    if isinstance(instance, list) and isinstance(schema.get("items"), dict):
        for idx, item in enumerate(instance):
            _mini_validate(schema["items"], item, f"{path}/{idx}", errors)
