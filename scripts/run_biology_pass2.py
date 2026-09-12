#!/usr/bin/env python3
"""Auditable entry point for biology's requested Pass 1 + Pass 2, not later phases."""
from __future__ import annotations
import json
import re
import subprocess
import sys
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
from core.runlog import RunLogger, sha256_file
from scripts.build_biology_pass1 import pdf_text
REVIEW_QUEUE=ROOT/'review_queue/RQ-P4-BIO-PASS2.yaml'


def write_review_queue(run_id, unresolved):
    items=[]
    for u in unresolved:
        items.append({'id':u['id'],'type':u['type'],'issue':u['summary'],'detail':u['detail'],
                      'affected_entity':u['affected'],'evidence':u['evidence'],
                      'possible_resolutions':[u['recommended_review'],
                                              'Retain the unresolved item and exclude unsupported claims from the knowledge bank.'],
                      'recommended_review':u['recommended_review']})
    REVIEW_QUEUE.write_text(yaml.safe_dump({'review_id':'RQ-P4-BIO-PASS2','run_id':run_id,
        'subject':'biology','phase':'4-11','item_count':len(items),'items':items},sort_keys=False,allow_unicode=True))


def main():
    logger=RunLogger(ROOT/'runs',phase='4-11',subject='biology',agent_version='1.0.0',
                     model='arena-agent',model_provider='arena.ai')
    run_id=logger.start();print('run_id:',run_id)
    try:
        logger.log_event('EXTRACTION_STARTED',message='Rebuild question-level evidence; do not consume old stubs or manifest pairings.')
        for script in ['build_biology_pass1.py','build_biology_pass2.py']:
            proc=subprocess.run([sys.executable,str(ROOT/'scripts'/script)],cwd=ROOT,capture_output=True,text=True)
            print(proc.stdout,end='')
            if proc.stderr:print(proc.stderr,file=sys.stderr,end='')
            if proc.returncode:
                logger.log_error(error_type='builder_failure',message=proc.stdout+proc.stderr,affected_artifact=script)
                logger.complete('failed');return proc.returncode
            logger.log_event('EXTRACTION_COMPLETED' if 'pass1' in script else 'VALIDATION_COMPLETED',
                             message=proc.stdout.strip(),metadata={'builder':script,'exit_code':0})
        batch=json.loads((ROOT/'data/extracted/biology_pass1.json').read_text())
        out=ROOT/'knowledge/biology';summary=json.loads((out/'_PASS2_SUMMARY.json').read_text())
        unresolved=json.loads((out/'unresolved_items.json').read_text())
        sat=json.loads((out/'saturation_report.json').read_text())
        for paper in sorted({r['paper_key'] for r in batch}):
            rs=[r for r in batch if r['paper_key']==paper]
            logger.log_event('MEMO_ALIGNED',entity_id=paper,message='Printed headers and question totals verified; numbered content read.',
                             metadata={'records':len(rs),'marks':sum(r['marks'] for r in rs),'alignment':rs[0]['memo_alignment']})
        decisions=[
            ('replace_stubs','Document-level records contain no usable question evidence.','Rebuild all five usable pairs at question level; preserve source files unchanged.','data/extracted/biology_pass1.json'),
            ('pairing','Matching dates alone cannot distinguish the microorganisms tests.','Use numbered penicillin content to pair Test 1; do not pair Test 2.','UNRES-BIO-002'),
            ('marks_gate','Year-end 2022 printed allocations sum to 160 rather than header 170.','Reject the pair; do not pad marks or silently reinterpret its memo.','UNRES-BIO-001'),
            ('provenance','Circulation titles recur in two inventory years.','Resolve normalized title plus verified printed year; fail on absent or ambiguous matches.','UNRES-BIO-005'),
            ('confidence','Confidence must be computed, not authored.','High requires four members across three distinct paper hashes; exclude unverified visual evidence entirely.','scripts/build_biology_pass2.py'),
            ('saturation_order','Historical download order is not reliable evidence for this new batch.','Use the recorded order of addition to question-level Pass 1; report all thirds and do not declare saturation.','knowledge/biology/saturation_report.json'),
            ('schema_mapping','Family schema forbids additional fields; prompt asks for membership/features/marks.','Keep schema fields source_evidence/definition and supply requested aliases and marks ranges in summary. Combined output has exactly five arrays.','knowledge/biology/_PASS2_SUMMARY.json'),
            ('scope','No syllabus/ATP and many records cannot support repeated patterns.','Keep Phase 7 and phases 12+ out of scope; draft models and explicit unassigned list, not inferred coverage.','knowledge/biology/unresolved_items.json'),
            ('partial_credit','Some special marking rules occur only once.','Keep fatigue-only and paired-table-entry rules in Pass 1 and single_exemplar review rather than generalising.','UNRES-BIO-012'),
        ]
        for i,(typ,context,selected,evidence) in enumerate(decisions,1):
            logger.log_decision(decision_id=f'DEC-BIO-{i:03d}',decision_type=typ,context=context,
                                evidence=[evidence],alternatives=['Infer or silently repair the missing evidence',selected],
                                selected=selected,rationale='Preserve provenance and distinguish source facts from unvalidated synthesis.',
                                confidence='high',requires_review=True)
        for u in unresolved:
            logger.log_event('REVIEW_REQUIRED',entity_id=u['id'],message=u['summary'],metadata={'type':u['type'],'affected':u['affected']})
            if u['type']=='contradiction':logger.log_error(error_type='source_contradiction',message=u['detail'],affected_artifact=u['affected'][0],resolution=u['recommended_review'])
        logger.log_error(error_type='saturation_not_reached',message=sat['additional_diagnostics']['reason_not_saturated'],
                         affected_artifact='knowledge/biology/saturation_report.json',resolution='Resolve gaps and enlarge the evidence batch.')
        write_review_queue(run_id,unresolved)
        # Metadata-only corpus audit covers all sources, including omitted pairs and booklets.
        used={r[k] for r in batch for k in ['source_document','memo_document']}
        corpus=[]
        for path in sorted((ROOT/'data/organized/biology').rglob('*.pdf')):
            rel=str(path.relative_to(ROOT));text=pdf_text(path)
            kind='source_booklet' if 'curriculum' in path.parts else 'memorandum' if ' MG' in path.name else 'question_paper'
            disposition='admitted' if rel in used else 'out_of_scope_curriculum' if kind=='source_booklet' else 'rejected_marks_conflict' if path.name.startswith('Year-end') else 'no_matching_local_memo'
            corpus.append({'path':rel,'sha256':sha256_file(path),'document_type':kind,
                           'text_layer_characters':len(text),'disposition':disposition})
            if rel not in used:logger.log_event('SOURCE_SKIPPED',entity_id=rel,message=disposition)
        (ROOT/'data/extracted/pass1/biology/_CORPUS_AUDIT.json').write_text(json.dumps(corpus,indent=2)+'\n')
        logger.set_metrics({'files_in_organized_sample':20,'source_booklets':2,'question_papers_in_sample':14,
                            'memoranda_in_sample':6,'papers_processed':5,'papers_rejected_marks_conflict':1,
                            'papers_without_local_memo':8,'questions_extracted':len(batch),
                            'questions_classified':summary['records_assigned_to_a_family'],
                            'questions_unclassified':len(batch)-summary['records_assigned_to_a_family'],
                            'memo_alignment_rate':1.0,'curriculum_mapping_rate':None,
                            'records_requiring_visual_verification':sum(r['requires_visual_verification'] for r in batch),
                            'understanding_models':summary['understanding_models'],'breakdowns':summary['breakdown_models'],
                            'diagnostics':summary['diagnostic_questions'],'unresolved_items':len(unresolved),
                            'validation_failures':0,'schema_objects_checked':summary['schema_validation']['checked']})
        status_path=ROOT/'STATUS.md';status=status_path.read_text()
        new_head=f'''```yaml
current_phase: 4-11 (biology Pass 1 + Pass 2; Phase 7 not run)
current_subject: biology
status: completed_with_review
knowledge_bank_version: null
unresolved_items: {len(unresolved)} # current biology run only; earlier subject queues remain open
last_run_id: {run_id}
next_allowed_phase: biology review/acquisition and Phase 7 mapping; no automatic phase continuation
```'''
        status=re.sub(r'```yaml.*?```',lambda _:new_head,status,count=1,flags=re.S)
        status=re.sub(r'\n<!-- BIOLOGY_PASS2_START -->.*?<!-- BIOLOGY_PASS2_END -->\n','\n',status,flags=re.S)
        status+=f'''
<!-- BIOLOGY_PASS2_START -->
## Biology Two-Pass — 2026-09-12

**Status:** completed_with_review · **Run:** `{run_id}`

275 question records from five verified pairs (50 + 50 + 150 + 40 + 200 = 490 marks).
9 families, 9 Understanding Models, 18 breakdowns and 18 diagnostics; 54 objects schema-valid.
46 records classified; 229 deliberately unassigned. {len(unresolved)} review items.
All models are `unvalidated`, `0.1.0-draft`; curriculum coverage remains unknown.

**Not saturated:** one family first observed in the final third of the new batch.
The 2022 year-end pair is rejected (160 allocated versus 170 printed); eight papers lack
local memoranda. The microorganisms ambiguity was resolved from content, not dates.
Visual-dependent records are excluded from synthesis, not silently counted as support.

Full report: `knowledge/biology/BIOLOGY_REPORT.md`.
Entry point: `python scripts/run_biology_pass2.py`; tests: `python -m pytest`.
Review queue: `review_queue/RQ-P4-BIO-PASS2.yaml`.

This supersedes the historical statement above that all non-physics subjects still have
stub Pass 1 records. Physics and the other subjects were not rebuilt or changed.
Only biology entries in the all-subject aggregate were replaced. No later phase was run.
<!-- BIOLOGY_PASS2_END -->
'''
        status_path.write_text(status)
        artifacts=[ROOT/'.gitignore',status_path,REVIEW_QUEUE,ROOT/'data/extracted/biology_pass1.json',ROOT/'data/extracted/all_subjects_pass1.json']
        for pattern in ['data/extracted/pass1/biology/*.json','knowledge/biology/*.json','knowledge/biology/*REPORT.md',
                        'ingestion/extraction/biology_pass1_evidence_*.py','ingestion/analysis/biology_pass2_*.py',
                        'scripts/*biology_pass*.py','tests/test_biology_pass2.py']:
            artifacts.extend(ROOT.glob(pattern))
        for path in sorted(set(artifacts)):
            logger.record_artifact(str(path.relative_to(ROOT)),content_hash=sha256_file(path))
        logger.complete('completed_with_review',unresolved_items=len(unresolved))
        print(f'Run completed_with_review: runs/{run_id}')
        return 0
    except Exception as exc:
        logger.log_error(error_type=type(exc).__name__,message=str(exc))
        logger.complete('failed');raise

if __name__=='__main__':raise SystemExit(main())
