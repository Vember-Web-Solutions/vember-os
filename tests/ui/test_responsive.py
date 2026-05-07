import pytest
from engine.windfall import Windfall
from rich.layout import Layout


def test_windfall_responsive_logic():
    engine = Windfall()
    mock_map = {"header": "H", "viewport": "V", "aside": "A", "footer": "F"}

    # 🔱 TEST LARGE SCREEN
    layout_large = engine.compose(mock_map, width=150)
    # Check the 'body' layout's children directly
    body_children = [l.name for l in layout_large["body"].children]

    assert "viewport" in body_children
    assert "aside" in body_children

    # 🔱 TEST SMALL SCREEN
    layout_small = engine.compose(mock_map, width=80)
    body_children_small = [l.name for l in layout_small["body"].children]

    assert "viewport" in body_children_small
    assert "aside" not in body_children_small  # The true test of responsiveness
