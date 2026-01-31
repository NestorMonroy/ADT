"""Tests para regex_patterns.py"""

import pytest
from scripts.lib.regex_patterns import (
    match_title_underline,
    is_valid_underline,
    get_indentation_level,
    extract_template_variables,
    HEADING_CHARS,
)


class TestTitleUnderline:
    """Tests para detección de títulos con underline."""
    
    def test_match_single_title(self):
        """Debe encontrar un título simple."""
        text = "Title\n====="
        matches = match_title_underline(text)
        assert len(matches) == 1
        assert matches[0][0] == "Title"
        assert matches[0][1] == "="
    
    def test_match_multiple_titles(self):
        """Debe encontrar múltiples títulos."""
        text = "Title 1\n=======\n\nTitle 2\n-------"
        matches = match_title_underline(text)
        assert len(matches) == 2
    
    def test_no_match_without_underline(self):
        """No debe encontrar títulos sin underline."""
        text = "Just text\nMore text"
        matches = match_title_underline(text)
        assert len(matches) == 0


class TestValidUnderline:
    """Tests para validación de underlines."""
    
    @pytest.mark.parametrize("line,expected", [
        ("======", True),
        ("------", True),
        ("~~~~~~", True),
        ("^^^^^^", True),
        ("===", True),
        ("--", False),  # Muy corto
        ("abc", False),
        ("==-==", False),  # Caracteres mezclados
        ("", False),
    ])
    def test_is_valid_underline(self, line, expected):
        """Debe validar correctamente underlines."""
        assert is_valid_underline(line) == expected


class TestIndentation:
    """Tests para detección de indentación."""
    
    @pytest.mark.parametrize("line,expected", [
        ("text", 0),
        ("  text", 2),
        ("    text", 4),
        ("        text", 8),
    ])
    def test_get_indentation_level(self, line, expected):
        """Debe detectar nivel de indentación."""
        assert get_indentation_level(line) == expected


class TestTemplateVariables:
    """Tests para variables de template."""
    
    def test_find_single_variable(self):
        """Debe encontrar una variable."""
        text = "Image at {{site.imageurl}}/img.png"
        vars_found = extract_template_variables(text)
        assert len(vars_found) == 1
        assert vars_found[0] == "imageurl"
    
    def test_find_multiple_variables(self):
        """Debe encontrar múltiples variables."""
        text = "{{site.baseurl}}/path and {{site.url}}/other"
        vars_found = extract_template_variables(text)
        assert len(vars_found) == 2


class TestHeadingLevels:
    """Tests para mapeo de niveles de heading."""
    
    def test_heading_chars_mapping(self):
        """Debe tener mapeo de caracteres."""
        assert HEADING_CHARS[1] == '='
        assert HEADING_CHARS[2] == '-'
        assert HEADING_CHARS[3] == '~'
