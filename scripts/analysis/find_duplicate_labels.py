"""Find duplicate labels in RST files with optional auto-fix."""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Dict


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


def auto_fix_duplicate_labels(duplicates: dict[str, list[str]]) -> int:
    """Auto-fix duplicate labels by renaming them with unique suffixes.
    
    Args:
        duplicates: Dict of label -> list of files containing it
        
    Returns:
        Number of labels fixed
    """
    fixed_count = 0
    
    for label, file_paths in duplicates.items():
        if len(file_paths) <= 1:
            continue
        
        # Keep first occurrence, rename others
        for idx, file_path in enumerate(file_paths[1:], start=2):
            path = Path(file_path)
            content = path.read_text(encoding='utf-8')
            
            # Create new unique label
            new_label = f"{label}-{idx}"
            
            # Replace label definition
            old_def = f".. _{label}:"
            new_def = f".. _{new_label}:"
            
            if old_def in content:
                content = content.replace(old_def, new_def, 1)  # Only first occurrence
                path.write_text(content, encoding='utf-8')
                print(f"✅ {file_path}: '{label}' → '{new_label}'")
                fixed_count += 1
    
    return fixed_count


def main() -> int:
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description="Find duplicate labels in RST files.",
    )
    parser.add_argument("paths", nargs="+", help="RST files to scan")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--fix", action="store_true", help="Auto-fix duplicates by renaming")
    args = parser.parse_args()

    content_map = {str(path): path.read_text(encoding="utf-8") for path in _iter_paths(args.paths)}
    duplicates = find_duplicate_labels(content_map)

    if not duplicates:
        print("✅ No duplicate labels found")
        return 0
    
    if args.fix:
        print(f"🔧 Auto-fixing {len(duplicates)} duplicate labels...")
        fixed = auto_fix_duplicate_labels(duplicates)
        print(f"\n✅ Fixed {fixed} labels")
        return 0
    
    if args.json:
        print(json.dumps(duplicates, ensure_ascii=False, indent=2))
    else:
        print(f"⚠️  Found {len(duplicates)} duplicate labels:")
        for label, paths in sorted(duplicates.items()):
            print(f"\n{label}:")
            for path in sorted(paths):
                print(f"  - {path}")
        print(f"\n💡 Run with --fix to auto-rename duplicates")

    return 1 if duplicates else 0


if __name__ == "__main__":
    raise SystemExit(main())
