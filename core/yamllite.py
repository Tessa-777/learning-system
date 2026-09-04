"""Minimal, dependency-free YAML support.

Why this module exists
----------------------
The repository declares ``PyYAML`` in ``requirements.txt``. In restricted
execution environments (no outbound TLS for ``pip``) that dependency cannot be
installed, which previously made ``core.config`` and ``core.runlog`` raise on
import and rendered the whole repository unrunnable.

This module provides a deliberately small subset of YAML so that the project
remains executable with only the Python standard library. It is a fallback:
when PyYAML *is* installed it is preferred, because it is the complete
implementation.

Supported on load
-----------------
* block mappings (``key: value``, ``key:`` + nested block)
* block sequences (``- value``, ``- key: value`` + sibling keys)
* empty flow collections (``{}``, ``[]``)
* single/double quoted scalars, ints, floats, ``true``/``false``/``null``
* whole-line comments, and unquoted trailing `` # comment``

NOT supported on load
---------------------
* multi-line folded (``>``) or literal (``|``) block scalars
* anchors, aliases, tags, multi-document streams
* complex flow collections spanning lines

The generated ``data/raw/<subject>/SOURCE_INVENTORY.yaml`` files DO contain
folded multi-line ``notes:`` scalars, so they must not be read with
``load()``. Use ``ingestion.acquisition.inventory.read_source_records()``
for those; it splits records textually and is unaffected by folded scalars.

Dumping supports the plain JSON-compatible value space (dict, list, str, int,
float, bool, None) and always emits block style.
"""

from __future__ import annotations

import re
from typing import Any, List, Tuple

__all__ = ["load", "loads", "dump", "dumps", "YAMLLiteError"]


class YAMLLiteError(ValueError):
    """Raised when input cannot be parsed by the supported subset."""


# --------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------

_INT_RE = re.compile(r"^[-+]?\d+$")
_FLOAT_RE = re.compile(r"^[-+]?(\d+\.\d*|\.\d+|\d+)([eE][-+]?\d+)?$")


def _strip_comment(line: str) -> str:
    """Remove a trailing comment from an unquoted scalar value.

    Only strips when a ``#`` is preceded by whitespace and the value does not
    begin with a quote, so URLs and quoted text containing ``#`` survive.
    """
    stripped = line.lstrip()
    if stripped.startswith("#"):
        return ""
    if stripped[:1] in ("'", '"'):
        return line
    idx = line.find(" #")
    if idx == -1:
        idx = line.find("\t#")
    return line[:idx] if idx != -1 else line


def _scalar(token: str) -> Any:
    token = token.strip()
    if token in ("", "null", "~", "Null", "NULL"):
        return None
    if token in ("true", "True", "TRUE", "yes", "Yes"):
        return True
    if token in ("false", "False", "FALSE", "no", "No"):
        return False
    if token == "{}":
        return {}
    if token == "[]":
        return []
    if len(token) >= 2 and token[0] == token[-1] and token[0] in ("'", '"'):
        inner = token[1:-1]
        if token[0] == '"':
            inner = inner.replace('\\"', '"').replace("\\n", "\n").replace("\\\\", "\\")
        else:
            inner = inner.replace("''", "'")
        return inner
    if _INT_RE.match(token):
        return int(token)
    if _FLOAT_RE.match(token) and any(c in token for c in ".eE"):
        return float(token)
    return token


def _needs_quotes(value: str) -> bool:
    if value == "":
        return True
    if value.strip() != value:
        return True
    lowered = value.lower()
    if lowered in ("null", "~", "true", "false", "yes", "no", "on", "off"):
        return True
    if _INT_RE.match(value) or (_FLOAT_RE.match(value) and any(c in value for c in ".eE")):
        return True
    if value[0] in "-?:,[]{}#&*!|>'\"%@`":
        return True
    if ": " in value or " #" in value or "\n" in value:
        return True
    return False


def _quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{escaped}"'


def _tokenize(text: str) -> List[Tuple[int, str]]:
    out: List[Tuple[int, str]] = []
    for raw in text.split("\n"):
        line = _strip_comment(raw.rstrip())
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        out.append((indent, line.strip()))
    return out


def loads(text: str) -> Any:
    """Parse the supported YAML subset into Python objects."""
    tokens = _tokenize(text)
    value, consumed = _parse_block(tokens, 0, tokens[0][0] if tokens else 0)
    if consumed != len(tokens):
        raise YAMLLiteError(
            f"unparsed input at token {consumed}: {tokens[consumed][1]!r}"
        )
    return value


def load(stream: Any) -> Any:
    """Parse from a file object or path-like/string path."""
    if hasattr(stream, "read"):
        return loads(stream.read())
    from pathlib import Path

    return loads(Path(stream).read_text(encoding="utf-8"))


def _parse_block(tokens: List[Tuple[int, str]], pos: int, indent: int) -> Tuple[Any, int]:
    if pos >= len(tokens):
        return None, pos
    if tokens[pos][1].startswith("- "):
        return _parse_sequence(tokens, pos, indent)
    if tokens[pos][1] == "-":
        return _parse_sequence(tokens, pos, indent)
    return _parse_mapping(tokens, pos, indent)


def _is_seq_token(content: str) -> bool:
    return content == "-" or content.startswith("- ")


def _parse_value(
    tokens: List[Tuple[int, str]], pos: int, key_indent: int
) -> Tuple[Any, int]:
    """Parse the value that follows an empty ``key:`` at ``key_indent``.

    A block sequence may sit at the same indentation as its key (the style
    PyYAML emits) or deeper, so both are accepted.
    """
    if pos >= len(tokens):
        return None, pos
    nxt_indent, nxt = tokens[pos]
    if _is_seq_token(nxt) and nxt_indent >= key_indent:
        return _parse_sequence(tokens, pos, nxt_indent)
    if nxt_indent > key_indent:
        return _parse_block(tokens, pos, nxt_indent)
    return None, pos


def _parse_sequence(tokens: List[Tuple[int, str]], pos: int, indent: int) -> Tuple[List[Any], int]:
    items: List[Any] = []
    while pos < len(tokens):
        cur_indent, content = tokens[pos]
        if cur_indent < indent or not _is_seq_token(content):
            break
        if cur_indent > indent:
            raise YAMLLiteError(f"unexpected indent in sequence at {content!r}")
        body = content[1:].strip() if content != "-" else ""
        pos += 1
        if not body:
            child, pos = _parse_block(tokens, pos, _next_indent(tokens, pos, cur_indent))
            items.append(child)
            continue
        if ":" in body and not body.startswith(('"', "'")):
            item, pos = _parse_inline_item(tokens, pos, cur_indent, body)
            items.append(item)
        else:
            items.append(_scalar(body))
    return items, pos


def _parse_inline_item(
    tokens: List[Tuple[int, str]], pos: int, dash_indent: int, body: str
) -> Tuple[dict, int]:
    """Parse ``- key: value`` plus any sibling keys belonging to the same item."""
    item: dict = {}
    # Sibling keys of a "- key:" item are indented to the column after "- ".
    key_indent = dash_indent + 2
    key, _, val = body.partition(":")
    if val.strip():
        item[key.strip()] = _scalar(val)
    else:
        child, pos = _parse_value(tokens, pos, key_indent)
        item[key.strip()] = child
    while pos < len(tokens):
        nxt_indent, nxt = tokens[pos]
        if nxt_indent < key_indent or _is_seq_token(nxt):
            break
        if nxt_indent > key_indent:
            raise YAMLLiteError(f"unexpected indent in sequence item at {nxt!r}")
        if ":" not in nxt:
            break
        k2, _, v2 = nxt.partition(":")
        pos += 1
        if v2.strip():
            item[k2.strip()] = _scalar(v2)
        else:
            child, pos = _parse_value(tokens, pos, key_indent)
            item[k2.strip()] = child
    return item, pos


def _next_indent(tokens: List[Tuple[int, str]], pos: int, current: int) -> int:
    if pos < len(tokens) and tokens[pos][0] > current:
        return tokens[pos][0]
    return current + 2


def _parse_mapping(tokens: List[Tuple[int, str]], pos: int, indent: int) -> Tuple[dict, int]:
    result: dict = {}
    while pos < len(tokens):
        cur_indent, content = tokens[pos]
        if cur_indent < indent or _is_seq_token(content):
            break
        if cur_indent > indent:
            raise YAMLLiteError(f"unexpected indent in mapping at {content!r}")
        if ":" not in content:
            raise YAMLLiteError(f"expected 'key: value' but got {content!r}")
        key, _, val = content.partition(":")
        key = key.strip().strip("'\"")
        pos += 1
        if val.strip():
            result[key] = _scalar(val)
        else:
            child, new_pos = _parse_value(tokens, pos, cur_indent)
            if new_pos == pos and child is None:
                result[key] = None
            else:
                result[key] = child
                pos = new_pos
    return result, pos


# --------------------------------------------------------------------------
# dumping
# --------------------------------------------------------------------------

def dumps(value: Any, indent: int = 0) -> str:
    lines: List[str] = []
    _emit(value, lines, indent, is_root=True)
    return "\n".join(lines) + "\n"


def dump(value: Any, stream: Any = None, indent: int = 0) -> str:
    text = dumps(value, indent)
    if stream is not None:
        if hasattr(stream, "write"):
            stream.write(text)
        else:
            from pathlib import Path

            Path(stream).write_text(text, encoding="utf-8")
    return text


def _emit_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return repr(value) if isinstance(value, float) else str(value)
    text = str(value)
    return _quote(text) if _needs_quotes(text) else text


def _emit(value: Any, lines: List[str], indent: int, is_root: bool = False) -> None:
    pad = " " * indent
    if isinstance(value, dict):
        if not value:
            lines.append(pad + "{}")
            return
        for key, item in value.items():
            if isinstance(item, dict) and item:
                lines.append(f"{pad}{key}:")
                _emit(item, lines, indent + 2)
            elif isinstance(item, list) and item:
                lines.append(f"{pad}{key}:")
                _emit_list(item, lines, indent)
            elif isinstance(item, dict):
                lines.append(f"{pad}{key}: {{}}")
            elif isinstance(item, list):
                lines.append(f"{pad}{key}: []")
            else:
                lines.append(f"{pad}{key}: {_emit_scalar(item)}")
    elif isinstance(value, list):
        _emit_list(value, lines, max(indent - 2, 0) if is_root else indent)
    else:
        lines.append(pad + _emit_scalar(value))


def _emit_list(items: List[Any], lines: List[str], indent: int) -> None:
    pad = " " * indent
    for item in items:
        if isinstance(item, dict) and item:
            keys = list(item.items())
            first_key, first_val = keys[0]
            if isinstance(first_val, (dict, list)) and first_val:
                lines.append(f"{pad}- {first_key}:")
                _emit(first_val, lines, indent + 4)
            else:
                lines.append(f"{pad}- {first_key}: {_emit_scalar(first_val)}")
            for key, val in keys[1:]:
                if isinstance(val, dict) and val:
                    lines.append(f"{pad}  {key}:")
                    _emit(val, lines, indent + 4)
                elif isinstance(val, list) and val:
                    lines.append(f"{pad}  {key}:")
                    _emit_list(val, lines, indent + 2)
                elif isinstance(val, dict):
                    lines.append(f"{pad}  {key}: {{}}")
                elif isinstance(val, list):
                    lines.append(f"{pad}  {key}: []")
                else:
                    lines.append(f"{pad}  {key}: {_emit_scalar(val)}")
        elif isinstance(item, list):
            lines.append(f"{pad}-")
            _emit_list(item, lines, indent + 2)
        else:
            lines.append(f"{pad}- {_emit_scalar(item)}")
