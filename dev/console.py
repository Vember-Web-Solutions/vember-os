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
from dev.factory import ForgeFactory

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
		self.factory = ForgeFactory()
		self.view_container = DeveloperView(self)

		self.current_scene = self.router.get_view("dev")

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
				self.master_layout['header'].update(self.header)
				self.master_layout['body'].update(self.view_container.compose_view(self, self.current_scene))
				time.sleep(0.05)

	def ignite_module_contract(self):
		"""🔱 IGNITION: Transitions selection from Registry to Action Node."""
		try:
			# 1. Map current selection to Node Name
			selected_node = self.controller.menu_items[self.controller.selection]

			# 2. THE RITUAL OF ENTRY: Handle specific node initialization
			if selected_node.get("cmd") == "ARCHITECT":
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

	def transition_to_view(self, scene_key: str) -> None:
		"""Route the active viewport back to a registered scene."""
		scene = self.router.get_view(scene_key)
		if scene is not None:
			self.current_scene = scene
			self.active_cmd = None
			self.status_msg = f"VIEW_TRANSITION: Routed to {scene_key.upper()}"

	def switch_node(self, node_name):
		"""The central hub for state transitions."""
		if node_name in self.nodes:
			self.current_node = node_name

def main():
	cli = VemberConsole()
	cli.run()


if __name__ == "__main__":
	main()
