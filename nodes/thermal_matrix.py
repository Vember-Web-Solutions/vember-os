"""
🔱 VEMBER-OS: THERMAL_MATRIX
Metadata: Enter summary of THERMAL_MATRIX functionality here.
"""
"""
🔱 VEMBER OS
"""
"""
🔱 VEMBER-OS: THERMAL MATRIX
Description: Kernel-integrated system monitor using Vember Extensions.
"""

import psutil
import time
import sys
from collections import deque
from rich.console import Group
from rich.panel import Panel
from engine.extensions import Sparkline, StatusMetric, NetworkStream
from dataclasses import dataclass, field

@dataclass
class ThermalState:
	"""Structured telemetry for v0.1.1a10"""
	cpu_percent: float = 0.0
	temp_celsius: float = 0.0
	fan_speed: float = 0.0
	net_iface: str = "eth0"
	net_speed_up: float = 0.0
	net_speed_dn: float = 0.0
	uptime: float = field(default_factory=time.time)

class ThermalNode:
	def __init__(self):
		# The Data Store
		self.state = ThermalState()
		# 1. Initialize Extensions (The "Eyes")
		self.cpu_load = StatusMetric("CPU TOTAL", color="green")
		self.temp_viz = StatusMetric("CORE TEMP", color="yellow")
		self.fan_viz  = Sparkline("FAN CURVE", color="blue")
		
		# Detect Network Interface (Simplified)
		ifaces = psutil.net_if_addrs()
		self.active_iface = "wlan0" if "wlan0" in ifaces else "eth0"
		self.net_viz  = NetworkStream(self.active_iface, ssid="VEMBER-MESH", color="magenta")
		
		self.log = deque(maxlen=3)
		self.log.append("Core Telemetry Online.")

	def poll(self):
		self.state.cpu_percent = psutil.cpu_percent()
		self.state.temp_celsius = self.get_package_temp()
		
		# Ensure these names match your __init__
		self.cpu_load.update(self.state.cpu_percent) 
		self.temp_viz.update(self.state.temp_celsius)
		self.fan_viz.update(self.state.cpu_percent)

	def get_package_temp(self):
		temps = psutil.sensors_temperatures()
		if not temps: return 0.0
		for key in ['k10temp', 'coretemp', 'cpu_thermal', 'package id 0']:
			if key in temps: return temps[key][0].current
		return 0.0

	def update_telemetry(self):
		"""Polls hardware and pushes to Extensions."""
		# CPU/Temp
		cpu = psutil.cpu_percent()
		temp = self.get_package_temp()
		self.cpu_load.update(cpu)
		self.temp_viz.update(temp)
		
		# Network (Get delta)
		net = psutil.net_io_counters(pernic=True).get(self.active_iface)
		if net:
			# We push the raw bytes; the extension handles the 'flow'
			self.net_viz.update(net.bytes_sent + net.bytes_recv)

	def render(self):
		"""Returns a Rich-compatible Panel for Windfall"""
		# Ensure data is fresh
		self.poll()

		# Build the Viewport content
		content = Group(
			self.cpu_bar,
			self.temp_bar,
			"",
			self.fan_viz
		)

		return Panel(
			content,
			title="🔱 [bold]THERMAL MATRIX[/]",
			border_style="bright_blue",
			padding=(1, 2)
		)

	def run(self):
		# In v0.1.1a10, the 'Runner' or 'Windfall' handles the loop.
		# But for standalone testing:
		from rich.live import Live
		with Live(self.render(), refresh_per_second=4) as live:
			while True:
				live.update(self.render())
				time.sleep(0.2)

if __name__ == "__main__":
	ThermalNode().run()