"""Tests for run and entity ID generation."""

import re

from core import ids


def test_make_run_id_format():
    run_id = ids.make_run_id()
    # Matches RUN_LOG_SPEC §2 format: YYYYMMDDTHHMMSSZ_xxxx
    assert re.fullmatch(r"\d{8}T\d{6}Z_[0-9a-f]{4}", run_id), run_id
    # Run IDs are unique enough to differ on consecutive calls.
    assert run_id != ids.make_run_id()


def test_make_run_id_uses_utc():
    run_id = ids.make_run_id()
    # The timestamp portion is UTC and Z-suffixed: YYYYMMDDTHHMMSSZ_xxxx
    timestamp_part = run_id.split("_", 1)[0]
    assert timestamp_part.endswith("Z"), "timestamp portion must be Z-suffixed UTC"


def test_make_entity_id_prefix():
    eid = ids.make_entity_id("DEC", unique="merging-families")
    assert eid.startswith("DEC-")
    assert eid == "DEC-" + eid.split("-", 1)[1]


def test_make_entity_id_deterministic():
    a = ids.make_entity_id("SRC", unique="stable-source")
    b = ids.make_entity_id("SRC", unique="stable-source")
    assert a == b


def test_make_entity_id_uses_hash_suffix():
    a = ids.make_entity_id("SRC", unique="abc")
    b = ids.make_entity_id("SRC", unique="xyz")
    assert a != b


def test_utc_now_iso_ends_with_z():
    assert ids.utc_now_iso().endswith("Z")


def test_epoch_now_is_numeric():
    from numbers import Number

    assert isinstance(ids.epoch_now(), Number)
