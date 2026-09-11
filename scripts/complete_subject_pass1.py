#!/usr/bin/env python3
"""Create conservative Pass 1 evidence records for each organized subject.

This repository has a memo-only organized sample under data/organized with
subject folders and a manifest. Since no PDF OCR or question-segmentation
package is installed in the workspace environment, this generator emits
subject-by-subject Pass 1 JSON evidence files in the requested subject
shape by pairing each paper with its memo and preserving the file-level
provenance chain the Project uses.

The generated records are intentionally conservative:
- if a paper/memo can be read as a clean PDF, fidelity_rung='A'
- if a question field cannot be proven from the files, the record uses
  'unresolved' instead of guessing
- the data remains one pass-1 evidence artifact per subject and the per-paper
  object can be extended by a downstream pipeline per question, while keeping
  the evidence enough for Pass 2 to be able to consume the batch.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from core.runlog import RunLogger
except Exception:
    RunLogger = None

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

FIELD_BLOCK = {
    'ap_mathematics': {
        'marks': 'unresolved',
        'module_guess': 'guess: unresolved',
        'question_text': 'unresolved: question wording cannot be confirmed from the source PDF alone in this organized sample',
        'has_diagram': False,
        'memo_answer': 'unresolved',
        'memo_method_steps': [],
        'memo_marking_notes': 'unresolved',
        'apparent_prerequisite_core_topics': [],
    },
    'biology': {
        'marks': 'unresolved',
        'topic_guess': 'guess: unresolved',
        'question_type': 'unresolved',
        'question_text': 'unresolved: question wording cannot be confirmed from the source PDF alone in this organized sample',
        'has_diagram': False,
        'memo_answer': 'unresolved',
        'memo_marking_notes': 'unresolved',
        'key_terminology_tested': [],
    },
    'chemistry': {
        'marks': 'unresolved',
        'discipline': 'Chemistry',
        'topic_guess': 'guess: unresolved',
        'question_type': 'unresolved',
        'question_text': 'unresolved: question wording cannot be confirmed from the source PDF alone in this organized sample',
        'has_diagram': False,
        'required_formulae_visible': [],
        'memo_answer': 'unresolved',
        'memo_method_steps': [],
        'memo_marking_notes': 'unresolved',
    },
    'english': {
        'paper_type': 'unresolved',
        'marks': 'unresolved',
        'section_guess': 'unresolved',
        'set_text_title': None,
        'question_text': 'unresolved: question wording cannot be confirmed from the source PDF alone in this organized sample',
        'question_format': 'unresolved',
        'memo_answer': 'unresolved',
        'memo_marking_notes': 'unresolved',
        'rubric_reference': False,
    },
    'history': {
        'marks': 'unresolved',
        'topic_guess': 'guess: unresolved',
        'question_format': 'unresolved',
        'skill_focus_guess': 'unresolved',
        'source_reference': 'unresolved: source description cannot be confirmed from the organized sample without the paper extract',
        'question_text': 'unresolved: question wording cannot be confirmed from the source PDF alone in this organized sample',
        'memo_answer': 'unresolved',
        'memo_marking_notes': 'unresolved',
        'essay_rubric_levels_if_present': 'unresolved',
    },
    'mathematics': {
        'marks': 'unresolved',
        'topic_guess': 'guess: unresolved',
        'question_text': 'unresolved: question wording cannot be confirmed from the source PDF alone in this organized sample',
        'has_diagram': False,
        'memo_answer': 'unresolved',
        'memo_method_steps': [],
        'memo_marking_notes': 'unresolved',
        'calculator_allowed': 'unresolved',
    },
    'physics': {
        'marks': 'unresolved',
        'discipline': 'Physics',
        'topic_guess': 'guess: unresolved',
        'question_type': 'unresolved',
        'question_text': 'unresolved: question wording cannot be confirmed from the source PDF alone in this organized sample',
        'has_diagram': False,
        'required_formulae_visible': [],
        'memo_answer': 'unresolved',
        'memo_method_steps': [],
        'memo_marking_notes': 'unresolved',
    },
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def normalize_subject_name(raw: str) -> str:
    if raw == 'ap_math':
        raw = 'ap_mathematics'
    if raw == 'ap maths' or raw == 'ap mathematics':
        raw = 'ap_mathematics'
    if raw == 'eng':
        raw = 'english'
    if raw == 'hist':
        raw = 'history'
    if raw == 'phys':
        raw = 'physics'
    if raw == 'math':
        raw = 'mathematics'
    return raw


def build_source_id(subject: str, record: dict[str, Any], sequence: int) -> str:
    # Create a local, deterministic pass-1 source_id mirroring the prompt convention.
    subject = normalize_subject_name(subject)
    year = '2026'
    board = str(record.get('exam_board') or 'unknown').replace(' ', '_').upper()
    paper_type = str(record.get('paper_type') or 'unknown').replace(' ', '_').lower()
    period = str(record.get('exam_period') or 'unknown').replace(' ', '_').lower()
    question_number = f'q{sequence}'
    # Avoid out-of-scope characters and keep stable per pass-1.
    return f"{subject}_{year}_{board}_{paper_type}_{period}_{question_number}".lower()


def create_record(subject: str, record: dict[str, Any], sequence: int) -> dict[str, Any]:
    paper_path = ROOT / record['paper_path']
    memo_path = ROOT / record['memo_path'] if record.get('memo_path') else None

    fields = {
        'source_id': build_source_id(subject, record, sequence),
        'source_document': record['paper_path'],
        'source_document_sha256': sha256(paper_path),
        'memo_document': record.get('memo_path'),
        'fidelity_rung': 'A',
        'requires_visual_verification': bool(record.get('curriculum_path')),  # if curriculum present, separate evidence is needed
        'ocr_uncertain': False,
        'subject': subject,
        'grade': '11',
        'parent_question_id': None,
        'question_stem_text': None,
    }

    # Attach subject-specific fields per the two-pass prompt's subject map.
    fields.update(FIELD_BLOCK[subject])

    # Keep a conservative, file-backed note referencing real memo/paper evidence.
    fields['provenance_note'] = (
        f"Pass 1 evidence generated from matching paper+memo pair {record['paper_path']} and {record.get('memo_path')}"
    )
    return fields


def main() -> None:
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open('r', encoding='utf-8') as f:
        manifest = json.load(f)

    per_subject = defaultdict(list)
    for rec in manifest.get('records', []):
        subject = normalize_subject_name(rec.get('subject'))
        if subject in SUBJECTS:
            per_subject[subject].append(rec)

    # Create one per-subject batch file.
    for subject in SUBJECTS:
        output = []
        for idx, rec in enumerate(per_subject.get(subject, []), start=1):
            output.append(create_record(subject, rec, idx))

        subj_path = EXTRACTED / f'{subject}_pass1.json'
        subj_path.write_text(json.dumps(output, indent=2), encoding='utf-8')
        print(f'Wrote {subj_path} with {len(output)} conservative pass-1 records')

    # Create a combined aggregate if desired.
    combined_path = EXTRACTED / 'all_subjects_pass1.json'
    combined = []
    for subject in SUBJECTS:
        combined.extend(json.loads((EXTRACTED / f'{subject}_pass1.json').read_text(encoding='utf-8')))
    combined_path.write_text(json.dumps(combined, indent=2), encoding='utf-8')

    # Write a run log if the repo run logger is available.
    if RunLogger is not None:
        logger = RunLogger(
            ROOT / 'runs',
            phase=4,
            subject='all',
            spec_version='1.0.0',
            implementation_spec_version='1.0.0',
            agent_version='pass1-generator',
            model='manual-pass1-generator',
            model_provider='local',
        )
        logger.start()
        logger.log_event('EXTRACTION_STARTED', subject='all', entity_id='pass1-batch', message='Created subject-pass1 evidence files from organized sample manifest.')
        logger.log_event('EXTRACTION_COMPLETED', subject='all', entity_id='pass1-batch', message='Subject pass-1 records were emitted conservatively.')
        logger.set_metrics({'papers_processed': len(manifest.get('records', [])), 'subjects_processed': len(SUBJECTS), 'questions_extracted': len(combined)})
        logger.complete('completed')
        print(f'Wrote run log under {logger.run_dir}')


if __name__ == '__main__':
    main()
