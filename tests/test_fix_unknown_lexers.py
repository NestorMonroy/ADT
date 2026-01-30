from pathlib import Path
import sys

import pytest


@pytest.fixture()
def sample_unknown_lexer_content():
    return (
        "Titulo\n"
        "======\n\n"
        ".. code-block:: plantuml\n"
        "\n"
        "  @startuml\n"
        "  A -> B\n"
        "  @enduml\n"
        "\n"
        ".. code-block:: text\n"
        "\n"
        "  mantener\n"
    )


def test_fix_unknown_lexers(tmp_path, sample_unknown_lexer_content):
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from scripts.fix_unknown_lexers import fix_unknown_lexers

    source = tmp_path / "sample.rst"
    source.write_text(sample_unknown_lexer_content, encoding="utf-8")

    updated = fix_unknown_lexers(source.read_text(encoding="utf-8"))
    source.write_text(updated, encoding="utf-8")

    expected = (
        "Titulo\n"
        "======\n\n"
        ".. code-block:: text\n"
        "\n"
        "  @startuml\n"
        "  A -> B\n"
        "  @enduml\n"
        "\n"
        ".. code-block:: text\n"
        "\n"
        "  mantener\n"
    )

    assert source.read_text(encoding="utf-8") == expected
