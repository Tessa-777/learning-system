"""Tests for the Phase 3 corpus-sufficiency revision.

Written with the standard library ``unittest`` so they run in restricted
environments where pytest cannot be installed. They also run under pytest
unchanged.

Several of these are regression tests for defects found while building the
revision; each such test names the defect in its docstring.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
import zlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core import yamllite
from core.schema import JSONSCHEMA_BACKEND, SchemaValidator
from ingestion.acquisition.content_probe import probe
from ingestion.acquisition.forms import classify_form, is_out_of_scope, normalize_title
from ingestion.acquisition.inventory import (
    drive_file_id,
    read_inventory_header,
    read_source_records,
)
from ingestion.acquisition.selection import (
    build_subject_selection,
    pair_memo,
)

SUBJECTS = ("biology", "physics", "history", "english", "ap_mathematics", "mathematics")
def _inventory(subject: str) -> Path:
    return REPO_ROOT / "data" / "raw" / subject / "SOURCE_INVENTORY.yaml"


def _record(**kwargs):
    base = {
        "source_id": None, "subject": None, "grade": "11", "document_type": None,
        "title": None, "year": None, "term": None, "paper_number": None,
        "source_url": None, "retrieved_at": None, "access_status": "accessible",
        "local_path": None, "file_hash": None,
    }
    base.update(kwargs)
    return base


def _pdf_bytes(lines):
    stream = b"".join(f"BT /F1 12 Tf ({line}) Tj ET\n".encode() for line in lines)
    compressed = zlib.compress(stream)
    return (
        b"%PDF-1.4\n1 0 obj\n<< /Length " + str(len(compressed)).encode()
        + b" /Filter /FlateDecode >>\nstream\n" + compressed
        + b"\nendstream\nendobj\ntrailer\n<<>>\n%%EOF\n"
    )


def _docx_bytes(paragraphs):
    body = "".join(
        f"<w:p><w:r><w:t>{text}</w:t></w:r></w:p>" for text in paragraphs
    )
    xml = f'<?xml version="1.0"?><w:document xmlns:w="x"><w:body>{body}</w:body></w:document>'
    import io

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("word/document.xml", xml)
    return buffer.getvalue()


# ==========================================================================
# yamllite
# ==========================================================================

class TestYamlLite(unittest.TestCase):
    def test_config_round_trips(self):
        for name in ("settings", "subjects"):
            with self.subTest(name):
                data = yamllite.load(REPO_ROOT / "config" / f"{name}.yaml")
                self.assertIsInstance(data, dict)
                self.assertEqual(yamllite.loads(yamllite.dumps(data)), data)

    def test_sequence_at_key_indent_parses(self):
        """Block sequences may sit at the same indent as their key (PyYAML style)."""
        text = "root:\n  items:\n  - a\n  - b\n  nested:\n    k: v\n"
        self.assertEqual(
            yamllite.loads(text),
            {"root": {"items": ["a", "b"], "nested": {"k": "v"}}},
        )

    def test_list_of_maps_with_nested_values(self):
        text = (
            "papers:\n"
            "- source_id: A\n"
            "  title: T\n"
            "  flags:\n"
            "  - f1\n"
            "  - f2\n"
            "- source_id: B\n"
            "  title: U\n"
            "  flags: []\n"
        )
        parsed = yamllite.loads(text)
        self.assertEqual(len(parsed["papers"]), 2)
        self.assertEqual(parsed["papers"][0]["flags"], ["f1", "f2"])
        self.assertEqual(parsed["papers"][1]["flags"], [])

    def test_selection_artifact_reparses(self):
        path = REPO_ROOT / "data" / "raw" / "CORPUS_SELECTION.yaml"
        if not path.exists():
            self.skipTest("selection not built yet")
        data = yamllite.load(path)
        self.assertEqual(set(data["subjects"]), set(SUBJECTS))
        totals = data["totals"]
        self.assertEqual(
            totals["documents_to_acquire"],
            totals["papers"] + totals["memoranda"]
            + totals["companions"] + totals["curriculum_anchors"],
        )

    def test_scalar_typing(self):
        parsed = yamllite.loads(
            "a: 1\nb: 1.5\nc: true\nd: null\ne: 'quoted'\nf: plain text\ng: {}\nh: []\n"
        )
        self.assertEqual(parsed["a"], 1)
        self.assertEqual(parsed["b"], 1.5)
        self.assertIs(parsed["c"], True)
        self.assertIsNone(parsed["d"])
        self.assertEqual(parsed["e"], "quoted")
        self.assertEqual(parsed["f"], "plain text")
        self.assertEqual(parsed["g"], {})
        self.assertEqual(parsed["h"], [])

    def test_url_with_hash_is_not_treated_as_comment(self):
        parsed = yamllite.loads("url: 'https://x/y#frag'\n")
        self.assertEqual(parsed["url"], "https://x/y#frag")


# ==========================================================================
# inventory reader
# ==========================================================================

class TestInventoryReader(unittest.TestCase):
    def test_source_id_is_populated(self):
        """Regression: records open with '- source_id:' at column 0 while every
        sibling field is indented two spaces. Restoring the indentation is
        required, otherwise every source_id reads back as None and selections
        silently collapse to one item per subject."""
        for subject in SUBJECTS:
            with self.subTest(subject):
                records = read_source_records(_inventory(subject))
                self.assertTrue(records)
                for record in records:
                    self.assertIsNotNone(record["source_id"], record["title"])

    def test_record_count_matches_header(self):
        for subject in SUBJECTS:
            with self.subTest(subject):
                path = _inventory(subject)
                header = read_inventory_header(path)
                records = read_source_records(path)
                self.assertEqual(header["record_count"], len(records))
                self.assertEqual(header["subject"], subject)

    def test_source_ids_are_unique(self):
        seen = set()
        for subject in SUBJECTS:
            for record in read_source_records(_inventory(subject)):
                self.assertNotIn(record["source_id"], seen)
                seen.add(record["source_id"])

    def test_drive_file_id_extraction(self):
        self.assertEqual(
            drive_file_id("https://drive.google.com/file/d/ABC-123_xyz"), "ABC-123_xyz"
        )
        self.assertEqual(
            drive_file_id("https://drive.google.com/uc?id=ABC123&export=download"), "ABC123"
        )
        self.assertIsNone(drive_file_id(None))
        self.assertIsNone(drive_file_id("https://example.com/x.pdf"))


# ==========================================================================
# form classification
# ==========================================================================

class TestFormClassification(unittest.TestCase):
    def test_filing_prefix_is_not_read_as_paper_number(self):
        """Regression: '1a. Midyear paper 2.pdf' must be Paper 2. The leading
        '1a.' is an ORC filing-sequence marker, not a paper number."""
        stratum = classify_form("mathematics", "1a. Midyear paper 2.pdf")
        self.assertEqual(stratum.paper_form, "P2")
        stratum = classify_form("mathematics", "3a. Nov 2018 Exam Paper 1.pdf")
        self.assertEqual(stratum.paper_form, "P1")
        self.assertEqual(stratum.session, "final")

    def test_paper_number_run_into_next_word(self):
        """Regression: the ORC filename '1a. Mid-year Paper 1pdf.pdf' is a typo
        for 'Paper 1 pdf'. A trailing \\b would miss it; (?![0-9]) does not, and
        still rejects a genuine 'Paper 10'."""
        self.assertEqual(
            classify_form("mathematics", "1a. Mid-year Paper 1pdf.pdf").paper_form, "P1"
        )
        self.assertEqual(
            classify_form("mathematics", "Paper 10.pdf").paper_form, "unknown"
        )

    def test_ieb_trial_is_externally_set(self):
        stratum = classify_form("physics", "2022_G11_Physics_IeBT-P1_QP.pdf")
        self.assertEqual(stratum.setter, "ieb_external")
        self.assertEqual(stratum.paper_form, "P1")
        self.assertEqual(stratum.session, "trial")

    def test_internal_exam_is_school_set(self):
        stratum = classify_form("physics", "2022_G11_Physics_Nov-Exam_QP.pdf")
        self.assertEqual(stratum.setter, "school_internal")
        self.assertEqual(stratum.session, "final")

    def test_mcq_detected(self):
        self.assertEqual(
            classify_form("physics", "2024_G11_Physics_IeBT-MCQ_QP.pdf").paper_form, "MCQ"
        )

    def test_ap_maths_content_names_map_to_paper_forms(self):
        self.assertEqual(
            classify_form("ap_mathematics", "1a.SBC G11 AP 2013 CALCULUS AND ALGEBRA.pdf").paper_form,
            "P1",
        )
        self.assertEqual(
            classify_form("ap_mathematics", "2a. SBC G11 2013 AP STATS.pdf").paper_form, "P2"
        )

    def test_chemistry_is_out_of_scope_for_physics(self):
        """The ORC Physics folder holds Physical Sciences Chemistry material."""
        self.assertIsNotNone(is_out_of_scope("physics", "IeBT 2021 Chemistry P2"))
        self.assertIsNone(is_out_of_scope("physics", "IeBT 2021 Physics P2"))

    def test_other_grades_are_out_of_scope(self):
        self.assertIsNotNone(is_out_of_scope("english", "MEMO Contextual Test Film Grade 12"))
        self.assertIsNone(is_out_of_scope("english", "Grade 11 Paper 2 July 2018.pdf"))

    def test_other_subjects_are_out_of_scope(self):
        self.assertIsNotNone(is_out_of_scope("mathematics", "Grade 11 Accounting P1"))

    def test_normalize_title_strips_noise(self):
        self.assertEqual(
            normalize_title("3b. Nov 2018 Exam Paper 1 Memo.pdf"), "nov 2018 exam paper 1"
        )
        # Filing prefix and the "Memo" noise token are both removed.
        self.assertNotIn("memo", normalize_title("3b. Nov 2018 Exam Paper 1 Memo.pdf"))
        self.assertNotIn("3b", normalize_title("3b. Nov 2018 Exam Paper 1 Memo.pdf"))


# ==========================================================================
# memorandum pairing
# ==========================================================================

class TestMemoPairing(unittest.TestCase):
    def test_stratum_year_unique(self):
        paper = _record(source_id="P1", title="IeBT 2023 G11 PS P1", year=2023,
                        document_type="past_paper")
        memos = [
            _record(source_id="M1", title="IeBT 2023 P1 Memo", year=2023,
                    document_type="memorandum"),
            _record(source_id="M2", title="IeBT 2023 P2 Memo", year=2023,
                    document_type="memorandum"),
        ]
        result = pair_memo(paper, "physics", memos)
        self.assertEqual(result.source_id, "M1")
        self.assertEqual(result.method, "stratum_year_unique")
        self.assertEqual(result.confidence, "high")

    def test_paper_form_must_agree(self):
        """A Paper 1 memorandum must never be attached to a Paper 2 paper."""
        paper = _record(source_id="P1", title="Grade 11 Paper 2 July 2018.pdf", year=2018,
                        document_type="past_paper")
        memos = [_record(source_id="M1", title="Grade 11 Paper 1 July 2018 Memo.pdf",
                         year=2018, document_type="memorandum")]
        self.assertIsNone(pair_memo(paper, "english", memos).source_id)

    def test_out_of_scope_memo_is_never_paired(self):
        """Regression: English P2 2023 was structurally matched to a Grade 12
        memorandum that Phase 2 had already marked out of scope. The memo pool
        must be scope-filtered by the caller, which build_subject_selection
        does; this asserts the filter itself rejects the record."""
        self.assertIsNotNone(
            is_out_of_scope("english", "Copy of MEMO Contextual Test Film Grade 12 2023")
        )

    def test_structural_match_wins_over_naming_conventions(self):
        """stratum_year_unique is the strongest signal and must pre-empt the
        filename-convention strategies, which depend on how a human happened to
        name the upload."""
        paper = _record(source_id="P1", title="3a. Nov 2018 Exam Paper 1.pdf", year=2018,
                        document_type="past_paper")
        memos = [_record(source_id="M1", title="3b. Nov 2018 Exam Paper 1 Memo.pdf",
                         year=2018, document_type="memorandum")]
        result = pair_memo(paper, "mathematics", memos)
        self.assertEqual(result.source_id, "M1")
        self.assertEqual(result.method, "stratum_year_unique")
        self.assertEqual(result.confidence, "high")

    def test_order_prefix_disambiguates_when_structure_cannot(self):
        """Two memoranda share the year and form, so only the ORC filing-prefix
        convention (3a. paper <-> 3b. memo) can separate them."""
        paper = _record(source_id="P1", title="3a. Nov 2018 Exam Paper 1.pdf", year=2018,
                        document_type="past_paper")
        memos = [
            _record(source_id="M1", title="3b. Nov 2018 Exam Paper 1 Memo.pdf", year=2018,
                    document_type="memorandum"),
            _record(source_id="M3", title="9b. Nov 2018 Paper 1 Memo.pdf", year=2018,
                    document_type="memorandum"),
        ]
        result = pair_memo(paper, "mathematics", memos)
        self.assertEqual(result.source_id, "M1")
        self.assertEqual(result.method, "order_prefix")

    def test_ambiguous_prefix_is_reported_low_confidence(self):
        """When the filing prefix matches several memoranda the pairing must be
        flagged for a human rather than guessed."""
        paper = _record(source_id="P1", title="2a. Grade 11 Paper 2.pdf", year=2020,
                        document_type="past_paper")
        memos = [
            _record(source_id="M1", title="2b. Grade 11 Paper 2 Memo A.pdf", year=2020,
                    document_type="memorandum"),
            _record(source_id="M2", title="2c. Grade 11 Paper 2 Memo B.pdf", year=2020,
                    document_type="memorandum"),
        ]
        result = pair_memo(paper, "mathematics", memos)
        self.assertIsNone(result.source_id)
        self.assertEqual(result.method, "order_prefix")
        self.assertEqual(result.confidence, "low")

    def test_qp_mg_suffix_disambiguates_when_structure_cannot(self):
        paper = _record(source_id="P1", title="2025_G11_Physics_MidYear-Exam_QP.pdf",
                        year=2025, document_type="past_paper")
        memos = [
            _record(source_id="M1", title="2025_G11_Physics_MidYear-Exam_MG.pdf", year=2025,
                    document_type="marking_guide"),
            _record(source_id="M2", title="G11 - MG - Physics Mid-Year Exam - 2025.pdf",
                    year=2025, document_type="marking_guide"),
        ]
        result = pair_memo(paper, "physics", memos)
        self.assertEqual(result.source_id, "M1")
        self.assertEqual(result.method, "qp_mg_suffix")

    def test_no_memo_returns_explicit_none(self):
        paper = _record(source_id="P1", title="GR 11 JULY EXAM 2013 P1.docx", year=2013,
                        document_type="past_paper")
        result = pair_memo(paper, "history", [])
        self.assertIsNone(result.source_id)
        self.assertEqual(result.method, "none")
        self.assertEqual(result.confidence, "none")


# ==========================================================================
# selection
# ==========================================================================

class TestSelection(unittest.TestCase):
    def _corpus(self):
        records = [
            _record(source_id="P-2025", title="Gr11 P1 Nov Exam.pdf", year=2025,
                    document_type="past_paper"),
            _record(source_id="M-2025", title="Gr11 P1 Nov Exam Memo.pdf", year=2025,
                    document_type="memorandum"),
            _record(source_id="P-2019", title="Nov 2019 Paper 1.pdf", year=2019,
                    document_type="past_paper"),
            _record(source_id="P-2018-P2", title="4a. Nov 2018 Exam Paper 2.pdf", year=2018,
                    document_type="past_paper"),
            _record(source_id="M-2018-P2", title="4b. Nov 2018 Exam Paper 2 Memo.pdf",
                    year=2018, document_type="memorandum"),
        ]
        return records

    def test_budget_respected(self):
        result = build_subject_selection("mathematics", self._corpus(), papers_per_subject=2)
        self.assertLessEqual(len(result.papers), 2)

    def test_memo_availability_is_a_selection_criterion(self):
        """Regression: History selected five papers and none of them was the one
        paper in the corpus that actually has a memorandum."""
        records = self._corpus() + [
            _record(source_id="P-orphan", title="Nov 2024 Paper 1.pdf", year=2024,
                    document_type="past_paper"),
        ]
        result = build_subject_selection("mathematics", records, papers_per_subject=2)
        chosen = {p.source_id for p in result.papers}
        self.assertIn("P-2025", chosen)  # has a memo, same stratum as P-orphan
        self.assertNotIn("P-orphan", chosen)

    def test_depth_pass_prefers_a_wide_year_gap(self):
        result = build_subject_selection(
            "mathematics", self._corpus(), papers_per_subject=4, min_year_gap=3
        )
        p1_final = [p for p in result.papers
                    if p.stratum.paper_form == "P1" and p.stratum.session == "final"]
        years = sorted(p.year for p in p1_final)
        if len(years) == 2:
            self.assertGreaterEqual(years[1] - years[0], 3)

    def test_companion_documents_are_attached(self):
        records = [
            _record(source_id="P1", title="Copy of Gr 11- Exam - Cold War - Exam - Oct 2017.docx",
                    year=2017, document_type="past_paper"),
            _record(source_id="M1", title="Copy of Gr 11- Exam - Cold War - Exam MEMO - Oct 2017.docx",
                    year=2017, document_type="memorandum"),
            _record(source_id="C1", title="Copy of Gr 11- Exam Source Booklet - Cold War - Exam - Oct 2017.docx",
                    year=2017, document_type="reference"),
        ]
        result = build_subject_selection("history", records)
        self.assertEqual(len(result.papers), 1)
        self.assertEqual([c["source_id"] for c in result.papers[0].companions], ["C1"])

    def test_curriculum_anchor_detected(self):
        records = self._corpus() + [
            _record(source_id="A1", title="IEB - SAG - PS (Subject Assessment Guidelines)",
                    year=None, document_type="curriculum"),
        ]
        result = build_subject_selection("physics", records)
        self.assertEqual([a["source_id"] for a in result.curriculum_anchors], ["A1"])

    def test_missing_anchor_is_reported_as_a_note(self):
        result = build_subject_selection("mathematics", self._corpus())
        self.assertEqual(result.curriculum_anchors, [])
        self.assertTrue(any("curriculum" in note.lower() for note in result.notes))

    def test_unpaired_memo_is_flagged_not_inferred(self):
        records = [_record(source_id="P1", title="GR 11 JULY EXAM 2013 P1.docx", year=2013,
                           document_type="past_paper")]
        result = build_subject_selection("history", records)
        self.assertIn("no_memorandum_in_corpus", result.papers[0].flags)
        self.assertIsNone(result.papers[0].memo.source_id)

    def test_out_of_scope_papers_excluded(self):
        records = self._corpus() + [
            _record(source_id="CHEM", title="IeBT 2021 Chemistry P2", year=2021,
                    document_type="past_paper"),
        ]
        result = build_subject_selection("physics", records)
        self.assertNotIn("CHEM", {p.source_id for p in result.papers})
        self.assertIn("CHEM", {e["source_id"] for e in result.excluded})

    def test_selection_is_deterministic(self):
        first = build_subject_selection("mathematics", self._corpus())
        second = build_subject_selection("mathematics", self._corpus())
        self.assertEqual(
            [(p.source_id, p.stratum.key()) for p in first.papers],
            [(p.source_id, p.stratum.key()) for p in second.papers],
        )

    def test_real_inventories_produce_a_bounded_sample(self):
        total = 0
        for subject in SUBJECTS:
            with self.subTest(subject):
                records = read_source_records(_inventory(subject))
                result = build_subject_selection(subject, records)
                self.assertLessEqual(len(result.papers), 5)
                self.assertTrue(result.papers)
                for paper in result.papers:
                    self.assertIsNotNone(paper.source_id)
                    self.assertIsNotNone(paper.source_url)
                total += len(result.papers)
        self.assertLessEqual(total, 30)


# ==========================================================================
# content probe
# ==========================================================================

class TestContentProbe(unittest.TestCase):
    def test_docx_memorandum_classified(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "memo.docx"
            path.write_bytes(_docx_bytes([
                "GRADE 11 HISTORY MEMORANDUM",
                "Question 1: Accept any two of the following. 2x2=(4)",
                "Do not accept irrelevant responses.",
            ]))
            result = probe(path)
            self.assertTrue(result.text_extracted)
            self.assertEqual(result.document_type, "memorandum")
            self.assertEqual(result.document_type_confidence, "high")
            self.assertFalse(result.visual_dependency)

    def test_docx_question_paper_with_diagram_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "paper.docx"
            path.write_bytes(_docx_bytes([
                "GRADE 11 PHYSICS QUESTION PAPER",
                "EXAMINER: Mr Hilder   TOTAL: 200",
                "Answer all questions. Please read the following instructions.",
                "QUESTION 2 - Refer to the graph shown below and the circuit diagram.",
            ]))
            result = probe(path)
            self.assertEqual(result.document_type, "past_paper")
            self.assertTrue(result.visual_dependency)
            self.assertIn("diagram", result.visual_signals)

    def test_pdf_text_extracted(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "paper.pdf"
            path.write_bytes(_pdf_bytes([
                "GRADE 11 MATHEMATICS QUESTION PAPER",
                "Answer all questions. TOTAL: 150",
                "Refer to the diagram below",
            ]))
            result = probe(path)
            self.assertTrue(result.text_extracted)
            self.assertEqual(result.detected_format, "pdf")
            self.assertEqual(result.document_type, "past_paper")
            self.assertTrue(result.visual_dependency)

    def test_legacy_doc_reports_honest_failure(self):
        """An unreadable file must be recorded as unresolved, never guessed at."""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "legacy.doc"
            path.write_bytes(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1" + b"\x00" * 64)
            result = probe(path)
            self.assertFalse(result.text_extracted)
            self.assertEqual(result.extraction_confidence, "none")
            self.assertIsNone(result.document_type)
            self.assertIsNotNone(result.error)

    def test_empty_pdf_yields_no_document_type(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "blank.pdf"
            path.write_bytes(_pdf_bytes([]))
            result = probe(path)
            self.assertIsNone(result.document_type)


# ==========================================================================
# schema validator fallback
# ==========================================================================

class TestSchemaFallback(unittest.TestCase):
    def setUp(self):
        self.validator = SchemaValidator(REPO_ROOT / "database" / "schema")

    def _valid_record(self):
        return {
            "source_id": "SOURCE-ORC-MAT-2025-001", "subject": "mathematics",
            "grade": "11", "document_type": "past_paper", "title": "P1",
            "year": 2025, "term": 4, "paper_number": 1,
            "source_url": "https://drive.google.com/file/d/abc",
            "retrieved_at": "2026-09-04T00:00:00Z", "access_status": "accessible",
            "local_path": "data/raw/mathematics/papers/P1.pdf",
            "file_hash": "0" * 64, "notes": "n",
        }

    def test_valid_record_passes(self):
        self.assertTrue(
            self.validator.validate("source_metadata.schema.json", self._valid_record()).valid
        )

    def test_missing_required_field_detected(self):
        record = self._valid_record()
        del record["subject"]
        result = self.validator.validate("source_metadata.schema.json", record)
        self.assertFalse(result.valid)

    def test_bad_enum_detected(self):
        record = self._valid_record()
        record["access_status"] = "downloaded"
        self.assertFalse(
            self.validator.validate("source_metadata.schema.json", record).valid
        )

    def test_additional_property_detected(self):
        record = self._valid_record()
        record["acquisition_mode"] = "proxy"
        self.assertFalse(
            self.validator.validate("source_metadata.schema.json", record).valid
        )

    def test_backend_is_reported(self):
        self.assertIn(JSONSCHEMA_BACKEND, ("jsonschema", "mini"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
