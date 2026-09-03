"""Shared infrastructure for the Grade 11 Adaptive Socratic Tutor.

Phase 1 provides the repository bootstrap layer: configuration loading, run
and decision logging, and JSON Schema validation. Later phases build on these.

Modules:
    ids:   run ID generation.
    config: base configuration loading.
    runlog: run logger (events, decisions, errors, metrics, artifacts).
    schema: JSON Schema validation for the data models.
"""

from __future__ import annotations

__all__ = [
    "ids",
    "config",
    "runlog",
    "schema",
]

__version__ = "1.0.0"
