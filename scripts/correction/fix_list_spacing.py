"""Insert blank lines before bullet/numbered lists after colon lines."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable


def _is_list_item(stripped: str) -> bool:
    if stripped.startswith(('* -', '- -')):
        return False
    if stripped.startswith(('-', '*')):
        return True
    if stripped[:1].isdigit() and stripped[1:2] == '.':
        return True
    return False


def fix_list_spacing(content: str) -> str:
    """Ensure a blank line after lines ending with ':' before lists."""
    lines = content.splitlines()
    output: list[str] = []
    prev_non_blank = ""
    in_literal_block = False
    literal_content_indent = None

    for line in lines:
        stripped = line.strip()
        leading_spaces = len(line) - len(line.lstrip(" "))

        if in_literal_block:
            if stripped == "":
                output.append(line)
                continue
            if literal_content_indent is None:
                literal_content_indent = leading_spaces
                output.append(line)
                continue
            if leading_spaces < literal_content_indent:
                in_literal_block = False
                literal_content_indent = None
            else:
                output.append(line)
                continue

        if (stripped.endswith("::") and not stripped.startswith("..")) or stripped.startswith(".. code-block::"):
            in_literal_block = True
            literal_content_indent = None
            output.append(line)
            prev_non_blank = stripped
            continue

        if stripped and _is_list_item(stripped):
            if prev_non_blank.endswith(":"):
                output.append(" " * leading_spaces)
            output.append(line)
            prev_non_blank = stripped
            continue

        output.append(line)
        if stripped:
            prev_non_blank = stripped

    return "\n".join(output) + ("\n" if content.endswith("\n") else "")


def _iter_paths(paths: Iterable[str]) -> Iterable[Path]:
    for raw in paths:
        path = Path(raw)
        if path.is_file():
            yield path
        else:
            raise FileNotFoundError(f"File not found: {path}")


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Insert blank lines before lists after colon lines.",
    )
    parser.add_argument("paths", nargs="+", help="RST files to normalize")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    args = parser.parse_args()

    dry_run = not args.apply
    mode_str = "DRY RUN" if dry_run else "APPLYING"
    print(f"fix_list_spacing.py - {mode_str}")
    
    changed = 0
    for path in _iter_paths(args.paths):
        content = path.read_text(encoding="utf-8")
        updated = fix_list_spacing(content)
        if updated != content:
            print(f"📄 {path}")
            changed += 1
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
                print("   ✅ Corregido")
    
    print(f"\nArchivos con cambios: {changed}")
    if dry_run and changed > 0:
        print("💡 Ejecuta con --apply para aplicar los cambios")
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
