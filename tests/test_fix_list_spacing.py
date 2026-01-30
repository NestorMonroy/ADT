from pathlib import Path
import sys

import pytest


@pytest.fixture()
def sample_list_spacing_content():
    return (
        "Titulo\n"
        "======\n\n"
        "Ejemplos:\n"
        "- Item uno\n"
        "- Item dos\n\n"
        ".. list-table::\n"
        " :header-rows: 1\n"
        "\n"
        " * - Col A\n"
        "   - Col B\n\n"
        "Seccion\n"
        "=======\n"
    )


def test_fix_list_spacing(tmp_path, sample_list_spacing_content):
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from scripts.fix_list_spacing import fix_list_spacing

    source = tmp_path / "sample.rst"
    source.write_text(sample_list_spacing_content, encoding="utf-8")

    updated = fix_list_spacing(source.read_text(encoding="utf-8"))
    source.write_text(updated, encoding="utf-8")

    expected = (
        "Titulo\n"
        "======\n\n"
        "Ejemplos:\n"
        "\n"
        "- Item uno\n"
        "- Item dos\n\n"
        ".. list-table::\n"
        " :header-rows: 1\n"
        "\n"
        " * - Col A\n"
        "   - Col B\n\n"
        "Seccion\n"
        "=======\n"
    )

    assert source.read_text(encoding="utf-8") == expected
