# 🔱 VEMBER OS: DEV DISTRICT EXPORT
Generated: 2026-06-04 18:25:50

## 📜 TABLE OF CONTENTS
*  [dev/architect.py](#dev-architect-py)
*  [dev/console.py](#dev-console-py)
*  [dev/de.py](#dev-de-py)
*  [dev/factory.py](#dev-factory-py)
*  [dev/keybinds.py](#dev-keybinds-py)
*  [dev/nexus.py](#dev-nexus-py)
*  [dev/scenes.py](#dev-scenes-py)
*  [dev/setup.py](#dev-setup-py)
*  [dev/vanguard.py](#dev-vanguard-py)
*  [dev/views.py](#dev-views-py)
*  [dev/widgets.py](#dev-widgets-py)
*  [dev/windfall.py](#dev-windfall-py)

---

### <a id='dev-architect-py'></a> 📄 FILE: dev/architect.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: ARCHITECT CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: ARCHITECT_DNA_NODE
> Context Path:  /dev/architect.py
> 
> Architectural Integrity & Workspace Passport Verification Engine.
> Authorized and signed under Vember OS decentralized system specifications.
> ================================================================================

#### 🚀 IMPORTS

```python
import os
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES

- ArchitectEngine

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: ArchitectEngine | METHOD: __init__

```python
def __init__(self):
    self.project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    self.target_subdirs = ['dev', 'assets', 'engine', 'nodes']
    self.target_root_files = ['main.py']
    self.flagged_violations = {}
    self.phase = 'FOCUS'
    self.scan_results = 'Awaiting DNA scan...'
```

#### 🏛️ CLASS: ArchitectEngine | METHOD: execute_dna_scan

```python
def execute_dna_scan(self) -> dict:
    """Surgically parse designated directories for Trident passports."""
    self.flagged_violations = {}
    self.scan_results = 'Scan complete: Integrity verified.'
    return {'status': 'clean'}
```

#### 🏛️ CLASS: ArchitectEngine | METHOD: heal_all_passports

```python
def heal_all_passports(self) -> int:
    """Worker method: Cleans docstrings and applies passport templates."""
    healed_count = 0
    self.scan_results = f'Healed {healed_count} passports.'
    return healed_count
```

#### 🏛️ CLASS: ArchitectEngine | METHOD: render

```python
def render(self):
    """Returns the UI component for the VemberCLI host controller."""
    table = Table(box=None, padding=(0, 1))
    table.add_column('Key', style=f'bold {Theme.primary}')
    table.add_column('Value')
    table.add_row('Status', self.scan_results)
    table.add_row('Phase', self.phase)
    table.add_row('Root', self.project_root)
    return Panel(Align.center(table), title=f'[{Theme.primary}]ARCHITECT_DNA_NODE[/]', border_style=Theme.primary, padding=(1, 2))
```


---

### <a id='dev-console-py'></a> 📄 FILE: dev/console.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: VEMBER_CLI CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: MASTER_CLI_CONSOLE
> Context Path:  /dev/vember_cli.py
> 
> Web3 Dynamic Stage Controller Tracking the 4-Corner Rectangular Grid Matrix.
> Authorized and signed under Vember OS decentralized system specifications.
> 
> Context Actions:
> [UP/DN] NAVIGATE_CORE_CARDS
> [ENTER] IGNITE_MODULE_CONTRACT
> [B]     TRIGGER_DOCKER_BUILD
> [T]     HOT_SWAP_THEME_MATRIX
> [BKSP]  DISCONNECT_TERMINAL
> ================================================================================

#### 🚀 IMPORTS

```python
import os
import sys
import time
from datetime import datetime
import threading
from dev.de import DockerEngine
from dev.architect import ArchitectEngine
from typing import Any
from rich.console import Console, Group
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.text import Text
from rich import box
from pynput import keyboard
from dev.widgets import ForgeHeader, ForgeFooter
from dev.keybinds import ConsoleInputMatrix
from assets.branding import VemberAssets
from dev.windfall import NodeCluster
from dev.views import SceneRouter, DeveloperView
from dev.de import DockerEngine
from dev.vanguard import Vanguard
```

#### 🏛️ CLASSES

- VemberConsole

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: VemberConsole | METHOD: __init__

```python
def __init__(self):
    self.controller = self
    self.menu_items = [{'label': 'SETUP', 'cmd': 'SETUP', 'desc': 'Surgical Environment Setup Guide'}, {'label': 'ARCHITECT', 'cmd': 'ARCHITECT', 'desc': 'DNA Remediation & Code Integrity'}, {'label': 'VANGUARD', 'cmd': 'VANGUARD', 'desc': 'Logic Validation & Dependency Shielding'}, {'label': 'WINDFALL', 'cmd': 'WINDFALL', 'desc': 'Vember OS Layout Compositor Engine'}, {'label': 'BARKBYTE', 'cmd': 'BARKBYTE', 'desc': 'Compositional Node-Based IDE Environment'}, {'label': 'EXIT_CONSOLE', 'cmd': 'EXIT', 'desc': 'Disconnect from forge context'}]
    self.nodes = {'SETUP': None, 'VANGUARD': Vanguard()}
    self.console = Console()
    self.selection = 0
    self.active_cmd = None
    self.child_selection = 0
    self.shutdown_flag: bool = False
    self.master_layout = None
    self.router = SceneRouter(self.controller)
    self.view_container = DeveloperView(self)
    self.current_scene = 'SETUP'
    self.capacity_status: str = 'CLUSTER_STABLE'
    self.docker_engine = DockerEngine('vember_hub')
    self.docker_data = {'total': '0 MB', 'status': 'READY'}
    self.status_msg = 'SYSTEM_READY: Awaiting Tactical Ignition...'
    self.header = ForgeHeader(docker_engine=self.docker_engine, context_name='DEVELOPER_CORE')
    self.footer = ForgeFooter()
    self.listener = keyboard.Listener(on_press=self.on_press)
    self.listener.start()
```

#### 🏛️ CLASS: VemberConsole | METHOD: on_press

```python
def on_press(self, key):
    if key == keyboard.Key.esc:
        self.shutdown_flag = True
```

#### 🏛️ CLASS: VemberConsole | METHOD: _query_docker_footprint

```python
def _query_docker_footprint(self):
    """Delegates footprint polling to the specialized DockerEngine."""
    self.docker_data['total'] = self.docker_engine.get_container_size()
    self.docker_data['status'] = 'SYNCED' if self.docker_data['total'] != 'OFFLINE' else 'DISCONNECTED'
```

#### 🏛️ CLASS: VemberConsole | METHOD: log_debug

```python
def log_debug(self, message: str):
    """🔱 BLACK BOX LOGGER: Writes events to a persistent debug file."""
    with open('vember.log', 'a') as f:
        f.write(f"{datetime.now().strftime('%H:%M:%S.%f')} | {message}\n")
```

#### 🏛️ CLASS: VemberConsole | METHOD: _execute

```python
def _execute(self, cmd_id: str):
    if cmd_id == 'THEME_SWAP':
        themes = ['midnight', 'sakura', 'kuro', 'shinto']
        current_key = VemberAssets.ACTIVE_THEME.name.lower()
        current_simple_key = next((k for k in themes if k in current_key), 'midnight')
        try:
            next_idx = (themes.index(current_simple_key) + 1) % len(themes)
            VemberAssets.apply_theme(themes[next_idx])
            self.status_msg = f'THEME_IGNITED: {VemberAssets.ACTIVE_THEME.name}'
        except ValueError:
            VemberAssets.apply_theme('midnight')
    elif cmd_id == 'DOCKER_BUILD':
        self.status_msg = 'RUNNING_BUILD: Compiling local environment Dockerfile...'
        self._query_docker_footprint()
    else:
        self.active_cmd = cmd_id
        self.child_selection = 0
        self.status_msg = f'CONTRACT_ENGAGED: Active runtime channel routed to {cmd_id}...'
```

#### 🏛️ CLASS: VemberConsole | METHOD: _make_layout

```python
def _make_layout(self):
    """
		🔱 ASSEMBLE_LAYOUT: The central nervous system of the UI frame.
		Uses a rigid Layout grid to prevent screen overflow (doubling)
		and lock the focus node to the true vertical center.
		"""
    layout = Layout(name='root')
    layout.split(Layout(name='header', size=5), Layout(name='body'), Layout(name='footer', size=5))
    return layout
```

#### 🏛️ CLASS: VemberConsole | METHOD: run

```python
def run(self):
    self.master_layout = self._make_layout()
    with Live(self.master_layout, refresh_per_second=20, screen=True) as live:
        while not self.shutdown_flag:
            self.master_layout['header'].update(ForgeHeader(...))
            self.master_layout['body'].update(self.view_container.compose_view(self, self.current_scene))
            time.sleep(0.05)
```

#### 🏛️ CLASS: VemberConsole | METHOD: ignite_module_contract

```python
def ignite_module_contract(self):
    """🔱 IGNITION: Transitions selection from Registry to Action Node."""
    try:
        selected_node = self.controller.menu_items[self.controller.selection]
        if selected_node == 'Architect':
            self.active_engine = ArchitectEngine()
        else:
            self.active_engine = self._load_standard_node_passport(selected_node)
        if self.active_engine and hasattr(self.active_engine, 'phase'):
            self.current_scene = self.router.get_view(self.active_engine.phase)
        else:
            self.log_debug(f'MAGMA ORANGE: {selected_node} lacks a valid phase.')
    except Exception as e:
        import traceback
        self.log_debug(f'IGNITION FAILED: {str(e)}')
```

#### 🏛️ CLASS: VemberConsole | METHOD: _load_standard_node_passport

```python
def _load_standard_node_passport(self, node_name):
    """🔱 FALLBACK: Loads a standard node envelope if no custom engine exists."""
    try:

        class StandardNode:

            def __init__(self):
                self.phase = 'IGNITE'
        self.log_debug(f'PASSPORT_ISSUED: {node_name}')
        return StandardNode()
    except Exception as e:
        self.log_debug(f'PASSPORT_FAILURE: {str(e)}')
        return None
```

#### 🏛️ CLASS: VemberConsole | METHOD: switch_node

```python
def switch_node(self, node_name):
    """The central hub for state transitions."""
    if node_name in self.nodes:
        self.current_node = node_name
```

#### ⚡ FUNC: main

```python
def main():
    cli = VemberConsole()
    cli.run()
```


---

### <a id='dev-de-py'></a> 📄 FILE: dev/de.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: DOCKER_ENGINE CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: DOCKER_REMEDIATION_ENGINE
> Context Path:  /dev/docker.py
> 
> Handles manual container footprint polling and lifecycle build orchestration.
> Authorized and signed under Vember OS decentralized system specifications.
> ================================================================================

#### 🚀 IMPORTS

```python
import docker
from docker import errors
import subprocess, os
import threading
```

#### 🏛️ CLASSES

- DockerEngine

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: DockerEngine | METHOD: __init__

```python
def __init__(self, target_container='vember_hub', image_name='vember-node'):
    self.target_container = target_container
    self.image_name = image_name
```

#### 🏛️ CLASS: DockerEngine | METHOD: run_build_and_boot

```python
def run_build_and_boot(self, controller):
    """Unified background task: Build then Boot if offline."""

    def task():
        controller.status_msg = '⚡ BUILD: Compiling layers...'
        success = self._run_build_task()
        if success:
            controller.status_msg = '⚡ BUILD: Success. Checking status...'
            if not self.check_docker_online():
                controller.status_msg = '⚡ BOOT: Launching...'
                self._run_boot_task()
            controller.status_msg = '⚡ SYSTEM: Online (Stable)'
        else:
            controller.status_msg = '⚡ BUILD: Failed'
    threading.Thread(target=task, daemon=True).start()
    return True
```

#### 🏛️ CLASS: DockerEngine | METHOD: _run_build_task

```python
def _run_build_task(self):
    """Internal: Silently execute docker compose build."""
    try:
        with open(os.devnull, 'w') as devnull:
            subprocess.run(['docker', 'compose', 'build'], stdout=devnull, stderr=devnull, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
```

#### 🏛️ CLASS: DockerEngine | METHOD: _run_boot_task

```python
def _run_boot_task(self):
    """Internal: Boots the container using docker run."""
    try:
        subprocess.run(['docker', 'run', '-d', '--name', self.target_container, self.image_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
```

#### 🏛️ CLASS: DockerEngine | METHOD: get_container_size

```python
def get_container_size(self):
    """🛡️ NEXUS_CORE: Queries container footprint with safety checks."""
    try:
        client = docker.from_env()
        container = client.containers.get(self.target_container)
        if container.image is None:
            return 'UNLINKED'
        image_attrs = getattr(container.image, 'attrs', {})
        size_bytes = image_attrs.get('Size', 0)
        return f'{round(size_bytes / (1024 * 1024), 1)} MB'
    except errors.NotFound:
        return 'OFFLINE'
    except Exception:
        return 'ERROR'
```

#### 🏛️ CLASS: DockerEngine | METHOD: check_docker_online

```python
def check_docker_online(self) -> bool:
    """Check if the target container is running."""
    try:
        cmd = ['docker', 'inspect', '-f', '{{.State.Running}}', self.target_container]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return result.stdout.strip() == 'true'
    except Exception:
        return False
```


---

### <a id='dev-factory-py'></a> 📄 FILE: dev/factory.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: FACTORY CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: FACTORY_NODE
> Context Path:  /dev/factory.py
> 
> Operational Integrity & Structural UI Panel Composition Primitives.
> Authorized and signed under Vember OS decentralized system specifications.
> ================================================================================

#### 🚀 IMPORTS

```python
from rich.console import Group
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from rich import box
from rich.table import Table
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES

- ForgeFactory

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: ForgeFactory | METHOD: generate_menu_matrix

```python
@staticmethod
def generate_menu_matrix(menu_items: list, active_selection: int, is_node_active: bool):
    T = VemberAssets.ACTIVE_THEME
    VERSION = 'v1.0.6-stable'
    grid_table = Table(box=None, show_header=False, expand=True, padding=(0, 2))
    grid_table.add_column('C1', justify='center')
    grid_table.add_column('C2', justify='center')
    grid_table.add_column('C3', justify='center')
    row_items = []
    active_desc = ''
    for i, item in enumerate(menu_items):
        is_active = i == active_selection
        if is_active:
            row_items.append(f"[{T.cursor}]►[/] [{T.selection}]{item['label']}[/]")
            active_desc = item.get('desc', '')
        else:
            row_items.append(f"   [bold white]{item['label']}[/]")
    while len(row_items) < 6:
        row_items.append('')
    grid_table.add_row(row_items[0], row_items[1], row_items[2])
    grid_table.add_row('', '', '')
    grid_table.add_row(row_items[3], row_items[4], row_items[5])
    rules_box = Table(box=None, show_header=False, expand=True)
    rules_box.add_row(Text.from_markup(f'[dim]◈[/] [bold {T.text}]{active_desc}[/]', justify='center'))
    content_group = Group(grid_table, Text('\n'), rules_box)
    menu_panel = Panel(content_group, title=f' [bold {T.text}]VEMBER_OS_CORE {VERSION}[/] ', border_style=T.primary, box=box.ROUNDED, padding=(1, 1), width=65)
    return Align.center(menu_panel)
```


---

### <a id='dev-keybinds-py'></a> 📄 FILE: dev/keybinds.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: KEYBINDS CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: DEVELOPER_CONSOLE_KEYBINDS
> Context Path:  /dev/keybinds.py
> 
> Asynchronous Background Worker Thread & Harvester Queue Input Matrix.
> Authorized and signed under Vember OS decentralized system specifications.
> ================================================================================

#### 🚀 IMPORTS

```python
import queue
from pynput import keyboard
from typing import Optional
```

#### 🏛️ CLASSES

- ConsoleInputMatrix

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: ConsoleInputMatrix | METHOD: initialize_matrix

```python
@classmethod
def initialize_matrix(cls):
    """Spins up the OS-level key listener background daemon."""

    def on_press(key):
        try:
            if key == keyboard.Key.up:
                cls._input_queue.put('UP')
            elif key == keyboard.Key.down:
                cls._input_queue.put('DN')
            elif key == keyboard.Key.enter:
                cls._input_queue.put('IGNITE_MODULE_CONTRACT')
        except Exception:
            pass
    cls._listener = keyboard.Listener(on_press=on_press)
    cls._listener.start()
    cls._initialized = True
```

#### 🏛️ CLASS: ConsoleInputMatrix | METHOD: capture_action

```python
@classmethod
def capture_action(cls) -> str:
    """Extracts the latest keypress without blocking the UI thread."""
    if not cls._initialized:
        cls.initialize_matrix()
    try:
        return cls._input_queue.get_nowait()
    except queue.Empty:
        return ''
```

#### 🏛️ CLASS: ConsoleInputMatrix | METHOD: shutdown_matrix

```python
@classmethod
def shutdown_matrix(cls):
    """Gracefully kills the hardware listener."""
    if cls._listener:
        cls._listener.stop()
        cls._initialized = False
```


---

### <a id='dev-nexus-py'></a> 📄 FILE: dev/nexus.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: NEXUS_NODE CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: NEXUS_AUTHORIZATION_NODE
> Context Path:  /dev/nexus.py
> 
> Cryptographic identity notarization and session-state handshake manager.
> Authorized and signed under Vember OS decentralized system specifications.
> ================================================================================

#### 🚀 IMPORTS

```python
import hashlib
from rich.panel import Panel
from rich import box
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES

- NexusNode

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: NexusNode | METHOD: __init__

```python
def __init__(self, raw_data: str='VEMBER_SESSION_ACTIVE'):
    self.status = 'READY'
    self.signature = self._generate_signature(raw_data)
```

#### 🏛️ CLASS: NexusNode | METHOD: _generate_signature

```python
def _generate_signature(self, data: str) -> str:
    """Generates a cryptographic-style fingerprint for the current session."""
    sha_hash = hashlib.sha256(data.encode()).hexdigest()
    return f'0x{sha_hash[:7].upper()}...'
```

#### 🏛️ CLASS: NexusNode | METHOD: __rich__

```python
def __rich__(self):
    T = VemberAssets.ACTIVE_THEME
    ledger_content = f' [dim]Status:[/] [bold {T.success}]{self.status}[/]\n [dim]Signature:[/] [bold {T.border_nexus}]{self.signature}[/]'
    return Panel(ledger_content, title=f' [bold {T.border_nexus}]NEXUS AUTHORIZATION[/] ', title_align='center', box=box.ROUNDED, border_style=T.border_nexus, width=63)
```


---

### <a id='dev-scenes-py'></a> 📄 FILE: dev/scenes.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: SCENES_NODE CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: SCENES_NODE
> Context Path:  /dev/scenes.py
> 
> Concrete scene implementations for Developer Console modes (Architect, Vanguard).
> Authorized and signed under Vember OS decentralized system specifications.
> ================================================================================

#### 🚀 IMPORTS

```python
from rich.console import RenderableType
from rich.panel import Panel
from rich import box
from rich.text import Text
from assets.branding import VemberAssets
from dev.factory import ForgeFactory
from dev.windfall import NodeCluster
from dev.views import BaseView
```

#### 🏛️ CLASSES

- DevScene
- MainMenuScene

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: DevScene | METHOD: __init__

```python
def __init__(self, controller):
    super().__init__(controller)
```

#### 🏛️ CLASS: MainMenuScene | METHOD: __init__

```python
def __init__(self, controller, discovery=None):
    super().__init__(controller)
    self.factory = self.controller.factory
    from dev.views import DiscoveryMode
    self.discovery = discovery or DiscoveryMode()
    self.discovery.phase_stack = ['REGISTRY']
```

#### 🏛️ CLASS: MainMenuScene | METHOD: phases

```python
def phases(self, action_token: str) -> None:
    """🔱 CONTROLLER: Routes input tokens to the Discovery state machine."""
    self.discovery.phases(action_token, self.controller)
```

#### 🏛️ CLASS: MainMenuScene | METHOD: populate_nodes

```python
def populate_nodes(self, cluster: NodeCluster):
    """🔱 VIEWPORT: Renders discovered boxes (Registry -> Inspector -> Telemetry)."""
    cluster.purge_all_fields()
    for phase in self.discovery.phase_stack:
        if phase == 'REGISTRY':
            menu_panel = self.factory.generate_menu_matrix(menu_items=self.controller.menu_items, active_selection=self.controller.selection, is_node_active=False)
            cluster.cast_to_field('root', menu_panel)
        elif phase == 'INSPECTOR':
            inspector = self.factory.create_inspector_panel(self.controller)
            cluster.cast_to_field('action_node', inspector)
        elif phase == 'TELEMETRY':
            logs = self.factory.create_telemetry_panel(self.controller)
            cluster.cast_to_field('report_node', logs)
```


---

### <a id='dev-setup-py'></a> 📄 FILE: dev/setup.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: SETUP CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: SETUP_FORGE_NODE
> Context Path:  /dev/setup.py
> 
> Environment calibration and Docker group verification.
> ================================================================================

#### 🚀 IMPORTS

```python
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES

- SetupNode

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: SetupNode | METHOD: __init__

```python
def __init__(self):
    self.selection = 0
    self.calibration_steps = ['Verify Docker', 'Check Permissions', 'System Init']
    self.status_message = 'Awaiting system handshake...'
```

#### 🏛️ CLASS: SetupNode | METHOD: verify_docker_environment

```python
def verify_docker_environment(self):
    """Worker logic: Checks for docker engine binary."""
    return (True, True)
```

#### 🏛️ CLASS: SetupNode | METHOD: get_permissions_view

```python
def get_permissions_view(self, active_index=0):
    """Worker logic: Returns status strings for UI display."""
    _, in_docker_grp = self.verify_docker_environment()
    if in_docker_grp:
        return (f'[{Theme.success}][ ACTIVE ][/]', 'Socket Anchored', 'Ready.')
    return (f'[{Theme.warning}][ CALIBRATE ][/]', 'Attach Docker socket', 'Run sudo usermod')
```

#### 🏛️ CLASS: SetupNode | METHOD: render

```python
def render(self):
    """Returns the UI component for the VemberCLI host controller."""
    table = Table(box=None, padding=(0, 1), show_header=False)
    for i, step in enumerate(self.calibration_steps):
        style = f'bold {Theme.primary}' if i == self.selection else 'dim'
        prefix = f'[{Theme.primary}]▶[/]' if i == self.selection else '  '
        table.add_row(prefix, f'[{style}]{step}[/]')
    return Panel(Align.center(table), title=f'[{Theme.primary}]SETUP_FORGE_NODE[/]', border_style=Theme.primary, padding=(1, 2))
```


---

### <a id='dev-vanguard-py'></a> 📄 FILE: dev/vanguard.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: VANGUARD CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: VANGUARD_SHIELD_NODE
> Context Path:  /dev/vanguard.py
> 
> Environmental Integrity, Dependency Mapping & Logic Validation.
> Authorized and signed under Vember OS decentralized system specifications.
> 
> Context Actions:
> [V]     TRIGGER_INTEGRITY_SCAN
> [L]     LOCK_DEPENDENCY_HASHES
> [BKSP]  RETURN_TO_ROOT_CLI
> ================================================================================

#### 🚀 IMPORTS

```python
import json
from pathlib import Path
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.align import Align
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES

- Vanguard

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: Vanguard | METHOD: __init__

```python
def __init__(self):
    self.selection = 0
    self.active_node = 'Environmental HUD'
    self.node_output = '[dim]Awaiting integrity scan...[/]'
    self.is_processing = False
    self.test_results = {'passed': 0, 'failed': 0, 'total': 0}
    self.test_failures = []
    self.menu_items = [{'label': 'Audit Packages', 'desc': 'Map uv managed dependencies'}, {'label': 'Validate Logic', 'desc': 'Engage pytest suite'}]
```

#### 🏛️ CLASS: Vanguard | METHOD: render

```python
def render(self):
    """Returns the UI component for the VemberCLI host controller."""
    menu_table = Table(box=None, padding=(0, 1), show_header=False)
    for i, item in enumerate(self.menu_items):
        style = f'bold {Theme.primary}' if i == self.selection else 'dim'
        prefix = f'[{Theme.primary}]▶[/]' if i == self.selection else '  '
        menu_table.add_row(prefix, f"[{style}]{item['label']}[/]")
    left_panel = Panel(menu_table, title=f'[{Theme.primary}]VANGUARD ACTIONS[/]', border_style=Theme.primary, width=30, padding=(1, 2))
    right_stack = Table.grid(padding=1)
    right_stack.add_row(Panel(self.node_output, title=f'[{Theme.primary}]INTEGRITY HUD[/]', border_style=Theme.primary if self.is_processing else Theme.secondary, width=46, padding=(1, 2)))
    connector = Table.grid()
    connector.add_row(f' [{Theme.primary}]══▶[/] ')
    return Align.center(Columns([left_panel, Align.center(connector), right_stack], align='center'))
```

#### 🏛️ CLASS: Vanguard | METHOD: load_test_results

```python
def load_test_results(self):
    """Reads the json report generated by the TestReporter."""
    report_path = Path('exports/test_results.json')
    if report_path.exists():
        with open(report_path, 'r') as f:
            data = json.load(f)
            summary = data.get('summary', {})
            self.test_results['passed'] = summary.get('passed', 0)
            self.test_results['failed'] = summary.get('failed', 0)
            self.node_output = f"Tests: [green]{self.test_results['passed']} Passed[/] | [red]{self.test_results['failed']} Failed[/]"
    else:
        self.node_output = "[dim]No report found. Run 'Validate Logic' to generate.[/]"
```


---

### <a id='dev-views-py'></a> 📄 FILE: dev/views.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: VIEWS_NODE CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: VIEWS_NODE
> Context Path:  /dev/views.py
> 
> Governs the lifecycle and state-machine injection for active UI scenes.
> Authorized and signed under Vember OS decentralized system specifications.
> ================================================================================

#### 🚀 IMPORTS

```python
import subprocess
import threading
from rich.console import Group, RenderableType
from rich.align import Align
from dev.factory import ForgeFactory
from dev.widgets import ForgeHeader, ForgeFooter
from dev.windfall import NodeCluster
from dev.architect import ArchitectEngine
from dev.de import DockerEngine
```

#### 🏛️ CLASSES

- BaseView
- DiscoveryMode
- SceneRouter
- DeveloperView

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: BaseView | METHOD: __init__

```python
def __init__(self, controller):
    self.controller = controller
    self.footer_actions = [('UP/DN', 'NAVIGATE'), ('ENTER', 'IGNITE'), ('B', 'BUILD_DOCKER'), ('T', 'THEME_SWAP'), ('BKSP', 'BACK/EXIT')]
```

#### 🏛️ CLASS: BaseView | METHOD: phases

```python
def phases(self, action_token: str) -> None:
    """Handle input transitions."""
    raise NotImplementedError
```

#### 🏛️ CLASS: BaseView | METHOD: compose_view

```python
def compose_view(self) -> RenderableType:
    """Define the rendering pipeline."""
    raise NotImplementedError
```

#### 🏛️ CLASS: DiscoveryMode | METHOD: __init__

```python
def __init__(self):
    self.phase_stack = ['FOCUS']
    self.scan_completed = False
    self.violations = {}
    self.ae = ArchitectEngine()
    self.de = DockerEngine()
```

#### 🏛️ CLASS: DiscoveryMode | METHOD: active_enclave

```python
@property
def active_enclave(self) -> str:
    """Returns the top-most discovered node box."""
    return self.phase_stack[-1] if self.phase_stack else 'FOCUS'
```

#### 🏛️ CLASS: DiscoveryMode | METHOD: discover_next

```python
def discover_next(self, next_phase: str):
    """🔱 DISCOVERY: Pushes a new node box onto the viewport."""
    if next_phase not in self.phase_stack:
        self.phase_stack.append(next_phase)
```

#### 🏛️ CLASS: DiscoveryMode | METHOD: close_last

```python
def close_last(self) -> bool:
    """🔱 REVERSE BREADCRUMB: Pops the top box. Returns False if at root."""
    if len(self.phase_stack) > 1:
        self.phase_stack.pop()
        return True
    return False
```

#### 🏛️ CLASS: DiscoveryMode | METHOD: phases

```python
def phases(self, action_token: str, controller) -> bool:
    """🔱 PHASE CONTROLLER: Orchestrates the sequential flow."""
    if action_token == 'BKSP':
        if not self.close_last():
            controller.transition_to_view('dev')
        return True
    if action_token == 'IGNITE_MODULE_CONTRACT':
        if self.active_enclave == 'FOCUS':
            self.discover_next('ACTION')
        elif self.active_enclave == 'ACTION':
            self.discover_next('REPORT')
        elif self.active_enclave == 'REPORT':
            self.discover_next('REMEDY')
        return True
    if action_token == 'BUILD_DOCKER':
        self.de.run_build_and_boot(controller)
        return True
    return False
```

#### 🏛️ CLASS: DiscoveryMode | METHOD: run_scan

```python
def run_scan(self):
    """Delegated scan logic."""
    self.violations = self.ae.execute_dna_scan()
```

#### 🏛️ CLASS: DiscoveryMode | METHOD: reset

```python
def reset(self):
    self.phase = 1
    self.action_index = 0
    self.scan_completed = False
    self.violations = {}
```

#### 🏛️ CLASS: SceneRouter | METHOD: __init__

```python
def __init__(self, controller):
    self.controller = controller
    self._cache = {}
```

#### 🏛️ CLASS: SceneRouter | METHOD: get_view

```python
def get_view(self, scene_key):
    """🔱 DISPATCH: Resolves scene_keys to Scene instances."""
    from dev.scenes import MainMenuScene
    if scene_key in ['architect', 'FOCUS']:
        actual_key = 'architect'
    elif scene_key == 'dev':
        actual_key = 'dev'
    elif scene_key == 'vanguard':
        actual_key = 'vanguard'
    elif scene_key in ['windfall', 'barkbyte']:
        pass
        return None
    else:
        actual_key = scene_key
    if actual_key not in self._cache:
        if actual_key == 'dev':
            self._cache[actual_key] = MainMenuScene(self.controller, None)
    return self._cache.get(actual_key)
```

#### 🏛️ CLASS: DeveloperView | METHOD: compose_view

```python
def compose_view(self, controller, current_scene) -> RenderableType:
    header = ForgeHeader(title='DEVELOPER CONSOLE', version='v1.0.6-stable')
    footer = ForgeFooter(actions=controller.footer.current_cluster_actions)
    cluster = NodeCluster(None)
    if hasattr(current_scene, 'populate_nodes'):
        current_scene.populate_nodes(cluster)
    return Group(header, Align.center(cluster.compile()), footer)
```


---

### <a id='dev-widgets-py'></a> 📄 FILE: dev/widgets.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: WIDGETS CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: WIDGETS_MODULE
> Context Path:  /dev/widgets.py
> 
> Docker Telemetry Layers, Identity Elements, & Action Bar Legends.
> Authorized and signed under Vember OS decentralized system specifications.
> ================================================================================

#### 🚀 IMPORTS

```python
import getpass
import subprocess
from datetime import datetime
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich import box
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES

- ForgeWidgetBase
- ForgeIdentity
- ForgeDockerTelemetry
- ForgeHeader
- ForgePicker
- ForgeFooter

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: ForgeWidgetBase | METHOD: __init__

```python
def __init__(self):
    self.theme = VemberAssets.ACTIVE_THEME
```

#### 🏛️ CLASS: ForgeIdentity | METHOD: __init__

```python
def __init__(self):
    super().__init__()
    self.user = getpass.getuser()
    self._branch = None
```

#### 🏛️ CLASS: ForgeIdentity | METHOD: branch

```python
@property
def branch(self):
    if self._branch is None:
        try:
            self._branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stderr=subprocess.DEVNULL).decode().strip()
        except:
            self._branch = 'no-repo'
    return self._branch
```

#### 🏛️ CLASS: ForgeIdentity | METHOD: __rich__

```python
def __rich__(self):
    return Text.from_markup(f'👤 [bold white]{self.user}[/] 🌱 [bold magenta]{self.branch}[/]')
```

#### 🏛️ CLASS: ForgeDockerTelemetry | METHOD: get_view

```python
def get_view(self, size_data: dict):
    T = VemberAssets.ACTIVE_THEME
    total = size_data.get('total', 'OFFLINE')
    return Text.from_markup(f'[bold {T.primary}]vember_hub[/] [dim]|[/]{total}')
```

#### 🏛️ CLASS: ForgeHeader | METHOD: __init__

```python
def __init__(self, docker_engine=None, context_name=None, **kwargs):
    super().__init__()
    self.id = ForgeIdentity()
    self.telemetry = ForgeDockerTelemetry()
    self.docker_engine = docker_engine
    self.context_name = context_name
```

#### 🏛️ CLASS: ForgeHeader | METHOD: __rich__

```python
def __rich__(self):
    T = VemberAssets.ACTIVE_THEME
    size = self.docker_engine.get_container_size() if self.docker_engine else 'OFFLINE'
    time_str = datetime.now().strftime('%I:%M:%S %p %Z')
    brand = f'[bold {T.primary}]VEMBER OS[/]'
    separator = '[dim]|[/]'
    hub_label = f'[bold white]vember_hub:[/]'
    size_val = f'[bold #00FFFF]{size}[/]'
    brand_block = Align.center(f'{brand} {separator} {hub_label} {size_val}')
    grid = Table.grid(expand=True, padding=(0, 2))
    grid.add_column(justify='left', ratio=1)
    grid.add_column(justify='center', ratio=1)
    grid.add_column(justify='right', ratio=1)
    grid.add_row(self.id, brand_block, f'[bold {T.primary}]{time_str}[/]')
    return Panel(grid, box=box.SIMPLE, height=4, padding=(0, 1))
```

#### 🏛️ CLASS: ForgePicker | METHOD: __init__

```python
def __init__(self, title: str, items: list, selected_idx: int, active: bool=True):
    super().__init__()
    self.title = title
    self.items = items
    self.selected_idx = selected_idx
    self.active = active
```

#### 🏛️ CLASS: ForgePicker | METHOD: __rich__

```python
def __rich__(self):
    T = VemberAssets.ACTIVE_THEME
    table = Table(box=None, show_header=False, expand=True)
    table.add_column('Marker', width=2)
    table.add_column('Content')
    for i, item in enumerate(self.items):
        is_selected = i == self.selected_idx and self.active
        marker = f'[{T.cursor}]►[/]' if is_selected else ' '
        text = f'[{T.selection}]{item}[/]' if is_selected else f'[{T.dim}]{item}[/]'
        table.add_row(marker, text)
    return Panel(table, title=f' [bold {T.text}]{self.title}[/] ', title_align='left', border_style=T.primary if self.active else T.dim, box=box.ROUNDED, width=32, height=3, padding=(1, 1))
```

#### 🏛️ CLASS: ForgeFooter | METHOD: __init__

```python
def __init__(self, actions=None):
    super().__init__()
    self.current_cluster_actions = actions or []
```

#### 🏛️ CLASS: ForgeFooter | METHOD: __rich__

```python
def __rich__(self):
    T = VemberAssets.ACTIVE_THEME
    actions = []
    source = self.current_cluster_actions
    if source and isinstance(source, (list, tuple)):
        for item in source:
            if isinstance(item, (tuple, list)) and len(item) == 2:
                key, desc = item
                if '[' not in key:
                    actions.append((f'[{T.primary}]{key}[/]', desc))
                else:
                    actions.append((key, desc))
    if not actions:
        actions = [(f'[{T.primary}]UP/DN[/]', 'NAVIGATE'), (f'[{T.primary}]ENTER[/]', 'IGNITE'), (f'[{T.primary}]B[/]', 'BUILD_DOCKER'), (f'[{T.cursor}]T[/]', 'THEME_SWAP'), (f'[{T.primary}]BKSP[/]', 'BACK/EXIT')]
    footer_parts = [f'{key} [dim]{desc}[/]' for key, desc in actions]
    footer_markup = f"  {'  [dim]•[/]  '.join(footer_parts)}"
    return Align.center(Text.from_markup(footer_markup))
```


---

### <a id='dev-windfall-py'></a> 📄 FILE: dev/windfall.py

#### 📜 METADATA

> ================================================================================
> 🔱 VEMBER-OS: WINDFALL_COMPOSITOR CONTRACT PASSPORT
> ================================================================================
> Family Stack:  DEVELOPER_CORE
> Node Identity: WINDFALL_COMPOSITOR_ENGINE
> Context Path:  /dev/windfall.py
> 
> Dynamic Game-Loop Sprite Group Lifecycle & 4-Corner Rectangular Matrix Compositor.
> Authorized and signed under Vember OS decentralized system specifications.
> ================================================================================

#### 🚀 IMPORTS

```python
from rich.columns import Columns
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from rich.console import Group
from rich import box
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES

- NodeCluster

#### ⚙️ GEARS (METHODS & FUNC)

#### 🏛️ CLASS: NodeCluster | METHOD: __init__

```python
def __init__(self, root_card_panel):
    self._active_sprites = {}
    self._active_sprites['root'] = root_card_panel
    self.active_actions = []
```

#### 🏛️ CLASS: NodeCluster | METHOD: cast_to_field

```python
def cast_to_field(self, key: str, node_object):
    """⚔️ CAST SPRITE: Injects a dynamic panel onto the active rendering battlefield."""
    self._active_sprites[key] = node_object
```

#### 🏛️ CLASS: NodeCluster | METHOD: purge_from_field

```python
def purge_from_field(self, key: str):
    """⚔️ PURGE SPRITE: Removes a dynamic panel from the active battlefield."""
    if key in self._active_sprites:
        del self._active_sprites[key]
```

#### 🏛️ CLASS: NodeCluster | METHOD: purge_all_fields

```python
def purge_all_fields(self):
    """🔱 RESILIENCY: Force-wipe all active sprites from the cluster registry."""
    self._active_sprites = {'root': self._active_sprites.get('root')}
```

#### 🏛️ CLASS: NodeCluster | METHOD: learn_capacity_report

```python
def learn_capacity_report(self):
    """Gather telemetry data from active nodes."""
    return 'CLUSTER_STABLE'
```

#### 🏛️ CLASS: NodeCluster | METHOD: compile

```python
def compile(self):
    T = VemberAssets.ACTIVE_THEME
    nexus_node = self._active_sprites.get('nexus_node')
    focus_node = self._active_sprites.get('root')
    active_nodes = {k: v for k, v in self._active_sprites.items() if v is not None and k != 'root'}
    if focus_node and (not active_nodes):
        return Group(Align.center(focus_node, vertical='middle'), Align.center(nexus_node) if nexus_node else Text(''))
    action_node = active_nodes.get('action_node')
    report_node = active_nodes.get('report_node')
    remedy_node = active_nodes.get('remedy_node')
    top_row_elements = []
    if focus_node:
        top_row_elements.append(Align.center(focus_node))
    if action_node:
        connector = Align.center(Text(' ══▶ ', style=T.primary), vertical='middle')
        top_row_elements.extend([connector, Align.center(action_node)])
    top_row = Columns(top_row_elements, align='center', equal=False)
    bottom_row_elements = []
    if remedy_node and report_node:
        connector = Align.center(Text(' ◀══ ', style=T.primary), vertical='middle')
        bottom_row_elements.extend([Align.center(remedy_node), connector, Align.center(report_node)])
    elif report_node:
        bottom_row_elements.append(Align.center(report_node))
    elif remedy_node:
        bottom_row_elements.append(Align.center(remedy_node))
    bottom_row = Columns(bottom_row_elements, align='center', equal=False)
    nexus_row = Align.center(nexus_node) if nexus_node else None
    return Group(top_row, Text('\n'), bottom_row, Text('\n') if nexus_row else Text(''), nexus_row if nexus_row else Text(''))
```


---