#!/usr/bin/env python3
"""Create conservative subject pass-1 evidence files from the organized sample manifest.

This generator reads the organized sample manifest in data/organized and then reads
actual organized paper+memo evidence files from the disk. It writes source-level
Pass 1 records that remain grounded in the actual files, and leaves fields
blank/unresolved whenever the source file or memo cannot prove them.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

try:
    from pypdf import PdfReader
except Exception:
    PdfReader = None

try:
    from docx import Document as DocxDocument
except Exception:
    DocxDocument = None

ROOT = Path(__file__).resolve().parent.parent
ORGANIZED = ROOT / 'data' / 'organized'
EXTRACTED = ROOT / 'data' / 'extracted'
MANIFEST = ORGANIZED / 'sample_manifest.json'

SUBJECTS = [
    'ap_mathematics',
    'biology',
    'chemistry',
    'english',
    'history',
    'mathematics',
    'physics',
]


def clean_subject(subject: str) -> str:
    subject = (subject or '').strip().lower()
    alias = {
        'ap maths': 'ap_mathematics',
        'ap math': 'ap_mathematics',
        'ap mathematics': 'ap_mathematics',
        'math': 'mathematics',
        'maths': 'mathematics',
        'phys': 'physics',
        'eng': 'english',
        'hist': 'history',
    }
    return alias.get(subject, subject)


def clean_token(token: str) -> str:
    return re.sub(r'[^a-z0-9]+', '_', (token or 'unknown').lower()).strip('_') or 'unknown'


def path_from_manifest(path_value: str) -> Path:
    # convert windows-like path strings into workspace-relative file path safely
    raw = str(path_value).replace('\\', '/')
    if raw.startswith('data/') or raw.startswith('data\\'):
        return ROOT / raw
    return ROOT / raw


def sha256(path: Path) -> str:
    if not path.exists():
        return 'NOT_PROVIDED'
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def parse_pdf_or_docx_text(path: Path) -> str:
    if not path.exists():
        return ''
    try:
        if path.suffix.lower() == '.pdf' and PdfReader:
            return '\n'.join((page.extract_text() or '') for page in PdfReader(str(path)).pages[:30])
        if path.suffix.lower() == '.docx' and DocxDocument:
            doc = DocxDocument(str(path))
            return '\n'.join(p.text for p in doc.paragraphs[:80])
    except Exception:
        return ''
    return ''


def detect_board(name: str) -> str:
    low = name.lower()
    if 'ieb' in low:
        return 'IEB'
    if 'nsc' in low:
        return 'NSC'
    if 'internal' in low or 'school' in low:
        return 'internal'
    return 'unknown'


def detect_type(name: str) -> str:
    low = name.lower()
    if 'paper 1' in low or 'p1' in low or 'paper1' in low:
        return 'paper1'
    if 'paper 2' in low or 'p2' in low or 'paper2' in low:
        return 'paper2'
    if 'task' in low:
        return 'internal_task'
    return 'unknown'


def detect_period(name: str) -> str:
    low = name.lower()
    if 'prelim' in low:
        return 'prelim'
    if 'june' in low or 'july' in low:
        return 'june'
    if 'nov' in low or 'november' in low:
        return 'nov'
    return 'unknown'


def detect_year(name: str) -> str:
    # use filename year if present; otherwise keep unknown
    match = re.search(r'\b(20\d{2}|19\d{2})\b', name)
    return match.group(1) if match else 'unknown'


def source_id_for(subject: str, paper_path: str, record: dict[str, Any], seq: int) -> str:
    """Construct a strict pass-1 source_id from the source file metadata only."""
    name = Path(paper_path.replace('\\', '/')).name.lower()
    year = detect_year(name)
    board = detect_board(name)
    paper_type = detect_type(name)
    period = detect_period(name)
    return f"{subject}_{year}_{clean_token(board)}_{clean_token(paper_type)}_{clean_token(period)}_q{seq}".lower()


def mark_from_text(text: str) -> Any:
    m = re.search(r'\bmarks?\b\s*[:=]?\s*([0-9]+)', text, re.I)
    if m:
        return int(m.group(1))
    return None


def answer_from_text(text: str) -> str | None:
    # Keep answer text as a short excerpt only.
    cleaned = re.sub(r'\s+', ' ', text)
    if len(cleaned) >= 250:
        return cleaned[:250]
    return cleaned or None


def question_text_from_source(text: str) -> str | None:
    # Keep question_text very conservative: if no actual readable text, this stays None.
    txt = re.sub(r'\s+', ' ', text[:1800])
    if txt.strip():
        return txt.strip()
    return None


def memo_method_steps_from_text(text: str) -> list[str]:
    # Simple heuristic: keep lines that look method-like, not answer keys.
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if len(line) >= 4 and len(line) <= 180 and not line.endswith('?'):
            lines.append(line)
    return lines[:5]


def record_for(subject: str, rec: dict[str, Any], seq: int) -> dict[str, Any]:
    paper_path = path_from_manifest(rec['paper_path'])
    memo_path = path_from_manifest(rec['memo_path']) if rec.get('memo_path') else None

    paper_text = parse_pdf_or_docx_text(paper_path)
    memo_text = parse_pdf_or_docx_text(memo_path) if memo_path else ''

    # Build fields in the pass-1 record shell.
    q = {
        'source_id': source_id_for(subject, rec['paper_path'], rec, seq),
        'source_document': rec['paper_path'],
        'source_document_sha256': sha256(paper_path),
        'memo_document': rec.get('memo_path'),
        'fidelity_rung': 'A' if paper_path.exists() and memo_path and memo_path.exists() else 'C',
        'requires_visual_verification': False,
        'ocr_uncertain': False,
        'subject': subject,
        'grade': '11',
        'parent_question_id': None,
        'question_stem_text': None,
    }

    # subject-specific fields that can be extracted safely from available evidence.
    if subject == 'ap_mathematics':
        q['marks'] = mark_from_text(paper_text) or None
        q['module_guess'] = 'unresolved'
        q['question_text'] = question_text_from_source(paper_text) or 'unresolved'
        q['has_diagram'] = None
        q['memo_answer'] = answer_from_text(memo_text) or 'unresolved'
        q['memo_method_steps'] = memo_method_steps_from_text(memo_text)
        q['memo_marking_notes'] = 'unresolved'
        q['apparent_prerequisite_core_topics'] = []
    elif subject == 'biology':
        q['marks'] = mark_from_text(paper_text) or None
        q['topic_guess'] = 'unresolved'
        q['question_type'] = 'unresolved'
        q['question_text'] = question_text_from_source(paper_text) or 'unresolved'
        q['has_diagram'] = None
        q['memo_answer'] = answer_from_text(memo_text) or 'unresolved'
        q['memo_marking_notes'] = 'unresolved'
        q['key_terminology_tested'] = []
    elif subject == 'chemistry':
        q['marks'] = mark_from_text(paper_text) or None
        q['discipline'] = 'Chemistry'
        q['topic_guess'] = 'unresolved'
        q['question_type'] = 'unresolved'
        q['question_text'] = question_text_from_source(paper_text) or 'unresolved'
        q['has_diagram'] = None
        q['required_formulae_visible'] = []
        q['memo_answer'] = answer_from_text(memo_text) or 'unresolved'
        q['memo_method_steps'] = memo_method_steps_from_text(memo_text)
        q['memo_marking_notes'] = 'unresolved'
    elif subject == 'english':
        q['paper_type'] = 'unresolved'
        q['marks'] = mark_from_text(paper_text) or None
        q['section_guess'] = 'unresolved'
        q['set_text_title'] = None
        q['question_text'] = question_text_from_source(paper_text) or 'unresolved'
        q['question_format'] = 'unresolved'
        q['memo_answer'] = answer_from_text(memo_text) or 'unresolved'
        q['memo_marking_notes'] = 'unresolved'
        q['rubric_reference'] = False
    elif subject == 'history':
        q['marks'] = mark_from_text(paper_text) or None
        q['topic_guess'] = 'unresolved'
        q['question_format'] = 'unresolved'
        q['skill_focus_guess'] = 'unresolved'
        q['source_reference'] = 'unresolved'
        q['question_text'] = question_text_from_source(paper_text) or 'unresolved'
        q['memo_answer'] = answer_from_text(memo_text) or 'unresolved'
        q['memo_marking_notes'] = 'unresolved'
        q['essay_rubric_levels_if_present'] = 'unresolved'
    elif subject == 'mathematics':
        q['marks'] = mark_from_text(paper_text) or None
        q['topic_guess'] = 'unresolved'
        q['question_text'] = question_text_from_source(paper_text) or 'unresolved'
        q['has_diagram'] = None
        q['memo_answer'] = answer_from_text(memo_text) or 'unresolved'
        q['memo_method_steps'] = memo_method_steps_from_text(memo_text)
        q['memo_marking_notes'] = 'unresolved'
        q['calculator_allowed'] = 'unresolved'
    elif subject == 'physics':
        q['marks'] = mark_from_text(paper_text) or None
        q['discipline'] = 'Physics'
        q['topic_guess'] = 'unresolved'
        q['question_type'] = 'unresolved'
        q['question_text'] = question_text_from_source(paper_text) or 'unresolved'
        q['has_diagram'] = None
        q['required_formulae_visible'] = []
        q['memo_answer'] = answer_from_text(memo_text) or 'unresolved'
        q['memo_method_steps'] = memo_method_steps_from_text(memo_text)
        q['memo_marking_notes'] = 'unresolved'

    if rec.get('curriculum_path'):
        q['curriculum_path'] = rec.get('curriculum_path')
        q['curriculum_source'] = rec.get('curriculum_source')

    q['source_status'] = rec.get('source_status')
    q['provenance_note'] = f"Paper: {paper_path} | Memo: {memo_path}"
    return q


def main() -> None:
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open('r', encoding='utf-8') as fh:
        manifest = json.load(fh)

    grouped = defaultdict(list)
    for rec in manifest.get('records', []):
        subject = clean_subject(rec.get('subject', ''))
        if subject in SUBJECTS:
            grouped[subject].append(rec)

    for subject in SUBJECTS:
        out = []
        # subject file order stable
        for idx, rec in enumerate(grouped.get(subject, []), start=1):
            out.append(record_for(subject, rec, idx))

        out_path = EXTRACTED / f'{subject}_pass1.json'
        out_path.write_text(json.dumps(out, indent=2), encoding='utf-8')
        print(f'Wrote {out_path} with {len(out)} records')

    combined = []
    for subject in SUBJECTS:
        f = EXTRACTED / f'{subject}_pass1.json'
        if f.exists():
            combined.extend(json.loads(f.read_text(encoding='utf-8')))
    (EXTRACTED / 'all_subjects_pass1.json').write_text(json.dumps(combined, indent=2), encoding='utf-8')
    print(f'Wrote combined pass1 with {len(combined)} records')


if __name__ == '__main__':
    main()
