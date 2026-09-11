"""Tests for the Physics two-pass output (Pass 1 evidence + Pass 2 synthesis).

These exercise the real builders rather than a copy of their logic:

* ``scripts/build_physics_pass1.py`` is executed into a temporary directory and
  its batch is checked against the papers' printed mark totals;
* ``scripts/build_physics_pass2.py`` is executed into a temporary directory and
  the emitted objects are checked for schema validity, referential integrity,
  family partition, the computed confidence rule and the saturation rules from
  TWO_PASS_PROMPTS Pass 2;
* the committed artifacts under ``knowledge/physics/`` are checked the same way,
  so a stale or hand-edited artifact fails here.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "knowledge" / "physics"
SCHEMA_DIR = ROOT / "database" / "schema"

# Fields required by TWO_PASS_PROMPTS Pass 2 section 9 for an Understanding Model.
# ``provenance`` is additionally required by AGENTS.md rule 6.
MODEL_FIELDS = {
    "identity", "definition", "subject", "grade", "topic", "question_family",
    "assessment_operations", "required_knowledge", "prerequisites",
    "required_reasoning", "required_procedure", "evidence_of_understanding",
    "marking_requirements", "common_breakdowns", "misconceptions",
    "diagnostic_dimensions", "diagnostic_questions", "source_references",
    "confidence", "validation_state", "version", "provenance",
}

SATURATION_FIELDS = {
    "papers_in_sample", "question_families_identified",
    "families_first_observed_in_final_third", "strata_left_unsampled",
    "families_supported_by_single_exemplar",
}


def load_builder(name: str):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[path.stem] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def batch() -> list[dict]:
    return json.loads((ROOT / "data" / "extracted" / "physics_pass1.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def knowledge() -> dict[str, list | dict]:
    return {
        "families": json.loads((KNOWLEDGE / "question_families.json").read_text(encoding="utf-8")),
        "models": json.loads((KNOWLEDGE / "understanding_models.json").read_text(encoding="utf-8")),
        "breakdowns": json.loads((KNOWLEDGE / "breakdown_models.json").read_text(encoding="utf-8")),
        "diagnostics": json.loads((KNOWLEDGE / "diagnostic_questions.json").read_text(encoding="utf-8")),
        "unresolved": json.loads((KNOWLEDGE / "unresolved_items.json").read_text(encoding="utf-8")),
        "saturation": json.loads((KNOWLEDGE / "saturation_report.json").read_text(encoding="utf-8")),
        "summary": json.loads((KNOWLEDGE / "_PASS2_SUMMARY.json").read_text(encoding="utf-8")),
    }


def check_pass2_output(payloads: dict, batch: list[dict], validator) -> None:
    """Shared referential / partition / rule assertions over one Pass 2 output set."""
    families, models = payloads["families"], payloads["models"]
    breakdowns, diagnostics = payloads["breakdowns"], payloads["diagnostics"]
    unresolved, saturation = payloads["unresolved"], payloads["saturation"]

    by_id = {r["source_id"]: r for r in batch}

    # -- every cited source_id exists in the Pass 1 batch -------------------
    for fam in families:
        assert len(fam["source_evidence"]) >= 2, f"{fam['question_family_id']} has <2 members"
        for sid in fam["source_evidence"]:
            assert sid in by_id, f"{fam['question_family_id']} cites unknown source_id {sid}"

    # -- family membership is a partition -----------------------------------
    seen: dict[str, str] = {}
    for fam in families:
        for sid in fam["source_evidence"]:
            assert sid not in seen, f"{sid} claimed by both {seen[sid]} and {fam['question_family_id']}"
            seen[sid] = fam["question_family_id"]

    # -- no family silently mixes Physics and Chemistry ----------------------
    for fam in families:
        disciplines = {by_id[sid]["discipline"] for sid in fam["source_evidence"]}
        assert disciplines == {"Physics"}, f"{fam['question_family_id']} mixes {disciplines}"

    # -- confidence is what the evidence supports ---------------------------
    for fam in families:
        papers = {by_id[sid]["paper_key"] for sid in fam["source_evidence"]}
        expected = (
            "high" if len(fam["source_evidence"]) >= 4 and len(papers) >= 3
            else "medium"
        )
        assert fam["confidence"] == expected, (
            f"{fam['question_family_id']}: confidence {fam['confidence']} but evidence is "
            f"{len(fam['source_evidence'])} members across {len(papers)} papers"
        )
        assert fam["validation_status"] == "unvalidated"

    # -- models, breakdowns, diagnostics reference real objects -------------
    family_ids = {f["question_family_id"] for f in families}
    model_ids = {m["identity"] for m in models}
    breakdown_ids = {b["breakdown_id"] for b in breakdowns}
    for model in models:
        assert set(model) == MODEL_FIELDS, f"{model['identity']} field list drifted"
        assert model["question_family"] in family_ids
        assert model["validation_state"] == "unvalidated"
        assert model["version"] == "0.1.0-draft"
        for bid in model["common_breakdowns"]:
            assert bid in breakdown_ids, f"{model['identity']} cites unknown breakdown {bid}"
    for b in breakdowns:
        assert b["parent_understanding_model"] in model_ids
        assert b["stage"] in {
            "interpretation", "prerequisite", "concept", "strategy", "execution",
            "reasoning", "explanation", "verification", "other",
        }
        for sid in b["source_basis"]:
            assert sid in by_id, f"{b['breakdown_id']} cites unknown source_id {sid}"
    per_model: dict[str, int] = {}
    for d in diagnostics:
        assert d["understanding_model_id"] in model_ids
        assert d["target_breakdown"] in breakdown_ids
        per_model[d["understanding_model_id"]] = per_model.get(d["understanding_model_id"], 0) + 1
        for bid in d["distinguishes"]:
            assert bid in breakdown_ids
    assert per_model and all(2 <= n <= 4 for n in per_model.values()), per_model
    assert set(per_model) == model_ids, "every model needs 2-4 diagnostics"

    # -- schema validity of the committed/emitted objects -------------------
    for schema, docs in [
        ("question_family.schema.json", families),
        ("knowledge_model.schema.json", models),
        ("breakdown.schema.json", breakdowns),
        ("diagnostic.schema.json", diagnostics),
    ]:
        for doc in docs:
            result = validator.validate(schema, doc)
            assert result.valid, f"{schema}: {result.errors[:2]}"

    # -- saturation report ---------------------------------------------------
    assert SATURATION_FIELDS <= set(saturation)
    final_third = set(saturation["thirds_split"][2])
    new_in_final = [
        f["question_family_id"] for f in families
        if {by_id[sid]["paper_key"] for sid in f["source_evidence"]} <= final_third
    ]
    assert saturation["families_first_observed_in_final_third"] == len(new_in_final)
    assert saturation["families_supported_by_single_exemplar"] == sum(
        1 for f in families if f["frequency"] == 1
    )
    single_paper = {
        f["question_family_id"] for f in families
        if len({by_id[sid]["paper_key"] for sid in f["source_evidence"]}) == 1
    }
    if saturation["families_first_observed_in_final_third"] > 0 or len(single_paper):
        assert saturation["additional_diagnostics"]["saturated"] is False

    # -- every single-paper family and every unassigned record is reported ---
    reported = {i["id"]: i for i in unresolved}
    assert single_paper <= set(reported["UNRES-PHY-022"]["affected"])
    claimed = {sid for f in families for sid in f["source_evidence"]}
    unassigned = {r["source_id"] for r in batch} - claimed
    assert unassigned == set(reported["UNRES-PHY-021"]["affected"])
    thin = {b["breakdown_id"] for b in breakdowns if len(b["source_basis"]) < 2}
    assert thin == set(reported["UNRES-PHY-023"]["affected"])
    assert reported["UNRES-PHY-023"]["type"] == "single_exemplar"
    # The image-dependent family list is derived from the batch, not hand-written.
    image_heavy = {
        f["question_family_id"] for f in families
        if sum(1 for sid in f["source_evidence"] if by_id[sid]["requires_visual_verification"])
        > len(f["source_evidence"]) / 2
    }
    assert image_heavy == set(reported["UNRES-PHY-011"]["affected"])
    for item in unresolved:
        assert {"id", "type", "summary", "detail", "affected", "evidence",
                "recommended_review"} <= set(item), item.get("id")


def read_output(out_dir: Path) -> dict:
    return {
        "families": json.loads((out_dir / "question_families.json").read_text(encoding="utf-8")),
        "models": json.loads((out_dir / "understanding_models.json").read_text(encoding="utf-8")),
        "breakdowns": json.loads((out_dir / "breakdown_models.json").read_text(encoding="utf-8")),
        "diagnostics": json.loads((out_dir / "diagnostic_questions.json").read_text(encoding="utf-8")),
        "unresolved": json.loads((out_dir / "unresolved_items.json").read_text(encoding="utf-8")),
        "saturation": json.loads((out_dir / "saturation_report.json").read_text(encoding="utf-8")),
        "summary": json.loads((out_dir / "_PASS2_SUMMARY.json").read_text(encoding="utf-8")),
    }


def test_pass1_builder_runs_clean(tmp_path):
    """Execute Pass 1: marks must sum to each paper's printed total."""
    mod = load_builder("build_physics_pass1.py")
    mod.EXTRACTED = tmp_path
    mod.PER_PAPER_DIR = tmp_path / "pass1" / "physics"
    assert mod.main() == 0

    batch = json.loads((tmp_path / "physics_pass1.json").read_text(encoding="utf-8"))
    assert batch, "Pass 1 produced no records"
    per_paper = sorted((tmp_path / "pass1" / "physics").glob("PHY-*.json"))
    assert len(per_paper) == 4
    for path in per_paper:
        doc = json.loads(path.read_text(encoding="utf-8"))
        assert doc["marks_sum_check"]["match"], path.name
        assert doc["memo_alignment_check"]["date_match"], path.name
        assert doc["records_extracted"] == len(doc["question_records"]) > 0
    summary = json.loads((tmp_path / "pass1" / "physics" / "_BATCH_SUMMARY.json").read_text())
    assert summary["problems"] == []
    assert summary["question_records"] == len(batch)


def test_pass2_builder_runs_clean(tmp_path, batch, validator):
    """Execute Pass 2 and validate what it just wrote."""
    mod = load_builder("build_physics_pass2.py")
    mod.OUT_DIR = tmp_path
    assert mod.main() == 0
    payloads = read_output(tmp_path)
    assert payloads["summary"]["errors"] == []
    assert payloads["summary"]["schema_validation"]["failed"] == 0
    check_pass2_output(payloads, batch, validator)


def test_committed_knowledge_matches_builder_rules(knowledge, batch, validator):
    """The artifacts on disk must satisfy the same rules as a fresh build."""
    check_pass2_output(knowledge, batch, validator)


def test_pass1_records_are_provenanced(batch):
    """Every record must cite a real source file whose SHA-256 matches."""
    assert batch
    checked: set[tuple[str, str]] = set()
    for record in batch:
        for kind in ("source_document", "memo_document"):
            rel, digest = record[kind], record[f"{kind}_sha256"]
            if (rel, digest) in checked:
                continue
            path = ROOT / rel
            assert path.exists(), f"missing source file {rel}"
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            assert actual == digest, f"hash mismatch for {rel}"
            checked.add((rel, digest))
        assert record["subject"] == "physics"
        assert record["discipline"] == "Physics"
        assert record["fidelity_rung"] in {"A", "B", "C"}
        assert record["question_text"] and record["question_text"] != "unresolved"
    assert len({r["source_id"] for r in batch}) == len(batch), "duplicate source_id in batch"


def test_provenance_chain_reaches_the_orc_inventory(batch, knowledge):
    """RUN_LOG_SPEC 9: model -> family -> source_id -> Phase 2 ORC source."""
    inventory = yaml.safe_load(
        (ROOT / "data" / "raw" / "physics" / "SOURCE_INVENTORY.yaml").read_text(encoding="utf-8")
    )["sources"]
    orc_ids = {r["source_id"] for r in inventory}
    by_id = {r["source_id"]: r for r in batch}

    for record in batch:
        assert record["orc_source_id"] in orc_ids, record["source_id"]
        assert record["orc_memo_source_id"] in orc_ids, record["source_id"]

    family_of = {f["question_family_id"]: f for f in knowledge["families"]}
    single_paper = {
        i["id"]: i for i in knowledge["unresolved"] if i["id"] == "UNRES-PHY-022"
    }["UNRES-PHY-022"]["affected"]
    for model in knowledge["models"]:
        family = family_of[model["question_family"]]
        chains = [by_id[sid]["orc_source_id"] for sid in family["source_evidence"]]
        assert chains and all(c in orc_ids for c in chains), model["identity"]
        if len(set(chains)) < 2:
            # Only a family resting on a single paper may cite one ORC source, and it
            # must be reported as such rather than passed off as cross-paper evidence.
            assert model["question_family"] in single_paper, model["identity"]
            assert model["confidence"] != "high", model["identity"]



def test_saturation_report_is_honest(knowledge):
    """Saturation must not be claimed while a family is new in the final third."""
    sat = knowledge["saturation"]
    assert sat["additional_diagnostics"]["saturated"] is False
    assert "families_first_observed_in_final_third > 0" in sat["additional_diagnostics"]["reason_not_saturated"]
    assert sat["papers_in_sample"] < 8
    assert sat["strata_left_unsampled"], "an empty strata list would claim full coverage"


def test_review_queue_items_state_resolutions():
    """RUN_LOG_SPEC 10: issue, affected entity, evidence, resolutions, review."""
    path = ROOT / "review_queue" / "RQ-P4-PHY-PASS2.yaml"
    assert path.exists(), "run scripts/run_physics_pass2.py to create the review queue"
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert doc["items"]
    assert doc["item_count"] == len(doc["items"])
    for item in doc["items"]:
        for field in ("issue", "type", "id", "affected_entity", "evidence",
                      "possible_resolutions", "recommended_review"):
            assert field in item and item[field], f"{item.get('id')}: missing {field}"
        assert isinstance(item["possible_resolutions"], list)


def test_run_log_was_written():
    """The run must be logged with a permitted status and the usual files."""
    runs = sorted((ROOT / "runs").iterdir())
    physics_runs = []
    for run in runs:
        manifest = run / "run.json"
        if not manifest.exists():
            continue
        meta = json.loads(manifest.read_text(encoding="utf-8"))
        if meta.get("subject") == "physics" and meta.get("phase") == "4-11":
            physics_runs.append((run, meta))
    assert physics_runs, "no physics two-pass run logged under runs/"
    run, meta = physics_runs[-1]
    assert meta["status"] in {"completed", "completed_with_review", "blocked", "failed"}
    assert meta["status"] != "completed", "this run has unresolved review items"
    for name in ("run.json", "events.jsonl", "decisions.json", "errors.json", "metrics.json"):
        assert (run / name).exists(), f"{run.name} is missing {name}"
    assert (run / "artifacts" / "artifacts.yaml").exists()
    metrics = json.loads((run / "metrics.json").read_text(encoding="utf-8"))
    assert metrics["questions_extracted"] == metrics["questions_classified"] + metrics["questions_unclassified"]
    assert metrics["validation_failures"] == 0
    decisions = json.loads((run / "decisions.json").read_text(encoding="utf-8"))
    assert {d["decision_id"] for d in decisions} >= {
        "DEC-P4-001", "DEC-P4-002", "DEC-P4-003", "DEC-P4-004", "DEC-P4-005", "DEC-P4-006",
    }
    errors = json.loads((run / "errors.json").read_text(encoding="utf-8"))
    assert any(e["error_type"] == "saturation_not_reached" for e in errors)
