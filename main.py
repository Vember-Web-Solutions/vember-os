"""
🔱 VEMBER-OS: KERNEL
Central execution engine. Orchestrates the dashboard lifecycle, 
asynchronous telemetry streaming, and the input kernel.
"""

import asyncio
import os
import sys
import queue
from rich.live import Live
from rich.console import Console

# Internal Engine Imports
from engine.input_handler import KeyListener
from engine.dashboards import MainDashboard
from engine.core import NodeScanner, NodeRunner

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class VemberKernel:
	def __init__(self):
		self.console = Console()
		self.dash = MainDashboard()
		self.keyboard = KeyListener()
		self.refresh_rate = 0.05

	async def startup(self):
		# 🔱 THE FIX: We must 'await' the async scan
		self.dash.nodes = await self.dash.scanner.scan()

		if not self.dash.nodes:
			self.dash.trigger_toast("WARNING: NO NODES DETECTED", duration=100)
			self.dash.nodes = [{"name": "OFFLINE", "path": "", "controls": {}}]

	def _update_telemetry(self):
		# Keep this sync for now unless get_latest_output becomes a coroutine
		new_data = self.dash.runner.get_latest_output()
		if not new_data or not new_data.strip():
			return

		if "--- REFRESH ---" in new_data:
			parts = new_data.split("--- REFRESH ---")
			frame = parts[-2].strip()
			if frame:
				self.dash.output_buffer = frame
		else:
			self.dash.output_buffer += new_data

	async def run(self):
		# 🔱 Startup is now awaited
		await self.startup()

		try:
			with self.console.screen():
				layout_map = self.dash.get_layout_map()
				frame = self.dash.windfall.compose(layout_map)

				with Live(
					frame, console=self.console, screen=True, auto_refresh=False
				) as live:
					while self.dash.running:
						# 1. Input Handoff
						try:
							key = self.keyboard.input_queue.get_nowait()
							self.dash.handle_input(key)
						except queue.Empty:
							pass

						# 2. Telemetry Bridge
						self._update_telemetry()

						# 3. Render
						current_map = self.dash.get_layout_map()
						live.update(
							self.dash.windfall.compose(
								current_map, width=self.console.width
							)
						)
						live.refresh()

						# 🔱 Use async sleep to yield control to the event loop
						await asyncio.sleep(self.refresh_rate)

		except KeyboardInterrupt:
			pass
		finally:
			self.cleanup()

	def cleanup(self):
		self.keyboard.stop()
		# If your new NodeRunner has a shutdown method, call it here
		if hasattr(self.dash.runner, "shutdown"):
			self.dash.runner.shutdown()
		else:
			self.dash.runner.stop()


if __name__ == "__main__":
	kernel = VemberKernel()
	# 🔱 Start the OS inside the Asyncio Event Loop
	asyncio.run(kernel.run())
