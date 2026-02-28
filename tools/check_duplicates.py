#!/usr/bin/env python3
"""Check duplicate IDs and aliases across genre files."""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency: pyyaml. Install with `pip install pyyaml`.") from exc


ROOT = Path(__file__).resolve().parents[1]
GENRES_DIR = ROOT / "data" / "genres"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def main() -> int:
    id_to_file: dict[str, Path] = {}
    alias_to_ids: dict[str, set[str]] = {}
    errors: list[str] = []
    warnings: list[str] = []

    for path in sorted(GENRES_DIR.rglob("*.yaml")):
        rel = path.relative_to(ROOT)
        data = load_yaml(path)
        gid = data.get("id")
        if not gid:
            errors.append(f"{rel}: missing `id`.")
            continue

        if gid in id_to_file:
            errors.append(f"Duplicate id `{gid}` in {rel} and {id_to_file[gid].relative_to(ROOT)}.")
        id_to_file[gid] = path

        for alias in data.get("aliases", []):
            key = str(alias).strip().casefold()
            alias_to_ids.setdefault(key, set()).add(gid)

    for alias, ids in sorted(alias_to_ids.items()):
        if len(ids) > 1:
            warnings.append(f"Alias `{alias}` used by multiple IDs: {', '.join(sorted(ids))}.")

    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        for err in errors:
            print(err)
        return 1

    print("Duplicate checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
