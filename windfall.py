"""
🔱 WINDFALL TRI-RENDER ENGINE (v1.0.0 Internal)
The Layout Compositor for Vember-OS.
Handles: Themes, State, Responsiveness, and Frame Generation.
"""
from io import StringIO
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
from branding import THEMES, LOGO_ANSI

class WindfallTUI:
	"""The Terminal Presentation Layer for the Tri-Render."""
	def __init__(self, theme_key="VEMBER_DARK"):
		self.theme = THEMES.get(theme_key, THEMES["VEMBER_DARK"])
		self.console = Console(
			file=StringIO(), 
			force_terminal=True, 
			width=120,
            color_system=None,  # 🔱 CRITICAL: This strips the ANSI chars
            legacy_windows=False # Ensures clean box-drawing characters
		)
		# Internal visibility state
		self.show_sidebar = True
		self.show_inspector = True

	def build_frame(self, width, height, components):
		"""
		Assembles components into a single 'Frame' (String).
		components: Dict of callables returning Rich objects (header, sidebar, etc.)
		"""
		# Update console dimensions for responsiveness
		self.console.width = width - 1
		self.console.height = height

		# 1. Initialize the Layout Grid
		root = Layout()
		
		# 2. Define the 3-Tier Column (Point 3 & 6 of Checklist)
		root.split_column(
			Layout(name="header", size=6),
			Layout(name="body"),
			Layout(name="footer", size=3)
		)

		# 3. Dynamic Body Composition (Point 2: State Management)
		body_elements = []
		if self.show_sidebar:
			body_elements.append(Layout(name="sidebar", ratio=1))
		if self.show_inspector:
			body_elements.append(Layout(name="inspector", ratio=2))
		
		# If both are hidden, the body remains empty or we could add a placeholder
		if body_elements:
			root["body"].split_row(*body_elements)

		# 4. Content Injection (Point 4: Theme Application)
		# Header (Logo + Subtitle)
		root["header"].update(
			Panel(
				Align.center(LOGO_ANSI, vertical="middle"), 
				border_style=self.theme.primary
			)
		)

		# Use root.get() to safely check for the sub-layouts
		sidebar_layout = root.get("sidebar")
		if sidebar_layout:
			sidebar_layout.update(
				Panel(components['sidebar'](), title="[ REGISTRY ]", border_style=self.theme.secondary)
			)

		inspector_layout = root.get("inspector")
		if inspector_layout:
			inspector_layout.update(
				Panel(components['inspector'](), title="[ INSPECTOR ]", border_style=self.theme.secondary)
			)

		# Footer
		root["footer"].update(
			Panel(components['footer'](), border_style=self.theme.primary)
		)

		# 5. Render to String Buffer
		self.console.file = StringIO()
		self.console.print(root)
		return self.console.file.getvalue()

class Windfall:
	"""The Master Compositor and Mode Switcher."""
	def __init__(self, theme_key="VEMBER_DARK"):
		self.active_mode = "TUI"
		self.tui = WindfallTUI(theme_key)

	def toggle_sidebar(self):
		self.tui.show_sidebar = not self.tui.show_sidebar

	def toggle_inspector(self):
		self.tui.show_inspector = not self.tui.show_inspector

	def switch_theme(self, theme_key):
		if theme_key in THEMES:
			self.tui.theme = THEMES[theme_key]

	def compose(self, width, height, components):
		"""Routes the composition to the active renderer."""
		if self.active_mode == "TUI":
			return self.tui.build_frame(width, height, components)
		# v2.0.0 will add 'elif self.active_mode == "2D":'
		return ""