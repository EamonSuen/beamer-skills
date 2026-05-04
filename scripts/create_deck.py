#!/usr/bin/env python3
"""Safely copy the bundled Beamer template into a new deck directory."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new Beamer deck from the bundled academic template."
    )
    parser.add_argument(
        "target",
        help="New deck directory to create. The path must not already exist.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parents[1]
    template_dir = skill_dir / "assets" / "beamer-universal-academic-template"
    target = Path(args.target).expanduser().resolve()

    if not template_dir.is_dir():
        print(f"Template asset not found: {template_dir}", file=sys.stderr)
        return 1

    if target.exists():
        print(f"Refusing to overwrite existing path: {target}", file=sys.stderr)
        return 2

    if not target.parent.is_dir():
        print(f"Parent directory does not exist: {target.parent}", file=sys.stderr)
        return 3

    shutil.copytree(template_dir, target)
    print(f"Created Beamer deck at: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
