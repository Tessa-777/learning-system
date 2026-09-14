#!/usr/bin/env python3
"""Build the English Pass 1 evidence batch from the authored evidence tables.

Mirrors ``scripts/build_physics_pass1.py`` (the reference implementation) but for
a subject whose sources are mostly ``.docx`` and whose marking is rubric-based:

* computes SHA-256 for every paper and memorandum (provenance, §14);
* verifies each paper<->memo pairing from PRINTED evidence — the header block
  (DATE / MARKS / EXAMINER) where it is printed, plus the numbered content and
  the printed mark totals where a memorandum carries no header at all. The
  inherited ``data/organized/sample_manifest.json`` pairing is never consulted;
* verifies, per record, that the paper really prints that question number with
  that bracketed mark, and that a memorandum which carries marking evidence
  prints the same item with the same bracketed mark;
* verifies every printed section total against the paper's cover table or its
  printed section headers, and fails on any mark-sum mismatch that the paper
  itself does not contain (declared and evidenced page-level exceptions only);
* resolves ``orc_source_id`` / ``orc_memo_source_id`` from
  ``data/raw/english/SOURCE_INVENTORY.yaml`` by title and fails if absent or
  ambiguous;
* writes nothing unless every check passed (fail closed).

Run from the repository root:  python scripts/build_english_pass1.py
"""
from __future__ import annotations

import importlib
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.runlog import sha256_file  # noqa: E402

EXTRACTED = ROOT / "data" / "extracted"
PER_PAPER_DIR = EXTRACTED / "pass1" / "english"
INVENTORY = ROOT / "data" / "raw" / "english" / "SOURCE_INVENTORY.yaml"

EVIDENCE_MODULES = [
    "english_pass1_evidence_2014_p2",
    "english_pass1_evidence_2015_p2",
    "english_pass1_evidence_2016_nov",
    "english_pass1_evidence_2017_nov",
    "english_pass1_evidence_2018_jul",
]

GENERATED_AT = datetime.now(timezone.utc).isoformat(timespec="seconds")

# The English prompt asks each question record to state which paper type its
# competence belongs to. Journalism-style sections stay Language; poetry and
# set-work sections are Literature; essay and transactional tasks are Writing.
PAPER_TYPES = {
    "Comprehension": "Language",
    "Summary": "Language",
    "Language Structures & Conventions": "Language",
    "Visual Literacy": "Language",
    "Poetry (Seen)": "Literature",
    "Poetry (Unseen)": "Literature",
    "Novel": "Literature",
    "Drama": "Literature",
    "Short Stories": "Literature",
    "Essay Writing": "Writing",
    "Transactional Writing": "Writing",
}


# --------------------------------------------------------------------------- text


def docx_text(path: Path) -> str:
    """Read a .docx without new dependencies (the prompt's zipfile+regex recipe)."""
    try:
        xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf8", "ignore")
    except Exception:  # noqa: BLE001 - unreadable sources are recorded, never guessed
        return ""
    return re.sub(r"<[^>]+>", "", re.sub(r"</w:p>", "\n", xml))


def pdf_text(path: Path) -> str:
    """Extract the text layer of a PDF (returns '' if there is none)."""
    try:
        from pypdf import PdfReader
    except ImportError:  # pragma: no cover - dependency guard
        return ""
    try:
        reader = PdfReader(str(path))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    except Exception:  # noqa: BLE001 - unreadable PDFs are recorded, not fatal
        return ""


def document_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return docx_text(path)
    if suffix == ".pdf":
        return pdf_text(path)
    raise ValueError(f"Unsupported document type: {path.name}")


def flatten(text: str) -> str:
    """Collapse all whitespace so header fields and item marks can be located."""
    return re.sub(r"\s+", " ", text).strip()


# ------------------------------------------------------------------ header checks

DATE_RE = r"((?:\d{1,2}\s+)?[A-Za-z]{3,9}\s*,?\s*\d{4})"


def header_fields(text: str, limit: int = 2200) -> dict:
    """Pull the DATE / MARKS / EXAMINER block out of a paper or memorandum.

    Raises ValueError when a field is not printed — the caller decides whether
    the document is a header-less memorandum (declared in the evidence module)
    or an unverifiable pairing.
    """
    head = flatten(text[:limit])

    def need(pattern: str, name: str) -> str:
        match = re.search(pattern, head)
        if not match:
            raise ValueError(f"Missing printed header field: {name}")
        return re.sub(r"\s+", " ", match.group(1)).strip(" ,;")

    date = need(r"DATE\s*:?\s*" + DATE_RE, "DATE")
    marks = need(r"\bMARKS\s*:?\s*(\d{1,3})", "MARKS")
    examiner = need(r"EXAMINERS?\s*:?\s*(.+?)\s*(?:MODERATOR|MARKS|NAME|CLASS|DURATION|\d{1,2}\s*%)", "EXAMINER")
    return {"date": date, "marks": int(marks), "examiner": examiner}


def parse_cover_table(text: str, meta: dict) -> dict:
    """Parse the paper's printed 'Possible Marks' cover row.

    Returns {'printed_numbers': [...], 'total': int}. Raises when the paper has
    no machine-readable cover table, unless the module declares its absence.
    """
    flat = flatten(text[:6000])
    match = re.search(r"Possible\s*Marks\s+((?:\d{1,3}\s+)+)", flat)
    if not match:
        if not meta.get("cover_table_absent_reason"):
            raise ValueError(f"{meta['paper_key']}: no printed 'Possible Marks' row found")
        return {"printed_numbers": [], "total": None, "basis": "absent: " + meta["cover_table_absent_reason"]}
    numbers = [int(n) for n in match.group(1).split()]
    if len(numbers) < 2:
        raise ValueError(f"{meta['paper_key']}: cover table unreadable ({match.group(1)!r})")
    return {"printed_numbers": numbers[:-1], "total": numbers[-1], "basis": "printed 'Possible Marks' row"}


def check_cover_table(meta: dict, cover: dict) -> None:
    """Verify the printed cover row against the authored section totals."""
    section_totals = meta["section_totals"]
    if not cover["printed_numbers"]:
        return
    groups = meta.get("cover_table_groups")
    if groups is None:
        flattened = list(section_totals.values())
    else:
        flattened = [n for key in groups for n in groups[key]]
        if {frozenset(key.split(":")) for key in groups} != {
            frozenset([k]) for k in section_totals
        }:
            raise ValueError(f"{meta['paper_key']}: cover_table_groups do not cover section_totals")
    if cover["printed_numbers"] != flattened:
        raise ValueError(
            f"{meta['paper_key']}: printed cover row {cover['printed_numbers']} != authored section totals {flattened}"
        )
    if cover["total"] != sum(section_totals.values()):
        raise ValueError(
            f"{meta['paper_key']}: printed cover total {cover['total']} != sum of section totals "
            f"{sum(section_totals.values())}"
        )
    if cover["total"] != meta["total_marks"]:
        raise ValueError(f"{meta['paper_key']}: printed cover total {cover['total']} != header MARKS {meta['total_marks']}")


def check_section_headers(text: str, meta: dict, anchors_key: str, label: str) -> None:
    """Verify the printed section-header anchors (marks per section) literally exist."""
    flat = flatten(text)
    for anchor in meta.get(anchors_key, []):
        if flatten(anchor) not in flat:
            raise ValueError(f"{meta['paper_key']}: {label} does not print section anchor {anchor!r}")


def verify_alignment(paper_path: Path, memo_path: Path, meta: dict) -> dict:
    """Verify a paper<->memo pairing from printed evidence. Raises on failure."""
    paper_text, memo_text = document_text(paper_path), document_text(memo_path)
    if not flatten(paper_text):
        raise ValueError(f"{meta['paper_key']}: paper has no readable text layer")

    basis = meta.get("pairing_basis", "printed_header")
    if basis == "printed_header":
        paper_head = header_fields(paper_text)
        memo_head = header_fields(memo_text)
        for field in ("date", "marks", "examiner"):
            if paper_head[field] != memo_head[field]:
                raise ValueError(
                    f"{meta['paper_key']}: paper/memo {field.upper()} mismatch "
                    f"({paper_head[field]!r} vs {memo_head[field]!r})"
                )
        if paper_head["date"] != meta["exam_date"]:
            raise ValueError(f"{meta['paper_key']}: authored exam_date disagrees with printed DATE {paper_head['date']!r}")
        if paper_head["marks"] != meta["total_marks"]:
            raise ValueError(f"{meta['paper_key']}: printed MARKS {paper_head['marks']} != authored {meta['total_marks']}")
        if flatten(meta["examiner"]).lower() not in flatten(paper_head["examiner"]).lower():
            raise ValueError(
                f"{meta['paper_key']}: authored examiner {meta['examiner']!r} not in printed {paper_head['examiner']!r}"
            )
    elif basis == "content_and_printed_totals":
        # A memorandum that carries no header block at all may still be paired on
        # numbered content plus printed totals. The absence must be proven, not assumed.
        try:
            header_fields(memo_text)
        except ValueError:
            pass
        else:
            raise ValueError(
                f"{meta['paper_key']}: pairing declared as content-based but the memorandum prints a header"
            )
        if not meta.get("pairing_anchors") or not meta.get("pairing_note"):
            raise ValueError(f"{meta['paper_key']}: content pairing requires anchors and a note")
        paper_head = header_fields(paper_text)
        memo_head = {}
        if paper_head["date"] != meta["exam_date"]:
            raise ValueError(f"{meta['paper_key']}: authored exam_date disagrees with printed DATE {paper_head['date']!r}")
        if paper_head["marks"] != meta["total_marks"]:
            raise ValueError(f"{meta['paper_key']}: printed MARKS {paper_head['marks']} != authored {meta['total_marks']}")
        if flatten(meta["examiner"]).lower() not in flatten(paper_head["examiner"]).lower():
            raise ValueError(
                f"{meta['paper_key']}: authored examiner {meta['examiner']!r} not in printed {paper_head['examiner']!r}"
            )
    else:  # pragma: no cover - guard against a typo in an evidence module
        raise ValueError(f"{meta['paper_key']}: unknown pairing_basis {basis!r}")

    for anchor in meta.get("pairing_anchors", []):
        if flatten(anchor) not in flatten(paper_text):
            raise ValueError(f"{meta['paper_key']}: pairing anchor absent from paper: {anchor!r}")
        if flatten(anchor) not in flatten(memo_text):
            raise ValueError(f"{meta['paper_key']}: pairing anchor absent from memorandum: {anchor!r}")

    check_section_headers(paper_text, meta, "section_anchors", "paper")
    check_section_headers(memo_text, meta, "memo_section_anchors", "memorandum")
    for anchor in meta.get("memo_section_anchors_absent", []):
        if flatten(anchor) in flatten(memo_text):
            raise ValueError(
                f"{meta['paper_key']}: memorandum was recorded as lacking {anchor!r} but prints it"
            )
    cover = parse_cover_table(paper_text, meta)
    check_cover_table(meta, cover)
    return {
        "pairing_basis": basis,
        "pairing_note": meta.get("pairing_note"),
        "paper_header": paper_head if basis == "printed_header" else header_fields(paper_text),
        "memo_header": memo_head,
        "date_match": True,
        "marks_match": True,
        "examiner_match": basis == "printed_header",
        "cover_table": cover,
        "verified_by": (
            "printed DATE/MARKS/EXAMINER in both documents, printed section headers, "
            "cover-table totals, and per-item printed marks"
            if basis == "printed_header"
            else "numbered-content anchors in both documents plus printed Q1 total (memo prints no header)"
        ),
    }


# --------------------------------------------------------------- record checks


def item_anchor_missing(text: str, printed_qn: str, marks: int, style: str = "parenthesised") -> bool:
    """True if the document does not print that question number with that mark.

    Two printed styles occur in this subject's documents: marks in brackets
    ('1.4 Explain ... (3)') and marks trailing the question as a bare number
    ('1.4Account for ...mind.3'), the latter used by the 2014 Paper 2 and its
    memorandum. The style is declared per paper in its evidence module so the
    check stays literal instead of permissive.
    """
    flat = flatten(text)
    pattern = re.compile(r"(?<![\d.])" + re.escape(printed_qn) + r"(?![\d])")
    for match in pattern.finditer(flat):
        window = flat[match.start(): match.start() + 900]
        if style == "parenthesised":
            if re.search(r"\(\s*" + str(marks) + r"\s*\)", window):
                return False
        else:
            trailing = re.search(
                r"[.?!:][\"”’')]*\s*" + str(marks) + r"(?![\d])",
                window,
            )
            next_item = re.search(str(marks) + r"(?=\s*\d{1,2}\.\d{1,2})", window)
            if trailing or next_item:
                return False
    return True


def check_items(meta: dict, vals: list[dict], paper_text: str, memo_text: str) -> dict:
    """Verify every transcribed item against the printed paper and memorandum."""
    overrides = meta.get("printed_numbering", {})
    anchors = meta.get("item_anchor_overrides", {})
    memo_overrides = meta.get("memo_numbering_overrides", {})
    style = meta.get("marks_style", "parenthesised")
    missing_paper, missing_memo, restated = [], [], []
    for v in vals:
        qn = v["qn"]
        suffix = qn.split(".", 1)[1] if "." in qn else qn
        prefix = overrides.get(v["top_level_question_number"], {}).get("printed_prefix")
        printed_qn = prefix + "." + suffix if prefix else qn
        if printed_qn != qn:
            v["printed_question_number"] = printed_qn
        else:
            v["printed_question_number"] = qn
        anchor = anchors.get(qn)
        if anchor:
            if flatten(anchor["paper"]) not in flatten(paper_text):
                missing_paper.append(f"{qn}({v['marks']}) anchor")
            if v["memo_evidence"] in {"model_answer", "rubric_reference"}:
                memo_anchor = anchor.get("memo")
                if not memo_anchor:
                    raise ValueError(
                        f"{meta['paper_key']}: {qn} claims marking evidence but its anchor override "
                        "declares no memorandum text"
                    )
                if flatten(memo_anchor) not in flatten(memo_text):
                    missing_memo.append(f"{qn}({v['marks']}) anchor")
        elif item_anchor_missing(paper_text, printed_qn, v["marks"], style):
            missing_paper.append(f"{printed_qn}({v['marks']})")
        memo_qn = memo_overrides.get(printed_qn, printed_qn)
        if not anchor and v["memo_evidence"] in {"model_answer", "rubric_reference"}:
            if item_anchor_missing(memo_text, memo_qn, v["marks"], style):
                missing_memo.append(f"{memo_qn}({v['marks']})")
        elif printed_qn + "(" + str(v["marks"]) + ")" in flatten(memo_text):
            restated.append(f"{printed_qn}({v['marks']})")
    if missing_paper:
        raise ValueError(f"{meta['paper_key']}: paper does not print {len(missing_paper)} item mark(s): {missing_paper[:6]}")
    if missing_memo:
        raise ValueError(
            f"{meta['paper_key']}: memorandum does not print {len(missing_memo)} item mark(s) for records "
            f"claiming marking evidence: {missing_memo[:6]}"
        )
    return {
        "items_verified_against_paper": len(vals),
        "items_verified_against_memo": sum(
            v["memo_evidence"] in {"model_answer", "rubric_reference"} for v in vals
        ),
        "restated_without_model_answer": restated,
    }


def validate_rows(meta: dict, schema: tuple, rows: list[tuple]) -> list[dict]:
    if any(len(r) != len(schema) for r in rows):
        widths = {len(r) for r in rows}
        raise ValueError(f"{meta['paper_key']}: evidence tuple width {widths} != schema {len(schema)}")
    vals = []
    for r in rows:
        v = dict(zip(schema, r))
        v["top_level_question_number"] = v["qn"].split(".")[0]
        vals.append(v)
    if len({v["qn"] for v in vals}) != len(vals):
        raise ValueError(f"{meta['paper_key']}: duplicate question number")
    if any(not isinstance(v["marks"], int) or v["marks"] <= 0 for v in vals):
        raise ValueError(f"{meta['paper_key']}: missing or invalid per-question marks")
    key_map = meta.get("section_key_map")
    section_sum: dict[str, int] = {}
    for v in vals:
        top = v["top_level_question_number"]
        key = (key_map or {}).get(top, top)
        if key not in meta["section_totals"]:
            raise ValueError(f"{meta['paper_key']}: question {v['qn']} has no section total for key {key!r}")
        v["section_key"] = key
        if v["allocation"] == "allocated":
            section_sum[key] = section_sum.get(key, 0) + v["marks"]
        elif v["allocation"] == "alternative":
            if key not in meta.get("alternative_sections", {}):
                raise ValueError(f"{meta['paper_key']}: {v['qn']} marked alternative but its section is not declared as optional")
        else:
            raise ValueError(f"{meta['paper_key']}: unknown allocation role {v['allocation']!r}")

    discrepancies = {d["section"]: d for d in meta.get("mark_discrepancies", [])}
    total_counted = 0
    for key, total in meta["section_totals"].items():
        counted = section_sum.get(key, 0)
        if key in meta.get("alternative_sections", {}):
            spec = meta["alternative_sections"][key]
            options = [v for v in vals if v["section_key"] == key and v["allocation"] == "alternative"]
            if len(options) != spec["options"] or {v["marks"] for v in options} != {spec["marks_each"]}:
                raise ValueError(f"{meta['paper_key']}: optional section {key} does not print {spec['options']} "
                                 f"options of {spec['marks_each']} marks")
            counted += spec["counted"] * spec["marks_each"]
        total_counted += counted
        if counted == total:
            continue
        declared = discrepancies.get(key)
        if not declared or (declared["printed_section_total"], declared["sum_of_printed_item_marks"]) != (total, counted):
            raise ValueError(
                f"{meta['paper_key']}: section {key} item marks {counted} != printed section total {total} "
                f"and no matching declared source discrepancy exists"
            )
    total_printed = sum(
        meta["section_totals"][k] for k in meta["section_totals"]
    ) - sum(d["printed_section_total"] - d["sum_of_printed_item_marks"] for d in discrepancies.values())
    if total_counted != total_printed:
        raise ValueError(
            f"{meta['paper_key']}: total counted marks {total_counted} != {total_printed} "
            f"(section totals less declared source shortfalls)"
        )
    if sum(meta["section_totals"].values()) != meta["total_marks"]:
        raise ValueError(f"{meta['paper_key']}: printed section totals do not sum to header MARKS")
    return vals


def source_id_for(meta: dict, qn: str) -> str:
    return "english_{year}_{board}_{ptype}_{period}_q{qn}".format(
        year=meta["year"], board=meta["exam_board"], ptype=meta["paper_type"],
        period=meta["exam_period"], qn=qn,
    )


def orc_index() -> dict:
    import yaml

    data = yaml.safe_load(INVENTORY.read_text(encoding="utf-8"))

    def norm(name: str) -> str:
        return re.sub(r"\s+", " ", str(name)).strip().lower()

    index: dict[tuple[str, str], set[str]] = {}
    for record in data.get("sources", []):
        title = record.get("title") or ""
        for candidate in {title, Path(title).stem}:
            if candidate:
                index.setdefault((norm(candidate), str(record.get("year"))), set()).add(record["source_id"])
    return index


def build_records(meta: dict, vals: list[dict], alignment: dict, hashes: dict, orc: list[str], module_name: str) -> list[dict]:
    stems = getattr(importlib.import_module("ingestion.extraction." + module_name), "STEMS", {})
    existing = {v["qn"] for v in vals}
    records = []
    for v in vals:
        qn = v["qn"]
        parent = None
        if "." in qn:
            candidate = qn.rsplit(".", 1)[0]
            while candidate:
                if candidate in existing:
                    parent = meta["paper_key"] + "-Q" + candidate
                    break
                candidate = candidate.rsplit(".", 1)[0] if "." in candidate else ""
        records.append({
            "source_id": source_id_for(meta, qn),
            "question_id": meta["paper_key"] + "-Q" + qn,
            "subject": "english",
            "grade": "11",
            "paper_key": meta["paper_key"],
            "paper_focus": meta["paper_focus"],
            "section_guess": v["section"],
            "paper_type": PAPER_TYPES.get(v["section"], "Language"),
            "paper_number": meta["paper_number"],
            "question_format": v["qformat"],
            "source_document": meta["paper_path"],
            "source_document_sha256": hashes["paper_path"],
            "memo_document": meta["memo_path"],
            "memo_document_sha256": hashes["memo_path"],
            "orc_source_id": orc[0],
            "orc_memo_source_id": orc[1],
            "fidelity_rung": meta["fidelity_rung"],
            "requires_visual_verification": bool(v["needs_visual"]),
            "ocr_uncertain": bool(v["ocr_uncertain"]),
            "question_number": qn,
            "printed_question_number": v["printed_question_number"],
            "top_level_question_number": v["top_level_question_number"],
            "parent_question_id": parent,
            "question_stem_text": stems.get(qn),
            "marks": v["marks"],
            "allocation": v["allocation"],
            "set_text_title": v["set_text"],
            "question_type": v["qformat"],
            "question_text": v["text"],
            "has_visual": bool(v["has_visual"]),
            "memo_evidence": v["memo_evidence"],
            "rubric_reference": bool(v["rubric_ref"]),
            "memo_answer": v["memo_answer"],
            "memo_method_steps": v["memo_steps"],
            "memo_marking_notes": v["memo_notes"],
            "memo_alignment": alignment,
            "extraction": {
                "method": "zipfile (docx) / pypdf (pdf) text layer + manual reading of paper and memorandum",
                "generated_at": GENERATED_AT,
                "evidence_module": module_name,
            },
        })
    return records


def main() -> int:
    try:
        index = orc_index()
        if not index:
            raise ValueError(f"Phase 2 inventory not readable at {INVENTORY}")
        batch: list[dict] = []
        docs: list[dict] = []
        for module_name in EVIDENCE_MODULES:
            module = importlib.import_module("ingestion.extraction." + module_name)
            meta = dict(module.PAPER)
            vals = validate_rows(meta, module.SCHEMA, module.RECORDS)
            paper_path, memo_path = ROOT / meta["paper_path"], ROOT / meta["memo_path"]
            if not paper_path.exists() or not memo_path.exists():
                raise ValueError(f"{module_name}: missing source file(s)")
            alignment = verify_alignment(paper_path, memo_path, meta)
            hashes = {key: sha256_file(paper_path if key == "paper_path" else memo_path) for key in ("paper_path", "memo_path")}
            if not meta.get("source_hashes"):
                raise ValueError(f"{meta['paper_key']}: no recorded source hashes")
            for key, digest in hashes.items():
                if meta["source_hashes"][key] != digest:
                    raise ValueError(f"{meta['paper_key']}: source changed since transcription: {meta[key]}")
            orc = []
            for key in ("paper_path", "memo_path"):
                name = Path(meta[key]).name
                matches = index.get((re.sub(r"\s+", " ", name).strip().lower(), str(meta["year"]))) or index.get(
                    (re.sub(r"\s+", " ", Path(name).stem).strip().lower(), str(meta["year"]))
                )
                if not matches or len(matches) != 1:
                    raise ValueError(f"{meta['paper_key']}: absent or ambiguous ORC source for {name}")
                orc.append(next(iter(matches)))
            paper_text, memo_text = document_text(paper_path), document_text(memo_path)
            item_report = check_items(meta, vals, paper_text, memo_text)
            records = build_records(meta, vals, alignment, hashes, orc, module_name)
            allocated = sum(r["marks"] for r in records if r["allocation"] == "allocated")
            shortfall = sum(d["printed_section_total"] - d["sum_of_printed_item_marks"] for d in meta.get("mark_discrepancies", []))
            docs.append({
                "paper": meta,
                "memo_alignment_check": alignment,
                "item_verification": item_report,
                "records_extracted": len(records),
                "marks_sum_check": {
                    "sum_of_transcribed_items": allocated,
                    "printed_total": meta["total_marks"],
                    "source_shortfall": shortfall,
                    "match": allocated == meta["total_marks"],
                    "declared_source_discrepancies": meta.get("mark_discrepancies", []),
                },
                "question_records": records,
            })
            batch.extend(records)
            print(f"  {meta['paper_key']}: {len(records):>3} records, {allocated} transcribed marks "
                  f"(header {meta['total_marks']}, source shortfall {shortfall})")
        if len({r["source_id"] for r in batch}) != len(batch):
            raise ValueError("Duplicate source_id in the English batch")
    except (ValueError, KeyError, OSError, ImportError) as exc:
        print(f"English Pass 1 FAILED (no outputs replaced): {exc}", file=sys.stderr)
        return 1

    PER_PAPER_DIR.mkdir(parents=True, exist_ok=True)

    def write(path: Path, obj) -> None:
        path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for doc in docs:
        write(PER_PAPER_DIR / (doc["paper"]["paper_key"] + ".json"), doc)
    write(EXTRACTED / "english_pass1.json", batch)
    aggregate = EXTRACTED / "all_subjects_pass1.json"
    previous = json.loads(aggregate.read_text(encoding="utf-8")) if aggregate.exists() else []
    write(aggregate, [r for r in previous if r.get("subject") != "english"] + batch)
    summary = {
        "subject": "english",
        "papers_in_batch": len(docs),
        "question_records": len(batch),
        "data_bearing_records": sum(r["memo_evidence"] in {"model_answer", "rubric_reference"} for r in batch),
        "records_without_marking_evidence": sum(r["memo_evidence"] in {"none", "restated_only"} for r in batch),
        "records_requiring_visual_verification": sum(bool(r["requires_visual_verification"]) for r in batch),
        "problems": [],
        "papers": [{
            "paper_key": d["paper"]["paper_key"],
            "records": d["records_extracted"],
            "marks": d["paper"]["total_marks"],
            "memo_has_header": bool(d["memo_alignment_check"]["memo_header"]),
            "source_shortfall": d["marks_sum_check"]["source_shortfall"],
        } for d in docs],
    }
    write(PER_PAPER_DIR / "_BATCH_SUMMARY.json", summary)
    print(f"\nEnglish Pass 1: {len(docs)} verified pairs, {len(batch)} question records")
    print(f"  records with marking evidence: {summary['data_bearing_records']}; "
          f"without: {summary['records_without_marking_evidence']}")
    print(f"  -> data/extracted/english_pass1.json and data/extracted/pass1/english/*.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
