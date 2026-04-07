"""
🔱 VEMBER-OS CORE DASHBOARD (v1.0.5 Patch)
The Primary Control Interface for the Node-Based Architecture.
Refactored for Native Input Kernel and Single-Drain Telemetry.
"""

import time
from rich.live import Live
from rich.console import Console
from windfall import Windfall
from core import NodeScanner
from runner import NodeRunner
from input_handler import KeyListener

class VemberDashboard:
	def __init__(self):
		self.scanner = NodeScanner()
		self.windfall = Windfall(theme_key="VEMBER_DARK")
		self.windfall.toggle_sidebar = True 
		
		self.runner = NodeRunner()
		self.console = Console()
		self.keyboard = KeyListener() 

		self.selected_index = 0
		self.running = True
		self.viewing_node = False # 🔱 NEW: Track if we are focused on a process
		self.nodes = []
		self.output_buffer = ""

	def handle_input(self):
		key = self.keyboard.get_key()
		if not key: return
		k = key.lower()

		# 🔱 GLOBAL: Always allow Shutdown
		if k == "q":
			self.running = False
			return

		# 🔱 CONTEXT: Inside a Node
		if self.viewing_node:
			if k == "\x1b": # ESC: Detach but keep running
				self.viewing_node = False
			elif k == "x": # New: Hard Kill process
				self.runner.stop()
				self.viewing_node = False
				self.output_buffer = "[bold red]SIGNAL: Process Terminated.[/]"

		# 🔱 CONTEXT: Main Dashboard
		else:
			if k in ["w", "\x1b[a"]: # Up
				if self.selected_index > 0:
					self.selected_index -= 1
			elif k in ["s", "\x1b[b"]: # Down
				if self.selected_index < len(self.nodes) - 1:
					self.selected_index += 1
			elif k in ["\n", "\r"]: # Enter
				self.viewing_node = True
				# Only execute if NOT already running
				if not self.runner.is_running:
					self.output_buffer = ""
					curr_node = self.nodes[self.selected_index]
					self.runner.execute(curr_node['path'])
				
	def update_logic(self):
		"""Single-Drain Telemetry Sync."""
		self.nodes = self.scanner.scan()
		
		# Pull everything currently in the pipe
		new_output = self.runner.get_latest_output()
		if not new_output:
			return

		if "--- REFRESH ---" in new_output:
			# Overwrite buffer with the most recent full frame
			parts = new_output.split("--- REFRESH ---")
			if len(parts) > 1:
				self.output_buffer = parts[-2].strip()
		else:
			# Append standard scrolling logs
			self.output_buffer += new_output

	def _get_sidebar_content(self):
		content = ""
		for i, node in enumerate(self.nodes):
			prefix = "▶ " if i == self.selected_index else "  "
			if i == self.selected_index:
				content += f"[bold cyan]{prefix}{node['name']}[/]\n"
			else:
				content += f"{prefix}{node['name']}\n"
		return content

	def _get_viewport_content(self):
		if self.viewing_node:
			return self.output_buffer
		
		status = "[bold cyan]Active in Background[/]" if self.runner.is_running else "Idle"
		return f"[dim]DASHBOARD MODE[/]\n[white]System Status: {status}[/]\n\nPress ENTER to focus view."

	def _get_footer_content(self):
		if self.viewing_node:
			return "[bold cyan]VIEWING NODE[/] | ESC Detach (Keep Running) | X Kill Process | Q Shutdown"
		
		nav = "W/S Navigate | ENTER Focus/Run | Q Shutdown"
		if self.runner.is_running:
			return f"[bold green]NODE ACTIVE[/] | {nav}"
		return f"[dim]{nav}[/]"

	def run(self):
		"""The Main Render Loop using Rich.Live."""
		components = {
			"sidebar": self._get_sidebar_content,
			"viewport": self._get_viewport_content,
			"footer": self._get_footer_content
		}

		try:
			with Live(
				self.windfall.compose(components), 
				console=self.console, 
				screen=True, 
				auto_refresh=False
			) as live:
				
				while self.running:
					# 🔱 Synchronous Input Handling
					self.handle_input()
					
					self.update_logic()
					
					live.update(self.windfall.compose(components))
					live.refresh()
					
					time.sleep(0.05) 

		finally:
			# 🔱 THE HAND-BACK SEQUENCE
			# Restores terminal TTY settings before the process exits
			self.keyboard.stop() 
			if self.runner.is_running:
				self.runner.stop()
			
			self.console.clear()
			print("[VEMBER-OS] Kernel Offline. Terminal Control Restored.")

if __name__ == "__main__":
	app = VemberDashboard()
	app.run()