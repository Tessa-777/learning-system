"""Pass 2 unresolved items for Physics.

Each item is something noticed in the batch that could NOT be validated from the
evidence available. TWO_PASS_PROMPTS Pass 2 requires these to be reported rather
than smoothed over: single-exemplar patterns, sources that could not contribute
evidence, contradictions between memos, and curriculum gaps the tutor must never
answer as if they were grounded in the knowledge bank.

Types: contradiction | fidelity | coverage_gap | curriculum_gap | data_quality | unsampled_stratum
"""

UNRESOLVED = [
    # ---------- contradictions between paper and memorandum ----------
    {"type": "contradiction",
     "id": "UNRES-PHY-001",
     "summary": "2023 memo marks table does not match the 2023 paper",
     "detail": (
         "The paper's 'Question Total' row has ten questions (14/24/10/23/9/24/19/20/12/10 = 165). "
         "The memo's 'Question Total' row has only nine columns (14/24/11/19/33/23/15/11/10 = 165). "
         "Individual memo question headings do match the paper (Q3 10 marks, Q4 23 marks), so the "
         "memo's summary row appears to be a stale template."
     ),
     "affected": ["physics_2023_internal_paper1_june_*"],
     "evidence": ["PHY-2023-MY question marks table", "PHY-2023-MY memo marks table"],
     "recommended_review": "Confirm with the school which allocation was used for moderation; until then use per-question marks printed on the paper."},

    {"type": "contradiction",
     "id": "UNRES-PHY-002",
     "summary": "2025 memo header states 125 marks; paper and the memo's own table state 135",
     "detail": (
         "Paper header MARKS 135; memo header MARKS 125; the memo's 'Question Total' row "
         "(18/23/15/18/16/17/5/7/16) sums to 135. The 125 is treated as a typo in the memo header."
     ),
     "affected": ["physics_2025_internal_paper1_nov_*"],
     "evidence": ["PHY-2025-NOV paper header", "PHY-2025-NOV memo header and marks row"],
     "recommended_review": "Confirm the paper total is 135."},

    {"type": "contradiction",
     "id": "UNRES-PHY-003",
     "summary": "2025 memo re-splits question 6.1.3 into three sub-parts worth more marks than the paper allocates",
     "detail": (
         "Paper 6.1.3 is worth 4 marks (gradient, its unit, and identifying the planet). The memo "
         "answers 6.1.3 (3), 6.1.4 (2: gradient = Fg/m so it represents g) and 6.1.5 (1: Mars) - "
         "6 marks and two sub-numbers that do not exist on the paper."
     ),
     "affected": ["physics_2025_internal_paper1_nov_q6.1.3"],
     "evidence": ["PHY-2025-NOV paper Q6.1.3", "PHY-2025-NOV memo 6.1.3-6.1.5"],
     "recommended_review": "Confirm the intended allocation before this item is used for mark-based diagnosis."},

    {"type": "contradiction",
     "id": "UNRES-PHY-004",
     "summary": "2025 memo mark allocations in Questions 5 and 8 exceed the paper's allocations",
     "detail": (
         "Paper 8.1 is 2 marks, memo shows (3); paper 8.3 is 4 marks, memo shows (3). Paper 5.3 and "
         "5.6 are 1 and 2 marks respectively, but the memo shows two and three ticks. Question totals "
         "still agree, so the distribution differs rather than the total."
     ),
     "affected": ["physics_2025_internal_paper1_nov_q8.1", "physics_2025_internal_paper1_nov_q8.3",
                  "physics_2025_internal_paper1_nov_q5.3", "physics_2025_internal_paper1_nov_q5.6"],
     "evidence": ["PHY-2025-NOV paper Q5/Q8", "PHY-2025-NOV memo Q5/Q8"],
     "recommended_review": "Confirm the intended per-part allocation; marking_requirements for "
                           "UNDERSTANDING-PHY-009 and -014 quote the memo values and inherit this uncertainty."},

    {"type": "contradiction",
     "id": "UNRES-PHY-005",
     "summary": "2025 memo answer to 6.2.1 contradicts its own reasoning in 6.2.2",
     "detail": (
         "6.2.1 is answered 'Positive', but every one of the three accepted reasonings in 6.2.2 "
         "concludes that Q2 must be NEGATIVE for the net force on Q3 to be to the left."
     ),
     "affected": ["physics_2025_internal_paper1_nov_q6.2.1", "physics_2025_internal_paper1_nov_q6.2.2"],
     "evidence": ["PHY-2025-NOV memo 6.2.1 and 6.2.2"],
     "recommended_review": "The memo is self-contradictory; this item must not be used as marking "
                           "evidence until the school confirms the intended answer."},

    {"type": "contradiction",
     "id": "UNRES-PHY-006",
     "summary": "2025 paper 4.6 names the wrong block for the motion described",
     "detail": (
         "4.6 asks how far 'block B' travelled along the slope, but block B hangs vertically and "
         "block A is the one on the 30-degree slope. The memo solves for the block on the slope "
         "using block A's forces."
     ),
     "affected": ["physics_2025_internal_paper1_nov_q4.6"],
     "evidence": ["PHY-2025-NOV paper Q4 stem", "PHY-2025-NOV memo 4.6"],
     "recommended_review": "Treat the item as referring to the block on the slope; flag the wording defect."},

    {"type": "contradiction",
     "id": "UNRES-PHY-007",
     "summary": "2021 memo substitutes 40 N where the paper states an applied force of 10 N",
     "detail": (
         "Question 5 states 'A horizontal force F of 10 N is applied to block A' and the diagram is "
         "labelled 'F = 10 N', but the memo's worked solution uses 40 N ('40 - T = 3a'), producing "
         "a = 4,34 m.s-2 and T = 26,98 N."
     ),
     "affected": ["physics_2021_internal_paper1_nov_q5.5", "physics_2021_internal_paper1_nov_q5.6"],
     "evidence": ["PHY-2021-NOV paper Q5 stem", "PHY-2021-NOV memo 5.5/5.6"],
     "recommended_review": "Do not use the numeric answers of 2021 Q5.5/5.6 as marking evidence; the "
                           "method structure is still valid evidence for QUESTION-FAMILY-PHY-006."},

    {"type": "contradiction",
     "id": "UNRES-PHY-008",
     "summary": "2019 paper and memo state different durations",
     "detail": "Paper header DURATION 150 minutes; memo header DURATION 180 minutes for the same sitting (22 July 2019).",
     "affected": ["PHY-2019-MY"],
     "evidence": ["PHY-2019-MY paper header", "PHY-2019-MY memo header"],
     "recommended_review": "Cosmetic, but recorded because it shows the memo header is not always re-checked."},

    {"type": "contradiction",
     "id": "UNRES-PHY-009",
     "summary": "2019 memo answer numbering is misaligned in Questions 3 and 7",
     "detail": (
         "The memo labels the answer to 7.6 as '7.4', and the answers to 7.7.1 and 7.7.2 as '7.5.1' "
         "and '7.5.2'. In Question 3 the answer to 3.2.2 is labelled '3.2.3' immediately before the "
         "real 3.2.3. Answers were matched to questions by content and mark value, not by the printed "
         "memo number."
     ),
     "affected": ["physics_2019_internal_paper1_june_q7.6", "physics_2019_internal_paper1_june_q7.7.1",
                  "physics_2019_internal_paper1_june_q7.7.2", "physics_2019_internal_paper1_june_q3.2.2"],
     "evidence": ["PHY-2019-MY memo Question 3 and Question 7 blocks"],
     "recommended_review": "Verify the content-based alignment against the original memo before validation."},

    {"type": "contradiction",
     "id": "UNRES-PHY-010",
     "summary": "2023 memo cross-reference points at the wrong question number",
     "detail": "The memo's explanation for 8.8 is introduced as 'Explain the answer to QUESTION 7.7' "
               "although the paper's item is 8.8 (referring to 8.7).",
     "affected": ["physics_2023_internal_paper1_june_q8.8"],
     "evidence": ["PHY-2023-MY memo Q8.8"],
     "recommended_review": "Cosmetic mis-numbering; no effect on the content of the answer."},

    # ---------- fidelity / visual verification ----------
    {"type": "fidelity",
     "id": "UNRES-PHY-011",
     "summary": "Most records depend on a diagram that could not be verified from the text layer",
     "detail": (
         "197 of the 238 extracted records are flagged requires_visual_verification because the "
         "question's meaning depends on a circuit diagram, motion graph, apparatus drawing or "
         "energy-level diagram that exists only as an image in the PDF. Per the fidelity ladder "
         "(TWO_PASS_PROMPTS section 17.2) these families are capped at medium confidence where the "
         "diagram is load-bearing, even though the text layer itself is Rung A."
     ),
     "affected": ["QUESTION-FAMILY-PHY-003", "QUESTION-FAMILY-PHY-004", "QUESTION-FAMILY-PHY-005",
                  "QUESTION-FAMILY-PHY-009", "QUESTION-FAMILY-PHY-010", "QUESTION-FAMILY-PHY-011",
                  "QUESTION-FAMILY-PHY-012"],
     "evidence": ["requires_visual_verification counts in data/extracted/physics_pass1.json"],
     "recommended_review": "A human reviewer with the original PDFs open should confirm the diagram "
                           "content for the flagged records before any of these models is validated."},

    {"type": "fidelity",
     "id": "UNRES-PHY-012",
     "summary": "2021 memo answers to 9.2-9.5 are images and could not be read",
     "detail": (
         "The marking guidelines for 2021 Q9.2, 9.3, 9.4 and 9.5 contain only tick marks in the "
         "extractable text; the worked answers are images. Those four Pass 1 records carry "
         "memo_answer = 'unresolved' and ocr_uncertain = true."
     ),
     "affected": ["physics_2021_internal_paper1_nov_q9.2", "physics_2021_internal_paper1_nov_q9.3",
                  "physics_2021_internal_paper1_nov_q9.4", "physics_2021_internal_paper1_nov_q9.5"],
     "evidence": ["PHY-2021-NOV memo Question 9"],
     "recommended_review": "The 2023 memo answers the same three items in text (Q10.1-10.3), so "
                           "QUESTION-FAMILY-PHY-011 has usable memo evidence from 2023 and 2025; the "
                           "2021 items remain unverified."},

    {"type": "fidelity",
     "id": "UNRES-PHY-013",
     "summary": "2023 paper sub-question numbers were not recoverable from the text layer",
     "detail": (
         "Questions 4, 6.2-6.7 and the 7.1/7.2 sub-parts use auto-numbered lists in the source "
         "document, so the numbers did not extract. They were assigned by visual order and every "
         "affected record is flagged ocr_uncertain. If the original numbering differs, the source_ids "
         "for those records change."
     ),
     "affected": ["physics_2023_internal_paper1_june_q4.*", "physics_2023_internal_paper1_june_q2.6.*"],
     "evidence": ["PHY-2023-MY paper Questions 2.6, 4, 6, 7"],
     "recommended_review": "Confirm the printed sub-numbers against the original PDF; re-run Pass 1 for "
                           "that paper if they differ."},

    # ---------- data quality in the inherited inputs ----------
    {"type": "data_quality",
     "id": "UNRES-PHY-014",
     "summary": "The inherited Pass 1 batch contained no question content",
     "detail": (
         "Before this run, data/extracted/physics_pass1.json held 15 records - one per paper - in "
         "which question_text, marks, memo_answer, memo_method_steps and topic_guess were all "
         "'unresolved', and the years in the source_ids were wrong ('physics_2026_...' for a 2019 "
         "paper). The generator script states that no PDF extraction package was available; pypdf "
         "extracts these files cleanly, so that constraint did not hold. All 102 records across the "
         "seven subject files were affected. Pass 2 could not have cited any evidence from that batch."
     ),
     "affected": ["data/extracted/all_subjects_pass1.json", "data/extracted/physics_pass1.json",
                  "data/extracted/ap_mathematics_pass1.json", "data/extracted/biology_pass1.json",
                  "data/extracted/chemistry_pass1.json", "data/extracted/english_pass1.json",
                  "data/extracted/history_pass1.json", "data/extracted/mathematics_pass1.json"],
     "evidence": ["scripts/complete_subject_pass1.py", "git show f91de4f --stat"],
     "recommended_review": "Physics has been rebuilt from the source PDFs. The other six subject files "
                           "still hold the hollow records and must be rebuilt before Pass 2 is run for "
                           "those subjects."},

    {"type": "data_quality",
     "id": "UNRES-PHY-015",
     "summary": "sample_manifest.json pairs four physics papers with the wrong memorandum",
     "detail": (
         "Header comparison (printed DATE, MARKS, EXAMINER) shows the manifest pairs: "
         "'PS11 Physics September Exam 2021 QP' (13 September 2021) with the November 2021 memo; "
         "'G11 July Physics Exam 2022 QP' (13 July 2022) with the November 2022 memo; "
         "'PS11 - Physics- Mid-Year - QP - 2025' (15 July 2025, 135 marks) with the IeBT MCQ memo "
         "(15 July 2025, 20 marks); and 'PS11- P1-Physics - IeBT - MCQ - 2024' (40 marks) with the "
         "135-mark Final Exam memo. None of these pairings was used as memo evidence in this run."
     ),
     "affected": ["data/organized/sample_manifest.json"],
     "evidence": ["scripts/build_physics_pass1.py verify_alignment()", "printed header blocks of each PDF"],
     "recommended_review": "Correct the manifest, or record these four papers as having no memorandum in "
                           "the organized sample."},

    {"type": "data_quality",
     "id": "UNRES-PHY-016",
     "summary": "'PS11- P1-Physics - IeBT - MCQ - 2024.pdf' is a memorandum, not a question paper",
     "detail": (
         "The file contains a 20-item answer grid (1-20 with crossed options), a header ending in "
         "'MEMO', MARKS 40 and DURATION 60 minutes for 08 November 2024. Its question paper is not "
         "in the organized sample."
     ),
     "affected": ["data/organized/physics/PS11- P1-Physics - IeBT - MCQ - 2024.pdf"],
     "evidence": ["extracted text of the file"],
     "recommended_review": "Re-file as a memo and locate the matching IeBT MCQ question paper."},

    # ---------- coverage ----------
    {"type": "coverage_gap",
     "id": "UNRES-PHY-017",
     "summary": "Nine further physics papers in the organized sample were not extracted in this run",
     "detail": (
         "Extracted: 2019 mid-year, 2021 November, 2023 mid-year, 2025 November. Not extracted: "
         "2020 November (QP exists as both .pdf and .docx), September 2021 (no memo), July 2022 "
         "(no memo), November 2022 (memo verified), November 2023, mid-year 2024, mid-year 2025 "
         "(no memo), IeBT 2025 (memo is an image), IeBT MCQ 2024 (memo only). The 2022, 2023 and "
         "2024 papers in particular would add exemplars to families currently resting on 2-3 papers."
     ),
     "affected": ["data/organized/physics/"],
     "evidence": ["data/extracted/pass1/physics/_BATCH_SUMMARY.json"],
     "recommended_review": "Run Pass 1 on the remaining paired papers, then re-run Pass 2 on the larger batch."},

    {"type": "curriculum_gap",
     "id": "UNRES-PHY-018",
     "summary": "Topics listed in the Pass 1 topic list have no or almost no evidence in this batch",
     "detail": (
         "The Pass 1 prompt's Physics topic list includes Waves Sound Light, Electrostatics and "
         "Electromagnetism. In this batch: Electrostatics appears only in 2025 Q6.2 (one item, one "
         "paper); Electromagnetism (motors, generators, transformers, electromagnetic induction) "
         "appears nowhere; Waves Sound Light appears only as photons/energy levels, with no "
         "mechanical waves, sound or geometric optics. Mechanics-Momentum appears only in 2025. "
         "The tutor must not answer as if these topics are grounded in the knowledge bank."
     ),
     "affected": ["UNDERSTANDING-PHY-011", "UNDERSTANDING-PHY-014"],
     "evidence": ["topic_guess distribution in data/extracted/physics_pass1.json"],
     "recommended_review": "Targeted acquisition: papers covering electrostatics, electromagnetism and "
                           "waves/optics, and at least two more papers containing momentum."},

    {"type": "unsampled_stratum",
     "id": "UNRES-PHY-019",
     "summary": "The IEB stratum and the multiple-choice stratum are not represented in the 2025 sitting",
     "detail": (
         "All four extracted papers are internally set school papers (exam_board = internal). The two "
         "IeBT papers in the sample were not usable: the 2025 IeBT memo is an image and the 2024 IeBT "
         "item is a memo without its paper. The 2025 paper also has no multiple-choice section, so "
         "QUESTION-FAMILY-PHY-012 rests on 2019, 2021 and 2023 only."
     ),
     "affected": ["QUESTION-FAMILY-PHY-012"],
     "evidence": ["exam_board field of all extracted records", "PHY-2025-NOV question list"],
     "recommended_review": "Acquire an IeBT question paper with a readable memo before claiming any "
                           "pattern is board-independent."},

    {"type": "curriculum_gap",
     "id": "UNRES-PHY-020",
     "summary": "No authoritative curriculum document was available to map topics against",
     "detail": (
         "data/organized/physics contains only papers and memoranda; the curriculum files in the "
         "sample belong to biology (source booklets). Topic labels in the Pass 1 records are "
         "therefore guesses based on the papers' own printed section headings (for example 2023 "
         "prints 'KINEMATICS - HORIZONTAL MOTION') and on the Pass 1 prompt's topic list. No "
         "curriculum mapping rate can be reported for this subject yet."
     ),
     "affected": ["all physics Pass 1 records"],
     "evidence": ["data/organized/physics/ file listing", "data/organized/sample_manifest.json curriculum fields"],
     "recommended_review": "Obtain the Grade 11 Physics curriculum/assessment plan from the ORC before "
                           "topic labels are treated as anything other than guesses."},

    {"type": "data_quality",
     "id": "UNRES-PHY-025",
     "summary": "The Phase 3 acquisition inventory has not been reconciled with data/organized/",
     "detail": (
         "data/raw/physics/SOURCE_INVENTORY.yaml lists all 233 ORC sources as access_status "
         "'inaccessible' with local_path null, and STATUS.md still reports 818 failed "
         "acquisitions. In fact data/organized/ holds 163 tracked source files, including the 25 "
         "physics documents this run used; the four processed papers and their memoranda were "
         "matched back to ORC records SOURCE-ORC-PHY-2019-132/133, 2021-137/138, 2023-145/146 and "
         "2025-154/155 by title. The inventory therefore understates what the repository holds, "
         "and its per-source hashes and access statuses are unverified."
     ),
     "affected": ["data/raw/physics/SOURCE_INVENTORY.yaml", "STATUS.md"],
     "evidence": ["git ls-files data/raw", "git ls-files data/organized | wc -l",
                  "orc_source_id field of the Pass 1 records"],
     "recommended_review": "Re-run Phase 3 reconciliation against data/organized/ so the inventory "
                           "records local_path and file_hash for the files actually held."},
]
