"""Phase 3 acquisition: corpus selection, form classification and content probing.

Modules
-------
``inventory``
    Read the Phase 2 ``SOURCE_INVENTORY.yaml`` files without PyYAML. Read-only:
    the inventories are discovery provenance and are never rewritten here.

``forms``
    Classify a past paper into its **assessment form** —
    ``setter x paper_form x session``. Form, not topic and not year, is what
    determines which question families a paper can contain.

``selection``
    Form-stratified saturation sampling: two-pass allocation (coverage then
    depth), memorandum pairing, companion-document attachment and curriculum
    anchors. Implements ``CORPUS_SUFFICIENCY_POLICY.md``.

``content_probe``
    Standard-library text extraction for acquired files, used to verify
    ``document_type`` from content rather than trusting Phase 2 metadata, and to
    flag diagram-bearing documents as ``requires_visual_verification``.

Drivers live in ``scripts/phase3_select.py`` (3a) and
``scripts/phase3_ingest_drop.py`` (3b).
"""

from __future__ import annotations

__all__ = ["inventory", "forms", "selection", "content_probe"]
