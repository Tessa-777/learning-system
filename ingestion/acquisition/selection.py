"""Form-stratified saturation sampling of the ORC corpus.

Rationale
---------
The knowledge bank's primary objects are question families and Understanding
Models, which SYSTEM_SPEC §9 defines as describing "the underlying competence
being assessed" — explicitly *not* topic content. IMPLEMENTATION_SPEC §9
further requires "Do not create one family for every individual question." The
taxonomy is therefore a compression, and acquiring all 821 discovered records to
feed a compression step is a mismatch between effort and objective.

Sampling is stratified on **assessment form** (see ``forms.py``) because form —
not topic, not year — is what determines which question families a paper can
contain.

Allocation is two-pass:

1. **Coverage pass** — one exemplar per stratum, so every distinct assessment
   form in the corpus is represented at least once. Where strata outnumber the
   per-subject budget, strata are ranked by candidate-pool size (the forms the
   school actually uses most) and then by recency.
2. **Depth pass** — remaining budget is spent adding a second, older exemplar to
   the strata with the largest pools. Two exemplars is the minimum that can
   distinguish "this family recurs" from "this was a one-off"; one cannot
   establish a family at all.

Every selected paper is paired with its memorandum or marking guide. This is not
optional: AGENTS.md rule 8 requires the memo to be the primary evidence for what
is assessed, and Phase 6 cannot align questions to marking evidence that was
never acquired.

Stopping rule
-------------
The sample size is a budget, not a claim of sufficiency. Sufficiency is decided
empirically at Phase 8/13 by the saturation test in ``CORPUS_SUFFICIENCY_POLICY.md``:
if the last papers added produced no new question family, the corpus is
saturated. If they did, targeted papers are added to the affected strata only —
never by reverting to blanket acquisition.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .forms import (
    FormStratum,
    classify_form,
    collapse_single_paper_subject,
    is_out_of_scope,
    normalize_title,
)
from .inventory import drive_file_id

__all__ = [
    "PaperSelection",
    "MemoPairing",
    "SubjectSelection",
    "build_selection",
]

MEMO_DOC_TYPES = ("memorandum", "marking_guide")

# Documents that a selected question paper cannot be answered without. History
# source-based questions reference a Source Booklet; Physics and Mathematics
# papers instruct the candidate to detach a Data Sheet / Information Sheet;
# IEB Physics trials ship a Diagram Booklet and an Answer Sheet. These are
# filed under `reference` / `other` in the Phase 2 inventory, so a sampler that
# only looks at `past_paper` records silently drops them.
COMPANION_RE = re.compile(
    r"(?i)(source\s+booklet|data\s+sheet|diagram\s+booklet|answer\s+sheet|"
    r"information\s+(?:sheet|booklet)|booklet|_ds\b|_as\b|_ib\b|\(ds\)|\(as\)|\(ib\))"
)

# Authoritative curriculum anchors. Phase 7 requires the topic hierarchy to come
# from authoritative source material; these are the only such documents present
# in the ORC inventory, and most subjects have none (see selection notes).
ANCHOR_RE = re.compile(
    r"(?i)(subject\s+assessment\s+guide|\bsag\b|syllabus|curriculum|"
    r"examination?\s+guideline|exam\s+requirements|assessment\s+guideline|"
    r"content\s*(?:&|and)\s*skills|prescribed)"
)

COMPANION_DOC_TYPES = ("reference", "other", "curriculum")

_ORDER_PREFIX_RE = re.compile(r"^\s*(\d{1,2})\s*([a-z])?\s*[.)]\s*")
_QP_MG_RE = re.compile(r"(?i)_QP\b")
_YEAR_RE = re.compile(r"(19|20)\d{2}")

DEFAULT_PAPERS_PER_SUBJECT = 5
DEFAULT_MIN_YEAR_GAP = 3
DEFAULT_SIMILARITY_THRESHOLD = 0.55


@dataclass
class MemoPairing:
    source_id: Optional[str]
    title: Optional[str]
    source_url: Optional[str]
    document_type: Optional[str]
    method: str  # order_prefix | qp_mg_suffix | title_similarity | manual | none
    confidence: str  # high | medium | low | none
    note: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_id": self.source_id,
            "title": self.title,
            "source_url": self.source_url,
            "document_type": self.document_type,
            "pair_method": self.method,
            "pair_confidence": self.confidence,
            "note": self.note,
        }


@dataclass
class PaperSelection:
    source_id: Optional[str]
    title: Optional[str]
    year: Optional[int]
    source_url: Optional[str]
    drive_file_id: Optional[str]
    stratum: FormStratum
    selection_reason: str
    exemplar_role: str  # primary (coverage pass) | secondary (depth pass)
    memo: Optional[MemoPairing] = None
    companions: List[Dict[str, Any]] = field(default_factory=list)
    expected_path: str = ""
    flags: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_id": self.source_id,
            "title": self.title,
            "year": self.year,
            "source_url": self.source_url,
            "drive_file_id": self.drive_file_id,
            "stratum": {
                "setter": self.stratum.setter,
                "paper_form": self.stratum.paper_form,
                "session": self.stratum.session,
            },
            "stratum_key": self.stratum.key(),
            "exemplar_role": self.exemplar_role,
            "selection_reason": self.selection_reason,
            "memo": self.memo.to_dict() if self.memo else None,
            "companions": list(self.companions),
            "expected_path": self.expected_path,
            "flags": list(self.flags),
        }


@dataclass
class SubjectSelection:
    subject: str
    papers: List[PaperSelection]
    strata_found: List[str]
    strata_sampled: List[str]
    pool_size: int
    excluded: List[Dict[str, Any]]
    curriculum_anchors: List[Dict[str, Any]]
    notes: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "subject": self.subject,
            "candidate_past_papers": self.pool_size,
            "strata_found": len(self.strata_found),
            "strata_sampled": len(self.strata_sampled),
            "papers_selected": len(self.papers),
            "papers": [p.to_dict() for p in self.papers],
            "curriculum_anchors": self.curriculum_anchors,
            "excluded": self.excluded,
            "notes": self.notes,
        }


# --------------------------------------------------------------------------
# memo pairing
# --------------------------------------------------------------------------

def _order_prefix(title: Optional[str]) -> Optional[Tuple[str, str]]:
    if not title:
        return None
    match = _ORDER_PREFIX_RE.match(title)
    if not match:
        return None
    return match.group(1), (match.group(2) or "").lower()


_SUBJECT_NOISE = {
    "biology": {"biology", "bio", "life", "sciences", "ps", "ps11"},
    "physics": {"physics", "physical", "sciences", "ps", "ps11"},
    "history": {"history", "hist"},
    "english": {"english", "eng", "hl", "home", "language"},
    "ap_mathematics": {"ap", "fs", "adv", "advanced", "maths", "mathematics", "math", "sbc"},
    "mathematics": {"maths", "mathematics", "math", "fs"},
}
_GRADE_NOISE = {"gr", "grade", "gr11", "g11", "g", "11", "s11", "veritas", "in", "caritate"}
_SESSION_ALIASES = {
    "jun": "june", "jul": "july", "nov": "november", "dec": "december",
    "sept": "september", "sep": "september", "oct": "october", "aug": "august",
    "midyear": "mid", "mid year": "mid",
}


def _canonical_tokens(text: Optional[str], subject: str) -> set:
    """Tokenise a title into discriminative terms.

    "Paper 2" and "P2" must not be treated as different forms, and grade /
    subject tokens must not dilute similarity, since they are constant within a
    subject inventory.
    """
    if not text:
        return set()
    cleaned = normalize_title(text)
    # Canonicalise paper markers before splitting: "paper 2" / "p 2" -> "p2".
    cleaned = re.sub(r"\bpaper\s+(\d)\b", r"p\1", cleaned)
    cleaned = re.sub(r"\bp\s+(\d)\b", r"p\1", cleaned)
    cleaned = re.sub(r"\b(\d)\s+paper\b", r"p\1", cleaned)
    tokens = set()
    noise = _SUBJECT_NOISE.get(subject, set()) | _GRADE_NOISE
    for token in cleaned.split():
        if _YEAR_RE.fullmatch(token) or len(token) < 2:
            continue
        token = _SESSION_ALIASES.get(token, token)
        if token in noise:
            continue
        tokens.add(token)
    return tokens


def _token_set(text: str, subject: str = "") -> set:
    return _canonical_tokens(text, subject)


def _jaccard(left: set, right: set) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def _stratum_matches(paper_stratum: FormStratum, memo_stratum: FormStratum) -> bool:
    """True when a memo's form agrees with the paper's on every known dimension.

    Dimensions the classifier could not determine (``unknown``) are not
    required to agree, so an ambiguously titled paper can still match its memo.
    """
    if paper_stratum.setter != memo_stratum.setter:
        return False
    for dimension in ("paper_form", "session"):
        paper_value = getattr(paper_stratum, dimension)
        memo_value = getattr(memo_stratum, dimension)
        if paper_value == "unknown" or memo_value == "unknown":
            continue
        if paper_value != memo_value:
            return False
    return True


def pair_memo(
    paper: Dict[str, Any],
    subject: str,
    memo_pool: Sequence[Dict[str, Any]],
    threshold: float = DEFAULT_SIMILARITY_THRESHOLD,
) -> MemoPairing:
    """Find the memorandum / marking guide belonging to ``paper``.

    Strategies are tried in order of reliability. A pairing is only accepted
    when the assessment form agrees, so a Paper 1 memo is never attached to a
    Paper 2 question paper.

    ``stratum_year_unique`` is the strongest signal: within one subject, one
    year and one assessment form the school normally sits a single assessment,
    so exactly one memorandum can belong to it. That inference is structural and
    does not depend on how the file happens to have been named.
    """
    paper_stratum = classify_form(subject, paper.get("title"))
    same_year = [
        m for m in memo_pool if str(m.get("year")) == str(paper.get("year"))
    ]
    paper_form = paper_stratum.paper_form

    def form_compatible(candidate: Dict[str, Any]) -> bool:
        memo_form = classify_form(subject, candidate.get("title")).paper_form
        if paper_form == "unknown" or memo_form == "unknown":
            return True
        return paper_form == memo_form

    # 0. Same year + same assessment form, and only one such memorandum.
    if same_year:
        structural = [
            m
            for m in same_year
            if _stratum_matches(paper_stratum, classify_form(subject, m.get("title")))
        ]
        if len(structural) == 1:
            return MemoPairing(
                source_id=structural[0].get("source_id"),
                title=structural[0].get("title"),
                source_url=structural[0].get("source_url"),
                document_type=structural[0].get("document_type"),
                method="stratum_year_unique",
                confidence="high",
                note=(
                    f"only memorandum in {paper.get('year')} matching form "
                    f"{paper_stratum.label()}"
                ),
            )

    candidates = same_year or list(memo_pool)

    # 1. Filing-prefix convention: "3a. ... Paper 1.pdf" <-> "3b. ... Paper 1 Memo.pdf"
    prefix = _order_prefix(paper.get("title"))
    if prefix:
        number, letter = prefix
        matches = []
        for candidate in candidates:
            cand_prefix = _order_prefix(candidate.get("title"))
            if cand_prefix and cand_prefix[0] == number and cand_prefix[1] != letter:
                if form_compatible(candidate):
                    matches.append(candidate)
        if len(matches) == 1:
            return MemoPairing(
                source_id=matches[0].get("source_id"),
                title=matches[0].get("title"),
                source_url=matches[0].get("source_url"),
                document_type=matches[0].get("document_type"),
                method="order_prefix",
                confidence="high",
                note=f"matched filing prefix {number}{letter or ''} -> {number}{_order_prefix(matches[0].get('title'))[1]}",
            )
        if len(matches) > 1:
            return MemoPairing(
                source_id=None,
                title=None,
                source_url=None,
                document_type=None,
                method="order_prefix",
                confidence="low",
                note=f"prefix {number} matched {len(matches)} memo candidates; needs human pairing",
            )

    # 2. Suffix convention: "..._QP.pdf" <-> "..._MG.pdf"
    title = paper.get("title") or ""
    if _QP_MG_RE.search(title):
        target = _QP_MG_RE.sub("_MG", title)
        target_norm = normalize_title(target)
        for candidate in candidates:
            if normalize_title(candidate.get("title")) == target_norm:
                if form_compatible(candidate):
                    return MemoPairing(
                        source_id=candidate.get("source_id"),
                        title=candidate.get("title"),
                        source_url=candidate.get("source_url"),
                        document_type=candidate.get("document_type"),
                        method="qp_mg_suffix",
                        confidence="high",
                    )

    # 3. Title similarity on normalised tokens.
    paper_tokens = _canonical_tokens(title, subject)
    scored = []
    for candidate in candidates:
        if not form_compatible(candidate):
            continue
        score = _jaccard(paper_tokens, _canonical_tokens(candidate.get("title"), subject))
        scored.append((score, candidate))
    scored.sort(key=lambda pair: (-pair[0], str(pair[1].get("title"))))
    if scored and scored[0][0] >= threshold:
        score, best = scored[0]
        runner_up = scored[1][0] if len(scored) > 1 else 0.0
        confidence = "medium" if score - runner_up >= 0.15 else "low"
        return MemoPairing(
            source_id=best.get("source_id"),
            title=best.get("title"),
            source_url=best.get("source_url"),
            document_type=best.get("document_type"),
            method="title_similarity",
            confidence=confidence,
            note=f"token Jaccard {score:.2f} (runner-up {runner_up:.2f})",
        )

    return MemoPairing(
        source_id=None,
        title=None,
        source_url=None,
        document_type=None,
        method="none",
        confidence="none",
        note="no memorandum or marking guide could be paired from metadata; requires human pairing",
    )


# --------------------------------------------------------------------------
# stratified sampling
# --------------------------------------------------------------------------

def _as_year(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _year_of(record: Dict[str, Any]) -> int:
    return _as_year(record.get("year"))


def _slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("_")[:80]


def _find_companions(
    paper: Dict[str, Any],
    stratum: FormStratum,
    subject: str,
    records: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Find data sheets / source booklets / diagram booklets for this paper.

    Matched on the same year and a compatible assessment form, so a 2023 IEB
    Trial P1 Diagram Booklet is not attached to a 2025 internal final exam.
    """
    year = paper.get("year")
    paper_tokens = _canonical_tokens(paper.get("title"), subject)
    found: List[Dict[str, Any]] = []
    for record in records:
        if record.get("document_type") not in COMPANION_DOC_TYPES:
            continue
        title = record.get("title") or ""
        if not COMPANION_RE.search(title):
            continue
        if is_out_of_scope(subject, title):
            continue
        candidate_form = classify_form(subject, title)
        if not _stratum_matches(stratum, candidate_form):
            continue
        record_year = record.get("year")
        # A companion must belong to the same sitting; an undated global
        # document (e.g. a standing Data Sheet) is admitted only on strong
        # title overlap.
        if str(record_year) != str(year):
            overlap = _jaccard(paper_tokens, _canonical_tokens(title, subject))
            if record_year is not None or overlap < 0.5:
                continue
        found.append(
            {
                "source_id": record.get("source_id"),
                "title": title,
                "year": record_year,
                "document_type": record.get("document_type"),
                "source_url": record.get("source_url"),
                "drive_file_id": drive_file_id(record.get("source_url")),
                "role": "companion_document",
                "reason": (
                    "the question paper cannot be answered without it "
                    "(source booklet / data sheet / diagram booklet / answer sheet)"
                ),
            }
        )
    return found


def _find_curriculum_anchors(
    subject: str, records: Sequence[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Return authoritative curriculum documents present in the inventory."""
    anchors: List[Dict[str, Any]] = []
    for record in records:
        title = record.get("title") or ""
        is_anchor_type = record.get("document_type") == "curriculum"
        if not (is_anchor_type or ANCHOR_RE.search(title)):
            continue
        if is_out_of_scope(subject, title):
            continue
        anchors.append(
            {
                "source_id": record.get("source_id"),
                "title": title,
                "year": record.get("year"),
                "document_type": record.get("document_type"),
                "source_url": record.get("source_url"),
                "drive_file_id": drive_file_id(record.get("source_url")),
                "role": "curriculum_anchor",
                "reason": (
                    "authoritative curriculum/assessment-guideline document "
                    "required by Phase 7 (curriculum hierarchy must come from "
                    "authoritative source material)"
                ),
            }
        )
    return anchors


def build_subject_selection(
    subject: str,
    records: Sequence[Dict[str, Any]],
    papers_per_subject: int = DEFAULT_PAPERS_PER_SUBJECT,
    min_year_gap: int = DEFAULT_MIN_YEAR_GAP,
    memo_threshold: float = DEFAULT_SIMILARITY_THRESHOLD,
) -> SubjectSelection:
    """Select the saturation sample for one subject."""
    notes: List[str] = []
    excluded: List[Dict[str, Any]] = []

    papers = [r for r in records if r.get("document_type") == "past_paper"]
    # The memo pool must be scope-filtered too: the ORC English folder holds
    # Grade 12 material (e.g. "MEMO Contextual Test Film Grade 12"), and without
    # this filter a Grade 12 memorandum can be structurally matched to a
    # Grade 11 question paper.
    memos = [
        r
        for r in records
        if r.get("document_type") in MEMO_DOC_TYPES
        and not is_out_of_scope(subject, r.get("title"))
    ]

    usable: List[Dict[str, Any]] = []
    for record in papers:
        reason = is_out_of_scope(subject, record.get("title"))
        if reason:
            excluded.append(
                {
                    "source_id": record.get("source_id"),
                    "title": record.get("title"),
                    "reason": reason,
                }
            )
            continue
        usable.append(record)

    if excluded:
        notes.append(
            f"{len(excluded)} past-paper record(s) excluded as out of scope "
            "(see `excluded`); these remain in the Phase 2 inventory for provenance."
        )

    # Pre-compute memo pairing for every candidate, because memo availability is
    # a selection criterion, not just an output: AGENTS.md rule 8 makes the memo
    # the primary evidence of what is assessed, and a paper with no memo cannot
    # support Phase 6 alignment or a defensible Understanding Model.
    pairings: Dict[int, MemoPairing] = {
        id(r): pair_memo(r, subject, memos, memo_threshold) for r in usable
    }

    def has_memo(record: Dict[str, Any]) -> bool:
        pairing = pairings[id(record)]
        return bool(pairing and pairing.source_id)

    # Does this subject split into P1/P2 at all? Derived from the corpus, and
    # computed per setter: Physics sits IEB Trials as P1/P2 but its own internal
    # exams as one combined 200-mark paper, so a subject-wide test would wrongly
    # leave every internal Physics exam as "unknown".
    base_strata = {id(r): classify_form(subject, r.get("title")) for r in usable}
    split_by_setter: Dict[str, bool] = {}
    for record in usable:
        stratum = base_strata[id(record)]
        if stratum.paper_form in ("P1", "P2", "MCQ"):
            split_by_setter[stratum.setter] = True
        split_by_setter.setdefault(stratum.setter, False)

    strata: Dict[str, List[Dict[str, Any]]] = {}
    for record in usable:
        base = base_strata[id(record)]
        stratum = collapse_single_paper_subject(
            base, split_by_setter.get(base.setter, False)
        )
        strata.setdefault(stratum.key(), []).append(record)
        record["_stratum"] = stratum

    for key in strata:
        strata[key].sort(key=lambda r: (-_year_of(r), str(r.get("title"))))

    def pick_exemplar(pool: List[Dict[str, Any]], mode: str) -> Dict[str, Any]:
        """Prefer a memo-backed candidate; within that prefer recency or age."""
        ordered = pool if mode == "recent" else list(reversed(pool))
        with_memo = [r for r in ordered if has_memo(r)]
        return with_memo[0] if with_memo else ordered[0]

    def stratum_rank_key(key_pool):
        key, pool = key_pool
        return (-int(any(has_memo(r) for r in pool)), -len(pool), key)

    # Group strata by (setter, paper_form). The paper form - not the sitting -
    # is what determines which question families can appear, so form diversity
    # must be secured before session diversity.
    pairs: Dict[Tuple[str, str], List[Tuple[str, List[Dict[str, Any]]]]] = {}
    for key, pool in strata.items():
        _, setter, form, session = key.split("|")
        pairs.setdefault((setter, form), []).append((key, pool))

    # A paper_form occurring in exactly one pair (e.g. Physics MCQ) contributes
    # question families found nowhere else in the corpus. Pool size measures how
    # often the school sits a form, NOT how much new taxonomy it yields, so a
    # unique form outranks a merely frequent one.
    form_pair_counts: Dict[str, int] = {}
    for setter, form in pairs:
        form_pair_counts[form] = form_pair_counts.get(form, 0) + 1
    ranked_pairs = sorted(
        pairs.items(),
        key=lambda kv: (-int(form_pair_counts[kv[0][1]] == 1),
                        -sum(len(pool) for _, pool in kv[1]),
                        kv[0]),
    )

    # Primary stratum per pair (best memo/pool), then the pair's other sittings.
    pair_primary: List[Tuple[str, List[Dict[str, Any]]]] = []
    pair_secondary: List[Tuple[str, List[Dict[str, Any]]]] = []
    for _, group in ranked_pairs:
        group.sort(key=stratum_rank_key)
        pair_primary.append(group[0])
        pair_secondary.extend(group[1:])

    ranked = pair_primary + pair_secondary + []
    strata_found = [k for k, _ in sorted(strata.items(), key=stratum_rank_key)]

    budget = papers_per_subject
    chosen: List[Tuple[Dict[str, Any], str, str]] = []

    # Pass 1 - coverage: one exemplar per (setter, paper_form) pair first, so
    # every distinct question-bearing form is represented; then per sitting.
    for phase_label, group in (("form", pair_primary), ("sitting", pair_secondary)):
        for key, pool in group:
            if len(chosen) >= budget:
                break
            exemplar = pick_exemplar(pool, "recent")
            chosen.append(
                (
                    exemplar,
                    "primary",
                    f"coverage pass ({phase_label} diversity): exemplar of stratum "
                    f"{key} ({len(pool)} candidate papers in this form)"
                    + ("; chosen because a memorandum exists for it"
                       if has_memo(exemplar) else " [no memorandum paired]"),
                )
            )
    unsampled = [
        (key, pool)
        for key, pool in ranked
        if not any(r["_stratum"].key() == key for r, _, _ in chosen)
    ]
    for key, pool in unsampled:
        notes.append(
            f"budget of {budget} papers exhausted before stratum {key} "
            f"({len(pool)} candidates) could be sampled; stratum left "
            "unrepresented and flagged for review."
        )

    # Pass 2 - depth: add an older exemplar to the largest strata.
    for key, pool in ranked:
        if len(chosen) >= budget:
            break
        if len(pool) < 2:
            continue
        already = {id(r) for r, _, _ in chosen if r["_stratum"].key() == key}
        remaining = [r for r in pool if id(r) not in already]
        newest_year = max(_year_of(r) for r in pool)
        older = [r for r in remaining if r.get("year") and newest_year - _year_of(r) >= min_year_gap]
        if not older:
            older = remaining
        if not older:
            continue
        pick = pick_exemplar(older, "oldest")
        chosen.append(
            (
                pick,
                "secondary",
                f"depth pass: second exemplar of stratum {key}, {_year_of(pick)} "
                f"vs newest {_year_of(pool[0])}; two exemplars are the minimum "
                "needed to show a question family recurs rather than being a one-off",
            )
        )

    selections: List[PaperSelection] = []
    seen_ids = set()
    for record, role, reason in chosen:
        sid = record.get("source_id")
        if sid in seen_ids:
            continue
        seen_ids.add(sid)
        stratum = record["_stratum"]
        memo = pairings[id(record)]
        companions = _find_companions(record, stratum, subject, records)
        flags: List[str] = []
        if not memo.source_id:
            flags.append("no_memorandum_in_corpus")
        elif memo.confidence in ("low",):
            flags.append("memo_pairing_needs_review")
        if "unknown" in (stratum.paper_form, stratum.session):
            flags.append("stratum_partially_unknown")
        fid = drive_file_id(record.get("source_url"))
        safe_title = _slug(record.get("title") or sid or "untitled")
        selections.append(
            PaperSelection(
                source_id=sid,
                title=record.get("title"),
                year=record.get("year"),
                source_url=record.get("source_url"),
                drive_file_id=fid,
                stratum=stratum,
                selection_reason=reason,
                exemplar_role=role,
                memo=memo,
                companions=companions,
                expected_path=f"data/raw/{subject}/papers/{safe_title}",
                flags=flags,
            )
        )

    selections.sort(key=lambda s: (s.stratum.key(), -_as_year(s.year)))

    anchors = _find_curriculum_anchors(subject, records)
    if not anchors:
        notes.append(
            "NO authoritative curriculum document (SAG / syllabus / examination "
            "guideline) exists for this subject in the ORC inventory. Phase 7 "
            "must therefore derive the topic hierarchy from Tier-1 evidence "
            "inside the papers themselves - several carry their own mark-"
            "allocation tables naming the topic of every question - and must "
            "mark that hierarchy `derived`, not `curriculum`."
        )

    unpaired = [s for s in selections if not s.memo.source_id]
    if unpaired:
        notes.append(
            f"{len(unpaired)} of {len(selections)} selected papers have no "
            "memorandum or marking guide in the ORC inventory. Phase 6 "
            "(question-to-memo alignment) cannot be completed for these; they "
            "remain unresolved rather than being inferred (AGENTS.md rule 4)."
        )

    for record in usable:
        record.pop("_stratum", None)

    return SubjectSelection(
        subject=subject,
        papers=selections,
        strata_found=strata_found,
        strata_sampled=sorted({s.stratum.key() for s in selections}),
        pool_size=len(usable),
        excluded=excluded,
        curriculum_anchors=anchors,
        notes=notes,
    )


def build_selection(
    inventories: Dict[str, Sequence[Dict[str, Any]]],
    papers_per_subject: int = DEFAULT_PAPERS_PER_SUBJECT,
    min_year_gap: int = DEFAULT_MIN_YEAR_GAP,
) -> Dict[str, SubjectSelection]:
    """Build the saturation sample for every subject."""
    return {
        subject: build_subject_selection(
            subject, records, papers_per_subject, min_year_gap
        )
        for subject, records in inventories.items()
    }
