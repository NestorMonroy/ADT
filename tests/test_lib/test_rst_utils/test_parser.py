"""Tests para parser.py"""

import pytest
from scripts.lib.rst_utils.parser import parse_content, parse_heading
from scripts.lib.rst_utils.rst_types import BlockType


def test_parse_simple_heading():
    """Debe parsear un heading simple."""
    content = "Title\n====="
    blocks = parse_content(content)
    assert len(blocks) >= 1
    assert blocks[0].type == BlockType.HEADING


def test_parse_multiple_headings():
    """Debe parsear múltiples headings."""
    content = "Title 1\n=======\n\nTitle 2\n-------"
    blocks = parse_content(content)
    headings = [b for b in blocks if b.type == BlockType.HEADING]
    assert len(headings) == 2


def test_parse_list_items():
    """Debe parsear items de lista."""
    content = "- Item 1\n- Item 2"
    blocks = parse_content(content)
    lists = [b for b in blocks if b.type == BlockType.LIST]
    assert len(lists) == 2


def test_parse_directive():
    """Debe parsear directivas."""
    content = ".. code-block:: python\n\n   code"
    blocks = parse_content(content)
    directives = [b for b in blocks if b.type == BlockType.DIRECTIVE]
    assert len(directives) >= 1
