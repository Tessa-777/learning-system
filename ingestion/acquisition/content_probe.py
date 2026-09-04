"""Standard-library content probing for acquired documents.

Two obligations from ``IMPLEMENTATION_SPEC.md`` §4 (v1.1.0) cannot be met from
Phase 2 metadata:

1. **``document_type`` must be verified from content.** Phase 2 labels are
   demonstrably unreliable: the History record
   ``2009_July_exam_Gr_11.doc.docx`` is filed as ``past_paper`` but its content
   is the July 2009 memorandum.
2. **Diagram-bearing questions must be flagged** ``requires_visual_verification``
   when the document is held only as a transcription (fidelity Rung B), because
   transcription loses figures, graphs and geometric diagrams.

``PyPDF2``/``pdfminer``/``python-docx`` cannot be installed offline, so this
module uses only the standard library: ``zipfile`` for OOXML containers and
``zlib`` for PDF content streams. Extraction is best-effort and always reports a
confidence; when it cannot extract text it says so rather than guessing.
"""

from __future__ import annotations

import html
import re
import zipfile
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

__all__ = ["ContentProbe", "probe", "detect_format"]

_MAGIC = (
    (b"PK\x03\x04", "ooxml"),
    (b"%PDF", "pdf"),
    (b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1", "ole2"),
    (b"{\\rtf", "rtf"),
)

_MEMO_SIGNALS = (
    r"\bmemorandum\b", r"\bmarking guideline\b", r"\bmarking guide\b",
    r"\bmodel answer\b", r"\bmarking memorandum\b", r"\bsuggested answer\b",
    r"\baccept\b", r"\bdo not accept\b", r"\baward\b.*\bmark\b",
    r"\bmemo\b",
)
_PAPER_SIGNALS = (
    r"\bquestion paper\b", r"\binstructions to candidates\b",
    r"\banswer all\b", r"\banswer the following\b", r"\btotal:\s*\d+",
    r"\btime:\s*\d+\s*(hours|minutes)", r"\bfull marks\b",
    r"\blearner name\b", r"\bexaminer\b", r"\bmoderator\b",
    r"\bplease read the following instructions\b",
)
_VISUAL_SIGNALS = (
    r"\bdiagram\b", r"\bgraph\b", r"\bfigure\b", r"\bcartoon\b",
    r"\bcircuit\b", r"\btable below\b", r"\bshown below\b",
    r"\bgiven below\b", r"\brefer to source\b", r"\bsource booklet\b",
    r"\bmap\b", r"\bphotograph\b", r"\bimage\b", r"\boxive\b",
    r"\bscatterplot\b", r"\bbox and whisker\b", r"\bdata sheet\b",
    r"\bdraw\b", r"\bsketch\b",
)


@dataclass
class ContentProbe:
    path: str
    detected_format: str  # ooxml | pdf | ole2 | rtf | text | unknown
    text_extracted: bool
    extraction_confidence: str  # high | medium | low | none
    text_chars: int
    document_type: Optional[str]  # memorandum | past_paper | unknown
    document_type_confidence: str  # high | medium | low
    document_type_evidence: list
    visual_dependency: bool
    visual_signals: list
    error: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "path": self.path,
            "detected_format": self.detected_format,
            "text_extracted": self.text_extracted,
            "extraction_confidence": self.extraction_confidence,
            "text_chars": self.text_chars,
            "document_type": self.document_type,
            "document_type_confidence": self.document_type_confidence,
            "document_type_evidence": self.document_type_evidence,
            "visual_dependency": self.visual_dependency,
            "visual_signals": self.visual_signals,
            "error": self.error,
        }


def detect_format(path: Path) -> str:
    try:
        with path.open("rb") as handle:
            head = handle.read(8)
    except OSError:
        return "unknown"
    for magic, name in _MAGIC:
        if head.startswith(magic):
            return name
    if head.startswith(b"<!DOCTYPE") or head.startswith(b"<html"):
        return "html"
    try:
        head.decode("utf-8")
        return "text"
    except UnicodeDecodeError:
        return "unknown"


def _extract_ooxml(path: Path) -> Tuple[str, str]:
    """Extract text from a .docx/.xlsx/.pptx container."""
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        target = None
        for candidate in ("word/document.xml", "xl/sharedStrings.xml",
                          "ppt/presentation.xml"):
            if candidate in names:
                target = candidate
                break
        if target is None:
            xml_parts = [n for n in names if n.endswith(".xml")]
            if not xml_parts:
                return "", "none"
            target = xml_parts[0]
        raw = archive.read(target).decode("utf-8", errors="replace")
    # Paragraph and tab boundaries must survive or question numbering collapses.
    raw = re.sub(r"</w:p>", "\n", raw)
    raw = re.sub(r"<w:tab[^>]*/>", "\t", raw)
    raw = re.sub(r"<w:br[^>]*/>", "\n", raw)
    text = re.sub(r"<[^>]+>", "", raw)
    return html.unescape(text), "high"


def _extract_pdf(path: Path) -> Tuple[str, str]:
    """Best-effort PDF text extraction using only zlib.

    Handles the common case of FlateDecode content streams with ``Tj``/``TJ``
    text operators. Scanned or image-only PDFs yield no text, which is reported
    honestly as low confidence rather than being filled in.
    """
    data = path.read_bytes()
    chunks = []
    for match in re.finditer(rb"stream\r?\n", data):
        start = match.end()
        end = data.find(b"endstream", start)
        if end == -1:
            continue
        payload = data[start:end]
        decompressed = None
        try:
            decompressed = zlib.decompress(payload)
        except zlib.error:
            try:
                decompressed = zlib.decompressobj().decompress(payload)
            except zlib.error:
                decompressed = None
        if decompressed is None:
            continue
        chunks.append(decompressed)

    if not chunks:
        return "", "none"

    out = []
    for chunk in chunks:
        text = chunk.decode("latin-1", errors="replace")
        # (string) Tj  and  [(a) -250 (b)] TJ
        for shown in re.findall(r"\((?:\\.|[^\\()])*\)", text):
            inner = shown[1:-1]
            inner = re.sub(r"\\([()\\])", r"\1", inner)
            inner = inner.replace("\\n", "\n").replace("\\r", "\n")
            out.append(inner)
        for marker in re.finditer(r"\b(T\*|TD|Td|TJ|Tj|ET)\b", text):
            pass
        out.append("\n")
    joined = "".join(out)
    joined = re.sub(r"[ \t]{2,}", " ", joined)
    confidence = "medium" if len(joined.strip()) > 200 else "low"
    return joined, confidence


def _classify(text: str) -> Tuple[str, str, list]:
    lower = text.lower()
    memo_hits = [p for p in _MEMO_SIGNALS if re.search(p, lower)]
    paper_hits = [p for p in _PAPER_SIGNALS if re.search(p, lower)]
    memo_score = len(memo_hits)
    paper_score = len(paper_hits)

    if memo_score and not paper_score:
        return "memorandum", "high", memo_hits
    if paper_score and not memo_score:
        return "past_paper", "high", paper_hits
    if memo_score > paper_score:
        return "memorandum", "medium", memo_hits
    if paper_score > memo_score:
        return "past_paper", "medium", paper_hits
    if memo_score and paper_score:
        # Both signal sets present: marking guidance embedded in a question
        # paper, or a memo that reproduces the questions. Not decidable here.
        return "unknown", "low", memo_hits + paper_hits
    return "unknown", "low", []


def probe(path: Path | str) -> ContentProbe:
    """Probe one acquired file."""
    path = Path(path)
    fmt = detect_format(path)
    text = ""
    confidence = "none"
    error: Optional[str] = None
    try:
        if fmt == "ooxml":
            text, confidence = _extract_ooxml(path)
        elif fmt == "pdf":
            text, confidence = _extract_pdf(path)
        elif fmt in ("text", "html"):
            text = path.read_text(encoding="utf-8", errors="replace")
            confidence = "high"
        elif fmt == "ole2":
            error = (
                "legacy OLE2 .doc binary; text extraction requires a converter "
                "not available offline"
            )
        else:
            error = f"unrecognised file format (magic bytes did not match)"
    except (OSError, zipfile.BadZipFile, ValueError) as exc:
        error = f"extraction failed: {exc}"
        confidence = "none"

    doc_type, doc_confidence, evidence = (
        _classify(text) if text.strip() else ("unknown", "low", [])
    )
    lower = text.lower()
    signals = sorted({
        match.group(0).lower()
        for pattern in _VISUAL_SIGNALS
        for match in [re.search(pattern, lower)]
        if match
    })
    return ContentProbe(
        path=str(path),
        detected_format=fmt,
        text_extracted=bool(text.strip()),
        extraction_confidence=confidence if text.strip() else "none",
        text_chars=len(text),
        document_type=doc_type if text.strip() else None,
        document_type_confidence=doc_confidence if text.strip() else "low",
        document_type_evidence=evidence[:8],
        visual_dependency=bool(signals) and bool(text.strip()),
        visual_signals=signals[:12],
        error=error,
    )
