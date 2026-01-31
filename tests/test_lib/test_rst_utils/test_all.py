"""Tests para renderer, analyzer y types."""

import pytest
from scripts.lib.rst_utils.rst_types import (
    Heading, BlockType, Issue, IssueSeverity, DocumentStructure
)
from scripts.lib.rst_utils.renderer import render_heading
from scripts.lib.rst_utils.analyzer import detect_heading_level_issues


class TestTypes:
    """Tests para tipos de datos."""
    
    def test_heading_creation(self):
        """Debe crear heading correctamente."""
        h = Heading(
            type=BlockType.HEADING,
            content="Test",
            line_number=1,
            raw_lines=("Test", "===="),
            level=1,
            underline_char='=',
            has_overline=False,
            title="Test"
        )
        assert h.level == 1
        assert h.title == "Test"
    
    def test_heading_immutability(self):
        """Heading debe ser inmutable."""
        h = Heading(
            type=BlockType.HEADING,
            content="Test",
            line_number=1,
            raw_lines=("Test", "===="),
            level=1,
            underline_char='=',
            has_overline=False,
            title="Test"
        )
        with pytest.raises(Exception):
            h.level = 2
    
    def test_document_structure_has_errors(self):
        """Debe detectar si hay errores."""
        issue = Issue(
            file_path="test.rst",
            line_number=1,
            severity=IssueSeverity.ERROR,
            category="test",
            message="Error"
        )
        doc = DocumentStructure(
            file_path="test.rst",
            blocks=(),
            headings=(),
            issues=(issue,)
        )
        assert doc.has_errors() == True


class TestRenderer:
    """Tests para renderer."""
    
    def test_render_heading(self):
        """Debe renderizar heading correctamente."""
        h = Heading(
            type=BlockType.HEADING,
            content="Test",
            line_number=1,
            raw_lines=("Test", "===="),
            level=1,
            underline_char='=',
            has_overline=False,
            title="Test"
        )
        rendered = render_heading(h)
        assert "Test" in rendered
        assert "====" in rendered


class TestAnalyzer:
    """Tests para analyzer."""
    
    def test_detect_heading_level_jump(self):
        """Debe detectar saltos de nivel."""
        h1 = Heading(
            type=BlockType.HEADING,
            content="H1",
            line_number=1,
            raw_lines=("H1", "=="),
            level=1,
            underline_char='=',
            has_overline=False,
            title="H1"
        )
        h2 = Heading(
            type=BlockType.HEADING,
            content="H4",
            line_number=4,
            raw_lines=("H4", "^^"),
            level=4,
            underline_char='^',
            has_overline=False,
            title="H4"
        )
        issues = detect_heading_level_issues((h1, h2), "test.rst")
        assert len(issues) > 0
