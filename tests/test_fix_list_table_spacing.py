from pathlib import Path
import sys

import pytest


@pytest.fixture()
def sample_list_table_content():
    return (
        "Titulo\n"
        "======\n\n"
        ".. list-table::\n"
        " :header-rows: 1\n"
        " :widths: 10 20\n"
        " * - Columna A\n"
        "   - Columna B\n"
        " * - Valor A\n"
        "   - Valor B\n"
        "\n"
        "Siguiente\n"
        "=========\n"
    )


def test_fix_list_table_spacing(tmp_path, sample_list_table_content):
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from scripts.fix_list_table_spacing import fix_list_table_spacing

    source = tmp_path / "sample.rst"
    source.write_text(sample_list_table_content, encoding="utf-8")

    updated = fix_list_table_spacing(source.read_text(encoding="utf-8"))
    source.write_text(updated, encoding="utf-8")

    expected = (
        "Titulo\n"
        "======\n\n"
        ".. list-table::\n"
        " :header-rows: 1\n"
        " :widths: 10 20\n"
        "\n"
        " * - Columna A\n"
        "   - Columna B\n"
        " * - Valor A\n"
        "   - Valor B\n"
        "\n"
        "Siguiente\n"
        "=========\n"
    )

    assert source.read_text(encoding="utf-8") == expected
