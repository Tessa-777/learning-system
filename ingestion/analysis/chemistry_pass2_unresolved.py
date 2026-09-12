"""Pass 2 analysis (Tier 2/3) for Chemistry — unresolved items authored for this run.

Authored to mirror ``ingestion/analysis/physics_pass2_unresolved.py`` in shape. Two
kinds of unresolved item live here: (a) standing review-queue items the analysis knows
about up front (image dependency and the Phase-2 ORC acquisition gap), and (b) derived
items the build appends after the family partition is computed (UNRES-CHEM-021 unassigned
records, UNRES-CHEM-022 single-paper families, UNRES-CHEM-023 thin breakdowns, plus the
deferred candidate families). The build rewrites ``affected`` for UNRES-CHEM-011 from the
actual family distribution, so its placeholder here is empty.
"""

UNRESOLVED = [
    {
        "type": "image_dependent",
        "id": "UNRES-CHEM-011",
        "summary": "Several families rest heavily on diagram- or image-dependent questions whose text layer was readable but whose diagram could not be verified",
        "detail": (
            "Chemistry questions frequently depend on a structure, apparatus or graph image. In this "
            "batch the text layer (Rung A) was transcribed, but the diagrams could not be visually "
            "verified, so the breakdowns and diagnostics that lean on them are unvalidated. The build "
            "appends the per-family image-dependency counts to this item."
        ),
        "affected": [],
        "evidence": [
            "chemistry_pass1_evidence modules: requires_visual_verification=True on diagram questions",
            "no data/raw/chemistry/SOURCE_INVENTORY.yaml exists (ORC never ran for chemistry)",
        ],
        "recommended_review": (
            "Where a family is majority image-dependent, verify the diagram against the source PDF before "
            "using its diagnostics in production; a tutor should not generate a diagnosis from a diagram "
            "that was never visually confirmed."
        ),
    },
    {
        "type": "provenance_gap",
        "id": "UNRES-CHEM-ACQ-001",
        "summary": "Chemistry Phase 2 (ORC) was never run, so no SOURCE-* id is available for the Pass 1 records",
        "detail": (
            "The repository has data/raw/physics/SOURCE_INVENTORY.yaml mapping question records to ORC "
            "SOURCE-* ids, but no equivalent exists for chemistry and the ORC step was never executed for "
            "the chemistry corpus. Per AGENTS.md and SUBJECT_PROMPTS.md, a fake inventory must NOT be "
            "invented. Every chemistry Pass 2 object therefore carries the sentinel "
            "SOURCE-ORC-CHEM-NOT-INDEXED as its orc_source_id, and this unresolved item records the gap. "
            "The referential chain chemistry_{year}_{board}_{ptype}_{period}_q{qn} -> "
            "SOURCE-ORC-CHEM-NOT-INDEXED terminates at the sentinel rather than at a real ORC id."
        ),
        "affected": ["SOURCE-ORC-CHEM-NOT-INDEXED"],
        "evidence": [
            "data/raw/chemistry/SOURCE_INVENTORY.yaml does not exist",
            "SUBJECT_PROMPTS.md: do not invent ORC ids or a fake inventory",
            "knowledge/chemistry/* orc_source_id == SOURCE-ORC-CHEM-NOT-INDEXED",
        ],
        "recommended_review": (
            "Run the Phase 2 ORC acquisition for chemistry and create data/raw/chemistry/SOURCE_INVENTORY.yaml; "
            "then map each chemistry_{...}_q{qn} source_id to a real SOURCE-* id and re-point the provenance chain."
        ),
    },
    {
        "type": "marking_anomaly",
        "id": "UNRES-CHEM-012",
        "summary": "Two marking anomalies were resolved during transcription using the question paper as authoritative",
        "detail": (
            "CHE-2024-NOV: the memo header for Question 5 reads '29 MARKS' but the question paper and the "
            "memo marks sum to 13; the memo also prints an incorrect formula for Q6.4.1 "
            "(CnH2n+2O2 instead of CnH2nO2). CHE-2025-JUL: the memo header swaps the Question 5 and "
            "Question 6 totals; the question paper (Q5=14, Q6=17) is authoritative. All were resolved in "
            "favour of the question paper; recorded here so a later reviewer knows the memo was overruled."
        ),
        "affected": ["chemistry_2024_nov_q5", "chemistry_2024_nov_q6", "chemistry_2025_july_q5", "chemistry_2025_july_q6"],
        "evidence": [
            "chemistry_pass1_evidence_2024_nov.py header note on Q5/Q6 memo misprints",
            "chemistry_pass1_evidence_2025_july.py header note on Q5/Q6 total swap",
        ],
        "recommended_review": "Confirm against a clean copy of the 2024 November and 2025 July memoranda if one becomes available.",
    },
    {
        "type": "visual_only_item",
        "id": "UNRES-CHEM-013",
        "summary": "A few questions could only be partially transcribed because the answer depends on an unreadable image",
        "detail": (
            "CHE-2024-NOV Question 6 asks for a flow-diagram completion whose boxes are images, and "
            "CHE-2025-NOV Questions 5.4-5.6 ask about displayed organic structures labelled X and Y that "
            "are images. The text was transcribed and the items were placed in their families, but the "
            "diagram content itself (which bonds, which isomers) could not be confirmed. They are marked "
            "requires_visual_verification=True and must not be used to assert a structural claim."
        ),
        "affected": ["chemistry_2024_nov_q6", "chemistry_2025_nov_q5"],
        "evidence": [
            "chemistry_pass1_evidence_2024_nov.py Q6 flow-diagram sub-questions",
            "chemistry_pass1_evidence_2025_nov.py X/Y displayed-structure items",
        ],
        "recommended_review": "Recover the source images and transcribe the structures before using these items in a diagnostic.",
    },
]
