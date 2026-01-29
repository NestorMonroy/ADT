import importlib.util
from pathlib import Path


def load_conf_module():
    conf_path = Path(__file__).resolve().parents[1] / "source" / "conf.py"
    spec = importlib.util.spec_from_file_location("adt_conf", conf_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_skip_intersphinx():
    conf = load_conf_module()
    mapping = conf.resolve_intersphinx_mapping(
        {"SPHINX_SKIP_INTERSPHINX": "1"},
        Path("/tmp/nonexistent"),
    )

    assert mapping == {}


def test_defaults_without_inventory(tmp_path):
    conf = load_conf_module()
    mapping = conf.resolve_intersphinx_mapping({}, tmp_path)

    assert mapping["python"] == ("https://docs.python.org/3/", None)
    assert mapping["sphinx"] == ("https://www.sphinx-doc.org/en/master/", None)


def test_inventory_from_env_path(tmp_path):
    conf = load_conf_module()
    python_inv = tmp_path / "custom-python.inv"
    python_inv.write_text("placeholder")

    mapping = conf.resolve_intersphinx_mapping(
        {"SPHINX_INTERSPHINX_PYTHON_INV": str(python_inv)},
        tmp_path,
    )

    assert mapping["python"][1] == str(python_inv)


def test_inventory_from_downloads_dir(tmp_path):
    conf = load_conf_module()
    sphinx_inv = tmp_path / "sphinx-objects.inv"
    sphinx_inv.write_text("placeholder")

    mapping = conf.resolve_intersphinx_mapping({}, tmp_path)

    assert mapping["sphinx"][1] == str(sphinx_inv)


def test_inventory_from_git_clone_layout(tmp_path):
    conf = load_conf_module()
    python_inv = tmp_path / "cpython" / "Doc" / "objects.inv"
    sphinx_inv = tmp_path / "sphinx" / "doc" / "objects.inv"
    python_inv.parent.mkdir(parents=True, exist_ok=True)
    sphinx_inv.parent.mkdir(parents=True, exist_ok=True)
    python_inv.write_text("placeholder")
    sphinx_inv.write_text("placeholder")

    mapping = conf.resolve_intersphinx_mapping({}, tmp_path)

    assert mapping["python"][1] == str(python_inv)
    assert mapping["sphinx"][1] == str(sphinx_inv)
