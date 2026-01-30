from pathlib import Path
import sys

import pytest


@pytest.fixture()
def sample_glossary_content():
    return (
        ".. glossary::\n"
        "\n"
        " Termino\n"
        " Definicion en una linea.\n"
        "\n"
        " Otra linea.\n"
        "\n"
        " Otro Termino\n"
        " Segunda definicion.\n"
        "\n"
        "Seccion Siguiente\n"
        "==================\n"
    )


def test_fix_glossary_indentation(tmp_path, sample_glossary_content):
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from scripts.fix_glossary_indentation import fix_glossary_indentation

    source = tmp_path / "sample.rst"
    source.write_text(sample_glossary_content, encoding="utf-8")

    updated = fix_glossary_indentation(source.read_text(encoding="utf-8"))
    source.write_text(updated, encoding="utf-8")

    expected = (
        ".. glossary::\n"
        "\n"
        "  Termino\n"
        "    Definicion en una linea.\n"
        "\n"
        "    Otra linea.\n"
        "\n"
        "  Otro Termino\n"
        "    Segunda definicion.\n"
        "\n"
        "Seccion Siguiente\n"
        "==================\n"
    )

    assert source.read_text(encoding="utf-8") == expected
