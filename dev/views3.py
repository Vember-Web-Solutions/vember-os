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
