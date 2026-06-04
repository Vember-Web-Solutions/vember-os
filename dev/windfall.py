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
		T = VemberAssets.THEME
		
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
