"""
🔱 VEMBER-OS: TASK SCHEDULER
The system heartbeat. Coordinates staggered execution intervals 
to optimize resource utilization and network stability.
"""

import time
import sys
import os

# Add the project root to path so it can find 'scripts' as a module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from scripts.fetch import WeatherFetcher, SystemFetcher, UpdateFetcher
except ImportError:
    from fetch import WeatherFetcher, SystemFetcher, UpdateFetcher

class VemberScheduler:
	def __init__(self):
		self.sensors = [
			{"worker": WeatherFetcher(), "interval": 1800}, # 30 mins
			{"worker": SystemFetcher(), "interval": 10},     # 5 seconds
			{"worker": UpdateFetcher(), "interval": 86400},  # 24 hours
			{"worker": UpdateFetcher(), "interval": 3600}   # 1 hour
		]
		self.last_run = {i: 0 for i in range(len(self.sensors))}

	def start(self):
		print("🌀 Vember-OS Scheduler: ONLINE")
		try:
			while True:
				now = time.time()
				for i, sensor in enumerate(self.sensors):
					if now - self.last_run[i] > sensor["interval"]:
						sensor["worker"].update()
						self.last_run[i] = now
				time.sleep(1) # CPU-friendly sleep
		except KeyboardInterrupt:
			print("🛑 Scheduler: Offline")

if __name__ == "__main__":
	VemberScheduler().start()