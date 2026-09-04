"""Assessment-form classification for corpus selection.

Purpose
-------
Question families are a function of a paper's **assessment form** — who set it,
which paper number it is, and which sitting it belongs to — not of its topics or
its year. Evidence for this is in the corpus itself:

* the Nov 2018 Mathematics Paper 2 declares its own structure in its mark
  table (Statistics, Analytical Geometry, Euclidean Geometry, Trigonometry,
  Measurement) and that structure repeats across years;
* the Nov 2022 Physics paper labels its own questions with family headings
  (``KINEMATICS GRAPH``, ``HORIZONTAL MOTION``, ``PROJECTILE MOTION``);
* the Nov 2017 History paper declares ``Section 1 – Single Source Analysis``,
  ``Section 2 – Multiple Source Questions``, ``Section 3 – Source Based Essay``.

Sampling is therefore stratified on form. This module assigns each discovered
past paper to a ``FormStratum``.

The classifier is intentionally conservative: when it cannot determine a
dimension it returns ``"unknown"`` rather than guessing, and callers must treat
``unknown`` strata as requiring human review (AGENTS.md rule 7 — separate fact
from inference).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional

__all__ = ["FormStratum", "classify_form", "is_out_of_scope", "normalize_title"]

# Ordering prefixes used by the ORC uploaders, e.g. "3a. Nov 2018 Exam Paper 1",
# "1b. July 2018 Exam Paper 1 Memo". These are filing sequence markers and must
# be removed BEFORE paper-number detection, otherwise "1a." reads as "Paper 1".
_ORDER_PREFIX_RE = re.compile(r"^\s*\d{1,2}\s*[a-z]?\s*[.)]\s*")

# Filing prefixes/suffixes that carry no form information.
_NOISE_RE = re.compile(
    r"""(?xi)
    \b(copy\s+of|qp|mg|memo|memorandum|marking\s*guide?line?|
       final\s+version|draft\s*\d*|print(?:ed)?\s+version|version)\b
    """
)

_EXT_RE = re.compile(r"(?i)\.(pdf|docx?|odt|rtf|pages|gdoc|gsheet|zip)$")

# -- setter -----------------------------------------------------------------
_IEB_RE = re.compile(r"(?i)\bieb\s*-?\s*t?\b|iebt")

# -- sitting ----------------------------------------------------------------
_MID_RE = re.compile(r"(?i)\b(mid[\s-]*year|midyear|mid|jun|june|jul|july|aug|august)\b")
_FINAL_RE = re.compile(
    r"(?i)\b(year[\s-]*end|final|nov|november|dec|december|sept|sep|september|oct|october)\b"
)

# -- paper form -------------------------------------------------------------
_MCQ_RE = re.compile(r"(?i)\bmcq\b|multiple[\s-]*choice")
# The trailing (?![0-9]) rather than \b is deliberate: several ORC filenames run
# the paper number into the next word ("1a. Mid-year Paper 1pdf.pdf", a typo for
# "Paper 1 pdf"), where \b would fail. (?![0-9]) still rejects "Paper 10".
_P2_RE = re.compile(r"(?i)(?:\bpaper\s*2|\bp\s*-?\s*2|\bp2)(?![0-9])")
_P1_RE = re.compile(r"(?i)(?:\bpaper\s*1|\bp\s*-?\s*1|\bp1)(?![0-9])")
# AP Mathematics splits by content name rather than by an explicit paper number
# in several years: Calculus/Algebra is Paper 1, Statistics is Paper 2.
_AP_P2_RE = re.compile(r"(?i)\bstats\b|\bstatistics\b")
_AP_P1_RE = re.compile(r"(?i)\bcalculus\b|\balgebra\b")

# -- out of scope -----------------------------------------------------------
# The ORC Physics folder also holds Physical Sciences *Chemistry* material
# (e.g. "IeBT 2021 Chemistry P2", "11_Chemistry Test-1A_Bonding-ReactionRate").
# Chemistry is not one of the six in-scope subjects (SYSTEM_SPEC §6).
_CHEMISTRY_RE = re.compile(r"(?i)\bchemistry\b|\bchem\b")
_OTHER_SUBJECT_RE = re.compile(
    r"(?i)\b(geography|accounting|business\s*studies|economics|tourism|"
    r"engineering\s*graphics|computer\s*applications|dramatic\s*arts|"
    r"music|art|design|consumer\s*studies|life\s*orientation)\b"
)
_GRADE_RE = re.compile(r"(?i)\b(?:gr(?:ade)?|g)\s*-?\s*(\d{1,2})\b")


@dataclass(frozen=True)
class FormStratum:
    """A cell in the stratification used to sample the corpus.

    setter
        ``ieb_external`` — externally set IEB trial paper.
        ``school_internal`` — set by St Benedict's staff (examiner named on the
        paper, e.g. "EXAMINER: Mr Hilder").
        ``unknown``
    paper_form
        ``P1`` / ``P2`` / ``MCQ`` / ``single`` / ``unknown``. ``single`` means
        the subject sits one combined paper rather than a P1/P2 split.
    session
        ``mid_year`` / ``final`` / ``trial`` / ``unknown``.
    """

    subject: str
    setter: str
    paper_form: str
    session: str

    def key(self) -> str:
        return f"{self.subject}|{self.setter}|{self.paper_form}|{self.session}"

    def label(self) -> str:
        return f"{self.setter} {self.paper_form} ({self.session})"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def normalize_title(title: Optional[str]) -> str:
    """Lower-case, strip extension/filing noise. Used for memo pairing."""
    if not title:
        return ""
    text = _EXT_RE.sub("", title)
    text = _ORDER_PREFIX_RE.sub("", text)
    text = _NOISE_RE.sub(" ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def is_out_of_scope(subject: str, title: Optional[str]) -> Optional[str]:
    """Return a reason string if the record is not usable for ``subject``."""
    text = title or ""
    if subject == "physics" and _CHEMISTRY_RE.search(text):
        return "chemistry material held in the Physical Sciences folder; not in scope (SYSTEM_SPEC §6)"
    if subject != "physics" and _CHEMISTRY_RE.search(text):
        return "chemistry material; not in scope (SYSTEM_SPEC §6)"
    if _OTHER_SUBJECT_RE.search(text):
        return "different subject; not in scope (SYSTEM_SPEC §6)"
    match = _GRADE_RE.search(text)
    if match and match.group(1) not in ("11",):
        return f"title indicates Grade {match.group(1)}; scope is Grade 11"
    return None


def _detect_paper_form(subject: str, text: str) -> str:
    if _MCQ_RE.search(text):
        return "MCQ"
    if subject == "ap_mathematics":
        if _P2_RE.search(text) or _AP_P2_RE.search(text):
            return "P2"
        if _P1_RE.search(text) or _AP_P1_RE.search(text):
            return "P1"
        return "unknown"
    if _P2_RE.search(text):
        return "P2"
    if _P1_RE.search(text):
        return "P1"
    return "unknown"


def classify_form(subject: str, title: Optional[str]) -> FormStratum:
    """Assign a past paper to its assessment-form stratum."""
    raw = title or ""
    # Strip the filing prefix before any paper-number detection.
    text = _ORDER_PREFIX_RE.sub("", raw)
    # ORC filenames use underscores as separators ("2022_G11_Physics_Nov-Exam_QP").
    # "_" is a regex word character, so \bnov\b would NOT match inside
    # "Physics_Nov-Exam". Replace separators with spaces first so every \b
    # anchor behaves as intended.
    text = re.sub(r"[_]+", " ", text)

    setter = "ieb_external" if _IEB_RE.search(text) else "school_internal"

    if setter == "ieb_external":
        session = "trial"
    elif _MID_RE.search(text):
        session = "mid_year"
    elif _FINAL_RE.search(text):
        session = "final"
    else:
        session = "unknown"

    paper_form = _detect_paper_form(subject, text)

    # Subjects that sit one combined paper: an undetermined paper number is
    # recorded as "single" rather than "unknown", but only where the corpus
    # shows no P1/P2 split at all for that subject. Physics internal exams and
    # History single papers are the observed cases; callers may override.
    return FormStratum(
        subject=subject,
        setter=setter,
        paper_form=paper_form,
        session=session,
    )


def collapse_single_paper_subject(
    stratum: FormStratum, subject_has_split: bool
) -> FormStratum:
    """Reclassify ``unknown`` paper forms for subjects with no P1/P2 split.

    ``subject_has_split`` must be derived from the corpus (does ANY paper for
    this subject carry an explicit P1/P2 marker?), not assumed.
    """
    if stratum.paper_form == "unknown" and not subject_has_split:
        return FormStratum(
            subject=stratum.subject,
            setter=stratum.setter,
            paper_form="single",
            session=stratum.session,
        )
    return stratum
