"""Configuración compartida para pytest."""

import pytest
from pathlib import Path

@pytest.fixture
def fixtures_dir():
    """Retorna directorio de fixtures."""
    return Path(__file__).parent / 'fixtures'

@pytest.fixture
def sample_rst_file(fixtures_dir, tmp_path):
    """Crea archivo RST temporal para testing."""
    test_file = tmp_path / 'test.rst'
    test_file.write_text("Título\n======\n\nContenido.\n")
    return test_file

@pytest.fixture
def expected_output(fixtures_dir):
    """Lee output esperado de fixture."""
    # Placeholder - se actualizará con fixtures reales
    return "Expected output"
