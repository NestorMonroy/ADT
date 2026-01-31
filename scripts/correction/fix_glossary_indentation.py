"""Normalize glossary indentation in reStructuredText files."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

UNDERLINE_CHARS = set('=~-^"`:+#<>')


def _is_underline(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and all(char in UNDERLINE_CHARS for char in stripped)


def fix_glossary_indentation(content: str) -> str:
    """Normalize indentation inside ``.. glossary::`` directives."""
    lines = content.splitlines()
    output: list[str] = []
    in_glossary = False
    prev_blank = True
    in_definition = False

    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith(".. glossary::"):
            in_glossary = True
            prev_blank = True
            output.append(line)
            continue

        if in_glossary:
            if stripped and not line.startswith(" "):
                next_line = lines[index + 1] if index + 1 < len(lines) else ""
                if _is_underline(next_line):
                    in_glossary = False
                    output.append(line)
                    prev_blank = False
                    in_definition = False
                    continue

            if stripped == "":
                output.append("")
                prev_blank = True
                continue

            is_term = prev_blank and ":" not in stripped and not stripped.endswith((".", "!", "?"))
            base_indent = 2 if is_term else 4
            leading_spaces = len(line) - len(line.lstrip(" "))
            indent_size = max(base_indent, leading_spaces)
            output.append(f"{' ' * indent_size}{stripped}")
            prev_blank = False
            if is_term:
                in_definition = True
            continue

        output.append(line)
        prev_blank = stripped == ""

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
        description="Normalize indentation inside .. glossary:: directives.",
    )
    parser.add_argument("paths", nargs="+", help="RST files to normalize")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    args = parser.parse_args()

    dry_run = not args.apply
    mode_str = "DRY RUN" if dry_run else "APPLYING"
    print(f"fix_glossary_indentation.py - {mode_str}")
    
    changed = 0
    for path in _iter_paths(args.paths):
        content = path.read_text(encoding="utf-8")
        updated = fix_glossary_indentation(content)
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
