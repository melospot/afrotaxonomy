#!/usr/bin/env python3
"""Lint IDs and core naming conventions."""

from __future__ import annotations

import re
from pathlib import Path
import sys

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency: pyyaml. Install with `pip install pyyaml`.") from exc


ROOT = Path(__file__).resolve().parents[1]
GENRES_DIR = ROOT / "data" / "genres"
ID_RE = re.compile(r"^[a-z0-9_]+$")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for path in sorted(GENRES_DIR.rglob("*.yaml")):
        rel = path.relative_to(ROOT)
        data = load_yaml(path)
        gid = data.get("id")
        if not gid:
            errors.append(f"{rel}: missing `id`.")
            continue
        if not ID_RE.match(gid):
            errors.append(f"{rel}: `id` must match {ID_RE.pattern}.")
        if not data.get("name"):
            errors.append(f"{rel}: missing `name`.")
        if "parents" not in data:
            errors.append(f"{rel}: missing `parents`.")

        aliases = data.get("aliases", [])
        alias_keys = set()
        for alias in aliases:
            key = str(alias).strip().casefold()
            if key in alias_keys:
                warnings.append(f"{rel}: duplicate alias `{alias}`.")
            alias_keys.add(key)

    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        for err in errors:
            print(err)
        return 1

    print("Lint checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
