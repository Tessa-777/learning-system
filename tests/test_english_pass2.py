"""English two-pass regression, provenance, rejection and artifact tests.

Mirrors the biology checks with the language-paper specifics: header-based
pairing where a header exists, content-based pairing for the one memorandum that
prints none, printed source defects that must survive extraction unchanged, and
the rule that image-dependent records may never carry a family claim.
"""
from __future__ import annotations
import copy
import importlib
import json
import subprocess
from pathlib import Path
import pytest
import yaml
from core.runlog import sha256_file
from scripts import build_english_pass1 as p1
from scripts import build_english_pass2 as p2
ROOT = Path(__file__).resolve().parent.parent
K = ROOT / 'knowledge/english'


def read(path):
    return json.loads(path.read_text())


@pytest.fixture(scope='module')
def batch():
    return read(ROOT / 'data/extracted/english_pass1.json')


@pytest.fixture(scope='module')
def payload():
    return read(K / 'pass2_output.json')


def test_both_builders_in_temporary_directory(tmp_path, monkeypatch, batch):
    monkeypatch.setattr(p1, 'EXTRACTED', tmp_path)
    monkeypatch.setattr(p1, 'PER_PAPER_DIR', tmp_path / 'pass1/english')
    assert p1.main() == 0
    fresh = read(tmp_path / 'english_pass1.json')

    def without_timestamp(records):
        records = copy.deepcopy(records)
        for r in records:
            r['extraction'].pop('generated_at')
        return records
    assert without_timestamp(fresh) == without_timestamp(batch)
    docs = list((tmp_path / 'pass1/english').glob('ENG-*.json'))
    assert len(docs) == 5
    for path in docs:
        d = read(path)
        assert d['marks_sum_check']['match']
        counted = sum(r['marks'] for r in d['question_records']
                      if r['allocation'] == 'allocated')
        counted += sum(
            d['paper'].get('alternative_sections', {}).get(key, {}).get('counted', 0)
            * d['paper'].get('alternative_sections', {}).get(key, {}).get('marks_each', 0)
            for key in d['paper'].get('alternative_sections', {}))
        shortfall = sum(x['printed_section_total'] - x['sum_of_printed_item_marks']
                        for x in d['paper'].get('mark_discrepancies', []))
        assert counted + shortfall == d['paper']['total_marks']
        alignment = d['memo_alignment_check']
        assert alignment['date_match'] and alignment['marks_match']
        assert alignment['pairing_basis'] in {'printed_header', 'content_and_printed_totals'}
    monkeypatch.setattr(p2, 'PASS1_BATCH', tmp_path / 'english_pass1.json')
    monkeypatch.setattr(p2, 'OUT_DIR', tmp_path / 'knowledge')
    assert p2.main() == 0
    for name in p2.ARRAYS + ['pass2_output', 'saturation_report', '_PASS2_SUMMARY']:
        assert read(tmp_path / 'knowledge' / f'{name}.json') == read(K / f'{name}.json')


def test_committed_invariants_and_combined_shape(batch, payload):
    assert set(payload) == set(p2.ARRAYS)
    assert p2.check_output(payload, batch, read(K / 'saturation_report.json')) == 90
    for key in p2.ARRAYS:
        assert payload[key] == read(K / f'{key}.json')
    claimed = [s for f in payload['question_families'] for s in f['source_evidence']]
    assert len(set(claimed)) == len(claimed) == 81
    assert len(batch) == 126
    assert len({r['source_id'] for r in batch}) == 126
    # Every question the papers print is transcribed — including all three
    # optional transactional tasks, of which a candidate answers two.
    assert sum(r['marks'] for r in batch) == 458
    assert sum(r['marks'] for r in batch if r['allocation'] == 'alternative') == 60
    # Marks counted the way the papers count them: two of the three options, plus
    # the two declared source shortfalls (2016 P1 Q1, 2018 P1 Q5).
    counted = sum(r['marks'] for r in batch if r['allocation'] == 'allocated')
    counted += 40 + 2
    assert counted == 440


def test_orc_chain_and_hashes(batch, payload):
    inventory = yaml.safe_load(p1.INVENTORY.read_text())['sources']
    orc = {s['source_id']: s for s in inventory}
    checked = set()
    for r in batch:
        assert r['subject'] == 'english' and r['grade'] == '11' and r['fidelity_rung'] == 'A'
        assert r['question_text'] and r['question_text'] != 'unresolved'
        assert r['paper_type'] in {'Language', 'Literature', 'Writing'}
        assert r['paper_number'] in {'P1', 'P2'}
        assert r['section_guess'] in {'Comprehension', 'Summary', 'Language Structures & Conventions',
                                      'Visual Literacy', 'Poetry (Seen)', 'Poetry (Unseen)', 'Novel',
                                      'Drama', 'Short Stories', 'Essay Writing', 'Transactional Writing'}
        assert isinstance(r['rubric_reference'], bool) and isinstance(r['memo_marking_notes'], str)
        for doc, source in [('source_document', 'orc_source_id'), ('memo_document', 'orc_memo_source_id')]:
            assert r[source] in orc
            assert orc[r[source]]['title'] == Path(r[doc]).name
            assert str(orc[r[source]]['year']) in r['source_id']
            if r[doc] not in checked:
                assert sha256_file(ROOT / r[doc]) == r[doc + '_sha256']
                checked.add(r[doc])
    assert len(checked) == 10
    by_id = {r['source_id']: r for r in batch}
    for m in payload['understanding_models']:
        assert len({by_id[s]['orc_source_id'] for s in m['source_references']}) >= 2
        assert all(by_id[s]['orc_memo_source_id'] in m['provenance'] for s in m['source_references'])


def test_real_content_and_source_defects_preserved(batch):
    b = {(r['paper_key'], r['question_number']): r for r in batch}
    # Reading of the actual documents, not of filenames.
    assert 'ardent' in b['ENG-2016-NOV-P1', '1.5.1']['memo_answer']
    assert "wasn't" in b['ENG-2017-NOV-P1', '5.2']['memo_answer']
    assert b['ENG-2014-JUL-P2', '1.1']['memo_answer'].startswith('Estha, when he was seven')
    assert 'plucking' in b['ENG-2015-JUL-P2', '1.4']['memo_answer'] or 'pluck' in b['ENG-2015-JUL-P2', '1.4']['memo_answer']
    assert 'indow-dressing' in b['ENG-2018-JUL-P1', '1.8']['memo_answer']
    # Source defects are declared, not repaired.
    assert b['ENG-2018-JUL-P1', '6.1']['printed_question_number'] == '5.1'
    assert b['ENG-2018-JUL-P1', '6.5']['printed_question_number'] == '5.5'
    assert b['ENG-2015-JUL-P2', '1.8']['printed_question_number'] == '1.8'
    p = read(ROOT / 'data/extracted/pass1/english/ENG-2018-JUL-P1.json')['paper']
    assert p['mark_discrepancies'][0]['printed_section_total'] == 25
    assert p['mark_discrepancies'][0]['sum_of_printed_item_marks'] == 24
    p16 = read(ROOT / 'data/extracted/pass1/english/ENG-2016-NOV-P1.json')['paper']
    assert p16['mark_discrepancies'][0]['printed_section_total'] == 26
    assert p16['mark_discrepancies'][0]['sum_of_printed_item_marks'] == 25
    # The 2016 Q1 records are still usable evidence for their own operation.
    assert b['ENG-2016-NOV-P1', '1.9']['memo_evidence'] == 'model_answer'
    assert b['ENG-2016-NOV-P1', '1.9']['rubric_reference'] is True
    assert b['ENG-2016-NOV-P1', '1.8']['memo_evidence'] == 'rubric_reference'
    assert b['ENG-2014-JUL-P2', '1.10']['rubric_reference'] is True
    # Alternative transactional options keep their role.
    assert b['ENG-2015-JUL-P2', '3.2']['allocation'] == 'alternative'
    assert b['ENG-2015-JUL-P2', '3.2']['memo_evidence'] == 'restated_only'


def test_headerless_memo_pairing_is_content_based():
    mod = importlib.import_module('ingestion.extraction.english_pass1_evidence_2014_p2')
    alignment = p1.verify_alignment(ROOT / mod.PAPER['paper_path'], ROOT / mod.PAPER['memo_path'], mod.PAPER)
    assert alignment['pairing_basis'] == 'content_and_printed_totals'
    assert alignment['memo_header'] == {}
    assert alignment['examiner_match'] is False
    assert 'numbered-content anchors' in alignment['verified_by']
    # A memorandum that prints a header must never be paired this way.
    other = importlib.import_module('ingestion.extraction.english_pass1_evidence_2015_p2')
    meta = dict(mod.PAPER)
    meta['paper_path'] = other.PAPER['paper_path']
    meta['memo_path'] = other.PAPER['memo_path']
    with pytest.raises(ValueError, match='prints a header'):
        p1.verify_alignment(ROOT / meta['paper_path'], ROOT / meta['memo_path'], meta)
    # A header-bearing paper must also fail the content-based checks if mis-declared.
    meta = dict(other.PAPER)
    meta['pairing_basis'] = 'content_and_printed_totals'
    with pytest.raises(ValueError):
        p1.verify_alignment(ROOT / meta['paper_path'], ROOT / meta['memo_path'], meta)


def test_orphan_2026_memo_is_not_paired_or_extracted(batch):
    audit = read(ROOT / 'data/extracted/pass1/english/_CORPUS_AUDIT.json')
    rows = {row['path']: row for row in audit}
    memo = rows['data/organized/english/Final of Grade 11 English Paper 1 July 2026 Memo.pdf']
    assert memo['disposition'] == 'rejected_no_matching_paper'
    assert memo['printed_date'] == '22 July 2025' and memo['printed_marks'] == 80
    assert memo['printed_cover_row'] == [20, 10, 15, 10, 20, 10, 85]
    assert memo['cover_row_sums_to_printed_marks'] is False
    assert not any(r['memo_document'].endswith('2026 Memo.pdf') for r in batch)
    assert len(audit) == 21


@pytest.mark.parametrize('fault', ['marks', 'date', 'examiner', 'provenance', 'source_hash', 'anchor'])
def test_pass1_failure_never_replaces_output(tmp_path, monkeypatch, fault):
    mod = importlib.import_module('ingestion.extraction.english_pass1_evidence_2016_nov')
    monkeypatch.setattr(p1, 'EXTRACTED', tmp_path)
    monkeypatch.setattr(p1, 'PER_PAPER_DIR', tmp_path / 'perpaper')
    sentinel = tmp_path / 'english_pass1.json'
    sentinel.write_text('do not replace')
    if fault == 'marks':
        rows = copy.deepcopy(mod.RECORDS)
        row = list(rows[0])
        row[1] += 1
        rows[0] = tuple(row)
        monkeypatch.setattr(mod, 'RECORDS', rows)
    elif fault in ['date', 'examiner']:
        meta = dict(mod.PAPER)
        meta['exam_date' if fault == 'date' else 'examiner'] = 'wrong'
        monkeypatch.setattr(mod, 'PAPER', meta)
    elif fault == 'provenance':
        inventory = tmp_path / 'inventory.yaml'
        inventory.write_text('sources: []\n')
        monkeypatch.setattr(p1, 'INVENTORY', inventory)
    elif fault == 'source_hash':
        meta = dict(mod.PAPER)
        meta['source_hashes'] = {'paper_path': 'wrong', 'memo_path': 'wrong'}
        monkeypatch.setattr(mod, 'PAPER', meta)
    else:  # a memorandum that stops printing an item it claims to answer
        meta = dict(mod.PAPER)
        meta['item_anchor_overrides'] = {'2.1': {'paper': 'not printed anywhere in this paper'}}
        monkeypatch.setattr(mod, 'PAPER', meta)
    assert p1.main() == 1
    assert sentinel.read_text() == 'do not replace'
    assert not (tmp_path / 'perpaper').exists()


@pytest.mark.parametrize('fault', ['partition', 'confidence', 'reference', 'single', 'visual', 'citation',
                                   'saturation', 'competence', 'ineligible'])
def test_pass2_rejects_invalid_knowledge(batch, payload, fault):
    b = copy.deepcopy(batch)
    p = copy.deepcopy(payload)
    s = read(K / 'saturation_report.json')
    if fault == 'partition':
        p['question_families'][1]['source_evidence'][0] = p['question_families'][0]['source_evidence'][0]
    if fault == 'confidence':
        p['question_families'][0]['confidence'] = 'medium'
    if fault == 'reference':
        p['diagnostic_questions'][0]['understanding_model_id'] = 'UNDERSTANDING-MISSING'
    if fault == 'single':
        p['breakdown_models'][0]['source_basis'] = p['breakdown_models'][0]['source_basis'][:1]
    if fault == 'visual':
        sid = p['question_families'][0]['source_evidence'][0]
        next(r for r in b if r['source_id'] == sid)['requires_visual_verification'] = True
    if fault == 'citation':
        p['understanding_models'][0]['required_knowledge'] = ['Unsupported claim']
    if fault == 'saturation':
        s['additional_diagnostics']['saturated'] = True
    if fault == 'competence':
        f = p['question_families'][6]
        sid = next(r['source_id'] for r in b if r['paper_number'] == 'P1'
                   and p2.eligible(r) and r['source_id'] not in f['source_evidence'])
        f['source_evidence'][0] = sid
    if fault == 'ineligible':
        sid = next(r['source_id'] for r in b if r['memo_evidence'] == 'restated_only')
        f = p['question_families'][0]
        f['source_evidence'][0] = sid
    with pytest.raises((AssertionError, KeyError)):
        p2.check_output(p, b, s)


def test_saturation_and_scope_are_honest(batch, payload):
    s = read(K / 'saturation_report.json')
    assert {'papers_in_sample', 'question_families_identified', 'families_first_observed_in_final_third',
            'strata_left_unsampled', 'families_supported_by_single_exemplar'} <= s.keys()
    assert s['papers_in_sample'] == 5 and s['question_families_identified'] == 15
    assert s['families_first_observed_in_final_third'] == 1
    assert s['families_new_in_final_third'] == ['QUESTION-FAMILY-ENG-010']
    assert not s['additional_diagnostics']['saturated']
    assert len(s['strata_left_unsampled']) == 13
    assert s['families_supported_by_single_exemplar'] == 0
    assert s['additional_diagnostics']['papers_separated_by_competence'] is True
    affected = {u['id']: u['affected'] for u in payload['unresolved_items']}
    assert len(affected['UNRES-ENG-UNASSIGNED']) == 45
    assert len(affected['UNRES-ENG-VISUAL']) == 26
    assert len(affected['UNRES-ENG-NO-MARKING-EVIDENCE']) == 13
    assert len(affected['UNRES-ENG-RUBRIC-ONLY']) == 2
    claimed = {sid for f in payload['question_families'] for sid in f['source_evidence']}
    assert not claimed.intersection(affected['UNRES-ENG-VISUAL'])
    assert not claimed.intersection(affected['UNRES-ENG-NO-MARKING-EVIDENCE'])
    assert len([u for u in payload['unresolved_items'] if u['type'] == 'single_exemplar']) == 5
    # No family may mix the two papers; the batch is split by competence.
    by_id = {r['source_id']: r for r in batch}
    for f in payload['question_families']:
        assert len({by_id[s]['paper_number'] for s in f['source_evidence']}) == 1


def test_review_queue_and_run_log(payload):
    queue = yaml.safe_load((ROOT / 'review_queue/RQ-P4-ENG-PASS2.yaml').read_text())
    assert queue['item_count'] == len(queue['items']) == len(payload['unresolved_items'])
    for item in queue['items']:
        assert all(item.get(f) for f in ['issue', 'affected_entity', 'evidence', 'possible_resolutions', 'recommended_review'])
    assert {u['id']: u['affected_entity'] for u in queue['items']} == {u['id']: u['affected'] for u in payload['unresolved_items']}
    run = ROOT / 'runs' / queue['run_id']
    meta = read(run / 'run.json')
    assert meta['subject'] == 'english' and meta['status'] == 'completed_with_review'
    for f in ['events.jsonl', 'decisions.json', 'errors.json', 'metrics.json', 'artifacts/artifacts.yaml']:
        assert (run / f).exists()
    metrics = read(run / 'metrics.json')
    assert metrics['questions_extracted'] == metrics['questions_classified'] + metrics['questions_unclassified']
    assert metrics['papers_processed'] == 5 and metrics['papers_without_local_memo'] == 10
    assert metrics['memoranda_without_matching_paper'] == 1
    assert metrics['validation_failures'] == 0 and metrics['curriculum_mapping_rate'] is None
    assert metrics['records_requiring_visual_verification'] == 26
    assert any(e['error_type'] == 'saturation_not_reached' for e in read(run / 'errors.json'))
    artifacts = yaml.safe_load((run / 'artifacts/artifacts.yaml').read_text())
    assert artifacts and all(a['content_hash'] and a['source_run'] == queue['run_id'] for a in artifacts)
    for a in artifacts:
        assert sha256_file(ROOT / a['path']) == a['content_hash'], a['path']


def test_report_and_aggregate_english_only_replaced(batch):
    report = (K / 'ENGLISH_REPORT.md').read_text()
    assert 'NOT saturated' in report and 'QUESTION-FAMILY-ENG-001' in report
    aggregate = read(ROOT / 'data/extracted/all_subjects_pass1.json')
    assert [r for r in aggregate if r['subject'] == 'english'] == batch
    original = json.loads(subprocess.check_output(
        ['git', 'show', '123baa26dc154adfa09437840bc374af4e8350d9:data/extracted/all_subjects_pass1.json'],
        cwd=ROOT, text=True))
    assert [r for r in aggregate if r['subject'] != 'english'] == [r for r in original if r['subject'] != 'english']
