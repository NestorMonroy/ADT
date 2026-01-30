from pathlib import Path
import sys

import pytest


@pytest.fixture()
def sample_label_map():
    return {
        "a.rst": """.. _shared_label:\n\nTitulo\n======\n\n.. _unique_a:\n""",
        "b.rst": """Intro\n=====\n\n.. _shared_label:\n""",
        "c.rst": """Ejemplo\n=======\n\n.. code-block:: rst\n\n   .. _ignored_label:\n""",
    }


def test_find_duplicate_labels(sample_label_map):
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))

    from scripts.find_duplicate_labels import find_duplicate_labels

    duplicates = find_duplicate_labels(sample_label_map)

    assert duplicates == {"shared_label": ["a.rst", "b.rst"]}
