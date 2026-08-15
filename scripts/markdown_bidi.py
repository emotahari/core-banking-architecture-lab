#!/usr/bin/env python3
"""Format and validate Persian Markdown for predictable bidirectional rendering."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MARKER = "<!-- bidi: rtl; code: ltr -->"
RTL_OPEN = '<div dir="rtl" align="right">'
LTR_OPEN = '<div dir="ltr" align="left">'
DIV_CLOSE = "</div>"
BDI_OPEN = '<bdi dir="ltr">'
BDI_CLOSE = "</bdi>"
PREFIX = f"{MARKER}\n{RTL_OPEN}\n\n"
SUFFIX = f"\n{DIV_CLOSE}\n"
TO_LTR = f"\n{DIV_CLOSE}\n\n{LTR_OPEN}\n\n"
TO_RTL = f"\n{DIV_CLOSE}\n\n{RTL_OPEN}\n\n"

PERSIAN_RE = re.compile(r"[\u0600-\u06ff]")
UNSAFE_BIDI_RE = re.compile(r"[\u061c\u200e\u200f\u202a-\u202e\u2066-\u2069]")
FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*?)(?:\n)?$")
INLINE_CODE_RE = re.compile(r"(?<!`)`[^`\n]+`(?!`)")
BDI_RE = re.compile(r'(<bdi dir="ltr">.*?</bdi>)')
MARKDOWN_LIST_PREFIX_RE = re.compile(r"^(\s*(?:>\s*)*(?:\d+[.)]|[-+*])\s+)")
ORDERED_PREFIX_IN_BDI_RE = re.compile(
    r'^(\s*)<bdi dir="ltr">(\d+[.)])\s+([^<]*?)</bdi>(.*)$'
)
ASCII_RUN_RE = re.compile(
    r"(?<![A-Za-z0-9])"
    r"([A-Za-z0-9][A-Za-z0-9._/+:#-]*"
    r"(?:[ \t]+[A-Za-z0-9][A-Za-z0-9._/+:#-]*)*)"
    r"(?![A-Za-z0-9])"
)
PROTECTED_RE = re.compile(
    r"(<bdi dir=\"ltr\">.*?</bdi>"
    r"|<!--.*?-->"
    r"|</?[A-Za-z][^>]*>"
    r"|\]\([^\n)]*\)"
    r"|https?://[^\s<>]+"
    r"|&[A-Za-z0-9#]+;)"
)


class BidiFormatError(ValueError):
    pass


def contains_persian(text: str) -> bool:
    return bool(PERSIAN_RE.search(text))


def fence_token(line: str) -> tuple[str, int, str] | None:
    match = FENCE_RE.match(line)
    if not match:
        return None
    delimiter = match.group(2)
    return delimiter[0], len(delimiter), match.group(3).strip()


def isolate_inline_code(text: str) -> str:
    parts = BDI_RE.split(text)
    for index in range(0, len(parts), 2):
        parts[index] = INLINE_CODE_RE.sub(
            lambda match: f"{BDI_OPEN}{match.group(0)}{BDI_CLOSE}", parts[index]
        )
    return "".join(parts)


def isolate_ltr_terms(text: str) -> str:
    prefix_match = MARKDOWN_LIST_PREFIX_RE.match(text)
    prefix = prefix_match.group(1) if prefix_match else ""
    body = text[len(prefix) :]
    parts = PROTECTED_RE.split(body)

    def wrap(match: re.Match[str]) -> str:
        value = match.group(1)
        letters = sum(character.isascii() and character.isalpha() for character in value)
        has_digit = any(character.isdigit() for character in value)
        if letters < 2 and not (letters == 1 and has_digit):
            return value
        return f"{BDI_OPEN}{value}{BDI_CLOSE}"

    for index in range(0, len(parts), 2):
        parts[index] = ASCII_RUN_RE.sub(wrap, parts[index])
    return prefix + "".join(parts)


def repair_formatted_markdown(text: str) -> str:
    output: list[str] = []
    fence_char: str | None = None
    fence_length = 0

    for line in text.splitlines(keepends=True):
        token = fence_token(line)
        if fence_char is None and token:
            fence_char, fence_length, _ = token
            output.append(line)
            continue
        if fence_char is not None:
            output.append(line)
            if token and token[0] == fence_char and token[1] >= fence_length and not token[2]:
                fence_char = None
                fence_length = 0
            continue

        newline = "\n" if line.endswith("\n") else ""
        content = line[:-1] if newline else line
        match = ORDERED_PREFIX_IN_BDI_RE.match(content)
        if match:
            indent, marker, value, remainder = match.groups()
            content = f"{indent}{marker} {BDI_OPEN}{value}{BDI_CLOSE}{remainder}"
        output.append(content + newline)

    return "".join(output)


def format_markdown(text: str) -> str:
    if text.startswith(MARKER):
        return repair_formatted_markdown(text)
    if not contains_persian(text):
        return text
    if UNSAFE_BIDI_RE.search(text):
        raise BidiFormatError("explicit Unicode BiDi control found")
    if text.startswith("---\n"):
        raise BidiFormatError("YAML front matter needs an explicit formatting strategy")

    output: list[str] = []
    fence_char: str | None = None
    fence_length = 0

    for line in text.splitlines(keepends=True):
        token = fence_token(line)
        if fence_char is None and token:
            fence_char, fence_length, _ = token
            output.append(TO_LTR)
            output.append(line)
            continue

        if fence_char is not None:
            output.append(line)
            if token and token[0] == fence_char and token[1] >= fence_length and not token[2]:
                fence_char = None
                fence_length = 0
                output.append(TO_RTL)
            continue

        output.append(isolate_ltr_terms(isolate_inline_code(line)))

    if fence_char is not None:
        raise BidiFormatError("unclosed fenced code block")

    return f"{PREFIX}{''.join(output)}{SUFFIX}"


def validate_markdown(text: str) -> list[str]:
    errors: list[str] = []
    if UNSAFE_BIDI_RE.search(text):
        errors.append("contains an invisible Unicode BiDi control")
    if not text.startswith(PREFIX):
        errors.append("missing canonical RTL document wrapper")
        return errors
    if not text.endswith(SUFFIX):
        errors.append("missing canonical closing wrapper")

    direction: str | None = None
    fence_char: str | None = None
    fence_length = 0

    for number, line in enumerate(text.splitlines(keepends=True), start=1):
        stripped = line.strip()
        token = fence_token(line)

        if fence_char is not None:
            if token and token[0] == fence_char and token[1] >= fence_length and not token[2]:
                fence_char = None
                fence_length = 0
            continue

        if stripped == MARKER:
            continue
        if ORDERED_PREFIX_IN_BDI_RE.match(line.rstrip("\n")):
            errors.append(f"line {number}: ordered-list marker must remain outside bdi")
        if stripped == RTL_OPEN:
            if direction is not None:
                errors.append(f"line {number}: nested direction wrapper")
            direction = "rtl"
            continue
        if stripped == LTR_OPEN:
            if direction is not None:
                errors.append(f"line {number}: nested direction wrapper")
            direction = "ltr"
            continue
        if stripped == DIV_CLOSE:
            if direction is None:
                errors.append(f"line {number}: closing wrapper without an open wrapper")
            direction = None
            continue

        if token:
            if direction != "ltr":
                errors.append(f"line {number}: fenced code must be inside an LTR wrapper")
            fence_char, fence_length, _ = token
            continue

        if stripped and direction != "rtl":
            errors.append(f"line {number}: prose must be inside an RTL wrapper")
        if direction == "rtl" and isolate_ltr_terms(isolate_inline_code(line)) != line:
            errors.append(f"line {number}: unisolated LTR term or inline code")

    if fence_char is not None:
        errors.append("unclosed fenced code block")
    if direction is not None:
        errors.append("unclosed direction wrapper")
    return errors


def markdown_files(root: Path, requested: list[str]) -> list[Path]:
    if requested:
        candidates = [(root / value).resolve() for value in requested]
    else:
        candidates = list(root.rglob("*.md"))
    ignored = {".git", ".idea", ".venv", "target", "node_modules"}
    return sorted(
        path
        for path in candidates
        if path.is_file() and path.suffix.lower() == ".md" and not ignored.intersection(path.parts)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="format Persian Markdown in place")
    mode.add_argument("--check", action="store_true", help="validate canonical BiDi formatting")
    parser.add_argument("paths", nargs="*", help="repository-relative Markdown paths")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    failures: list[str] = []
    changed = 0
    checked = 0

    for path in markdown_files(root, args.paths):
        text = path.read_text(encoding="utf-8")
        if not contains_persian(text) and not text.startswith(MARKER):
            continue
        relative = path.relative_to(root)
        checked += 1
        try:
            if args.write:
                formatted = format_markdown(text)
                if formatted != text:
                    path.write_text(formatted, encoding="utf-8", newline="\n")
                    changed += 1
            else:
                for error in validate_markdown(text):
                    failures.append(f"{relative}: {error}")
        except (BidiFormatError, UnicodeError) as error:
            failures.append(f"{relative}: {error}")

    if failures:
        print("Markdown BiDi validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    action = "formatted" if args.write else "validated"
    print(f"{action} {checked} Persian Markdown files; changed {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
