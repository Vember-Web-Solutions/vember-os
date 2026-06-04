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
