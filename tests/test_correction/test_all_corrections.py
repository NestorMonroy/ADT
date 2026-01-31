"""Tests para scripts de corrección."""

import pytest
from pathlib import Path


class TestFixSectionStructure:
    """Tests para fix_section_structure.py"""
    
    def test_detect_missing_blank_line(self, tmp_path):
        """Debe detectar secciones sin línea en blanco antes."""
        from scripts.correction.fix_section_structure import detect_section_structure_issues
        
        content = "Paragraph text\nTitle\n====="
        issues = detect_section_structure_issues(content)
        assert len(issues) > 0
    
    def test_fix_adds_blank_line(self, tmp_path):
        """Debe agregar línea en blanco antes de título."""
        from scripts.correction.fix_section_structure import fix_section_structure
        
        content = "Paragraph\nTitle\n====="
        fixed = fix_section_structure(content)
        assert "\n\nTitle" in fixed


class TestFixTitleUnderlines:
    """Tests para fix_title_underlines.py"""
    
    def test_fix_short_underline(self):
        """Debe corregir underline corto."""
        from scripts.correction.fix_title_underlines import fix_title_underlines
        
        content = "Long Title Here\n===="
        fixed = fix_title_underlines(content)
        lines = fixed.split('\n')
        assert len(lines[1]) == len(lines[0].rstrip())


class TestFixIndentation:
    """Tests para fix_indentation_errors.py"""
    
    def test_fix_list_continuation(self):
        """Debe corregir indentación de continuación de lista."""
        from scripts.correction.fix_indentation_errors import fix_indentation
        
        content = "- Item\nContinuation"
        fixed = fix_indentation(content)
        assert "  Continuation" in fixed


class TestFixHeadingLevels:
    """Tests para fix_heading_levels.py"""
    
    def test_normalize_to_h1(self):
        """Debe normalizar el primer heading a H1."""
        from scripts.correction.fix_heading_levels import normalize_heading_levels
        
        content = "Title\n-----"  # H2
        fixed = normalize_heading_levels(content)
        assert "====" in fixed  # Cambiado a H1


class TestResolveImageRefs:
    """Tests para resolve_image_references.py"""
    
    def test_remove_template_vars(self):
        """Debe eliminar variables de template."""
        from scripts.correction.resolve_image_references import resolve_image_refs
        
        content = ".. image:: {{site.imageurl}}/img.png"
        fixed = resolve_image_refs(content, Path("."))
        assert "{{site" not in fixed
