#!/usr/bin/env python3
"""Create a memo-only, machine-readable Pass 1-ready organisational sample.

This helper:
- scans the raw subject folders for paper+memo pairs that are explicit enough to keep;
- copies the physical_science Chemistry/Physics material into organized chemistry/physics folders;
- writes a machine-readable manifest that stays conservative and memo-only.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from shutil import copy2


ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / 'data' / 'raw'
ORGANIZED = ROOT / 'data' / 'organized'
PHYSICAL_SCIENCE = RAW / 'physical_science'

SUBJECTS = {
    'biology': RAW / 'biology',
    'physics': RAW / 'physics',
    'history': RAW / 'history',
    'english': RAW / 'english',
    'ap_mathematics': RAW / 'ap_mathematics',
    'mathematics': RAW / 'mathematics',
}

ORGANIZED_SUBJECTS = [
    'biology', 'physics', 'chemistry', 'history', 'english', 'ap_mathematics', 'mathematics'
]

PAPER_EXTS = {'.pdf', '.doc', '.docx', '.odt', '.rtf'}
MEMO_HINTS = ('memo', 'memorandum', 'marking guide', 'mark guide', 'mg', 'answers', 'solution')


def make_subject_root_dirs() -> None:
    for sub in ORGANIZED_SUBJECTS:
        (ORGANIZED / sub).mkdir(parents=True, exist_ok=True)


def is_memo(path: Path) -> bool:
    low = path.name.lower()
    return any(h in low for h in MEMO_HINTS)


def norm(value: str) -> str:
    value = value.lower()
    value = re.sub(r'[^a-z0-9]+', ' ', value)
    value = re.sub(r'\b(mg|memo|memorandum|marking guide|mark guide|answers|solution)\b', ' ', value)
    value = re.sub(r'\s+', ' ', value).strip()
    return value


def stem_key(path: Path) -> str:
    return norm(path.stem)


def classify_exam_period(name: str) -> str:
    low = name.lower()
    if 'prelim' in low:
        return 'prelim'
    if 'june' in low:
        return 'june'
    if 'nov' in low or 'november' in low:
        return 'nov'
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


def classify_paper_type(name: str) -> str:
    low = name.lower()
    if 'paper 2' in low or 'p2' in low or 'paper2' in low:
        return 'paper2'
    if 'paper 1' in low or 'p1' in low or 'paper1' in low:
        return 'paper1'
    if 'task' in low:
        return 'internal_task'
    return 'unknown'


def copy_physical_science_split() -> None:
    """Manually inspect and copy known chemistry/physics folders from physical_science into organized subject folders."""
    chemistry_roots = [
        PHYSICAL_SCIENCE / 'PS11 Past Exams' / 'Chemistry',
        PHYSICAL_SCIENCE / 'PS11 Past Tests' / 'Chemistry',
        PHYSICAL_SCIENCE / '2025' / 'Chemistry',
    ]
    physics_roots = [
        PHYSICAL_SCIENCE / 'PS11 Past Exams' / 'Physics',
        PHYSICAL_SCIENCE / 'PS11 Past Tests' / 'Physics',
        PHYSICAL_SCIENCE / '2025' / 'Physics',
    ]

    def copy_tree(src_root: Path, dst_subject: str) -> None:
        if not src_root.exists():
            return
        for file in src_root.rglob('*'):
            if file.is_file() and file.suffix.lower() in PAPER_EXTS:
                rel = file.relative_to(src_root)
                target = ORGANIZED / dst_subject / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                copy2(file, target)

    for root in chemistry_roots:
        copy_tree(root, 'chemistry')
    for root in physics_roots:
        copy_tree(root, 'physics')


def construct_manifest() -> list[dict]:
    records = []
    for subject, subject_root in SUBJECTS.items():
        if not subject_root.exists():
            continue
        paper_files = sorted([p for p in subject_root.rglob('*') if p.is_file() and p.suffix.lower() in PAPER_EXTS and not is_memo(p)])
        memo_files = sorted([p for p in subject_root.rglob('*') if p.is_file() and is_memo(p)])

        for paper in paper_files:
            # pair existing memo candidates in same folder first
            memo_same_dir = [m for m in memo_files if m.parent == paper.parent]
            memo = None
            for matched in memo_same_dir:
                # pair by lexical overlap or same stem base
                if stem_key(matched).startswith(stem_key(paper)) or stem_key(paper).startswith(stem_key(matched)) or stem_key(paper).replace('paper1', '').replace('paper2', '') == stem_key(matched).replace('paper1', '').replace('paper2', ''):
                    memo = matched
                    break
            if memo is None:
                # if no same-folder memo, continue to satisfy memo-only requirement
                continue

            # copy the pair into organized subject folder, preserving relative structure and pairing by directory
            rel_paper = paper.relative_to(subject_root)
            rel_memo = memo.relative_to(subject_root)
            target_paper = ORGANIZED / subject / rel_paper
            target_memo = ORGANIZED / subject / rel_memo
            target_paper.parent.mkdir(parents=True, exist_ok=True)
            target_memo.parent.mkdir(parents=True, exist_ok=True)
            copy2(paper, target_paper)
            copy2(memo, target_memo)

            # produce a manifest record
            paper_name = paper.name.lower()
            paper_type = classify_paper_type(paper_name)
            board = classify_exam_board(paper_name)
            period = classify_exam_period(paper_name)

            records.append({
                'subject': subject,
                'paper_path': str(target_paper.relative_to(ROOT)),
                'memo_path': str(target_memo.relative_to(ROOT)),
                'paper_type': paper_type,
                'exam_board': board,
                'exam_period': period,
                'year': paper.parent.name,
                'memo_only': True,
                'source_status': 'raw_pdf_or_doc',
                'notes': 'Memo-backed paper sample copied into organized subject folder.',
            })

    # Keep up to 15 per subject and produce a stable list
    per_subject = {}
    for rec in records:
        per_subject.setdefault(rec['subject'], []).append(rec)

    final_records = []
    for subject in list(SUBJECTS.keys()):
        selected = per_subject.get(subject, [])[:15]
        final_records.extend(selected)

    return final_records


if __name__ == '__main__':
    make_subject_root_dirs()
    copy_physical_science_split()
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
        'records': construct_manifest(),
    }
    (ORGANIZED / 'sample_manifest.json').write_text(json.dumps(manifest, indent=2))
    print(f'Created organized intake at {ORGANIZED}.')
    print(f'Memo-backed sample manifest written to {ORGANIZED / "sample_manifest.json"}.')
