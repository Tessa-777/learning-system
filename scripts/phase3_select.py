#!/usr/bin/env python3
"""Phase 3 (revised) — Build the form-stratified saturation corpus selection.

This driver implements the corpus-sufficiency revision recorded in
``CORPUS_SUFFICIENCY_POLICY.md`` and ``IMPLEMENTATION_SPEC.md`` §4 (v1.1.0).

It replaces blanket acquisition of all 821 discovered records with an explicit,
reviewable *selection* of the documents that can actually populate the
knowledge bank's primary objects: question families and Understanding Models.

What it does
------------
1. reads the six Phase 2 source inventories (read-only; they are provenance)
2. classifies every past paper into an assessment-form stratum
   (setter x paper form x sitting) - see ingestion/acquisition/forms.py
3. samples the strata in two passes (coverage, then depth)
4. pairs each selected paper with its memorandum / marking guide
5. attaches companion documents without which the paper cannot be answered
   (source booklets, data sheets, diagram booklets, answer sheets)
6. attaches authoritative curriculum anchors where the ORC holds any
7. writes data/raw/CORPUS_SELECTION.yaml and data/raw/DOWNLOAD_CHECKLIST.md
8. writes the run log, decisions, metrics and a review-queue item

What it deliberately does NOT do
--------------------------------
* download anything (no network is available to sandbox code; acquisition is
  performed by scripts/phase3_ingest_drop.py from files supplied locally, or by
  a proxy-assisted acquisition run)
* modify the Phase 2 inventories
* analyse any educational content (that is Phase 5 and later)
* proceed into Phase 4

Usage
-----
    python3 scripts/phase3_select.py
    python3 scripts/phase3_select.py --papers-per-subject 5 --min-year-gap 3
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from core import yamllite  # noqa: E402
from core.config import Config  # noqa: E402
from ingestion.acquisition.inventory import read_source_records  # noqa: E402
from ingestion.acquisition.selection import (  # noqa: E402
    DEFAULT_MIN_YEAR_GAP,
    DEFAULT_PAPERS_PER_SUBJECT,
    build_selection,
)
from ingestion.run_context import RunContext  # noqa: E402

PHASE = "3-selection"
SUBJECTS = ("biology", "physics", "history", "english", "ap_mathematics", "mathematics")
SELECTION_PATH = REPO_ROOT / "data" / "raw" / "CORPUS_SELECTION.yaml"
CHECKLIST_PATH = REPO_ROOT / "data" / "raw" / "DOWNLOAD_CHECKLIST.md"
REVIEW_PATH = REPO_ROOT / "review_queue" / "RQ-P3-CORPUS-SELECTION.yaml"


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def build_selection_document(
    selection, inventories, papers_per_subject, min_year_gap
) -> dict:
    """Assemble the CORPUS_SELECTION.yaml document."""
    totals = {"papers": 0, "memoranda": 0, "companions": 0, "curriculum_anchors": 0}
    subjects_block = {}
    for subject in SUBJECTS:
        result = selection[subject]
        totals["papers"] += len(result.papers)
        totals["memoranda"] += sum(1 for p in result.papers if p.memo.source_id)
        totals["companions"] += sum(len(p.companions) for p in result.papers)
        totals["curriculum_anchors"] += len(result.curriculum_anchors)
        subjects_block[subject] = result.to_dict()

    return {
        "selection_id": "CORPUS-SEL-V1",
        "phase": PHASE,
        "generated_at": _utcnow(),
        "policy_document": "CORPUS_SUFFICIENCY_POLICY.md",
        "spec_version": "1.1.0",
        "primary_source": "https://sites.google.com/stbenedicts.co.za/orc",
        "objective": (
            "Select the minimum authoritative corpus that saturates the question "
            "taxonomy and the Understanding Models, rather than the maximum "
            "corpus that covers the syllabus."
        ),
        "sampling_method": {
            "stratification": "assessment form = setter x paper_form x session",
            "pass_1": "coverage - one exemplar per stratum",
            "pass_2": "depth - a second, older exemplar for the largest strata",
            "papers_per_subject_budget": papers_per_subject,
            "min_year_gap_between_exemplars": min_year_gap,
            "memo_pairing_strategies": [
                "stratum_year_unique",
                "order_prefix",
                "qp_mg_suffix",
                "title_similarity",
            ],
            "memo_availability_is_a_selection_criterion": True,
            "stopping_rule": (
                "empirical saturation at Phase 8/13, not a fixed document count; "
                "see CORPUS_SUFFICIENCY_POLICY.md"
            ),
        },
        "discovered_records_total": sum(len(v) for v in inventories.values()),
        "totals": {
            **totals,
            "documents_to_acquire": (
                totals["papers"]
                + totals["memoranda"]
                + totals["companions"]
                + totals["curriculum_anchors"]
            ),
        },
        "subjects": subjects_block,
    }


def build_checklist(document: dict) -> str:
    """Render a human-actionable download checklist."""
    lines = [
        "# Corpus download checklist",
        "",
        f"Generated {_utcnow()} by `scripts/phase3_select.py` "
        f"(selection `{document['selection_id']}`).",
        "",
        f"**{document['totals']['documents_to_acquire']} documents** across six "
        "subjects, selected by assessment form rather than by topic coverage.",
        "",
        "Download each file from its Drive link and save it under the target path",
        "shown. Keep the original filename. Do not convert, re-save or edit the",
        "files - Phase 3 must hash the originals byte-for-byte.",
        "",
        "When the files are in place, run:",
        "",
        "```bash",
        "python3 scripts/phase3_ingest_drop.py",
        "```",
        "",
        "---",
        "",
    ]
    for subject in SUBJECTS:
        block = document["subjects"][subject]
        lines.append(f"## {subject}")
        lines.append("")
        lines.append(
            f"{block['papers_selected']} papers selected from "
            f"{block['candidate_past_papers']} candidate past papers "
            f"({block['strata_found']} assessment forms present)."
        )
        lines.append("")
        for paper in block["papers"]:
            stratum = paper["stratum"]
            label = f"{stratum['setter']} / {stratum['paper_form']} / {stratum['session']}"
            lines.append(f"### {paper['title']}")
            lines.append("")
            lines.append(f"- **form:** {label}  ")
            lines.append(f"- **role:** {paper['exemplar_role']} ({paper['year']})  ")
            lines.append(f"- **source_id:** `{paper['source_id']}`  ")
            if paper.get("flags"):
                lines.append(f"- **flags:** {', '.join(paper['flags'])}  ")
            lines.append(f"- **why:** {paper['selection_reason']}")
            lines.append("")
            lines.append("| # | document | type | drive link | save as |")
            lines.append("|---|---|---|---|---|")
            lines.append(
                f"| [ ] | {paper['title']} | question paper | "
                f"[download]({paper['source_url']}) | `{paper['expected_path']}` |"
            )
            memo = paper.get("memo") or {}
            if memo.get("source_id"):
                lines.append(
                    f"| [ ] | {memo.get('title')} | {memo.get('document_type')} "
                    f"(paired by {memo.get('pair_method')}, {memo.get('pair_confidence')}) | "
                    f"[download]({memo.get('source_url')}) | "
                    f"`data/raw/{subject}/memoranda/{memo.get('title')}` |"
                )
            else:
                lines.append(
                    "| - | **no memorandum exists in the ORC for this paper** | "
                    "unresolved | - | - |"
                )
            for companion in paper.get("companions") or []:
                lines.append(
                    f"| [ ] | {companion.get('title')} | companion "
                    f"({companion.get('document_type')}) | "
                    f"[download]({companion.get('source_url')}) | "
                    f"`data/raw/{subject}/companions/{companion.get('title')}` |"
                )
            lines.append("")
        anchors = block.get("curriculum_anchors") or []
        if anchors:
            lines.append("### Curriculum anchors")
            lines.append("")
            lines.append("| # | document | drive link | save as |")
            lines.append("|---|---|---|---|")
            for anchor in anchors:
                lines.append(
                    f"| [ ] | {anchor.get('title')} | "
                    f"[download]({anchor.get('source_url')}) | "
                    f"`data/raw/{subject}/curriculum/{anchor.get('title')}` |"
                )
            lines.append("")
        for note in block.get("notes") or []:
            lines.append(f"> **Note:** {note}")
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--papers-per-subject",
        type=int,
        default=DEFAULT_PAPERS_PER_SUBJECT,
        help="per-subject paper budget (default: %(default)s)",
    )
    parser.add_argument(
        "--min-year-gap",
        type=int,
        default=DEFAULT_MIN_YEAR_GAP,
        help="minimum year gap between the two exemplars of a form (default: %(default)s)",
    )
    parser.add_argument(
        "--no-run-log", action="store_true", help="skip writing a run log"
    )
    args = parser.parse_args()

    inventories = {
        subject: read_source_records(
            REPO_ROOT / "data" / "raw" / subject / "SOURCE_INVENTORY.yaml"
        )
        for subject in SUBJECTS
    }
    selection = build_selection(
        inventories,
        papers_per_subject=args.papers_per_subject,
        min_year_gap=args.min_year_gap,
    )
    document = build_selection_document(
        selection, inventories, args.papers_per_subject, args.min_year_gap
    )

    SELECTION_PATH.write_text(yamllite.dumps(document), encoding="utf-8")
    CHECKLIST_PATH.write_text(build_checklist(document), encoding="utf-8")

    unpaired = [
        (subject, paper.title)
        for subject in SUBJECTS
        for paper in selection[subject].papers
        if not paper.memo.source_id
    ]

    print(f"wrote {SELECTION_PATH.relative_to(REPO_ROOT)}")
    print(f"wrote {CHECKLIST_PATH.relative_to(REPO_ROOT)}")
    totals = document["totals"]
    print(
        "papers={papers} memoranda={memoranda} companions={companions} "
        "anchors={curriculum_anchors} TOTAL={documents_to_acquire}".format(**totals)
    )
    if unpaired:
        print(f"\n{len(unpaired)} selected paper(s) have no memorandum in the ORC:")
        for subject, title in unpaired:
            print(f"  - {subject}: {title}")

    if args.no_run_log:
        return 0

    config = Config.load()
    ctx = RunContext(config=config, phase=PHASE, subject="all")
    ctx.start()
    ctx.log_event(
        "corpus_selection_built",
        message="form-stratified saturation sample built for all six subjects",
        metadata={"totals": totals},
    )
    ctx.log_decision(
        decision_id="DEC-P3-SEL-001",
        decision_type="corpus_scope",
        context=(
            "IMPLEMENTATION_SPEC §4 (v1.0.0) required acquiring every accessible "
            "source (821 records). Phase 3 failed for all of them because sandbox "
            "code has no outbound TLS, and the objective was later revised."
        ),
        evidence=[
            "821 records = 209 past papers + 237 memoranda + 122 marking guides "
            "+ 165 assessment items + 85 reference docs + 1 curriculum + 7 other",
            "verified duplicate content: physics Nov-2022 exam exists under two "
            "distinct Drive IDs (1BLMEfPahfO7b751FXS8oM_ZhtxcIxQcT and "
            "16NXMYVKTVQ4K2zeHjm-0DS-AXUoLF5wD) with identical extracted text",
            "physics 2022 IEB Trial P1 appears under three Drive IDs and three "
            "naming schemes",
            "SYSTEM_SPEC §9: an Understanding Model describes 'the underlying "
            "competence being assessed', not topic content",
            "IMPLEMENTATION_SPEC §9 hard rule: 'Do not create one family for "
            "every individual question'",
            "question families track assessment form, not year or topic: the Nov "
            "2018 Mathematics P2 declares its own topic/mark table and the Nov "
            "2022 Physics paper labels its own question families",
        ],
        alternatives=[
            "acquire all 821 records (original plan; infeasible offline and "
            "mismatched to a compression objective)",
            "acquire all 209 past papers",
            "form-stratified saturation sample with an empirical stopping rule",
            "arbitrary fixed sample with no stratification",
        ],
        selected="form-stratified saturation sample with an empirical stopping rule",
        rationale=(
            "Stratifying on assessment form guarantees every distinct kind of "
            "paper the school sits is represented, which is what determines which "
            "question families can appear. Two exemplars per form is the minimum "
            "that can show a family recurs rather than being a one-off. "
            "Sufficiency is then decided empirically by the Phase 8/13 saturation "
            "test rather than asserted up front."
        ),
        confidence="high",
        requires_review=True,
    )
    ctx.log_decision(
        decision_id="DEC-P3-SEL-002",
        decision_type="memo_pairing",
        context=(
            "A question paper without its memorandum cannot support Phase 6 "
            "alignment or a defensible Understanding Model (AGENTS.md rule 8)."
        ),
        evidence=[
            "four pairing strategies implemented, strongest first: "
            "stratum_year_unique, order_prefix, qp_mg_suffix, title_similarity",
            "memo pool is scope-filtered: without it, English P2 2023 was "
            "structurally matched to 'MEMO Contextual Test Film Grade 12'",
            "history holds only 3 memoranda for 11 past papers, and 2 of the 3 "
            "are class tests, so 4 of 5 selected history papers have no memo",
        ],
        alternatives=[
            "select papers without regard to memo availability",
            "prefer papers that have a memorandum",
        ],
        selected="prefer papers that have a memorandum",
        rationale=(
            "Memo availability is treated as a selection criterion, not just an "
            "output, so the limited budget is spent on papers that can actually "
            "carry marking evidence."
        ),
        confidence="high",
        requires_review=False,
    )
    for subject in SUBJECTS:
        for note in selection[subject].notes:
            ctx.log_error(
                subject=subject,
                error_type="corpus_gap",
                message=note,
                status="unresolved",
            )
    ctx.set_metrics(
        {
            "discovered_records_total": document["discovered_records_total"],
            "papers_selected": totals["papers"],
            "memoranda_paired": totals["memoranda"],
            "companions_attached": totals["companions"],
            "curriculum_anchors": totals["curriculum_anchors"],
            "documents_to_acquire": totals["documents_to_acquire"],
            "papers_without_memorandum": len(unpaired),
            "papers_per_subject_budget": args.papers_per_subject,
        }
    )
    ctx.record_artifact(
        SELECTION_PATH, type="yaml", description="form-stratified corpus selection"
    )
    ctx.record_artifact(
        CHECKLIST_PATH, type="markdown", description="human download checklist"
    )

    REVIEW_PATH.write_text(
        yamllite.dumps(
            {
                "review_id": "RQ-P3-CORPUS-SELECTION",
                "phase": PHASE,
                "raised_at": _utcnow(),
                "severity": "high",
                "status": "open",
                "title": "Corpus scope reduced from 821 records to a saturation sample",
                "summary": (
                    "Phase 3 no longer acquires every discovered source. The "
                    f"selection is {totals['documents_to_acquire']} documents "
                    "chosen by assessment form. This requires human sign-off "
                    "because it changes what the knowledge bank can claim to "
                    "cover."
                ),
                "requires_human_decision": [
                    "approve the per-subject paper budget "
                    f"({args.papers_per_subject})",
                    "approve the strata left unrepresented (see per-subject notes)",
                    "accept that 4 of 6 subjects have no curriculum anchor "
                    "document, so Phase 7 topic hierarchies will be `derived`",
                    "accept that history has effectively no memoranda, so Phase 6 "
                    "cannot align most history questions",
                    "confirm whether byte-exact originals will be supplied, or "
                    "whether proxy transcriptions are acceptable as Tier-1 "
                    "derivative evidence",
                ],
                "papers_without_memorandum": [
                    {"subject": s, "title": t} for s, t in unpaired
                ],
                "affected_artifacts": [
                    "data/raw/CORPUS_SELECTION.yaml",
                    "data/raw/DOWNLOAD_CHECKLIST.md",
                    "CORPUS_SUFFICIENCY_POLICY.md",
                    "SYSTEM_SPEC.md",
                    "IMPLEMENTATION_SPEC.md",
                ],
            }
        ),
        encoding="utf-8",
    )
    ctx.record_artifact(
        REVIEW_PATH, type="yaml", description="review item for the scope change"
    )
    ctx.complete("completed_with_review", unresolved_items=len(unpaired))
    print(f"\nrun logged: {ctx.logger.run_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
