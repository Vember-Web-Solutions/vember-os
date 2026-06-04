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
		self.theme = VemberAssets.THEME


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
		T = VemberAssets.THEME
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
		T = VemberAssets.THEME

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
		T = VemberAssets.THEME
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
		T = VemberAssets.THEME
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
