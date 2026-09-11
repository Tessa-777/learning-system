#!/usr/bin/env python3
"""Create a deterministic, memo-only organized sample for Pass 1.

Policy:
- Every selected paper must have a matching memorandum/marking guide.
- Physics and chemistry records are split from the physical_science tree.
- The organized subject folders are written under data/organized.
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

RAW_SUBJECT_MAP = {
    'biology': [RAW / 'biology'],
    'history': [RAW / 'history'],
    'english': [RAW / 'english'],
    'ap_mathematics': [RAW / 'ap_mathematics'],
    'mathematics': [RAW / 'mathematics'],
}

PHYSICAL_SUBJECT_MAP = {
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
CURRICULUM_HINTS = ('curriculum', 'syllabus', 'source booklet', 'source_booklet', 'guide', 'reference', 'topic')


def is_memo(path: Path) -> bool:
    low = path.name.lower()
    return any(token in low for token in MEMO_HINTS)


def is_curriculum(path: Path) -> bool:
    if not path.is_file() or path.suffix.lower() not in PAPER_EXTS:
        return False
    low = path.name.lower()
    return any(token in low for token in CURRICULUM_HINTS)


def is_paper(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in PAPER_EXTS and not is_memo(path) and not is_curriculum(path)


def normalized_key(name: str) -> str:
    value = name.lower()
    value = re.sub(r'[^a-z0-9]+', ' ', value)
    value = re.sub(r'\b(memo|memorandum|marking guide|mark guide|mg|answers|solution)\b', ' ', value)
    value = re.sub(r'\s+', ' ', value)
    return value.strip()


def paper_class(name: str) -> str:
    lower = name.lower()
    if 'paper 1' in lower or 'p1' in lower or 'paper1' in lower:
        return 'paper1'
    if 'paper 2' in lower or 'p2' in lower or 'paper2' in lower:
        return 'paper2'
    if 'task' in lower:
        return 'internal_task'
    return 'unknown'


def board_class(name: str) -> str:
    lower = name.lower()
    if 'ieb' in lower:
        return 'IEB'
    if 'nsc' in lower:
        return 'NSC'
    if 'internal' in lower or 'school' in lower:
        return 'internal'
    return 'unknown'


def period_class(name: str) -> str:
    lower = name.lower()
    if 'prelim' in lower:
        return 'prelim'
    if 'june' in lower:
        return 'june'
    if 'nov' in lower or 'november' in lower:
        return 'nov'
    return 'unknown'


def clean_organized() -> None:
    for folder in ['biology', 'physics', 'chemistry', 'history', 'english', 'ap_mathematics', 'mathematics']:
        p = ORG / folder
        if p.exists():
            rmtree(p)
        p.mkdir(parents=True, exist_ok=True)


def pair_memo(paper: Path, memo_set: list[Path]) -> Path | None:
    # same-folder memo best-case
    same_dir = [m for m in memo_set if m.parent == paper.parent]
    if same_dir:
        pk = normalized_key(paper.stem)
        for memo in sorted(same_dir, key=lambda x: len(x.name)):
            mk = normalized_key(memo.stem)
            overlap = len(set(pk.split()) & set(mk.split()))
            if overlap >= 2 or pk == mk or pk in mk or mk in pk:
                return memo

    # cross-folder fallback: same lexical stem in same subject tree
    pk = normalized_key(paper.stem)
    candidates = []
    for memo in memo_set:
        mk = normalized_key(memo.stem)
        overlap = len(set(pk.split()) & set(mk.split()))
        if overlap >= 2 or pk == mk or pk in mk or mk in pk:
            candidates.append((overlap, memo))
    if candidates:
        candidates.sort(reverse=True)
        return candidates[0][1]

    return None


def source_subject_collection(subject: str, roots: list[Path], cap: int = 15) -> list[dict]:
    papers = []
    memos = []
    curricula = []

    # Collect evidence from all configured roots for the subject.
    for root in roots:
        if not root.exists():
            continue
        papers.extend([p for p in root.rglob('*') if is_paper(p)])
        memos.extend([m for m in root.rglob('*') if m.is_file() and is_memo(m)])
        # Curriculum/reference files are non-paper, non-memo docs that advertise curriculum/syllabus/booklet/reference.
        curricula.extend([c for c in root.rglob('*') if c.is_file() and c.suffix.lower() in PAPER_EXTS and is_curriculum(c)])

    papers = sorted(list({str(p): p for p in papers}.values()), key=lambda p: str(p))
    memos = sorted(list({str(m): m for m in memos}.values()), key=lambda m: str(m))
    curricula = sorted(list({str(c): c for c in curricula}.values()), key=lambda c: str(c))

    # Copy curriculum/reference evidence into the subject curriculum bucket.
    curriculum_targets = []
    for ref in curricula[:3]:
        tgt = ORG / subject / 'curriculum' / ref.name
        tgt.parent.mkdir(parents=True, exist_ok=True)
        if not tgt.exists():
            try:
                copy2(ref, tgt)
            except Exception:
                pass
        curriculum_targets.append(str(tgt.relative_to(ROOT)))

    records = []
    selected = 0

    for paper in papers:
        if selected >= cap:
            break
        memo = pair_memo(paper, memos)

        # History may retain papers even if there is no matching memo; curriculum evidence becomes the fallback.
        if memo is None and subject != 'history':
            continue

        # Normalize path for copy: copy every paper straight into organized subject folder.
        target_paper = ORG / subject / paper.name
        target_paper.parent.mkdir(parents=True, exist_ok=True)
        if not target_paper.exists():
            try:
                copy2(paper, target_paper)
            except Exception:
                pass

        if memo:
            target_memo = ORG / subject / memo.name
            target_memo.parent.mkdir(parents=True, exist_ok=True)
            if not target_memo.exists():
                try:
                    copy2(memo, target_memo)
                except Exception:
                    pass
            memo_path = str(target_memo.relative_to(ROOT))
            memo_only = True
            notes = 'Memo-backed paper selected from the subject source inventory and copied into organized sample scope.'
            source_status = 'raw_pdf_or_doc'
        else:
            memo_path = None
            memo_only = False
            notes = 'History paper retained without memo and paired with curriculum/reference evidence in the organized scope.'
            source_status = 'paper_only_history_with_curriculum'

        # Record the curriculum/reference trace where we found it.
        record = {
            'subject': subject,
            'paper_path': str(target_paper.relative_to(ROOT)),
            'memo_path': memo_path,
            'paper_type': paper_class(paper.name.lower()),
            'exam_board': board_class(paper.name.lower()),
            'exam_period': period_class(paper.name.lower()),
            'memo_only': memo_only,
            'source_status': source_status,
            'notes': notes,
        }
        if curriculum_targets:
            record['curriculum_path'] = curriculum_targets[0]
            record['curriculum_source'] = 'source_reference_tree'

        records.append(record)
        selected += 1

    return records


def main() -> None:
    clean_organized()
    manifest_records = []

    # Official six subjects from raw inventory
    for subject, roots in RAW_SUBJECT_MAP.items():
        manifest_records.extend(source_subject_collection(subject, roots, cap=15))

    # Split chemistry and physics from physical_science into those same organized folders.
    for subject, roots in PHYSICAL_SUBJECT_MAP.items():
        manifest_records.extend(source_subject_collection(subject, roots, cap=15))

    # De-duplicate by paper path and memo path
    dedup = []
    seen = set()
    for rec in manifest_records:
        key = (rec['subject'], rec['paper_path'], rec['memo_path'])
        if key in seen:
            continue
        seen.add(key)
        dedup.append(rec)

    manifest = {
        'generated_at': '2026-09-11T00:00:00Z',
        'source_of_truth': 'data/raw',
        'memo_only': True,
        'split_physical_science': True,
        'subjects': sorted(list(RAW_SUBJECT_MAP.keys()) + list(PHYSICAL_SUBJECT_MAP.keys())),
        'strata': {
            'paper_type': ['paper1', 'paper2'],
            'exam_board': ['NSC', 'IEB', 'internal'],
            'exam_period': ['nov', 'june', 'prelim'],
        },
        'records': dedup,
    }
    (ORG / 'sample_manifest.json').write_text(json.dumps(manifest, indent=2))
    print(f'Wrote {len(dedup)} memo-only organized records to {ORG / "sample_manifest.json"}')


if __name__ == '__main__':
    main()
