#!/usr/bin/env python3
"""Phase 3b — Ingest locally supplied source files into the preserved corpus.

Sandbox code has no outbound TLS, so the documents selected by
``scripts/phase3_select.py`` are supplied by a human from the ORC and dropped
into a local directory. This runner turns that drop into a preserved, hashed,
schema-valid corpus.

For every expected document in ``data/raw/CORPUS_SELECTION.yaml`` it:

1. looks for a matching file in the drop directory, by Drive file ID first and
   then by normalised filename
2. copies it (never moves) into ``data/raw/<subject>/<role>/``
3. computes SHA-256 of the **original bytes** -> fidelity Rung A
   (``SYSTEM_SPEC.md`` §17.2)
4. probes the content to verify ``document_type`` from the text rather than
   trusting the Phase 2 label, and to flag diagram-bearing documents
5. detects duplicates **by content hash**, not by Drive file ID
6. updates only the four mutable fields on the matching source record in the
   Phase 2 inventory (``access_status``, ``local_path``, ``file_hash``,
   ``notes``) - ``source_metadata.schema.json`` sets ``additionalProperties:
   false``, so nothing else may be written
7. validates every mutated record against that schema
8. writes ``data/raw/<subject>/ACQUISITION_REPORT.yaml``, the run log and
   review-queue items

Nothing is invented. An expected document that is not present in the drop
directory stays ``inaccessible`` and is reported as unresolved.

Usage
-----
    python3 scripts/phase3_ingest_drop.py --dry-run
    python3 scripts/phase3_ingest_drop.py
    python3 scripts/phase3_ingest_drop.py --drop-dir ~/Downloads/orc
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from core import yamllite  # noqa: E402
from core.config import Config  # noqa: E402
from ingestion.acquisition.content_probe import probe  # noqa: E402
from ingestion.acquisition.inventory import drive_file_id  # noqa: E402
from ingestion.run_context import RunContext  # noqa: E402

PHASE = "3-acquisition"
SUBJECTS = ("biology", "physics", "history", "english", "ap_mathematics", "mathematics")
SELECTION_PATH = REPO_ROOT / "data" / "raw" / "CORPUS_SELECTION.yaml"
DEFAULT_DROP_DIR = REPO_ROOT / "data" / "incoming"
ROLE_DIR = {
    "paper": "papers",
    "memo": "memoranda",
    "companion": "companions",
    "anchor": "curriculum",
}
MUTABLE_FIELDS = ("access_status", "local_path", "file_hash", "notes")


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _normalize(name: str) -> str:
    name = re.sub(r"(?i)\.(pdf|docx?|odt|rtf|pages|gdoc|zip)$", "", name)
    name = re.sub(r"[^a-z0-9]+", "", name.lower())
    return name


def expected_documents(selection: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Flatten the selection into the list of documents to acquire."""
    out: List[Dict[str, Any]] = []
    for subject in SUBJECTS:
        block = selection["subjects"][subject]
        for paper in block.get("papers") or []:
            out.append(
                {
                    "subject": subject,
                    "role": "paper",
                    "source_id": paper.get("source_id"),
                    "title": paper.get("title"),
                    "year": paper.get("year"),
                    "source_url": paper.get("source_url"),
                    "drive_file_id": paper.get("drive_file_id"),
                    "stratum": paper.get("stratum"),
                    "flags": list(paper.get("flags") or []),
                }
            )
            memo = paper.get("memo") or {}
            if memo.get("source_id"):
                out.append(
                    {
                        "subject": subject,
                        "role": "memo",
                        "source_id": memo.get("source_id"),
                        "title": memo.get("title"),
                        "year": paper.get("year"),
                        "source_url": memo.get("source_url"),
                        "drive_file_id": drive_file_id(memo.get("source_url")),
                        "paired_with": paper.get("source_id"),
                        "pair_method": memo.get("pair_method"),
                        "pair_confidence": memo.get("pair_confidence"),
                    }
                )
            for companion in paper.get("companions") or []:
                out.append(
                    {
                        "subject": subject,
                        "role": "companion",
                        "source_id": companion.get("source_id"),
                        "title": companion.get("title"),
                        "year": companion.get("year"),
                        "source_url": companion.get("source_url"),
                        "drive_file_id": companion.get("drive_file_id"),
                        "paired_with": paper.get("source_id"),
                    }
                )
        for anchor in block.get("curriculum_anchors") or []:
            out.append(
                {
                    "subject": subject,
                    "role": "anchor",
                    "source_id": anchor.get("source_id"),
                    "title": anchor.get("title"),
                    "year": anchor.get("year"),
                    "source_url": anchor.get("source_url"),
                    "drive_file_id": anchor.get("drive_file_id"),
                }
            )
    return out


def index_drop_dir(drop_dir: Path) -> Dict[str, Dict[str, List[Path]]]:
    """Index every candidate file in the drop directory, by ID and by name."""
    by_id: Dict[str, List[Path]] = {}
    by_name: Dict[str, List[Path]] = {}
    if drop_dir.exists():
        for path in sorted(drop_dir.rglob("*")):
            if not path.is_file() or path.name.startswith("."):
                continue
            # A human may keep the Drive ID in the filename; match on it first
            # because it is exact, unlike any title normalisation.
            for match in re.finditer(r"[A-Za-z0-9_-]{25,}", path.name):
                by_id.setdefault(match.group(0), []).append(path)
            by_name.setdefault(_normalize(path.name), []).append(path)
    return {"by_id": by_id, "by_name": by_name}


def find_match(expected: Dict[str, Any], index: Dict[str, Any]) -> Optional[Path]:
    """Locate the dropped file for one expected document."""
    by_id = index["by_id"]
    by_name = index["by_name"]
    file_id = expected.get("drive_file_id")
    if file_id and file_id in by_id:
        return by_id[file_id][0]
    title = expected.get("title") or ""
    for candidate in (_normalize(title), _normalize(re.sub(r"\s+", " ", title))):
        if candidate and candidate in by_name:
            return by_name[candidate][0]
    # Partial: the drop filename may carry a Drive prefix or a suffix the ORC
    # title lacks. Require a unique containment match to avoid mis-filing.
    norm = _normalize(title)
    if norm:
        hits = [p for key, paths in by_name.items() if norm in key or key in norm for p in paths]
        if len(hits) == 1:
            return hits[0]
    return None


def update_inventory_record(
    inventory_path: Path,
    source_id: str,
    values: Dict[str, str],
) -> bool:
    """Surgically rewrite the four mutable fields of one source record.

    The Phase 2 inventories are provenance and are otherwise never touched.
    Only the block belonging to ``source_id`` is modified.
    """
    text = inventory_path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"(^- source_id: {re.escape(source_id)}\n(?:^  (?!- source_id:).*\n)*)",
        re.M,
    )
    match = pattern.search(text)
    if not match:
        return False
    block = match.group(1)
    updated = block
    for field_name, new_value in values.items():
        if field_name not in MUTABLE_FIELDS:
            raise ValueError(f"{field_name} is not a mutable source-record field")
        rendered = "null" if new_value is None else f"'{str(new_value).replace(chr(39), chr(39)*2)}'"
        field_re = re.compile(rf"^  {field_name}:.*(?:\n^    .*)*$", re.M)
        if field_re.search(updated):
            updated = field_re.sub(f"  {field_name}: {rendered}", updated, count=1)
        else:
            updated = updated.rstrip("\n") + f"\n  {field_name}: {rendered}\n"
    if updated == block:
        return False
    inventory_path.write_text(text[: match.start()] + updated + text[match.end():], encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--drop-dir",
        type=Path,
        default=DEFAULT_DROP_DIR,
        help="directory holding the downloaded ORC files (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report matching without copying, hashing or editing inventories",
    )
    parser.add_argument("--subject", choices=SUBJECTS, help="limit to one subject")
    parser.add_argument("--no-run-log", action="store_true")
    args = parser.parse_args()

    if not SELECTION_PATH.exists():
        print(
            f"ERROR: {SELECTION_PATH} not found. Run scripts/phase3_select.py first.",
            file=sys.stderr,
        )
        return 2

    selection = yamllite.load(SELECTION_PATH)
    expected = expected_documents(selection)
    if args.subject:
        expected = [e for e in expected if e["subject"] == args.subject]

    drop_dir: Path = args.drop_dir
    index = index_drop_dir(drop_dir)
    dropped = sum(len(v) for v in index["by_name"].values())

    print(f"selection: {len(expected)} documents expected")
    print(f"drop dir : {drop_dir} ({dropped} file(s) indexed)")
    if not drop_dir.exists():
        print(
            f"\nThe drop directory does not exist yet. Create it and put the "
            f"files from data/raw/DOWNLOAD_CHECKLIST.md there:\n  mkdir -p {drop_dir}"
        )

    config = Config.load()
    schema_name = config.schema["source_metadata"]
    ctx: Optional[RunContext] = None
    if not args.no_run_log:
        ctx = RunContext(config=config, phase=PHASE, subject=args.subject or "all")
        ctx.start()
        ctx.log_event(
            "acquisition_started",
            message=f"ingesting locally supplied files from {drop_dir}",
            metadata={"expected_documents": len(expected), "dry_run": args.dry_run},
        )

    acquired: List[Dict[str, Any]] = []
    missing: List[Dict[str, Any]] = []
    duplicates: List[Dict[str, Any]] = []
    type_mismatches: List[Dict[str, Any]] = []
    hash_seen: Dict[str, str] = {}
    validation_failures: List[str] = []

    for item in expected:
        match = find_match(item, index) if dropped else None
        if match is None:
            missing.append(item)
            continue

        role_dir = ROLE_DIR[item["role"]]
        destination_dir = REPO_ROOT / "data" / "raw" / item["subject"] / role_dir
        destination = destination_dir / match.name

        if args.dry_run:
            print(f"  [dry-run] {item['subject']}/{role_dir}/{match.name}  <- {item['title']}")
            acquired.append({**item, "local_path": str(destination.relative_to(REPO_ROOT)),
                             "matched_file": str(match), "dry_run": True})
            continue

        destination_dir.mkdir(parents=True, exist_ok=True)
        if destination.exists() and _sha256(destination) != _sha256(match):
            # Never silently overwrite a preserved source.
            suffix = 1
            while destination.with_name(f"{destination.stem}__{suffix}{destination.suffix}").exists():
                suffix += 1
            destination = destination.with_name(f"{destination.stem}__{suffix}{destination.suffix}")
        shutil.copy2(match, destination)

        file_hash = _sha256(destination)
        relative = str(destination.relative_to(REPO_ROOT))
        result = probe(destination)

        duplicate_of = hash_seen.get(file_hash)
        if duplicate_of:
            duplicates.append(
                {"title": item["title"], "local_path": relative, "duplicate_of": duplicate_of,
                 "file_hash": file_hash}
            )
        else:
            hash_seen[file_hash] = relative

        expected_type = "past_paper" if item["role"] == "paper" else (
            "memorandum" if item["role"] == "memo" else None
        )
        if (
            expected_type
            and result.document_type
            and result.document_type != expected_type
        ):
            type_mismatches.append(
                {
                    "source_id": item["source_id"],
                    "title": item["title"],
                    "phase2_document_type": expected_type,
                    "content_document_type": result.document_type,
                    "confidence": result.document_type_confidence,
                    "local_path": relative,
                }
            )

        notes = (
            f"Phase 3b acquisition {_utcnow()}: original bytes preserved at "
            f"fidelity rung A (SYSTEM_SPEC 17.2); SHA-256 of the original file. "
            f"Content probe: format={result.detected_format}, "
            f"document_type={result.document_type} "
            f"({result.document_type_confidence}), "
            f"visual_dependency={result.visual_dependency}."
        )
        if result.error:
            notes += f" Extraction note: {result.error}."
        if duplicate_of:
            notes += f" CONTENT DUPLICATE of {duplicate_of}."

        updated = update_inventory_record(
            REPO_ROOT / "data" / "raw" / item["subject"] / "SOURCE_INVENTORY.yaml",
            item["source_id"],
            {
                "access_status": "accessible",
                "local_path": relative,
                "file_hash": file_hash,
                "notes": notes,
            },
        ) if item.get("source_id") else False

        if updated and ctx is not None:
            record = {
                "source_id": item["source_id"],
                "subject": item["subject"],
                "grade": "11",
                "document_type": result.document_type or expected_type or "other",
                "title": item["title"],
                "year": item.get("year"),
                "term": None,
                "paper_number": None,
                "source_url": item.get("source_url"),
                "retrieved_at": _utcnow(),
                "access_status": "accessible",
                "local_path": relative,
                "file_hash": file_hash,
                "notes": notes,
            }
            result_check = ctx.validate(schema_name, record)
            if not result_check.valid:
                validation_failures.append(
                    f"{item['source_id']}: " + "; ".join(result_check.errors[:3])
                )

        acquired.append(
            {
                **item,
                "local_path": relative,
                "matched_file": str(match),
                "file_hash": file_hash,
                "fidelity_rung": "A",
                "content_probe": result.to_dict(),
                "inventory_updated": updated,
                "duplicate_of": duplicate_of,
            }
        )

    # ---- reports -----------------------------------------------------------
    per_subject: Dict[str, Dict[str, Any]] = {}
    for item in acquired:
        bucket = per_subject.setdefault(
            item["subject"], {"acquired": 0, "missing": 0, "duplicates": 0, "documents": []}
        )
        bucket["acquired"] += 1
        bucket["documents"].append(
            {
                "role": item["role"],
                "source_id": item.get("source_id"),
                "title": item.get("title"),
                "local_path": item.get("local_path"),
                "file_hash": item.get("file_hash"),
                "fidelity_rung": item.get("fidelity_rung", "A"),
                "document_type_verified": (item.get("content_probe") or {}).get("document_type"),
                "requires_visual_verification": bool(
                    (item.get("content_probe") or {}).get("visual_dependency")
                ),
            }
        )
    for item in missing:
        per_subject.setdefault(
            item["subject"], {"acquired": 0, "missing": 0, "duplicates": 0, "documents": []}
        )["missing"] += 1
    for dup in duplicates:
        for subject, bucket in per_subject.items():
            if any(d["local_path"] == dup["local_path"] for d in bucket["documents"]):
                bucket["duplicates"] += 1

    if not args.dry_run:
        for subject, bucket in per_subject.items():
            report = {
                "report_id": f"ACQ-REPORT-{subject.upper()}",
                "phase": PHASE,
                "subject": subject,
                "generated_at": _utcnow(),
                "selection_id": selection.get("selection_id"),
                "acquisition_mode": "local_drop",
                "drop_dir": str(drop_dir),
                "fidelity_rung": "A",
                "expected": bucket["acquired"] + bucket["missing"],
                "acquired": bucket["acquired"],
                "missing": bucket["missing"],
                "content_duplicates": bucket["duplicates"],
                "documents": bucket["documents"],
                "unresolved": [
                    {"title": m["title"], "role": m["role"], "source_id": m.get("source_id"),
                     "reason": "not present in the drop directory"}
                    for m in missing if m["subject"] == subject
                ],
            }
            path = REPO_ROOT / "data" / "raw" / subject / "ACQUISITION_REPORT.yaml"
            path.write_text(yamllite.dumps(report), encoding="utf-8")
            if ctx:
                ctx.record_artifact(path, type="yaml", description=f"{subject} acquisition report")

    print(f"\nacquired={len(acquired)} missing={len(missing)} "
          f"duplicates={len(duplicates)} type_mismatches={len(type_mismatches)}")
    if type_mismatches:
        print("\nPhase 2 document_type contradicted by content:")
        for m in type_mismatches:
            print(f"  - {m['subject']}: '{m['title']}' labelled {m['phase2_document_type']}, "
                  f"content is {m['content_document_type']} ({m['confidence']})")
    if duplicates:
        print("\nContent duplicates (distinct source records, identical bytes):")
        for d in duplicates:
            print(f"  - {d['local_path']} == {d['duplicate_of']}")
    if missing:
        print(f"\n{len(missing)} expected document(s) not found in the drop directory:")
        for m in missing[:20]:
            print(f"  - {m['subject']}/{m['role']}: {m['title']}")
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more")
    if validation_failures:
        print("\nSchema validation failures:")
        for failure in validation_failures:
            print(f"  - {failure}")

    if ctx is not None:
        ctx.log_decision(
            decision_id="DEC-P3B-001",
            decision_type="acquisition_mode",
            context=(
                "Sandbox code has no outbound TLS to any host, so Phase 3 cannot "
                "download from Google Drive. The selected documents are supplied "
                "by a human and ingested from a local drop directory."
            ),
            evidence=[
                "curl to example.com fails with SSL_ERROR_SYSCALL, confirming the "
                "restriction is not specific to Google",
                "the platform's proxied fetcher CAN reach the ORC, but returns "
                "transcribed text rather than original bytes (fidelity Rung B)",
                "the saturation sample is 61 documents, which is small enough to "
                "supply by hand - the scope reduction is what makes Rung A "
                "achievable",
            ],
            alternatives=[
                "accept Rung B transcriptions for everything",
                "wait for an environment with working Drive access",
                "ingest human-supplied originals (Rung A)",
            ],
            selected="ingest human-supplied originals (Rung A)",
            rationale=(
                "Rung A is the only mode that preserves original bytes and "
                "diagrams, and the reduced corpus makes it practical. Rung B "
                "remains available as a fallback for individual documents."
            ),
            confidence="high",
            requires_review=False,
        )
        for mismatch in type_mismatches:
            ctx.log_error(
                subject=mismatch["subject"],
                error_type="metadata_contradicted_by_content",
                message=(
                    f"'{mismatch['title']}' is labelled {mismatch['phase2_document_type']} "
                    f"in the Phase 2 inventory but its content is "
                    f"{mismatch['content_document_type']} "
                    f"({mismatch['confidence']} confidence)"
                ),
                affected_artifact=mismatch["local_path"],
                status="unresolved",
            )
        for dup in duplicates:
            ctx.log_error(
                error_type="content_duplicate",
                message=(
                    f"{dup['local_path']} is byte-identical to {dup['duplicate_of']} "
                    "despite being a distinct source record"
                ),
                affected_artifact=dup["local_path"],
                status="unresolved",
            )
        for failure in validation_failures:
            ctx.log_error(error_type="schema_validation", message=failure, status="unresolved")
        ctx.set_metrics(
            {
                "expected_documents": len(expected),
                "acquired": len(acquired),
                "missing": len(missing),
                "content_duplicates": len(duplicates),
                "document_type_mismatches": len(type_mismatches),
                "schema_validation_failures": len(validation_failures),
                "fidelity_rung": "A",
                "dry_run": args.dry_run,
            }
        )
        if missing:
            ctx.log_error(
                error_type="incomplete_drop",
                message=(
                    f"{len(missing)} of {len(expected)} selected documents were not "
                    "present in the drop directory"
                ),
                status="unresolved",
            )
        status = "completed" if not missing and not validation_failures else "completed_with_review"
        if not acquired and not args.dry_run:
            status = "blocked"
        ctx.complete(status, unresolved_items=len(missing) + len(validation_failures))
        print(f"\nrun logged: {ctx.logger.run_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
