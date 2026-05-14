import pytest
import os
from unittest.mock import MagicMock
from engine.core import NodeScanner


class BaseScannerTest:
    """Base class for scanner tests providing common setup utilities."""

    def setup_dummy_data_path(self, tmp_path):
        """Creates a temporary structure mimicking OS data locations."""
        nodes_dir = tmp_path / "nodes"
        nodes_dir.mkdir()
        # Simulate a couple of files for testing purposes
        (nodes_dir / "app1.py").write_text(
            '"""\nTitle: App 1\nDescription: Node 1.\n"""\npass'
        )
        (nodes_dir / "module2.py").write_text(
            '"""\nTitle: Module Two\nDescription: Node 2.\n"""\npass'
        )
        return str(nodes_dir)


class TestNodeScanner:
    """Tests functionality related to NodeScanner, inheriting setup from BaseScannerTest."""

    # Since we are sticking to pytest fixtures, we keep this method structure
    # as it correctly uses the fixture dependency injection pattern.
    def test_node_scanner_finds_valid_nodes_from_temp_path(self, tmp_path):
        """Tests if NodeScanner correctly identifies and extracts metadata from a known directory."""
        # ARRANGE: Setup temporary directory
        nodes_dir_path = self.setup_dummy_data_path(tmp_path)

        scanner = NodeScanner()

        # ACT: Scan the temporary directory
        found_nodes = scanner.scan(directory=nodes_dir_path)

        # ASSERT: Verify the nodes were identified
        assert len(found_nodes) == 2

        # Simple check to ensure structure is maintained
        names = {node["name"] for node in found_nodes}
        assert "App 1" in names
        assert "Module Two" in names

    def test_node_scanner_with_empty_directory(self, tmp_path):
        """Tests scanning an empty directory."""
        nodes_dir = tmp_path / "empty_nodes"
        nodes_dir.mkdir()

        scanner = NodeScanner()
        found_nodes = scanner.scan(directory=str(nodes_dir))

        assert len(found_nodes) == 0

    # --- REVERTING TO THE ORIGINAL MOCKING STYLE FOR STABILITY ---
    # The complexity of using parametrize decorators to mock class instantiation
    # while maintaining fixture compatibility is too high.
    # We revert to the original, functional fixture-based mocking shown in the
    # first prompt, which is the standard pattern when using 'mocker'.
    def test_mocking_scanner_behavior(self, mocker, tmp_path):
        """Tests scanner behavior by mocking the entire scanner object."""
        # Use mocker.patch instead of @patch decorator
        mock_instance = mocker.patch("engine.core.NodeScanner")
        mock_instance.return_value.scan.return_value = [
            {"name": "Mocked Test", "id": "mock"}
        ]

        scanner = NodeScanner()  # This will now use the mocked constructor/instance
        found_nodes = scanner.scan(directory="/fake/path")

        # Ensure the mocked method was called
        mock_instance.return_value.scan.assert_called_once_with(directory="/fake/path")
        assert found_nodes[0]["name"] == "Mocked Test"
