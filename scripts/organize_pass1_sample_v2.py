#!/usr/bin/env python3
"""Build a clean memo-only organized corpus for Pass 1.

Rules:
1. Only papers with a matching memo are copied.
2. Subject roots are split into chemistry and physics from physical_science.
3. A single manifest is written under data/organized/sample_manifest.json.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from shutil import copy2, rmtree

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / 'data' / 'raw'
ORG = ROOT / 'data' / 'organized'
PHYSICAL = RAW / 'physical_science'

SUBJECTS = {
    'biology': [RAW / 'biology'],
    'history': [RAW / 'history'],
    'english': [RAW / 'english'],
    'ap_mathematics': [RAW / 'ap_mathematics'],
    'mathematics': [RAW / 'mathematics'],
    'physics': [
        RAW / 'physics',
        PHYSICAL / 'PS11 Past Exams' / 'Physics',
        PHYSICAL / 'PS11 Past Tests' / 'Physics',
        PHYSICAL / '2025' / 'Physics',
    ],
    'chemistry': [
        PHYSICAL / 'PS11 Past Exams' / 'Chemistry',
        PHYSICAL / 'PS11 Past Tests' / 'Chemistry',
        PHYSICAL / '2025' / 'Chemistry',
    ],
}

PAPER_EXTS = {'.pdf', '.doc', '.docx', '.odt', '.rtf'}
MEMO_HINTS = ('memo', 'memorandum', 'marking guide', 'mark guide', 'mg', 'answers', 'solution')


def is_memo(path: Path) -> bool:
    low = path.name.lower()
    return any(h in low for h in MEMO_HINTS)


def thin_path(path: Path) -> str:
    return str(path.relative_to(ROOT))


def normalized_key(name: str) -> str:
    value = name.lower()
    value = re.sub(r'[^a-z0-9]+', ' ', value)
    value = re.sub(r'\b(memo|memorandum|marking guide|mark guide|mg|answers|solution)\b', ' ', value)
    value = re.sub(r'\s+', ' ', value)
    return value.strip()


def classify_paper_type(name: str) -> str:
    low = name.lower()
    if 'paper 1' in low or 'p1' in low or 'paper1' in low:
        return 'paper1'
    if 'paper 2' in low or 'p2' in low or 'paper2' in low:
        return 'paper2'
    if 'task' in low:
        return 'internal_task'
    return 'unknown'


def classify_exam_board(name: str) -> str:
    low = name.lower()
    if 'ieb' in low:
        return 'IEB'
    if 'nsc' in low:
        return 'NSC'
    if 'internal' in low or 'school' in low:
        return 'internal'
    return 'unknown'


def classify_exam_period(name: str) -> str:
    low = name.lower()
    if 'prelim' in low:
        return 'prelim'
    if 'june' in low:
        return 'june'
    if 'nov' in low or 'november' in low:
        return 'nov'
    return 'unknown'


def clean_organized() -> None:
    # Remove only organized folders we are about to repopulate.
    for p in ['biology', 'physics', 'chemistry', 'history', 'english', 'ap_mathematics', 'mathematics']:
        d = ORG / p
        if d.exists():
            rmtree(d)
        d.mkdir(parents=True, exist_ok=True)


def choose_memo(paper: Path, memo_files: list[Path]) -> Path | None:
    # Strongest rule: same folder paper/memo pairing.
    in_same_folder = [m for m in memo_files if m.parent == paper.parent]
    if in_same_folder:
        pk = normalized_key(paper.stem)
        for m in sorted(in_same_folder, key=lambda x: len(x.name)):
            mk = normalized_key(m.stem)
            if pk == mk or pk in mk or mk in pk:
                return m

    # Same exam location fallback by approximate raw token overlap.
    pk = normalized_key(paper.stem)
    candidates = []
    for m in memo_files:
        mk = normalized_key(m.stem)
        if pk in mk or mk in pk:
            candidates.append(m)
    if candidates:
        return candidates[0]

    return None


def copy_and_pair(source_roots: list[Path], subject: str, limit: int = 15) -> list[dict]:
    records = []
    paper_files = []
    memo_files = []

    for root in source_roots:
        if not root.exists():
            continue
        paper_files.extend([p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in PAPER_EXTS and not is_memo(p)])
        memo_files.extend([m for m in root.rglob('*') if m.is_file() and is_memo(m)])

    paper_files = sorted(list({str(p): p for p in paper_files}.values()), key=lambda p: str(p))
    memo_files = sorted(list({str(m): m for m in memo_files}.values()), key=lambda m: str(m))

    for paper in paper_files:
        if len(records) >= limit:
            break
        memo = choose_memo(paper, memo_files)
        if memo is None:
            continue

        # Sanity: skip if memo path points to same file path or very unsafe
        if memo == paper:
            continue

        rel_paper = paper.relative_to(ROOT) if paper.is_relative_to(ROOT) else paper
        rel_memo = memo.relative_to(ROOT) if memo.is_relative_to(ROOT) else memo

        # For explicit file copy into organized tree, use relative route from source root.
        # The exact file source remains the raw object's parent path.
        target_paper = ORG / subject / paper.name
        target_memo = ORG / subject / memo.name

        # preserve a simple same-tree arrangement by using original leaf names only
        target_paper.parent.mkdir(parents=True, exist_ok=True)
        target_memo.parent.mkdir(parents=True, exist_ok=True)

        # if the same filename exists in multiple source folders, keep the candidate in sorted deterministic order
        copy2(paper, target_paper)
        copy2(memo, target_memo)

        name = paper.name.lower()
        rec = {
            'subject': subject,
            'paper_path': str(target_paper.relative_to(ROOT)),
            'memo_path': str(target_memo.relative_to(ROOT)),
            'paper_type': classify_paper_type(name),
            'exam_board': classify_exam_board(name),
            'exam_period': classify_exam_period(name),
            'memo_only': True,
            'source_status': 'raw_pdf_or_doc',
            'notes': 'Paper kept only when paired with a matching memo from the same subject tree.',
        }
        records.append(rec)

    return records


def main() -> None:
    clean_organized()
    manifest_records = []

    for subject, roots in SUBJECTS.items():
        records = copy_and_pair(roots, subject, limit=15)
        manifest_records.extend(records)

    manifest = {
        'generated_at': '2026-09-11T00:00:00Z',
        'source_of_truth': 'data/raw',
        'memo_only': True,
        'split_physical_science': True,
        'subjects': list(SUBJECTS.keys()),
        'strata': {
            'paper_type': ['paper1', 'paper2'],
            'exam_board': ['NSC', 'IEB', 'internal'],
            'exam_period': ['nov', 'june', 'prelim'],
        },
        'records': manifest_records,
    }
    (ORG / 'sample_manifest.json').write_text(json.dumps(manifest, indent=2))
    print(f'Wrote {len(manifest_records)} memo-only organized records.')


if __name__ == '__main__':
    main()
