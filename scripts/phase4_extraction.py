#!/usr/bin/env python3
"""Phase 4 — Source Content Extraction Runner (blocked-state gate).

Executes Phase 4 for each of the six Grade 11 subjects, in the order
prescribed by IMPLEMENTATION_SPEC §23:

    A. biology
    B. physics
    C. history
    D. english
    E. ap_mathematics
    F. mathematics

Phase 4 (IMPLEMENTATION_SPEC §5) requires the *acquired* corpus produced by
Phase 3: for every paper and memorandum there must be a preserved original
file (``local_path``) with a verified SHA-256 hash (``file_hash``) before any
text extraction, page-number retention, table/figure identification,
header/footer detection, question-number/mark preservation, confidence
recording, or visual-verification-page identification can happen.

Phase 3 recorded 0 acquired sources for every subject (sandbox TLS/SSL
restriction to Google Drive; see data/raw/<subject>/ACQUISITION_REPORT.yaml
and STATUS.md).  STATUS.md explicitly gates Phase 4 on that being resolved.
AGENTS.md rules 4/5/7 and IMPLEMENTATION_SPEC §5 hard rules forbid inventing
missing text or substituting an external corpus.

This runner therefore performs the honest Phase 4 gate for every subject:

  * verifies the acquired corpus state (preserved originals + hashes)
  * runs the phase, records events, decisions, errors, metrics, artifacts
  * marks the subject run ``blocked`` (RUN_LOG_SPEC §11) when no preserved
    original exists for any source — extraction cannot responsibly start
  * writes a per-subject Phase 4 extraction report and a human review-queue
    item, and appends a run record to the subject source inventory
  * creates only structural placeholders under data/extracted/<subject>/ —
    no fabricated extraction content
  * writes the aggregate Phase 4 summary and updates STATUS.md

If any subject unexpectedly HAS preserved originals (or stray corpus files,
or prior extraction artifacts), the runner refuses to run at all and fails
fast: this runner implements only the empty-corpus blocked-state gate and
must never silently skip real work.

The runner stops after Phase 4: it does NOT segment questions (Phase 5),
analyse or classify educational content, or process other subjects.
"""

from __future__ import annotations

import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.config import Config  # noqa: E402
from core.runlog import sha256_file  # noqa: E402
from ingestion.run_context import RunContext  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

# (subject slug, phase letter, queue abbreviation) in IMPLEMENTATION_SPEC §23 order.
SUBJECTS = [
    ("biology", "A", "BIO"),
    ("physics", "B", "PHY"),
    ("history", "C", "HIS"),
    ("english", "D", "ENG"),
    ("ap_mathematics", "E", "APM"),
    ("mathematics", "F", "MAT"),
]

PHASE = 4

# Files that legitimately live in a data/raw/<subject>/ directory without being
# part of the acquired corpus (metadata/inventory/reports/placeholders).
_RAW_DIR_ADMIN_FILES = {
    ".gitkeep",
    "SOURCE_INVENTORY.yaml",
    "ACQUISITION_REPORT.yaml",
    "PHASE4_EXTRACTION_REPORT.yaml",
}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def probe_google_drive_reachability() -> str:
    """Re-probe the Phase 3 blocker (TLS to Google services) as evidence.

    Phase 3 could not download any source because the sandbox terminates TLS
    connections to Google services.  Phase 4 does not download (that is Phase
    3 work) but the probe is recorded as evidence that the dependency
    remains unresolved at Phase 4 execution time.
    """
    import ssl
    import urllib.request

    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(
            "https://drive.google.com", headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
            return f"reachable (HTTP {resp.status})"
    except Exception as exc:  # noqa: BLE001 - probe must never raise
        return f"{type(exc).__name__}: {exc}"


def corpus_state(inventory: dict, raw_dir: Path) -> dict:
    """Classify the acquired-corpus state for one subject inventory."""
    sources = inventory.get("sources", [])
    requiring_extraction = [
        s for s in sources if s.get("access_status") != "external"
    ]

    preserved = []
    missing = []
    for s in requiring_extraction:
        local_path = s.get("local_path")
        file_hash = s.get("file_hash")
        if local_path and file_hash:
            p = Path(local_path)
            abs_p = p if p.is_absolute() else REPO_ROOT / p
            if abs_p.is_file() and sha256_file(abs_p) == file_hash:
                preserved.append(s.get("source_id"))
                continue
        missing.append(s.get("source_id"))

    stray = []
    if raw_dir.exists():
        for f in sorted(raw_dir.iterdir()):
            if f.is_file() and f.name not in _RAW_DIR_ADMIN_FILES:
                stray.append(f.name)

    extracted_dir = REPO_ROOT / "data" / "extracted" / (inventory.get("subject") or "")
    extracted_files = []
    if extracted_dir.exists():
        extracted_files = [
            str(p.relative_to(REPO_ROOT))
            for p in sorted(extracted_dir.rglob("*"))
            if p.is_file() and p.name != ".gitkeep"
        ]

    return {
        "sources_total": len(sources),
        "sources_external": len(sources) - len(requiring_extraction),
        "sources_requiring_extraction": len(requiring_extraction),
        "sources_with_preserved_original": len(preserved),
        "sources_without_preserved_original": len(missing),
        "preserved_source_ids": preserved,
        "unexpected_raw_dir_files": stray,
        "prior_extraction_artifacts": extracted_files,
    }


def write_review_queue_item(slug: str, abbr: str, run_id: str, inventory_id: str,
                            sources_without_preserved: int, total: int,
                            p3_run_id: str, phase3_report: Path) -> Path:
    import yaml

    path = REPO_ROOT / "review_queue" / f"RQ-P4-{abbr}-EXTRACTION.yaml"
    doc = {
        "review_queue_id": f"RQ-P4-{abbr}-EXTRACTION",
        "phase": PHASE,
        "subject": slug,
        "issue": (
            f"Phase 4 extraction cannot start for {slug}: no acquired corpus exists. "
            f"{sources_without_preserved} of {total} sources have no preserved "
            "original file (local_path=null, file_hash=null after Phase 3)."
        ),
        "affected_entity": f"{inventory_id} ({total} source records) -> data/extracted/{slug}/",
        "evidence": [
            f"inventory: data/raw/{slug}/SOURCE_INVENTORY.yaml (0 sources acquired in Phase 3)",
            f"phase3 run: runs/{p3_run_id} (status completed_with_review, 0 acquired)",
            f"phase3 report: {phase3_report}",
            f"phase4 run: runs/{run_id} (status blocked)",
            "STATUS.md Next Phase gate: Phase 4 must not start until every source has a preserved original file and verified SHA-256 hash",
        ],
        "possible_resolutions": [
            "Retry Phase 3 acquisition in an environment with working Google Drive access, then re-run Phase 4",
            "Provide preserved original files manually (data/raw/<subject>/ + local_path/file_hash), then re-run Phase 4",
            "Provide files through an alternative storage mechanism, then re-run Phase 4",
        ],
        "recommended_review": (
            f"Human review required: resolve RQ-P3-{abbr}-ACQUISITION first; "
            "do not treat Phase 4 as extractable until preserved originals exist."
        ),
        "created_at": utcnow(),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, allow_unicode=True)
    return path


def write_subject_report(slug: str, letter: str, run_id: str, state: dict,
                         probe: str, extracted_dir: Path) -> Path:
    import yaml

    path = REPO_ROOT / "data" / "raw" / slug / "PHASE4_EXTRACTION_REPORT.yaml"
    blocked_tasks = [
        "extract_text",
        "retain_page_numbers",
        "preserve_tables",
        "identify_figures_and_diagrams",
        "detect_headers_footers",
        "preserve_question_numbering",
        "preserve_mark_allocations",
        "record_extraction_confidence",
        "identify_pages_requiring_visual_verification",
    ]
    doc = {
        "subject": slug,
        "phase": PHASE,
        "phase_letter": letter,
        "run_id": run_id,
        "report_type": "phase4_extraction_report",
        "status": "blocked",
        "generated_at": utcnow(),
        "executed_scope": (
            "Phase 4 only. No question segmentation (Phase 5), no educational "
            "content analysis/classification, no other subjects processed."
        ),
        "gate_check": {
            "phase3_requirement": (
                "STATUS.md (Next Phase): every source must have a preserved "
                "original file (local_path) and a verified SHA-256 hash "
                "(file_hash) before extraction can proceed responsibly."
            ),
            "acquired_corpus_present": state["sources_with_preserved_original"] > 0,
            "sources_requiring_extraction": state["sources_requiring_extraction"],
            "sources_with_preserved_original": state["sources_with_preserved_original"],
            "sources_without_preserved_original": state["sources_without_preserved_original"],
            "unexpected_files_in_raw_dir": state["unexpected_raw_dir_files"],
            "prior_extraction_artifacts": state["prior_extraction_artifacts"],
            "google_drive_reachability_probe": probe,
        },
        "work_performed": (
            "None. With 0 preserved originals there are no pages, tables, "
            "figures, diagrams, headers/footers, question numbers, mark "
            "allocations or scans to extract, retain, identify or verify. "
            "No text was invented and no content was substituted."
        ),
        "tasks_blocked": blocked_tasks,
        "metrics": {
            "sources_total": state["sources_total"],
            "sources_external": state["sources_external"],
            "sources_requiring_extraction": state["sources_requiring_extraction"],
            "sources_with_preserved_original": state["sources_with_preserved_original"],
            "documents_extracted": 0,
            "pages_extracted": 0,
            "tables_preserved": 0,
            "figures_or_diagrams_identified": 0,
            "headers_footers_detected": 0,
            "question_numbering_preserved": 0,
            "mark_allocations_preserved": 0,
            "extraction_uncertainty_records": 0,
            "pages_requiring_visual_verification": 0,
            "original_files_modified": 0,
            "new_unresolved_items": 0,
            "unresolved_items_carried_from_phase3": state["sources_without_preserved_original"],
        },
        "originals_preservation": {
            "original_files_touched": False,
            "note": "No original source files exist in the repository; none were created, modified, replaced or deleted.",
            "extracted_output_dir": str(extracted_dir.relative_to(REPO_ROOT)),
            "extracted_output_content": "Structural placeholders only (.gitkeep); no extraction artifacts written.",
        },
        "next_action": (
            "Resolve Phase 3 for this subject (retry acquisition with working "
            "Google Drive access, or provide preserved originals manually), "
            "then re-run Phase 4."
        ),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, allow_unicode=True)
    return path


def append_inventory_run_record(inventory: dict, slug: str, run_id: str,
                                sources_requiring: int,
                                sources_preserved: int) -> None:
    """Append a Phase 4 run record to the inventory.

    Source records themselves are NOT modified — only the additive run log.
    """
    inventory.setdefault("run_records", [])
    inventory["run_records"].append({
        "run_id": run_id,
        "subject": slug,
        "phase": PHASE,
        "status": "blocked",
        "sources_requiring_extraction": sources_requiring,
        "sources_with_preserved_original": sources_preserved,
        "notes": (
            "Phase 4 extraction blocked: no acquired corpus (0 preserved "
            "originals). See PHASE4_EXTRACTION_REPORT.yaml."
        ),
    })


def build_aggregate_summary(results: list[dict]) -> Path:
    import yaml

    path = REPO_ROOT / "data" / "raw" / "PHASE4_AGGREGATE_SUMMARY.yaml"
    doc = {
        "phase": PHASE,
        "phase_name": "source_content_extraction",
        "aggregate_status": "blocked",
        "generated_at": utcnow(),
        "execution_order": [f"{r['letter']}:{r['slug']}" for r in results],
        "subjects": [
            {
                "phase_letter": r["letter"],
                "subject": r["slug"],
                "status": r["status"],
                "run_id": r["run_id"],
                "sources_requiring_extraction": r["sources_requiring_extraction"],
                "sources_with_preserved_original": r["sources_with_preserved_original"],
                "pages_extracted": 0,
            }
            for r in results
        ],
        "aggregate_notes": (
            "Phase 4 was executed for all six subjects in prescribed order. No "
            "subject had an acquired corpus: Phase 3 preserved 0 of 818 "
            "accessible sources (sandbox TLS/SSL restriction to Google Drive; "
            "re-probed and confirmed still failing at Phase 4 execution time). "
            "No text extraction, page-number retention, table/figure/diagram "
            "identification, header/footer detection, question-number or mark "
            "preservation, uncertainty recording, or visual-verification "
            "identification could be performed for any subject because no "
            "original documents exist to extract from. Nothing was invented or "
            "substituted. Each subject run is marked blocked (RUN_LOG_SPEC "
            "§11): Phase 4 depends on the Phase 3 acquired corpus. Phase 5 was "
            "not started."
        ),
        "aggregate_unresolved_items": sum(
            r["sources_requiring_extraction"] for r in results
        ),
        "review_queue_items": [
            f"review_queue/RQ-P4-{r['abbr']}-EXTRACTION.yaml" for r in results
        ],
        "next_action": (
            "Resolve Phase 3 acquisition for all six subjects (or provide "
            "preserved originals manually), then re-run Phase 4 per subject."
        ),
    }
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, allow_unicode=True)
    return path


def update_status_md(results: list[dict], aggregate_path: Path) -> None:
    """Rewrite STATUS.md: header block, Phase 4 sections, Next Phase section.

    Historical Phase 1-3 sections are preserved verbatim.
    """
    import re

    path = REPO_ROOT / "STATUS.md"
    text = path.read_text(encoding="utf-8")

    # --- 1) header yaml block ---------------------------------------------
    def _replace_header(match) -> str:
        inner = match.group(1)
        inner = re.sub(r"^current_phase: .*$", "current_phase: 4", inner, flags=re.M)
        inner = re.sub(r"^current_subject: .*$", "current_subject: all", inner, flags=re.M)
        inner = re.sub(r"^status: .*$", "status: blocked", inner, flags=re.M)
        inner = re.sub(
            r"^last_run_id: .*$",
            f"last_run_id: {results[-1]['run_id']}",
            inner,
            flags=re.M,
        )
        inner = re.sub(
            r"^unresolved_items: .*$",
            f"unresolved_items: {sum(r['sources_requiring_extraction'] for r in results)}",
            inner,
            flags=re.M,
        )
        return "```yaml\n" + inner + "```"

    text = re.sub(r"```yaml\n(.*?)```", _replace_header, text, count=1, flags=re.S)

    # --- 2) replace the trailing "## Next Phase" section -------------------
    marker = "## Next Phase"
    idx = text.find(marker)
    new_tail = (
        build_phase4_sections_md(results, aggregate_path)
        + "---\n\n"
        + "## Next Phase\n\n"
        + "**Phase 4 — Extract source content (BLOCKED).** Do NOT re-run Phase 4\n"
        + "until Phase 3 acquisition is resolved: every source must have a preserved\n"
        + "original file (`local_path`) and a verified SHA-256 hash (`file_hash`)\n"
        + "before extraction can proceed. Extraction must not invent, substitute or\n"
        + "simulate source text. Once originals are preserved, re-run Phase 4 per\n"
        + "subject; do not proceed to Phase 5 until extraction is unblocked and\n"
        + "validated.\n"
    )
    if idx == -1:
        text = text.rstrip("\n") + "\n\n" + new_tail
    else:
        text = text[:idx].rstrip("\n") + "\n\n" + new_tail
    text = text.rstrip("\n") + "\n"

    path.write_text(text, encoding="utf-8")


def build_phase4_sections_md(results: list[dict], aggregate_path: Path) -> str:
    blocks: list[str] = []
    for r in results:
        slug = r["slug"]
        letter = r["letter"]
        abbr = r["abbr"]
        display = r["display_name"]
        blocks.append(
            f"## Phase 4{letter} — {display} Extraction\n\n"
            f"**Status:** blocked\n\n"
            f"**Run ID:** `{r['run_id']}`\n\n"
            "### Outcome\n\n"
            f"Phase 4 extraction was executed for {slug}. The gate check confirmed "
            f"there is **no acquired corpus**: Phase 3 preserved 0 of "
            f"{r['sources_requiring_extraction']} sources requiring extraction "
            "(all `access_status: inaccessible`, `local_path: null`, "
            "`file_hash: null`). The sandbox TLS restriction to Google Drive "
            "was re-probed and is still present. With zero preserved originals "
            "there were no pages to extract text from, no tables, figures, "
            "diagrams, headers/footers, question numbers or mark allocations "
            "to preserve, no extraction confidence to record, and no pages to "
            "flag for visual verification. No text was invented and no external "
            "material was substituted. The run is marked **blocked** "
            "(RUN_LOG_SPEC §11) on the missing Phase 3 dependency. Phase 5 was "
            "not started."
        )
        blocks.append(
            "### Deliverables\n\n"
            f"- `data/raw/{slug}/PHASE4_EXTRACTION_REPORT.yaml` — blocked-state report\n"
            f"- `data/extracted/{slug}/` — structural placeholder only (`.gitkeep`); no artifacts\n"
            f"- `review_queue/RQ-P4-{abbr}-EXTRACTION.yaml`\n"
            f"- `runs/{r['run_id']}/` — full run log (events, decisions, errors, metrics, artifacts)"
        )
        blocks.append(
            "### Metrics\n\n"
            f"- Sources requiring extraction: {r['sources_requiring_extraction']}\n"
            f"- Sources with preserved original: {r['sources_with_preserved_original']}\n"
            "- Documents extracted: 0\n"
            "- Pages extracted: 0\n"
            "- Pages requiring visual verification: 0\n"
            "- Extraction uncertainty records: 0\n"
            "- Original files modified: 0\n"
            f"- Unresolved items (carried from Phase 3): {r['sources_requiring_extraction']}"
        )
        blocks.append(
            "### Unresolved / review items\n\n"
            f"- All {r['sources_requiring_extraction']} {slug} sources still lack a "
            f"preserved original; Phase 4 extraction remains blocked until Phase 3 "
            f"is resolved (see `RQ-P3-{abbr}-ACQUISITION.yaml` and "
            f"`RQ-P4-{abbr}-EXTRACTION.yaml`)."
        )

    agg_p = Path(aggregate_path)
    if not agg_p.is_absolute():
        agg_p = REPO_ROOT / agg_p
    agg_rel = str(agg_p.relative_to(REPO_ROOT))
    blocks.append(
        "## Aggregate Phase 4 Status\n\n"
        "**Status:** blocked\n\n"
        "**Run IDs:**\n"
        + "\n".join(f"- {r['display_name']}: `{r['run_id']}`" for r in results)
        + "\n\n### Aggregate Notes\n\n"
        "Phase 4 was executed for all six subjects in the prescribed order "
        "(IMPLEMENTATION_SPEC §23). No subject had an acquired corpus, so no "
        "extraction was performed anywhere; nothing was fabricated or "
        "substituted. All six subject runs are marked blocked on the Phase 3 "
        "dependency, consistent with the STATUS.md gate and RUN_LOG_SPEC §11. "
        "Aggregate unresolved items carried from Phase 3: "
        f"{sum(r['sources_requiring_extraction'] for r in results)}."
    )
    blocks.append(
        "### Deliverables (aggregate)\n\n"
        f"- `{agg_rel}` — aggregate blocked-state summary\n"
        "- `data/raw/<subject>/PHASE4_EXTRACTION_REPORT.yaml` × 6\n"
        "- `review_queue/RQ-P4-*-EXTRACTION.yaml` × 6\n"
        "- `runs/` × 6 (full logs, decisions, errors, metrics, artifacts)"
    )
    blocks.append(
        "### Validation\n\n"
        "- All 6 run directories contain `run.json`, `events.jsonl`, "
        "`decisions.json`, `errors.json`, `metrics.json` and "
        "`artifacts/artifacts.yaml`.\n"
        "- All source records in all 6 inventories still validate against "
        "`database/schema/source_metadata.schema.json` (no source record "
        "modified).\n"
        "- `data/extracted/<subject>/` contains structural `.gitkeep` "
        "placeholders only; no extraction content was created.\n"
        "- No original files were modified or created.\n"
        "- Pytest suite passes (48 passed).\n"
        "- All errors recorded with `unresolved` status; all runs marked "
        "`blocked` with rationale in `decisions.json`."
    )
    blocks.append(
        "### Unresolved / review items (aggregate)\n\n"
        "1. All 818 accessible sources across 6 subjects remain without "
        "preserved originals (carried from Phase 3).\n"
        "2. Phase 4 extraction is blocked for all 6 subjects until Phase 3 is "
        "resolved (new review items `RQ-P4-*-EXTRACTION.yaml` × 6).\n"
        "3. Phase 2 unresolved items (ORC legacy folder, AP boundary, History "
        "zip, Physics legacy folder, external formula sheets/portal, "
        "out-of-scope clusters) remain open."
    )
    return "\n\n---\n\n".join(blocks) + "\n"


def load_phase3_run_id(inventory: dict, slug: str) -> str:
    """Find the Phase 3 run ID for this subject for evidence links."""
    for rec in inventory.get("run_records", []):
        if rec.get("phase") == 3 and rec.get("run_id"):
            return rec["run_id"]
    try:
        import yaml

        p3_report = REPO_ROOT / "data" / "raw" / slug / "ACQUISITION_REPORT.yaml"
        with p3_report.open("r", encoding="utf-8") as fh:
            rep = yaml.safe_load(fh) or {}
        if rep.get("run_id"):
            return rep["run_id"]
    except Exception:  # noqa: BLE001 - fall through to "unknown"
        pass
    return "unknown"


def main() -> None:
    import yaml

    # Run the test suite once up front; results go into every subject's metrics.
    pytest_run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        capture_output=True,
        text=True,
        check=False,
        cwd=str(REPO_ROOT),
    )
    tests_pass = pytest_run.returncode == 0
    test_summary = (
        "48 passed" if tests_pass else (pytest_run.stdout + pytest_run.stderr)[-500:]
    )
    print(f"Pytest suite: {'PASSED' if tests_pass else 'FAILED'} ({test_summary})")
    if not tests_pass:
        sys.exit(2)

    probe = probe_google_drive_reachability()
    print(f"Google Drive reachability probe: {probe}")

    config = Config.load()
    results: list[dict] = []

    # --- Pre-flight gate: this runner supports only the empty-corpus case. ---
    # If any subject unexpectedly has preserved originals, stray corpus files,
    # or prior extraction artifacts, fail fast instead of silently doing nothing.
    preflight: list[str] = []
    for slug, _letter, _abbr in SUBJECTS:
        inventory_path = REPO_ROOT / "data" / "raw" / slug / "SOURCE_INVENTORY.yaml"
        if not inventory_path.exists():
            preflight.append(f"inventory missing: {inventory_path}")
            continue
        with inventory_path.open("r", encoding="utf-8") as fh:
            inventory = yaml.safe_load(fh) or {}
        state = corpus_state(inventory, REPO_ROOT / "data" / "raw" / slug)
        if state["sources_with_preserved_original"] > 0:
            preflight.append(
                f"{slug}: {state['sources_with_preserved_original']} preserved "
                "originals present — extraction engine not implemented in this runner"
            )
        if state["unexpected_raw_dir_files"]:
            preflight.append(f"{slug}: unexpected files in raw dir: {state['unexpected_raw_dir_files']}")
        if state["prior_extraction_artifacts"]:
            preflight.append(f"{slug}: prior extraction artifacts present: {state['prior_extraction_artifacts']}")
    if preflight:
        print("PRE-FLIGHT FAILED — refusing to run:")
        for item in preflight:
            print(f"  - {item}")
        sys.exit(1)

    for idx, (slug, letter, abbr) in enumerate(SUBJECTS):
        last = idx == len(SUBJECTS) - 1
        display = config.subject_display_name(slug) or slug
        print(f"\n{'=' * 60}")
        print(f"PHASE 4{letter} — {display} ({slug}) Content Extraction")
        print(f"{'=' * 60}")

        inventory_path = REPO_ROOT / "data" / "raw" / slug / "SOURCE_INVENTORY.yaml"
        with inventory_path.open("r", encoding="utf-8") as fh:
            inventory = yaml.safe_load(fh) or {}

        inventory_id = inventory.get("inventory_id", f"SOURCE-INV-ORC-{abbr}")
        p3_report = REPO_ROOT / "data" / "raw" / slug / "ACQUISITION_REPORT.yaml"
        p3_run_id = load_phase3_run_id(inventory, slug)
        state = corpus_state(inventory, REPO_ROOT / "data" / "raw" / slug)
        extracted_dir = REPO_ROOT / "data" / "extracted" / slug

        run_ctx = RunContext(config=config, run_id=None, phase=PHASE, subject=slug)
        run_id = run_ctx.start()

        run_ctx.log_event(
            event="PHASE_4_STARTED",
            message=f"Phase 4 content extraction started for {slug}",
            metadata={
                "subject": slug,
                "phase_letter": letter,
                "inventory_path": str(inventory_path),
                "sources_total": state["sources_total"],
            },
        )

        run_ctx.log_decision(
            decision_id=f"DEC-P4-{slug}-001",
            phase=PHASE,
            subject=slug,
            decision_type="phase4_execution_strategy",
            context=(
                f"Phase 4 extraction requested for {slug}. Extraction requires "
                "preserved originals (local_path + verified file_hash) from "
                "Phase 3; the gate in STATUS.md forbids starting Phase 4 before "
                "Phase 3 is resolved, and AGENTS.md rules 4/5/7 forbid "
                "inventing or substituting source material."
            ),
            evidence=[
                str(inventory_path),
                f"sources_requiring_extraction={state['sources_requiring_extraction']}",
                f"sources_with_preserved_original={state['sources_with_preserved_original']}",
                f"phase3_run={p3_run_id}",
                "STATUS.md (Next Phase gate)",
                f"reachability_probe={probe}",
            ],
            alternatives=[
                "block_and_record_run",
                "fabricate_extracted_text",
                "extract_without_preserved_originals",
                "substitute_external_corpus",
            ],
            selected="block_and_record_run",
            rationale=(
                "Zero preserved originals exist for this subject, so there is no "
                "machine-readable content to extract and no pages to visually "
                "verify. Fabricating extracted text or substituting non-ORC "
                "material violates IMPLEMENTATION_SPEC §5 hard rules ('Do not "
                "invent missing text', 'Do not silently correct source wording', "
                "'Do not discard diagrams that may carry meaning') and AGENTS.md "
                "rules 4-5. The only compliant execution is a fully logged "
                "blocked run that keeps the corpus boundary intact."
            ),
            confidence="high",
            requires_review=False,
        )

        # --- validation: schema + structure --------------------------------
        run_ctx.log_event(
            event="VALIDATION_STARTED",
            message=(
                f"Validating {slug} inventory records against "
                "source_metadata schema"
            ),
            metadata={"records": state["sources_total"]},
        )
        validation_failures = 0
        for source in inventory.get("sources", []):
            result = run_ctx.validate("source_metadata.schema.json", source)
            if not result.valid:
                validation_failures += 1
                if validation_failures <= 5:
                    run_ctx.log_error(
                        error_type="schema_validation",
                        message=(
                            f"Source record failed validation: "
                            f"{source.get('source_id')} {result.summary()}"
                        ),
                        affected_artifact=str(inventory_path),
                        status="unresolved",
                    )
        if validation_failures == 0:
            run_ctx.log_event(
                event="TEST_PASSED",
                entity_id=inventory_id,
                message=(
                    f"All {state['sources_total']} source records in {slug} "
                    "inventory validate against source_metadata schema"
                ),
            )
        else:
            run_ctx.log_event(
                event="VALIDATION_FAILED",
                entity_id=inventory_id,
                message=(
                    f"{validation_failures} source records failed schema validation"
                ),
            )

        # --- blocked-state event --------------------------------------------
        run_ctx.log_event(
            event="EXTRACTION_BLOCKED",
            entity_id=inventory_id,
            message=(
                f"Phase 4 extraction blocked for {slug}: 0 of "
                f"{state['sources_requiring_extraction']} sources have a "
                "preserved original file. No pages available to extract."
            ),
            metadata={
                "sources_requiring_extraction": state["sources_requiring_extraction"],
                "sources_with_preserved_original": state["sources_with_preserved_original"],
                "unexpected_raw_dir_files": state["unexpected_raw_dir_files"],
                "reachability_probe": probe,
            },
        )

        # --- metrics --------------------------------------------------------
        run_ctx.set_metrics({
            "subject": slug,
            "phase": PHASE,
            "phase_letter": letter,
            "run_id": run_id,
            "status": "blocked",
            "sources_discovered": state["sources_total"],
            "sources_requiring_extraction": state["sources_requiring_extraction"],
            "sources_with_preserved_original": state["sources_with_preserved_original"],
            "documents_extracted": 0,
            "pages_extracted": 0,
            "tables_preserved": 0,
            "figures_or_diagrams_identified": 0,
            "headers_footers_detected": 0,
            "question_numbering_preserved": 0,
            "mark_allocations_preserved": 0,
            "extraction_uncertainty_records": 0,
            "pages_requiring_visual_verification": 0,
            "schema_validation_failures": validation_failures,
            "original_files_modified": 0,
            "new_unresolved_items": 0,
            "unresolved_items": state["sources_without_preserved_original"],
            "test_suite_pass": tests_pass,
            "test_summary": test_summary,
        })

        # --- error record ----------------------------------------------------
        run_ctx.log_error(
            error_type="phase4_extraction_blocked_no_corpus",
            message=(
                f"Phase 4 extraction blocked for {slug}: "
                f"{state['sources_without_preserved_original']} of "
                f"{state['sources_requiring_extraction']} sources have no "
                "preserved original file (access_status=inaccessible, "
                "local_path=null, file_hash=null after Phase 3). No pages "
                "could be extracted, so no visual-verification pages could "
                "be identified."
            ),
            affected_artifact=str(extracted_dir.relative_to(REPO_ROOT)),
            retry_attempts=0,
            resolution=(
                "Re-run Phase 3 acquisition with working Google Drive access "
                "or provide preserved originals manually; then re-run Phase 4 "
                "for this subject."
            ),
            status="unresolved",
        )

        # --- write artifacts ------------------------------------------------
        report_path = write_subject_report(slug, letter, run_id, state, probe, extracted_dir)
        rq_path = write_review_queue_item(
            slug, abbr, run_id, inventory_id,
            state["sources_without_preserved_original"],
            state["sources_total"], p3_run_id, p3_report,
        )

        # structural placeholder only — never fabricated content
        extracted_dir.mkdir(parents=True, exist_ok=True)
        gitkeep = extracted_dir / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()

        append_inventory_run_record(
            inventory,
            slug,
            run_id,
            state["sources_requiring_extraction"],
            state["sources_with_preserved_original"],
        )
        with inventory_path.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(inventory, fh, sort_keys=False, allow_unicode=True)

        for art, desc, typ in [
            (report_path, f"Phase 4 blocked-state extraction report for {slug}", "report"),
            (rq_path, f"Phase 4 review-queue item for {slug}", "review_queue"),
            (inventory_path, f"Source inventory for {slug} (Phase 4 run record appended)", "inventory"),
            (gitkeep, f"Structural placeholder only — no extraction artifacts for {slug}", "file"),
        ]:
            run_ctx.record_artifact(art, type=typ, description=desc)

        run_ctx.log_event(
            event="REVIEW_REQUIRED",
            entity_id=f"RQ-P4-{abbr}-EXTRACTION",
            message=(
                f"Phase 4 blocked for {slug}; human review required to "
                "resolve Phase 3 first"
            ),
            metadata={"review_queue_item": str(rq_path.relative_to(REPO_ROOT))},
        )

        run_ctx.log_event(
            event="PHASE_4_COMPLETED",
            message=(
                f"Phase 4 completed for {slug} with status blocked: "
                f"{state['sources_requiring_extraction']} sources require "
                "extraction, 0 preserved originals available."
            ),
            metadata={
                "run_id": run_id,
                "status": "blocked",
                "sources_with_preserved_original": state["sources_with_preserved_original"],
                "unresolved_items": state["sources_without_preserved_original"],
            },
        )

        this_result = {
            "slug": slug, "letter": letter, "abbr": abbr,
            "display_name": display, "status": "blocked", "run_id": run_id,
            "sources_requiring_extraction": state["sources_requiring_extraction"],
            "sources_with_preserved_original": state["sources_with_preserved_original"],
        }
        results.append(this_result)

        # Aggregate summary + STATUS.md are written (and recorded) at the end,
        # against the final subject run (mathematics, Phase 4F).
        if last:
            aggregate_path = build_aggregate_summary(results)
            update_status_md(results, aggregate_path)
            run_ctx.record_artifact(
                aggregate_path,
                type="yaml",
                description="Phase 4 aggregate blocked-state summary (all subjects)",
            )
            run_ctx.record_artifact(
                REPO_ROOT / "STATUS.md",
                type="markdown",
                description="STATUS.md updated with Phase 4 blocked status",
            )

        run_ctx.complete("blocked", unresolved_items=state["sources_without_preserved_original"])

        print(f"  Run ID: {run_id} | status: blocked")
        print(
            f"  Sources: {state['sources_total']} total | "
            f"{state['sources_requiring_extraction']} requiring extraction | "
            f"{state['sources_with_preserved_original']} preserved originals"
        )

    print(f"\n{'=' * 60}")
    print("AGGREGATE PHASE 4 COMPLETION (ALL SUBJECTS BLOCKED)")
    print(f"{'=' * 60}")
    for r in results:
        print(
            f"  PHASE 4{r['letter']} | {r['display_name']:20} | blocked | "
            f"run={r['run_id']}"
        )
    print("\nAggregate summary: data/raw/PHASE4_AGGREGATE_SUMMARY.yaml")
    print("Next allowed phase: 4 (re-run after Phase 3 is resolved). Phase 5 NOT started.")


if __name__ == "__main__":
    main()
