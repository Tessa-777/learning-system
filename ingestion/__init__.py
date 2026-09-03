"""Ingestion framework package.

Phase 1 (bootstrap) provides the shared plumbing that later phases use to
acquire, extract, segment, classify, analyse and validate source material.

Sub-packages (added in later phases):

    acquisition    -- download/copy authoritative sources (Phase 3)
    extraction     -- convert documents to machine-readable text (Phase 4)
    segmentation   -- split papers into structured questions (Phase 5)
    classification -- group questions into families (Phase 8)
    analysis       -- build Understanding Models (Phase 9) and diagnostics (Phase 11)
    validation     -- validate a knowledge bank (Phase 13)

Nothing in Phase 1 performs curriculum analysis.
"""

from __future__ import annotations

from .run_context import RunContext

__all__ = ["RunContext"]
