# Corpus Sufficiency Policy

**Version:** 1.0.0
**Status:** Authoritative for Phase 3 and Phase 4 from spec v1.1.0
**Supersedes:** the blanket-acquisition requirement of `IMPLEMENTATION_SPEC.md` §4 v1.0.0
**Requires:** human sign-off (`review_queue/RQ-P3-CORPUS-SELECTION.yaml`)

---

## 1. The problem this policy resolves

Phase 3 v1.0.0 required acquiring *every* accessible source discovered in
Phase 2 — 821 records. That requirement was wrong for this system, and it was
never satisfiable in the execution environment.

It was wrong because it confused **coverage of a syllabus** with **saturation of
a taxonomy**. This system does not need to know every topic the school teaches.
Its primary knowledge objects are question families (Phase 8) and Understanding
Models (Phase 9), and `SYSTEM_SPEC.md` §9 defines an Understanding Model as
describing *"the underlying competence being assessed"* — explicitly not topic
content. `IMPLEMENTATION_SPEC.md` §9 already forbids the exhaustive reading:
*"Do not create one family for every individual question."*

A taxonomy is a **compression** of a corpus. Acquiring 821 documents to feed a
compression step spends effort on redundancy the compression is designed to
remove.

---

## 2. What the 821 records actually were

Counted from the six Phase 2 inventories (`scripts/phase3_select.py`):

| document_type | count |
|---|---|
| memorandum | 237 |
| past_paper | 209 |
| assessment_material | 165 |
| marking_guide | 122 |
| reference | 85 |
| other | 7 |
| curriculum | 1 |
| **total** | **821** |

Only **209** were question papers. The 359 memoranda and marking guides are not
additional corpus — they are the marking evidence *for* those papers, and
`AGENTS.md` rule 8 makes them mandatory companions rather than optional extras.

The 209 figure is itself inflated. Phase 2 deduplicated on Drive **file ID**
only and removed exactly one record. It never compared **content**. Verified
during this revision:

* `2022_G11_Physics_Nov-Exam_QP.pdf` (`1BLMEfPahfO7b751FXS8oM_ZhtxcIxQcT`) and
  `G11 Nov Physics Exam 2022 QP.pdf` (`16NXMYVKTVQ4K2zeHjm-0DS-AXUoLF5wD`) are
  two distinct Drive IDs returning identical text — same examiner (Mr Hilder),
  same moderator (Mr McCoy), same date (21 November 2022), same 200-mark table,
  same multiple-choice items.
* The 2022 IEB Trial Physics Paper 1 is present under **three** Drive IDs and
  three naming schemes: `2022_G11_Physics_IeBT-P1_QP.pdf`,
  `IeBT 2022 Physics P1`, and `P1_QP 2022`.
* `IeBT 2022 Physical Sciences P2` appears twice under two IDs.

The ORC was clearly re-filed more than once, and each filing left its copies in
place. The true count of distinct Grade 11 question papers is materially below
209.

---

## 3. What determines a question family

Not the topic. Not the year. The **assessment form**.

Evidence, all of it from documents retrieved during this revision:

* The **November 2018 Mathematics Paper 2** prints its own structure in a
  front-matter table: Question 1–3 *Statistics*, 4–5 *Analytical Geometry*,
  6–7 *Euclidean Geometry*, 8–10 *Trigonometry*, 11 *Measurement*, 150 marks
  total. Topics rotate between years; that skeleton does not.
* The **November 2022 Physics paper** labels its own question families in the
  question headings: `MULTIPLE CHOICE`, `KINEMATICS GRAPH`,
  `HORIZONTAL MOTION`, `PROJECTILE MOTION`. The paper declares its taxonomy.
* The **November 2017 History paper** declares `Section 1 – Single Source
  Analysis /60`, `Section 2 – Multiple Source Questions /90`,
  `Section 3 – Source Based Essay /50`, and the **July 2009 History memo**
  shows the same recurring set plus *Discursive Essay* and *Stimulus Based
  Writing*, with an explicit three-step rubric (Context 6 / Knowledge 20 /
  Conclusion 8).
* Marking conventions repeat verbatim across years: `2x2=(4)`, `(3)` for a
  definition, the instruction *"Answers only, without the relevant calculations
  will not be given marks."*

These are the *meta* patterns the tutor must model — command words, evidence
rules, mark-allocation logic, answer structure. They are properties of the form,
and they are exactly what is **not** topic-specific.

---

## 4. The sampling design

Stratify on form, then saturate.

### 4.1 Stratum

```
stratum = setter × paper_form × session
```

* **setter** — `ieb_external` (externally set IEB trial) or `school_internal`
  (set by St Benedict's staff, examiner named on the paper). These have
  different voices, different standards and different structures, so they cannot
  stand in for one another.
* **paper_form** — `P1`, `P2`, `MCQ`, or `single`. Determined per
  *(subject, setter)* pair from the corpus, never assumed: Physics sits its IEB
  Trials as P1/P2 but its own internal exams as one combined 200-mark paper.
* **session** — `mid_year`, `final`, or `trial`. A mid-year paper covers less
  content and is set differently from a final.

Where the classifier cannot determine a dimension it returns `unknown` rather
than guessing (`AGENTS.md` rule 7). Such selections carry the flag
`stratum_partially_unknown` for human review.

### 4.2 Two-pass allocation

1. **Coverage pass** — one exemplar per stratum, so every distinct assessment
   form the school actually sits is represented at least once. Where strata
   outnumber the budget, they are ranked by (a) whether a memorandum exists and
   (b) how many papers the corpus holds in that form — i.e. the forms the school
   genuinely uses most.
2. **Depth pass** — remaining budget adds a second, *older* exemplar to the
   largest strata, preferring the widest year gap available.

**Two exemplars is a floor, not a preference.** A single instance cannot
distinguish "this question family recurs" from "this was a one-off". Any family
asserted from one exemplar must be recorded at `confidence: low` and flagged for
review at Phase 13.

Form diversity is secured **before** sitting diversity: the coverage pass takes
one exemplar per `(setter, paper_form)` pair, and only then adds further
sittings of pairs already represented. The paper form is what determines which
question families can appear; the sitting mainly affects how much of the syllabus
is in scope.

A `paper_form` occurring in exactly one pair — Physics `MCQ` is the case in this
corpus — outranks a merely frequent form. **Pool size measures how often the
school sits a form, not how much new taxonomy it yields.** A multiple-choice
paper contributes question families (distractor reasoning, elimination, single-
answer justification) that appear nowhere else in the subject, so it is sampled
even though the school has only ever sat one.

### 4.2.1 Papers with no memorandum

Some selected papers have no memorandum in the ORC. They are still acquired, but
their evidential reach is restricted:

| may support | may NOT support |
|---|---|
| question families (Phase 8) | marking requirements |
| question wording and command verbs | Understanding Model `marking_requirements` |
| mark *allocations* printed on the paper | partial-credit rules |
| paper structure and section layout | any Phase 6 alignment |

Such papers carry the flag `no_memorandum_in_corpus`, and any Understanding Model
built partly on them must record `confidence: low` with the missing memo named as
the reason. Marking criteria must never be inferred for them (`AGENTS.md` rule 8).

### 4.3 Memorandum availability is a selection criterion

A question paper without its memorandum cannot support Phase 6 alignment, and
without marking evidence an Understanding Model is pedagogical inference rather
than Tier-1 grounding. Memo availability is therefore used to *rank* candidates,
not merely reported afterwards.

Pairing uses four strategies, strongest first:

| strategy | rule | confidence |
|---|---|---|
| `stratum_year_unique` | exactly one memorandum in the same year matching the same assessment form | high |
| `order_prefix` | ORC filing convention `3a.` paper ↔ `3b.` memo | high |
| `qp_mg_suffix` | `_QP` ↔ `_MG` filename convention | high |
| `title_similarity` | token Jaccard on canonicalised titles, forms must agree | medium / low |

The memorandum pool is scope-filtered identically to the paper pool. Without
this, English Paper 2 (2023) was structurally matched to
`Copy of MEMO Contextual Test Film Grade 12 2023` — a **Grade 12** memorandum
that Phase 2 had already marked out of scope.

### 4.4 Companion documents are part of the unit

A paper is not self-contained. History source-based questions are unanswerable
without the **Source Booklet**; Physics and Mathematics papers instruct the
candidate to detach a **Data Sheet** or **Information Sheet**; IEB Physics trials
ship a **Diagram Booklet** and an **Answer Sheet**. These are filed under
`reference` / `other` in the Phase 2 inventory, so a sampler that filters to
`past_paper` silently discards them. They are matched on year plus compatible
form.

### 4.5 Curriculum anchors

Phase 7 requires the topic hierarchy to come from authoritative source material.
The ORC holds almost none:

| subject | curriculum anchor present |
|---|---|
| physics | `IEB - SAG - PS (Subject Assessment Guidelines)` |
| history | `July 2015 Exam Requirements for 10, 11 and 12` |
| biology | **none** |
| english | **none** |
| ap_mathematics | **none** |
| mathematics | **none** |

For the four subjects with no anchor, Phase 7 must derive the hierarchy from
Tier-1 evidence *inside the papers themselves* — the Mathematics and Physics
front-matter tables name the topic of every question — and must mark the result
`derived`, never `curriculum`. This is a standing limitation, not a defect
introduced by sampling.

---

## 5. Stopping rule (the part that makes a small sample defensible)

The sample size is a **budget**, not a claim of sufficiency. Sufficiency is
decided empirically, at Phase 8 and again at Phase 13:

> **Saturation test.** Order the acquired papers by acquisition sequence. If the
> final third of the sample yields **no question family, no assessment operation
> and no marking structure** that the first two thirds did not already contain,
> the corpus is saturated for taxonomy purposes and acquisition stops.
>
> If it does yield new families, acquisition continues — but **targeted at the
> strata that produced them**, never by reverting to blanket acquisition.

Each Phase 13 validation report must state, per subject:

```
papers_in_sample
question_families_identified
families_first_observed_in_final_third   <- must be 0 at saturation
strata_left_unsampled                    <- with justification
families_supported_by_single_exemplar    <- confidence: low
```

A subject may not be marked validated while
`families_first_observed_in_final_third > 0`.

---

## 6. What this policy explicitly does **not** claim

* It does **not** claim the sample covers the Grade 11 syllabus. It does not.
  Topic coverage is out of scope by design, and Work-Through Mode
  (`SYSTEM_SPEC.md` §4.2) will encounter questions on topics no selected paper
  touches. Those must be handled by the tutor's general reasoning and recorded
  as knowledge-bank gaps — not silently answered as though they were grounded.
* It does **not** claim every question family has been found. Saturation is
  evidence of sufficiency for the sample, not proof of completeness.
* It does **not** license substituting external material for missing ORC
  sources (`AGENTS.md` rule 3).
* It does **not** weaken provenance. Every selected document keeps its
  `source_id`, Drive URL and ORC subject page.

---

## 7. Known unresolved gaps created or exposed by this revision

Current selection: **60 documents** — 30 question papers, 24 memoranda, 4
companion documents, 2 curriculum anchors.

1. **History has effectively no memoranda.** The ORC holds 3 memoranda for 11
   past papers, and 2 of the 3 are class tests. Only the October 2017 Cold War
   exam has both a memo and a Source Booklet. **4 of the 5 selected History
   papers carry `no_memorandum_in_corpus`**, so Phase 6 can align at most one
   History paper. This is a property of the ORC, not of the sampling: acquiring
   all 11 History papers would not produce a single additional memorandum.
2. **History `document_type` labels are unreliable.**
   `2009_July_exam_Gr_11.doc.docx` is recorded as `past_paper`; its retrieved
   content is the **July 2009 memorandum** ("July Exam Memo 2009", complete with
   marking guidance and the marker's own apology for a mis-set question).
   Document type is therefore re-verified from content at ingest
   (`ingestion/acquisition/content_probe.py`), never trusted from Phase 2
   metadata. The companion record `Gr11_Exam_July_2009.doc.docx` is probably the
   actual question paper, so this pair should be re-typed together.
3. **Physics IEB MCQ has no marking guide in the inventory**
   (`2024_G11_Physics_IeBT-MCQ_QP.pdf`). It is still acquired because MCQ is a
   unique form (§4.2), but per §4.2.1 it may support taxonomy only, never
   marking requirements.
4. **Mathematics 2020 `2a. Grade 11 Paper 2.pdf`** could not be paired: the
   filing prefix `2` matched two memorandum candidates. Needs human pairing.
5. **Strata left unsampled** are listed in the per-subject `notes` of
   `data/raw/CORPUS_SELECTION.yaml` and must be reviewed before Phase 13
   sign-off. Physics is the worst case: 9 strata exist and 5 were sampled,
   leaving `ieb_external|unknown|trial`, `school_internal|unknown|mid_year`,
   `school_internal|unknown|unknown` and `school_internal|P1|final`
   unrepresented. Several of those `unknown` strata are the *same* internal exam
   filed under different names, so the true number of distinct unsampled Physics
   forms is probably smaller — but that can only be settled by content-hash
   dedupe at Phase 3b, not from metadata.
6. **Chemistry material sits inside the Physics folder** (`IeBT 2021 Chemistry
   P2`, `11_Chemistry Test-1A_Bonding-ReactionRate`, `IEB Chemistry - Data
   Sheet`). Excluded by `is_out_of_scope`; retained in the inventory for
   provenance only.
7. **Duplicate content was never detected by Phase 2**, which deduplicated on
   Drive file ID and removed exactly one record. Phase 3b must deduplicate on
   **content hash**. `scripts/phase3_ingest_drop.py` does this and reports every
   collision rather than silently dropping one copy.

---

## 8. Re-running the selection

```bash
python3 scripts/phase3_select.py                       # default budget
python3 scripts/phase3_select.py --papers-per-subject 6
```

The selection is deterministic: the same inventories and budget always produce
the same sample. Outputs are `data/raw/CORPUS_SELECTION.yaml` (machine) and
`data/raw/DOWNLOAD_CHECKLIST.md` (human). Neither modifies the Phase 2
inventories.
