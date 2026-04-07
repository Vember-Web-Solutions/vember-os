"""
🔱 WINDFALL TRI-RENDER ENGINE (v2.0.0)
The Scene Compositor and Navigation Orchestrator for VEMBER-OS.
"""
from rich.layout import Layout
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

		self.layout.split_column(
			Layout(name="header", size=3), # Tighter header for Modern UI
			Layout(name="body"),
			Layout(name="footer", size=3)
		)
		self.layout["body"].split_row(
		Layout(name="viewport", ratio=3), # Mesh stays on the left (75% width)
		Layout(name="aside", ratio=1)     # Action Sidebar on the right (25% width)
	)

	def compose(self, layout_map):
		"""
		🔱 THE INJECTOR: Safely maps widgets to named slots.
		Fixes the KeyError by accessing named slots directly.
		"""
		for slot_name, factory in layout_map.items():
			try:
				# We access the sub-layout by name directly
				target_layout = self.layout[slot_name]
				
				# Execute the lambda to get the Rich renderable
				content = factory() if callable(factory) else factory
				target_layout.update(content)
			except KeyError:
				# Silently skip slots that don't exist in this specific layout
				# This prevents the 'KeyError: 0' crash
				continue
				
		return self.layout
		
		# Initialize the Manager
		self.manager = SceneManager(self)

	def get_renderable(self):
		return self.layout