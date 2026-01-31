"""Ensure list-table blocks include a blank line before rows."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable


def fix_list_table_spacing(content: str) -> str:
    """Insert a blank line between list-table options and the first row."""
    lines = content.splitlines()
    output: list[str] = []
    pending_blank = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith(".. list-table::"):
            pending_blank = True
            output.append(line)
            continue

        if pending_blank:
            if stripped.startswith(":"):
                output.append(line)
                continue
            if stripped.startswith("*") or stripped.startswith("-"):
                output.append("")
                output.append(line)
                pending_blank = False
                continue
            if stripped == "":
                output.append(line)
                pending_blank = False
                continue

        output.append(line)

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
        description="Ensure list-table blocks include a blank line before rows.",
    )
    parser.add_argument("paths", nargs="+", help="RST files to normalize")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    args = parser.parse_args()

    dry_run = not args.apply
    mode_str = "DRY RUN" if dry_run else "APPLYING"
    print(f"fix_list_table_spacing.py - {mode_str}")
    
    changed = 0
    for path in _iter_paths(args.paths):
        content = path.read_text(encoding="utf-8")
        updated = fix_list_table_spacing(content)
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
