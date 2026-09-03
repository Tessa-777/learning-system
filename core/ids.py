"""Run ID generation.

The run ID format follows RUN_LOG_SPEC §2:

    runs/2026-09-03T084100Z_a91f/

i.e. a UTC timestamp ``YYYYMMDDTHHMMSSZ`` followed by a short random suffix.
"""

from __future__ import annotations

import hashlib
import secrets
import time
from datetime import datetime, timezone


def _timestamp_now() -> str:
    """Current UTC time formatted as ``YYYYMMDDTHHMMSSZ``."""
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _suffix() -> str:
    """A short, unpredictable lowercase hex suffix."""
    return secrets.token_hex(2)  # 4 hex characters


def make_run_id() -> str:
    """Create a fresh run ID, e.g. ``2026-09-03T084100Z_a91f``."""
    return f"{_timestamp_now()}_{_suffix()}"


def make_entity_id(prefix: str, unique: str | None = None) -> str:
    """Create a deterministic-ish entity identifier.

    ``prefix`` is a human-readable token (e.g. ``DEC``, ``SRC``). If ``unique``
    is supplied it is hashed to produce a stable suffix; otherwise a random
    suffix is used. The result is upper-cased for consistency with the
    examples in RUN_LOG_SPEC (e.g. ``DEC-0042``).
    """
    token = prefix.strip().upper().replace(" ", "-")
    if unique is None:
        suffix = secrets.token_hex(3).upper()
    else:
        digest = hashlib.sha1(unique.encode("utf-8")).hexdigest()[:8].upper()
        suffix = digest
    return f"{token}-{suffix}"


def utc_now_iso() -> str:
    """Current UTC time as an ISO-8601 string with ``Z`` suffix."""
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def epoch_now() -> float:
    """Current Unix epoch time in seconds."""
    return time.time()
