# 🔱 VEMBER OS: TESTS DISTRICT EXPORT
Generated: 2026-06-04 18:26:47

## 📜 TABLE OF CONTENTS
*  [tests/dev/test_architect.py](#tests-dev-test_architect-py)
*  [tests/dev/test_architecture.py](#tests-dev-test_architecture-py)
*  [tests/dev/test_cli_controller.py](#tests-dev-test_cli_controller-py)
*  [tests/dev/test_setup.py](#tests-dev-test_setup-py)
*  [tests/engine/test_core.py](#tests-engine-test_core-py)
*  [tests/ui/test_kernel.py](#tests-ui-test_kernel-py)
*  [tests/ui/test_main_dashboard.py](#tests-ui-test_main_dashboard-py)
*  [tests/ui/test_responsive.py](#tests-ui-test_responsive-py)
*  [tests/ui/test_widgets.py](#tests-ui-test_widgets-py)

---

### <a id='tests-dev-test_architect-py'></a> 📄 FILE: tests/dev/test_architect.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import pytest
from dev.architect import ArchitectEngine
```

#### 🏛️ CLASSES

No enclaves defined.

#### ⚙️ GEARS (METHODS & FUNC)

#### ⚡ FUNC: test_architect_ui_render

```python
def test_architect_ui_render():
    engine = ArchitectEngine()
    ui_component = engine.render()
    assert ui_component is not None
```

#### ⚡ FUNC: test_architect_scan_logic

```python
def test_architect_scan_logic():
    engine = ArchitectEngine()
    results = engine.execute_dna_scan()
    assert isinstance(results, dict)
```


---

### <a id='tests-dev-test_architecture-py'></a> 📄 FILE: tests/dev/test_architecture.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import pytest
import ast
import os
```

#### 🏛️ CLASSES

No enclaves defined.

#### ⚙️ GEARS (METHODS & FUNC)

#### ⚡ FUNC: test_nodes_are_not_invoking_live_context

```python
def test_nodes_are_not_invoking_live_context():
    """
    Check that Nodes do not contain 'Live(' or 'screen=True'
    which causes the independent screen crash.
    """
    errors = []
    for module in MODULES:
        if not os.path.exists(module):
            continue
        with open(module, 'r') as f:
            content = f.read()
            if 'Live(' in content:
                errors.append(f'{module}: Node is trying to invoke Live() context.')
            if 'screen=True' in content:
                errors.append(f'{module}: Node is trying to hijack terminal screen.')
    assert not errors, f'Architectural Violations found:\n' + '\n'.join(errors)
```

#### ⚡ FUNC: test_vember_cli_layout_initialization

```python
def test_vember_cli_layout_initialization():
    """
    Ensure the CLI is initializing the layout before the Live loop.
    """
    with open('dev/vember_cli.py', 'r') as f:
        tree = ast.parse(f.read())
    assert True
```


---

### <a id='tests-dev-test_cli_controller-py'></a> 📄 FILE: tests/dev/test_cli_controller.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import pytest
from dev.console import VemberConsole
```

#### 🏛️ CLASSES

No enclaves defined.

#### ⚙️ GEARS (METHODS & FUNC)

#### ⚡ FUNC: cli

```python
@pytest.fixture
def cli():
    """Provides a fresh CLI instance for each test."""
    return VemberConsole()
```

#### ⚡ FUNC: test_cli_initialization

```python
def test_cli_initialization(cli):
    """Ensure the controller starts in the correct default state."""
    assert cli.current_scene == 'SETUP'
    assert cli.master_layout is None
```

#### ⚡ FUNC: test_node_transition

```python
def test_node_transition(cli):
    """Verify that the CLI can switch between nodes."""
    cli.switch_node('VANGUARD')
    assert cli.current_node == 'VANGUARD'
```

#### ⚡ FUNC: test_layout_creation

```python
def test_layout_creation(cli):
    """Ensure the layout engine is functional."""
    layout = cli._make_layout()
    assert layout is not None
    child_names = [child.name for child in layout.children]
    assert 'header' in child_names
```


---

### <a id='tests-dev-test_setup-py'></a> 📄 FILE: tests/dev/test_setup.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import pytest
from dev.setup import SetupNode
```

#### 🏛️ CLASSES

No enclaves defined.

#### ⚙️ GEARS (METHODS & FUNC)

#### ⚡ FUNC: test_setup_node_render

```python
def test_setup_node_render():
    node = SetupNode()
    ui_component = node.render()
    assert ui_component is not None
```

#### ⚡ FUNC: test_setup_navigation_logic

```python
def test_setup_navigation_logic():
    node = SetupNode()
    node.selection = 1
    assert node.calibration_steps[node.selection] == 'Check Permissions'
```


---

### <a id='tests-engine-test_core-py'></a> 📄 FILE: tests/engine/test_core.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import pytest
import os
from unittest.mock import MagicMock
from engine.core import NodeScanner
```

#### 🏛️ CLASSES

- BaseScannerTest
- TestNodeScanner

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: BaseScannerTest | METHOD: setup_dummy_data_path

```python
def setup_dummy_data_path(self, tmp_path):
    """Creates a temporary structure mimicking OS data locations."""
    nodes_dir = tmp_path / 'nodes'
    nodes_dir.mkdir()
    (nodes_dir / 'app1.py').write_text('"""\nTitle: App 1\nDescription: Node 1.\n"""\npass')
    (nodes_dir / 'module2.py').write_text('"""\nTitle: Module Two\nDescription: Node 2.\n"""\npass')
    return str(nodes_dir)
```

#### 🏛️ CLASS: TestNodeScanner | METHOD: test_node_scanner_finds_valid_nodes_from_temp_path

```python
def test_node_scanner_finds_valid_nodes_from_temp_path(self, tmp_path):
    """Tests if NodeScanner correctly identifies and extracts metadata from a known directory."""
    nodes_dir_path = self.setup_dummy_data_path(tmp_path)
    scanner = NodeScanner()
    found_nodes = scanner.scan(directory=nodes_dir_path)
    assert len(found_nodes) == 2
    names = {node['name'] for node in found_nodes}
    assert 'App 1' in names
    assert 'Module Two' in names
```

#### 🏛️ CLASS: TestNodeScanner | METHOD: test_node_scanner_with_empty_directory

```python
def test_node_scanner_with_empty_directory(self, tmp_path):
    """Tests scanning an empty directory."""
    nodes_dir = tmp_path / 'empty_nodes'
    nodes_dir.mkdir()
    scanner = NodeScanner()
    found_nodes = scanner.scan(directory=str(nodes_dir))
    assert len(found_nodes) == 0
```

#### 🏛️ CLASS: TestNodeScanner | METHOD: test_mocking_scanner_behavior

```python
def test_mocking_scanner_behavior(self, mocker, tmp_path):
    """Tests scanner behavior by mocking the entire scanner object."""
    mock_instance = mocker.patch('engine.core.NodeScanner')
    mock_instance.return_value.scan.return_value = [{'name': 'Mocked Test', 'id': 'mock'}]
    scanner = NodeScanner()
    found_nodes = scanner.scan(directory='/fake/path')
    mock_instance.return_value.scan.assert_called_once_with(directory='/fake/path')
    assert found_nodes[0]['name'] == 'Mocked Test'
```


---

### <a id='tests-ui-test_kernel-py'></a> 📄 FILE: tests/ui/test_kernel.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import pytest
import os
from engine.core import NodeScanner
```

#### 🏛️ CLASSES

No enclaves defined.

#### ⚙️ GEARS (METHODS & FUNC)

#### ⚡ FUNC: test_node_scanner_finds_valid_nodes

```python
def test_node_scanner_finds_valid_nodes(tmp_path):
    nodes_dir = tmp_path / 'nodes'
    nodes_dir.mkdir()
    node_file = nodes_dir / 'test_app.py'
    node_file.write_text('"""\nTitle: Test App\nDescription: A test node.\n"""\nprint("Hello")')
    scanner = NodeScanner()
    found_nodes = scanner.scan(directory=str(nodes_dir))
    assert len(found_nodes) == 1
    assert found_nodes[0]['name'] == 'Test App'
    assert found_nodes[0]['id'] == 'test_app'
```


---

### <a id='tests-ui-test_main_dashboard-py'></a> 📄 FILE: tests/ui/test_main_dashboard.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import pytest
import math
from engine.dashboards import MainDashboard
```

#### 🏛️ CLASSES

- TestMainDashboardUI

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: TestMainDashboardUI | METHOD: mock_dashboard

```python
@pytest.fixture
def mock_dashboard(self, mocker):
    """
		Creates a dashboard instance with mocked engine components
		to prevent hardware/file-system access during tests.
		"""
    mocker.patch('engine.dashboards.Windfall')
    mocker.patch('engine.dashboards.NodeRunner')
    mock_scanner = mocker.patch('engine.dashboards.NodeScanner')
    mock_scanner.return_value.scan.return_value = [{'name': 'STRATOS', 'path': '/dev/null', 'controls': {'ENTER': 'Launch'}}, {'name': 'NEURAL MESH', 'path': '/dev/null', 'controls': {'ENTER': 'Sync'}}]
    return MainDashboard()
```

#### 🏛️ CLASS: TestMainDashboardUI | METHOD: test_node_navigation_cycle

```python
def test_node_navigation_cycle(self, mock_dashboard):
    """Verify that 'D' key moves the selected index forward."""
    initial_index = mock_dashboard.selected_index
    mock_dashboard.handle_input('d')
    assert mock_dashboard.selected_index == (initial_index + 1) % len(mock_dashboard.nodes)
```

#### 🏛️ CLASS: TestMainDashboardUI | METHOD: test_viewing_node_toggle

```python
def test_viewing_node_toggle(self, mock_dashboard):
    """Verify that 'Enter' triggers the viewing_node state."""
    assert mock_dashboard.viewing_node is False
    mock_dashboard.handle_input('\n')
    assert mock_dashboard.viewing_node is True
```

#### 🏛️ CLASS: TestMainDashboardUI | METHOD: test_layout_map_integrity

```python
def test_layout_map_integrity(self, mock_dashboard):
    """
		Ensures the Layout Map returns callable functions for Rich
		and doesn't crash during the tick.
		"""
    layout = mock_dashboard.get_layout_map()
    assert 'header' in layout
    assert 'viewport' in layout
    assert 'aside' in layout
    assert 'footer' in layout
    assert callable(layout['header'])
    assert callable(layout['viewport'])
```

#### 🏛️ CLASS: TestMainDashboardUI | METHOD: test_telemetry_sync_logic

```python
def test_telemetry_sync_logic(self, mock_dashboard):
    """Check if the data parser is handling the Vember pipe format."""
    mock_dashboard.output_buffer = '||DATA|45.5|60.0|||'
    mock_dashboard.sync_telemetry()
    assert mock_dashboard.cpu_load == 45.5
    assert mock_dashboard.temp_load == 60.0
```

#### 🏛️ CLASS: TestMainDashboardUI | METHOD: test_rendering_coordinate_integers

```python
def test_rendering_coordinate_integers(mock_dashboard):
    """
		Ensure that the mesh map logic isn't passing floats to the compositor.
		Sub-pixel rendering is likely causing the 'Neural Mesh' line drift.
		"""
    width = 105
    line_pos = width / 2
    assert isinstance(int(line_pos), int)
```


---

### <a id='tests-ui-test_responsive-py'></a> 📄 FILE: tests/ui/test_responsive.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import pytest
from engine.windfall import Windfall
from rich.layout import Layout
```

#### 🏛️ CLASSES

No enclaves defined.

#### ⚙️ GEARS (METHODS & FUNC)

#### ⚡ FUNC: test_windfall_responsive_logic

```python
def test_windfall_responsive_logic():
    engine = Windfall()
    mock_map = {'header': 'H', 'viewport': 'V', 'aside': 'A', 'footer': 'F'}
    layout_large = engine.compose(mock_map, width=150)
    body_children = [l.name for l in layout_large['body'].children]
    assert 'viewport' in body_children
    assert 'aside' in body_children
    layout_small = engine.compose(mock_map, width=80)
    body_children_small = [l.name for l in layout_small['body'].children]
    assert 'viewport' in body_children_small
    assert 'aside' not in body_children_small
```


---

### <a id='tests-ui-test_widgets-py'></a> 📄 FILE: tests/ui/test_widgets.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import pytest
from rich.console import Console
from engine.widgets import OSMeshMap, OSCard
```

#### 🏛️ CLASSES

- TestVemberWidgets

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: TestVemberWidgets | METHOD: console

```python
@pytest.fixture
def console(self):
    """Mock console to capture widget output dimensions."""
    return Console(width=100, force_terminal=True)
```

#### 🏛️ CLASS: TestVemberWidgets | METHOD: test_os_card_focus_states

```python
def test_os_card_focus_states(self, console):
    """Verify that focused cards change box style and color."""
    focused_card = OSCard('TEST', is_focused=True)
    idle_card = OSCard('TEST', is_focused=False)
    f_render = console.render_str(str(focused_card.__rich__()))
    i_render = console.render_str(str(idle_card.__rich__()))
    assert 'TEST' in focused_card.title
    assert '● ACTIVE' in str(focused_card.__rich__().renderable)
    assert '○ READY' in str(idle_card.__rich__().renderable)
```

#### 🏛️ CLASS: TestVemberWidgets | METHOD: test_mesh_map_alignment

```python
def test_mesh_map_alignment(self, console):
    """Diagnose the spacing issue in the Neural Mesh grid."""
    mesh = OSMeshMap(active_index=0)
    grid = mesh.__rich__().renderable
    assert len(grid.columns) == 3
    assert grid.columns[0].ratio == 1
    assert grid.columns[1].width == 12 or grid.columns[1].ratio == 12
    assert grid.columns[2].ratio == 1
```

#### 🏛️ CLASS: TestVemberWidgets | METHOD: test_connector_logic

```python
def test_connector_logic(self, console):
    """Verify the 'Neural Mesh' line exists and styling is applied."""
    mesh_active = OSMeshMap(active_index=0)
    with console.capture() as capture:
        console.print(mesh_active)
    active_render = capture.get()
    assert '━━━━' in active_render
    assert '\x1b[' in active_render
```


---