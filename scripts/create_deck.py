#!/usr/bin/env python3
"""Safely create a new Beamer working directory from the bundled template."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new Beamer working directory from the bundled academic template."
    )
    parser.add_argument(
        "target",
        help="New deck directory to create. The path must not already exist.",
    )
    parser.add_argument(
        "--parents",
        action="store_true",
        help="Create missing parent directories before creating the deck directory.",
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

    if not target.parent.exists() and args.parents:
        target.parent.mkdir(parents=True)

    if not target.parent.is_dir():
        print(f"Parent directory does not exist: {target.parent}", file=sys.stderr)
        print("Use --parents to create missing parent directories.", file=sys.stderr)
        return 3

    shutil.copytree(template_dir, target)
    print(f"Created Beamer working directory at: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
