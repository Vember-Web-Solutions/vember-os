"""
🔱 VEMBER-OS | WINDFALL ENGINE
File: windfall.py
Author: Vember-Web-Solutions
Description: The Universal Display Server (UDS) for the Vember Ecosystem. 
			Coordinates high-level draw calls from the OS Core to 
			mode-specific rendering backends (TUI, 2D, 3D).
"""

from typing import Dict, Any, Optional
from vember_core.engine.backends.tui import TUIBackend

class Windfall:
	"""
	The main routing interface for all Vember-OS visual output.
	
	Windfall abstracts the rendering hardware/methodology away from the 
	applications. Whether an app is running in a terminal or a VR 
	headset, it calls the same Windfall methods.
	"""

	def __init__(self, mode: str = "tui"):
		"""
		Initializes the Windfall Router and selects the active backend.
		
		Args:
			mode: The display mode to initialize ("tui", "2d", or "3d").
		"""
		self.mode = mode.lower()
		
		# Backend Initialization
		# ARCHITECTURE NOTE: We lazy-load backends here to keep the 
		# startup footprint minimal, especially for TUI-only nodes.
		self.tui: Optional[TUIBackend] = None
		
		if self.mode == "tui":
			self.tui = TUIBackend()
		elif self.mode == "2d":
			# Future: Initialize SDL2 / Pygame backend
			pass
		elif self.mode == "3d":
			# Future: Initialize Vulkan / Godot / Custom VR backend
			pass

	def draw_component(self, component_type: str, data: Dict[str, Any]) -> str:
		"""
		The universal entry point for drawing UI elements or game assets.
		
		This method routes the request to the active backend.
		
		Args:
			component_type: The identifier for the UI element (e.g., 'header', 'node_grid').
			data: A dictionary containing the dynamic values to be rendered.
			
		Returns:
			The rendered output (typically a string for TUI, or a surface/buffer for others).
		"""
		if self.mode == "tui" and self.tui:
			return self._dispatch_tui(component_type, data)
		
		return f"[Windfall Error]: Mode '{self.mode}' not implemented for component '{component_type}'."

	def _dispatch_tui(self, component_type: str, data: Dict[str, Any]) -> str:
		"""Internal dispatcher for TUI rendering."""
		if component_type == "header":
			# Map 'header' to the render_box method
			return self.tui.render_box(
				title=data.get("title", "Vember-OS"),
				content=f"Status: {data.get('status', 'Unknown')}"
			)
		
		# Fix for the 'node_grid' error in your last screenshot
		elif component_type == "node_grid":
			nodes = data.get("nodes", [])
			return self.tui.render_node_grid(nodes)
			
		return f"<!> Unknown TUI Component: {component_type}"
