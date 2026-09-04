"""Base configuration loading.

Loads the YAML configuration shipped under ``config/`` and exposes it as a
lightweight, immutable accessor. Nothing in here performs curriculum analysis;
it is purely structural configuration for Phase 1 (repository bootstrap).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

try:  # prefer the complete implementation when it is installed
    import yaml

    YAML_BACKEND = "pyyaml"
except ImportError:  # pragma: no cover - restricted/offline environments
    # PyYAML cannot be installed where pip has no network. Fall back to the
    # bundled standard-library subset parser so the repository stays runnable.
    # See core/yamllite.py for the exact supported subset and its limits.
    from . import yamllite as _yamllite

    yaml = None
    YAML_BACKEND = "yamllite"

# Repo root is the directory that contains this package's parent.
REPO_ROOT = Path(__file__).resolve().parent.parent

_DEFAULT_SETTINGS = REPO_ROOT / "config" / "settings.yaml"
_DEFAULT_SUBJECTS = REPO_ROOT / "config" / "subjects.yaml"


class ConfigError(RuntimeError):
    """Raised when configuration is missing or malformed."""


class Config:
    """Immutable read-only view over the merged project configuration."""

    def __init__(self, settings: Mapping[str, Any], subjects: Mapping[str, Any]):
        self._settings = _freeze(settings)
        self._subjects = _freeze(subjects)

    @classmethod
    def load(
        cls,
        settings_path: Path | str = _DEFAULT_SETTINGS,
        subjects_path: Path | str = _DEFAULT_SUBJECTS,
    ) -> "Config":
        settings_path = Path(settings_path)
        subjects_path = Path(subjects_path)
        if not settings_path.exists():
            raise ConfigError(f"Missing settings config: {settings_path}")
        if not subjects_path.exists():
            raise ConfigError(f"Missing subjects config: {subjects_path}")
        settings = _read_yaml(settings_path)
        subj = _read_yaml(subjects_path)
        return cls(settings, subj)

    # -- accessors ---------------------------------------------------------
    @property
    def settings(self) -> Mapping[str, Any]:
        return self._settings

    @property
    def subjects(self) -> Mapping[str, Any]:
        return self._subjects

    @property
    def project(self) -> Mapping[str, Any]:
        return self._settings.get("project", {})

    @property
    def specs(self) -> Mapping[str, Any]:
        return self._settings.get("specs", {})

    @property
    def agents(self) -> Mapping[str, Any]:
        return self._settings.get("agents", {})

    @property
    def paths(self) -> Mapping[str, Any]:
        return self._settings.get("paths", {})

    @property
    def logging(self) -> Mapping[str, Any]:
        return self._settings.get("logging", {})

    @property
    def schema(self) -> Mapping[str, Any]:
        return self._settings.get("schema", {})

    def subject_slugs(self) -> list[str]:
        return list(self._subjects.get("subjects", {}).keys())

    def subject_display_name(self, slug: str) -> str | None:
        entry = self._subjects.get("subjects", {}).get(slug)
        if not entry:
            return None
        return entry.get("display_name")

    def execution_order(self) -> list[str]:
        return list(self._subjects.get("execution_order", []))

    def resolve_path(self, rel_path: str) -> Path:
        """Resolve a path relative to the repository root (absolute paths passthrough)."""
        p = Path(rel_path)
        return p if p.is_absolute() else REPO_ROOT / p

    def resolve_schema(self, schema_name: str) -> Path:
        """Resolve a JSON Schema file path by its configured name."""
        schema_dir = self.schema_dir()
        return schema_dir / self.schema.get(schema_name, schema_name)

    def schema_dir(self) -> Path:
        return self.resolve_path(self.paths.get("schema_dir", "database/schema"))


def _read_yaml(path: Path) -> Mapping[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        if YAML_BACKEND == "pyyaml":
            data = yaml.safe_load(fh)
        else:
            data = _yamllite.loads(fh.read())
    if data is None:
        raise ConfigError(f"Config file is empty: {path}")
    if not isinstance(data, dict):
        raise ConfigError(f"Config file must contain a mapping: {path}")
    return data


def _freeze(obj: Any) -> Any:
    """Deep-freeze a nested structure into immutable built-ins."""
    if isinstance(obj, dict):
        return {k: _freeze(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return tuple(_freeze(v) for v in obj)
    return obj
