"""
🔱 VEMBER-OS: WIDGET LIBRARY
A standardized UI component set. Implements inheritance-based 
rendering for spatial cards, inspectors, and status indicators.
"""

from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.padding import Padding
from rich.align import Align
from rich.console import Group
from datetime import datetime
from assets.branding import VemberAssets

class WindfallElement:
	"""🔱 THE ANCESTOR: Handles common 'Vember' styling and focus logic."""
	def __init__(self, title="", is_focused=False):
		self.title = title
		self.is_focused = is_focused
		self.theme = VemberAssets.THEME
		self.icons = VemberAssets.Icons

	def wrap(self, content):
		"""Standardized wrapper for the 'Modern' look."""
		return Panel(
			content,
			title=f"[bold]{self.title}[/]" if self.title else None,
			# Selection Glow: primary color + double lines when focused
			border_style=self.theme.primary if self.is_focused else self.theme.dim,
			box=box.DOUBLE if self.is_focused else box.ROUNDED,
			padding=(0, 1)
		)

# --- REFACTORED COMPONENTS ---

class OSHeader(WindfallElement):
	def __init__(self, cpu=0.0, ram=0.0):
		super().__init__()
		self.cpu = cpu
		self.ram = ram

	def __rich__(self):
		grid = Table.grid(expand=True)
		# ... columns setup ...
		grid.add_column(justify="left", ratio=1)
		grid.add_column(justify="center", ratio=2)
		grid.add_column(justify="right", ratio=1)

		# FIX: Changed 'active_theme' to 'self.theme'
		stats = f"[{self.theme.primary}]CPU:[/] {self.cpu:>3.0f}% [{self.theme.secondary}]RAM:[/] {self.ram:>3.0f}%"
		title = f"[bold {self.theme.primary}]🔱 VEMBER-OS[/]"
		clock = datetime.now().strftime("%I:%M:%S %p")

		grid.add_row(stats, title, clock)
		return grid

class OSToast(WindfallElement):
	"""🔱 SYSTEM NOTIFICATION: A slim, high-priority alert widget."""
	def __init__(self, message=None, **kwargs):
		super().__init__(**kwargs)
		self.message = message

	def __rich__(self):
		if not self.message:
			return "" # Return empty so it doesn't take up layout space
			
		# Toasts usually look best centered and bold
		return self.wrap(Align.center(f"[bold]{self.message}[/]"))

class OSFooter(WindfallElement):
	"""🔱 COMMAND BAR: A dynamic tooltip that pops up when needed."""
	def __init__(self, actions=None, **kwargs):
		super().__init__(**kwargs)
		self.actions = actions

	def __rich__(self):
		if not self.actions: return ""
		
		# Build horizontal command list: [A] NAVIGATE  [ENTER] SELECT
		commands = [f"[{self.theme.primary}][{k}][/] [dim]{v}[/]" for k, v in self.actions.items()]
		return Align.center(Padding("  ".join(commands), (0, 1)))

class OSActionMenu(WindfallElement):
	"""🔱 SIDEBAR: The source of truth for Node details and commands."""
	def __init__(self, node_data, **kwargs):
		name = node_data.get('name', 'SYSTEM').upper()
		super().__init__(title=f"ACTIONS: {name}", **kwargs)
		self.node = node_data

	def __rich__(self):
		# Pull description from the metadata we scanned
		desc = f"[dim italic]{self.node.get('description', 'No metadata available.')}[/]\n"
		
		# Static action hints (we can make these dynamic later)
		actions = [
			f"[{self.theme.primary}][ENTER][/] Launch", 
			f"[{self.theme.secondary}][V][/] Source",
			f"[{self.theme.dim}][X][/] Terminate"
		]
		
		return self.wrap(Group(desc, Padding("\n".join(actions), (1, 0))))

class OSCard(WindfallElement):
	"""🔱 NODE COMPONENT: Displays identity and real-time status."""
	def __init__(self, title, is_running=False, icon="?", is_focused=False, **kwargs):
		super().__init__(title=f"{icon} {title}", is_focused=is_focused, **kwargs)
		self.is_running = is_running

	def __rich__(self):
		# 🔱 LOGIC: 
		# Focused = Primary Color (Cyan/White)
		# Running (Background) = Secondary Color (Blue/Green)
		# Standby = Dim
		
		if self.is_focused:
			style = self.theme.primary
			status_text = "● ACTIVE"
		elif self.is_running:
			style = self.theme.secondary
			status_text = "● RUNNING"
		else:
			style = "dim"
			status_text = "○ READY"
		
		content = Align.center(
			f"\n[{style}]{status_text}[/]",
			vertical="middle"
		)
		return self.wrap(content)

class OSMeshConnector(WindfallElement):
	"""The 'Peer-to-Peer' lines that build the decentralized web."""
	def __init__(self, active=False, vertical=False):
		super().__init__()
		self.active = active
		self.char = "┃" if vertical else "━━━━"

	def __rich__(self):
		# FIX: Use self.theme inherited from WindfallElement
		style = self.theme.primary if self.active else self.theme.dim
		return f"[{style}]{self.char}[/]"

class OSMeshMap(WindfallElement):
	def __init__(self, active_index=0, running_index=None):
		super().__init__(title="NEURAL MESH")
		self.active_index = active_index
		self.running_index = running_index

	def __rich__(self):
		grid = Table.grid(expand=True, padding=1)
		grid.add_column(justify="center", ratio=1)
		grid.add_column(justify="center", ratio=1) # Connector col
		grid.add_column(justify="center", ratio=1)

		# 🔱 Determine states for each card
		weather = OSCard(
			"STRATOS", 
			icon=self.icons.TEMP,
			is_focused=(self.active_index == 0),
			is_running=(self.running_index == 0)
		)
		
		hub = OSCard(
			"CORE", 
			icon=self.icons.HUB,
			is_focused=(self.active_index == 1),
			is_running=(self.running_index == 1)
		)
		
		# The dynamic connector from our previous logic
		connector = "[cyan]━━━━[/]" if (self.active_index < 2) else "[dim]━━━━[/]"
		grid.add_row(weather, connector, hub)

		return self.wrap(grid)

class OSNodeInspector(WindfallElement):
	"""🔱 TERMINAL: The 'Zoomed In' view when a node is active."""
	def __init__(self, node_name, output="", **kwargs):
		super().__init__(title=f"STREAMS: {node_name}", is_focused=True, **kwargs)
		self.output = output

	def __rich__(self):
		# Display the last 12 lines of process output
		lines = self.output.split("\n")[-12:]
		content = "\n".join([f"[dim]>[/] {line}" for line in lines if line.strip()])
		return self.wrap(content if content else "[dim italic]Waiting for telemetry...[/]")

class OSWeatherDisplay:
	@staticmethod
	def render(data, location):
		# We reuse the new OSCard widget for consistency
		header = OSCard(
			title=f"{data['temp']}°F", 
			description=f"LOC: {location} | STAT: {data['desc']}",
			icon="❄️", 
			is_focused=True # Highlighted because it's the active focus
		)
		return header