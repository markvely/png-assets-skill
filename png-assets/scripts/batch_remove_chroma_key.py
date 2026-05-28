#!/usr/bin/env python3
"""Batch remove chroma-key backgrounds from generated PNG assets."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def iter_inputs(path: Path) -> list[Path]:
    if path.is_dir():
        return sorted(p for p in path.rglob("*.png") if p.is_file())
    if path.suffix.lower() == ".png":
        return [path]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Raw PNG file or directory")
    parser.add_argument("--out-dir", type=Path, required=True, help="Directory for alpha PNG outputs")
    parser.add_argument("--suffix", default="-alpha", help="Suffix before .png for output files")
    parser.add_argument("--edge-contract", type=int, default=0, help="Pass edge-contract to the chroma-key script")
    parser.add_argument("--script", type=Path, default=Path.home() / ".codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
    args = parser.parse_args()

    files = iter_inputs(args.input)
    if not files:
        print("No PNG inputs found.", file=sys.stderr)
        return 2

    args.out_dir.mkdir(parents=True, exist_ok=True)
    failures = 0

    for source in files:
        out = args.out_dir / f"{source.stem}{args.suffix}.png"
        cmd = [
            sys.executable,
            str(args.script),
            "--input",
            str(source),
            "--out",
            str(out),
            "--auto-key",
            "border",
            "--soft-matte",
            "--transparent-threshold",
            "12",
            "--opaque-threshold",
            "220",
            "--despill",
        ]
        if args.edge_contract:
            cmd.extend(["--edge-contract", str(args.edge_contract)])

        print(f"{source} -> {out}")
        result = subprocess.run(cmd, text=True)
        if result.returncode != 0:
            failures += 1

    print(f"Processed {len(files)} file(s), failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
