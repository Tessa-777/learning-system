#!/usr/bin/env python3
"""Build Biology Pass 2 from question records ONLY; validate before publishing."""
from __future__ import annotations
import copy
import json
import sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
from core.schema import SchemaValidator
from ingestion.analysis.biology_pass2_families import FAMILIES
from ingestion.analysis.biology_pass2_models import MODELS, DEFERRED
from ingestion.analysis.biology_pass2_unresolved import UNRESOLVED, QUESTION_ISSUES

PASS1_BATCH=ROOT/'data/extracted/biology_pass1.json'
OUT_DIR=ROOT/'knowledge/biology'
# Order of addition to the NEW, question-level evidence batch, not exam dates
# inferred from an unreliable manifest. The Pass 1 module list uses this order.
ACQUISITION_ORDER=['BIO-2022-CYCLE1','BIO-2022-CIRC','BIO-2023-JUL','BIO-2023-MICRO','BIO-2023-NOV']
ARRAYS=['question_families','understanding_models','breakdown_models','diagnostic_questions','unresolved_items']


def compute_confidence(records):
    if len(records)<2:return 'low'
    if any(r['requires_visual_verification'] or r['ocr_uncertain'] or r['fidelity_rung']!='A' for r in records):return 'medium'
    return 'high' if len(records)>=4 and len({r['source_document_sha256'] for r in records})>=3 else 'medium'


def check_output(payload, batch, saturation):
    """Public invariant gate, also exercised against mutations by the tests."""
    by_id={r['source_id']:r for r in batch}
    assert len(by_id)==len(batch), 'Duplicate Pass 1 source IDs'
    claimed=set(); family_by={};models={};breakdowns={};diagnostics={}
    validator=SchemaValidator(ROOT/'database/schema')
    count=0
    for name,schema,idkey,target in [
        ('question_families','question_family','question_family_id',family_by),
        ('understanding_models','knowledge_model','identity',models),
        ('breakdown_models','breakdown','breakdown_id',breakdowns),
        ('diagnostic_questions','diagnostic','diagnostic_id',diagnostics)]:
        for obj in payload[name]:
            assert obj[idkey] not in target,'Duplicate object ID'
            target[obj[idkey]]=obj
            result=validator.validate(schema+'.schema.json',obj)
            assert result.valid,result.errors
            count+=1
    for f in family_by.values():
        ids=f['source_evidence'];assert len(set(ids))==len(ids)>=2
        assert not claimed.intersection(ids),'Family membership overlaps'
        assert set(ids)<=by_id.keys(),'Unknown source ID'
        rs=[by_id[s] for s in ids]
        assert all(r['subject']=='biology' and r['memo_answer'] and not r['memo_answer'].startswith('unresolved') for r in rs)
        assert all(not r['requires_visual_verification'] and not r['ocr_uncertain'] and r['fidelity_rung']=='A' for r in rs),'Unverified evidence in family'
        assert f['confidence']==compute_confidence(rs)
        assert f['frequency']==len(ids)
        claimed.update(ids)
    required={'identity','definition','subject','grade','topic','question_family','assessment_operations','required_knowledge','prerequisites','required_reasoning','required_procedure','evidence_of_understanding','marking_requirements','common_breakdowns','misconceptions','diagnostic_dimensions','diagnostic_questions','source_references','confidence','validation_state','version','provenance'}
    assert len(models)==len(family_by)
    assert {m['question_family'] for m in models.values()}==set(family_by)
    for m in models.values():
        assert required==set(m)
        f=family_by[m['question_family']]
        assert m['source_references']==f['source_evidence'] and m['confidence']==f['confidence']
        assert m['validation_state']=='unvalidated' and m['version']=='0.1.0-draft'
        assert set(m['source_references'])<=set(m['provenance'])
        for field in ['definition','required_knowledge','prerequisites','required_reasoning','required_procedure','evidence_of_understanding','marking_requirements','misconceptions']:
            claims=m[field] if isinstance(m[field],list) else [m[field]]
            for claim in claims:assert sum(sid in claim for sid in m['source_references'])>=2,'Uncited claim'
        assert 2<=len(m['diagnostic_questions'])<=4
        assert set(m['common_breakdowns'])<=breakdowns.keys()
        assert set(m['diagnostic_questions'])<=diagnostics.keys()
        for bid in m['common_breakdowns']:assert breakdowns[bid]['parent_understanding_model']==m['identity']
        for did in m['diagnostic_questions']:assert diagnostics[did]['understanding_model_id']==m['identity']
    for b in breakdowns.values():
        m=models[b['parent_understanding_model']]
        assert len(set(b['source_basis']))>=2
        assert set(b['source_basis'])<=set(m['source_references'])
        assert all(by_id[sid]['memo_marking_notes'] for sid in b['source_basis'])
        assert set(b['distinguishing_questions'])<=diagnostics.keys()
        assert b['confidence']==compute_confidence([by_id[sid] for sid in b['source_basis']])
    for d in diagnostics.values():
        m=models[d['understanding_model_id']]
        assert d['target_breakdown'] in m['common_breakdowns']
        assert set(d['distinguishes'])<=set(m['common_breakdowns'])
        assert len(d['distinguishes'])>=2
        assert sum(sid in d['source_or_rationale'] for sid in m['source_references'])>=2
    unassigned=set(by_id)-claimed
    unres={u['id']:u for u in payload['unresolved_items']}
    assert unassigned==set(unres['UNRES-BIO-UNASSIGNED']['affected'])
    assert {r['source_id'] for r in batch if r['requires_visual_verification']}==set(unres['UNRES-BIO-VISUAL']['affected'])
    for u in unres.values():
        assert all(u.get(k) for k in ['type','summary','detail','affected','evidence','recommended_review'])
    order=saturation['acquisition_order_used']
    assert set(order)=={r['paper_key'] for r in batch} and len(set(order))==len(order)
    n=len(order);thirds=[order[:round(n/3)],order[round(n/3):round(2*n/3)],order[round(2*n/3):]]
    assert saturation['thirds_split']==thirds
    new=[f['question_family_id'] for f in family_by.values() if {by_id[s]['paper_key'] for s in f['source_evidence']}<=set(thirds[-1])]
    assert saturation['papers_in_sample']==n
    assert saturation['question_families_identified']==len(family_by)
    assert saturation['families_first_observed_in_final_third']==len(new)
    assert saturation['families_new_in_final_third']==new
    assert saturation['families_supported_by_single_exemplar']==0
    if new or n<8 or saturation['strata_left_unsampled']:
        assert saturation['additional_diagnostics']['saturated'] is False
    return count


def build(batch):
    by_pair={(r['paper_key'],r['question_number']):r for r in batch}
    assert len(by_pair)==len(batch)
    payload={key:[] for key in ARRAYS};summary_families=[]
    def resolve(pairs):return [by_pair[tuple(p)]['source_id'] for p in pairs]
    for i,f in enumerate(FAMILIES,1):
        ids=resolve(f['members']);rs=[by_pair[tuple(p)] for p in f['members']]
        assert len(set(ids))>=2
        confidence=compute_confidence(rs)
        cite=' [sources: '+', '.join(ids)+']'
        claim=lambda text: '[Tier 2 derived] '+text+cite
        model=MODELS[i];mid=f'UNDERSTANDING-BIO-{i:03d}'
        bids=[f'BREAKDOWN-BIO-{i:03d}-{s}' for s in 'AB']
        dids=[f'DIAG-BIO-{i:03d}-{s}' for s in 'AB']
        family={'question_family_id':f['family_id'],'name':f['name'],'definition':claim(f['definition']),
                'subject':'biology','grade':'11','topics':[f['topic']],
                'assessment_operations':f['operations'],'representative_questions':ids[:3],
                'frequency':len(ids),'source_evidence':ids,'confidence':confidence,'validation_status':'unvalidated'}
        payload['question_families'].append(family)
        payload['understanding_models'].append({
            'identity':mid,'definition':claim(f['definition']),'subject':'biology','grade':'11',
            'topic':f['topic'],'question_family':f['family_id'],'assessment_operations':f['operations'],
            'required_knowledge':[claim(model['knowledge'])],'prerequisites':[claim(model['prerequisites'])],
            'required_reasoning':[claim(model['reasoning'])],'required_procedure':claim(model['procedure']),
            'evidence_of_understanding':[claim(model['evidence'])],'marking_requirements':[claim(model['marking'])],
            'common_breakdowns':bids,'misconceptions':['[Tier 3 possible belief, not observed] '+model['misconception']+cite],
            'diagnostic_dimensions':[b[0] for b in model['breakdowns']],
            'diagnostic_questions':dids,'source_references':ids,
            'confidence':confidence,'validation_state':'unvalidated','version':'0.1.0-draft',
            'provenance':[f['family_id']]+ids+sorted({r[k] for r in rs for k in ['orc_source_id','orc_memo_source_id']})})
        for j,(stage,description,signal) in enumerate(model['breakdowns']):
            payload['breakdown_models'].append({
                'breakdown_id':bids[j],'description':'[Tier 3 possible failure] '+description+cite,
                'parent_understanding_model':mid,'stage':stage,
                'observable_signals':[signal+cite],
                'possible_confusions':[model['breakdowns'][1-j][1]+cite],
                'distinguishing_questions':dids,'source_basis':ids,'confidence':confidence})
        for j,(question,evidence) in enumerate(model['diagnostics']):
            payload['diagnostic_questions'].append({
                'diagnostic_id':dids[j],'understanding_model_id':mid,'target_breakdown':bids[j],
                'question':question,'purpose':'[Tier 3] Distinguish '+model['breakdowns'][j][1]+' from '+model['breakdowns'][1-j][1],
                'distinguishes':bids,'expected_evidence':['[Tier 3] '+evidence+cite],
                'follow_up_conditions':[{'condition':'The response does not locate the evidence in the question.',
                                         'follow_up':'Which part of the supplied information supports your choice?'}],
                'source_or_rationale':'[Tier 3 proposed diagnostic, not validated on learners] '+model['marking']+cite,
                'confidence':confidence})
        summary_families.append({'family_id':f['family_id'],'name':f['name'],'members':len(ids),
                                 'papers':sorted({r['paper_key'] for r in rs}),'confidence':confidence,
                                 'marks_range':[min(r['marks'] for r in rs),max(r['marks'] for r in rs)],
                                 'distinguishing_features':f['definition'],'member_source_ids':ids,
                                 'breakdown_memo_basis':{r['source_id']:r['memo_marking_notes'] for r in rs}})
    unresolved=copy.deepcopy(UNRESOLVED)
    for i,u in enumerate(unresolved,1):u['id']=f'UNRES-BIO-{i:03d}'
    for typ,title,detail,pairs in QUESTION_ISSUES:
        ids=resolve(pairs)
        unresolved.append({'id':f'UNRES-BIO-{len(unresolved)+1:03d}','type':typ,'summary':title,
                           'detail':detail,'affected':ids,'evidence':ids,
                           'recommended_review':'Verify the original marking guidance with the examiner; do not generalise or silently correct the local rule.'})
    for typ,title,pairs in DEFERRED:
        ids=resolve(pairs)
        unresolved.append({'id':f'UNRES-BIO-{len(unresolved)+1:03d}','type':typ,'summary':title,
                           'detail':'Deferred candidate, not an established cross-paper model. '+title,
                           'affected':ids,'evidence':ids,
                           'recommended_review':'Acquire independent marking examples or verify the source visuals before promoting this candidate.'})
    claimed={s for f in payload['question_families'] for s in f['source_evidence']}
    for name,ids,detail in [
        ('UNASSIGNED',sorted({r['source_id'] for r in batch}-claimed),'Records not fitting an admitted, independently supported family remain unassigned; no coverage is implied.'),
        ('VISUAL',[r['source_id'] for r in batch if r['requires_visual_verification']], 'These records depend on an unverified figure, graph or image answer. Their text/memo is retained, but none contributes to Pass 2 families.')]:
        unresolved.append({'id':'UNRES-BIO-'+name,'type':'fidelity' if name=='VISUAL' else 'coverage_gap',
                           'summary':f'{len(ids)} {name.lower()} question records','detail':detail,
                           'affected':ids,'evidence':ids,
                           'recommended_review':'Review the source pages and expand the batch before classifying these records.'})
    payload['unresolved_items']=unresolved
    order=ACQUISITION_ORDER;n=len(order);thirds=[order[:round(n/3)],order[round(n/3):round(2*n/3)],order[round(2*n/3):]]
    by_id={r['source_id']:r for r in batch}
    new=[f['question_family_id'] for f in payload['question_families'] if {by_id[s]['paper_key'] for s in f['source_evidence']}<=set(thirds[-1])]
    sat={'papers_in_sample':n,'question_families_identified':len(FAMILIES),
         'families_first_observed_in_final_third':len(new),
         'strata_left_unsampled':['2022 year-end paper (marks conflict)','Paper 2 (no local memorandum)',
                                  '2024 class tests (no local memoranda)','Other locally unpaired class/cycle tests',
                                  'External-board and preliminary sittings not represented; school applicability unverified'],
         'families_supported_by_single_exemplar':0,
         'acquisition_order_used':order,'acquisition_order_basis':'Order added to the rebuilt question-level Pass 1 batch; not inferred historical download order.',
         'thirds_split':thirds,'families_new_in_final_third':new,
         'additional_diagnostics':{'saturated':False,'reason_not_saturated':'New family in final third; five papers are below recommended 8–15; missing strata and large unassigned/visual portion.',
                                   'deferred_single_exemplar_candidates':sum(u['type']=='single_exemplar' for u in unresolved),
                                   'records_unassigned':len(batch)-len(claimed)}}
    checked=check_output(payload,batch,sat)
    summary={'subject':'biology','question_records_in_batch':len(batch),'papers_in_sample':n,
             'records_assigned_to_a_family':len(claimed),**{k:len(v) for k,v in payload.items()},
             'schema_validation':{'checked':checked,'failed':0},'families':summary_families,
             'confidence_distribution':dict(Counter(f['confidence'] for f in payload['question_families'])),'errors':[]}
    return payload,sat,summary


def main():
    try:
        batch=json.loads(PASS1_BATCH.read_text())
        if len({r['paper_key'] for r in batch})<2:raise ValueError('Pass 2 blocked: fewer than two usable pairs')
        payload,sat,summary=build(batch)
    except (AssertionError,ValueError,KeyError,OSError) as exc:
        print(f'Biology Pass 2 FAILED (no outputs replaced): {exc}',file=sys.stderr);return 1
    OUT_DIR.mkdir(parents=True,exist_ok=True)
    outputs={k+'.json':v for k,v in payload.items()}
    outputs.update({'pass2_output.json':payload,'saturation_report.json':sat,'_PASS2_SUMMARY.json':summary})
    for name,obj in outputs.items():(OUT_DIR/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
    print(f"Biology Pass 2: {summary['question_families']} families, {summary['understanding_models']} models, "
          f"{summary['breakdown_models']} breakdowns, {summary['diagnostic_questions']} diagnostics; "
          f"{summary['schema_validation']['checked']} schema-valid objects. NOT saturated.")
    return 0

if __name__=='__main__':raise SystemExit(main())
