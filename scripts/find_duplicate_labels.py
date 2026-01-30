"""Find duplicate labels in RST files."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Iterable


def _extract_labels(lines: Iterable[str]) -> list[str]:
    labels: list[str] = []
    in_literal_block = False
    literal_content_indent = None

    for line in lines:
        stripped = line.strip()
        leading_spaces = len(line) - len(line.lstrip(" "))
        if in_literal_block:
            if stripped == "":
                continue
            if literal_content_indent is None:
                literal_content_indent = leading_spaces
                continue
            if leading_spaces < literal_content_indent:
                in_literal_block = False
                literal_content_indent = None
            else:
                continue
        if (stripped.endswith("::") and not stripped.startswith("..")) or stripped.startswith(".. code-block::"):
            in_literal_block = True
            literal_content_indent = None
            continue
        if stripped.startswith(".. _") and stripped.endswith(":"):
            label = stripped[4:-1].strip()
            if label:
                labels.append(label)
    return labels


def find_duplicate_labels(content_map: dict[str, str]) -> dict[str, list[str]]:
    """Return labels that appear in more than one file."""
    seen: dict[str, list[str]] = defaultdict(list)
    for path, content in content_map.items():
        for label in _extract_labels(content.splitlines()):
            if path not in seen[label]:
                seen[label].append(path)
    return {label: paths for label, paths in seen.items() if len(paths) > 1}


def _iter_paths(paths: Iterable[str]) -> Iterable[Path]:
    for raw in paths:
        path = Path(raw)
        if path.is_file():
            yield path
        else:
            raise FileNotFoundError(f"File not found: {path}")


def main() -> int:
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description="Find duplicate labels in RST files.",
    )
    parser.add_argument("paths", nargs="+", help="RST files to scan")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    content_map = {str(path): path.read_text(encoding="utf-8") for path in _iter_paths(args.paths)}
    duplicates = find_duplicate_labels(content_map)

    if args.json:
        print(json.dumps(duplicates, ensure_ascii=False, indent=2))
    else:
        for label, paths in sorted(duplicates.items()):
            print(f"{label}:")
            for path in sorted(paths):
                print(f"  - {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
