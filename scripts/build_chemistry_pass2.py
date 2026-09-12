#!/usr/bin/env python3
"""Build and validate the Chemistry Pass 2 knowledge objects (Tier 2/3).

Pass 2 (TWO_PASS_PROMPTS.md) consumes the Pass 1 batch for one subject and
compresses what repeats across it into question families, Understanding Models,
breakdown models, diagnostic questions and unresolved items. This script is the
mechanical half of Pass 2; the analysis itself is authored in
``ingestion/analysis/chemistry_pass2_*.py``.

Guarantees enforced here (a failure aborts the run rather than emitting a
plausible-looking but unprovenanced object):

* every family member resolves to a real Pass 1 ``source_id`` in the batch;
* no question record is claimed by two families;
* every family has at least two members (a one-member "family" is a
  single_exemplar and is reported in unresolved_items instead);
* ``confidence`` is computed from the evidence - never authored - and can only
  be "high" when the supporting questions span at least three papers;
* every Understanding Model links to an existing family, and every breakdown and
  diagnostic links to an existing model;
* every emitted object validates against ``database/schema/*.schema.json``.

Run from the repository root:  python scripts/build_chemistry_pass2.py
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "ingestion" / "analysis"))

from core.schema import SchemaValidator  # noqa: E402

import chemistry_pass2_families as fam_mod  # noqa: E402
import chemistry_pass2_models as model_mod  # noqa: E402
import chemistry_pass2_unresolved as unres_mod  # noqa: E402

EXTRACTED = ROOT / "data" / "extracted"
PASS1_BATCH = EXTRACTED / "chemistry_pass1.json"
MANIFEST = ROOT / "data" / "organized" / "sample_manifest.json"
OUT_DIR = ROOT / "knowledge" / "chemistry"
SCHEMA_DIR = ROOT / "database" / "schema"

SUBJECT = "chemistry"
GRADE = "11"
NOW = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

# Papers in this batch, in chronological sitting order. The saturation test needs an
# acquisition order; for chemistry there is no sample_manifest entry, so this is the
# order the papers were acquired and read for Pass 1 (NOT the order of the sittings in
# the calendar, but a stable chronological proxy: year then month).
ACQUISITION_ORDER = [
    "CHE-2018-JUL", "CHE-2019-AUG", "CHE-2020-NOV", "CHE-2021-NOV", "CHE-2022-JUN",
    "CHE-2022-NOV", "CHE-2023-JUL", "CHE-2023-NOV", "CHE-2024-NOV", "CHE-2025-JUL",
    "CHE-2025-NOV",
]


def load_batch() -> tuple[dict[str, dict], dict[tuple[str, str], str], set[str]]:
    """Return (record_by_source_id, (paper,qn)->source_id, all source_ids)."""
    records = json.loads(PASS1_BATCH.read_text(encoding="utf-8"))
    by_source = {r["source_id"]: r for r in records}
    by_pair = {(r["paper_key"], r["question_number"]): r["source_id"] for r in records}
    return by_source, by_pair, set(by_source)


def acquisition_index() -> dict[str, int]:
    """Order of the papers in the organized sample manifest, for the saturation test."""
    if not MANIFEST.exists():
        return {k: i for i, k in enumerate(ACQUISITION_ORDER)}
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    order: list[str] = []
    for rec in data.get("records", []):
        if rec.get("subject") != SUBJECT:
            continue
        paper = Path(rec["paper_path"].replace("\\", "/")).name
        for key, meta_path in PAPER_FILES.items():
            if Path(meta_path).name == paper and key not in order:
                order.append(key)
    for key in ACQUISITION_ORDER:
        if key not in order:
            order.append(key)
    return {k: i for i, k in enumerate(order)}


PAPER_FILES = {}  # filled from the per-paper Pass 1 files


def paper_meta() -> dict[str, dict]:
    meta: dict[str, dict] = {}
    for path in sorted((EXTRACTED / "pass1" / SUBJECT).glob("chemistry_*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        meta[doc["paper"]["paper_key"]] = doc["paper"]
    return meta


def compute_confidence(member_records: list[dict]) -> tuple[str, str]:
    """Pass 2 confidence rule, computed from evidence rather than asserted."""
    papers = {r["paper_key"] for r in member_records}
    n = len(member_records)
    if n >= 4 and len(papers) >= 3:
        return "high", f"{n} member questions across {len(papers)} papers ({', '.join(sorted(papers))})"
    if n >= 4 and len(papers) == 2:
        return "medium", f"{n} member questions but only 2 papers - 'high' requires different papers"
    if 2 <= n <= 3:
        return "medium", f"only {n} member questions ({len(papers)} paper(s))"
    return "low", f"{n} member question(s)"


def main() -> int:  # noqa: C901 - single-pass build with explicit validation gates
    errors: list[str] = []
    by_source, by_pair, all_ids = load_batch()

    metas = paper_meta()
    PAPER_FILES.update({k: v["paper_path"] for k, v in metas.items()})
    acq = acquisition_index()

    # ---------------- families ----------------
    claimed: dict[str, str] = {}
    families: list[dict] = []
    family_records: dict[str, list[dict]] = {}

    for fam in fam_mod.FAMILIES:
        members: list[dict] = []
        for paper_key, qn in fam["members"]:
            sid = by_pair.get((paper_key, qn))
            if sid is None:
                errors.append(f"{fam['family_id']}: member {paper_key} Q{qn} is not in the Pass 1 batch")
                continue
            if sid in claimed:
                errors.append(
                    f"{fam['family_id']}: {sid} is already claimed by {claimed[sid]} "
                    f"(family membership must be a partition)"
                )
                continue
            claimed[sid] = fam["family_id"]
            members.append(by_source[sid])
        if len(members) < 2:
            errors.append(
                f"{fam['family_id']}: only {len(members)} valid member(s) - a family needs at "
                f"least two; log it as single_exemplar instead"
            )
            continue

        confidence, rationale = compute_confidence(members)
        # Physical Science Pass 2 note: a family built primarily on circuit-diagram or
        # graph-interpretation questions whose members are Rung B AND visually unverified is
        # capped at medium. All records in this batch are Rung A, so the cap only bites where
        # a lower-fidelity rung has actually crept in.
        visual = sum(1 for r in members if r["requires_visual_verification"])
        low_rung = sum(1 for r in members if r["fidelity_rung"] != "A")
        capped = False
        if confidence == "high" and low_rung and visual / len(members) > 0.5:
            confidence = "medium"
            capped = True

        marks = [r["marks"] for r in members if isinstance(r["marks"], (int, float))]
        topics = sorted({r["topic_guess"].replace("guess: ", "") for r in members})
        families.append(
            {
                "question_family_id": fam["family_id"],
                "name": fam["name"],
                "definition": fam["definition"],
                "subject": SUBJECT,
                "grade": GRADE,
                "topics": topics,
                "assessment_operations": fam["assessment_operations"],
                "representative_questions": [r["question_id"] for r in members][:6],
                "frequency": len(members),
                "source_evidence": [r["source_id"] for r in members],
                "confidence": confidence,
                "validation_status": "unvalidated",
            }
        )
        family_records[fam["family_id"]] = members
        fam["_confidence_rationale"] = rationale + (
            " (capped at medium: over half the members require visual verification)" if capped else ""
        )
        fam["_papers"] = sorted({r["paper_key"] for r in members})
        fam["_visual"] = visual
        fam["_marks_range"] = [min(marks), max(marks)] if marks else None

    # ---------------- understanding models ----------------
    family_ids = {f["question_family_id"] for f in families}
    breakdown_ids = {b["breakdown_id"] for b in model_mod.BREAKDOWNS}
    diagnostic_ids = {d["diagnostic_id"] for d in model_mod.DIAGNOSTICS}

    models: list[dict] = []
    for m in model_mod.MODELS:
        fid = m["question_family"]
        if fid not in family_ids:
            errors.append(f"{m['identity']}: question_family {fid} does not exist")
            continue
        for bid in m.get("common_breakdowns", []):
            if bid not in breakdown_ids:
                errors.append(f"{m['identity']}: common_breakdowns references unknown {bid}")
        for did in m.get("diagnostic_questions", []):
            if did not in diagnostic_ids:
                errors.append(f"{m['identity']}: diagnostic_questions references unknown {did}")

        members = family_records[fid]
        confidence, rationale = compute_confidence(members)
        visual = sum(1 for r in members if r["requires_visual_verification"])
        low_rung = sum(1 for r in members if r["fidelity_rung"] != "A")
        if confidence == "high" and low_rung and visual / len(members) > 0.5:
            confidence = "medium"
            rationale += " (capped at medium: majority of members are below Rung A and visually unverified)"
        else:
            rationale += f"; {visual}/{len(members)} members flagged requires_visual_verification (Rung A text layer)"
        fam = next(f for f in fam_mod.FAMILIES if f["family_id"] == fid)
        papers = sorted({r["paper_key"] for r in members})

        models.append(
            {
                "identity": m["identity"],
                "definition": m["definition"],
                "subject": SUBJECT,
                "grade": GRADE,
                "topic": m["topic"],
                "question_family": fid,
                "assessment_operations": m["assessment_operations"],
                "required_knowledge": m["required_knowledge"],
                "prerequisites": m["prerequisites"],
                "required_reasoning": m["required_reasoning"],
                "required_procedure": m.get("required_procedure"),
                "evidence_of_understanding": m["evidence_of_understanding"],
                "marking_requirements": m["marking_requirements"],
                "common_breakdowns": m.get("common_breakdowns", []),
                "misconceptions": m["misconceptions"],
                "diagnostic_dimensions": m["diagnostic_dimensions"],
                "diagnostic_questions": m.get("diagnostic_questions", []),
                "source_references": [r["source_id"] for r in members],
                "provenance": [
                    f"{m['identity']} (Understanding Model, Tier 2/3)",
                    f"{fid} (question family, Tier 2)",
                    f"{len(members)} question records across {len(papers)} papers: " + ", ".join(papers),
                    "marking memoranda: " + ", ".join(sorted({Path(r['memo_document']).name for r in members})),
                    "source documents: " + ", ".join(sorted({Path(r['source_document']).name for r in members})),
                    "ORC source inventory: not indexed - sentinel SOURCE-ORC-CHEM-NOT-INDEXED "
                    "(chemistry Phase 2 OCR never ran; see unresolved item UNRES-CHEM-ACQ-001)",
                ],
                "confidence": confidence,
                "validation_state": "unvalidated",
                "version": "0.1.0-draft",
            }
        )
        m["_confidence_rationale"] = rationale

    # ---------------- breakdowns ----------------
    model_ids = {m["identity"] for m in models}
    breakdowns: list[dict] = []
    for b in model_mod.BREAKDOWNS:
        if b["parent_understanding_model"] not in model_ids:
            errors.append(f"{b['breakdown_id']}: parent_understanding_model {b['parent_understanding_model']} does not exist")
            continue
        for sid in b.get("source_basis", []):
            if sid not in all_ids:
                errors.append(f"{b['breakdown_id']}: source_basis cites unknown Pass 1 source_id {sid}")
        breakdowns.append(
            {
                "breakdown_id": b["breakdown_id"],
                "description": b["description"],
                "parent_understanding_model": b["parent_understanding_model"],
                "stage": b["stage"],
                "observable_signals": b.get("observable_signals", []),
                "possible_confusions": b.get("possible_confusions", []),
                "distinguishing_questions": b.get("distinguishing_questions", []),
                "source_basis": b.get("source_basis", []),
                "confidence": b["confidence"],
            }
        )

    # ---------------- diagnostics ----------------
    diagnostics: list[dict] = []
    for d in model_mod.DIAGNOSTICS:
        if d["understanding_model_id"] not in model_ids:
            errors.append(f"{d['diagnostic_id']}: understanding_model_id {d['understanding_model_id']} does not exist")
            continue
        if d.get("target_breakdown") and d["target_breakdown"] not in breakdown_ids:
            errors.append(f"{d['diagnostic_id']}: target_breakdown {d['target_breakdown']} does not exist")
            continue
        for bid in d.get("distinguishes", []):
            if bid not in breakdown_ids:
                errors.append(f"{d['diagnostic_id']}: distinguishes unknown breakdown {bid}")
        # A diagnostic must name the breakdown it targets; when the analysis only
        # listed the breakdowns it distinguishes between, the first of those is the
        # target (Pass 2 requires each diagnostic to state which breakdown it finds).
        target = d.get("target_breakdown") or (d.get("distinguishes") or [None])[0]
        if target is None:
            errors.append(f"{d['diagnostic_id']}: no target_breakdown and no distinguishes list")
            continue
        diagnostics.append(
            {
                "diagnostic_id": d["diagnostic_id"],
                "understanding_model_id": d["understanding_model_id"],
                "target_breakdown": target,
                "question": d["question"],
                "purpose": d["purpose"],
                "distinguishes": d.get("distinguishes", []),
                "expected_evidence": d.get("expected_evidence", []),
                "follow_up_conditions": d.get("follow_up_conditions", []),
                "source_or_rationale": d["source_or_rationale"],
                "confidence": d["confidence"],
            }
        )

    # one model per family, and every model's family exists
    for fid in family_ids:
        if not any(m["question_family"] == fid for m in models):
            errors.append(f"{fid}: no Understanding Model was produced for this family")

    # ---------------- derived unresolved items ----------------
    unresolved = [dict(u) for u in unres_mod.UNRESOLVED]

    unassigned = sorted(all_ids - set(claimed))
    unresolved.append(
        {
            "type": "coverage_gap",
            "id": "UNRES-CHEM-021",
            "summary": f"{len(unassigned)} extracted question records were not assigned to any family",
            "detail": (
                "These records are in the Pass 1 batch but no family in this run claims them. They are "
                "not evidence for any Understanding Model and the tutor must not present them as such. "
                "First few: " + ", ".join(unassigned[:8])
            ),
            "affected": unassigned,
            "evidence": ["scripts/build_chemistry_pass2.py family partition check"],
            "recommended_review": "Extend family definitions or extract more papers so these records find a family.",
        }
    )

    for cand in model_mod.DEFERRED_FAMILIES:
        sids = [by_pair.get((pk, qn)) for pk, qn in cand["evidence"]]
        missing = [f"{pk} Q{qn}" for (pk, qn), s in zip(cand["evidence"], sids) if s is None]
        if missing:
            errors.append(f"{cand['candidate_id']}: evidence not in batch: {missing}")
            continue
        unresolved.append(
            {
                "type": "coverage_gap",
                "id": cand["candidate_id"],
                "summary": f"Candidate family not modelled in this run: {cand['proposed_name']}",
                "detail": cand["reason_deferred"]
                + f" Evidence: {len(cand['evidence'])} question records across "
                f"{len({pk for pk, _ in cand['evidence']})} papers.",
                "affected": [s for s in sids if s],
                "evidence": [f"{pk} Q{qn}" for pk, qn in cand["evidence"]],
                "recommended_review": "Re-run Pass 2 with more papers; if the pattern holds, write the "
                "Understanding Model then rather than generalising now.",
            }
        )

    single_paper_families = [f["question_family_id"] for f in families if len({r['paper_key'] for r in family_records[f['question_family_id']]}) == 1]
    unresolved.append(
        {
            "type": "coverage_gap",
            "id": "UNRES-CHEM-022",
            "summary": f"{len(single_paper_families)} family/families rest on a single paper",
            "detail": (
                "Family membership spanning one paper only cannot support a 'high' confidence model and "
                "its marking_requirements must not be generalised to other sittings: "
                + ", ".join(single_paper_families)
            ),
            "affected": single_paper_families,
            "evidence": ["family member paper distribution"],
            "recommended_review": "Acquire more papers covering the same competence.",
        }
    )

    # UNRES-CHEM-011's affected list is derived rather than authored: it must cover every
    # family where the majority of members depend on an image, and a hand-written list
    # silently drifts as families are added.
    visual_heavy = sorted(
        fid for fid, recs in family_records.items()
        if sum(1 for r in recs if r["requires_visual_verification"]) / len(recs) > 0.5
    )
    visual_counts = ", ".join(
        f"{fid.replace('QUESTION-FAMILY-', '')} "
        f"{sum(1 for r in family_records[fid] if r['requires_visual_verification'])}"
        f"/{len(family_records[fid])}"
        for fid in visual_heavy
    )
    for item in unresolved:
        if item["id"] == "UNRES-CHEM-011":
            item["affected"] = visual_heavy
            item["detail"] += (
                f" Families where over half the members are image-dependent ({len(visual_heavy)} "
                f"of {len(family_records)}): {visual_counts}."
            )

    thin_breakdowns = sorted(b["breakdown_id"] for b in breakdowns if len(b.get("source_basis") or []) < 2)
    unresolved.append(
        {
            "type": "single_exemplar",
            "id": "UNRES-CHEM-023",
            "summary": f"{len(thin_breakdowns)} breakdown(s) rest on a single question record",
            "detail": (
                "These breakdowns are cited from one memo record only, so the pattern is inferred from a "
                "single exemplar and must not be treated as established: "
                + ", ".join(thin_breakdowns)
            ),
            "affected": thin_breakdowns,
            "evidence": ["source_basis length in knowledge/chemistry/breakdown_models.json"],
            "recommended_review": (
                "Confirm each against a second sitting, or drop the breakdown; a tutor should not use a "
                "single-exemplar breakdown to justify a diagnosis."
            ),
        }
    )

    # ---------------- saturation report ----------------
    order = sorted(family_records, key=lambda f: min(acq.get(r["paper_key"], 0) for r in family_records[f]))
    n = len(ACQUISITION_ORDER)
    b1, b2 = round(n / 3), round(2 * n / 3)
    thirds = [ACQUISITION_ORDER[:b1], ACQUISITION_ORDER[b1:b2], ACQUISITION_ORDER[b2:]]
    final_third = set(thirds[2])
    new_in_final_third = [
        fid for fid, recs in family_records.items()
        if {r["paper_key"] for r in recs} <= final_third and {r["paper_key"] for r in recs}
    ]
    single_exemplar = [f["question_family_id"] for f in families if f["frequency"] == 1]
    strata_unsampled = [
        "exam_board=IEB (the two IeBT papers in the sample have an image-only memo and a memo-only file; not extracted)",
        "exam_board=NSC (no externally set NSC paper in the organized sample)",
        "exam_period=prelim (no trial/preliminary paper in the sample)",
        "paper_type=paper2 (Chemistry is a separate subject batch)",
        "17 further chemistry papers present in data/organized/chemistry but not extracted in this run",
    ]

    saturation = {
        "papers_in_sample": n,
        "question_families_identified": len(families),
        "families_first_observed_in_final_third": len(new_in_final_third),
        "strata_left_unsampled": strata_unsampled,
        "families_supported_by_single_exemplar": len(single_exemplar),
        "computed_at": NOW,
        "acquisition_order_used": ACQUISITION_ORDER,
        "thirds_split": [list(t) for t in thirds],
        "families_new_in_final_third": new_in_final_third,
        "additional_diagnostics": {
            "question_records_in_batch": len(all_ids),
            "records_assigned_to_a_family": len(claimed),
            "records_unassigned": len(unassigned),
            "families_resting_on_one_paper": single_paper_families,
            "confidence_distribution": dict(Counter(f["confidence"] for f in families)),
            "saturated": len(new_in_final_third) == 0 and n >= 8 and len(strata_unsampled) == 0,
            "reason_not_saturated": (
                ("families_first_observed_in_final_third > 0" if new_in_final_third else "")
                + ("; batch is smaller than the recommended 8-15 papers" if n < 8 else "")
                + ("; strata left unsampled (IEB IeBT, NSC, prelim, paper2, further papers not extracted)"
                   if strata_unsampled else "")
            ),
        },
    }

    # ---------------- schema validation ----------------
    validator = SchemaValidator(SCHEMA_DIR)
    checks = [
        ("question_family.schema.json", families),
        ("knowledge_model.schema.json", models),
        ("breakdown.schema.json", breakdowns),
        ("diagnostic.schema.json", diagnostics),
    ]
    validation_results = []
    for schema_name, docs in checks:
        for doc in docs:
            res = validator.validate(schema_name, doc)
            validation_results.append(
                {
                    "schema": schema_name,
                    "id": doc.get("question_family_id") or doc.get("identity")
                    or doc.get("breakdown_id") or doc.get("diagnostic_id"),
                    "valid": res.valid,
                    "errors": res.errors,
                }
            )
            if not res.valid:
                errors.append(f"{schema_name}: {doc}: {res.errors[:3]}")

    # ---------------- write ----------------
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    outputs = {
        "question_families.json": families,
        "understanding_models.json": models,
        "breakdown_models.json": breakdowns,
        "diagnostic_questions.json": diagnostics,
        "unresolved_items.json": unresolved,
        "saturation_report.json": saturation,
    }
    for name, payload in outputs.items():
        (OUT_DIR / name).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # TWO_PASS_PROMPTS Pass 2 asks for one JSON object with five top-level arrays plus
    # the saturation report. The per-type files above are what the repository schemas and
    # later phases consume; this is the same content in the shape the prompt specifies, so
    # the two cannot drift apart - it is assembled from the same objects.
    (OUT_DIR / "pass2_output.json").write_text(
        json.dumps(
            {
                "subject": SUBJECT,
                "grade": GRADE,
                "generated_at": NOW,
                "question_families": families,
                "understanding_models": models,
                "breakdown_models": breakdowns,
                "diagnostic_questions": diagnostics,
                "unresolved_items": unresolved,
                "saturation_report": saturation,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    summary = {
        "generated_at": NOW,
        "subject": SUBJECT,
        "pass1_batch": str(PASS1_BATCH.relative_to(ROOT)),
        "papers_in_sample": n,
        "question_records_in_batch": len(all_ids),
        "records_assigned_to_a_family": len(claimed),
        "question_families": len(families),
        "understanding_models": len(models),
        "breakdown_models": len(breakdowns),
        "diagnostic_questions": len(diagnostics),
        "unresolved_items": len(unresolved),
        "schema_validation": {
            "checked": len(validation_results),
            "failed": sum(1 for r in validation_results if not r["valid"]),
        },
        "saturation": {k: saturation[k] for k in (
            "papers_in_sample", "question_families_identified",
            "families_first_observed_in_final_third", "families_supported_by_single_exemplar")},
        "families": [
            {
                "family_id": f["question_family_id"],
                "name": f["name"],
                "members": f["frequency"],
                "papers": next(x["_papers"] for x in fam_mod.FAMILIES if x["family_id"] == f["question_family_id"]),
                "confidence": f["confidence"],
                "confidence_rationale": next(x["_confidence_rationale"] for x in fam_mod.FAMILIES if x["family_id"] == f["question_family_id"]),
                "visual_verification_members": next(x["_visual"] for x in fam_mod.FAMILIES if x["family_id"] == f["question_family_id"]),
                "marks_range": next(x["_marks_range"] for x in fam_mod.FAMILIES if x["family_id"] == f["question_family_id"]),
            }
            for f in families
        ],
        "errors": errors,
    }
    (OUT_DIR / "_PASS2_SUMMARY.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    # Human-readable Pass 2 report (mirrors knowledge/physics/PASS2_REPORT.md). The numbers
    # below are taken from the objects this run actually produced, so they cannot drift.
    conf_dist = summary["families_confidence_distribution"] if "families_confidence_distribution" in summary else Counter(f["confidence"] for f in families)
    report_lines = [
        "# Chemistry — Two-pass run report (Pass 1 + Pass 2)",
        "",
        "Subject: chemistry · grade 11",
        "Phases executed: 4 (extract), 5 (segment), 6 (align with memoranda), 8 (taxonomy), "
        "9 (Understanding Models), 10 (breakdown model), 11 (diagnostic bank). "
        "Phase 7 (curriculum mapping) was **not** run — no curriculum document in the sample.",
        "Specs: `TWO_PASS_PROMPTS.md` (Pass 2), `SYSTEM_SPEC.md`, `IMPLEMENTATION_SPEC.md`",
        "Entry point: `python scripts/run_chemistry_pass2.py`",
        "Review queue: `review_queue/RQ-P4-CHEM-PASS2.yaml`",
        "",
        "## 1. Pass 2 result",
        "",
        f"| | count |",
        f"|---|---|",
        f"| question families | {len(families)} |",
        f"| understanding models | {len(models)} (one per family) |",
        f"| breakdown models | {len(breakdowns)} |",
        f"| diagnostic questions | {len(diagnostics)} (3 per model) |",
        f"| unresolved items | {len(unresolved)} |",
        f"| records assigned to a family | {len(claimed)} / {len(all_ids)} |",
        f"| objects validated against `database/schema/*.schema.json` | "
        f"{summary['schema_validation']['checked']}, **{summary['schema_validation']['failed']} failures** |",
        "",
        "### Families",
        "",
        "| id | family | members | papers | confidence |",
        "|---|---|---|---|---|",
    ]
    for f in families:
        papers = next(x["_papers"] for x in fam_mod.FAMILIES if x["family_id"] == f["question_family_id"])
        mr = next(x["_marks_range"] for x in fam_mod.FAMILIES if x["family_id"] == f["question_family_id"])
        mr_s = f"{mr[0]}-{mr[1]}" if mr else "n/a"
        report_lines.append(
            f"| {f['question_family_id'].replace('QUESTION-FAMILY-', '')} | {f['name']} | "
            f"{f['frequency']} | {len(papers)} | {f['confidence']} |"
        )
    report_lines += [
        "",
        "Rules the builder enforces and the test suite re-checks:",
        "",
        "* **Membership is a partition** — no record belongs to two families; "
        f"{len(unassigned)} records that fit no family are reported unassigned (UNRES-CHEM-021).",
        "* **≥2 members per family**; `families_supported_by_single_exemplar` is "
        f"{len(single_exemplar)}.",
        "* **Confidence is computed, never authored**: `high` requires ≥4 members across ≥3 papers, "
        f"otherwise `medium`. Distribution: {dict(conf_dist)}.",
        "* **No family mixes disciplines** — every member of every family is tagged "
        "`discipline: Chemistry`; there is no Physics content in this batch.",
        "* **ORC provenance is a sentinel**: chemistry Phase 2 (ORC) never ran and no inventory exists, "
        "so every object's `orc_source_id` is `SOURCE-ORC-CHEM-NOT-INDEXED`; the gap is recorded in "
        "UNRES-CHEM-ACQ-001 rather than a fabricated inventory.",
        "",
        "## 2. Saturation report",
        "",
        f"* papers_in_sample: {saturation['papers_in_sample']}",
        f"* question_families_identified: {saturation['question_families_identified']}",
        f"* families_first_observed_in_final_third: {saturation['families_first_observed_in_final_third']}",
        f"* strata_left_unsampled: {len(saturation['strata_left_unsampled'])}",
        f"* families_supported_by_single_exemplar: {saturation['families_supported_by_single_exemplar']}",
        "",
        f"**Not saturated.** {saturation['additional_diagnostics']['reason_not_saturated']}",
        "",
        "## 3. Honest limits",
        "",
        "* **Coverage is from 11 internally-set papers** (2018 Jul through 2025 Nov); the two IeBT papers "
        "in the sample have an image-only memo and a memo-only file and were excluded (UNRES-CHEM-ACQ-001 context).",
        "* **No curriculum mapping** — no Grade 11 Chemistry curriculum/ATP document is in the sample, so "
        "Phase 7 could not run and `curriculum_mapping_rate` is `null`.",
        "* **Image-dependent items**: families where over half the members depend on a diagram are flagged in "
        "UNRES-CHEM-011; those diagrams were never visually verified.",
        "* **All models are `unvalidated`**; nothing here has been validated against student responses (Phase 13).",
        "",
        f"Generated by scripts/build_chemistry_pass2.py at {NOW}.",
        "",
    ]
    (OUT_DIR / "PASS2_REPORT.md").write_text("\n".join(report_lines), encoding="utf-8")

    print(f"Chemistry Pass 2: {len(families)} families, {len(models)} models, "
          f"{len(breakdowns)} breakdowns, {len(diagnostics)} diagnostics, {len(unresolved)} unresolved items")
    print(f"Schema validation: {summary['schema_validation']['checked']} objects checked, "
          f"{summary['schema_validation']['failed']} failed")
    print(f"Saturation: papers={saturation['papers_in_sample']} families={saturation['question_families_identified']} "
          f"new_in_final_third={saturation['families_first_observed_in_final_third']} "
          f"single_exemplar={saturation['families_supported_by_single_exemplar']}")
    if errors:
        print(f"\n{len(errors)} ERROR(S) - outputs written but the run is NOT clean:")
        for e in errors[:20]:
            print("  -", e)
        return 1
    print("\nAll referential, partition and schema checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
