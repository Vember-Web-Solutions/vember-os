"""
🔱 WINDFALL TRI-RENDER ENGINE (v1.0.5 Patch)
The Layout Compositor for Vember-OS.
Transitioned to Native Rich rendering.
"""
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
from branding import THEMES, LOGO_ANSI

class WindfallTUI:
	"""The Terminal Presentation Layer for the Tri-Render."""
	def __init__(self, theme_key="VEMBER_DARK"):
		self.theme = THEMES.get(theme_key, THEMES["VEMBER_DARK"])
		
		# 🔱 1.0.5 Shift: Removed StringIO and manual Console.
		# Logic: Rich Live/Console will now manage the draw-calls directly.
		
		self.show_sidebar = True

	def build_frame(self, components):
		root = Layout()
		
		# 1. Primary Vertical Split
		root.split_column(
			Layout(name="header", size=6),
			Layout(name="body"),
			Layout(name="footer", size=3)
		)

		# 2. Body Configuration (Viewport is Anchor)
		body_elements = []
		if self.show_sidebar:
			body_elements.append(Layout(name="sidebar", ratio=1))
		
		body_elements.append(Layout(name="viewport", ratio=2))
		
		root["body"].split_row(*body_elements)

		# 3. Component Rendering
		root["header"].update(
			Panel(Align.center(LOGO_ANSI, vertical="middle"), border_style=self.theme.primary)
		)

		if self.show_sidebar:
			root["sidebar"].update(
				Panel(components['sidebar'](), title="[ NODES ]", border_style=self.theme.secondary)
			)

		# The permanent Viewport
		root["viewport"].update(
			Panel(components['viewport'](), title="[ VIEWPORT ]", border_style=self.theme.secondary)
		)

		root["footer"].update(
			Panel(components['footer'](), border_style=self.theme.primary)
		)

		# 🔱 Return the Layout Object directly
		return root

class Windfall:
	"""The Master Compositor and Mode Switcher."""
	def __init__(self, theme_key="VEMBER_DARK"):
		self.active_mode = "TUI"
		self.tui = WindfallTUI(theme_key)

	def toggle_sidebar(self):
		self.tui.show_sidebar = not self.tui.show_sidebar

	def switch_theme(self, theme_key):
		if theme_key in THEMES:
			self.tui.theme = THEMES[theme_key]

	def compose(self, components):
		"""Routes the composition to the active renderer."""
		if self.active_mode == "TUI":
			return self.tui.build_frame(components)
		return None