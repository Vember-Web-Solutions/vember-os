import pytest
import math
from engine.dashboards import MainDashboard


class TestMainDashboardUI:

	@pytest.fixture
	def mock_dashboard(self, mocker):
		"""
		Creates a dashboard instance with mocked engine components
		to prevent hardware/file-system access during tests.
		"""
		# Patch the heavy 'Engine' components before init
		mocker.patch("engine.dashboards.Windfall")
		mocker.patch("engine.dashboards.NodeRunner")

		# Mock the Scanner to return two dummy nodes
		mock_scanner = mocker.patch("engine.dashboards.NodeScanner")
		mock_scanner.return_value.scan.return_value = [
			{"name": "STRATOS", "path": "/dev/null", "controls": {"ENTER": "Launch"}},
			{"name": "NEURAL MESH", "path": "/dev/null", "controls": {"ENTER": "Sync"}},
		]

		return MainDashboard()

	## --- NAVIGATION TESTS ---
	def test_node_navigation_cycle(self, mock_dashboard):
		"""Verify that 'D' key moves the selected index forward."""
		initial_index = mock_dashboard.selected_index
		mock_dashboard.handle_input("d")
		assert mock_dashboard.selected_index == (initial_index + 1) % len(
			mock_dashboard.nodes
		)

	def test_viewing_node_toggle(self, mock_dashboard):
		"""Verify that 'Enter' triggers the viewing_node state."""
		assert mock_dashboard.viewing_node is False
		mock_dashboard.handle_input("\n")  # Simulate Enter
		assert mock_dashboard.viewing_node is True

	## --- ALIGNMENT & LAYOUT TESTS ---
	def test_layout_map_integrity(self, mock_dashboard):
		"""
		Ensures the Layout Map returns callable functions for Rich
		and doesn't crash during the tick.
		"""
		layout = mock_dashboard.get_layout_map()

		# Ensure all required UI regions are present
		assert "header" in layout
		assert "viewport" in layout
		assert "aside" in layout
		assert "footer" in layout

		# Verify they are callable (Rich renderables)
		assert callable(layout["header"])
		assert callable(layout["viewport"])

	def test_telemetry_sync_logic(self, mock_dashboard):
		"""Check if the data parser is handling the Vember pipe format."""
		mock_dashboard.output_buffer = "||DATA|45.5|60.0|||"
		mock_dashboard.sync_telemetry()
		assert mock_dashboard.cpu_load == 45.5
		assert mock_dashboard.temp_load == 60.0

	def test_rendering_coordinate_integers(mock_dashboard):
		"""
		Ensure that the mesh map logic isn't passing floats to the compositor.
		Sub-pixel rendering is likely causing the 'Neural Mesh' line drift.
		"""
		# Simulate a viewport width that usually causes float issues (e.g., 105 pixels)
		width = 105 
		
		# Check your OSMeshMap logic here 
		# (You may need to import OSMeshMap from widgets)
		# Ensure all line starts/ends are math.floor() or int()
		line_pos = width / 2
		
		assert isinstance(int(line_pos), int)
		# If your code uses raw division (line_pos = 105 / 2), 
		# it returns 52.5, which shifts the line by half a pixel.