#!/usr/bin/env python3
"""Check static asset references in a standalone HTML file."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ATTR_RE = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
URL_RE = re.compile(r"""url\(\s*(['"]?)(.*?)\1\s*\)""", re.IGNORECASE)
SKIP_PREFIXES = ("http://", "https://", "data:", "blob:", "mailto:", "tel:", "#", "javascript:")


def should_skip(value: str) -> bool:
    stripped = value.strip()
    if not stripped:
        return True
    lower = stripped.lower()
    return lower.startswith(SKIP_PREFIXES)


def normalize_ref(value: str) -> str | None:
    value = value.strip()
    if should_skip(value):
        return None
    parsed = urlparse(value)
    path = parsed.path if parsed.scheme == "" else value
    if not path:
        return None
    return unquote(path)


def collect_refs(text: str) -> list[str]:
    refs: list[str] = []
    for match in ATTR_RE.finditer(text):
        ref = normalize_ref(match.group(1))
        if ref:
            refs.append(ref)
    for match in URL_RE.finditer(text):
        ref = normalize_ref(match.group(2))
        if ref:
            refs.append(ref)
    return sorted(set(refs))


def resolve_ref(ref: str, base: Path) -> Path:
    path = Path(ref)
    if path.is_absolute():
        return path
    return (base / path).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="HTML file to inspect")
    parser.add_argument("--base", type=Path, help="base directory for relative paths; defaults to HTML parent")
    args = parser.parse_args()

    html = args.html.resolve()
    if not html.exists():
        print(f"HTML file not found: {html}", file=sys.stderr)
        return 2

    base = args.base.resolve() if args.base else html.parent
    text = html.read_text(encoding="utf-8")
    refs = collect_refs(text)
    missing: list[tuple[str, Path]] = []

    for ref in refs:
        path = resolve_ref(ref, base)
        if not path.exists():
            missing.append((ref, path))
            print(f"MISS {ref} -> {path}")
        else:
            print(f"OK   {ref}")

    print(f"Checked {len(refs)} static reference(s), missing: {len(missing)}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
