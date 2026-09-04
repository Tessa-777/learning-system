# Corpus download checklist

Generated 2026-09-04T16:58:15.361376Z by `scripts/phase3_select.py` (selection `CORPUS-SEL-V1`).

**60 documents** across six subjects, selected by assessment form rather than by topic coverage.

Download each file from its Drive link and save it under the target path
shown. Keep the original filename. Do not convert, re-save or edit the
files - Phase 3 must hash the originals byte-for-byte.

When the files are in place, run:

```bash
python3 scripts/phase3_ingest_drop.py
```

---

## biology

5 papers selected from 10 candidate past papers (3 assessment forms present).

### Year-end exam paper 1 2025.pdf

- **form:** school_internal / P1 / final  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-BIO-2025-045`  
- **why:** coverage pass (form diversity): exemplar of stratum biology|school_internal|P1|final (4 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Year-end exam paper 1 2025.pdf | question paper | [download](https://drive.google.com/file/d/1I5AoWXWh3cI90kJDqEqVl5ZLov1ytPWa) | `data/raw/biology/papers/Year-end_exam_paper_1_2025.pdf` |
| [ ] | Year-end exam paper 1 MG 2025.pdf | marking_guide (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1z2dKUWTd6EQV60neP2GNKwZXaCO6ZJxs) | `data/raw/biology/memoranda/Year-end exam paper 1 MG 2025.pdf` |

### Year-end exam P1.pdf

- **form:** school_internal / P1 / final  
- **role:** secondary (2022)  
- **source_id:** `SOURCE-ORC-BIO-2022-012`  
- **why:** depth pass: second exemplar of stratum biology|school_internal|P1|final, 2022 vs newest 2025; two exemplars are the minimum needed to show a question family recurs rather than being a one-off

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Year-end exam P1.pdf | question paper | [download](https://drive.google.com/file/d/1ypXeJufcNU3hbhFZfkRXwNVwI6ojMwYv) | `data/raw/biology/papers/Year-end_exam_P1.pdf` |
| [ ] | Year-end exam P1 MG.pdf | marking_guide (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1Eub9mhE-rRNAan75CzntbKYC9r_gZTgK) | `data/raw/biology/memoranda/Year-end exam P1 MG.pdf` |

### Mid-year exam Paper 1.pdf

- **form:** school_internal / P1 / mid_year  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-BIO-2025-043`  
- **why:** coverage pass (sitting diversity): exemplar of stratum biology|school_internal|P1|mid_year (3 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Mid-year exam Paper 1.pdf | question paper | [download](https://drive.google.com/file/d/1xIW64qHssbdKKfodqq55rjt8ZjRvsUvK) | `data/raw/biology/papers/Mid-year_exam_Paper_1.pdf` |
| [ ] | Mid-year exam Paper 1 MG.pdf | marking_guide (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1B2HvA9JfbnPTBgfaA6rGJAOGYxrhCLiQ) | `data/raw/biology/memoranda/Mid-year exam Paper 1 MG.pdf` |

### Year-end exam paper 2 2025.pdf

- **form:** school_internal / P2 / final  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-BIO-2025-048`  
- **why:** coverage pass (form diversity): exemplar of stratum biology|school_internal|P2|final (3 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Year-end exam paper 2 2025.pdf | question paper | [download](https://drive.google.com/file/d/1bw76ue1bNFT8jfyCN99ihgguYGNWauTU) | `data/raw/biology/papers/Year-end_exam_paper_2_2025.pdf` |
| [ ] | Year-end exam paper 2 2025 MG.pdf | marking_guide (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/13FnEc_apcoGx3lL8pdxFKF7ef0xR3Nrc) | `data/raw/biology/memoranda/Year-end exam paper 2 2025 MG.pdf` |
| [ ] | NOVEMBER P2 SOURCE BOOKLET.pdf | companion (reference) | [download](https://drive.google.com/file/d/17nUa51I7VogcAIa224iiHC115SWTeRoi) | `data/raw/biology/companions/NOVEMBER P2 SOURCE BOOKLET.pdf` |

### November exam paper 2.pdf

- **form:** school_internal / P2 / final  
- **role:** secondary (2023)  
- **source_id:** `SOURCE-ORC-BIO-2023-024`  
- **why:** depth pass: second exemplar of stratum biology|school_internal|P2|final, 2023 vs newest 2025; two exemplars are the minimum needed to show a question family recurs rather than being a one-off

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | November exam paper 2.pdf | question paper | [download](https://drive.google.com/file/d/1XoHjdMs3Fdjiws7I51f06XgU5D6BbjG7) | `data/raw/biology/papers/November_exam_paper_2.pdf` |
| [ ] | November exam paper 2 MG.pdf | marking_guide (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1LH_Y7QvKh0MbLR7Jl-f_hkgQSw587GMZ) | `data/raw/biology/memoranda/November exam paper 2 MG.pdf` |

> **Note:** NO authoritative curriculum document (SAG / syllabus / examination guideline) exists for this subject in the ORC inventory. Phase 7 must therefore derive the topic hierarchy from Tier-1 evidence inside the papers themselves - several carry their own mark-allocation tables naming the topic of every question - and must mark that hierarchy `derived`, not `curriculum`.

---

## physics

5 papers selected from 67 candidate past papers (9 assessment forms present).

### 2024_G11_Physics_IeBT-MCQ_QP.pdf

- **form:** ieb_external / MCQ / trial  
- **role:** primary (2024)  
- **source_id:** `SOURCE-ORC-PHY-2024-047`  
- **flags:** no_memorandum_in_corpus  
- **why:** coverage pass (form diversity): exemplar of stratum physics|ieb_external|MCQ|trial (2 candidate papers in this form) [no memorandum paired]

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | 2024_G11_Physics_IeBT-MCQ_QP.pdf | question paper | [download](https://drive.google.com/file/d/1PzAht7LYTT6qRBBqESX4HtqmRysQrmof) | `data/raw/physics/papers/2024_G11_Physics_IeBT-MCQ_QP.pdf` |
| - | **no memorandum exists in the ORC for this paper** | unresolved | - | - |

### 2023_G11_Physics_IeBT-P1_QP.pdf

- **form:** ieb_external / P1 / trial  
- **role:** primary (2023)  
- **source_id:** `SOURCE-ORC-PHY-2023-046`  
- **why:** coverage pass (form diversity): exemplar of stratum physics|ieb_external|P1|trial (17 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | 2023_G11_Physics_IeBT-P1_QP.pdf | question paper | [download](https://drive.google.com/file/d/1tFAP_WwJpDro9-e1N1-hcMa2vgJExTqZ) | `data/raw/physics/papers/2023_G11_Physics_IeBT-P1_QP.pdf` |
| [ ] | 2023_G11_Physics_IeBT-P1_MG.pdf | marking_guide (paired by qp_mg_suffix, high) | [download](https://drive.google.com/file/d/12TvWB7g55SA3FloAaUhRUVmvBndoVrml) | `data/raw/physics/memoranda/2023_G11_Physics_IeBT-P1_MG.pdf` |

### IeBT 2023 P2

- **form:** ieb_external / P2 / trial  
- **role:** primary (2023)  
- **source_id:** `SOURCE-ORC-PHY-2023-129`  
- **why:** coverage pass (form diversity): exemplar of stratum physics|ieb_external|P2|trial (9 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | IeBT 2023 P2 | question paper | [download](https://drive.google.com/file/d/12CcwcJlfUuPtYnFImeFp7vm6AuSo_fqa) | `data/raw/physics/papers/IeBT_2023_P2` |
| [ ] | IeBT 2023 P2 Memo | memorandum (paired by stratum_year_unique, high) | [download](https://drive.google.com/file/d/12BjSZBGU32VBpB_bJPiXsk1G1SpfUK5Y) | `data/raw/physics/memoranda/IeBT 2023 P2 Memo` |

### P1_QP 2025

- **form:** school_internal / P1 / unknown  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-PHY-2025-233`  
- **flags:** stratum_partially_unknown  
- **why:** coverage pass (form diversity): exemplar of stratum physics|school_internal|P1|unknown (11 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | P1_QP 2025 | question paper | [download](https://drive.google.com/file/d/1HWPnGoTtUIoSlth6L2PhIp73irznVlkA) | `data/raw/physics/papers/P1_QP_2025` |
| [ ] | P1_MG 2025 | marking_guide (paired by qp_mg_suffix, high) | [download](https://drive.google.com/file/d/1DUbRsICu5SKoR_vEr7hH0jbjUoYShYYm) | `data/raw/physics/memoranda/P1_MG 2025` |
| [ ] | P1_DS 2025 | companion (reference) | [download](https://drive.google.com/file/d/1cRYiee9O70xAx_UOzXVIq1L2K9wvvuxT) | `data/raw/physics/companions/P1_DS 2025` |

### 2025_G11_Physics_Nov-Exam_QP.pdf

- **form:** school_internal / unknown / final  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-PHY-2025-063`  
- **flags:** stratum_partially_unknown  
- **why:** coverage pass (form diversity): exemplar of stratum physics|school_internal|unknown|final (11 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | 2025_G11_Physics_Nov-Exam_QP.pdf | question paper | [download](https://drive.google.com/file/d/1VmC43SnMFmWnWGbSeuSoSygSXpfsRM_z) | `data/raw/physics/papers/2025_G11_Physics_Nov-Exam_QP.pdf` |
| [ ] | 2025_G11_Physics_Nov-Exam_MG.pdf | marking_guide (paired by qp_mg_suffix, high) | [download](https://drive.google.com/file/d/1zlBXrqWiA9-MkQChLEyvhBtIALv0Khj6) | `data/raw/physics/memoranda/2025_G11_Physics_Nov-Exam_MG.pdf` |
| [ ] | P1_DS 2025 | companion (reference) | [download](https://drive.google.com/file/d/1cRYiee9O70xAx_UOzXVIq1L2K9wvvuxT) | `data/raw/physics/companions/P1_DS 2025` |

### Curriculum anchors

| # | document | drive link | save as |
|---|---|---|---|
| [ ] | IEB - SAG - PS (Subject Assessment Guidelines) | [download](https://drive.google.com/file/d/12gEedbL2Yaj14pNf-YQDJ_Q9x4QDzt13) | `data/raw/physics/curriculum/IEB - SAG - PS (Subject Assessment Guidelines)` |

> **Note:** 1 past-paper record(s) excluded as out of scope (see `excluded`); these remain in the Phase 2 inventory for provenance.

> **Note:** budget of 5 papers exhausted before stratum physics|ieb_external|unknown|trial (3 candidates) could be sampled; stratum left unrepresented and flagged for review.

> **Note:** budget of 5 papers exhausted before stratum physics|school_internal|unknown|mid_year (8 candidates) could be sampled; stratum left unrepresented and flagged for review.

> **Note:** budget of 5 papers exhausted before stratum physics|school_internal|unknown|unknown (5 candidates) could be sampled; stratum left unrepresented and flagged for review.

> **Note:** budget of 5 papers exhausted before stratum physics|school_internal|P1|final (1 candidates) could be sampled; stratum left unrepresented and flagged for review.

> **Note:** 1 of 5 selected papers have no memorandum or marking guide in the ORC inventory. Phase 6 (question-to-memo alignment) cannot be completed for these; they remain unresolved rather than being inferred (AGENTS.md rule 4).

---

## history

5 papers selected from 11 candidate past papers (6 assessment forms present).

### GRADE 11 Nov Exam P1.docx

- **form:** school_internal / P1 / final  
- **role:** primary (unknown)  
- **source_id:** `SOURCE-ORC-HIS-UNK-014`  
- **flags:** no_memorandum_in_corpus  
- **why:** coverage pass (form diversity): exemplar of stratum history|school_internal|P1|final (1 candidate papers in this form) [no memorandum paired]

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | GRADE 11 Nov Exam P1.docx | question paper | [download](https://drive.google.com/file/d/1S04Ao5SY0sLBY5tZQiR3vrRAXqkFZW2W) | `data/raw/history/papers/GRADE_11_Nov_Exam_P1.docx` |
| - | **no memorandum exists in the ORC for this paper** | unresolved | - | - |

### GR 11 JULY EXAM 2013 P1.docx

- **form:** school_internal / P1 / mid_year  
- **role:** primary (2013)  
- **source_id:** `SOURCE-ORC-HIS-2013-007`  
- **flags:** no_memorandum_in_corpus  
- **why:** coverage pass (sitting diversity): exemplar of stratum history|school_internal|P1|mid_year (1 candidate papers in this form) [no memorandum paired]

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | GR 11 JULY EXAM 2013 P1.docx | question paper | [download](https://drive.google.com/file/d/1CC4AXPcoJbWK2VfoTOGam_JI34EgsM6x) | `data/raw/history/papers/GR_11_JULY_EXAM_2013_P1.docx` |
| - | **no memorandum exists in the ORC for this paper** | unresolved | - | - |

### GRADE 11 Nov Exam P2 2013.docx

- **form:** school_internal / P2 / final  
- **role:** primary (2013)  
- **source_id:** `SOURCE-ORC-HIS-2013-015`  
- **flags:** no_memorandum_in_corpus  
- **why:** coverage pass (form diversity): exemplar of stratum history|school_internal|P2|final (1 candidate papers in this form) [no memorandum paired]

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | GRADE 11 Nov Exam P2 2013.docx | question paper | [download](https://drive.google.com/file/d/1NCjO2UsL3ZkCZ1PQNlhwQ04vlnfNurhw) | `data/raw/history/papers/GRADE_11_Nov_Exam_P2_2013.docx` |
| - | **no memorandum exists in the ORC for this paper** | unresolved | - | - |

### Copy of Gr 11- Exam - Cold War - Exam - Oct 2017.docx

- **form:** school_internal / unknown / final  
- **role:** primary (2017)  
- **source_id:** `SOURCE-ORC-HIS-2017-002`  
- **flags:** stratum_partially_unknown  
- **why:** coverage pass (form diversity): exemplar of stratum history|school_internal|unknown|final (1 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Copy of Gr 11- Exam - Cold War - Exam - Oct 2017.docx | question paper | [download](https://drive.google.com/file/d/1BLZ7PDd7ixujROZZ219TJj5OPCUCpFg6) | `data/raw/history/papers/Copy_of_Gr_11-_Exam_-_Cold_War_-_Exam_-_Oct_2017.docx` |
| [ ] | Copy of Gr 11- Exam - Cold War - Exam MEMO - Oct 2017.docx | memorandum (paired by stratum_year_unique, high) | [download](https://drive.google.com/file/d/1NWJ15t-mBmyECZclqn_J0nzhEFLqDWaJ) | `data/raw/history/memoranda/Copy of Gr 11- Exam - Cold War - Exam MEMO - Oct 2017.docx` |
| [ ] | Copy of Gr 11- Exam Source Booklet - Cold War - Exam - Oct 2017.docx | companion (reference) | [download](https://drive.google.com/file/d/1GHl4VuFEe_DnGNSk0ht2bFfehzJS7XI5) | `data/raw/history/companions/Copy of Gr 11- Exam Source Booklet - Cold War - Exam - Oct 2017.docx` |

### GR 11 JULY EXAM 2013.docx

- **form:** school_internal / unknown / mid_year  
- **role:** primary (2013)  
- **source_id:** `SOURCE-ORC-HIS-2013-008`  
- **flags:** no_memorandum_in_corpus, stratum_partially_unknown  
- **why:** coverage pass (sitting diversity): exemplar of stratum history|school_internal|unknown|mid_year (6 candidate papers in this form) [no memorandum paired]

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | GR 11 JULY EXAM 2013.docx | question paper | [download](https://drive.google.com/file/d/1jdN6MfF4hHdhjRszPKOaRopHQCNBNRuF) | `data/raw/history/papers/GR_11_JULY_EXAM_2013.docx` |
| - | **no memorandum exists in the ORC for this paper** | unresolved | - | - |

### Curriculum anchors

| # | document | drive link | save as |
|---|---|---|---|
| [ ] | July 2015 Exam Requirements for 10,11 and 12 (1).docx | [download](https://drive.google.com/file/d/13FfbIeCNuZ1JLtEvwslYWqnHrADxtemy) | `data/raw/history/curriculum/July 2015 Exam Requirements for 10,11 and 12 (1).docx` |

> **Note:** budget of 5 papers exhausted before stratum history|school_internal|P2|mid_year (1 candidates) could be sampled; stratum left unrepresented and flagged for review.

> **Note:** 4 of 5 selected papers have no memorandum or marking guide in the ORC inventory. Phase 6 (question-to-memo alignment) cannot be completed for these; they remain unresolved rather than being inferred (AGENTS.md rule 4).

---

## english

5 papers selected from 35 candidate past papers (4 assessment forms present).

### Grade 11 FINAL EXAM P1 2025.pdf

- **form:** school_internal / P1 / final  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-ENG-2025-069`  
- **why:** coverage pass (form diversity): exemplar of stratum english|school_internal|P1|final (12 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Grade 11 FINAL EXAM P1 2025.pdf | question paper | [download](https://drive.google.com/file/d/1nkCT-WCeydgO9V7ZJgYYwLH_TNWOqtiC) | `data/raw/english/papers/Grade_11_FINAL_EXAM_P1_2025.pdf` |
| [ ] | Grade 11 EXAM P1 2025- Final version MG.pdf | marking_guide (paired by stratum_year_unique, high) | [download](https://drive.google.com/file/d/1CtJtSmylSh2w0JtKgAZBlFbFv9ukZUzt) | `data/raw/english/memoranda/Grade 11 EXAM P1 2025- Final version MG.pdf` |

### Grade 11 Paper 1 Nov 2014.docx

- **form:** school_internal / P1 / final  
- **role:** secondary (2014)  
- **source_id:** `SOURCE-ORC-ENG-2014-005`  
- **why:** depth pass: second exemplar of stratum english|school_internal|P1|final, 2014 vs newest 2025; two exemplars are the minimum needed to show a question family recurs rather than being a one-off

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Grade 11 Paper 1 Nov 2014.docx | question paper | [download](https://drive.google.com/file/d/1V97dc4JGqV3smirzbBZjq541q0VWTKFY) | `data/raw/english/papers/Grade_11_Paper_1_Nov_2014.docx` |
| [ ] | Grade 11 Paper 1 Nov 2014 Memo.docx | memorandum (paired by stratum_year_unique, high) | [download](https://drive.google.com/file/d/1t55tyWFb53pA13PzV6CpnJ3Xi0OpPtPf) | `data/raw/english/memoranda/Grade 11 Paper 1 Nov 2014 Memo.docx` |

### Grade 11 English Paper 1 July 2026 .pdf

- **form:** school_internal / P1 / mid_year  
- **role:** primary (2026)  
- **source_id:** `SOURCE-ORC-ENG-2026-074`  
- **why:** coverage pass (sitting diversity): exemplar of stratum english|school_internal|P1|mid_year (12 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Grade 11 English Paper 1 July 2026 .pdf | question paper | [download](https://drive.google.com/file/d/14dYLdQlGJw8bEqM8WDL-W6jnQW4aa7eg) | `data/raw/english/papers/Grade_11_English_Paper_1_July_2026_.pdf` |
| [ ] | Final of Grade 11 English Paper 1 July 2026 Memo.pdf | memorandum (paired by stratum_year_unique, high) | [download](https://drive.google.com/file/d/1dFBZwzmNHEMTPVomzFeAIBoUoFfKIMr5) | `data/raw/english/memoranda/Final of Grade 11 English Paper 1 July 2026 Memo.pdf` |

### Grade 11 Paper 1 2020.docx.pdf

- **form:** school_internal / P1 / unknown  
- **role:** primary (2020)  
- **source_id:** `SOURCE-ORC-ENG-2020-036`  
- **flags:** stratum_partially_unknown  
- **why:** coverage pass (sitting diversity): exemplar of stratum english|school_internal|P1|unknown (1 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Grade 11 Paper 1 2020.docx.pdf | question paper | [download](https://drive.google.com/file/d/1DdO0IpZtF0ZOXklDXGuK6CnK3_6tPrTa) | `data/raw/english/papers/Grade_11_Paper_1_2020.docx.pdf` |
| [ ] | Grade 11 Paper 1 2020 memo.docx.pdf | memorandum (paired by stratum_year_unique, high) | [download](https://drive.google.com/file/d/1Jg_Blzx3Dnh-0yLsv5Vr3vckhb-skUoR) | `data/raw/english/memoranda/Grade 11 Paper 1 2020 memo.docx.pdf` |

### Grade 11 Paper 2 July 2018 .pdf

- **form:** school_internal / P2 / mid_year  
- **role:** primary (2018)  
- **source_id:** `SOURCE-ORC-ENG-2018-027`  
- **why:** coverage pass (form diversity): exemplar of stratum english|school_internal|P2|mid_year (10 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Grade 11 Paper 2 July 2018 .pdf | question paper | [download](https://drive.google.com/file/d/1n_jBGpLPlPO0UPOwNGPljnekPI6CN52b) | `data/raw/english/papers/Grade_11_Paper_2_July_2018_.pdf` |
| [ ] | Grade 11 Paper 2 July 2018 Memo.pdf | memorandum (paired by stratum_year_unique, high) | [download](https://drive.google.com/file/d/1pZjCvC6qUnGA6blCV0-KzwhDrwkbvLGQ) | `data/raw/english/memoranda/Grade 11 Paper 2 July 2018 Memo.pdf` |

> **Note:** NO authoritative curriculum document (SAG / syllabus / examination guideline) exists for this subject in the ORC inventory. Phase 7 must therefore derive the topic hierarchy from Tier-1 evidence inside the papers themselves - several carry their own mark-allocation tables naming the topic of every question - and must mark that hierarchy `derived`, not `curriculum`.

---

## ap_mathematics

5 papers selected from 46 candidate past papers (9 assessment forms present).

### Gr 11 FS Paper 1 November Exam 2025.pdf

- **form:** school_internal / P1 / final  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-APM-2025-079`  
- **why:** coverage pass (form diversity): exemplar of stratum ap_mathematics|school_internal|P1|final (10 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Gr 11 FS Paper 1 November Exam 2025.pdf | question paper | [download](https://drive.google.com/file/d/1dH3wm_JMeba7loiUH6w4eC-j7NgIxp_s) | `data/raw/ap_mathematics/papers/Gr_11_FS_Paper_1_November_Exam_2025.pdf` |
| [ ] | Gr 11 FS Paper 1 November Exam 2025 memo.pdf | memorandum (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/19TnqAgx6wP6JNft60k04r_slrvpU3cWD) | `data/raw/ap_mathematics/memoranda/Gr 11 FS Paper 1 November Exam 2025 memo.pdf` |

### July Gr11FS P1.pdf

- **form:** school_internal / P1 / mid_year  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-APM-2025-083`  
- **why:** coverage pass (sitting diversity): exemplar of stratum ap_mathematics|school_internal|P1|mid_year (7 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | July Gr11FS P1.pdf | question paper | [download](https://drive.google.com/file/d/1Qdm8FFoDxq9ReJJ2rgd_vHXdi2U1HvbW) | `data/raw/ap_mathematics/papers/July_Gr11FS_P1.pdf` |
| [ ] | July Gr11FS P1 - Memo.pdf | memorandum (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1uZGiwDjuhsJH1ykAYuR6sLzXxn10G1yR) | `data/raw/ap_mathematics/memoranda/July Gr11FS P1 - Memo.pdf` |

### 1a.SBC G11 AP 2013 CALCULUS AND ALGEBRA 2013.pdf

- **form:** school_internal / P1 / unknown  
- **role:** primary (2013)  
- **source_id:** `SOURCE-ORC-APM-2013-001`  
- **flags:** stratum_partially_unknown  
- **why:** coverage pass (sitting diversity): exemplar of stratum ap_mathematics|school_internal|P1|unknown (2 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | 1a.SBC G11 AP 2013 CALCULUS AND ALGEBRA 2013.pdf | question paper | [download](https://drive.google.com/file/d/1-MDiQsUvCOOJgBuLTiV8nGEf1UsYqPq-) | `data/raw/ap_mathematics/papers/1a.SBC_G11_AP_2013_CALCULUS_AND_ALGEBRA_2013.pdf` |
| [ ] | 1b. SBC G11 AP 2013 Algebra and Calculus Memo.pdf | memorandum (paired by stratum_year_unique, high) | [download](https://drive.google.com/file/d/1rKhRKnzovEneh8tvbvC0-aahrdLcwIxt) | `data/raw/ap_mathematics/memoranda/1b. SBC G11 AP 2013 Algebra and Calculus Memo.pdf` |

### 11 FS Nov Paper 2 2024.pdf

- **form:** school_internal / P2 / final  
- **role:** primary (2024)  
- **source_id:** `SOURCE-ORC-APM-2024-069`  
- **why:** coverage pass (form diversity): exemplar of stratum ap_mathematics|school_internal|P2|final (10 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | 11 FS Nov Paper 2 2024.pdf | question paper | [download](https://drive.google.com/file/d/1cuALuCug_sKa__33cbew18BxhiQQKstP) | `data/raw/ap_mathematics/papers/11_FS_Nov_Paper_2_2024.pdf` |
| [ ] | 11 FS Paper 2 Nov 2024 Memo.pdf | memorandum (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1Tn8wuQyBPyN6RUtoLqpmwgVch-3ERZ-C) | `data/raw/ap_mathematics/memoranda/11 FS Paper 2 Nov 2024 Memo.pdf` |

### 1a. Grade 11 AP Exam - July 2014 (1).docx

- **form:** school_internal / unknown / mid_year  
- **role:** primary (2014)  
- **source_id:** `SOURCE-ORC-APM-2014-005`  
- **flags:** stratum_partially_unknown  
- **why:** coverage pass (form diversity): exemplar of stratum ap_mathematics|school_internal|unknown|mid_year (5 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | 1a. Grade 11 AP Exam - July 2014 (1).docx | question paper | [download](https://drive.google.com/file/d/1uohinJO66tU2XuDXORKRiaJwU2FOJ9da) | `data/raw/ap_mathematics/papers/1a._Grade_11_AP_Exam_-_July_2014_1_.docx` |
| [ ] | 1b. Grade 11 AP Exam - July 2014 - Memorandum (1).docx | memorandum (paired by stratum_year_unique, high) | [download](https://drive.google.com/file/d/1j0g_T9C36lbPvp56k850qLOmG2NkWDO0) | `data/raw/ap_mathematics/memoranda/1b. Grade 11 AP Exam - July 2014 - Memorandum (1).docx` |

> **Note:** budget of 5 papers exhausted before stratum ap_mathematics|school_internal|P2|mid_year (5 candidates) could be sampled; stratum left unrepresented and flagged for review.

> **Note:** budget of 5 papers exhausted before stratum ap_mathematics|school_internal|P2|unknown (2 candidates) could be sampled; stratum left unrepresented and flagged for review.

> **Note:** budget of 5 papers exhausted before stratum ap_mathematics|school_internal|unknown|unknown (3 candidates) could be sampled; stratum left unrepresented and flagged for review.

> **Note:** budget of 5 papers exhausted before stratum ap_mathematics|school_internal|unknown|final (2 candidates) could be sampled; stratum left unrepresented and flagged for review.

> **Note:** NO authoritative curriculum document (SAG / syllabus / examination guideline) exists for this subject in the ORC inventory. Phase 7 must therefore derive the topic hierarchy from Tier-1 evidence inside the papers themselves - several carry their own mark-allocation tables naming the topic of every question - and must mark that hierarchy `derived`, not `curriculum`.

---

## mathematics

5 papers selected from 39 candidate past papers (5 assessment forms present).

### Gr11 P1 Nov Exam.pdf

- **form:** school_internal / P1 / final  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-MAT-2025-270`  
- **why:** coverage pass (form diversity): exemplar of stratum mathematics|school_internal|P1|final (11 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Gr11 P1 Nov Exam.pdf | question paper | [download](https://drive.google.com/file/d/1iI_kVDZX2OiCc0R8kr8QKVbaeOL39pmD) | `data/raw/mathematics/papers/Gr11_P1_Nov_Exam.pdf` |
| [ ] | Gr11 P1 Nov Exam Memo.pdf | memorandum (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1tnEaZ-CjMd1IoVjMQUdbYUJXnfAKPb4U) | `data/raw/mathematics/memoranda/Gr11 P1 Nov Exam Memo.pdf` |

### 2025 July paper 1 .pdf

- **form:** school_internal / P1 / mid_year  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-MAT-2025-267`  
- **why:** coverage pass (sitting diversity): exemplar of stratum mathematics|school_internal|P1|mid_year (8 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | 2025 July paper 1 .pdf | question paper | [download](https://drive.google.com/file/d/11w34udet-txDaaiw3T9a9RtgrX_zPc8E) | `data/raw/mathematics/papers/2025_July_paper_1_.pdf` |
| [ ] | 11 Paper 1 July 2025 MEMO.pdf | memorandum (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1_DW-m07-KMNbLgxqv5kuwN-Mz3F4W1iW) | `data/raw/mathematics/memoranda/11 Paper 1 July 2025 MEMO.pdf` |

### 11 Nov Paper 2 2025 FINAL.pdf

- **form:** school_internal / P2 / final  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-MAT-2025-263`  
- **why:** coverage pass (form diversity): exemplar of stratum mathematics|school_internal|P2|final (10 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | 11 Nov Paper 2 2025 FINAL.pdf | question paper | [download](https://drive.google.com/file/d/1jgddhWifTJyEl0UY2esKZYp5c4gGYXzy) | `data/raw/mathematics/papers/11_Nov_Paper_2_2025_FINAL.pdf` |
| [ ] | 11 Nov Paper 2 2025 MEMO.pdf | memorandum (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1kLviwSXvvgL99czk_ifbujaQEsFIcmzo) | `data/raw/mathematics/memoranda/11 Nov Paper 2 2025 MEMO.pdf` |

### Gr11 Exam P2 July 2025.pdf

- **form:** school_internal / P2 / mid_year  
- **role:** primary (2025)  
- **source_id:** `SOURCE-ORC-MAT-2025-268`  
- **why:** coverage pass (sitting diversity): exemplar of stratum mathematics|school_internal|P2|mid_year (9 candidate papers in this form); chosen because a memorandum exists for it

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | Gr11 Exam P2 July 2025.pdf | question paper | [download](https://drive.google.com/file/d/1D_ClZbNvxfNmSFxKCGMB-dzer_Q9-XBp) | `data/raw/mathematics/papers/Gr11_Exam_P2_July_2025.pdf` |
| [ ] | 11 Paper 2 July 2025 MEMO.pdf | memorandum (paired by title_similarity, medium) | [download](https://drive.google.com/file/d/1NUEi1DKgBxztEHV6d6n0JNQUWwzC2evE) | `data/raw/mathematics/memoranda/11 Paper 2 July 2025 MEMO.pdf` |

### 2a. Grade 11 Paper 2.pdf

- **form:** school_internal / P2 / unknown  
- **role:** primary (2020)  
- **source_id:** `SOURCE-ORC-MAT-2020-230`  
- **flags:** no_memorandum_in_corpus, stratum_partially_unknown  
- **why:** coverage pass (sitting diversity): exemplar of stratum mathematics|school_internal|P2|unknown (1 candidate papers in this form) [no memorandum paired]

| # | document | type | drive link | save as |
|---|---|---|---|---|
| [ ] | 2a. Grade 11 Paper 2.pdf | question paper | [download](https://drive.google.com/file/d/1gc6xSJSobL4oYGhtuuTZ-8YRR4twq3RN) | `data/raw/mathematics/papers/2a._Grade_11_Paper_2.pdf` |
| - | **no memorandum exists in the ORC for this paper** | unresolved | - | - |

> **Note:** NO authoritative curriculum document (SAG / syllabus / examination guideline) exists for this subject in the ORC inventory. Phase 7 must therefore derive the topic hierarchy from Tier-1 evidence inside the papers themselves - several carry their own mark-allocation tables naming the topic of every question - and must mark that hierarchy `derived`, not `curriculum`.

> **Note:** 1 of 5 selected papers have no memorandum or marking guide in the ORC inventory. Phase 6 (question-to-memo alignment) cannot be completed for these; they remain unresolved rather than being inferred (AGENTS.md rule 4).

---

