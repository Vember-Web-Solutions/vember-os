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
