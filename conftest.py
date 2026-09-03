"""Root pytest configuration.

Adds the repository root to ``sys.path`` so tests can import the ``core``,
``ingestion`` and other packages directly. Also makes fixtures available to all
test modules in the ``tests/`` directory.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pytest

from core.config import Config


@pytest.fixture(scope="session")
def config() -> Config:
    """Session-scoped project configuration loaded from config/."""
    return Config.load()
