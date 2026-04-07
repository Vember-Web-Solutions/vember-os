"""
Vember-OS Weather App
---
Description: Local-first weather telemetry utilizing the DataHub service.
Category: Apps
Coord: 2,1
Version: 2.0.0
"""

from scripts.data_hub import DataHub
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

class WeatherNode:
	def __init__(self, location="New York"):
		self.location = location
		self.hub = DataHub()
		self.data = {}
		self.last_sync = "NEVER"
		self.unit = "F"

	def refresh(self):
		"""
		Polls the local DataHub for weather telemetry.
		Bypasses all networking issues by reading from the filesystem.
		"""
		# Request 'weather.json' payload from the Hub
		payload, sync_time = self.hub.read("weather")
		
		if payload is None:
			# sync_time will contain "FILE_MISSING" or "CORRUPT" from Hub
			self.data = {"error": f"State: {sync_time}"}
			return False

		try:
			# Map Open-Meteo Schema from the local JSON payload
			current = payload['current']
			daily = payload['daily']
			
			self.data = {
				"temp": current['temperature_2m'],
				"wind": current.get('wind_speed_10m', '--'),
				"desc": self._decode_weather_code(current['weather_code']),
				"forecast": []
			}
			
			# Map 3-day forecast
			for i in range(3):
				self.data["forecast"].append({
					"date": daily['time'][i],
					"max": daily['temperature_2m_max'][i],
					"min": daily['temperature_2m_min'][i]
				})
				
			self.last_sync = sync_time
			return True
		except KeyError as e:
			self.data = {"error": f"Schema Mismatch: {str(e)}"}
			return False

	def _decode_weather_code(self, code):
		"""Standard WMO Weather interpretation codes."""
		codes = {
			0: "Clear Sky", 1: "Mainly Clear", 2: "Partly Cloudy", 3: "Overcast",
			45: "Foggy", 51: "Drizzle", 61: "Rain", 71: "Snow", 80: "Showers", 95: "Storm"
		}
		return codes.get(code, "Cloudy")

	def render_viewport(self):
		"""Generates the Rich-formatted UI panel for the OS dashboard."""
		if "error" in self.data:
			err_msg = self.data.get("error", "Data Unavailable")
			return Panel(
				f"[bold red]OFFLINE[/bold red]\n[dim]{err_msg}[/dim]", 
				title="WEATHER.STATUS", 
				border_style="red"
			)

		# Main Layout Grid
		grid = Table.grid(expand=True)
		grid.add_column(ratio=1)

		# Current Weather Section
		header_text = Text.assemble(
			(f"{self.data['desc']}\n", "bold yellow"),
			(f"TEMP: {self.data['temp']}°{self.unit}\n", "bold white"),
			(f"LOC: {self.location.upper()}", "cyan")
		)
		
		grid.add_row(Panel(
			header_text, 
			title="WEATHER.TELEMETRY", 
			subtitle=f"SYNC: {self.last_sync}", 
			border_style="blue"
		))

		# Forecast Table
		forecast_table = Table(box=box.SIMPLE_HEAD, expand=True)
		forecast_table.add_column("Date", style="dim")
		forecast_table.add_column(f"Hi/Lo ({self.unit})", justify="right")

		for day in self.data.get("forecast", []):
			forecast_table.add_row(
				day['date'], 
				f"[red]{day['max']}°[/red] / [blue]{day['min']}°[/blue]"
			)
		
		grid.add_row(forecast_table)
		
		return Panel(grid, border_style="blue", padding=(0, 1))

if __name__ == "__main__":
	# Standalone execution test
	app = WeatherNode()
	app.refresh()
	console.clear()
	console.print(app.render_viewport())