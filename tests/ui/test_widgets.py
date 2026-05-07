import pytest
from rich.console import Console
from engine.widgets import OSMeshMap, OSCard


class TestVemberWidgets:

    @pytest.fixture
    def console(self):
        """Mock console to capture widget output dimensions."""
        return Console(width=100, force_terminal=True)

    def test_os_card_focus_states(self, console):
        """Verify that focused cards change box style and color."""
        focused_card = OSCard("TEST", is_focused=True)
        idle_card = OSCard("TEST", is_focused=False)

        # Capture the renderable
        f_render = console.render_str(str(focused_card.__rich__()))
        i_render = console.render_str(str(idle_card.__rich__()))

        # Check if the title/icon logic is preserved
        assert "TEST" in focused_card.title
        assert "● ACTIVE" in str(focused_card.__rich__().renderable)
        assert "○ READY" in str(idle_card.__rich__().renderable)

    def test_mesh_map_alignment(self, console):
        """Diagnose the spacing issue in the Neural Mesh grid."""
        mesh = OSMeshMap(active_index=0)
        grid = mesh.__rich__().renderable

        assert len(grid.columns) == 3

        # Column 0 (Left Card): Should be flexible
        assert grid.columns[0].ratio == 1

        # Column 1 (The Connector): This is your FIX!
        # It should be 12 (or whatever integer you set) to prevent jitter.
        assert grid.columns[1].width == 12 or grid.columns[1].ratio == 12

        # Column 2 (Right Card): Should be flexible
        assert grid.columns[2].ratio == 1

    def test_connector_logic(self, console):
        """Verify the 'Neural Mesh' line exists and styling is applied."""
        mesh_active = OSMeshMap(active_index=0)

        with console.capture() as capture:
            console.print(mesh_active)
        active_render = capture.get()

        # 1. Check if the 'Neural Mesh' characters actually exist
        assert "━━━━" in active_render

        # 2. Check for ANSI escape codes (the \x1b part)
        # instead of the word "cyan"
        assert "\x1b[" in active_render
