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
