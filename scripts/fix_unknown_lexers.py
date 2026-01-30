"""Replace unknown code-block lexers with text to avoid highlighting warnings."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

UNKNOWN_LEXERS = {"plantuml", "atl", "ocl"}


def fix_unknown_lexers(content: str) -> str:
    """Replace code-block directives with unknown lexers to `text`."""
    lines = content.splitlines()
    output: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith(".. code-block::"):
            parts = stripped.split()
            if len(parts) >= 3 and parts[2] in UNKNOWN_LEXERS:
                output.append(".. code-block:: text")
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
        description="Replace unknown code-block lexers with text.",
    )
    parser.add_argument("paths", nargs="+", help="RST files to normalize")
    args = parser.parse_args()

    for path in _iter_paths(args.paths):
        content = path.read_text(encoding="utf-8")
        updated = fix_unknown_lexers(content)
        if updated != content:
            path.write_text(updated, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
