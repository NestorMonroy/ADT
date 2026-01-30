from pathlib import Path
import sys

import pytest


@pytest.fixture()
def sample_toctree_map():
    return {
        "a.rst": """Titulo\n======\n\n.. toctree::\n   :maxdepth: 1\n\n   faq\n   intro\n""",
        "b.rst": """Otro\n====\n\n.. toctree::\n   :maxdepth: 2\n\n   faq\n   guia\n""",
        "c.rst": """Doc\n===\n\n.. toctree::\n   :maxdepth: 1\n\nSeccion\n=======\n""",
        "d.rst": (
            "Ejemplo\n=======\n\n.. code-block:: rst\n\n"
            "   .. toctree::\n"
            "      :maxdepth: 1\n\n"
            "      ejemplo\n"
        ),
    }


def test_find_duplicate_toctree(sample_toctree_map):
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from scripts.find_duplicate_toctree import find_duplicate_toctree_entries

    duplicates = find_duplicate_toctree_entries(sample_toctree_map)

    assert duplicates == {"faq": ["a.rst", "b.rst"]}
