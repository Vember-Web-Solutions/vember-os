"""
🔱 VEMBER-OS: THERMAL MATRIX
Kernel-integrated system monitor. Provides high-resolution 
vitals tracking and hardware thermal mapping.
"""

import psutil
import time
import sys
from collections import deque

class ThermalNode:
	def __init__(self):
		self.log = deque(maxlen=5)
		self.log.append("Core Telemetry Online.")
		self.core_count = 12

	def get_package_temp(self):
		"""Polls hardware sensors for the primary CPU package temperature."""
		temps = psutil.sensors_temperatures()
		if not temps: return 0.0
		# Check common driver keys
		for key in ['k10temp', 'coretemp', 'cpu_thermal', 'package id 0']:
			if key in temps: return temps[key][0].current
		return list(temps.values())[0][0].current

	def render(self):
		# 1. Hardware Poll
		per_core = psutil.cpu_percent(interval=0.2, percpu=True)
		per_core = (per_core + [0]*self.core_count)[:self.core_count]
		avg_load = sum(per_core) / len(per_core)
		temp = self.get_package_temp()

		# 2. Viewport Output (Raw Rich-tagged text)
		print(" [bold cyan]CORE TELEMETRY GRID[/]")
		print(" [dim]" + "—" * 30 + "[/]")
		for i in range(0, self.core_count, 3):
			row = [f"C{j+i:02d}: [bold]{per_core[j+i]:>3.0f}%[/]" for j in range(3)]
			print(f"  {'  '.join(row)}")

		print(f"\n [bold yellow]SYSTEM LOG[/]")
		for entry in self.log:
			print(f"  [dim]❯[/] {entry}")

		# 3. 🔱 The Vember Handshake
		sys.stdout.write(f"||DATA|{avg_load:.1f}|{temp:.1f}||\n")
		sys.stdout.write("--- REFRESH ---\n")
		sys.stdout.flush()

	def run(self):
		while True:
			self.render()
			time.sleep(0.1)

if __name__ == "__main__":
	ThermalNode().run()