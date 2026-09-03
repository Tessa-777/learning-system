"""Tests for the JSON Schemas shipped under database/schema/."""

import copy

import pytest

# Schema filenames (all shipped in database/schema/) to exercise.
REQUIRED_SCHEMAS = [
    "source_metadata.schema.json",
    "question.schema.json",
    "question_family.schema.json",
    "knowledge_model.schema.json",
    "breakdown.schema.json",
    "diagnostic.schema.json",
    "validation.schema.json",
]


def test_all_required_schemas_present(validator, config):
    assert set(REQUIRED_SCHEMAS).issubset(set(validator.all_names()))
    # Ensure the aliases configured in settings resolve to present files.
    for key in ["source_metadata", "question", "question_family", "knowledge_model",
                "understanding_model", "breakdown", "diagnostic", "validation"]:
        assert (config.resolve_schema(key)).exists(), key


@pytest.mark.parametrize("name", REQUIRED_SCHEMAS)
def test_schema_documents_are_valid_draft7(validator, name):
    schema = validator.load(name)
    # Loading plus calling validate() on an empty-ish doc exercises check_schema.
    assert schema.get("$schema") == "http://json-schema.org/draft-07/schema#"


def test_source_document_valid(validator, valid_source_document):
    result = validator.validate("source_metadata.schema.json", valid_source_document)
    assert result.valid, result.summary()


def test_source_document_requires_access_status(validator, valid_source_document):
    doc = copy.deepcopy(valid_source_document)
    del doc["access_status"]
    result = validator.validate("source_metadata.schema.json", doc)
    assert not result.valid
    assert any("access_status" in e for e in result.errors)


def test_source_document_rejects_unknown_subject(validator, valid_source_document):
    doc = copy.deepcopy(valid_source_document)
    doc["subject"] = "astronomy"
    result = validator.validate("source_metadata.schema.json", doc)
    assert not result.valid


def test_question_document_valid(validator, valid_question_document):
    result = validator.validate("question.schema.json", valid_question_document)
    assert result.valid, result.summary()


def test_question_document_rejects_missing_verbatim(validator, valid_question_document):
    doc = copy.deepcopy(valid_question_document)
    del doc["verbatim_text"]
    result = validator.validate("question.schema.json", doc)
    assert not result.valid


def test_knowledge_model_document_valid(validator, valid_knowledge_model_document):
    result = validator.validate("knowledge_model.schema.json", valid_knowledge_model_document)
    assert result.valid, result.summary()


def test_knowledge_model_document_valid_against_alias(validator, valid_knowledge_model_document):
    # understanding_model resolves to knowledge_model.schema.json (same file).
    result = validator.validate("knowledge_model.schema.json", valid_knowledge_model_document)
    assert result.valid


def test_knowledge_model_requires_identity(validator, valid_knowledge_model_document):
    doc = copy.deepcopy(valid_knowledge_model_document)
    del doc["identity"]
    result = validator.validate("knowledge_model.schema.json", doc)
    assert not result.valid


def test_validation_document_valid(validator, valid_validation_document):
    result = validator.validate("validation.schema.json", valid_validation_document)
    assert result.valid, result.summary()


def test_validation_document_rejects_bad_status(validator, valid_validation_document):
    doc = copy.deepcopy(valid_validation_document)
    doc["status"] = "done"
    result = validator.validate("validation.schema.json", doc)
    assert not result.valid


def test_question_family_document_valid(validator, valid_question_family_document):
    result = validator.validate("question_family.schema.json", valid_question_family_document)
    assert result.valid, result.summary()


def test_breakdown_document_valid(validator, valid_breakdown_document):
    result = validator.validate("breakdown.schema.json", valid_breakdown_document)
    assert result.valid, result.summary()


def test_diagnostic_document_valid(validator, valid_diagnostic_document):
    result = validator.validate("diagnostic.schema.json", valid_diagnostic_document)
    assert result.valid, result.summary()


def test_unknown_schema_raises(validator):
    with pytest.raises(Exception):
        validator.validate("does_not_exist.schema.json", {})


def test_additional_properties_rejected(validator, valid_source_document):
    doc = copy.deepcopy(valid_source_document)
    doc["unexpected_field"] = True
    result = validator.validate("source_metadata.schema.json", doc)
    assert not result.valid
    assert any("unexpected_field" in e for e in result.errors)
