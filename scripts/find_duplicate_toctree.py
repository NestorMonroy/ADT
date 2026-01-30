"""Find duplicate toctree references across documentation files."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Iterable
import os


def _extract_toctree_entries(lines: Iterable[str]) -> list[str]:
    entries: list[str] = []
    in_toctree = False
    base_indent = None
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
        if stripped.startswith(".. toctree::"):
            in_toctree = True
            base_indent = None
            continue
        if in_toctree:
            if stripped == "":
                if base_indent is None:
                    continue
                entries.append("")
                continue
            indent = leading_spaces
            if base_indent is None:
                if stripped.startswith(":"):
                    continue
                if indent == 0:
                    in_toctree = False
                    base_indent = None
                    continue
                base_indent = indent
            if stripped.startswith(":"):
                continue
            if indent < (base_indent or 0):
                in_toctree = False
                base_indent = None
                continue
            entries.append(stripped)
    return [entry for entry in entries if entry]


def _normalize_entry(entry: str, file_path: Path, root: Path) -> str | None:
    normalized = entry.strip()
    if not normalized or normalized.startswith("http") or normalized.startswith("mailto:"):
        return None
    normalized = normalized.lstrip("/")
    if normalized.endswith((".rst", ".md")):
        normalized = normalized.rsplit(".", 1)[0]
    if entry.startswith("/"):
        resolved = root / normalized
    else:
        resolved = file_path.parent / normalized
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return resolved.as_posix()


def _common_root(paths: Iterable[Path]) -> Path:
    path_list = [path.resolve() for path in paths]
    if not path_list:
        return Path(".")
    common = os.path.commonpath([str(path.parent) for path in path_list])
    return Path(common)


def find_duplicate_toctree_entries(content_map: dict[str, str]) -> dict[str, list[str]]:
    """Return entries that appear in more than one toctree."""
    seen: dict[str, list[str]] = defaultdict(list)
    paths = [Path(path) for path in content_map]
    root = _common_root(paths)
    for path, content in content_map.items():
        file_path = Path(path)
        entries = _extract_toctree_entries(content.splitlines())
        for entry in entries:
            normalized = _normalize_entry(entry, file_path, root)
            if not normalized:
                continue
            if path not in seen[normalized]:
                seen[normalized].append(path)
    return {entry: paths for entry, paths in seen.items() if len(paths) > 1}


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
        description="Find duplicate toctree entries across RST files.",
    )
    parser.add_argument("paths", nargs="+", help="RST files to scan")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    content_map = {str(path): path.read_text(encoding="utf-8") for path in _iter_paths(args.paths)}
    duplicates = find_duplicate_toctree_entries(content_map)

    if args.json:
        print(json.dumps(duplicates, ensure_ascii=False, indent=2))
    else:
        for entry, paths in sorted(duplicates.items()):
            print(f"{entry}:")
            for path in sorted(paths):
                print(f"  - {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
