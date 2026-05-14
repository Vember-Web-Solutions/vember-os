"""
🔱 VEMBER-OS: WINDFALL ENGINE
The Scene Compositor. Defines the physical layout architecture and 
orchestrates dynamic widget injection across named render zones.
"""

from rich.layout import Layout
from rich.console import Console
from rich.panel import Panel
from assets.branding import VemberAssets as Assets

class WindfallScene:
	"""🔱 BASE SCENE: The blueprint for different OS states."""
	def __init__(self):
		self.header = None
		self.aside = None
		self.viewport = None
		self.footer = None

	def sync(self, layout):
		"""Injects scene components into the physical layout slots."""
		if self.header: layout["header"].update(self.header)
		if self.aside:  layout["aside"].update(self.aside)
		if self.viewport: layout["viewport"].update(self.viewport)
		if self.footer: layout["footer"].update(self.footer)

class SceneManager:
	"""🔱 THE NAVIGATOR: Handles 'Fast Travel' and Scene transitions."""
	def __init__(self, windfall_instance):
		self.windfall = windfall_instance
		self.current_scene = None
		self.history = []

	def travel_to(self, scene: WindfallScene):
		"""Switches the entire UI state to a new scene."""
		self.current_scene = scene
		self.current_scene.sync(self.windfall.layout)


class Windfall:
	"""🔱 THE COMPOSITOR: Maintains the physical Grid/Layout structure."""

	def __init__(self):
		self.layout = Layout()
		self.manager = SceneManager(self)

	def _setup_responsive_layout(self, width: int):
		"""Configures the layout skeleton based on terminal width."""
		# Reset the base layout
		self.layout = Layout()

		# 1. Vertical Split
		self.layout.split_column(
			Layout(name="header", size=3),
			Layout(name="body"),
			Layout(name="footer", size=3)
		)

		# 2. Horizontal Body Split (Responsive logic)
		if width > 110:
			self.layout["body"].split_row(
				Layout(name="viewport", ratio=3),
				Layout(name="aside", ratio=1)
			)
		else:
			# Purge 'aside' for small screens to prevent clipping
			self.layout["body"].split_row(
				Layout(name="viewport")
			)

	def compose(self, layout_map, width=120):
		"""🔱 THE INJECTOR: Rebuilds layout and injects widgets."""
		self._setup_responsive_layout(width)

		for slot_name, factory in layout_map.items():
			try:
				# Access the named slot from the newly built layout
				target_layout = self.layout[slot_name]
				content = factory() if callable(factory) else factory
				target_layout.update(content)
			except (KeyError, AttributeError):
				# This is why the responsive purge works: 
				# if 'aside' doesn't exist in the layout, we just skip it.
				continue
				
		return self.layout

	def get_renderable(self):
		return self.layout
