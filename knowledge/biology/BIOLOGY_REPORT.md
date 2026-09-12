# Biology — Pass 1 and Pass 2 report

**Grade 11 Life Sciences · completed_with_review · not saturated**

Executed only the requested extraction, segmentation, memo alignment, taxonomy,
Understanding Model, breakdown and diagnostic work (phases 4, 5, 6, 8–11).
Phase 7 curriculum mapping and phases 12 onward were **not** executed.

## Results

| Deliverable | Result |
|---|---:|
| Usable paper–memo pairs processed | 5 |
| Question/subquestion records | 275 |
| Allocated marks, checked against printed totals | 490 |
| Question families / Understanding Models | 9 / 9 |
| Possible breakdowns / proposed diagnostics | 18 / 18 |
| Knowledge objects schema-checked | 54; zero failures |
| Records assigned / unassigned | 46 / 229 |
| Records requiring visual verification | 84; none used in families |
| Review items | 19 |

This is a **partial, unvalidated assessment knowledge bank**, not a complete biology
curriculum or a validated tutor. Every model is `unvalidated`, version `0.1.0-draft`.
The limited classification rate is intentional: unverified figures, disputed marking
and insufficiently repeated competences were not replaced with plausible general knowledge.

## Pass 1: question evidence, not document stubs

| Paper key | Printed date | Questions | Marks | ORC paper / memo IDs |
|---|---|---:|---:|---|
| BIO-2022-CYCLE1 | 9 February 2022 | 26 | 50 | SOURCE-ORC-BIO-2022-006 / -005 |
| BIO-2022-CIRC | 16 May 2022 | 29 | 50 | SOURCE-ORC-BIO-2022-002 / -001 |
| BIO-2023-JUL | 21 July 2023 | 78 | 150 | SOURCE-ORC-BIO-2023-020 / -019 |
| BIO-2023-MICRO | 2 October 2023 | 29 | 40 | SOURCE-ORC-BIO-2023-018 / -017 |
| BIO-2023-NOV | 24 November 2023 | 113 | 200 | SOURCE-ORC-BIO-2023-022 / -021 |

Each record includes the actual question text, memo answer and marking notes,
source and memo pages, shared context, source-file SHA-256 hashes, ORC IDs, visual
flags and terminology present in its own evidence. Text is taken from the digital
PDF layer; blank answer lines, repeating headers and whitespace layout are normalized.
Extended source passages are referenced rather than reproduced. Tables remain in
text where readable; image connections and placements are explicitly unresolved.
Memo ticks are retained; `memo_method_steps` segments their text without asserting
that ticks imply an ordered biological procedure.

The authored `PAPER`, `SCHEMA`, `RECORDS` modules also carry `LOCATORS` and pinned
`SOURCE_HASHES`. Parent IDs resolve to non-mark-bearing stem objects in each per-paper
file. `rowN` is an analytical identifier for an originally unnumbered matching row;
lettered components retain their source letters. A printed numbered item with a
single aggregate allocation remains one question when its individual answers have
no separately printed allocation.

The builder fails **before replacing output** if headers disagree, any subtotal or
total is wrong, source bytes changed, or the inventory lookup is absent/ambiguous.
It checks printed DATE, MARKS and EXAMINER, cover question totals, memo question
totals and source-content anchors. The cycle-test memo lacks top-level totals;
its explicitly printed grouped allocations are checked as 5+4+13 and 15+13 instead.

The inherited document-level stubs and `sample_manifest.json` pairings are not used.
Only biology entries in `all_subjects_pass1.json` were replaced; other subjects and
all original files under `data/organized/` remain unchanged.

### Important findings and exclusions

1. **Microorganisms ambiguity resolved.** Test 1, Test 2 and the memo have matching
   dates and totals. The memo's penicillin investigation, Q2.1 “Type of bacteria”
   and Q2.7.B “Penicillin” match **Test 1**. Test 2 instead uses Vibramycin and asks
   for a dependent variable at Q2.1. The inventory lists a separate Test 2 MG.docx,
   but it is not in the local sample. It was not substituted or guessed.
2. **2022 year-end pair rejected.** Its cover and body allocate 70+30+30+40 = **160**,
   while the total is printed as **170**. The memo labels Q3 as 40 although its
   subsections are 16+9+5 = 30. The prompt's mandatory total check therefore blocks
   this pair. No ten-mark balancing question, guessed mark or corrected total was
   invented. It is excluded from the Pass 1 batch and saturation sample pending
   examiner clarification (`UNRES-BIO-001`). This is why there are five usable pairs,
   even after resolving the microorganisms ambiguity.
3. **Eight papers have no matching local memo:** Circulation Test 2; Microorganisms
   Test 2; nervous system; skeletal system; excretion and skeletal system; Cycle
   Test 2; excretion class test; November Paper 2. They supply no marking evidence
   in this run. Together with the rejected year-end pair, these account for the
   nine of fourteen local papers not admitted.
4. **The prompt's date summary needs a correction:** Circulation Test 2 prints
   “FEBRUARY 2024”, without a day. It does not have an entirely absent date.
5. **ORC title lookup needed year disambiguation.** The circulation paper/MG titles
   occur in both 2022 and 2024 inventory entries. Normalized title plus verified
   printed year resolves the correct IDs. The inventory still describes organized
   copies as inaccessible; reconciliation remains review work, not a silent edit.
6. **Memo defects remain visible.** Examples include “radium” in July bone labelling,
   rate units for November's one-hour blood volume, snail wording in the lady-bug
   calculation, the excretion/colon boundary and differing accounts of blood-pressure
   fluctuation. The affected disputed requirements are not synthesized into families.

The entry point writes a hashed `_CORPUS_AUDIT.json` classifying all 20 assessment
files and two source booklets, including dispositions for omitted material.

## Pass 2: evidence-led competences

| ID suffix | Family | Members | Papers | Confidence |
|---|---|---:|---:|---|
| BIO-001 | Recognise microorganism terminology | 22 | 2 | medium |
| BIO-002 | Identify the independent variable | 3 | 3 | medium |
| BIO-003 | Identify the measured response | 2 | 2 | medium |
| BIO-004 | Specify controls that keep comparisons fair | 6 | 3 | high |
| BIO-005 | Apply water balance to urine outcomes | 3 | 2 | medium |
| BIO-006 | Explain osteoarthritis through cartilage damage | 2 | 2 | medium |
| BIO-007 | Distinguish controllable/uncontrollable circulatory risks | 3 | 2 | medium |
| BIO-008 | Link oxygen delivery to cellular energy demands | 2 | 2 | medium |
| BIO-009 | State a conclusion from a biological comparison | 3 | 3 | medium |

Recall is not merged with mechanism explanation simply because the topic matches.
Family membership is a partition of the **assigned subset**, not a claim to cover
all questions. Every unassigned source ID is listed in `UNRES-BIO-UNASSIGNED`.
Every family has independent questions from at least two papers. Confidence is
computed: high requires at least four members across at least three distinct paper
hashes. Only the fixed-variable family meets that rule.

All nine models have the full §9 field list and provenance. Substantive model
claims carry explicit supporting source IDs. Each model has two possible breakdowns
and two open diagnostics. Breakdowns cite the same member memo evidence; the summary
includes their literal `memo_marking_notes` basis. Possible failures and diagnostic
interpretations are marked Tier 3, not observed student states. No psychological
or curriculum claims were added from outside the batch.

One-off patterns remain deferred: the antibiotic-resistance explanation, antibiotic
hypothesis formulation, mark-recapture calculation, within-sitting population
terminology, and biological drawings whose memo diagrams have not been verified.
Local partial-credit rules—“fatigue” alone and both table entries correct—are not
promoted into universal marking requirements.

### Schema compatibility

The existing family schema forbids extra properties. As in physics, persisted
families use `question_family_id`, `name`, `source_evidence` and `definition`.
The summary preserves membership aliases, distinguishing features and mark ranges.
`pass2_output.json` contains **exactly the five requested arrays**; the separate
`saturation_report.json` contains the saturation object. No schema was weakened.

## Saturation report

| Required field | Value |
|---|---|
| papers_in_sample | 5 |
| question_families_identified | 9 |
| families_first_observed_in_final_third | 1 |
| strata_left_unsampled | 5 explicitly described gaps/strata |
| families_supported_by_single_exemplar | 0 admitted families |

The last field counts admitted families, not deferred candidates. The JSON reports
single-exemplar review items separately so zero cannot be mistaken for complete coverage.

Order used is **addition to this new question-level batch**, recorded by the Pass 1
module sequence—not an asserted historical download order:

- First third: Cycle Test 1 → circulation test.
- Middle third: July 2023 Paper 1.
- Final third: microorganisms test → November 2023 Paper 1.

BIO-008 occurs entirely in the final third. **Not saturated.** Five papers are also
below the recommended 8–15 and the batch omits the rejected year-end assessment,
Paper 2, 2024 class tests and other unpaired tests. External-board/preliminary
coverage and applicability remain unverified, not presumed school requirements.

The files in `biology/curriculum/` are exam **source booklets**, not a syllabus or ATP.
No numerical curriculum-mapping rate or authoritative list of missing curriculum
topics can be established from them.

## Reproduction, tests and logs

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python scripts/run_biology_pass2.py
python -m pytest
```

Entry point: `scripts/run_biology_pass2.py`.
Review queue: `review_queue/RQ-P4-BIO-PASS2.yaml` (all affected IDs retained, not truncated).
Run ID: `STATUS.md` and the review queue identify the corresponding `runs/` directory.
Each run writes events, decisions, errors, metrics and a SHA-256 artifact manifest,
with status **completed_with_review**.

`tests/test_biology_pass2.py` executes both builders in temporary directories,
compares their outputs with committed artifacts, and checks provenance, schema
validity, references, partitioning, confidence, saturation and review/log format.
Validation on 2026-09-12: **78 tests passed**, including 21 biology checks.
Negative tests cover marks, header, missing inventory, changed source hash, wrong
same-date microorganism pairing, duplicate membership, unsupported claims and
unverified visual evidence.

**Next work:** obtain examiner clarification for the year-end total; acquire the
missing memoranda and syllabus/ATP; visually verify the 84 flagged questions;
then extend the evidence batch and rerun synthesis. Human validation is still owed.
