#!/usr/bin/env python3
"""Expand authored question evidence; fail closed on headers, totals and provenance.

Only the five usable pairs are in EVIDENCE_MODULES. The 2022 year-end paper
fails the printed-total gate (160 != 170) and remains an acquisition/review gap.
No organized file, inherited pairing or document-level stub is used as evidence.
"""
from __future__ import annotations
import importlib
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from core.runlog import sha256_file
from scripts.build_physics_pass1 import pdf_text, _norm_title
import yaml

EXTRACTED = ROOT / 'data/extracted'
PER_PAPER_DIR = EXTRACTED / 'pass1/biology'
INVENTORY = ROOT / 'data/raw/biology/SOURCE_INVENTORY.yaml'
EVIDENCE_MODULES = ['biology_pass1_evidence_'+s for s in
                    ['2022_cycle','2022_circulation','2023_july','2023_microorganisms','2023_november']]
GENERATED_AT = datetime.now(timezone.utc).isoformat(timespec='seconds')


def source_id_for(meta, qn):
    return f"biology_{meta['year']}_{meta['exam_board']}_{meta['paper_type']}_{meta['exam_period']}_q{qn}"


def header_fields(text):
    # All admitted biology papers print the same header layout.
    def get(pattern):
        match = re.search(pattern, text[:1100])
        if not match:
            raise ValueError(f'Missing printed header field: {pattern}')
        return re.sub(r'\s+', ' ', match.group(1)).strip()
    return {'date': get(r'DATE\s+(\d{1,2}\s+[A-Z]+\s+20\d\d)'),
            'marks': int(get(r'\bMARKS\s+(\d+)')),
            'examiner': get(r'EXAMINER\s+(.+?)\s+MODERATOR')}


def verify_alignment(paper_path, memo_path, meta):
    paper, memo = pdf_text(paper_path), pdf_text(memo_path)
    ph, mh = header_fields(paper), header_fields(memo)
    if ph != mh:
        raise ValueError(f'{meta["paper_key"]}: printed header mismatch: {ph} vs {mh}')
    if ph != {'date':meta['exam_date'], 'marks':meta['total_marks'], 'examiner':meta['examiner']}:
        raise ValueError('Authored metadata disagrees with printed header')
    cover = paper.split('TOTAL:')[0]
    cover_marks = [int(m) for _,m in re.findall(r'(?m)^\s*(\d+)\s+(\d+)\s*$', cover)]
    if cover_marks != meta['question_totals'] or sum(cover_marks) != ph['marks']:
        raise ValueError(f'Printed Question Total rows disagree: {cover_marks} vs {ph["marks"]}')
    sections = re.split(r'(?im)^Question\s+(\d+)\s*:?\s*\n', memo)
    memo_totals = []
    for i in range(1,len(sections),2):
        body=sections[i+1]
        explicit = re.search(r'(?i)Total Question\s+\d+\s*:\s*(\d+)',body)
        brackets = re.findall(r'\[(\d+)\]',body)
        if explicit: memo_totals.append(int(explicit.group(1)))
        elif brackets: memo_totals.append(int(brackets[-1]))
        elif meta['paper_key']=='BIO-2022-CYCLE1':
            # No top-level memo totals printed; its grouped allocations are (5),
            # (4), (13) for Q1 and (15), (13) for Q2. Preserve this distinction.
            groups = [5,4,13] if sections[i]=='1' else [15,13]
            for allocation in groups:
                if not re.search(r'\('+str(allocation)+r'\)',body):
                    raise ValueError('Cycle memo grouped allocation missing')
            memo_totals.append(sum(groups))
        else: raise ValueError('No readable memorandum question total')
    if memo_totals != cover_marks:
        raise ValueError(f'Memo Question Total disagreement: {memo_totals} vs {cover_marks}')
    for kind,text in [('paper',paper),('memo',memo)]:
        anchor=meta['alignment_anchors'][kind]
        if anchor not in re.sub(r'\s+',' ',text):
            raise ValueError(f'Numbered content does not match verified pair: {kind}')
    return {'paper_header':ph,'memo_header':mh,'date_match':True,'marks_match':True,
            'examiner_match':True,'paper_question_totals':cover_marks,
            'memo_question_totals':memo_totals,'question_totals_match':True,
            'memo_total_basis':'grouped allocations (5+4+13 and 15+13)' if meta['paper_key']=='BIO-2022-CYCLE1' else 'printed question totals',
            'verified_by':'printed DATE/MARKS/EXAMINER and per-question totals; numbered content checked during authoring'}


def validate_rows(meta, schema, rows):
    if any(len(r)!=len(schema) for r in rows): raise ValueError('Evidence tuple width')
    vals=[dict(zip(schema,r)) for r in rows]
    if len({v['qn'] for v in vals}) != len(vals): raise ValueError('Duplicate question number')
    if any(not isinstance(v['marks'],int) or v['marks']<=0 for v in vals):
        raise ValueError('Missing/invalid per-question marks')
    if sum(v['marks'] for v in vals)!=meta['total_marks']:
        raise ValueError(f'{meta["paper_key"]}: marks sum does not equal printed total')
    for i,total in enumerate(meta['question_totals'],1):
        if sum(v['marks'] for v in vals if v['qn'].split('.')[0]==str(i))!=total:
            raise ValueError(f'{meta["paper_key"]}: Q{i} subtotal mismatch')
    return vals


# Terms here are emitted ONLY when present literally in the individual source
# stem/memo (not assumed knowledge or a curriculum taxonomy).
TERMS = ('excretion','urea','glucose','proteins','nephron','renal corpuscle','renal vein',
         'urethra','ureter','ADH','diastole','systole','myogenic','heart rate','hypertension',
         'lymph','phagocytes','aorta','antibodies','bacteria','virus','HIV','AIDS','Plasmodium',
         'malaria','CD4','penicillin','antibiotics','agar','fungus','fungi','algae','protists',
         'pathogen','synovial fluid','rheumatoid arthritis','osteoarthritis','joint','rickets',
         'osteoporosis','tendon','ligament','cartilage','carrying capacity','population',
         'predator','prey','biodiversity','succession','cholesterol','dialysis','mutualistic')


def main():
    try:
        sources=yaml.safe_load(INVENTORY.read_text())['sources']
        index={}
        for s in sources:
            for title in (s.get('title',''),Path(s.get('title','')).stem):
                if title: index.setdefault((_norm_title(title),s.get("year")),set()).add(s['source_id'])
        batch=[]; docs=[]
        for module_name in EVIDENCE_MODULES:
            mod=importlib.import_module('ingestion.extraction.'+module_name)
            meta=dict(mod.PAPER)
            vals=validate_rows(meta,mod.SCHEMA,mod.RECORDS)
            alignment=verify_alignment(ROOT/meta['paper_path'],ROOT/meta['memo_path'],meta)
            orc=[]; hashes=[]
            for key in ('paper_path','memo_path'):
                path=ROOT/meta[key]
                matches=index.get((_norm_title(path.name),meta['year'])) or index.get((_norm_title(path.stem),meta['year']))
                if not matches or len(matches)!=1: raise ValueError(f'Absent/ambiguous ORC title: {path.name}')
                digest=sha256_file(path)
                if digest!=mod.SOURCE_HASHES[key]:raise ValueError(f'Source changed since transcription: {path.name}')
                orc.append(next(iter(matches)));hashes.append(digest)
            records=[]
            for v in vals:
                q=v['qn'];loc=mod.LOCATORS[q]
                if not loc['page'] or not loc['memo_page']:raise ValueError(f'Missing page locator {q}')
                sid=source_id_for(meta,q)
                text=v['text'];answer=v['memo_answer']
                rec={'source_id':sid,'question_id':meta['paper_key']+'-Q'+q,'subject':'biology','grade':'11',
                     'paper_key':meta['paper_key'],'source_document':meta['paper_path'],
                     'memo_document':meta['memo_path'],'source_document_sha256':hashes[0],
                     'memo_document_sha256':hashes[1],'orc_source_id':orc[0],'orc_memo_source_id':orc[1],
                     'question_number':q,'top_level_question_number':q.split('.')[0],
                     'parent_question_id':(meta['paper_key']+'-STEM-'+loc['parent_question_number']) if loc['parent_question_number'] else None,
                     'question_stem_text':loc['question_stem_text'],'page':loc['page'],'memo_page':loc['memo_page'],
                     'marks':v['marks'],'topic_guess':'guess: '+v['topic'],'question_type':v['qtype'],
                     'question_text':text,'has_diagram':v['has_diagram'],
                     'fidelity_rung':meta['fidelity_rung'],'requires_visual_verification':v['needs_visual'],
                     'ocr_uncertain':v['ocr_uncertain'],'memo_answer':answer,
                     'memo_method_steps':v['memo_steps'],'memo_marking_notes':v['memo_notes'],
                     'key_terminology_tested':[t for t in TERMS if re.search(r'\b'+re.escape(t)+r'\b',text+' '+answer,re.I)],
                     'memo_alignment':alignment,
                     'extraction':{'method':'pypdf text layer + question/memo reading; authored evidence table',
                                   'generated_at':GENERATED_AT,'evidence_module':module_name}}
                records.append(rec)
            stems={r['parent_question_id']:{'stem_id':r['parent_question_id'],
                     'question_stem_text':r['question_stem_text']} for r in records if r['parent_question_id']}
            docs.append({'paper':meta,'memo_alignment_check':alignment,'records_extracted':len(records),
                         'marks_sum_check':{'sum_of_records':sum(r['marks'] for r in records),
                                            'printed_total':meta['total_marks'],'match':True},
                         'question_stems':list(stems.values()),'question_records':records})
            batch.extend(records)
        if len({r['source_id'] for r in batch})!=len(batch):raise ValueError('Duplicate source_id')
    except (ValueError,KeyError,OSError) as exc:
        print(f'Biology Pass 1 FAILED (no outputs replaced): {exc}',file=sys.stderr)
        return 1
    PER_PAPER_DIR.mkdir(parents=True,exist_ok=True)
    def write(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
    for doc in docs:write(PER_PAPER_DIR/(doc['paper']['paper_key']+'.json'),doc)
    write(EXTRACTED/'biology_pass1.json',batch)
    aggregate=EXTRACTED/'all_subjects_pass1.json'
    previous=json.loads(aggregate.read_text()) if aggregate.exists() else []
    write(aggregate,[r for r in previous if r.get('subject')!='biology']+batch)
    summary={'subject':'biology','papers_in_batch':len(docs),'question_records':len(batch),
             'problems':[],'papers':[{'paper_key':d['paper']['paper_key'],'records':d['records_extracted'],
                                    'marks':d['paper']['total_marks']} for d in docs]}
    write(PER_PAPER_DIR/'_BATCH_SUMMARY.json',summary)
    print(f'Biology Pass 1: {len(docs)} pairs, {len(batch)} question records; all headers and totals agree.')
    return 0

if __name__=='__main__':raise SystemExit(main())
