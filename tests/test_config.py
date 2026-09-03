"""Tests for base configuration loading."""

import pytest

from core.config import Config, ConfigError, REPO_ROOT


def test_config_loads_default(config):
    assert isinstance(config, Config)
    assert config.project["name"] == "Grade 11 Adaptive Socratic Tutor"


def test_config_subject_list_matches_scope(config):
    slugs = config.subject_slugs()
    assert slugs == [
        "biology",
        "physics",
        "history",
        "english",
        "ap_mathematics",
        "mathematics",
    ]


def test_execution_order_prescribed(config):
    # IMPLEMENTATION_SPEC §23 order.
    assert config.execution_order() == [
        "biology",
        "physics",
        "history",
        "english",
        "ap_mathematics",
        "mathematics",
    ]


def test_subject_display_name(config):
    assert config.subject_display_name("ap_mathematics") == "AP Mathematics"
    assert config.subject_display_name("nonsense") is None


def test_primary_source_set(config):
    assert config.subjects["primary_source"]["base_url"].startswith("https://")


def test_resolve_path_absolute_subdir(config):
    assert str(config.resolve_path("runs")).endswith("runs")


def test_resolve_schema_maps_understanding_model_to_knowledge_model(config):
    # The understanding_model and knowledge_model aliases resolve to the same file.
    assert config.resolve_schema("understanding_model") == config.resolve_schema(
        "knowledge_model"
    )


def test_schema_files_exist(config):
    schema_dir = config.schema_dir()
    assert (schema_dir / config.schema["source_metadata"]).exists()
    assert (schema_dir / config.schema["question"]).exists()
    assert (schema_dir / config.schema["knowledge_model"]).exists()
    assert (schema_dir / config.schema["validation"]).exists()


def test_missing_settings_raises(tmp_path):
    with pytest.raises(ConfigError):
        Config.load(settings_path=tmp_path / "absent.yaml")
