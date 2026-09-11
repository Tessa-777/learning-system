#!/usr/bin/env python3
"""Execute the Physics two-pass run (Pass 1 rebuild + Pass 2 synthesis) and log it.

This is the auditable entry point required by RUN_LOG_SPEC. It runs the two
builders in order and records events, decisions, errors, metrics and artifacts
under ``runs/<run_id>/``:

    scripts/build_physics_pass1.py   Pass 1 - per-paper evidence extraction
    scripts/build_physics_pass2.py   Pass 2 - families, models, breakdowns, diagnostics

Phases touched (IMPLEMENTATION_SPEC): 4 extract source content, 5 segment
assessment questions, 6 align questions with memoranda, 8 discover question
taxonomy, 9 build Understanding Models, 10 build the breakdown model, 11 build
the diagnostic question bank. Phase 7 (curriculum mapping) could not run: the
organized sample contains no Grade 11 Physics curriculum document
(UNRES-PHY-020).

Usage:  python scripts/run_physics_pass2.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.runlog import RunLogger  # noqa: E402

PHASE = "4-11"  # 4, 5, 6, 8, 9, 10, 11; phase 7 skipped (no curriculum document)
SUBJECT = "physics"
ORGANIZED = ROOT / "data" / "organized" / "physics"
REVIEW_QUEUE = ROOT / "review_queue" / "RQ-P4-PHY-PASS2.yaml"

# RUN_LOG_SPEC 10 requires every review-queue item to state possible resolutions.
# These are the resolutions the evidence actually admits, per item type.
RESOLUTIONS = {
    "contradiction": [
        "obtain the corrected memorandum or an examiner clarification from the school",
        "exclude the affected record(s) from marking evidence until resolved",
        "keep the record but flag the contradiction to the student-facing tutor",
    ],
    "fidelity": [
        "re-extract the affected pages as images and read the diagrams",
        "cap the affected family/model at medium confidence (already applied)",
        "drop the affected record(s) from the evidence base",
    ],
    "data_quality": [
        "correct the upstream manifest or file naming and re-run the builder",
        "leave the record in place with the defect documented",
    ],
    "coverage_gap": [
        "extract the remaining paired papers and re-run Pass 2 on the larger batch",
        "acquire further papers covering the missing topic or stratum",
        "accept the gap and keep the affected records unassigned",
    ],
    "curriculum_gap": [
        "acquire the Grade 11 Physical Sciences curriculum / ATP document",
        "record the topic as out of scope for this batch and tell the tutor not to use it",
    ],
    "unsampled_stratum": [
        "acquire a paper from the missing stratum",
        "report the pattern as board-dependent rather than general",
    ],
    "single_exemplar": [
        "confirm the pattern against a second sitting",
        "drop the item",
    ],
}


def run_builder(name: str) -> int:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / name)],
        cwd=ROOT, capture_output=True, text=True,
    )
    print(proc.stdout.strip())
    if proc.stderr.strip():
        print(proc.stderr.strip(), file=sys.stderr)
    return proc.returncode


def corpus_counts() -> dict[str, int]:
    """Count what is physically present in the organized physics sample."""
    files = sorted(p.name for p in ORGANIZED.iterdir() if p.suffix.lower() in (".pdf", ".docx"))
    qp_named = [f for f in files if "MG" not in f]
    # PS11 Physics Exam 2020 QP ships as both .pdf and .docx (same paper).
    stems = {Path(f).stem for f in qp_named}
    return {
        "files_in_organized_sample": len(files),
        "qp_named_documents": len(qp_named),
        "qp_named_distinct_papers": len(stems),
        # UNRES-PHY-016: one 'QP' file is a memorandum, not a question paper.
        "question_papers_in_sample": len(stems) - 1,
        "memoranda_in_sample": len(files) - len(qp_named) + 1,
    }


def yaml_str(value: str) -> str:
    return '"' + value.replace('"', "'") + '"'


def write_review_queue(run_id: str, unresolved: list[dict]) -> None:
    REVIEW_QUEUE.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "review_id: RQ-P4-PHY-PASS2",
        f"run_id: {run_id}",
        "subject: physics",
        "phase: 4-11",
        "created_by: scripts/run_physics_pass2.py",
        f"item_count: {len(unresolved)}",
        "items:",
    ]
    for item in unresolved:
        lines += [
            f"  - issue: {yaml_str(item['summary'])}",
            f"    type: {item['type']}",
            f"    id: {item['id']}",
            f"    detail: {yaml_str(item.get('detail', ''))}",
            f"    affected_entity: {json.dumps(item.get('affected', [])[:8])}",
            f"    evidence: {json.dumps(item.get('evidence', [])[:4])}",
            "    possible_resolutions:",
        ]
        options = [item["recommended_review"]] + RESOLUTIONS.get(item["type"], [])
        seen: list[str] = []
        for opt in options:
            if opt and opt not in seen:
                seen.append(opt)
                lines.append(f"      - {yaml_str(opt)}")
        lines.append(f"    recommended_review: {yaml_str(item['recommended_review'])}")
    REVIEW_QUEUE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    logger = RunLogger(
        ROOT / "runs",
        phase=PHASE,
        subject=SUBJECT,
        agent_version="1.0.0",
        model="arena-agent",
        model_provider="arena.ai",
    )
    run_id = logger.start()
    print(f"run_id: {run_id}")
    corpus = corpus_counts()

    logger.log_event(
        "EXTRACTION_STARTED",
        message="Pass 1 re-run for physics from the organized source PDFs",
        metadata={"reason": "the inherited Pass 1 batch contained no question content", **corpus},
    )

    rc1 = run_builder("build_physics_pass1.py")
    pass1_summary = json.loads((ROOT / "data/extracted/pass1/physics/_BATCH_SUMMARY.json").read_text())
    if rc1 != 0 or pass1_summary["problems"]:
        logger.log_error(
            error_type="pass1_build_failed",
            message=f"Pass 1 builder reported problems: {pass1_summary['problems']}",
            affected_artifact="data/extracted/physics_pass1.json",
            status="unresolved",
        )
    else:
        logger.log_event(
            "EXTRACTION_COMPLETED",
            message=f"{pass1_summary['question_records']} question records extracted from "
                    f"{pass1_summary['papers_in_batch']} papers; each paper's record marks sum to "
                    f"its printed Question Total",
            metadata={"papers": [p["paper_key"] for p in pass1_summary["papers"]]},
        )

    for paper in pass1_summary["papers"]:
        logger.log_event(
            "MEMO_ALIGNED", entity_id=paper["paper_key"],
            message=f"paper/memo pairing verified from the printed header (DATE {paper['exam_date']}); "
                    f"date_match={paper['memo_date_match']}",
            metadata={"records": paper["records"], "marks": paper["marks"],
                      "exam_period": paper["exam_period"]},
        )

    logger.log_decision(
        decision_id="DEC-P4-001",
        decision_type="pass1_rebuild",
        context="The inherited data/extracted/physics_pass1.json held one record per paper with "
                "question_text, marks, memo_answer and topic_guess all set to 'unresolved'. Pass 2 "
                "requires citable per-question evidence, so it had nothing to cite.",
        evidence=["scripts/complete_subject_pass1.py", "git show HEAD:data/extracted/physics_pass1.json"],
        alternatives=["run Pass 2 on the hollow batch and report zero families",
                      "rebuild Pass 1 from the source PDFs, then run Pass 2"],
        selected="rebuild Pass 1 from the source PDFs, then run Pass 2",
        rationale="The PDFs in data/organized/physics are tracked in git and have a clean text layer "
                  "(verified with pypdf), so the recorded Phase 3 blocker ('Drive downloads fail') does "
                  "not apply to the organized corpus. Every Pass 2 claim then rests on a real question "
                  "record with a verified source SHA-256.",
        confidence="high",
        requires_review=True,
    )
    logger.log_decision(
        decision_id="DEC-P4-002",
        decision_type="memo_pairing_verification",
        context="data/organized/sample_manifest.json pairs four physics papers with a memorandum from a "
                "different sitting (UNRES-PHY-015).",
        evidence=["scripts/build_physics_pass1.py verify_alignment()",
                  "printed DATE / MARKS / EXAMINER header blocks"],
        alternatives=["trust the manifest pairing",
                      "verify each pairing from the printed headers and use only matching pairs"],
        selected="verify each pairing from the printed headers and use only matching pairs",
        rationale="Using a cross-paired memorandum would attribute one sitting's marking guidance to "
                  "another paper, corrupting every marking_requirements field downstream.",
        confidence="high",
        requires_review=False,
    )
    logger.log_decision(
        decision_id="DEC-P4-003",
        decision_type="confidence_rule",
        context="Pass 2 states confidence is 'high' with 4+ member questions across different papers, "
                "'medium' with 2-3, and never 'high' if all support comes from one paper.",
        evidence=["scripts/build_physics_pass2.py compute_confidence()"],
        alternatives=["author confidence by hand per family", "compute it from member evidence"],
        selected="compute it from member evidence, requiring 4+ members across 3+ papers for 'high'",
        rationale="An asserted confidence cannot be audited; a computed one can, and it changes "
                  "automatically as the batch grows.",
        confidence="high",
        requires_review=False,
    )
    logger.log_decision(
        decision_id="DEC-P4-004",
        decision_type="family_membership_partition",
        context="Several records could plausibly belong to more than one family (2023 Q4.3 is both a "
                "graph reading and a calculation).",
        evidence=["scripts/build_physics_pass2.py partition check"],
        alternatives=["allow overlapping membership", "enforce a partition"],
        selected="enforce a partition - each record belongs to at most one family",
        rationale="Overlap would let one question inflate several families and make frequency counts "
                  "meaningless. Records fitting no family are reported unassigned (UNRES-PHY-021) "
                  "rather than force-fitted.",
        confidence="high",
        requires_review=False,
    )
    logger.log_decision(
        decision_id="DEC-P4-005",
        decision_type="schema_field_mapping",
        context="Pass 2 names its family fields member_source_ids, distinguishing_features and "
                "typical_marks_range; database/schema/question_family.schema.json sets "
                "additionalProperties: false and offers no such fields.",
        evidence=["database/schema/question_family.schema.json"],
        alternatives=["relax the repo schema to accept the prompt's field names",
                      "map the prompt's fields onto the repo schema and record the marks range elsewhere"],
        selected="map onto the repo schema: member_source_ids -> source_evidence, "
                 "distinguishing_features -> definition + assessment_operations + topics, "
                 "typical_marks_range -> _PASS2_SUMMARY.json families[].marks_range",
        rationale="The persisted object must validate against the repository schema, which "
                  "IMPLEMENTATION_SPEC Phase 8 makes authoritative; the marks range is preserved in "
                  "the run summary and the report rather than being dropped.",
        confidence="high",
        requires_review=True,
    )
    logger.log_decision(
        decision_id="DEC-P4-006",
        decision_type="family_promotion_threshold",
        context="Four recurring patterns (CANDIDATE-FAMILY-PHY-A, -B, -C, -E) meet the prompt's minimum "
                "of 2 members but rest on only 2 papers.",
        evidence=["ingestion/analysis/physics_pass2_models.py DEFERRED_FAMILIES"],
        alternatives=["promote them to families on 2 papers' evidence",
                      "defer them to unresolved_items and say so"],
        selected="defer them to unresolved_items, flagged CANDIDATE-FAMILY-PHY-*",
        rationale="Stricter than the letter of the spec: their marking_requirements could not be "
                  "generalised from two sittings. Nothing is hidden - all four are in "
                  "unresolved_items.json with their evidence, so promoting them later is a one-line "
                  "change in the families module.",
        confidence="medium",
        requires_review=True,
    )

    logger.log_event("EXTRACTION_STARTED", message="Pass 2 synthesis over the physics batch")
    rc2 = run_builder("build_physics_pass2.py")
    summary = json.loads((ROOT / "knowledge/physics/_PASS2_SUMMARY.json").read_text())
    saturation = json.loads((ROOT / "knowledge/physics/saturation_report.json").read_text())
    unresolved = json.loads((ROOT / "knowledge/physics/unresolved_items.json").read_text())

    for fam in summary["families"]:
        logger.log_event(
            "QUESTION_CLASSIFIED", entity_id=fam["family_id"],
            message=f"{fam['name']} - {fam['members']} members across {len(fam['papers'])} papers, "
                    f"confidence {fam['confidence']}",
            metadata={"papers": fam["papers"], "marks_range": fam["marks_range"],
                      "rationale": fam["confidence_rationale"]},
        )
    for model in json.loads((ROOT / "knowledge/physics/understanding_models.json").read_text()):
        logger.log_event(
            "UNDERSTANDING_MODEL_CREATED", entity_id=model["identity"],
            message=f"{model['question_family']} -> {model['identity']} "
                    f"(confidence {model['confidence']}, validation_state {model['validation_state']}, "
                    f"version {model['version']})",
        )
    for b in json.loads((ROOT / "knowledge/physics/breakdown_models.json").read_text()):
        logger.log_event("BREAKDOWN_CREATED", entity_id=b["breakdown_id"],
                         message=f"stage={b['stage']} parent={b['parent_understanding_model']}")
    for d in json.loads((ROOT / "knowledge/physics/diagnostic_questions.json").read_text()):
        logger.log_event("DIAGNOSTIC_CREATED", entity_id=d["diagnostic_id"],
                         message=f"model={d['understanding_model_id']} target={d['target_breakdown']}")
    for item in unresolved:
        logger.log_event("REVIEW_REQUIRED", entity_id=item["id"],
                         message=f"[{item['type']}] {item['summary']}",
                         metadata={"affected_count": len(item.get("affected", []))})

    logger.log_event("VALIDATION_STARTED", message="schema and referential validation of Pass 2 output")
    if summary["schema_validation"]["failed"]:
        logger.log_event("VALIDATION_FAILED",
                         message=f"{summary['schema_validation']['failed']} object(s) failed schema validation")
    else:
        logger.log_event("VALIDATION_PASSED",
                         message=f"{summary['schema_validation']['checked']} objects valid against "
                                 f"database/schema/*.schema.json")

    for err in summary["errors"]:
        logger.log_error(error_type="pass2_consistency", message=err,
                         affected_artifact="knowledge/physics/", status="unresolved")
    if saturation["families_first_observed_in_final_third"] > 0:
        logger.log_error(
            error_type="saturation_not_reached",
            message="families_first_observed_in_final_third > 0 "
                    f"({saturation['families_new_in_final_third']}): physics cannot be declared saturated",
            affected_artifact="knowledge/physics/saturation_report.json",
            status="unresolved",
        )

    batch = json.loads((ROOT / "data/extracted/physics_pass1.json").read_text())
    marks_mismatch = sorted({r["paper_key"] for r in batch if not r["memo_alignment"]["marks_match"]})
    logger.set_metrics({
        "papers_discovered": corpus["files_in_organized_sample"],
        "question_papers_in_sample": corpus["question_papers_in_sample"],
        "papers_processed": summary["papers_in_sample"],
        "papers_not_processed": corpus["question_papers_in_sample"] - summary["papers_in_sample"],
        "questions_extracted": summary["question_records_in_batch"],
        "questions_classified": summary["records_assigned_to_a_family"],
        "questions_unclassified": summary["question_records_in_batch"] - summary["records_assigned_to_a_family"],
        "memo_alignment_rate": sum(1 for r in batch if r["memo_alignment"]["date_match"]) / len(batch),
        "memo_marks_agreement_papers": marks_mismatch,
        "curriculum_mapping_rate": None,  # Phase 7 not run: no curriculum document in the sample
        "records_requiring_visual_verification": sum(1 for r in batch if r["requires_visual_verification"]),
        "question_families": summary["question_families"],
        "understanding_models": summary["understanding_models"],
        "breakdowns": summary["breakdown_models"],
        "diagnostics": summary["diagnostic_questions"],
        "unresolved_items": summary["unresolved_items"],
        "validation_failures": summary["schema_validation"]["failed"],
        "families_first_observed_in_final_third": saturation["families_first_observed_in_final_third"],
        "strata_left_unsampled": len(saturation["strata_left_unsampled"]),
        "saturated": saturation["additional_diagnostics"]["saturated"],
    })

    write_review_queue(run_id, unresolved)

    for rel in [
        "data/extracted/physics_pass1.json",
        "data/extracted/pass1/physics/_BATCH_SUMMARY.json",
        "knowledge/physics/question_families.json",
        "knowledge/physics/understanding_models.json",
        "knowledge/physics/breakdown_models.json",
        "knowledge/physics/diagnostic_questions.json",
        "knowledge/physics/unresolved_items.json",
        "knowledge/physics/saturation_report.json",
        "knowledge/physics/_PASS2_SUMMARY.json",
        "knowledge/physics/PASS2_REPORT.md",
        str(REVIEW_QUEUE.relative_to(ROOT)),
    ]:
        path = ROOT / rel
        if path.exists():
            logger.record_artifact(path, description=f"Physics two-pass artifact: {rel}")

    clean = (rc1 == 0 and rc2 == 0 and not summary["errors"]
             and not summary["schema_validation"]["failed"] and not pass1_summary["problems"])
    # Never 'completed': this phase has recorded unresolved review items (RUN_LOG_SPEC 11).
    status = "completed_with_review" if clean else "failed"
    logger.complete(status, unresolved_items=summary["unresolved_items"])
    print(f"\nstatus: {status}  run: {run_id}")
    return 0 if clean else 1


if __name__ == "__main__":
    raise SystemExit(main())
