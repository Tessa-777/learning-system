"""Biology two-pass regression, provenance, rejection and artifact tests.

Mirrors the physics checks, but adds fail-before-publish tests and rejects all
unverified visual members rather than allowing them to inflate confidence.
"""
from __future__ import annotations
import copy
import importlib
import json
from pathlib import Path
import subprocess
import pytest
import yaml
from core.runlog import sha256_file
from scripts import build_biology_pass1 as p1
from scripts import build_biology_pass2 as p2
ROOT=Path(__file__).resolve().parent.parent
K=ROOT/'knowledge/biology'

def read(path):return json.loads(path.read_text())

@pytest.fixture(scope='module')
def batch():return read(ROOT/'data/extracted/biology_pass1.json')

@pytest.fixture(scope='module')
def payload():return read(K/'pass2_output.json')


def test_both_builders_in_temporary_directory(tmp_path,monkeypatch,batch):
    monkeypatch.setattr(p1,'EXTRACTED',tmp_path)
    monkeypatch.setattr(p1,'PER_PAPER_DIR',tmp_path/'pass1/biology')
    assert p1.main()==0
    fresh=read(tmp_path/'biology_pass1.json')
    def without_timestamp(b):
        b=copy.deepcopy(b)
        for r in b:r['extraction'].pop('generated_at')
        return b
    assert without_timestamp(fresh)==without_timestamp(batch)
    docs=list((tmp_path/'pass1/biology').glob('BIO-*.json'));assert len(docs)==5
    for path in docs:
        d=read(path)
        assert d['marks_sum_check']['match']
        assert sum(r['marks'] for r in d['question_records'])==d['paper']['total_marks']
        assert all(d['memo_alignment_check'][k] for k in ['date_match','marks_match','examiner_match','question_totals_match'])
        stems={s['stem_id'] for s in d['question_stems']}
        assert all(r['parent_question_id'] is None or r['parent_question_id'] in stems for r in d['question_records'])
    monkeypatch.setattr(p2,'PASS1_BATCH',tmp_path/'biology_pass1.json')
    monkeypatch.setattr(p2,'OUT_DIR',tmp_path/'knowledge')
    assert p2.main()==0
    for name in p2.ARRAYS+['pass2_output','saturation_report','_PASS2_SUMMARY']:
        assert read(tmp_path/'knowledge'/f'{name}.json')==read(K/f'{name}.json')


def test_committed_invariants_and_combined_shape(batch,payload):
    assert set(payload)==set(p2.ARRAYS)
    assert p2.check_output(payload,batch,read(K/'saturation_report.json'))==54
    for key in p2.ARRAYS:assert payload[key]==read(K/f'{key}.json')
    claimed=[s for f in payload['question_families'] for s in f['source_evidence']]
    assert len(set(claimed))==len(claimed)==46
    assert len(batch)==275
    assert len({r['source_id'] for r in batch})==275
    assert sum(r['marks'] for r in batch)==490


def test_orc_chain_and_hashes(batch,payload):
    inventory=yaml.safe_load(p1.INVENTORY.read_text())['sources'];orc={s['source_id']:s for s in inventory}
    checked=set()
    for r in batch:
        assert r['subject']=='biology' and r['grade']=='11' and r['fidelity_rung']=='A'
        assert r['question_text'] and r['question_text']!='unresolved'
        assert 'INSTRUCTIONS:' not in r['question_text']
        assert r['page']>=2 and r['memo_page']>=2
        assert isinstance(r['key_terminology_tested'],list)
        for doc,source in [('source_document','orc_source_id'),('memo_document','orc_memo_source_id')]:
            assert r[source] in orc
            assert orc[r[source]]['title']==Path(r[doc]).name
            assert str(orc[r[source]]['year']) in r['source_id']
            if r[doc] not in checked:
                assert sha256_file(ROOT/r[doc])==r[doc+'_sha256'];checked.add(r[doc])
    assert len(checked)==10
    by_id={r['source_id']:r for r in batch}
    for m in payload['understanding_models']:
        assert len({by_id[s]['orc_source_id'] for s in m['source_references']})>=2
        assert all(by_id[s]['orc_memo_source_id'] in m['provenance'] for s in m['source_references'])


def test_real_content_and_local_memo_rules(batch):
    b={(r['paper_key'],r['question_number']):r for r in batch}
    assert b['BIO-2023-MICRO','1.row6']['question_stem_text'].find('A Gel extract')>=0
    assert b['BIO-2023-MICRO','2.1']['memo_answer'].startswith('Type of bacteria')
    assert 'fatigue' in b['BIO-2023-MICRO','3.1.5']['memo_marking_notes']
    assert 'both correct' in b['BIO-2023-JUL','1.4.5']['memo_marking_notes']
    assert 'radium' in b['BIO-2023-JUL','3.1.1']['memo_answer'] # no silent correction
    assert 'cm3/minute' in b['BIO-2023-NOV','1.5.6']['memo_answer']
    assert 'Name of synovial joint' not in b['BIO-2023-JUL','3.2.4']['memo_answer'] # displaced table cleaned
    assert 'QUESTION 2.1.3.' in b['BIO-2023-JUL','2.1.4']['question_text'] # cross-reference not mistaken for heading
    assert b['BIO-2023-NOV','4.1.5.c.i']['page']==24
    assert b['BIO-2022-CYCLE1','2.1.1.a']['question_stem_text']


def test_same_date_microorganisms_wrong_pair_rejected():
    mod=importlib.import_module('ingestion.extraction.biology_pass1_evidence_2023_microorganisms')
    with pytest.raises(ValueError,match='content does not match'):
        p1.verify_alignment(ROOT/'data/organized/biology/Class test 2- microorganisms.pdf',ROOT/mod.PAPER['memo_path'],mod.PAPER)


def test_year_end_printed_total_conflict_is_not_padded():
    meta={'paper_key':'BIO-2022-NOV','exam_date':'24 NOVEMBER 2022','total_marks':170,
          'examiner':'MRS S. STEGMANN','question_totals':[70,30,30,40]}
    with pytest.raises(ValueError,match='Question Total'):
        p1.verify_alignment(ROOT/'data/organized/biology/Year-end exam P1.pdf',ROOT/'data/organized/biology/Year-end exam P1 MG.pdf',meta)
    assert not (ROOT/'data/extracted/pass1/biology/BIO-2022-NOV.json').exists()


@pytest.mark.parametrize('fault',['marks','date','examiner','provenance','source_hash'])
def test_pass1_failure_never_replaces_output(tmp_path,monkeypatch,fault):
    mod=importlib.import_module('ingestion.extraction.biology_pass1_evidence_2022_cycle')
    monkeypatch.setattr(p1,'EXTRACTED',tmp_path)
    monkeypatch.setattr(p1,'PER_PAPER_DIR',tmp_path/'perpaper')
    sentinel=tmp_path/'biology_pass1.json';sentinel.write_text('do not replace')
    if fault=='marks':
        rows=copy.deepcopy(mod.RECORDS);row=list(rows[0]);row[1]+=1;rows[0]=tuple(row)
        monkeypatch.setattr(mod,'RECORDS',rows)
    elif fault in ['date','examiner']:
        meta=dict(mod.PAPER);meta['exam_date' if fault=='date' else 'examiner']='wrong'
        monkeypatch.setattr(mod,'PAPER',meta)
    elif fault=='provenance':
        inventory=tmp_path/'inventory.yaml';inventory.write_text('sources: []\n');monkeypatch.setattr(p1,'INVENTORY',inventory)
    else:monkeypatch.setattr(mod,'SOURCE_HASHES',{'paper_path':'wrong','memo_path':'wrong'})
    assert p1.main()==1
    assert sentinel.read_text()=='do not replace'
    assert not (tmp_path/'perpaper').exists()


@pytest.mark.parametrize('fault',['partition','confidence','reference','single','visual','citation','saturation'])
def test_pass2_rejects_invalid_knowledge(batch,payload,fault):
    b=copy.deepcopy(batch);p=copy.deepcopy(payload);s=read(K/'saturation_report.json')
    if fault=='partition':p['question_families'][1]['source_evidence'][0]=p['question_families'][0]['source_evidence'][0]
    if fault=='confidence':p['question_families'][0]['confidence']='high'
    if fault=='reference':p['diagnostic_questions'][0]['understanding_model_id']='UNDERSTANDING-MISSING'
    if fault=='single':p['breakdown_models'][0]['source_basis']=p['breakdown_models'][0]['source_basis'][:1]
    if fault=='visual':
        sid=p['question_families'][0]['source_evidence'][0]
        next(r for r in b if r['source_id']==sid)['requires_visual_verification']=True
    if fault=='citation':p['understanding_models'][0]['required_knowledge']=['Unsupported claim']
    if fault=='saturation':s['additional_diagnostics']['saturated']=True
    with pytest.raises((AssertionError,KeyError)):p2.check_output(p,b,s)


def test_saturation_and_scope_are_honest(batch,payload):
    s=read(K/'saturation_report.json')
    assert {'papers_in_sample','question_families_identified','families_first_observed_in_final_third','strata_left_unsampled','families_supported_by_single_exemplar'}<=s.keys()
    assert s['papers_in_sample']==5 and s['families_first_observed_in_final_third']==1
    assert s['families_new_in_final_third']==['QUESTION-FAMILY-BIO-008']
    assert not s['additional_diagnostics']['saturated']
    assert s['strata_left_unsampled']
    assert s['acquisition_order_used']==[importlib.import_module('ingestion.extraction.'+name).PAPER['paper_key'] for name in p1.EVIDENCE_MODULES]
    affected={u['id']:u['affected'] for u in payload['unresolved_items']}
    assert len(affected['UNRES-BIO-VISUAL'])==84 and len(affected['UNRES-BIO-UNASSIGNED'])==229
    claimed={sid for f in payload['question_families'] for sid in f['source_evidence']}
    assert not claimed.intersection(affected['UNRES-BIO-VISUAL'])
    assert len(affected['UNRES-BIO-003'])==8


def test_review_queue_and_run_log(payload):
    queue=yaml.safe_load((ROOT/'review_queue/RQ-P4-BIO-PASS2.yaml').read_text())
    assert queue['item_count']==len(queue['items'])==len(payload['unresolved_items'])
    for item in queue['items']:
        assert all(item.get(f) for f in ['issue','affected_entity','evidence','possible_resolutions','recommended_review'])
    assert {u['id']:u['affected_entity'] for u in queue['items']}=={u['id']:u['affected'] for u in payload['unresolved_items']}
    run=ROOT/'runs'/queue['run_id'];meta=read(run/'run.json')
    assert meta['subject']=='biology' and meta['status']=='completed_with_review'
    for f in ['events.jsonl','decisions.json','errors.json','metrics.json','artifacts/artifacts.yaml']:assert (run/f).exists()
    metrics=read(run/'metrics.json')
    assert metrics['questions_extracted']==metrics['questions_classified']+metrics['questions_unclassified']
    assert metrics['validation_failures']==0 and metrics['curriculum_mapping_rate'] is None
    assert any(e['error_type']=='saturation_not_reached' for e in read(run/'errors.json'))
    artifacts=yaml.safe_load((run/'artifacts/artifacts.yaml').read_text())
    assert artifacts and all(a['content_hash'] and a['source_run']==queue['run_id'] for a in artifacts)
    for a in artifacts:assert sha256_file(ROOT/a['path'])==a['content_hash'],a['path']


def test_aggregate_biology_only_replaced(batch):
    aggregate=read(ROOT/'data/extracted/all_subjects_pass1.json')
    assert [r for r in aggregate if r['subject']=='biology']==batch
    # Other subject files remain byte-preserved; aggregate objects likewise.
    original=json.loads(subprocess.check_output(['git','show','fc4dd558c42b8b5458c461207b4214649d5169a0:data/extracted/all_subjects_pass1.json'],cwd=ROOT,text=True))
    assert [r for r in aggregate if r['subject']!='biology']==[r for r in original if r['subject']!='biology']
