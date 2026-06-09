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
			from dev.scenes import ArchitectScene, VanguardScene

			if actual_key == "dev":
				self._cache[actual_key] = MainMenuScene(self.controller, None)
			elif actual_key == "architect":
				self._cache[actual_key] = ArchitectScene(self.controller)
			elif actual_key == "vanguard":
				self._cache[actual_key] = VanguardScene(self.controller)

		return self._cache.get(actual_key)


class DeveloperView(BaseView):
	"""🔱 CONTAINER: Manages layout, footer, and menu orchestration."""

	def compose_view(self, controller, current_scene) -> RenderableType:
		# 1. Boilerplate: Header and Footer
		# Ensure your footer is accessible on the controller object
		header = ForgeHeader(
			docker_engine=controller.docker_engine,
			context_name="DEVELOPER_CORE",
			title="DEVELOPER CONSOLE",
			version="v1.0.6-stable",
		)
		footer_actions = controller.footer.current_cluster_actions or getattr(
			current_scene, "footer_actions", None
		)
		footer = ForgeFooter(actions=footer_actions)

		cluster = NodeCluster(None)

		# 3. Payload Injection
		# The scene 'payload' adds its specific panels to the cluster
		if hasattr(current_scene, "populate_nodes"):
			current_scene.populate_nodes(cluster)

		# 4. Assemble into a full layout
		# Return a Group to render the vertical stack (Header -> Cluster -> Footer)
		return Group(header, Align.center(cluster.compile()), footer)
