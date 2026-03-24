"""
🔱 VEMBER-OS | WINDFALL ENGINE
File: tui.py
Author: Vember-Web-Solutions
Description: The primary TUI (Terminal User Interface) rendering backend. 
			Handles character-based box drawing, dynamic data injection, 
			and terminal-specific layout logic.
"""

from typing import Dict, Any

class TUIBackend:
	"""
	The TUI Rendering Engine for Windfall.
	
	This class acts as the 'Graphic Driver' for terminal-based displays. 
	It translates raw system data into formatted strings using 
	Unicode/ASCII character sets.
	"""

	def __init__(self, theme: str = "default"):
		"""
		Initializes the TUI Backend with a specific color/border theme.
		
		Args:
			theme: The visual aesthetic to apply to the rendered boxes.
		"""
		self.theme = theme
		self.borders = {
			"heavy": "┏━┓┃┗━┛",
			"light": "┌─┐│└─┘",
			"double": "╔═╗║╚═╝"
		}

	def render_box(self, title: str, content: str, width: int = 40) -> str:
		"""
		Renders a stylized 'Windfall' box for the terminal.
		
		Args:
			title: The text to display in the top border.
			content: The body text or data to wrap.
			width: The fixed width of the box.
			
		Returns:
			A string formatted with Unicode borders ready for the TUI.
		"""
		b = self.borders["light"]
		# Logic to calculate padding and draw the box
		header = f"{b[0]}─ {title} {'─' * (width - len(title) - 4)}{b[2]}"
		body = f"{b[3]} {content:<{width-4}} {b[3]}"
		footer = f"{b[4]}{'─' * (width - 2)}{b[5]}"
		
		return f"{header}\n{body}\n{footer}"
	
	def render_node_grid(self, nodes: list) -> str:
		"""
		Iterates through the ecosystem nodes and renders 
		individual Windfall boxes for each.
		"""
		grid_output = ""
		for node in nodes:
			name = node.get("name", "Unknown")
			state = node.get("state", "OFFLINE")
			
			# Rendering a more compact box for nodes
			grid_output += self.render_box(
				title=f"NODE: {name}", 
				content=f"STATE: {state}",
				width=35
			) + "\n"
			
		return grid_output