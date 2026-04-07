"""
🔱 VEMBER-OS: STRATOS-LINK
Description: Atmospheric telemetry engine. Handles satellite weather relays and environmental data ingestion via the Vember Data Protocol.
"""

import time
import sys
import shutil
from rich.console import Console
from scripts.data_hub import DataHub
from engine.widgets import OSWeatherDisplay

class WeatherNode:
	def __init__(self, location="NEW YORK"):
		self.hub = DataHub()
		self.location = location.upper()
		self.unit = "F"
		self.data = {}
		
		self.full_width = shutil.get_terminal_size().columns
		self.safe_width = max(50, self.full_width - 35) 
		
		self.console = Console(force_terminal=True, width=self.safe_width, color_system="standard")

	def update(self):
		"""Gather and format data for the component."""
		try:
			payload, sync_time = self.hub.read("weather")
			if payload:
				self.data = {
					"temp": payload.get('temperature', 0),
					"desc": payload.get('description', 'Unknown'),
					"humidity": payload.get('humidity', '--'),
					"forecast": payload.get('forecast', [
						{"date": "MON", "max": 52, "min": 40, "desc": "Clear"},
						{"date": "TUE", "max": 48, "min": 38, "desc": "Cloudy"},
						{"date": "WED", "max": 55, "min": 42, "desc": "Rain"}
					])
				}
				return True
			return False
		except Exception as e:
			self.console.print(f"[red]LINK ERROR:[/] {e}")
			return False

	def render(self):
		"""Render using the shared Windfall Component."""
		if not self.data: return

		# 1. Capture the UI from the component
		ui = OSWeatherDisplay.render(self.data, self.location)
		
		# 2. Print using the CONSTRAINED console
		self.console.print(ui)
		
		# 3. 🔱 THE HIDDEN HANDSHAKE
		# Ensure this is a clean line so the Dashboard can parse and hide it
		sys.stdout.write(f"\n||DATA|0.0|{self.data.get('temp', 0)}||\n")

	def run(self):
		while True:
			if self.update():
				self.render()
			
			# The heartbeat tag for the Dashboard
			sys.stdout.write("--- REFRESH ---\n")
			sys.stdout.flush()
			time.sleep(5)

if __name__ == "__main__":
	WeatherNode().run()