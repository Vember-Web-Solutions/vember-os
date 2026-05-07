import pytest
import os
from engine.core import NodeScanner


def test_node_scanner_finds_valid_nodes(tmp_path):
    # ARRANGE: Create a temporary 'nodes' directory and a dummy node file
    nodes_dir = tmp_path / "nodes"
    nodes_dir.mkdir()
    node_file = nodes_dir / "test_app.py"
    node_file.write_text(
        '"""\nTitle: Test App\nDescription: A test node.\n"""\nprint("Hello")'
    )

    scanner = NodeScanner()

    # ACT: Scan the temporary directory
    found_nodes = scanner.scan(directory=str(nodes_dir))

    # ASSERT: Verify the node was identified and metadata extracted
    assert len(found_nodes) == 1
    assert found_nodes[0]["name"] == "Test App"
    assert found_nodes[0]["id"] == "test_app"
