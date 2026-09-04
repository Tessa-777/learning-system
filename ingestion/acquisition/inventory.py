"""Read Phase 2 source inventories without requiring PyYAML.

``data/raw/<subject>/SOURCE_INVENTORY.yaml`` was machine-generated in Phase 2
and contains folded multi-line ``notes:`` scalars. Those defeat a naive
indentation parser, and PyYAML cannot be installed in restricted environments.

This module therefore reads the ``sources:`` block by splitting on record
boundaries (``- source_id:``) and extracting the schema fields with anchored
regular expressions. It is deliberately read-only: inventories are Phase 2
provenance and are never rewritten here.

The field list mirrors ``database/schema/source_metadata.schema.json``.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Optional

__all__ = ["read_source_records", "read_inventory_header", "SOURCE_FIELDS"]

SOURCE_FIELDS = (
    "source_id",
    "subject",
    "grade",
    "document_type",
    "title",
    "year",
    "term",
    "paper_number",
    "source_url",
    "retrieved_at",
    "access_status",
    "local_path",
    "file_hash",
)

_HEADER_FIELDS = (
    "inventory_id",
    "subject",
    "grade",
    "subject_page",
    "drive_root",
    "record_count",
)


def _unquote(value: str) -> Optional[Any]:
    value = value.strip()
    if value in ("null", "~", ""):
        return None
    if value.startswith("'") and value.endswith("'") and len(value) >= 2:
        return value[1:-1].replace("''", "'")
    if value.startswith('"') and value.endswith('"') and len(value) >= 2:
        return value[1:-1]
    if re.fullmatch(r"[-+]?\d+", value):
        return int(value)
    return value


def _sources_block(text: str) -> str:
    match = re.search(r"^sources:\s*$", text, re.M)
    return text[match.end():] if match else ""


def read_source_records(path: Path | str) -> List[Dict[str, Any]]:
    """Return every source record in an inventory, in file order."""
    text = Path(path).read_text(encoding="utf-8")
    body = _sources_block(text)
    records: List[Dict[str, Any]] = []
    for chunk in re.split(r"^- source_id:", body, flags=re.M)[1:]:
        # Records open with "- source_id:" at column 0 while every sibling field
        # is indented two spaces, so restore the indentation before matching.
        chunk = "  source_id:" + chunk
        record: Dict[str, Any] = {}
        for field_name in SOURCE_FIELDS:
            match = re.search(rf"^  {field_name}:\s*(.*)$", chunk, re.M)
            record[field_name] = _unquote(match.group(1)) if match else None
        records.append(record)
    return records


def read_inventory_header(path: Path | str) -> Dict[str, Any]:
    """Return the scalar header fields of an inventory (before ``sources:``)."""
    text = Path(path).read_text(encoding="utf-8")
    match = re.search(r"^sources:\s*$", text, re.M)
    head = text[: match.start()] if match else text
    header: Dict[str, Any] = {}
    for field_name in _HEADER_FIELDS:
        found = re.search(rf"^{field_name}:\s*(.*)$", head, re.M)
        header[field_name] = _unquote(found.group(1)) if found else None
    return header


def drive_file_id(source_url: Optional[str]) -> Optional[str]:
    """Extract the Google Drive file ID from a source URL, if present."""
    if not source_url:
        return None
    match = re.search(r"/file/d/([A-Za-z0-9_-]+)", source_url)
    if match:
        return match.group(1)
    match = re.search(r"[?&]id=([A-Za-z0-9_-]+)", source_url)
    return match.group(1) if match else None
