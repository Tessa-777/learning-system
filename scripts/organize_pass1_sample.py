#!/usr/bin/env python3
"""Build the memo-only scheduled sample for Pass 1.

This writes a deterministic, memo-only sample into the organized folder. It uses:
- all official six subject roots under data/raw
- a manual chemistry/physics split from data/raw/physical_science
- same-folder paper+memo pairing only, and never creates a paper record without a memo
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

SUBJECT_ROOTS = {
    'biology': RAW / 'biology',
    'physics': RAW / 'physics',
    'history': RAW / 'history',
    'english': RAW / 'english',
    'ap_mathematics': RAW / 'ap_mathematics',
    'mathematics': RAW / 'mathematics',
}

CHEMISTRY_SPLITS = [
    PHYSICAL / 'PS11 Past Exams' / 'Chemistry',
    PHYSICAL / 'PS11 Past Tests' / 'Chemistry',
]
PHYSICS_SPLITS = [
    PHYSICAL / 'PS11 Past Exams' / 'Physics',
    PHYSICAL / 'PS11 Past Tests' / 'Physics',
]

PAPER_EXTS = {'.pdf', '.doc', '.docx', '.doc', '.odt', '.rtf'}
MEMO_HINTS = (
    'memo', 'memorandum', 'marking guide', 'mark guide', 'mg', 'answers', 'solution'
)


def is_memo(path: Path) -> bool:
    low = path.name.lower()
    return any(h in low for h in MEMO_HINTS)


def clean_org_subjects() -> None:
    # Ensure organized subject roots exist and are clean from previous incomplete scans.
    for subject in list(SUBJECT_ROOTS.keys()) + ['chemistry', 'physics']:
        subject_dir = ORG / subject
        if subject_dir.exists():
            rmtree(subject_dir)
        subject_dir.mkdir(parents=True, exist_ok=True)


def normalize_stem(path: Path) -> str:
    # Equivalent lexical normalization for paper and memo filenames.
    value = path.stem.lower()
    value = re.sub(r'[^a-z0-9]+', ' ', value)
    value = re.sub(r'\b(memo|memorandum|mg|guide|marking|mark|answers|solution)\b', ' ', value)
    value = re.sub(r'\s+', ' ', value)
    return value.strip()


def pair_memo_for_paper(paper: Path, memo_files: list[Path]) -> Path | None:
    # Prefer same folder memo; then same-base lexical overlap; then same directory folder name.
    same_dir = [m for m in memo_files if m.parent == paper.parent]
    if same_dir:
        candidates = []
        pkey = normalize_stem(paper)
        for m in same_dir:
            mkey = normalize_stem(m)
            if pkey == mkey or pkey in mkey or mkey in pkey:
                candidates.append(m)
        if candidates:
            return candidates[0]

    # fallback: same tree and same folder chain by base lexical/key characters
    pkey = normalize_stem(paper)
    candidates = []
    for m in memo_files:
        mkey = normalize_stem(m)
        if pkey in mkey or mkey in pkey:
            candidates.append(m)
    if candidates:
        return candidates[0]

    return None


def copy_pdfs_and_memocopies() -> list[dict]:
    # Holds output records
    records = []

    # 1. Official subjects from data/raw/{subject}
    for subject, source_root in SUBJECT_ROOTS.items():
        if not source_root.exists():
            continue
        papers = sorted([p for p in source_root.rglob('*') if p.is_file() and p.suffix.lower() in PAPER_EXTS and not is_memo(p)], key=lambda x: str(x))
        memos = sorted([m for m in source_root.rglob('*') if m.is_file() and is_memo(m)], key=lambda x: str(x))

        chosen = 0
        for paper in papers:
            memo = pair_memo_for_paper(paper, memos)
            if memo is None:
                continue
            # one paper+memo per pair only
            if chosen >= 15:
                break

            # copy paper and memo into organized subject tree preserving relative structure
            rel_paper = paper.relative_to(source_root)
            rel_memo = memo.relative_to(source_root)
            dst_paper = ORG / subject / rel_paper
            dst_memo = ORG / subject / rel_memo
            dst_paper.parent.mkdir(parents=True, exist_ok=True)
            dst_memo.parent.mkdir(parents=True, exist_ok=True)
            copy2(paper, dst_paper)
            copy2(memo, dst_memo)

            name = paper.name.lower()
            rec = {
                'subject': subject,
                'paper_path': str(dst_paper.relative_to(ROOT)),
                'memo_path': str(dst_memo.relative_to(ROOT)),
                'paper_type': 'paper1' if 'paper 1' in name or 'p1' in name else 'paper2' if 'paper 2' in name or 'p2' in name else 'unknown',
                'exam_board': 'NSC' if 'nsc' in name else 'IEB' if 'ieb' in name else 'internal' if 'school' in name or 'internal' in name else 'unknown',
                'exam_period': 'prelim' if 'prelim' in name else 'june' if 'june' in name else 'nov' if 'nov' in name or 'november' in name else 'unknown',
                'memo_only': True,
                'source_status': 'raw_pdf_or_doc',
                'notes': 'Memo-paired paper copied into organized sample folder.',
            }
            records.append(rec)
            chosen += 1

    # 2. Chemistry and Physics were only partially represented via data/raw/physical_science tree.
    for subject, splits in [('chemistry', CHEMISTRY_SPLITS), ('physics', PHYSICS_SPLITS)]:
        # create one pair per source tree by scanning paper+memo in same folder
        papers = []
        memos = []
        for root in splits:
            if not root.exists():
                continue
            papers.extend([p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in PAPER_EXTS and not is_memo(p)])
            memos.extend([m for m in root.rglob('*') if m.is_file() and is_memo(m)])

        # deterministic sort and keep 15 max per subject
        chosen = 0
        for paper in sorted(papers, key=lambda x: str(x)):
            memo = pair_memo_for_paper(paper, memos)
            if memo is None:
                continue
            if chosen >= 15:
                break

            rel_paper = paper.relative_to(PHYSICAL)
            rel_memo = memo.relative_to(PHYSICAL)
            dst_paper = ORG / subject / rel_paper
            dst_memo = ORG / subject / rel_memo
            dst_paper.parent.mkdir(parents=True, exist_ok=True)
            dst_memo.parent.mkdir(parents=True, exist_ok=True)
            copy2(paper, dst_paper)
            copy2(memo, dst_memo)

            name = paper.name.lower()
            rec = {
                'subject': subject,
                'paper_path': str(dst_paper.relative_to(ROOT)),
                'memo_path': str(dst_memo.relative_to(ROOT)),
                'paper_type': 'paper1' if 'paper 1' in name or 'p1' in name else 'paper2' if 'paper 2' in name or 'p2' in name else 'unknown',
                'exam_board': 'NSC' if 'nsc' in name else 'IEB' if 'ieb' in name else 'internal' if 'school' in name or 'internal' in name else 'unknown',
                'exam_period': 'prelim' if 'prelim' in name else 'june' if 'june' in name else 'nov' if 'nov' in name or 'november' in name else 'unknown',
                'memo_only': True,
                'source_status': 'split_physical_science_pdf_or_doc',
                'notes': 'Chemistry/physics paper from physical_science split into the organized subject folder with memo pairing.',
            }
            records.append(rec)
            chosen += 1

    # Deduplicate any same relative path accidentally added twice.
    seen = set()
    unique_records = []
    for item in records:
        key = item['subject'], item['paper_path'], item['memo_path']
        if key in seen:
            continue
        seen.add(key)
        unique_records.append(item)

    return unique_records


def main() -> None:
    clean_org_subjects()
    records = copy_pdfs_and_memocopies()

    # manifest exactly:
    manifest = {
        'generated_at': '2026-09-11T00:00:00Z',
        'source_of_truth': 'data/raw',
        'memo_only': True,
        'split_physical_science': True,
        'subjects': sorted(list(SUBJECT_ROOTS.keys()) + ['chemistry', 'physics']),
        'strata': {
            'paper_type': ['paper1', 'paper2'],
            'exam_board': ['NSC', 'IEB', 'internal'],
            'exam_period': ['nov', 'june', 'prelim'],
        },
        'records': records,
    }
    (ORG / 'sample_manifest.json').write_text(json.dumps(manifest, indent=2))
    print(f'Wrote {len(records)} memo-only organized records to {ORG / "sample_manifest.json"}')


if __name__ == '__main__':
    main()
