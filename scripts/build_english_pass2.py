#!/usr/bin/env python3
"""Build English Pass 2 from the question-level Pass 1 batch ONLY; validate before publishing."""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.schema import SchemaValidator  # noqa: E402
from ingestion.analysis.english_pass2_families import FAMILIES  # noqa: E402
from ingestion.analysis.english_pass2_models import MODELS  # noqa: E402
from ingestion.analysis.english_pass2_unresolved import DEFERRED, QUESTION_ISSUES, UNRESOLVED  # noqa: E402

PASS1_BATCH = ROOT / 'data/extracted/english_pass1.json'
OUT_DIR = ROOT / 'knowledge/english'
# Order in which the pairs entered THIS question-level batch (not historical
# download order, and not inferred from the unreliable manifest).
ACQUISITION_ORDER = ['ENG-2014-JUL-P2', 'ENG-2015-JUL-P2', 'ENG-2016-NOV-P1', 'ENG-2017-NOV-P1', 'ENG-2018-JUL-P1']
ARRAYS = ['question_families', 'understanding_models', 'breakdown_models', 'diagnostic_questions', 'unresolved_items']

ELIGIBLE_EVIDENCE = 'model_answer'


def compute_confidence(records):
    """Mechanical, not authored: 4+ members across 3+ papers is high, otherwise medium."""
    if len(records) < 2:
        return 'low'
    if any(r['requires_visual_verification'] or r['ocr_uncertain'] or r['fidelity_rung'] != 'A' for r in records):
        return 'medium'
    return 'high' if len(records) >= 4 and len({r['paper_key'] for r in records}) >= 3 else 'medium'


def eligible(record):
    return (record['memo_evidence'] == ELIGIBLE_EVIDENCE
            and bool(record['memo_answer'])
            and not record['memo_answer'].startswith('NOT ANSWERED')
            and not record['requires_visual_verification']
            and not record['ocr_uncertain'])


def check_output(payload, batch, saturation):
    """Public invariant gate; also exercised against mutations by the tests."""
    by_id = {r['source_id']: r for r in batch}
    assert len(by_id) == len(batch), 'Duplicate Pass 1 source IDs'
    claimed = set()
    family_by, models, breakdowns, diagnostics = {}, {}, {}, {}
    validator = SchemaValidator(ROOT / 'database/schema')
    count = 0
    for name, schema, idkey, target in [
        ('question_families', 'question_family', 'question_family_id', family_by),
        ('understanding_models', 'knowledge_model', 'identity', models),
        ('breakdown_models', 'breakdown', 'breakdown_id', breakdowns),
        ('diagnostic_questions', 'diagnostic', 'diagnostic_id', diagnostics),
    ]:
        for obj in payload[name]:
            assert obj[idkey] not in target, 'Duplicate object ID'
            target[obj[idkey]] = obj
            result = validator.validate(schema + '.schema.json', obj)
            assert result.valid, result.errors
            count += 1
    for f in family_by.values():
        ids = f['source_evidence']
        assert len(set(ids)) == len(ids) >= 2, 'A family needs two distinct members'
        assert not claimed.intersection(ids), 'Family membership overlaps'
        assert set(ids) <= by_id.keys(), 'Unknown source ID'
        rs = [by_id[s] for s in ids]
        assert all(r['subject'] == 'english' for r in rs)
        assert all(eligible(r) for r in rs), 'Ineligible member in a family'
        assert len({r['paper_key'] for r in rs}) >= 2, 'Family confined to one paper'
        assert len({r['paper_number'] for r in rs}) == 1, 'Family mixes Paper 1 and Paper 2 competences'
        assert f['confidence'] == compute_confidence(rs)
        assert f['frequency'] == len(ids)
        claimed.update(ids)
    required = {'identity', 'definition', 'subject', 'grade', 'topic', 'question_family',
                'assessment_operations', 'required_knowledge', 'prerequisites', 'required_reasoning',
                'required_procedure', 'evidence_of_understanding', 'marking_requirements',
                'common_breakdowns', 'misconceptions', 'diagnostic_dimensions', 'diagnostic_questions',
                'source_references', 'confidence', 'validation_state', 'version', 'provenance'}
    assert len(models) == len(family_by)
    assert {m['question_family'] for m in models.values()} == set(family_by)
    for m in models.values():
        assert required == set(m)
        f = family_by[m['question_family']]
        assert m['source_references'] == f['source_evidence'] and m['confidence'] == f['confidence']
        assert m['validation_state'] == 'unvalidated' and m['version'] == '0.1.0-draft'
        assert set(m['source_references']) <= set(m['provenance'])
        for field in ['definition', 'required_knowledge', 'prerequisites', 'required_reasoning',
                      'required_procedure', 'evidence_of_understanding', 'marking_requirements', 'misconceptions']:
            claims = m[field] if isinstance(m[field], list) else [m[field]]
            for claim in claims:
                assert sum(sid in claim for sid in m['source_references']) >= 2, 'Uncited claim'
        assert 2 <= len(m['diagnostic_questions']) <= 4
        assert set(m['common_breakdowns']) <= breakdowns.keys()
        assert set(m['diagnostic_questions']) <= diagnostics.keys()
        for bid in m['common_breakdowns']:
            assert breakdowns[bid]['parent_understanding_model'] == m['identity']
        for did in m['diagnostic_questions']:
            assert diagnostics[did]['understanding_model_id'] == m['identity']
    for b in breakdowns.values():
        m = models[b['parent_understanding_model']]
        assert len(set(b['source_basis'])) >= 2
        assert set(b['source_basis']) <= set(m['source_references'])
        assert all(by_id[sid]['memo_marking_notes'] for sid in b['source_basis'])
        assert set(b['distinguishing_questions']) <= diagnostics.keys()
        assert b['confidence'] == compute_confidence([by_id[sid] for sid in b['source_basis']])
    for d in diagnostics.values():
        m = models[d['understanding_model_id']]
        assert d['target_breakdown'] in m['common_breakdowns']
        assert set(d['distinguishes']) <= set(m['common_breakdowns'])
        assert len(d['distinguishes']) >= 2
        assert sum(sid in d['source_or_rationale'] for sid in m['source_references']) >= 2
    unassigned = set(by_id) - claimed
    unres = {u['id']: u for u in payload['unresolved_items']}
    assert unassigned == set(unres['UNRES-ENG-UNASSIGNED']['affected'])
    assert {r['source_id'] for r in batch if r['requires_visual_verification']} == set(unres['UNRES-ENG-VISUAL']['affected'])
    assert {r['source_id'] for r in batch if r['memo_evidence'] in {'none', 'restated_only'}} == set(unres['UNRES-ENG-NO-MARKING-EVIDENCE']['affected'])
    for u in unres.values():
        assert all(u.get(k) for k in ['type', 'summary', 'detail', 'affected', 'evidence', 'recommended_review'])
    order = saturation['acquisition_order_used']
    assert set(order) == {r['paper_key'] for r in batch} and len(set(order)) == len(order)
    n = len(order)
    thirds = [order[:round(n / 3)], order[round(n / 3):round(2 * n / 3)], order[round(2 * n / 3):]]
    assert saturation['thirds_split'] == thirds
    new = [f['question_family_id'] for f in family_by.values()
           if {by_id[s]['paper_key'] for s in f['source_evidence']} <= set(thirds[-1])]
    assert saturation['papers_in_sample'] == n
    assert saturation['question_families_identified'] == len(family_by)
    assert saturation['families_first_observed_in_final_third'] == len(new)
    assert saturation['families_new_in_final_third'] == new
    if new or n < 8 or saturation['strata_left_unsampled']:
        assert saturation['additional_diagnostics']['saturated'] is False
    return count


def build(batch):
    by_pair = {(r['paper_key'], r['question_number']): r for r in batch}
    assert len(by_pair) == len(batch)
    payload = {key: [] for key in ARRAYS}
    summary_families = []

    def resolve(pairs):
        return [by_pair[tuple(p)]['source_id'] for p in pairs]

    for i, f in enumerate(FAMILIES, 1):
        ids = resolve(f['members'])
        rs = [by_pair[tuple(p)] for p in f['members']]
        assert len(set(ids)) >= 2
        assert all(eligible(r) for r in rs), f'{f["family_id"]} has an ineligible member'
        assert len({r['paper_number'] for r in rs}) == 1, f'{f["family_id"]} mixes papers'
        confidence = compute_confidence(rs)
        cite = ' [sources: ' + ', '.join(ids) + ']'
        claim = lambda text: '[Tier 2 derived, unvalidated] ' + text + cite
        model = MODELS[i]
        mid = f'UNDERSTANDING-ENG-{i:03d}'
        bids = [f'BREAKDOWN-ENG-{i:03d}-{s}' for s in 'AB']
        dids = [f'DIAG-ENG-{i:03d}-{s}' for s in 'AB']
        payload['question_families'].append({
            'question_family_id': f['family_id'], 'name': f['name'], 'definition': claim(f['definition']),
            'subject': 'english', 'grade': '11', 'topics': [f['topic']],
            'assessment_operations': f['operations'], 'representative_questions': ids[:3],
            'frequency': len(ids), 'source_evidence': ids, 'confidence': confidence,
            'validation_status': 'unvalidated'})
        payload['understanding_models'].append({
            'identity': mid, 'definition': claim(f['definition']), 'subject': 'english', 'grade': '11',
            'topic': f['topic'], 'question_family': f['family_id'], 'assessment_operations': f['operations'],
            'required_knowledge': [claim(model['knowledge'])], 'prerequisites': [claim(model['prerequisites'])],
            'required_reasoning': [claim(model['reasoning'])], 'required_procedure': claim(model['procedure']),
            'evidence_of_understanding': [claim(model['evidence'])],
            'marking_requirements': [claim(model['marking'])],
            'common_breakdowns': bids,
            'misconceptions': ['[Tier 3 possible belief, not observed] ' + model['misconception'] + cite],
            'diagnostic_dimensions': [b[0] for b in model['breakdowns']],
            'diagnostic_questions': dids, 'source_references': ids,
            'confidence': confidence, 'validation_state': 'unvalidated', 'version': '0.1.0-draft',
            'provenance': [f['family_id']] + ids + sorted({r[k] for r in rs for k in ['orc_source_id', 'orc_memo_source_id']})})
        for j, (stage, description, signal) in enumerate(model['breakdowns']):
            payload['breakdown_models'].append({
                'breakdown_id': bids[j], 'description': '[Tier 3 possible failure] ' + description + cite,
                'parent_understanding_model': mid, 'stage': stage,
                'observable_signals': [signal + cite],
                'possible_confusions': [model['breakdowns'][1 - j][1] + cite],
                'distinguishing_questions': dids, 'source_basis': ids, 'confidence': confidence})
        for j, (question, evidence) in enumerate(model['diagnostics']):
            payload['diagnostic_questions'].append({
                'diagnostic_id': dids[j], 'understanding_model_id': mid, 'target_breakdown': bids[j],
                'question': question,
                'purpose': '[Tier 3] Distinguish ' + model['breakdowns'][j][1] + ' from ' + model['breakdowns'][1 - j][1],
                'distinguishes': bids, 'expected_evidence': ['[Tier 3] ' + evidence + cite],
                'follow_up_conditions': [{'condition': 'The answer names the feature but states no effect.',
                                          'follow_up': 'What does that feature make the reader notice or feel here?'}],
                'source_or_rationale': '[Tier 3 proposed diagnostic, not validated on learners] ' + model['marking'] + cite,
                'confidence': confidence})
        summary_families.append({
            'family_id': f['family_id'], 'name': f['name'], 'members': len(ids),
            'papers': sorted({r['paper_key'] for r in rs}), 'paper_number': rs[0]['paper_number'],
            'confidence': confidence, 'marks_range': [min(r['marks'] for r in rs), max(r['marks'] for r in rs)],
            'distinguishing_features': f['definition'], 'member_source_ids': ids,
            'breakdown_memo_basis': {r['source_id']: r['memo_marking_notes'] for r in rs}})
    unresolved = copy.deepcopy(UNRESOLVED)
    for i, u in enumerate(unresolved, 1):
        u['id'] = f'UNRES-ENG-{i:03d}'
    for typ, title, detail, pairs in QUESTION_ISSUES:
        ids = resolve(pairs)
        unresolved.append({'id': f'UNRES-ENG-{len(unresolved) + 1:03d}', 'type': typ, 'summary': title,
                           'detail': detail + ' Affected records: ' + ', '.join(ids) + '.',
                           'affected': ids, 'evidence': ids,
                           'recommended_review': 'Confirm the printed allocation with the examiner; preserve the source wording and do not pad or renumber it.'})
    for typ, title, pairs in DEFERRED:
        ids = resolve(pairs)
        unresolved.append({'id': f'UNRES-ENG-{len(unresolved) + 1:03d}', 'type': typ, 'summary': title,
                           'detail': 'Deferred candidate: this operation is observed once in the batch (' + ', '.join(ids) + ') and cannot support a family or any claim needing two independent sources.',
                           'affected': ids, 'evidence': ids,
                           'recommended_review': 'Acquire further sittings or class material containing the same operation before promoting it.'})
    claimed = {s for f in payload['question_families'] for s in f['source_evidence']}
    by_id = {r['source_id']: r for r in batch}
    for name, ids, detail in [
        ('UNASSIGNED', sorted({r['source_id'] for r in batch} - claimed),
         'Records that do not fit an admitted, independently supported family remain unassigned; no coverage is implied by their absence.'),
        ('VISUAL', [r['source_id'] for r in batch if r['requires_visual_verification']],
         'These records depend on an image, advertisement or cartoon that the text layer cannot verify. Their text and memorandum answers are retained in Pass 1, but none contributes to a Pass 2 family or model.'),
        ('NO-MARKING-EVIDENCE', [r['source_id'] for r in batch if r['memo_evidence'] in {'none', 'restated_only'}],
         'The summary, essay and transactional records whose memoranda print no model answer or rubric cannot ground any marking requirement or breakdown model.'),
        ('RUBRIC-ONLY', [r['source_id'] for r in batch if r['rubric_reference'] and r['memo_evidence'] == 'rubric_reference'],
         'These records are to be marked against an IEB rubric that the supplied memorandum does not print, so no level descriptors or criteria could be transcribed.')]:
        unresolved.append({'id': 'UNRES-ENG-' + name,
                           'type': 'fidelity' if name in {'VISUAL', 'RUBRIC-ONLY'} else 'coverage_gap',
                           'summary': f'{len(ids)} {name.lower().replace("-", " ")} question records',
                           'detail': detail + ' This is a view over the batch; it overlaps the other views and the unassigned set.',
                           'affected': ids, 'evidence': ids,
                           'recommended_review': 'Review the source documents (and the rubric, where one exists) before treating these records as evidence.'})
    payload['unresolved_items'] = unresolved
    order = ACQUISITION_ORDER
    n = len(order)
    thirds = [order[:round(n / 3)], order[round(n / 3):round(2 * n / 3)], order[round(2 * n / 3):]]
    new = [f['question_family_id'] for f in payload['question_families']
           if {by_id[s]['paper_key'] for s in f['source_evidence']} <= set(thirds[-1])]
    sat = {'papers_in_sample': n, 'question_families_identified': len(FAMILIES),
           'families_first_observed_in_final_third': len(new),
           'strata_left_unsampled': [
               'July 2013 Paper 1 (no readable header block, no memorandum)',
               'July 2014 Paper 1 (no local memorandum)',
               'July 2015 Paper 1 (no local memorandum; printed total conflict)',
               'July 2016 Paper 1 (no local memorandum; printed total conflict)',
               'July 2017 Paper 1 (no local memorandum)',
               'November 2014 Paper 1 (no local memorandum)',
               'November 2015 Paper 1 (no local memorandum)',
               'November 2018 Paper 1 PDF (no local memorandum; printed total conflict)',
               'Paper 2 July 2016 (no local memorandum)',
               'Paper 2 July 2017 (no local memorandum; printed total conflict)',
               'The orphaned 2025/2026 Paper 1 memorandum (no matching paper)',
               'Essay and transactional writing (no marking evidence in any local memorandum)',
               'Visual literacy (all local evidence is image-dependent)'],
           'families_supported_by_single_exemplar': 0,
           'acquisition_order_used': order,
           'acquisition_order_basis': 'Order in which the five verified pairs entered this question-level Pass 1 batch; not inferred historical download order.',
           'thirds_split': thirds, 'families_new_in_final_third': new,
           'additional_diagnostics': {
               'saturated': False,
               'reason_not_saturated': 'A family (the dictionary-entry operation) is first observed in the final third of the batch; five papers are well below the recommended 8-15; thirteen strata are unsampled and 45 records remain unassigned (26 of them image-dependent).',
               'deferred_single_exemplar_candidates': sum(u['type'] == 'single_exemplar' for u in unresolved),
               'records_unassigned': len(batch) - len(claimed),
               'records_image_dependent': len([r for r in batch if r['requires_visual_verification']]),
               'records_without_marking_evidence': len([r for r in batch if r['memo_evidence'] in {'none', 'restated_only'}]),
               'set_texts_represented': ['The God of Small Things (one sitting)', 'Othello (one sitting)'],
               'papers_separated_by_competence': True}}
    checked = check_output(payload, batch, sat)
    summary = {'subject': 'english', 'question_records_in_batch': len(batch), 'papers_in_sample': n,
               'records_assigned_to_a_family': len(claimed), **{k: len(v) for k, v in payload.items()},
               'schema_validation': {'checked': checked, 'failed': 0}, 'families': summary_families,
               'confidence_distribution': dict(Counter(f['confidence'] for f in payload['question_families'])),
               'errors': []}
    return payload, sat, summary


def main():
    try:
        batch = json.loads(PASS1_BATCH.read_text())
        if len({r['paper_key'] for r in batch}) < 2:
            raise ValueError('Pass 2 blocked: fewer than two usable pairs')
        payload, sat, summary = build(batch)
    except (AssertionError, ValueError, KeyError, OSError) as exc:
        print(f'English Pass 2 FAILED (no outputs replaced): {exc}', file=sys.stderr)
        return 1
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    outputs = {k + '.json': v for k, v in payload.items()}
    outputs.update({'pass2_output.json': payload, 'saturation_report.json': sat, '_PASS2_SUMMARY.json': summary})
    for name, obj in outputs.items():
        (OUT_DIR / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')
    print(f"English Pass 2: {summary['question_families']} families, {summary['understanding_models']} models, "
          f"{summary['breakdown_models']} breakdowns, {summary['diagnostic_questions']} diagnostics; "
          f"{summary['schema_validation']['checked']} schema-valid objects. NOT saturated.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
