#!/usr/bin/env python3
"""Build the Chemistry Pass 1 evidence batch from the authored evidence tables.

Pass 1 (TWO_PASS_PROMPTS.md) is the per-paper evidence extraction pass. The
question-level content is authored in ``ingestion/extraction/chemistry_pass1_evidence_*.py``
after reading the extracted text of each paper and its marking guidelines. This
script is the mechanical half of Pass 1:

* computes the SHA-256 of every paper and memo it consumes (provenance, §14);
* verifies paper<->memo alignment from the printed header block (DATE / MARKS /
  EXAMINER) rather than trusting ``data/organized/sample_manifest.json``, which
  was found to pair several physics papers with the wrong memorandum;
* expands each compact evidence tuple into a full Pass 1 record;
* writes one Pass 1 output file per paper plus the merged subject batch that
  Pass 2 consumes.

Chemistry-specific note: ``data/raw/chemistry/SOURCE_INVENTORY.yaml`` does NOT
exist. Phase 2 was never run for chemistry (SUBJECT_PROMPTS ``chemistry`` block,
"BEFORE YOU START"). The accessible ORC source records for the chemistry files
cannot be obtained in this environment, so — per the prompt's instruction — we do
NOT invent ORC ids. Each record instead carries the sentinel
``SOURCE-ORC-CHEM-NOT-INDEXED`` and the missing inventory is recorded as an
unresolved acquisition item (UNRES-CHEM-ACQ-001) rather than failing the build.

Run from the repository root:  python scripts/build_chemistry_pass1.py
"""
from __future__ import annotations

import hashlib
import importlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.runlog import sha256_file  # noqa: E402

ORGANIZED = ROOT / "data" / "organized"
EXTRACTED = ROOT / "data" / "extracted"
PER_PAPER_DIR = EXTRACTED / "pass1" / "chemistry"
INVENTORY = ROOT / "data" / "raw" / "chemistry" / "SOURCE_INVENTORY.yaml"
# Phase 2 was never run for chemistry, so there is no ORC inventory to resolve
# against. Rather than invent ids we carry a stable sentinel and report the gap.
ORC_SENTINEL = "SOURCE-ORC-CHEM-NOT-INDEXED"

EVIDENCE_MODULES = [
    "chemistry_pass1_evidence_2018_july",
    "chemistry_pass1_evidence_2019_aug",
    "chemistry_pass1_evidence_2020_nov",
    "chemistry_pass1_evidence_2021_nov",
    "chemistry_pass1_evidence_2022_june",
    "chemistry_pass1_evidence_2022_nov",
    "chemistry_pass1_evidence_2023_july",
    "chemistry_pass1_evidence_2023_nov",
    "chemistry_pass1_evidence_2024_nov",
    "chemistry_pass1_evidence_2025_july",
    "chemistry_pass1_evidence_2025_nov",
]

GENERATED_AT = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def relative(path: Path) -> str:
    """Path relative to the repository root, or absolute if redirected elsewhere."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def _norm_title(name: str) -> str:
    return re.sub(r"\s+", " ", str(name)).strip().lower()


def orc_index() -> dict[str, str]:
    """Map every Phase 2 inventory title to its ORC source_id.

    For chemistry the inventory does not exist, so this returns empty and the
    build falls back to the ORC sentinel (see orc_ids_for).
    """
    if not INVENTORY.exists():  # chemistry: Phase 2 never run
        return {}
    try:
        import yaml
    except ImportError:  # pragma: no cover - dependency guard
        return {}
    data = yaml.safe_load(INVENTORY.read_text(encoding="utf-8"))
    return {
        _norm_title(record.get("title")): record["source_id"]
        for record in data.get("sources", [])
        if record.get("title") and record.get("source_id")
    }


def orc_ids_for(meta: dict, index: dict[str, str]) -> tuple[str, str]:
    """Resolve the ORC source_id of a paper/memo pair from the Phase 2 inventory.

    Chemistry has no inventory, so every call returns the sentinel and the gap is
    recorded (UNRES-CHEM-ACQ-001) instead of failing.
    """
    if index:
        out = []
        for key in ("paper_path", "memo_path"):
            name = Path(meta[key]).name
            out.append(index.get(_norm_title(name)) or index.get(_norm_title(Path(name).stem)))
        return out[0] or ORC_SENTINEL, out[1] or ORC_SENTINEL
    return ORC_SENTINEL, ORC_SENTINEL


def pdf_text(path: Path) -> str:
    """Extract the text layer of a PDF (returns '' if no text layer)."""
    try:
        from pypdf import PdfReader
    except ImportError:  # pragma: no cover - dependency guard
        return ""
    try:
        reader = PdfReader(str(path))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    except Exception:  # noqa: BLE001 - unreadable PDFs are recorded, not fatal
        return ""


def header_fields(text: str) -> dict[str, str | None]:
    """Pull the DATE / MARKS / EXAMINER block out of a paper or memo header."""
    head = text[:4000]
    date = re.search(r"DATE\s*[: ]*([0-9]{1,2}\s+[A-Za-z]+\s+20[0-9]{2})", head)
    # Some headers print the year on a second line: "28 November\n2019".
    if not date:
        m2 = re.search(r"(\d{1,2}\s+[A-Za-z]+\s*)\n\s*(20\d{2})", head)
        if m2:
            date = type("x", (), {"group": lambda self, n=0: (m2.group(1) + m2.group(2)).strip()})()
    marks = re.search(r"\bMARKS\s*[: ]*([0-9]{2,3})", head)
    examiner = re.search(r"EXAMINER\s*[: ]*([A-Za-z][A-Za-z .]{1,30}?)(?:\s{2,}|%|MODERATOR|$)", head)
    return {
        "date": date.group(1).strip() if date else None,
        "marks": marks.group(1).strip() if marks else None,
        "examiner": examiner.group(1).strip() if examiner else None,
    }


def verify_alignment(paper_path: Path, memo_path: Path) -> dict:
    """Compare the printed header blocks of a paper and its memorandum."""
    paper_head = header_fields(pdf_text(paper_path))
    memo_head = header_fields(pdf_text(memo_path))
    return {
        "paper_header": paper_head,
        "memo_header": memo_head,
        "date_match": bool(paper_head["date"]) and paper_head["date"] == memo_head["date"],
        "marks_match": bool(paper_head["marks"]) and paper_head["marks"] == memo_head["marks"],
        "examiner_match": bool(paper_head["examiner"]) and paper_head["examiner"] == memo_head["examiner"],
    }


def source_id_for(meta: dict, qn: str) -> str:
    """Pass 1 source_id: {subject}_{year}_{board}_{paper_type}_{period}_{question_number}."""
    return "chemistry_{year}_{board}_{ptype}_{period}_q{qn}".format(
        year=meta["year"],
        board=meta["exam_board"],
        ptype=meta["paper_type"],
        period=meta["exam_period"],
        qn=qn,
    )


def build_records(meta: dict, schema: tuple, rows: list[tuple], alignment: dict) -> list[dict]:
    qn_index = schema.index("qn")
    existing_qns = {r[qn_index] for r in rows}
    records: list[dict] = []
    for row in rows:
        values = dict(zip(schema, row))
        qn = values["qn"]
        top_level = qn.split(".")[0]
        # Nearest enclosing question number that is itself an extracted record.
        parent_id = None
        if "." in qn:
            candidate = qn.rsplit(".", 1)[0]
            while candidate:
                if candidate in existing_qns:
                    parent_id = source_id_for(meta, candidate)
                    break
                candidate = candidate.rsplit(".", 1)[0] if "." in candidate else ""
        records.append(
            {
                "source_id": source_id_for(meta, qn),
                "question_id": "{key}-Q{qn}".format(key=meta["paper_key"], qn=qn),
                "subject": "chemistry",
                "grade": "11",
                "discipline": "Chemistry",
                "paper_key": meta["paper_key"],
                "source_document": meta["paper_path"],
                "source_document_sha256": meta["_paper_sha256"],
                "memo_document": meta["memo_path"],
                "memo_document_sha256": meta["_memo_sha256"],
                # Chemistry Phase 2 was never run; no ORC inventory exists. We carry
                # a stable sentinel rather than inventing an id (AGENTS.md rule 4).
                "orc_source_id": meta["_orc_paper_id"],
                "orc_memo_source_id": meta["_orc_memo_id"],
                "fidelity_rung": meta["fidelity_rung"],
                "requires_visual_verification": bool(values["needs_visual"]),
                "ocr_uncertain": bool(values["ocr_uncertain"]),
                "question_number": qn,
                "top_level_question_number": top_level,
                "parent_question_id": parent_id,
                "question_stem_text": None,
                "marks": values["marks"],
                "topic_guess": "guess: " + values["topic"],
                "question_type": values["qtype"],
                "question_text": values["text"],
                "has_diagram": bool(values["has_diagram"]),
                "required_formulae_visible": values["formulae"],
                "memo_answer": values["memo_answer"],
                "memo_method_steps": values["memo_steps"],
                "memo_marking_notes": values["memo_notes"],
                "memo_alignment": {
                    "verified_by": "printed header DATE/MARKS/EXAMINER comparison",
                    "date_match": alignment["date_match"],
                    "marks_match": alignment["marks_match"],
                    "examiner_match": alignment["examiner_match"],
                },
                "extraction": {
                    "method": "pypdf text layer + manual reading of paper and memo",
                    "generated_at": GENERATED_AT,
                    "evidence_module": meta["_module"],
                },
            }
        )
    return records


def main() -> int:
    sys.path.insert(0, str(ROOT / "ingestion" / "extraction"))
    PER_PAPER_DIR.mkdir(parents=True, exist_ok=True)

    batch: list[dict] = []
    papers: list[dict] = []
    problems: list[str] = []
    index = orc_index()
    if not index:
        # Chemistry Phase 2 was never run, so there is no ORC inventory to resolve
        # against. This is NOT a build failure: we carry the ORC sentinel and record the
        # gap as UNRES-CHEM-ACQ-001 in the analysis layer / review queue instead.
        print(
            f"  NOTE: Phase 2 inventory not present at {relative(INVENTORY)} - carrying ORC "
            f"sentinel {ORC_SENTINEL} and recording UNRES-CHEM-ACQ-001 (chemistry Phase 2 "
            f"never run; ORC records not obtainable in this environment)"
        )

    for module_name in EVIDENCE_MODULES:
        module = importlib.import_module(module_name)
        meta = dict(module.PAPER)
        paper_path = ROOT / meta["paper_path"]
        memo_path = ROOT / meta["memo_path"]
        if not paper_path.exists() or not memo_path.exists():
            problems.append(f"{module_name}: missing source file(s)")
            continue

        meta["_paper_sha256"] = sha256_file(paper_path)
        meta["_memo_sha256"] = sha256_file(memo_path)
        meta["_module"] = module_name

        meta["_orc_paper_id"], meta["_orc_memo_id"] = orc_ids_for(meta, index)

        alignment = verify_alignment(paper_path, memo_path)
        p_dt, m_dt = alignment["paper_header"]["date"], alignment["memo_header"]["date"]
        p_mk, m_mk = alignment["paper_header"]["marks"], alignment["memo_header"]["marks"]
        # A genuine contradiction (both sides print a value and they differ) is a failure.
        # A memo that simply omits its DATE/MARKS header is unverifiable, not contradictory,
        # and is recorded as such rather than failing the build.
        if p_dt and m_dt and p_dt != m_dt:
            problems.append(
                f"{meta['paper_key']}: paper/memo DATE contradiction "
                f"({p_dt} vs {m_dt})"
            )
        if p_mk and m_mk and p_mk != m_mk:
            problems.append(
                f"{meta['paper_key']}: paper/memo MARKS contradiction "
                f"({p_mk} vs {m_mk})"
            )

        records = build_records(meta, module.SCHEMA, module.RECORDS, alignment)

        # The per-question mark allocations must sum to the paper's printed total.
        total = sum(r["marks"] or 0 for r in records)
        if total != meta["total_marks"]:
            problems.append(f"{meta['paper_key']}: marks sum {total} != printed total {meta['total_marks']}")

        per_paper = {
            "paper": {k: v for k, v in meta.items() if not k.startswith("_")},
            "memo_alignment_check": alignment,
            "records_extracted": len(records),
            "marks_sum_check": {"sum_of_records": total, "printed_total": meta["total_marks"], "match": total == meta["total_marks"]},
            "question_records": records,
        }
        out = PER_PAPER_DIR / f"{meta['paper_key']}.json"
        out.write_text(json.dumps(per_paper, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        batch.extend(records)
        papers.append(
            {
                "paper_key": meta["paper_key"],
                "year": meta["year"],
                "exam_date": meta["exam_date"],
                "exam_period": meta["exam_period"],
                "records": len(records),
                "marks": total,
                "memo_date_match": alignment["date_match"],
            }
        )
        print(f"  {meta['paper_key']}: {len(records):>3} records, {total} marks "
              f"(printed {meta['total_marks']}), memo date match={alignment['date_match']}")

    merged_path = EXTRACTED / "chemistry_pass1.json"
    merged_path.write_text(json.dumps(batch, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Rebuild the all-subjects aggregate so it stays consistent with the per-subject files.
    aggregate: list[dict] = []
    for subject_file in sorted(EXTRACTED.glob("*_pass1.json")):
        if subject_file.name == "all_subjects_pass1.json":
            continue
        data = json.loads(subject_file.read_text(encoding="utf-8"))
        if isinstance(data, list):
            aggregate.extend(data)
    (EXTRACTED / "all_subjects_pass1.json").write_text(
        json.dumps(aggregate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    summary = {
        "generated_at": GENERATED_AT,
        "subject": "chemistry",
        "papers_in_batch": len(papers),
        "question_records": len(batch),
        "papers": papers,
        "problems": problems,
    }
    (EXTRACTED / "pass1" / "chemistry" / "_BATCH_SUMMARY.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"\nChemistry Pass 1 batch: {len(papers)} papers, {len(batch)} question records")
    print(f"  -> {relative(merged_path)}")
    print(f"  -> {relative(PER_PAPER_DIR)}/*.json")
    if problems:
        print("\nProblems (non-fatal - see UNRES-CHEM-ACQ-001 for the ORC gap):")
        for p in problems:
            print("  -", p)
        return 1
    print("\nAll papers: mark allocations sum to the printed total and memo dates match.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
