"""
🔱 VEMBER-OS KERNEL
Central execution engine. Manages Dashboard lifecycle, 
Telemetry streaming, and the Input Kernel.
"""

import time
import os
import sys
import queue
from rich.live import Live
from rich.console import Console

# Internal Engine Imports
from engine.input_handler import KeyListener
from engine.dashboards import MainDashboard
from engine.core import NodeScanner

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class VemberKernel:
	def __init__(self):
		self.console = Console()
		self.dash = MainDashboard()
		self.keyboard = KeyListener()
		self.refresh_rate = 0.05

	def startup(self):
		self.dash.nodes = self.dash.scanner.scan()
		if not self.dash.nodes:
			# Just trigger a toast instead of killing the OS
			self.dash.trigger_toast("WARNING: NO NODES DETECTED", duration=100)
			# Create a dummy node so the MeshMap doesn't crash on index lookup
			self.dash.nodes = [{"name": "OFFLINE", "path": "", "controls": {}}]

	def _update_telemetry(self):
		"""
		Drains the Node Runner queue.
		Implements Frame-Swapping logic via '--- REFRESH ---' tags.
		"""
		new_data = self.dash.runner.get_latest_output()
		if not new_data or not new_data.strip():
			return 

		if "--- REFRESH ---" in new_data:
			# 🔱 STABILITY: Only replace the buffer if we have a full new frame.
			# This prevents the 'flicker' or 'empty viewport' issues.
			parts = new_data.split("--- REFRESH ---")
			frame = parts[-2].strip()
			if frame:
				self.dash.output_buffer = frame
		else:
			# Standard append mode for logging/linear nodes
			self.dash.output_buffer += new_data

	def run(self):
		# 🔱 Removed manual clear: startup happens before we flip screens
		self.startup()
		
		try:
			# 🔱 THE FIX: Enter the Alternate Screen Buffer
			# This ensures that when the OS closes, your terminal scrollback is preserved
			with self.console.screen():
				
				# Initialize the first frame
				layout_map = self.dash.get_layout_map()
				frame = self.dash.windfall.compose(layout_map)

				# 🔱 Set screen=True in Live for proper sizing inside the alternate buffer
				with Live(frame, console=self.console, screen=True, auto_refresh=False) as live:
					while self.dash.running:
						# 1. Input Handoff
						try:
							key = self.keyboard.input_queue.get_nowait()
							self.dash.handle_input(key)
						except queue.Empty:
							pass
						
						# 2. Telemetry Bridge (Thermal Matrix -> OS Header)
						self._update_telemetry()
						
						# 3. Render Handoff
						# Re-calculate the map (handles Toast expiry and selection changes)
						current_map = self.dash.get_layout_map()
						live.update(self.dash.windfall.compose(current_map))
						live.refresh()
						
						time.sleep(self.refresh_rate)

		except KeyboardInterrupt:
			pass
		finally:
			# 🔱 Cleanup no longer needs console.clear() 
			# The .screen() context manager handles the "wipe" automatically
			self.cleanup()

	def cleanup(self):
		self.keyboard.stop()
		self.dash.runner.stop()

if __name__ == "__main__":
	kernel = VemberKernel()
	kernel.run()