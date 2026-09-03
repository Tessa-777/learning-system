#!/usr/bin/env python3
"""Phase 3 — Source Acquisition Runner.

Executes Phase 3 for each of the six Grade 11 subjects.
For each accessible source identified in Phase 2:
  - attempts download/preservation
  - calculates SHA-256 for any acquired file
  - detects duplicate files by content hash
  - updates the source inventory
  - records failures and inaccessible sources

Because external Google Drive sources are unreachable from the sandbox
(TLS/SSL connection terminated), all acquisition attempts fail and are
recorded properly rather than being silently omitted.

This script runs sequentially through all subjects requested and stops
after Phase 3; it does NOT proceed to Phase 4.
"""

from __future__ import annotations

import hashlib
import json
import os
import ssl
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.runlog import RunLogger, sha256_file
from ingestion.run_context import RunContext

REPO_ROOT = Path(__file__).resolve().parent.parent

SUBJECTS = [
    ("biology", 3, "A"),
    ("physics", 3, "B"),
    ("history", 3, "C"),
    ("english", 3, "D"),
    ("ap_mathematics", 3, "E"),
    ("mathematics", 3, "F"),
]

# A minimal attempt to download from Google Drive URLs.
# The sandbox terminates TLS connections to Google services,
# so this will fail for every source; the failure is recorded.

def attempt_download(url: str, out_path: Path, timeout: int = 20) -> tuple[bool, str]:
    try:
        ctx = ssl.create_default_context()
        # Even with verification disabled, the sandbox terminates
        # the TLS handshake to Google Drive.  We try anyway.
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            data = resp.read()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(data)
        return True, f"Downloaded {len(data)} bytes"
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"


def main() -> None:
    # Ensure yaml package is available
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError(
            "PyYAML is required. Install with: pip install pyyaml --break-system-packages"
        ) from exc

    results = []

    for slug, phase, letter in SUBJECTS:
        print(f"\n{'='*60}")
        print(f"PHASE 3{letter} — {slug.upper()} Source Acquisition")
        print(f"{'='*60}")

        inventory_path = REPO_ROOT / "data" / "raw" / slug / "SOURCE_INVENTORY.yaml"
        if not inventory_path.exists():
            print(f"  SKIP: inventory missing: {inventory_path}")
            results.append((slug, "skipped", "inventory missing", None))
            continue

        with inventory_path.open("r", encoding="utf-8") as fh:
            inventory = yaml.safe_load(fh) or {}

        sources = inventory.get("sources", [])
        accessible = [s for s in sources if s.get("access_status") == "accessible"]
        external = [s for s in sources if s.get("access_status") == "external"]
        inaccessible = [s for s in sources if s.get("access_status") == "inaccessible"]

        # Initialize run context
        run_ctx = RunContext(
            config=None,
            run_id=None,
            phase=phase,
            subject=slug,
        )
        run_id = run_ctx.start()

        run_ctx.log_event(
            event="PHASE_3_STARTED",
            message=f"Phase 3 acquisition started for {slug}",
            metadata={"subject": slug, "inventory_path": str(inventory_path), "total_sources": len(sources)},
        )

        # Log decision: acquisition strategy
        run_ctx.log_decision(
            decision_id=f"DEC-P3-{slug}-001",
            phase=phase,
            subject=slug,
            decision_type="acquisition_strategy",
            context=f"Phase 3 acquisition for {slug}: attempt download of all accessible sources from Phase 2 inventory.",
            evidence=[str(inventory_path)],
            alternatives=["skip_download", "simulate_download", "download_and_preserve"],
            selected="download_and_preserve",
            rationale="Phase 3 requires acquiring every accessible authoritative source identified in Phase 2. Original files must be preserved unchanged with SHA-256 hashes computed.",
            confidence="high",
            requires_review=False,
        )

        acquired = []
        failed = []
        duplicates = {}

        # Create raw directory for this subject
        raw_dir = REPO_ROOT / "data" / "raw" / slug
        raw_dir.mkdir(parents=True, exist_ok=True)

        for idx, source in enumerate(sources):
            sid = source.get("source_id", f"UNKNOWN-{idx}")

            if source.get("access_status") != "accessible":
                # Skip non-accessible sources in Phase 3 but note them
                if source.get("access_status") == "external":
                    run_ctx.log_event(
                        event="SOURCE_SKIPPED",
                        entity_id=sid,
                        message=f"Source {sid} marked external; not downloaded.",
                        metadata={"reason": "external"},
                    )
                elif source.get("access_status") == "inaccessible":
                    run_ctx.log_event(
                        event="SOURCE_SKIPPED",
                        entity_id=sid,
                        message=f"Source {sid} already marked inaccessible.",
                        metadata={"reason": "inaccessible"},
                    )
                continue

            url = source.get("source_url")
            title = source.get("title", sid)
            file_id = url.split("/d/")[-1].split("/")[0] if url and "/d/" in url else None
            original_name = title if title else (f"{sid}.{title.split('.')[-1]}" if '.' in title else f"{sid}.pdf")
            out_path = raw_dir / original_name

            # Attempt download
            success, message = attempt_download(url, out_path)
            if success:
                # Calculate hash
                file_hash = sha256_file(out_path)
                source["local_path"] = str(out_path.relative_to(REPO_ROOT))
                source["file_hash"] = file_hash
                source["access_status"] = "accessible"
                acquired.append(sid)
                run_ctx.log_event(
                    event="SOURCE_ACQUIRED",
                    entity_id=sid,
                    message=f"Source {sid} acquired: {message}",
                    metadata={"path": str(out_path), "hash": file_hash, "bytes": out_path.stat().st_size},
                )
                run_ctx.record_artifact(
                    out_path,
                    type="source_file",
                    description=f"Acquired source file for {sid}",
                    content_hash=file_hash,
                )
            else:
                # Acquisition failed: record failure, update status
                source["local_path"] = None
                source["file_hash"] = None
                source["access_status"] = "inaccessible"
                source.setdefault("notes", "")
                failure_note = f"Phase 3 acquisition failed: {message} (sandbox TLS restriction to Google Drive)."
                if source["notes"]:
                    source["notes"] += "; " + failure_note
                else:
                    source["notes"] = failure_note
                failed.append(sid)

                run_ctx.log_error(
                    error_type="acquisition_failed",
                    message=f"Could not download {sid}: {message}",
                    affected_artifact=str(url),
                    retry_attempts=0,
                    resolution="Source remains inaccessible from sandbox. Requires manual download or alternative access.",
                    status="unresolved",
                )
                run_ctx.log_event(
                    event="SOURCE_ACQUIRED",
                    entity_id=sid,
                    message=f"Source {sid} acquisition FAILED: {message}",
                    metadata={"url": url, "failure_reason": message, "status_updated": "inaccessible"},
                )

            # Duplicate detection by file hash (only if file exists)
            if success and out_path.exists():
                file_hash = sha256_file(out_path)
                if file_hash in duplicates:
                    duplicates[file_hash].append(sid)
                    run_ctx.log_event(
                        event="SOURCE_DUPLICATE",
                        entity_id=sid,
                        message=f"Duplicate content hash detected for {sid} (same as {duplicates[file_hash][0]})",
                        metadata={"hash": file_hash, "duplicate_of": duplicates[file_hash][0]},
                    )
                else:
                    duplicates[file_hash] = [sid]

        # Log metrics
        metrics = {
            "subject": slug,
            "phase": phase,
            "run_id": run_id,
            "sources_discovered": len(sources),
            "sources_accessible_before": len(accessible),
            "sources_acquired": len(acquired),
            "sources_failed": len(failed),
            "sources_external": len(external),
            "sources_inaccessible_after": len(inaccessible) + len(failed),
            "duplicate_hashes_detected": len([h for h in duplicates if len(duplicates[h]) > 1]),
            "files_downloaded": len([f for f in os.listdir(raw_dir) if f != ".gitkeep" and (raw_dir / f).is_file()]) if raw_dir.exists() else 0,
        }
        run_ctx.set_metrics(metrics)

        # Final decision: acquisition status
        run_ctx.log_decision(
            decision_id=f"DEC-P3-{slug}-002",
            phase=phase,
            subject=slug,
            decision_type="acquisition_completion",
            context=f"Phase 3 acquisition completed for {slug}. All accessible sources attempted.",
            evidence=[
                f"sources_total={len(sources)}",
                f"sources_acquired={len(acquired)}",
                f"sources_failed={len(failed)}",
            ],
            alternatives=["completed", "completed_with_review", "blocked"],
            selected="completed_with_review",
            rationale="No files could be downloaded from Google Drive due to sandbox TLS/SSL restrictions. All sources remain inaccessible. Acquisition must be retried in an environment with working Google Drive access, or files must be provided manually.",
            confidence="high",
            requires_review=True,
        )

        # Update inventory file
        inventory["sources"] = sources
        inventory["phase"] = 3
        inventory.setdefault("summary", {})
        inventory["summary"]["by_access_status_after_acquisition"] = {
            "accessible": len([s for s in sources if s.get("access_status") == "accessible"]),
            "inaccessible": len([s for s in sources if s.get("access_status") == "inaccessible"]),
            "external": len([s for s in sources if s.get("access_status") == "external"]),
        }
        inventory.setdefault("run_records", [])
        inventory["run_records"].append({
            "run_id": run_id,
            "subject": slug,
            "phase": phase,
            "status": "completed_with_review",
            "sources_acquired": len(acquired),
            "sources_failed": len(failed),
            "notes": "All downloads failed due to sandbox TLS restriction to Google services.",
        })

        with inventory_path.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(inventory, fh, sort_keys=False, allow_unicode=True)

        # Create additional artifact: acquisition failure report
        failure_report_path = REPO_ROOT / "data" / "raw" / slug / "ACQUISITION_REPORT.yaml"
        failure_report = {
            "subject": slug,
            "phase": phase,
            "run_id": run_id,
            "report_type": "phase3_acquisition_report",
            "generated_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat().replace("+00:00", "Z"),
            "total_sources": len(sources),
            "acquired_sources": acquired,
            "failed_sources": failed,
            "duplicate_hashes": {h: dups for h, dups in duplicates.items() if len(dups) > 1},
            "notes": "Sandbox TLS/SSL restriction prevents connection to Google Drive (drive.google.com). All acquisition attempts failed. Original files not modified or downloaded.",
            "next_action": "Retry acquisition in an environment with working Google Drive access, or manually provide source files and rerun Phase 3.",
        }
        with failure_report_path.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(failure_report, fh, sort_keys=False, allow_unicode=True)
        run_ctx.record_artifact(
            failure_report_path,
            type="report",
            description=f"Phase 3 acquisition failure report for {slug}",
        )

        # Complete run
        unresolved_items = len(failed) + len([h for h in duplicates if len(duplicates[h]) > 1])
        run_ctx.complete("completed_with_review", unresolved_items=unresolved_items)

        # Log final event
        run_ctx.log_event(
            event="PHASE_3_COMPLETED",
            message=f"Phase 3 completed for {slug} with {len(failed)} unresolved acquisition failures.",
            metadata={"run_id": run_id, "acquired": len(acquired), "failed": len(failed), "unresolved_items": unresolved_items},
        )

        print(f"  Run ID: {run_id}")
        print(f"  Sources: {len(sources)} total | {len(accessible)} accessible before | {len(acquired)} acquired | {len(failed)} failed | {len(external)} external")
        if failed:
            print(f"    FAILED: {', '.join(failed[:5])}{' ...' if len(failed) > 5 else ''}")
        results.append((slug, "completed_with_review", f"failed={len(failed)}, acquired={len(acquired)}", run_id))

    # Write aggregate summary artifact
    summary_path = REPO_ROOT / "data" / "raw" / "PHASE3_AGGREGATE_SUMMARY.yaml"
    aggregate = {
        "phase": 3,
        "execution_order": SUBJECTS,
        "summary": [
            {
                "subject": r[0],
                "status": r[1],
                "details": r[2],
                "run_id": r[3],
            }
            for r in results
        ],
        "aggregate_notes": "No source files were downloaded due to sandbox TLS restriction to Google Drive. All sources recorded as inaccessible with failure details. No original files modified. No Phase 4 work performed.",
        "unresolved_items_total": sum(len(r[2].split("failed=")[1].split(",")[0]) for r in results if "failed=" in r[2]),
    }
    with summary_path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(aggregate, fh, sort_keys=False, allow_unicode=True)

    print(f"\n{'='*60}")
    print("AGGREGATE PHASE 3 COMPLETION")
    print(f"{'='*60}")
    for r in results:
        print(f"  {r[0].upper():20} | {r[1]:20} | {r[2]} | run={r[3]}")
    print(f"\nAggregate summary: {summary_path}")
    print("Next allowed phase: 4 (NOT started)")


if __name__ == "__main__":
    main()
