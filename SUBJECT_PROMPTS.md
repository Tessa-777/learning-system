# Per-subject Pass 1 + Pass 2 prompts

One prompt per subject. Point an AI at this branch
(`arena/01a091a0-learning-system`), paste the **shared preamble** first, then the
**subject block** for the subject you want. Do one subject per session.

Physics is already done — do not redo it. Use it as the reference implementation.

| Subject | Corpus | Expected yield | Blocking issue |
|---|---|---|---|
| biology | 20 files, all readable, 6 memo-named | good (≈6 papers) | none |
| chemistry | 28 files, all readable, 12 memo-named | best (≈11 papers) | none |
| english | 21 files, all readable, 6 memo-named | modest (≈4 papers) | dates not printed in most `.docx` |
| history | 15 files, all readable, 2 memo-named | **too thin** | only 1 paper+memo pair exists |
| ap_mathematics | 21 files, **only 8 readable** | **blocked** | 13 PDFs are scanned images |
| mathematics | 29 files, 19 readable | **too thin** | 10 scanned; most files are notes, not exams |

---

# SHARED PREAMBLE — paste this into every subject run

```text
You are continuing work in the repository `learning-system` on branch
`arena/01a091a0-learning-system`. Before writing anything, read these in full:

  AGENTS.md                  12 absolute rules — provenance, no fabrication, phase discipline
  TWO_PASS_PROMPTS.md        the Pass 1 / Pass 2 method you are executing
  SYSTEM_SPEC.md             the system, now scoped to SEVEN subjects (chemistry added 2026-09-12)
  IMPLEMENTATION_SPEC.md     phases 4, 5, 6, 8, 9, 10, 11 are the ones you will touch
  RUN_LOG_SPEC.md            the run directory you must write
  STATUS.md                  current state
  knowledge/physics/PASS2_REPORT.md   what a finished subject looks like, including its limits

PHYSICS IS THE REFERENCE IMPLEMENTATION. Read these before you start and mirror
their structure exactly for your subject:

  ingestion/extraction/physics_pass1_evidence_2019.py   Pass 1 evidence table (PAPER, SCHEMA, RECORDS)
  ingestion/analysis/physics_pass2_families.py          authored families + member lists
  ingestion/analysis/physics_pass2_models.py            models, breakdowns, diagnostics, deferred candidates
  ingestion/analysis/physics_pass2_unresolved.py        authored unresolved items
  scripts/build_physics_pass1.py                        expands evidence -> Pass 1 batch, verifies it
  scripts/build_physics_pass2.py                        Pass 2 builder + every invariant
  scripts/run_physics_pass2.py                          entry point: builds, logs the run, writes the review queue
  tests/test_physics_pass2.py                           the checks your subject must also pass

============================================================
THE MOST IMPORTANT RULE
============================================================
Do NOT use `scripts/complete_subject_pass1.py` or the existing
`data/extracted/<subject>_pass1.json` files as Pass 1 output. Those are
DOCUMENT-LEVEL stubs: one record per PDF, where `question_text` is the paper's
COVER PAGE, `marks` is the whole paper's total, `memo_answer` is the memo's
cover page, and `question_type`, `topic_guess` and `memo_marking_notes` are
'unresolved' for 100% of records. Pass 2 cannot synthesise anything from them.
Any family or Understanding Model derived from them would be invented, which
AGENTS.md rule 4 and TWO_PASS_PROMPTS both forbid.

Pass 1 must produce ONE RECORD PER QUESTION, read out of the actual paper and
its actual memorandum.

============================================================
PASS 1 — what you must produce
============================================================
For each usable paper+memo pair, author an evidence module
`ingestion/extraction/<subject>_pass1_evidence_<year>.py` containing:

  PAPER   = {paper_key, paper_path, memo_path, year, exam_date, exam_period,
             paper_type, exam_board, total_marks, examiner, moderator,
             duration_stated, fidelity_rung, notes}
  SCHEMA  = ("qn","marks","topic","qtype","text","has_diagram","formulae",
             "memo_answer","memo_steps","memo_notes","needs_visual","ocr_uncertain")
  RECORDS = one tuple per question/sub-question, transcribed from the source

Then write `scripts/build_<subject>_pass1.py` (copy the physics one) which:
  * expands the evidence modules into `data/extracted/<subject>_pass1.json`
    and `data/extracted/pass1/<subject>/<PAPER_KEY>.json`
  * FAILS if any paper's per-question marks do not sum to its printed total
  * FAILS if a paper/memo pairing does not agree on its printed header
  * records `source_document_sha256` and `memo_document_sha256`
  * resolves `orc_source_id` / `orc_memo_source_id` from
    `data/raw/<subject>/SOURCE_INVENTORY.yaml` by title, and FAILS if absent

HARD RULES FOR PASS 1
  * Verify every paper↔memo pairing from the PRINTED header (DATE, MARKS,
    EXAMINER) plus the "Question Total" row. NEVER trust
    `data/organized/sample_manifest.json` — it is known to pair papers with a
    memorandum from a different sitting.
  * Never alter, rename or move a file in `data/organized/`. Read only.
  * Transcribe what the source says. If a figure, table or answer is an image
    you cannot read, set `needs_visual=True` and record it as unresolved. Never
    guess a stem, a mark or an answer.
  * `.docx` files are readable without new dependencies:
        import zipfile, re
        xml = zipfile.ZipFile(p).read('word/document.xml').decode('utf8','ignore')
        text = re.sub(r'<[^>]+>', '', re.sub(r'</w:p>', '\n', xml))
  * `pypdf` is in requirements.txt for PDFs.

============================================================
PASS 2 — what you must produce
============================================================
Only after Pass 1 is real. Follow TWO_PASS_PROMPTS "PASS 2" exactly:

  * every claim cites ≥2 independent source_ids, else it goes to
    unresolved_items tagged `single_exemplar`
  * no outside or general knowledge — only what the batch shows
  * a family needs ≥2 members; membership must be a PARTITION (no record in two
    families); records fitting no family are reported unassigned
  * `confidence` must be COMPUTED from member evidence (high needs ≥4 members
    across ≥3 papers; never high on one paper) — never authored
  * understanding models carry the full §9 field list, `validation_state:
    "unvalidated"`, `version: "0.1.0-draft"`, plus `provenance`
  * breakdowns are grounded in `memo_marking_notes` and cite their source_ids
  * 2–4 diagnostics per model, none of which gives the answer away
  * the SATURATION REPORT with the five exact fields; you may NOT declare
    saturation while `families_first_observed_in_final_third > 0`
  * if the batch is too small or too uniform, SAY SO and record it. Do not fill
    the gap with plausible-sounding claims.

Write the output to `knowledge/<subject>/` as the physics run does, including
`pass2_output.json` (the single five-array object) and `<SUBJECT>_REPORT.md`.

============================================================
WHEN YOU FINISH
============================================================
  1. `python scripts/run_<subject>_pass2.py`   -> must exit 0
  2. `python -m pytest`                        -> all tests pass
  3. Write `tests/test_<subject>_pass2.py` mirroring the physics tests: execute
     both builders into a temp dir, then re-check the committed artifacts
     (partition, computed confidence, referential integrity, schema validity,
     saturation rules, ORC provenance chain, review-queue format).
  4. A run directory under `runs/` with events, decisions, errors, metrics and
     hashed artifacts, status `completed_with_review` — never `completed` just
     because the code ran (RUN_LOG_SPEC §11).
  5. `review_queue/RQ-P4-<SUBJ>-PASS2.yaml`, every item stating issue, affected
     entity, evidence, possible resolutions and a recommended review.
  6. Update `STATUS.md`.
  7. Commit and push to `arena/01a091a0-learning-system`.

STOP CONDITIONS — record them, do not work around them
  * A subject with fewer than 2 usable paper+memo pairs cannot support Pass 2.
    Build Pass 1, then write the saturation report saying it is not saturated
    and stop. Do not manufacture families.
  * If a file has no text layer (scanned image), you cannot extract it. Record
    it as an unresolved acquisition item and move on.
```

---

# SUBJECT BLOCKS

## biology

```text
SUBJECT: biology (Life Sciences, Grade 11)

CORPUS — verified: data/organized/biology holds 20 files, all with a readable
text layer, 6 of them memorandum-named, 19 carrying a printed DATE.

Files, with the printed DATE verified from each text layer (memo in the right
column where one exists):

  Class test- circulation.pdf              16 MAY 2022      Class test- circulation MG.pdf            16 MAY 2022
  Class test 2- circulation.pdf            (no DATE)        —
  Class test- microorganisms.pdf            2 OCTOBER 2023  Class test- microorganisms MG.pdf          2 OCTOBER 2023
  Class test 2- microorganisms.pdf          2 OCTOBER 2023  (ambiguous — see traps)
  Class test- nervous system.pdf           10 OCTOBER 2022  —
  Class test- skeletal system.pdf          13 JUNE 2024     —
  Class test- excretion and skeletal system.pdf  14 JUNE 2023  —
  Grade 11 cycle test 1.pdf                 9 FEBRUARY 2022 Grade 11 cycle test 1 MG.pdf               9 FEBRUARY 2022
  Grade 11 cycle test 2.pdf                 9 MARCH 2022    —
  Grade 11 excretion class test.pdf        16 FEBRUARY 2022 —
  July exam p1.pdf                         21 JULY 2023     July exam p1 MG.pdf                       21 JULY 2023
  November exam paper 1.pdf                24 NOVEMBER 2023 November exam paper 1 MG.pdf              24 NOVEMBER 2023
  November exam paper 2.pdf                20 NOVEMBER 2023 —
  Year-end exam P1.pdf                     24 NOVEMBER 2022 Year-end exam P1 MG.pdf                   24 NOVEMBER 2022

That is FIVE date-verified pairs plus one ambiguous case — not six.

TRAPS YOU MUST HANDLE
  * THE MICROORGANISMES AMBIGUITY: "Class test- microorganisms.pdf" and
    "Class test 2- microorganisms.pdf" are BOTH dated 2 OCTOBER 2023, and there
    is only ONE microorganisms memo, also dated 2 OCTOBER 2023. Date matching
    cannot decide which paper the memo belongs to. Decide from content —
    question numbering, total marks, and the memo's own question headings — and
    if you cannot decide, extract only the paper you can prove and log the
    other as unresolved. Do not guess.
  * There are TWO circulation class tests. Only the one dated 16 MAY 2022 has a
    matching memo; "Class test 2- circulation.pdf" prints no DATE at all.
  * The document-level stubs paired the nervous-system paper (10 OCTOBER 2022)
    with a memo dated 16 MAY 2022 — a different sitting. Six of fourteen stub
    records were mispaired that way. Verify every pair yourself.
  * "Grade 11 cycle test 2.pdf" (9 MARCH 2022) was paired with a 9 FEBRUARY
    2022 memo in the stubs. It has no memo in this sample.
  * data/organized/biology/curriculum/ holds two P2 SOURCE BOOKLETS. They are
    exam source material, NOT a syllabus or ATP — they do not satisfy Phase 7
    curriculum mapping. Do not treat them as a curriculum.

EXPECTED YIELD: 5 verified pairs, 6 if the microorganisms memo can be
attributed. That is enough for real families, though confidence will be capped
at medium for anything resting on 2 papers.

Report honestly which class tests have no memorandum and are therefore
unusable for marking evidence (7 of the 14 papers have none).
```

## chemistry

```text
SUBJECT: chemistry (Physical Sciences Paper 2, Grade 11)

Chemistry was added as the seventh subject on 2026-09-12. `config/subjects.yaml`
and the `subject` enum in all five schemas already accept it. It sits after
physics in `execution_order` because it shares the Grade 11 Physical Sciences
corpus.

CORPUS — verified: data/organized/chemistry holds 28 files, ALL with a readable
text layer, 12 memorandum-named, 26 carrying a printed DATE. This is the
richest corpus in the repository — richer than physics.

Verified printed dates across the 28 files (14 distinct): 19 July 2018,
5 August 2019, 23 November 2020, 22 November 2021, 22 July 2022,
28 November 2022, 25 July 2023, 27 November 2023, 31 July 2024,
08 November 2024, 11 November 2024, 23 July 2025, 10 November 2025, and one
file whose header renders as "28 November\n2019" (newline inside the date —
handle that when you parse).

TRAPS YOU MUST HANDLE
  * Several filenames are misleading. "G11 - Chemistry - Examination - MG2 -
    2025.pdf" is memorandum-named but carries a 2025 date while "G11 -
    Chemistry - Nov Examination - MG - 2024.pdf" carries 2024 — do not assume
    the year in the filename is the year of the sitting.
  * "PS11- P2-Chemistry- IeBT - MCQ - 2024.pdf" is only 593 characters. In the
    physics corpus the equivalent file turned out to be a MEMO, not a question
    paper. Check it before assuming.
  * "PS11 Chemistry IeBT Test QP - Print (ZN).pdf" and "Gr 11 chemistry July
    2025.pdf" both relate to 23 July 2025 — establish which paper the IeBT memo
    actually belongs to.
  * Five papers appear to have no memorandum in the sample (Mid-Year 2024,
    Paper 1 Nov 2019, IeBT Test QP, November 2021 QP, IeBT MCQ 2024). Report
    them as unusable for marking evidence rather than guessing.
  * Cross-check Physics vs Chemistry discipline tagging inside every family.
    TWO_PASS_PROMPTS §17.2 requires that a family must not silently mix
    disciplines. Physics families already exist in knowledge/physics/ — a
    chemistry family must not reuse a physics source_id.

EXPECTED YIELD: about 11 usable pairs. Enough to reach several high-confidence
families and to make a real saturation test meaningful.
```

## english

```text
SUBJECT: english (Grade 11, Papers 1 and 2)

CORPUS — verified: data/organized/english holds 21 files (4 PDF, 17 .docx), ALL
with a readable text layer, 6 memorandum-named. Only 4 files print a DATE in
the header block, because most are .docx and lay the date out differently.

Papers: P1 July 2013, 2014, 2015, 2016, 2017, 2018; P1 Nov 2014, 2015, 2016,
2017; P2 July 2014, 2015, 2016, 2017; plus "Grade 11 Paper 1 November 2018 .pdf".
Memos: "Grade 11 English P1 Nov Memo 2016.docx", "Grade 11 Paper 1 Nov
2017.memo.docx", "Grade 11 Paper 2 July 2015 Memo.docx", "Grade 11 Paper 1
July 2018 Memo.pdf", "Grade 11 Paper 2 July Memo.docx", "Final of Grade 11
English Paper 1 July 2026 Memo.pdf".

TRAPS YOU MUST HANDLE
  * "Final of Grade 11 English Paper 1 July 2026 Memo.pdf" prints DATE 22 July
    2025 in its header but 2026 in its filename. Establish which it is before
    pairing it with anything.
  * "Grade 11 Paper 2 July Memo.docx" has no year in its name. Match it on
    content and printed marks, not on the filename.
  * The document-level stubs paired the July 2013 paper with the 2025/2026
    memo. That pairing is wrong — verify every pair from content.
  * Paper 1 is comprehension/contextual questions on set texts; Paper 2 is
    language. These are different competences and must not be merged into one
    family. Note the set texts named in each paper (for example "The God of
    Small Things" appears in the 2014–2016 memos) — a family built across
    different set texts is not testing the same content knowledge.
  * English marks are heavily rubric-based ("30 Marks CONTEXTUAL"). Capture the
    rubric levels in `memo_marking_notes` — that is what the breakdown models
    will need.

EXPECTED YIELD: about 4 usable pairs. Enough for a modest Pass 2; expect most
families at medium confidence and say so.
```

## history

```text
SUBJECT: history (Grade 11)

CORPUS — verified: data/organized/history holds 15 .docx files, ALL readable,
but only TWO are memorandum-named, and only ONE credible paper+memo pair
exists: "Copy of Gr 11- Exam - Cold War - Exam - Oct 2017.docx" with "Copy of
Gr 11- Exam - Cold War - Exam MEMO - Oct 2017.docx". The second memo ("Copy of
Gr11 - Class Test SSA MEMO - Botha's Reforms and Response - March 2016(1).docx")
has no matching paper in the sample.

None of the history files print a DATE in the extractable header, so you cannot
use the header check physics used. Establish the pairing from content and
question numbering instead, and record that you had to.

WHAT TO DO
  * Build Pass 1 for the papers that exist (source-based questions, essay
    questions) even where no memorandum is present — but mark every such record
    as having no marking evidence, and do not invent marking notes.
  * PASS 2 CANNOT RUN on one pair. A family needs ≥2 members and confidence
    needs 2–3 papers minimum. Write the saturation report with
    papers_in_sample = 1, declare NOT saturated, list the missing memoranda as
    an acquisition gap, and STOP. Do not manufacture families from a single
    paper.
  * data/organized/history/curriculum/ holds one Cold War SOURCE BOOKLET. That
    is exam source material, not a syllabus — it does not satisfy Phase 7.
  * Watch for duplicates: "GR11 July exam 2012 2 (1).docx" and "GR11 July exam
    2012 2.docx" are the same size and almost certainly the same file.

EXPECTED YIELD: Pass 1 only. This subject is acquisition-blocked, and the
honest output is a report saying so.
```

## ap_mathematics

```text
SUBJECT: ap_mathematics (Grade 11 AP Mathematics)

CORPUS — verified: data/organized/ap_mathematics holds 21 files but ONLY 8 have
a readable text layer. THIRTEEN are scanned images with 3–21 characters of
extractable text, including:
  1a. G11 AP Maths P1 July 2016.pdf
  1a.SBC G11 AP 2013 CALCULUS AND ALGEBRA 2013.pdf
  1b. Grade 11 AP Mid-Year Exam Memo.pdf        <- the only Mid-Year memo, unusable
  2a. G11 AP Maths P1 Nov 2014.pdf
  2a. G11 AP Maths P2 Stats July 2016.pdf
  2a. SBC G11 2013 AP STATS.pdf
  2b. AP Gr 11 Paper 2 Stats - MEMO.pdf
  2b. Grade 11 ap Memo Nov 2014.pdf
  2b.SBC G11 AP 2013 Stats Memo.pdf
  3a. G11 AP Maths P1 Nov 2016.pdf
  4a. G11 AP Maths P2 Nov 2016.pdf
  4b. G 11 AP Maths P2 Nov 2016 memo.pdf
  G11 AP Maths P2 Nov 2014.pdf

Readable: "1a. Grade 11 AP Mid-Year Exam.pdf", "3a. Grade 11 AP November Stats
Exam.pdf", "Gr 11 AP Algebra Jun.pdf", "Gr 11 AP Algebra Nov.pdf", "Gr 11 AP
Stats Jun.pdf" + "Gr 11 AP Stats Jun Memo.pdf", and two .docx papers.

WHAT TO DO
  * The ONLY verifiable pair is "Gr 11 AP Stats Jun.pdf" with "Gr 11 AP Stats
    Jun Memo.pdf" (both 19 June 2017). Build Pass 1 for it and for the other
    readable papers, marking the ones with no memo.
  * The stubs paired BOTH "Gr 11 AP Algebra Jun.pdf" (08 July 2017) and "Gr 11
    AP Algebra Nov.pdf" (11 November 2017) with a memo dated 19 June 2017. Both
    pairings are wrong.
  * PASS 2 CANNOT RUN on one pair. Write the saturation report declaring NOT
    saturated, and STOP.
  * Record the 13 scanned files as an acquisition/OCR gap in the review queue.
    There is no OCR capability in this repository — do not attempt to install
    one silently, and do not guess at their contents.
  * AP Mathematics has no dedicated ORC page (Phase 2 unresolved item 2) — its
    source boundary is still unconfirmed. Note that in your report.

EXPECTED YIELD: Pass 1 for ~6 readable papers, Pass 2 blocked.
```

## mathematics

```text
SUBJECT: mathematics (Grade 11)

CORPUS — verified: data/organized/mathematics holds 29 files, 19 readable, 10
with no text layer. Critically, MOST of the readable files are NOT examination
papers — they are notes and workshop material:
  01.a Equations gr 11 (without cubic equations).pdf   <- notes
  01.b Gr 11 Equations.pdf                             <- notes
  02. WORD PROBLEMS Gr 11 Examples.pdf                 <- notes
  03.a Exponents and Surds Gr 11..pdf                  <- notes
  04. NUMBER PATTERNS NOTES Gr 11.pdf                  <- notes
  05. ANALYTICAL GEOMETRY NOTES.pdf                    <- notes
  06. FUNCTIONS SECTION NOTES.pdf                      <- notes
  07. Grade 11 Functions - 1 - Parabolas (1).pdf       <- notes
  09. Grade 11 Functions - 2 - Hyperbolas.pdf          <- notes
  12. gr 11 and 12 Core Probability (1).pdf            <- notes, and covers Grade 12

Actual assessments, with verified printed dates:
  1a. Gr11 Equations Test.pdf (no DATE)  <->  1b. Gr11 Equations Memo.pdf (no DATE)
  2a Gr 11 Exponents Test March 2017.pdf (2 March 2017)  <-> its memo has NO text layer (1 char)
  3a. Assessment Week test.pdf (31 March 2017)  <-> 3b. Assessment week test memo.pdf has NO text layer (5 chars)

FIVE memoranda have no question paper in the sample at all:
  1c. Grade 11 Paper 1 November 2020 memo p6+17+18.pdf   (partial: pages 6, 17, 18 only)
  2b. Grade 11 Paper 2 2020 Memo.pdf                     (11 November 2020)
  2b.Gr 11 Juy 2019 Paper 1 Memo.pdf
  5d. Functions and Statistics 7 June Section B memo.pdf (7 June 2023)
  Gr 11 July Exam 2024 Paper 2 memo.pdf                  (19 July 2024)
These are marking guidance with nothing to mark. Log them as an acquisition gap.

WHAT TO DO
  * Classify each file as examination vs notes BEFORE extracting. Notes are not
    assessment evidence and must not become question records. Record them in
    the review queue as out-of-scope-for-Pass-1 material — they may be useful
    later for prerequisite mapping, but they are not questions.
  * The stubs paired "07. Grade 11 Functions - 1 - Parabolas" (a notes file)
    with a November 2020 memorandum, and "06. FUNCTIONS SECTION NOTES" with a
    June memorandum. Both are wrong: they paired notes with memos.
  * "3a. Assessment Week test.pdf" (31 March 2017) and "5b. Gr 11 Assessment
    Week Test (AG and Stats) Memo.pdf" (8 April 2019) are two years apart —
    not a pair. Its real memo, "3b. Assessment week test memo.pdf", has no text
    layer, so this assessment is unusable for marking evidence.
  * PASS 2 CANNOT RUN on one pair. Write the saturation report declaring NOT
    saturated, and STOP.
  * Two external sources (stithian.com, Mindbourne) are marked `external` in
    the inventory and need grade-applicability verification. Do not use them.

EXPECTED YIELD: Pass 1 for 1 verifiable assessment (the Equations Test) plus
two papers whose memoranda are unreadable. Pass 2 blocked. The main finding
will be that this subject's organized sample is mostly notes and orphan
memoranda.
```

---

## Physics (done — reference only)

```text
Physics is complete on this branch: 238 question records from 4 papers, 16
question families, 16 Understanding Models, 48 breakdowns, 44 diagnostics, 28
unresolved items, 124 objects schema-valid. Saturation was tested and the
subject was declared NOT saturated (1 family first observed in the final third,
5 strata unsampled, 9 of 13 papers unextracted).

Do not redo it. If you are asked to extend physics, the highest-value work is
extracting the 9 unextracted papers listed in UNRES-PHY-017, which would let
two deferred candidate families (CANDIDATE-FAMILY-PHY-A static-friction
threshold, CANDIDATE-FAMILY-PHY-B work-energy theorem) be promoted.

Note for anyone copying the shape: `saturation_report` has the five spec fields
plus `acquisition_order_used`, `thirds_split`, `families_new_in_final_third`
and `additional_diagnostics`. There is no boolean `saturated` field — the
verdict is derived from `families_first_observed_in_final_third > 0`, and for
physics that value is 1.
```
