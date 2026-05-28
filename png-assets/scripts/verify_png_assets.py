#!/usr/bin/env python3
"""Verify generated PNG assets used by apps, websites, H5 pages, and design outputs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required. Install with: python3 -m pip install pillow") from exc


PNG_SUFFIX = ".png"


def iter_pngs(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(p for p in path.rglob("*") if p.suffix.lower() == PNG_SUFFIX))
        elif path.suffix.lower() == PNG_SUFFIX:
            files.append(path)
        else:
            print(f"skip non-png: {path}", file=sys.stderr)
    return files


def alpha_bbox(alpha: Image.Image, threshold: int) -> tuple[int, int, int, int] | None:
    mask = alpha.point(lambda value: 255 if value > threshold else 0)
    return mask.getbbox()


def check_file(path: Path, args: argparse.Namespace) -> tuple[bool, list[str]]:
    messages: list[str] = []
    ok = True

    try:
        with Image.open(path) as image:
            image.load()
            width, height = image.size
            mode = image.mode

            if width < args.min_size or height < args.min_size:
                ok = False
                messages.append(f"too small {width}x{height}")

            if mode not in {"RGBA", "LA"} and "transparency" not in image.info:
                if args.allow_rgb:
                    messages.append(f"no alpha ({mode})")
                    return ok, messages
                ok = False
                messages.append(f"missing alpha ({mode})")
                return ok, messages

            rgba = image.convert("RGBA")
            alpha = rgba.getchannel("A")
            corners = [
                alpha.getpixel((0, 0)),
                alpha.getpixel((width - 1, 0)),
                alpha.getpixel((0, height - 1)),
                alpha.getpixel((width - 1, height - 1)),
            ]
            if max(corners) > args.corner_alpha:
                ok = False
                messages.append(f"corners not transparent alpha={corners}")

            bbox = alpha_bbox(alpha, args.subject_alpha)
            if bbox is None:
                ok = False
                messages.append("empty alpha bbox")
            else:
                left, top, right, bottom = bbox
                subject_width = right - left
                subject_height = bottom - top
                coverage = (subject_width * subject_height) / float(width * height)
                if coverage < args.min_coverage:
                    ok = False
                    messages.append(f"subject coverage too low {coverage:.1%}")
                if coverage > args.max_coverage:
                    messages.append(f"subject coverage high {coverage:.1%}")
                margin = min(left, top, width - right, height - bottom)
                if margin < args.min_margin:
                    messages.append(f"tight crop margin={margin}px")

            return ok, messages
    except Exception as exc:  # pragma: no cover
        return False, [f"cannot open: {exc}"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="PNG files or directories to verify")
    parser.add_argument("--allow-rgb", action="store_true", help="allow RGB PNGs such as full backgrounds")
    parser.add_argument("--min-size", type=int, default=32, help="minimum width and height in px")
    parser.add_argument("--corner-alpha", type=int, default=8, help="maximum allowed alpha at image corners")
    parser.add_argument("--subject-alpha", type=int, default=16, help="alpha threshold for subject bbox")
    parser.add_argument("--min-coverage", type=float, default=0.01, help="minimum subject bbox coverage")
    parser.add_argument("--max-coverage", type=float, default=0.92, help="warn when subject bbox coverage is above this")
    parser.add_argument("--min-margin", type=int, default=2, help="warn when subject bbox is closer than this to any edge")
    args = parser.parse_args()

    files = iter_pngs(args.paths)
    if not files:
        print("No PNG files found.", file=sys.stderr)
        return 2

    failures = 0
    for file in files:
        ok, messages = check_file(file, args)
        status = "OK" if ok else "FAIL"
        suffix = f" - {'; '.join(messages)}" if messages else ""
        print(f"{status} {file}{suffix}")
        if not ok:
            failures += 1

    print(f"Checked {len(files)} PNG file(s), failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
