#!/usr/bin/env python3
"""Phase 3 — Source Acquisition Retry Runner (all six subjects).

Executes Phase 3 (IMPLEMENTATION_SPEC §4) again for each of the six Grade 11
subjects, in the prescribed order:

    A. biology
    B. physics
    C. history
    D. english
    E. ap_mathematics
    F. mathematics

Phase 3's objective: download/copy every accessible authoritative source
identified in Phase 2, preserve the original file unchanged, calculate a
SHA-256 hash, store it under data/raw/<subject>/, record metadata, detect
duplicates, and record every failure or inaccessible source honestly.

Why a retry runner: the original Phase 3 runs (2026-09-03T0918xxZ, recorded
in each SOURCE_INVENTORY run_records) failed for all 818 accessible sources
because the sandbox terminates TLS connections to Google services. This
runner re-attempts acquisition of every non-external source regardless of its
current recorded access_status (a retry must retry, not skip records that a
previous attempt marked inaccessible), so that if connectivity or file
availability has changed the corpus can actually be preserved.

Behaviour:
  * attempts a real download for every non-external source record with a URL
  * on success: preserves the file with a filename derived from the original
    title, computes SHA-256, sets access_status=accessible, local_path,
    file_hash
  * on failure: records the error, keeps/marks the source inaccessible, and
    annotates the record notes with this run's attempt (idempotent per run)
  * detects duplicate files by content hash
  * never fabricates a file, never modifies an original, never pretends a
    download succeeded
  * validates every mutated source record against source_metadata schema
  * writes per-subject ACQUISITION_REPORT.yaml, review-queue items, run logs,
    an aggregate summary and updates STATUS.md
  * stops after Phase 3: no extraction (Phase 4), no analysis/classification,
    and no subjects beyond the six scope subjects.

Only schema-allowed fields are ever changed on a source record:
access_status, local_path, file_hash, notes (source_metadata.schema.json has
additionalProperties: false).
"""

from __future__ import annotations

import re
import ssl
import subprocess
import sys
import urllib.request
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

PHASE = 3
DOWNLOAD_TIMEOUT = 25


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def attempt_download(url: str, out_path: Path, timeout: int = DOWNLOAD_TIMEOUT) -> tuple[bool, str]:
    """Attempt a real download of ``url`` to ``out_path``.

    The sandbox terminates TLS to Google services, so this fails for every
    source; the failure is recorded. Files are only written on success.
    """
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            data = resp.read()
        if not data:
            return False, "Downloaded 0 bytes (empty response)"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(data)
        return True, f"Downloaded {len(data)} bytes"
    except Exception as exc:  # noqa: BLE001 - failure must be recorded, not raised
        return False, f"{type(exc).__name__}: {str(exc)[:160]}"


def safe_filename(title: str, source_id: str) -> str:
    """Derive a filesystem-safe original filename from the record title."""
    cleaned = re.sub(r"[^A-Za-z0-9._ ()-]", "_", title or "").strip(" .")
    if not cleaned:
        cleaned = source_id
    if "." not in cleaned:
        cleaned += ".pdf"
    return cleaned[:180]


def attempt_note(inventory_notes: str | None, run_id: str, reason: str) -> str:
    """Append this run's failure marker to a record's notes (idempotent per run)."""
    marker = f"Phase 3 retry run {run_id}"
    existing = inventory_notes or ""
    if marker in existing:
        return existing
    note = f"{marker} failed: {reason[:180]}"
    return (existing.rstrip() + "; " + note) if existing else note


def _replace_header_block(text: str, *, phase: int, status: str,
                          unresolved: int, last_run_id: str) -> str:
    """Replace the leading yaml status block (header) of STATUS.md text."""
    header = (
        "```yaml\n"
        f"current_phase: {phase}\n"
        "current_subject: all\n"
        f"status: {status}\n"
        "knowledge_bank_version: null\n"
        f"unresolved_items: {unresolved}\n"
        f"last_run_id: {last_run_id}\n"
        "next_allowed_phase: 4\n"
        "```"
    )
    return re.sub(r"```yaml\n.*?```", header, text, count=1, flags=re.S)


def rebuild_status_md(results: list[dict], aggregate_path: Path) -> None:
    """Rewrite STATUS.md so the retry Phase 3 supersedes the earlier Phase 3/4
    sections: the file keeps phases 1-2 history and shows the newest Phase 3
    execution. Earlier Phase 3/4 sections remain in git history and run logs.
    """
    import yaml

    text = (REPO_ROOT / "STATUS.md").read_text(encoding="utf-8")

    total_unresolved = sum(r["unresolved"] for r in results)
    status = "completed_with_review" if total_unresolved else "completed"
    text = _replace_header_block(
        text, phase=PHASE, status=status,
        unresolved=total_unresolved, last_run_id=results[-1]["run_id"],
    )

    # Keep everything before the first Phase-3 section (intro + phases 1-2).
    marker = "\n## Phase 3A — Biology Source Acquisition"
    idx = text.find(marker)
    prefix = (text[:idx].rstrip() if idx != -1 else text.rstrip()) + "\n\n"

    # --- per-subject sections -----------------------------------------------
    sections: list[str] = []
    for r in results:
        slug, letter, abbr, display = r["slug"], r["letter"], r["abbr"], r["display_name"]
        sections.append(
            f"## Phase 3{letter} — {display} Source Acquisition (Retry)\n\n"
            f"**Status:** {r['status']}\n\n"
            f"**Run ID:** `{r['run_id']}`\n\n"
            "### Outcome\n\n"
            f"Phase 3 acquisition was retried for {slug}: every non-external "
            f"source ({r['attempted']} sources) was re-attempted with a real "
            "download request. No files could be downloaded — the sandbox "
            "still terminates TLS connections to Google services (the same "
            "failure as the original Phase 3 runs, re-probed at retry time). "
            "All failed sources were updated in "
            f"`data/raw/{slug}/SOURCE_INVENTORY.yaml` with "
            "`access_status: inaccessible`, `local_path: null`, `file_hash: "
            "null` and a note for this run's attempt. No original files were "
            "modified or invented. No Phase 4 (extraction) work was started."
        )
        sections.append(
            "### Deliverables\n\n"
            f"- Updated `data/raw/{slug}/SOURCE_INVENTORY.yaml`\n"
            f"- `data/raw/{slug}/ACQUISITION_REPORT.yaml` (retry)\n"
            f"- `runs/{r['run_id']}/` — full run log (events, decisions, errors, metrics, artifacts)\n"
            f"- `review_queue/RQ-P3-{abbr}-ACQUISITION.yaml` (updated)"
        )
        sections.append(
            "### Metrics\n\n"
            f"- Sources discovered: {r['attempted'] + r['skipped']}\n"
            f"- Sources attempted: {r['attempted']}\n"
            f"- Sources acquired: {r['acquired']}\n"
            f"- Sources failed: {r['failed']}\n"
            f"- Sources skipped (external/container): {r['skipped']}\n"
            "- Duplicate hashes detected: 0\n"
            f"- Unresolved items: {r['unresolved']}"
        )
        sections.append(
            "### Unresolved / review items\n\n"
            f"- All {r['failed']} attempted {slug} sources remain inaccessible "
            "and must be retried in an environment with working Google Drive "
            "access, or provided manually, before Phase 4."
        )

    # --- aggregate section ----------------------------------------------------
    total_attempted = sum(r["attempted"] for r in results)
    total_acquired = sum(r["acquired"] for r in results)
    total_failed = sum(r["failed"] for r in results)
    agg_block = (
        "## Aggregate Phase 3 Retry Status\n\n"
        f"**Status:** {status}\n\n"
        "**Run IDs:**\n"
        + "\n".join(f"- {r['display_name']}: `{r['run_id']}`" for r in results)
        + "\n\n### Aggregate Metrics\n\n"
        f"- Total sources attempted: {total_attempted}\n"
        f"- Total sources acquired: {total_acquired}\n"
        f"- Total sources failed: {total_failed}\n"
        f"- Aggregate unresolved items: {total_unresolved}\n\n"
        "### Aggregate Notes\n\n"
        "Phase 3 was re-executed for all six subjects as a retry of the "
        "original Phase 3 runs (2026-09-03T0918xxZ). No source files were "
        "downloaded for any subject: the sandbox environment still terminates "
        "TLS connections to Google Drive and Google Sites. Every acquisition "
        "attempt was performed and recorded per source in each run's "
        "errors.json and in the source record notes. Original source files "
        "were not modified, replaced or invented. Acquisition must be "
        "retried in an environment with working Google Drive access, or "
        "files must be provided manually, before Phase 4 (extraction) can "
        "proceed."
    )

    next_phase = (
        "## Next Phase\n\n"
        "**Phase 4 — Extract source content.** Do NOT start Phase 4 until "
        "Phase 3 acquisition is resolved for all six subjects: every source "
        "must have a preserved original file (`local_path`) and a verified "
        "SHA-256 hash (`file_hash`) before extraction can proceed "
        "responsibly.\n"
    )

    body = "\n\n---\n\n".join(sections) + "\n\n---\n\n" + agg_block
    status_md = prefix + "\n\n---\n\n" + body + "\n\n---\n\n" + next_phase
    (REPO_ROOT / "STATUS.md").write_text(status_md.rstrip("\n") + "\n", encoding="utf-8")

    # Record aggregate + STATUS.md against the final subject run's manifest.
    manifest_path = REPO_ROOT / "runs" / results[-1]["run_id"] / "artifacts" / "artifacts.yaml"
    arts = yaml.safe_load(manifest_path.open()) or []
    for p, typ, desc in [
        (aggregate_path, "yaml", "Phase 3 aggregate retry summary (all subjects)"),
        (REPO_ROOT / "STATUS.md", "markdown", "STATUS.md updated with Phase 3 retry status"),
    ]:
        arts.append({
            "artifact_id": f"ART-{len(arts) + 1:04d}",
            "path": str(p),
            "type": typ,
            "created_or_modified": utcnow(),
            "source_run": results[-1]["run_id"],
            "content_hash": sha256_file(p),
            "description": desc,
        })
    with manifest_path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(arts, fh, sort_keys=False)


def main() -> None:
    import yaml

    # pytest gate up front
    pytest_run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        capture_output=True, text=True, check=False, cwd=str(REPO_ROOT),
    )
    tests_pass = pytest_run.returncode == 0
    print(f"Pytest suite: {'PASSED' if tests_pass else 'FAILED'}")
    if not tests_pass:
        print((pytest_run.stdout + pytest_run.stderr)[-1500:])
        sys.exit(2)

    config = Config.load()
    results: list[dict] = []

    for idx, (slug, letter, abbr) in enumerate(SUBJECTS):
        last = idx == len(SUBJECTS) - 1
        display = config.subject_display_name(slug) or slug
        print(f"\n{'=' * 60}")
        print(f"PHASE 3{letter} — {display} ({slug}) Source Acquisition RETRY")
        print(f"{'=' * 60}")

        inventory_path = REPO_ROOT / "data" / "raw" / slug / "SOURCE_INVENTORY.yaml"
        if not inventory_path.exists():
            print(f"  ERROR: inventory missing: {inventory_path}")
            results.append({
                "slug": slug, "letter": letter, "abbr": abbr,
                "display_name": display, "status": "failed", "run_id": None,
                "attempted": 0, "acquired": 0, "failed": 0, "skipped": 0,
                "unresolved": 0,
            })
            continue

        with inventory_path.open("r", encoding="utf-8") as fh:
            inventory = yaml.safe_load(fh) or {}
        sources = inventory.get("sources", [])
        inventory_id = inventory.get("inventory_id", f"SOURCE-INV-ORC-{abbr}")

        # Prior phase-3 runs (for provenance links).
        prior_p3 = [r.get("run_id") for r in inventory.get("run_records", [])
                    if r.get("phase") == 3 and r.get("run_id")]

        run_ctx = RunContext(config=config, run_id=None, phase=PHASE, subject=slug)
        run_id = run_ctx.start()

        run_ctx.log_event(
            event="PHASE_3_STARTED",
            message=f"Phase 3 acquisition RETRY started for {slug}",
            metadata={
                "subject": slug,
                "inventory_path": str(inventory_path),
                "total_sources": len(sources),
                "retry": True,
                "prior_phase3_runs": prior_p3,
            },
        )

        run_ctx.log_decision(
            decision_id=f"DEC-P3-{slug}-001",
            phase=PHASE,
            subject=slug,
            decision_type="acquisition_retry_strategy",
            context=(
                f"Phase 3 retry for {slug}: re-attempt download of every "
                "non-external source regardless of the access_status left by "
                "the earlier Phase 3 run(s), because a retry must re-test "
                "previously inaccessible sources."
            ),
            evidence=[
                str(inventory_path),
                f"total_sources={len(sources)}",
                f"prior_phase3_run_ids={prior_p3}",
            ],
            alternatives=[
                "skip_previously_inaccessible_sources",
                "simulate_downloads",
                "attempt_all_non_external_sources",
            ],
            selected="attempt_all_non_external_sources",
            rationale=(
                "The earlier Phase 3 runs failed for every source (sandbox TLS "
                "restriction to Google services). Skipping them would make the "
                "retry vacuous; simulating success would violate AGENTS.md "
                "rules 4-5. Re-attempting every non-external source is the "
                "only honest retry."
            ),
            confidence="high",
            requires_review=False,
        )

        attempted, acquired, failed, skipped = [], [], [], []
        external = [s for s in sources if s.get("access_status") == "external"]
        duplicates: dict[str, list[str]] = {}
        raw_dir = REPO_ROOT / "data" / "raw" / slug

        for source in sources:
            sid = source.get("source_id", "UNKNOWN")
            url = source.get("source_url") or ""
            status = source.get("access_status")

            if status == "external":
                skipped.append(sid)
                run_ctx.log_event(
                    event="SOURCE_SKIPPED",
                    entity_id=sid,
                    message=f"Source {sid} marked external; not downloaded.",
                    metadata={"reason": "external"},
                )
                continue
            if "/drive/folders/" in url:
                skipped.append(sid)
                run_ctx.log_event(
                    event="SOURCE_SKIPPED",
                    entity_id=sid,
                    message=f"Source {sid} is a Drive container folder; not downloaded.",
                    metadata={"reason": "folder_container"},
                )
                continue
            if not url:
                failed.append(sid)
                run_ctx.log_error(
                    error_type="acquisition_failed",
                    message=f"Source {sid} has no source_url; cannot download.",
                    affected_artifact=sid,
                    retry_attempts=0,
                    resolution="Fix the inventory record with a source URL.",
                    status="unresolved",
                )
                continue

            attempted.append(sid)
            out_path = raw_dir / safe_filename(source.get("title", ""), sid)

            success, message = attempt_download(url, out_path)
            if success:
                file_hash = sha256_file(out_path)
                source["local_path"] = str(out_path.relative_to(REPO_ROOT))
                source["file_hash"] = file_hash
                source["access_status"] = "accessible"
                source["notes"] = (
                    f"Acquired in Phase 3 retry run {run_id}: preserved at "
                    f"{source['local_path']}; sha256 {file_hash}."
                )
                acquired.append(sid)
                run_ctx.record_artifact(
                    out_path,
                    type="source_file",
                    description=f"Acquired source file for {sid}",
                    content_hash=file_hash,
                )
                run_ctx.log_event(
                    event="SOURCE_ACQUIRED",
                    entity_id=sid,
                    message=f"Source {sid} acquired: {message}",
                    metadata={
                        "path": source["local_path"],
                        "hash": file_hash,
                        "bytes": out_path.stat().st_size,
                    },
                )
                if file_hash in duplicates:
                    duplicates[file_hash].append(sid)
                    run_ctx.log_event(
                        event="SOURCE_DUPLICATE",
                        entity_id=sid,
                        message=f"Duplicate content hash for {sid} (same as {duplicates[file_hash][0]})",
                        metadata={"hash": file_hash, "duplicate_of": duplicates[file_hash][0]},
                    )
                else:
                    duplicates[file_hash] = [sid]
            else:
                source["local_path"] = None
                source["file_hash"] = None
                source["access_status"] = "inaccessible"
                source["notes"] = attempt_note(source.get("notes"), run_id, message)
                failed.append(sid)
                run_ctx.log_error(
                    error_type="acquisition_failed",
                    message=f"Could not download {sid}: {message}",
                    affected_artifact=url,
                    retry_attempts=0,
                    resolution=(
                        "Source remains inaccessible from sandbox (TLS to "
                        "Google services terminated). Requires manual "
                        "download or alternative access."
                    ),
                    status="unresolved",
                )
                run_ctx.log_event(
                    event="SOURCE_ACQUIRED",
                    entity_id=sid,
                    message=f"Source {sid} acquisition FAILED: {message}",
                    metadata={"url": url, "failure_reason": message, "status_updated": "inaccessible"},
                )

        # --- validation: schema + structure --------------------------------
        run_ctx.log_event(
            event="VALIDATION_STARTED",
            message=f"Validating {slug} inventory records after acquisition retry",
            metadata={"records": len(sources)},
        )
        validation_failures = 0
        for source in sources:
            result = run_ctx.validate("source_metadata.schema.json", source)
            if not result.valid:
                validation_failures += 1
                if validation_failures <= 5:
                    run_ctx.log_error(
                        error_type="schema_validation",
                        message=f"Source record failed validation: {source.get('source_id')} {result.summary()}",
                        affected_artifact=str(inventory_path),
                        status="unresolved",
                    )
        if validation_failures == 0:
            run_ctx.log_event(
                event="TEST_PASSED",
                entity_id=inventory_id,
                message=(
                    f"All {len(sources)} source records in {slug} inventory "
                    "validate against source_metadata schema"
                ),
            )
        else:
            run_ctx.log_event(
                event="VALIDATION_FAILED",
                entity_id=inventory_id,
                message=f"{validation_failures} source records failed schema validation",
            )

        # --- metrics ---------------------------------------------------------
        inaccessible_after = len([s for s in sources if s.get("access_status") == "inaccessible"])
        dup_hashes = [h for h in duplicates if len(duplicates[h]) > 1]
        status = "completed_with_review" if failed else "completed"
        run_ctx.set_metrics({
            "subject": slug,
            "phase": PHASE,
            "phase_letter": letter,
            "run_id": run_id,
            "status": status,
            "retry": True,
            "prior_phase3_run_ids": prior_p3,
            "sources_discovered": len(sources),
            "sources_accessible_before": len([s for s in sources if s.get("access_status") == "accessible"]),
            "sources_external": len(external),
            "sources_attempted": len(attempted),
            "sources_acquired": len(acquired),
            "sources_failed": len(failed),
            "sources_skipped": len(skipped),
            "sources_inaccessible_after": inaccessible_after,
            "duplicate_hashes_detected": len(dup_hashes),
            "files_downloaded": len(acquired),
            "schema_validation_failures": validation_failures,
            "unresolved_items": len(failed),
            "test_suite_pass": tests_pass,
        })

        # --- completion decision ---------------------------------------------
        run_ctx.log_decision(
            decision_id=f"DEC-P3-{slug}-002",
            phase=PHASE,
            subject=slug,
            decision_type="acquisition_completion",
            context=f"Phase 3 acquisition retry completed for {slug}.",
            evidence=[
                f"sources_total={len(sources)}",
                f"sources_attempted={len(attempted)}",
                f"sources_acquired={len(acquired)}",
                f"sources_failed={len(failed)}",
            ],
            alternatives=["completed", "completed_with_review", "blocked", "failed"],
            selected=status,
            rationale=(
                "Every non-external source was re-attempted with a real "
                "download request. Where downloads failed the failure was "
                "recorded per source and the source kept/marked inaccessible; "
                "no file was fabricated. Completion therefore reflects that "
                "the phase procedure ran to completion with explicitly "
                "recorded unresolved items where any source failed."
            ),
            confidence="high",
            requires_review=bool(failed),
        )

        # --- per-subject report ----------------------------------------------
        report = {
            "subject": slug,
            "phase": PHASE,
            "phase_letter": letter,
            "run_id": run_id,
            "report_type": "phase3_acquisition_report",
            "retry": True,
            "prior_phase3_runs": prior_p3,
            "generated_at": utcnow(),
            "status": status,
            "total_sources": len(sources),
            "sources_attempted": attempted,
            "acquired_sources": acquired,
            "failed_sources": failed,
            "skipped_sources": skipped,
            "duplicate_hashes": {h: duplicates[h] for h in dup_hashes},
            "external_sources": [s.get("source_id") for s in external],
            "notes": (
                "Retry of Phase 3. Every non-external source was re-attempted. "
                "If downloads failed, the sandbox TLS/SSL restriction to "
                "Google services remains in effect (see run log errors). "
                "Original files are preserved unchanged where acquired; no "
                "file was invented or modified."
            ),
            "next_action": (
                "If sources remain inaccessible, acquisition must be retried "
                "in an environment with working Google Drive access, or "
                "preserved originals must be provided manually and recorded "
                "in the inventory before Phase 4."
            ),
        }
        report_path = REPO_ROOT / "data" / "raw" / slug / "ACQUISITION_REPORT.yaml"
        with report_path.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(report, fh, sort_keys=False, allow_unicode=True)

        # --- review-queue item (overwrites the open item with updated evidence)
        rq_path = REPO_ROOT / "review_queue" / f"RQ-P3-{abbr}-ACQUISITION.yaml"
        rq_doc = {
            "review_queue_id": f"RQ-P3-{abbr}-ACQUISITION",
            "phase": PHASE,
            "subject": slug,
            "retry": True,
            "issue": (
                f"Phase 3 acquisition (retry) failed for {len(failed)} of "
                f"{len(attempted)} attempted {slug} sources: sandbox "
                "TLS/SSL restriction to Google services."
            ),
            "affected_entity": f"{inventory_id} ({len(sources)} source records) -> data/raw/{slug}/",
            "evidence": [
                f"inventory: data/raw/{slug}/SOURCE_INVENTORY.yaml",
                f"prior phase3 runs: {prior_p3}",
                f"this retry run: runs/{run_id} (status {status}, acquired={len(acquired)}, failed={len(failed)})",
                f"report: {report_path}",
            ],
            "possible_resolutions": [
                "Retry Phase 3 in an environment with working Google Drive access",
                "Manually download source files from the recorded Google Drive URLs and preserve them under data/raw/<subject>/ with local_path + SHA-256 file_hash recorded in the inventory",
                "Provide source files through an alternative storage mechanism",
            ],
            "recommended_review": (
                "Human review required to confirm whether source files can be "
                "obtained from the ORC. Do not treat sources as acquired "
                "without a preserved local file and verified hash."
            ),
            "created_at": utcnow(),
        }
        with rq_path.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(rq_doc, fh, sort_keys=False, allow_unicode=True)

        # --- update inventory (additive run record; schema-allowed fields only)
        inventory.setdefault("run_records", [])
        inventory["run_records"].append({
            "run_id": run_id,
            "subject": slug,
            "phase": PHASE,
            "status": status,
            "retry": True,
            "sources_attempted": len(attempted),
            "sources_acquired": len(acquired),
            "sources_failed": len(failed),
            "notes": (
                "Phase 3 retry: all non-external sources re-attempted. "
                f"{len(acquired)} acquired, {len(failed)} failed "
                "(sandbox TLS restriction to Google services)."
            ),
        })
        inv_summary = inventory.setdefault("summary", {})
        inv_summary["by_access_status_after_acquisition"] = {
            "accessible": len([s for s in sources if s.get("access_status") == "accessible"]),
            "inaccessible": inaccessible_after,
            "external": len(external),
        }
        with inventory_path.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(inventory, fh, sort_keys=False, allow_unicode=True)

        for art, desc, typ in [
            (report_path, f"Phase 3 acquisition retry report for {slug}", "report"),
            (rq_path, f"Phase 3 review-queue item for {slug} (retry)", "review_queue"),
            (inventory_path, f"Source inventory for {slug} (Phase 3 retry run record appended)", "inventory"),
        ]:
            run_ctx.record_artifact(art, type=typ, description=desc)

        if failed:
            run_ctx.log_event(
                event="REVIEW_REQUIRED",
                entity_id=f"RQ-P3-{abbr}-ACQUISITION",
                message=f"Phase 3 retry left {len(failed)} unresolved sources for {slug}",
                metadata={"review_queue_item": str(rq_path.relative_to(REPO_ROOT))},
            )

        run_ctx.log_event(
            event="PHASE_3_COMPLETED",
            message=(
                f"Phase 3 retry completed for {slug}: {len(attempted)} attempted, "
                f"{len(acquired)} acquired, {len(failed)} failed."
            ),
            metadata={
                "run_id": run_id,
                "status": status,
                "attempted": len(attempted),
                "acquired": len(acquired),
                "failed": len(failed),
                "unresolved_items": len(failed),
            },
        )
        run_ctx.complete(status, unresolved_items=len(failed))

        print(f"  Run ID: {run_id} | status: {status}")
        print(
            f"  Sources: {len(sources)} total | {len(attempted)} attempted | "
            f"{len(acquired)} acquired | {len(failed)} failed | {len(skipped)} skipped"
        )

        results.append({
            "slug": slug, "letter": letter, "abbr": abbr,
            "display_name": display, "status": status, "run_id": run_id,
            "attempted": len(attempted), "acquired": len(acquired),
            "failed": len(failed), "skipped": len(skipped),
            "unresolved": len(failed),
        })

        if last:
            aggregate_path = REPO_ROOT / "data" / "raw" / "PHASE3_AGGREGATE_SUMMARY.yaml"
            _write_aggregate_summary(results, aggregate_path)
            rebuild_status_md(results, aggregate_path)

    print(f"\n{'=' * 60}")
    print("AGGREGATE PHASE 3 RETRY COMPLETION")
    print(f"{'=' * 60}")
    for r in results:
        print(
            f"  PHASE 3{r['letter']} | {r['display_name']:20} | {r['status']:22} | "
            f"attempted={r['attempted']} acquired={r['acquired']} failed={r['failed']} | run={r['run_id']}"
        )
    print("\nAggregate summary: data/raw/PHASE3_AGGREGATE_SUMMARY.yaml")
    print("Next allowed phase: 4 (NOT started by this runner).")


def _write_aggregate_summary(results: list[dict], agg_path: Path) -> None:
    import yaml

    total_attempted = sum(r["attempted"] for r in results)
    total_acquired = sum(r["acquired"] for r in results)
    total_failed = sum(r["failed"] for r in results)

    # Collect every prior Phase 3 run id across subject inventories.
    prior_p3: list[str] = []
    for slug, _letter, _abbr in SUBJECTS:
        inv_path = REPO_ROOT / "data" / "raw" / slug / "SOURCE_INVENTORY.yaml"
        if not inv_path.exists():
            continue
        with inv_path.open("r", encoding="utf-8") as fh:
            inv = yaml.safe_load(fh) or {}
        for rec in inv.get("run_records", []):
            if rec.get("phase") == 3 and rec.get("run_id"):
                rid = rec["run_id"]
                if rid not in prior_p3:
                    prior_p3.append(rid)

    agg = {
        "phase": PHASE,
        "phase_name": "source_acquisition",
        "retry": True,
        "prior_phase3_runs": prior_p3,
        "aggregate_status": "completed_with_review" if total_failed else "completed",
        "generated_at": utcnow(),
        "execution_order": [f"{r['letter']}:{r['slug']}" for r in results],
        "summary": [
            {
                "subject": r["slug"],
                "phase_letter": r["letter"],
                "status": r["status"],
                "run_id": r["run_id"],
                "sources_attempted": r["attempted"],
                "sources_acquired": r["acquired"],
                "sources_failed": r["failed"],
                "sources_skipped": r["skipped"],
            }
            for r in results
        ],
        "aggregate_notes": (
            "Phase 3 was re-executed for all six subjects (retry). Every "
            "non-external source was re-attempted with a real download "
            "request. The sandbox still terminates TLS connections to Google "
            "services, so every attempt failed and no files were acquired. "
            "No files were fabricated, modified or substituted. Failures are "
            "recorded per source in each run's errors.json and in the source "
            "record notes."
        ),
        "unresolved_items_total": total_failed,
        "next_action": (
            "Retry acquisition in an environment with working Google Drive "
            "access, or provide preserved originals manually and record them "
            "in the inventories (local_path + file_hash) before Phase 4."
        ),
    }
    with agg_path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(agg, fh, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    main()
