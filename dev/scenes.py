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
from dev.views import BaseView, DiscoveryMode
from dev.vanguard import Vanguard


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

		self.controller.footer.current_cluster_actions = self.footer_actions


class ArchitectScene(DevScene):
	"""Architect district scene driven by the shared DiscoveryMode state machine."""

	def __init__(self, controller):
		super().__init__(controller)
		self.discovery = DiscoveryMode()
		self.footer_actions = [
			("ENTER", "IGNITE"),
			("B", "BUILD_DOCKER"),
			("BKSP", "BACK/EXIT"),
		]

	def phases(self, action_token: str) -> None:
		self.discovery.phases(action_token, self.controller)

	def populate_nodes(self, cluster: NodeCluster):
		cluster.purge_all_fields()
		cluster.cast_to_field("root", self.discovery.ae.render())
		self.controller.footer.current_cluster_actions = self.footer_actions


class VanguardScene(DevScene):
	"""Vanguard district scene for integrity and dependency telemetry."""

	def __init__(self, controller):
		super().__init__(controller)
		self.vanguard = controller.nodes.get("VANGUARD") or Vanguard()

	def populate_nodes(self, cluster: NodeCluster):
		cluster.purge_all_fields()
		cluster.cast_to_field("root", self.vanguard.render())
		self.controller.footer.current_cluster_actions = self.footer_actions
