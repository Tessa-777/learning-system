"""Shared test fixtures for the Phase 1 test suite.

Provides a session-scoped schema validator plus example (valid) documents that
satisfy each required schema, so tests can verify the schemas themselves and
exercise the validator.
"""

from __future__ import annotations

import pytest

from core.schema import SchemaValidator


@pytest.fixture(scope="session")
def validator(config) -> SchemaValidator:
    """SchemaValidator bound to the repository's schema directory."""
    return SchemaValidator(config.schema_dir())


# --- Valid document fixtures -------------------------------------------------

@pytest.fixture
def valid_source_document() -> dict:
    return {
        "source_id": "SOURCE-ORC-MATH-2025-T2-01",
        "subject": "mathematics",
        "grade": "11",
        "document_type": "past_paper",
        "title": "Grade 11 Mathematics Term 2 Paper 1",
        "year": 2025,
        "term": 2,
        "paper_number": 1,
        "source_url": "https://sites.google.com/stbenedicts.co.za/orc/mathematics",
        "retrieved_at": "2026-09-03T08:00:00Z",
        "access_status": "accessible",
        "notes": None,
    }


@pytest.fixture
def valid_question_document() -> dict:
    return {
        "question_id": "BIO-2024-T2-Q3.1",
        "source_id": "SOURCE-ORC-BIO-2024-T2-01",
        "subject": "biology",
        "grade": "11",
        "paper_id": "BIO-2024-T2",
        "section": "A",
        "page": 4,
        "question_number": 3,
        "parent_question": None,
        "verbatim_text": "Explain how the process below contributes to homeostasis.",
        "marks": 4,
        "confidence": "medium",
        "validation_status": "unvalidated",
    }


@pytest.fixture
def valid_knowledge_model_document() -> dict:
    return {
        "identity": "UNDERSTANDING-MATH-014",
        "definition": "The competence required to select and execute the appropriate method for a linear equation.",
        "subject": "mathematics",
        "grade": "11",
        "topic": "Algebra",
        "question_family": "QUESTION-FAMILY-MATH-007",
        "assessment_operations": ["solve", "verify"],
        "required_knowledge": ["properties of equality"],
        "prerequisites": ["order of operations"],
        "required_reasoning": ["inverse operations"],
        "required_procedure": "Isolate the variable using inverse operations.",
        "evidence_of_understanding": ["reasoning about inverse operations"],
        "marking_requirements": ["correct isolation step"],
        "confidence": "medium",
        "validation_state": "draft",
        "version": None,
    }


@pytest.fixture
def valid_validation_document() -> dict:
    return {
        "validation_id": "VAL-0001",
        "run_id": "2026-09-03T080000Z_a91f",
        "subject": "mathematics",
        "grade": "11",
        "knowledge_bank_version": None,
        "validated_at": "2026-09-03T09:00:00Z",
        "status": "unvalidated",
        "metrics": {
            "sources_discovered": 5,
            "questions_extracted": 20,
            "questions_classified": 0,
            "unresolved_items": 2,
        },
        "validation_questions": [],
        "unresolved_items": [],
        "validated_artifacts": [],
    }


@pytest.fixture
def valid_question_family_document() -> dict:
    return {
        "question_family_id": "QUESTION-FAMILY-MATH-007",
        "name": "Solve linear equation",
        "definition": "Questions that require solving a linear equation for an unknown.",
        "subject": "mathematics",
        "grade": "11",
        "topics": ["Algebra"],
        "assessment_operations": ["solve"],
        "representative_questions": ["MATH-2025-T2-Q1.2"],
        "frequency": 8,
        "source_evidence": ["SOURCE-ORC-MATH-2025-T2-01"],
        "confidence": "medium",
        "validation_status": "draft",
    }


@pytest.fixture
def valid_breakdown_document() -> dict:
    return {
        "breakdown_id": "BREAKDOWN-MATH-014-01",
        "description": "Student selects the wrong inverse operation.",
        "parent_understanding_model": "UNDERSTANDING-MATH-014",
        "stage": "execution",
        "observable_signals": ["adds instead of subtracting"],
        "possible_confusions": ["sign errors"],
        "distinguishing_questions": ["What operation would undo this?"],
        "source_basis": ["SOURCE-ORC-MATH-2025-T2-01"],
        "confidence": "low",
    }


@pytest.fixture
def valid_diagnostic_document() -> dict:
    return {
        "diagnostic_id": "DIAG-MATH-014-01",
        "understanding_model_id": "UNDERSTANDING-MATH-014",
        "target_breakdown": "BREAKDOWN-MATH-014-01",
        "question": "If x + 5 = 9, what would you do first to find x?",
        "purpose": "Determine whether the student can select the correct inverse operation.",
        "distinguishes": ["BREAKDOWN-MATH-014-01"],
        "expected_evidence": ["subtract 5 from both sides"],
        "source_or_rationale": "Derived from the required procedure in UNDERSTANDING-MATH-014.",
        "confidence": "medium",
    }
