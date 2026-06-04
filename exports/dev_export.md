# 🔱 VEMBER OS: DEV DISTRICT EXPORT
Generated: 2026-06-04 19:39:41

## 📜 TABLE OF CONTENTS
* [dev/architect.py](#dev-architect-py)
* [dev/console.py](#dev-console-py)
* [dev/de.py](#dev-de-py)
* [dev/factory.py](#dev-factory-py)
* [dev/keybinds.py](#dev-keybinds-py)
* [dev/nexus.py](#dev-nexus-py)
* [dev/scenes.py](#dev-scenes-py)
* [dev/setup.py](#dev-setup-py)
* [dev/vanguard.py](#dev-vanguard-py)
* [dev/views.py](#dev-views-py)
* [dev/views3.py](#dev-views3-py)
* [dev/widgets.py](#dev-widgets-py)
* [dev/windfall.py](#dev-windfall-py)

---

### <a id='dev-architect-py'></a> 📄 FILE: dev/architect.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import os
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES & GEARS

- **ArchitectEngine**: __init__, execute_dna_scan, heal_all_passports, render
```python
"""
================================================================================
🔱 VEMBER-OS: ARCHITECT CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: ARCHITECT_DNA_NODE
Context Path:  /dev/architect.py

Architectural Integrity & Workspace Passport Verification Engine.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

import os
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from assets.branding import VemberAssets

# Map the active theme from the centralized registry
Theme = VemberAssets.ACTIVE_THEME


class ArchitectEngine:
	"""The workspace scanner: verifies passports across the project structure."""

	def __init__(self):
		# Establish repository root relative to /dev
		self.project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

		# Surgical boundaries
		self.target_subdirs = ["dev", "assets", "engine", "nodes"]
		self.target_root_files = ["main.py"]

		self.flagged_violations = {}
		self.phase = "FOCUS"
		self.scan_results = "Awaiting DNA scan..."

	def execute_dna_scan(self) -> dict:
		"""Surgically parse designated directories for Trident passports."""
		self.flagged_violations = {}
		# ... [Your existing logic for scanning goes here] ...
		self.scan_results = "Scan complete: Integrity verified."
		return {"status": "clean"}

	def heal_all_passports(self) -> int:
		"""Worker method: Cleans docstrings and applies passport templates."""
		healed_count = 0
		# ... [Your existing logic for healing goes here] ...
		self.scan_results = f"Healed {healed_count} passports."
		return healed_count

	def render(self):
		"""Returns the UI component for the VemberCLI host controller."""

		table = Table(box=None, padding=(0, 1))
		table.add_column("Key", style=f"bold {Theme.primary}")
		table.add_column("Value")

		table.add_row("Status", self.scan_results)
		table.add_row("Phase", self.phase)
		table.add_row("Root", self.project_root)

		return Panel(
			Align.center(table),
			title=f"[{Theme.primary}]ARCHITECT_DNA_NODE[/]",
			border_style=Theme.primary,
			padding=(1, 2),
		)

```

---

### <a id='dev-console-py'></a> 📄 FILE: dev/console.py

#### 📜 METADATA

> No Node Passport detected.

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

#### 🏛️ CLASSES & GEARS

- **VemberConsole**: __init__, on_press, _query_docker_footprint, log_debug, _execute, _make_layout, run, ignite_module_contract, _load_standard_node_passport, switch_node

#### ⚡ GLOBAL GEARS: main

```python
"""
================================================================================
🔱 VEMBER-OS: VEMBER_CLI CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: MASTER_CLI_CONSOLE
Context Path:  /dev/vember_cli.py

Web3 Dynamic Stage Controller Tracking the 4-Corner Rectangular Grid Matrix.
Authorized and signed under Vember OS decentralized system specifications.

Context Actions:
[UP/DN] NAVIGATE_CORE_CARDS
[ENTER] IGNITE_MODULE_CONTRACT
[B]     TRIGGER_DOCKER_BUILD
[T]     HOT_SWAP_THEME_MATRIX
[BKSP]  DISCONNECT_TERMINAL
================================================================================
"""

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

# Ensure core workspace package paths map cleanly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dev.widgets import ForgeHeader, ForgeFooter
from dev.keybinds import ConsoleInputMatrix  # 🔱 REFACTORED: Unified keybind listener
from assets.branding import VemberAssets
from dev.windfall import NodeCluster  # 🔱 STREAMLINED: Lightened layout compositor
from dev.views import SceneRouter, DeveloperView
from dev.de import DockerEngine
from dev.vanguard import Vanguard

class VemberConsole:
	"""🔱 THE CORE CLI: Manages the dynamic sprite lifecycle of active layout nodes."""

	def __init__(self):

		self.controller = self

		self.menu_items = [
			{
				"label": "SETUP",
				"cmd": "SETUP",
				"desc": "Surgical Environment Setup Guide",
			},
			{
				"label": "ARCHITECT",
				"cmd": "ARCHITECT",
				"desc": "DNA Remediation & Code Integrity",
			},
			{
				"label": "VANGUARD",
				"cmd": "VANGUARD",
				"desc": "Logic Validation & Dependency Shielding",
			},
			{
				"label": "WINDFALL",
				"cmd": "WINDFALL",
				"desc": "Vember OS Layout Compositor Engine",
			},
			{
				"label": "BARKBYTE",
				"cmd": "BARKBYTE",
				"desc": "Compositional Node-Based IDE Environment",
			},
			{
				"label": "EXIT_CONSOLE",
				"cmd": "EXIT",
				"desc": "Disconnect from forge context",
			},
		]

		self.nodes = {
			"SETUP": None,        # Or your SetupNode()
			"VANGUARD": Vanguard(),
			# "ARCHITECT": Architect()
		}

		self.console = Console()
		self.selection = 0
		self.active_cmd = None
		self.child_selection = 0

		self.shutdown_flag: bool = False
		self.master_layout = None
		self.router = SceneRouter(self.controller)
		self.view_container = DeveloperView(self)

		self.current_scene = "SETUP"

		self.capacity_status: str = "CLUSTER_STABLE"

		self.docker_engine = DockerEngine("vember_hub")
		self.docker_data = {"total": "0 MB", "status": "READY"}

		self.status_msg = "SYSTEM_READY: Awaiting Tactical Ignition..."
		self.header = ForgeHeader(
			docker_engine=self.docker_engine, context_name="DEVELOPER_CORE"
		)
		self.footer = ForgeFooter()

		# Start the keyboard listener as the Host
		self.listener = keyboard.Listener(on_press=self.on_press)
		self.listener.start()

	def on_press(self, key):
		# Global input handling for the OS
		if key == keyboard.Key.esc:
			self.shutdown_flag = True

	def _query_docker_footprint(self):
		"""Delegates footprint polling to the specialized DockerEngine."""
		self.docker_data["total"] = self.docker_engine.get_container_size()
		# You can set status based on the result
		self.docker_data["status"] = "SYNCED" if self.docker_data["total"] != "OFFLINE" else "DISCONNECTED"

	def log_debug(self, message: str):
		"""🔱 BLACK BOX LOGGER: Writes events to a persistent debug file."""
		with open("vember.log", "a") as f:
			f.write(f"{datetime.now().strftime('%H:%M:%S.%f')} | {message}\n")

	def _execute(self, cmd_id: str):
		if cmd_id == "THEME_SWAP":
			themes = ["midnight", "sakura", "kuro", "shinto"]
			current_key = VemberAssets.ACTIVE_THEME.name.lower()
			current_simple_key = next(
				(k for k in themes if k in current_key), "midnight"
			)
			try:
				next_idx = (themes.index(current_simple_key) + 1) % len(themes)
				VemberAssets.apply_theme(themes[next_idx])
				self.status_msg = f"THEME_IGNITED: {VemberAssets.ACTIVE_THEME.name}"
			except ValueError:
				VemberAssets.apply_theme("midnight")
		elif cmd_id == "DOCKER_BUILD":
			self.status_msg = "RUNNING_BUILD: Compiling local environment Dockerfile..."
			self._query_docker_footprint()
		else:
			self.active_cmd = cmd_id
			self.child_selection = 0
			self.status_msg = (
				f"CONTRACT_ENGAGED: Active runtime channel routed to {cmd_id}..."
			)

	def _make_layout(self):
		"""
		🔱 ASSEMBLE_LAYOUT: The central nervous system of the UI frame.
		Uses a rigid Layout grid to prevent screen overflow (doubling)
		and lock the focus node to the true vertical center.
		"""
		layout = Layout(name="root")

		# split() without 'column' or 'row' defaults to stacking vertically
		layout.split(
			Layout(name="header", size=5),
			Layout(name="body"),
			Layout(name="footer", size=5)
		)
		return layout

	def run(self):
		self.master_layout = self._make_layout()
		with Live(self.master_layout, refresh_per_second=20, screen=True) as live:
			while not self.shutdown_flag:
				# 3. Update Display
				self.master_layout['header'].update(ForgeHeader(...))
				self.master_layout['body'].update(self.view_container.compose_view(self, self.current_scene))
				time.sleep(0.05)

	def ignite_module_contract(self):
		"""🔱 IGNITION: Transitions selection from Registry to Action Node."""
		try:
			# 1. Map current selection to Node Name
			selected_node = self.controller.menu_items[self.controller.selection]

			# 2. THE RITUAL OF ENTRY: Handle specific node initialization
			if selected_node == "Architect":
				# Initialize with a FOCUS phase to prevent NoneType crash [1]
				self.active_engine = ArchitectEngine()
			else:
				# Fallback for standard nodes to prevent 'SETUP' error
				# Replace 'None' with your standard node loader logic
				self.active_engine = self._load_standard_node_passport(selected_node)

			# 3. SAFETY HANDSHAKE: Ensure engine carrying .phase is valid
			if self.active_engine and hasattr(self.active_engine, "phase"):
				# Route the Windfall Compositor to the new Action Node view
				self.current_scene = self.router.get_view(self.active_engine.phase)
			else:
				# Log specific break if the node was a shell
				self.log_debug(f"MAGMA ORANGE: {selected_node} lacks a valid phase.")

		except Exception as e:
			import traceback

			self.log_debug(f"IGNITION FAILED: {str(e)}")
			# Dump the traceback to dev_audit.json for a Gleaning session

	def _load_standard_node_passport(self, node_name):
		"""🔱 FALLBACK: Loads a standard node envelope if no custom engine exists."""
		try:
			# For now, we return a simple object carrying the FOCUS phase
			# to keep the Windfall Compositor from buckling.
			class StandardNode:
				def __init__(self):
					self.phase = "IGNITE"

			self.log_debug(f"PASSPORT_ISSUED: {node_name}")
			return StandardNode()
		except Exception as e:
			self.log_debug(f"PASSPORT_FAILURE: {str(e)}")
			return None

	def switch_node(self, node_name):
		"""The central hub for state transitions."""
		if node_name in self.nodes:
			self.current_node = node_name

def main():
	cli = VemberConsole()
	cli.run()


if __name__ == "__main__":
	main()

```

---

### <a id='dev-de-py'></a> 📄 FILE: dev/de.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import docker
from docker import errors
import subprocess, os
import threading
```

#### 🏛️ CLASSES & GEARS

- **DockerEngine**: __init__, run_build_and_boot, _run_build_task, _run_boot_task, get_container_size, check_docker_online
```python
"""
================================================================================
🔱 VEMBER-OS: DOCKER_ENGINE CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: DOCKER_REMEDIATION_ENGINE
Context Path:  /dev/docker.py

Handles manual container footprint polling and lifecycle build orchestration.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

import docker
from docker import errors
import subprocess, os
import threading


class DockerEngine:
	"""🛠️ DOCKER_ENGINE: Unified lifecycle manager for Vember OS containers."""

	def __init__(self, target_container="vember_hub", image_name="vember-node"):
		self.target_container = target_container
		self.image_name = image_name

	def run_build_and_boot(self, controller):
		"""Unified background task: Build then Boot if offline."""
		def task():
			controller.status_msg = "⚡ BUILD: Compiling layers..."
			
			# 1. Build
			success = self._run_build_task()
			
			if success:
				controller.status_msg = "⚡ BUILD: Success. Checking status..."
				# 2. Boot (only if not already running)
				if not self.check_docker_online():
					controller.status_msg = "⚡ BOOT: Launching..."
					self._run_boot_task()
				controller.status_msg = "⚡ SYSTEM: Online (Stable)"
			else:
				controller.status_msg = "⚡ BUILD: Failed"
				
		threading.Thread(target=task, daemon=True).start()
		return True

	def _run_build_task(self):
		"""Internal: Silently execute docker compose build."""
		try:
			with open(os.devnull, "w") as devnull:
				subprocess.run(
					["docker", "compose", "build"],
					stdout=devnull,
					stderr=devnull,
					check=True,
				)
			return True
		except subprocess.CalledProcessError:
			return False

	def _run_boot_task(self):
		"""Internal: Boots the container using docker run."""
		try:
			# -d: Detached, --name: Identity for tracking
			subprocess.run(
				[
					"docker",
					"run",
					"-d",
					"--name",
					self.target_container,
					self.image_name,
				],
				stdout=subprocess.DEVNULL,
				stderr=subprocess.DEVNULL,
				check=True,
			)
			return True
		except subprocess.CalledProcessError:
			return False

	def get_container_size(self):
		"""🛡️ NEXUS_CORE: Queries container footprint with safety checks."""
		try:
			client = docker.from_env()
			container = client.containers.get(self.target_container)

			# 🔱 SAFETY CHECK: Ensure the container has an associated image
			if container.image is None:
				return "UNLINKED"

			# Use getattr for safer attribute access
			image_attrs = getattr(container.image, "attrs", {})
			size_bytes = image_attrs.get("Size", 0)

			return f"{round(size_bytes / (1024 * 1024), 1)} MB"

		except errors.NotFound:
			# 🔱 FIX: Now using the correctly imported errors module
			return "OFFLINE"
		except Exception:
			# Catch-all for other daemon issues
			return "ERROR"

	def check_docker_online(self) -> bool:
		"""Check if the target container is running."""
		try:
			# We use the target_container attribute initialized in __init__
			cmd = ["docker", "inspect", "-f", "{{.State.Running}}", self.target_container]
			result = subprocess.run(cmd, capture_output=True, text=True, check=False)
			return result.stdout.strip() == "true"
		except Exception:
			return False

```

---

### <a id='dev-factory-py'></a> 📄 FILE: dev/factory.py

#### 📜 METADATA

> No Node Passport detected.

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

#### 🏛️ CLASSES & GEARS

- **ForgeFactory**: generate_menu_matrix
```python
"""
================================================================================
🔱 VEMBER-OS: FACTORY CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: FACTORY_NODE
Context Path:  /dev/factory.py

Operational Integrity & Structural UI Panel Composition Primitives.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

from rich.console import Group
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from rich import box
from rich.table import Table
from assets.branding import VemberAssets


class ForgeFactory:
	"""🔱 THE ASSEMBLER: Welding widget configurations together into static composite blocks."""

	@staticmethod
	def generate_menu_matrix(
		menu_items: list, active_selection: int, is_node_active: bool
	):
		T = VemberAssets.ACTIVE_THEME
		VERSION = "v1.0.6-stable"

		# 1. Main Grid Construction
		grid_table = Table(box=None, show_header=False, expand=True, padding=(0, 2))
		grid_table.add_column("C1", justify="center")
		grid_table.add_column("C2", justify="center")
		grid_table.add_column("C3", justify="center")

		row_items = []
		active_desc = ""

		# Build the list of displayable items
		for i, item in enumerate(menu_items):
			# Check if active based on index
			is_active = (i == active_selection)
			if is_active:
				row_items.append(f"[{T.cursor}]►[/] [{T.selection}]{item['label']}[/]")
				active_desc = item.get("desc", "")
			else:
				row_items.append(f"   [bold white]{item['label']}[/]")

		# 🔱 SAFETY FIX: Ensure we always have exactly 6 slots to prevent IndexError
		while len(row_items) < 6:
			row_items.append("")

		# Construct the table rows
		grid_table.add_row(row_items[0], row_items[1], row_items[2])
		grid_table.add_row("", "", "")  # spacer row
		grid_table.add_row(row_items[3], row_items[4], row_items[5])

		# 2. Rules Box Construction
		rules_box = Table(box=None, show_header=False, expand=True)
		rules_box.add_row(
			Text.from_markup(
				f"[dim]◈[/] [bold {T.text}]{active_desc}[/]", justify="center"
			)
		)

		# 3. Combine into a Group
		content_group = Group(grid_table, Text("\n"), rules_box)

		# 4. Final Panel Assembly
		menu_panel = Panel(
			content_group,
			title=f" [bold {T.text}]VEMBER_OS_CORE {VERSION}[/] ",
			border_style=T.primary,
			box=box.ROUNDED,
			padding=(1, 1),
			width=65,
		)

		# 🔱 ALIGN FIX: Wrapping the Panel ensures it is dead-center
		return Align.center(menu_panel)

```

---

### <a id='dev-keybinds-py'></a> 📄 FILE: dev/keybinds.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import queue
from pynput import keyboard
from typing import Optional
```

#### 🏛️ CLASSES & GEARS

- **ConsoleInputMatrix**: initialize_matrix, capture_action, shutdown_matrix
```python
"""
================================================================================
🔱 VEMBER-OS: KEYBINDS CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: DEVELOPER_CONSOLE_KEYBINDS
Context Path:  /dev/keybinds.py

Asynchronous Background Worker Thread & Harvester Queue Input Matrix.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

import queue
from pynput import keyboard
from typing import Optional


class ConsoleInputMatrix:
	_input_queue: queue.Queue = queue.Queue()
	_listener: Optional[keyboard.Listener] = None
	_initialized: bool = False

	@classmethod
	def initialize_matrix(cls):
		"""Spins up the OS-level key listener background daemon."""

		def on_press(key):
			try:
				if key == keyboard.Key.up:
					cls._input_queue.put("UP")
				elif key == keyboard.Key.down:
					cls._input_queue.put("DN")
				elif key == keyboard.Key.enter:
					cls._input_queue.put("IGNITE_MODULE_CONTRACT")
			except Exception:
				pass

		cls._listener = keyboard.Listener(on_press=on_press)
		cls._listener.start()
		cls._initialized = True

	@classmethod
	def capture_action(cls) -> str:
		"""Extracts the latest keypress without blocking the UI thread."""
		if not cls._initialized:
			cls.initialize_matrix()

		try:
			return cls._input_queue.get_nowait()
		except queue.Empty:
			return ""

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

> No Node Passport detected.

#### 🚀 IMPORTS

```python
import hashlib
from rich.panel import Panel
from rich import box
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES & GEARS

- **NexusNode**: __init__, _generate_signature, __rich__
```python
"""
================================================================================
🔱 VEMBER-OS: NEXUS_NODE CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: NEXUS_AUTHORIZATION_NODE
Context Path:  /dev/nexus.py

Cryptographic identity notarization and session-state handshake manager.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

import hashlib
from rich.panel import Panel
from rich import box
from assets.branding import VemberAssets


class NexusNode:
    """🛡️ THE NEXUS: Cryptographic identity and authorization ledger."""

    def __init__(self, raw_data: str = "VEMBER_SESSION_ACTIVE"):
        self.status = "READY"
        self.signature = self._generate_signature(raw_data)

    def _generate_signature(self, data: str) -> str:
        """Generates a cryptographic-style fingerprint for the current session."""
        sha_hash = hashlib.sha256(data.encode()).hexdigest()
        return f"0x{sha_hash[:7].upper()}..."

    def __rich__(self):
        T = VemberAssets.ACTIVE_THEME

        # Build the ledger content dynamically
        ledger_content = (
            f" [dim]Status:[/] [bold {T.success}]{self.status}[/]\n"
            f" [dim]Signature:[/] [bold {T.border_nexus}]{self.signature}[/]"
        )

        # Encapsulate into the panel
        return Panel(
            ledger_content,
            title=f" [bold {T.border_nexus}]NEXUS AUTHORIZATION[/] ",
            title_align="center",
            box=box.ROUNDED,
            border_style=T.border_nexus,
            width=63,
        )

```

---

### <a id='dev-scenes-py'></a> 📄 FILE: dev/scenes.py

#### 📜 METADATA

> No Node Passport detected.

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

#### 🏛️ CLASSES & GEARS

- **DevScene**: __init__
- **MainMenuScene**: __init__, phases, populate_nodes
```python
"""
================================================================================
🔱 VEMBER-OS: SCENES_NODE CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: SCENES_NODE
Context Path:  /dev/scenes.py

Concrete scene implementations for Developer Console modes (Architect, Vanguard).
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

from rich.console import RenderableType
from rich.panel import Panel
from rich import box
from rich.text import Text
from assets.branding import VemberAssets
from dev.factory import ForgeFactory
from dev.windfall import NodeCluster
from dev.views import BaseView


class DevScene(BaseView):
	"""🔱 BASE DEV SCENE: Simplified shared controller access."""

	def __init__(self, controller):
		super().__init__(controller)


class MainMenuScene(DevScene):
	"""🎬 MAIN_MENU: Orchestrates the primary District Registry view."""

	def __init__(self, controller, discovery=None):
		super().__init__(controller)
		self.factory = self.controller.factory

		# 🔱 OPTION A: LOCAL INJECTION
		# Prevents circular import with dev.views.SceneRouter
		from dev.views import DiscoveryMode

		self.discovery = discovery or DiscoveryMode()

		# 🔱 REGISTRY INIT: Start the stack with the main menu list
		self.discovery.phase_stack = ["REGISTRY"]

	def phases(self, action_token: str) -> None:
		"""🔱 CONTROLLER: Routes input tokens to the Discovery state machine."""
		self.discovery.phases(action_token, self.controller)

	def populate_nodes(self, cluster: NodeCluster):
		"""🔱 VIEWPORT: Renders discovered boxes (Registry -> Inspector -> Telemetry)."""
		# 1. PURGE: Clear the field for the fresh game-loop cycle
		cluster.purge_all_fields()

		for phase in self.discovery.phase_stack:
			if phase == "REGISTRY":
				menu_panel = self.factory.generate_menu_matrix(
					menu_items=self.controller.menu_items,
					active_selection=self.controller.selection,
					is_node_active=False,
				)
				cluster.cast_to_field("root", menu_panel)
			elif phase == "INSPECTOR":
				# Slides in when a node is "Discovered" via [ENTER]
				inspector = self.factory.create_inspector_panel(self.controller)
				cluster.cast_to_field("action_node", inspector)
			elif phase == "TELEMETRY":
				# Appears as a report node for active execution
				logs = self.factory.create_telemetry_panel(self.controller)
				cluster.cast_to_field("report_node", logs)


# class ArchitectScene(DevScene):
# 	"""🔱 ARCHITECT SCENE: Concrete implementation (Payload only)."""

# 	def __init__(self, controller, discovery_mode):
# 		super().__init__(controller, discovery_mode)
# 		self.track = discovery_mode

# 	def phases(self, action_token: str) -> None:
# 		"""Delegates input handling to the shared DiscoveryMode state machine."""
# 		# 🔱 1. ALWAYS check navigation first
# 		if action_token in ["UP", "DN"]:
# 			menu_len = len(self.controller.menu_items)
# 			if action_token == "UP":
# 				self.controller.selection = (self.controller.selection - 1) % menu_len
# 			else:
# 				self.controller.selection = (self.controller.selection + 1) % menu_len
# 			return # STOP here so DiscoveryMode doesn't eat the token

# 		# 🔱 2. ONLY delegate if it's not navigation
# 		self.track.phases(action_token, self.controller)

# 	def populate_nodes(self, cluster: NodeCluster):
# 		"""Purely injects data into the provided cluster (The Payload)."""
# 		T = VemberAssets.ACTIVE_THEME

# 		# --- ACTION NODE ---
# 		action_border = T.warning if self.track.phase == 2 else T.dim
# 		marker_0 = (
# 			f"[{T.cursor}]►[/]"
# 			if (self.track.phase == 2 and self.track.action_index == 0)
# 			else "   "
# 		)
# 		marker_1 = (
# 			f"[{T.cursor}]►[/]"
# 			if (self.track.phase == 2 and self.track.action_index == 1)
# 			else "   "
# 		)

# 		action_content = (
# 			f"{marker_0} IGNITE_WORKSPACE_DNA_SCAN\n    [dim]Parses local workspace script headers[/]\n\n"
# 			f"{marker_1} REFRESH_SYSTEM_TELEMETRY\n    [dim]Flushes internal tracking structures[/]"
# 		)

# 		cluster.cast_to_field(
# 			"action_node",
# 			Panel(
# 				action_content,
# 				title=" [bold yellow]ACTION NODE[/] ",
# 				title_align="center",
# 				box=box.ROUNDED,
# 				border_style=action_border,
# 				width=65,
# 				padding=(1, 1),
# 			),
# 		)

# 		# --- REPORT NODE ---
# 		if self.track.scan_completed:
# 			total_violations = sum(
# 				len(files) for files in self.track.violations.values()
# 			)
# 			report_text = f" ┠─ SCAN_STATUS: RUNTIME_COMPLETE\n ┠─ VIOLATIONS: [bold {'red' if total_violations > 0 else 'green'}]{total_violations} Anomalies Found[/]\n"

# 			for dir_label, files in self.track.violations.items():
# 				report_text += f"\n   [bold {T.primary}]📁 {dir_label}/[/]\n"
# 				for file_name in files:
# 					report_text += f"     [bold red]❌[/] [dim]{file_name}[/]\n"

# 			cluster.cast_to_field(
# 				"report_node",
# 				Panel(
# 					report_text.rstrip(),
# 					title=" [bold magenta]REPORT NODE[/] ",
# 					title_align="center",
# 					box=box.ROUNDED,
# 					border_style=T.primary,
# 					width=65,
# 				),
# 			)

# 		# --- REMEDY NODE ---
# 		if (
# 			self.track.scan_completed
# 			and sum(len(files) for files in self.track.violations.values()) > 0
# 		):
# 			remedy_border = T.success if self.track.phase == 3 else T.dim
# 			remedy_marker = f" [{T.cursor}]►[/]" if self.track.phase == 3 else "   "
# 			remedy_content = f"{remedy_marker} [bold {T.success}]GRAFT_AUTOMATED_DNA_REMEDIATION[/]\n    [dim]Surgically welds trident passports to targets[/]"

# 			cluster.cast_to_field(
# 				"remedy_node",
# 				Panel(
# 					remedy_content,
# 					title=" [bold cyan]REMEDY NODE[/] ",
# 					title_align="center",
# 					box=box.ROUNDED,
# 					border_style=remedy_border,
# 					width=65,
# 					padding=(1, 1),
# 				),
# 			)

# 		# Sync the footer actions to the controller
# 		self.controller.footer.current_cluster_actions = self.footer_actions

# 	def handle_enter(self):
# 		# Access the current selection
# 		selected_item = self.controller.menu_items[self.controller.selection]
# 		cmd = selected_item.get("cmd")
# 		print(f"Executing: {cmd}")


# class VanguardScene(DevScene):
# 	"""🔱 VANGUARD SCENE: Specialized data pipeline and security telemetry."""

# 	def __init__(self, controller, discovery_mode):
# 		super().__init__(controller, discovery_mode)
# 		self.track = discovery_mode
# 		self.security_level = "ACTIVE"

# 	def phases(self, action_token: str) -> None:
# 		pass  # To be mapped to Vanguard-specific state logic

# 	def compose_scene(self) -> RenderableType:
# 		return Text("Vanguard Security Layer Active")

```

---

### <a id='dev-setup-py'></a> 📄 FILE: dev/setup.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES & GEARS

- **SetupNode**: __init__, verify_docker_environment, get_permissions_view, render
```python
"""
================================================================================
🔱 VEMBER-OS: SETUP CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: SETUP_FORGE_NODE
Context Path:  /dev/setup.py

Environment calibration and Docker group verification.
================================================================================
"""

from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from assets.branding import VemberAssets

# Map the active theme from the centralized registry
Theme = VemberAssets.ACTIVE_THEME


class SetupNode:
    """The environment calibrator: handles Docker groups and system checks."""

    def __init__(self):
        self.selection = 0
        self.calibration_steps = ["Verify Docker", "Check Permissions", "System Init"]
        self.status_message = "Awaiting system handshake..."

    def verify_docker_environment(self):
        """Worker logic: Checks for docker engine binary."""
        # Add your existing sub-process check logic here
        return True, True

    def get_permissions_view(self, active_index=0):
        """Worker logic: Returns status strings for UI display."""
        _, in_docker_grp = self.verify_docker_environment()

        if in_docker_grp:
            return f"[{Theme.success}][ ACTIVE ][/]", "Socket Anchored", "Ready."
        return (
            f"[{Theme.warning}][ CALIBRATE ][/]",
            "Attach Docker socket",
            "Run sudo usermod",
        )

    def render(self):
        """Returns the UI component for the VemberCLI host controller."""

        table = Table(box=None, padding=(0, 1), show_header=False)
        for i, step in enumerate(self.calibration_steps):
            # Apply theme colors dynamically
            style = f"bold {Theme.primary}" if i == self.selection else "dim"
            prefix = f"[{Theme.primary}]▶[/]" if i == self.selection else "  "
            table.add_row(prefix, f"[{style}]{step}[/]")

        # Assemble the UI Panel
        return Panel(
            Align.center(table),
            title=f"[{Theme.primary}]SETUP_FORGE_NODE[/]",
            border_style=Theme.primary,
            padding=(1, 2),
        )

```

---

### <a id='dev-vanguard-py'></a> 📄 FILE: dev/vanguard.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.align import Align
from assets.branding import VemberAssets
```

#### 🏛️ CLASSES & GEARS

- **Vanguard**: __init__, render
```python
"""
================================================================================
🔱 VEMBER-OS: VANGUARD CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: VANGUARD_SHIELD_NODE
Context Path:  /dev/vanguard.py

Environmental Integrity, Dependency Mapping & Logic Validation.
Authorized and signed under Vember OS decentralized system specifications.

Context Actions:
[V]     TRIGGER_INTEGRITY_SCAN
[L]     LOCK_DEPENDENCY_HASHES
[BKSP]  RETURN_TO_ROOT_CLI
================================================================================
"""

from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.align import Align
from assets.branding import VemberAssets

Theme = VemberAssets.ACTIVE_THEME


class Vanguard:
	"""Protects the environment via uv dependency audits and logic validation."""

	def __init__(self):
		self.selection = 0
		self.active_node = "Environmental HUD"
		self.node_output = "[dim]Awaiting integrity scan...[/]"
		self.is_processing = False
		self.test_failures = []
		self.menu_items = [
			{"label": "Audit Packages", "desc": "Map uv managed dependencies"},
			{"label": "Validate Logic", "desc": "Engage pytest suite"},
		]

	def render(self):
		"""Returns the UI component for the VemberCLI host controller."""

		# Menu Panel
		menu_table = Table(box=None, padding=(0, 1), show_header=False)
		for i, item in enumerate(self.menu_items):
			# Using 'primary' for ACCENT
			style = f"bold {Theme.primary}" if i == self.selection else "dim"
			prefix = f"[{Theme.primary}]▶[/]" if i == self.selection else "  "
			menu_table.add_row(prefix, f"[{style}]{item['label']}[/]")

		left_panel = Panel(
			menu_table,
			title=f"[{Theme.primary}]VANGUARD ACTIONS[/]",
			border_style=Theme.primary, # Changed from ACCENT
			width=30,
			padding=(1, 2),
		)

		# Integrity HUD Panel
		right_stack = Table.grid(padding=1)
		right_stack.add_row(
			Panel(
				self.node_output,
				title=f"[{Theme.primary}]INTEGRITY HUD[/]",
				border_style=Theme.primary if self.is_processing else Theme.border_action,
				width=46,
				padding=(1, 2),
			)
		)

		connector = Table.grid()
		connector.add_row(f" [{Theme.primary}]══▶[/] ")

		return Align.center(
			Columns([left_panel, Align.center(connector), right_stack], align="center")
		)

```

---

### <a id='dev-views-py'></a> 📄 FILE: dev/views.py

#### 📜 METADATA

> No Node Passport detected.

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

#### 🏛️ CLASSES & GEARS

- **BaseView**: __init__, phases, compose_view
- **DiscoveryMode**: __init__, active_enclave, discover_next, close_last, phases, run_scan, reset
- **SceneRouter**: __init__, get_view
- **DeveloperView**: compose_view
```python
"""
================================================================================
🔱 VEMBER-OS: VIEWS_NODE CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: VIEWS_NODE
Context Path:  /dev/views.py

Governs the lifecycle and state-machine injection for active UI scenes.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""


import subprocess
import threading

from rich.console import Group, RenderableType
from rich.align import Align
from dev.factory import ForgeFactory
from dev.widgets import ForgeHeader,ForgeFooter
from dev.windfall import NodeCluster
from dev.architect import ArchitectEngine
from dev.de import DockerEngine

# 1. THE CONTRACT
class BaseView:
	"""🎬 Abstract View Contract: Defines the lifecycle for all UI modes."""

	def __init__(self, controller):
		self.controller = controller
		self.footer_actions = [
			("UP/DN", "NAVIGATE"),
			("ENTER", "IGNITE"),
			("B", "BUILD_DOCKER"),
			("T", "THEME_SWAP"),
			("BKSP", "BACK/EXIT"),
		]

	def phases(self, action_token: str) -> None:
		"""Handle input transitions."""
		raise NotImplementedError

	def compose_view(self) -> RenderableType:
		"""Define the rendering pipeline."""
		raise NotImplementedError


# 2. THE SHARED STATE MACHINE
class DiscoveryMode:
	"""🛰️ DISCOVERY TRACKER: Manages the sequential 'Gleaning' of node boxes."""

	def __init__(self):
		# 🔱 THE STACK: Operates as the "Reverse Breadcrumb" registry
		# Initialized with 'FOCUS' as the mandatory entry enclave
		self.phase_stack = ["FOCUS"]
		self.scan_completed = False
		self.violations = {}
		
		# Internal engine references
		self.ae = ArchitectEngine()
		self.de = DockerEngine()

	@property
	def active_enclave(self) -> str:
		"""Returns the top-most discovered node box."""
		return self.phase_stack[-1] if self.phase_stack else "FOCUS"

	def discover_next(self, next_phase: str):
		"""🔱 DISCOVERY: Pushes a new node box onto the viewport."""
		if next_phase not in self.phase_stack:
			self.phase_stack.append(next_phase)

	def close_last(self) -> bool:
		"""🔱 REVERSE BREADCRUMB: Pops the top box. Returns False if at root."""
		if len(self.phase_stack) > 1:
			self.phase_stack.pop()
			return True
		return False

	def phases(self, action_token: str, controller) -> bool:
		"""🔱 PHASE CONTROLLER: Orchestrates the sequential flow."""
		
		# 1. THE RETREAT: Handle Backspace (Reverse Breadcrumbs)
		if action_token == "BKSP":
			if not self.close_last():
				# If stack is empty, return to Master CLI (Node 01 Face)
				controller.transition_to_view("dev")
			return True

		# 2. THE ADVANCE: Handle Ignition (Sequential Discovery)
		if action_token == "IGNITE_MODULE_CONTRACT":
			if self.active_enclave == "FOCUS":
				# Logic: Target selected -> Discovery: ACTION
				self.discover_next("ACTION")
			elif self.active_enclave == "ACTION":
				# Logic: DNA Scan triggered -> Discovery: REPORT
				# self.violations = self.ae.execute_dna_scan()
				self.discover_next("REPORT")
			elif self.active_enclave == "REPORT":
				# Logic: Telemetry parsed -> Discovery: REMEDY
				self.discover_next("REMEDY")
			return True

		# 3. DOCKER INTEGRATION: Node-specific side quests
		if action_token == "BUILD_DOCKER":
			self.de.run_build_and_boot(controller)
			return True

		return False

	def run_scan(self):
		"""Delegated scan logic."""
		self.violations = self.ae.execute_dna_scan()

	def reset(self):
		self.phase = 1
		self.action_index = 0
		self.scan_completed = False
		self.violations = {}


class SceneRouter:
	"""🔱 ROUTER: Maps district keys and engine phases to visual UI scenes."""

	def __init__(self, controller):
		self.controller = controller
		self._cache = {}  # 🔱 Persistent storage for active enclaves

	def get_view(self, scene_key):
		"""🔱 DISPATCH: Resolves scene_keys to Scene instances."""
		from dev.scenes import MainMenuScene

		# 1. DISTRICT ALIGNMENT: Mapping phases to their respective scenes
		if scene_key in ["architect", "FOCUS"]:
			actual_key = "architect"
		elif scene_key == "dev":
			actual_key = "dev"
		elif scene_key == "vanguard":
			actual_key = "vanguard"
		elif scene_key in ["windfall", "barkbyte"]:
			# 🔱 ARCHITECT DIRECTIVE: Pass for now
			pass
			return None
		else:
			actual_key = scene_key

		# 2. CACHE INITIALIZATION: Instantiate scenes only when needed (3% Idle Target)
		if actual_key not in self._cache:
			if actual_key == "dev":
				self._cache[actual_key] = MainMenuScene(self.controller, None)

		return self._cache.get(actual_key)


class DeveloperView(BaseView):
	"""🔱 CONTAINER: Manages layout, footer, and menu orchestration."""

	def compose_view(self, controller, current_scene) -> RenderableType:
		# 1. Boilerplate: Header and Footer
		# Ensure your footer is accessible on the controller object
		header = ForgeHeader(title="DEVELOPER CONSOLE", version="v1.0.6-stable")
		footer = ForgeFooter(actions=controller.footer.current_cluster_actions)

		cluster = NodeCluster(None)

		# 3. Payload Injection
		# The scene 'payload' adds its specific panels to the cluster
		if hasattr(current_scene, "populate_nodes"):
			current_scene.populate_nodes(cluster)

		# 4. Assemble into a full layout
		# Return a Group to render the vertical stack (Header -> Cluster -> Footer)
		return Group(header, Align.center(cluster.compile()), footer)

```

---

### <a id='dev-views3-py'></a> 📄 FILE: dev/views3.py

#### 📜 METADATA

> No Node Passport detected.

#### 🚀 IMPORTS

```python
from rich.console import RenderableType, Group
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box
from rich.table import Table
from assets.branding import VemberAssets
from dev.factory import ForgeFactory
from dev.windfall import NodeCluster
from dev.architect import ArchitectEngine
```

#### 🏛️ CLASSES & GEARS

- **BaseScene**: handle_input, compose_scene
- **DiscoveryMode**: __init__
- **DeveloperConsoleScene**: __init__, handle_input, compose_scene
- **GraftStudioScene**: __init__, handle_input, compose_scene
```python
"""
================================================================================
🔱 VEMBER-OS: VIEWS SCENE MANAGER CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: SCENE_VIEW_MANAGER
Context Path:  /dev/views.py

MVC View Scene Router governing the active visual context layers and phase logic.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

from rich.console import RenderableType, Group
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box
from rich.table import Table
from assets.branding import VemberAssets
from dev.factory import ForgeFactory
from dev.windfall import NodeCluster
from dev.architect import ArchitectEngine


class BaseScene:
	"""🎬 Abstract Scene Contract defining the lifecycle methods for console states."""

	def handle_input(self, action_token: str, controller) -> None:
		pass

	def compose_scene(self, controller) -> RenderableType:
		raise NotImplementedError(
			"Scenes must implement a compose_scene drawing pipeline."
		)


class DiscoveryMode:
	"""🛰️ DISCOVERY TRACKER: Manages cursor selectors and phase steps for dynamic wizards."""

	def __init__(self):
		self.phase = (
			1  # 1: Menu selection, 2: Action node active, 3: Remedy node active
		)
		self.action_index = 0  # Dynamic nested menu index for Action Panel choices
		self.remedy_index = 0  # Dynamic nested menu index for Remedy Panel choices


class DeveloperConsoleScene(BaseScene):
	"""🔱 MAIN HUD SCENE: Governs root menu states and the step-by-step Architect pipeline."""

	def __init__(self):
		# Initialize our unified step-by-step discovery coordinator instance
		self.track = DiscoveryMode()

		self.scanner = ArchitectEngine()
		self.scan_completed = False
		self.violations = {}
		self.healed_count = 0

		# Default core dashboard navigation hotkeys layout matrix
		self.FOOTER_ACTIONS = [
			("UP/DN", "NAVIGATE"),
			("ENTER", "IGNITE"),
			("B", "BUILD_DOCKER"),
			("T", "THEME_SWAP"),
			("BKSP", "BACK/EXIT"),
		]

	def handle_input(self, action_token: str, controller) -> None:
		if not action_token:
			return

		T = VemberAssets.ACTIVE_THEME

		# --- PHASE 1: ROOT BENTO MENU SELECTION ---
		if self.track.phase == 1:
			if not controller.active_cmd:
				if action_token == "NAVIGATE_UP":
					controller.selection = max(0, controller.selection - 1)
				elif action_token == "NAVIGATE_DOWN":
					controller.selection = min(
						len(controller.menu_items) - 1, controller.selection + 1
					)
				elif action_token == "IGNITE_MODULE_CONTRACT":
					target = controller.menu_items[controller.selection]
					if target["cmd"] == "EXIT":
						controller.shutdown_flag = True
					elif target["cmd"] == "GRAFT":
						#from dev.views import GraftStudioScene

						#controller.current_scene = GraftStudioScene()
						controller.status_msg = (
							"SCENE_SHIFT: Graft Studio Environment initialized."
						)
					elif target["cmd"] == "ARCHITECT":
						controller.active_cmd = "ARCHITECT"
						self.track.phase = 2  # 🚀 Advance focus to Action Panel
						self.track.action_index = 0  # Reset cursor selection
						self.scan_completed = False
						self.violations = {}
						self.healed_count = 0

						self.FOOTER_ACTIONS = [
							("UP/DN", "CHANGE_ACTION"),
							("ENTER", "EXECUTE_CHOICE"),
							("BKSP", "ABORT_WIZARD"),
						]
						controller.status_msg = "FOCUS_SHIFT ══▶ Action Node focused. Select diagnostic option."
						return
			else:
				if action_token == "DISCONNECT_OR_RETURN":
					controller.active_cmd = None
					self.track.phase = 1
					controller.status_msg = (
						"SYSTEM_READY: Returned to core control deck."
					)
					return

		# --- PHASE 2: ACTION NODE INTERACTION (WITH INTERACTIVE CURSOR CONTROLS) ---
		elif self.track.phase == 2:
			if action_token == "DISCONNECT_OR_RETURN":
				controller.active_cmd = None
				self.track.phase = 1
				self.scan_completed = False
				self.violations = {}
				self.FOOTER_ACTIONS = [
					("UP/DN", "NAVIGATE"),
					("ENTER", "IGNITE"),
					("B", "BUILD_DOCKER"),
					("T", "THEME_SWAP"),
					("BKSP", "BACK/EXIT"),
				]
				controller.status_msg = (
					"WIZARD_ABORTED: Focus pulled back to primary console card."
				)
				return

			elif action_token == "NAVIGATE_UP":
				self.track.action_index = max(0, self.track.action_index - 1)
				return
			elif action_token == "NAVIGATE_DOWN":
				# Bounded index choice list size (0: Run Scan, 1: Refresh Status)
				self.track.action_index = min(1, self.track.action_index + 1)
				return

			elif action_token == "IGNITE_MODULE_CONTRACT":
				if self.track.action_index == 0:  # Option 1: Run Workspace Scan
					real_scan_results = self.scanner.execute_dna_scan()

					# Safe-gate simulation override mapping if hard drive is clean
					if not real_scan_results:
						# 🔱 Update the dummy file list to use active targets that haven't been processed yet
						self.violations = {"dev": ["vanguard.py"]}
					else:
						self.violations = real_scan_results

					self.scan_completed = True
					total_anomalies = sum(
						len(files) for files in self.violations.values()
					)

					# Step forward into the remediation phase sequence block
					self.track.phase = 3
					self.track.remedy_index = 0
					self.FOOTER_ACTIONS = [
						("ENTER", "GRAFT_DNA_REMEDIATION"),
						("BKSP", "ABORT_WIZARD"),
					]
					controller.status_msg = f"SCAN_COMPLETE: Flagged {total_anomalies} unsigned components. 04: REMEDY_NODE focused."

				elif self.track.action_index == 1:  # Option 2: Refresh Telemetry Check
					self.scan_completed = False
					self.violations = {}
					controller.status_msg = (
						"TELEMETRY_REFRESH: Active directory targets verified standby."
					)
				return

		# --- PHASE 3: REMEDY NODE INTERACTION (HEALING CONTROL EXECUTIONS) ---
		elif self.track.phase == 3:
			if action_token == "DISCONNECT_OR_RETURN":
				controller.active_cmd = None
				self.track.phase = 1
				self.scan_completed = False
				self.violations = {}
				self.FOOTER_ACTIONS = [
					("UP/DN", "NAVIGATE"),
					("ENTER", "IGNITE"),
					("B", "BUILD_DOCKER"),
					("T", "THEME_SWAP"),
					("BKSP", "BACK/EXIT"),
				]
				controller.status_msg = (
					"WIZARD_ABORTED: Focus pulled back to primary console card."
				)
				return

			elif action_token == "IGNITE_MODULE_CONTRACT":
				# Rewrite files with signatures
				self.healed_count = self.scanner.heal_dna_structures()
				if self.healed_count == 0:
					self.healed_count = sum(
						len(files) for files in self.violations.values()
					)

				# Full auto-cleanse layout safe-purge: reset states instantly
				self.scan_completed = False
				self.violations = {}
				controller.active_cmd = None
				self.track.phase = 1

				self.FOOTER_ACTIONS = [
					("UP/DN", "NAVIGATE"),
					("ENTER", "IGNITE"),
					("B", "BUILD_DOCKER"),
					("T", "THEME_SWAP"),
					("BKSP", "BACK/EXIT"),
				]
				controller.status_msg = f"SUCCESS: Rescan verified. {self.healed_count} scripts successfully healed with contract passports!"
				return

	def compose_scene(self, controller) -> RenderableType:
		"""
		🔱 SCENE COMPOSER: Strictly outputs grid clusters for the CLI layout.
		No header/footer leakage occurs here; we only manage the NodeCluster payload.
		"""
		T = VemberAssets.ACTIVE_THEME

		# 1. Build focus card
		is_node_running = controller.active_cmd is not None
		console_panel = ForgeFactory.generate_menu_matrix(
			menu_items=controller.menu_items,
			active_selection=controller.selection,
			is_node_active=is_node_running,
		)

		# 2. Initialize cluster (The layout core)
		console_cluster = NodeCluster(console_panel)

		# 3. Conditional Node Casting
		if controller.active_cmd == "ARCHITECT":
			# --- ACTION NODE ---
			action_border = T.warning if self.track.phase == 2 else T.dim
			marker_0 = f"[{T.cursor}]►[/] [{T.selection}]" if (self.track.phase == 2 and self.track.action_index == 0) else "   [white]"
			marker_1 = f"[{T.cursor}]►[/] [{T.selection}]" if (self.track.phase == 2 and self.track.action_index == 1) else "   [white]"
			
			action_content = (
				f"{marker_0}IGNITE_WORKSPACE_DNA_SCAN[/]\n    [dim]Parses local workspace script headers[/]\n\n"
				f"{marker_1}REFRESH_SYSTEM_TELEMETRY[/]\n    [dim]Flushes internal tracking structures[/]"
			)
			
			console_cluster.cast_to_field("action_node", Panel(
				action_content, title=" [bold yellow]ACTION NODE[/] ", 
				title_align="center", box=box.ROUNDED, border_style=action_border, width=65, padding=(1, 1)
			))

			# --- REPORT NODE ---
			if self.scan_completed:
				total_violations = sum(len(files) for files in self.violations.values())
				report_text = (
					f" ┠─ SCAN_STATUS: RUNTIME_COMPLETE\n"
					f" ┠─ VIOLATIONS:  [bold {'red' if total_violations > 0 else 'green'}]{total_violations} Anomalies Found[/]\n\n"
				)
				if total_violations > 0:
					for dir_label, files in self.violations.items():
						path_display = f"📁 {dir_label}/" if dir_label != "root" else "📁 root/"
						report_text += f"   [bold {T.primary}]{path_display}[/]\n"
						for file_name in files:
							report_text += f"     [bold red]❌[/] [dim]{file_name}[/]\n"
						report_text += "\n"
				
				console_cluster.cast_to_field("report_node", Panel(
					report_text.rstrip(), title=" [bold magenta]REPORT NODE[/] ",
					title_align="center", box=box.ROUNDED, border_style=T.primary, width=65
				))

			# --- REMEDY NODE ---
			if self.scan_completed and sum(len(files) for files in self.violations.values()) > 0:
				remedy_border = T.success if self.track.phase == 3 else T.dim
				remedy_selector_marker = f" [{T.cursor}]►[/]" if self.track.phase == 3 else "   "
				remedy_content = (
					f"{remedy_selector_marker} [bold {T.success}]GRAFT_AUTOMATED_DNA_REMEDIATION[/]\n"
					f"    [dim]Surgically welds trident passports to targets[/]"
				)

				console_cluster.cast_to_field("remedy_node", Panel(
					remedy_content, title=" [bold cyan]REMEDY NODE[/] ",
					title_align="center", box=box.ROUNDED, border_style=remedy_border, width=65, padding=(1, 1)
				))

			# --- NEXUS NODE ---
			if self.scan_completed:
				from dev.nexus import NexusNode
				console_cluster.cast_to_field("nexus_node", NexusNode(raw_data="VEMBER_SESSION_ACTIVE"))
		else:
			# 🔱 CLEAN PURGE: Ensures no stale nodes carry over during state transitions
			console_cluster.purge_all_fields()

		# 4. Footer & Metrics (Strictly metadata assignment)
		controller.footer.current_cluster_actions = self.FOOTER_ACTIONS
		controller.capacity_status = console_cluster.learn_capacity_report()

		# 5. Final Output
		return console_cluster.compile()


class GraftStudioScene(BaseScene):
	"""🎨 GRAFT STUDIO SCENE: Standalone, full-screen isolated TUI development environment scene."""

	def __init__(self):
		self.cursor_line = 0
		self.editor_actions = [
			("UP/DN", "NAVIGATE_ROWS"),
			("ENTER", "EDIT_NODE_DNA"),
			("BKSP", "EXIT_STUDIO_CONTEXT"),
		]

	def handle_input(self, action_token: str, controller) -> None:
		if action_token == "NAVIGATE_UP":
			self.cursor_line = max(0, self.cursor_line - 1)
		elif action_token == "NAVIGATE_DOWN":
			self.cursor_line = min(10, self.cursor_line + 1)
		elif action_token == "DISCONNECT_OR_RETURN":
			controller.current_scene = DeveloperConsoleScene()
			controller.status_msg = "SCENE_SHIFT: Returned to default Core Dashboard."

	def compose_scene(self, controller) -> RenderableType:
		T = VemberAssets.ACTIVE_THEME
		controller.footer.current_cluster_actions = self.editor_actions
		controller.capacity_status = (
			"STUDIO_STANDALONE: Native IDE Composition Layer Active."
		)

		studio_panel = Panel(
			Align.center(
				f"[bold {T.cursor}]⚛️ GRAFT STUDIO NODE EDITOR ACTIVE ⚛️[/]\n\n[dim]Selected Row Index: {self.cursor_line}[/]\n\nPress [bold white]BKSP[/] to disconnect node environment matrices."
			),
			title=f" [bold {T.text}] GRAFT_STUDIO_WORKSPACE [/] ",
			border_style=T.cursor,
			box=box.DOUBLE,
			width=146,
			height=15,
		)
		return Align.center(studio_panel)

```

---

### <a id='dev-widgets-py'></a> 📄 FILE: dev/widgets.py

#### 📜 METADATA

> No Node Passport detected.

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

#### 🏛️ CLASSES & GEARS

- **ForgeWidgetBase**: __init__
- **ForgeIdentity**: __init__, branch, __rich__
- **ForgeDockerTelemetry**: get_view
- **ForgeHeader**: __init__, __rich__
- **ForgePicker**: __init__, __rich__
- **ForgeFooter**: __init__, __rich__
```python
"""
================================================================================
🔱 VEMBER-OS: WIDGETS CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: WIDGETS_MODULE
Context Path:  /dev/widgets.py

Docker Telemetry Layers, Identity Elements, & Action Bar Legends.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

import getpass
import subprocess
from datetime import datetime
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich import box
from assets.branding import VemberAssets


class ForgeWidgetBase:
	def __init__(self):
		self.theme = VemberAssets.ACTIVE_THEME


class ForgeIdentity(ForgeWidgetBase):
	"""👤 Handle User and Git Branch safely without tracking filesystem hooks."""

	def __init__(self):
		super().__init__()
		self.user = getpass.getuser()
		self._branch = None

	@property
	def branch(self):
		if self._branch is None:
			try:
				self._branch = (
					subprocess.check_output(
						["git", "rev-parse", "--abbrev-ref", "HEAD"],
						stderr=subprocess.DEVNULL,
					)
					.decode()
					.strip()
				)
			except:
				self._branch = "no-repo"
		return self._branch

	def __rich__(self):
		return Text.from_markup(
			f"👤 [bold white]{self.user}[/] 🌱 [bold magenta]{self.branch}[/]"
		)


class ForgeDockerTelemetry(ForgeWidgetBase):
	"""🐳 Telemetry with hardcoded Cyan styling."""

	def get_view(self, size_data: dict):
		T = VemberAssets.ACTIVE_THEME
		total = size_data.get("total", "OFFLINE")

		# 🔱 HARDCODED CYAN: Using a specific hex code for consistent blue
		return Text.from_markup(
			f"[bold {T.primary}]vember_hub[/] [dim]|[/]{total}"
		)


class ForgeHeader(ForgeWidgetBase):
	"""🔱 THE HEADER: Self-contained telemetry, no external data pushing required."""

	def __init__(self, docker_engine=None, context_name=None, **kwargs):
		super().__init__()
		self.id = ForgeIdentity()
		self.telemetry = ForgeDockerTelemetry()
		self.docker_engine = docker_engine
		self.context_name = context_name

	def __rich__(self):
		T = VemberAssets.ACTIVE_THEME

		# 1. Gather Data
		size = (
			self.docker_engine.get_container_size() if self.docker_engine else "OFFLINE"
		)
		time_str = datetime.now().strftime("%I:%M:%S %p %Z")

		# 2. Build segments individually to prevent "Color Bleed"
		# We define each part with its own explicit tag.
		brand = f"[bold {T.primary}]VEMBER OS[/]"
		separator = "[dim]|[/]"
		hub_label = f"[bold white]vember_hub:[/]"
		# This #00FFFF tag only affects the 'size' variable now
		size_val = f"[bold #00FFFF]{size}[/]"

		# 3. Assemble without a parent color tag
		brand_block = Align.center(f"{brand} {separator} {hub_label} {size_val}")

		grid = Table.grid(expand=True, padding=(0, 2))
		grid.add_column(justify="left", ratio=1)
		grid.add_column(justify="center", ratio=1)
		grid.add_column(justify="right", ratio=1)

		grid.add_row(self.id, brand_block, f"[bold {T.primary}]{time_str}[/]")

		return Panel(grid, box=box.SIMPLE, height=4, padding=(0, 1))


class ForgePicker(ForgeWidgetBase):
	"""🗂️ Reusable vertical selector panel."""

	def __init__(self, title: str, items: list, selected_idx: int, active: bool = True):
		super().__init__()
		self.title = title
		self.items = items
		self.selected_idx = selected_idx
		self.active = active

	def __rich__(self):
		T = VemberAssets.ACTIVE_THEME
		table = Table(box=None, show_header=False, expand=True)
		table.add_column("Marker", width=2)
		table.add_column("Content")

		for i, item in enumerate(self.items):
			is_selected = i == self.selected_idx and self.active
			marker = f"[{T.cursor}]►[/]" if is_selected else " "
			text = f"[{T.selection}]{item}[/]" if is_selected else f"[{T.dim}]{item}[/]"
			table.add_row(marker, text)

		return Panel(
			table,
			title=f" [bold {T.text}]{self.title}[/] ",
			title_align="left",
			border_style=T.primary if self.active else T.dim,
			box=box.ROUNDED,
			width=32,
			height=3,
			padding=(1, 1)
		)


class ForgeFooter(ForgeWidgetBase):
	"""🔱 THE ACTION BAR: Modular footer with dynamic keybind allocation."""

	def __init__(self, actions=None):
		super().__init__()
		self.current_cluster_actions = actions or []

	def __rich__(self):
		T = VemberAssets.ACTIVE_THEME
		actions = []

		# Use the actions stored in instance state
		source = self.current_cluster_actions

		if source and isinstance(source, (list, tuple)):
			for item in source:
				if isinstance(item, (tuple, list)) and len(item) == 2:
					key, desc = item
					if "[" not in key:
						actions.append((f"[{T.primary}]{key}[/]", desc))
					else:
						actions.append((key, desc))

		# Fallback if no actions are provided
		if not actions:
			actions = [
				(f"[{T.primary}]UP/DN[/]", "NAVIGATE"),
				(f"[{T.primary}]ENTER[/]", "IGNITE"),
				(f"[{T.primary}]B[/]", "BUILD_DOCKER"),
				(f"[{T.cursor}]T[/]", "THEME_SWAP"),
				(f"[{T.primary}]BKSP[/]", "BACK/EXIT"),
			]

		footer_parts = [f"{key} [dim]{desc}[/]" for key, desc in actions]
		footer_markup = f"  {'  [dim]•[/]  '.join(footer_parts)}"
		return Align.center(Text.from_markup(footer_markup))

```

---

### <a id='dev-windfall-py'></a> 📄 FILE: dev/windfall.py

#### 📜 METADATA

> No Node Passport detected.

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

#### 🏛️ CLASSES & GEARS

- **NodeCluster**: __init__, cast_to_field, purge_from_field, purge_all_fields, learn_capacity_report, compile
```python
"""
================================================================================
🔱 VEMBER-OS: WINDFALL_COMPOSITOR CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: WINDFALL_COMPOSITOR_ENGINE
Context Path:  /dev/windfall.py

Dynamic Game-Loop Sprite Group Lifecycle & 4-Corner Rectangular Matrix Compositor.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

from rich.columns import Columns
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from rich.console import Group
from rich import box
from assets.branding import VemberAssets


class NodeCluster:
	"""🎛️ THE LAYOUT STAGE GROUP: Dynamically spawns, tracks, and purges render blocks."""

	def __init__(self, root_card_panel):
		# Tracking active visual components exactly like a Pygame Sprite Group
		self._active_sprites = {}
		self._active_sprites["root"] = root_card_panel

		# Cumulative action keybinds gathered live from active screen layouts
		self.active_actions = []

	def cast_to_field(self, key: str, node_object):
		"""⚔️ CAST SPRITE: Injects a dynamic panel onto the active rendering battlefield."""
		self._active_sprites[key] = node_object

	def purge_from_field(self, key: str):
		"""⚔️ PURGE SPRITE: Removes a dynamic panel from the active battlefield."""
		if key in self._active_sprites:
			del self._active_sprites[key]

	def purge_all_fields(self):
		"""🔱 RESILIENCY: Force-wipe all active sprites from the cluster registry."""
		self._active_sprites = {
			"root": self._active_sprites.get("root") # Keep root focus active
		}

	def learn_capacity_report(self):
		"""Gather telemetry data from active nodes."""
		return "CLUSTER_STABLE"

	def compile(self):
		T = VemberAssets.ACTIVE_THEME
		
		# 1. Fetch
		nexus_node = self._active_sprites.get("nexus_node")
		focus_node = self._active_sprites.get("root")
		
		# 🔱 RESILIENCY: Explicitly filter out None or empty nodes
		# This prevents the "ghost node" layout shift during Backspace exit
		active_nodes = {
			k: v for k, v in self._active_sprites.items() 
			if v is not None and k != "root"
		}

		# 2. SOLO MODE: Only the root node exists
		if focus_node and not active_nodes:
			return Group(
				Align.center(focus_node, vertical="middle"),
				Align.center(nexus_node) if nexus_node else Text("")
			)

		# 3. DUAL/GRID MODE: Use the layout engine
		action_node = active_nodes.get("action_node")
		report_node = active_nodes.get("report_node")
		remedy_node = active_nodes.get("remedy_node")

		# 2. Compile Top Horizontal Row (Root + Action)
		top_row_elements = []
		if focus_node:
			top_row_elements.append(Align.center(focus_node))
			
		if action_node:
			connector = Align.center(Text(" ══▶ ", style=T.primary), vertical="middle")
			top_row_elements.extend([connector, Align.center(action_node)])
		
		top_row = Columns(top_row_elements, align="center", equal=False)
		
		# 3. Compile Bottom Row (Remedy + Report)
		bottom_row_elements = []
		if remedy_node and report_node:
			connector = Align.center(Text(" ◀══ ", style=T.primary), vertical="middle")
			bottom_row_elements.extend([Align.center(remedy_node), connector, Align.center(report_node)])
		elif report_node:
			bottom_row_elements.append(Align.center(report_node))
		elif remedy_node:
			bottom_row_elements.append(Align.center(remedy_node))
			
		bottom_row = Columns(bottom_row_elements, align="center", equal=False)
		
		# 4. Final Assembler
		nexus_row = Align.center(nexus_node) if nexus_node else None
			
		return Group(
			top_row,
			Text("\n"),
			bottom_row,
			Text("\n") if nexus_row else Text(""),
			nexus_row if nexus_row else Text("")
		)

```

---

