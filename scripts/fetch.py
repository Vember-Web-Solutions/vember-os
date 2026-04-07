"""
Vember-OS Fetcher Suite
----------------------
Consolidated telemetry acquisition engine. Handles external APIs (Weather), 
local system vitals (Load/Thermal), and Git version tracking. 
Supports both manual targeted polling and automatic scheduler updates.
"""

import subprocess
import json
import sys
import os
from datetime import datetime

# 🔱 Force the scripts directory into the path so siblings can see each other
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
	from data_hub import DataHub
except ImportError:
	from scripts.data_hub import DataHub

class BaseFetcher:
	def __init__(self, sensor_name):
		self.sensor_name = sensor_name
		self.hub = DataHub()
		self.user_agent = "Vember-OS/1.0"

	def _get_json(self, url):
		try:
			# 🔱 ADDED -L: wttr.in often redirects. Without -L, curl returns nothing.
			result = subprocess.run(
				['curl', '-sL', '-H', f'User-Agent: {self.user_agent}', url],
				capture_output=True, text=True, timeout=15, check=True
			)
			if not result.stdout.strip():
				print(f"❌ {self.sensor_name}: Curl returned empty string")
				return None
			return json.loads(result.stdout)
		except Exception as e:
			print(f"❌ {self.sensor_name} Network Error: {e}")
			return None

	def broadcast(self, data):
		print(f"📡 {self.sensor_name}: Writing to Hub...")
		return self.hub.write(self.sensor_name, data)

class WeatherFetcher(BaseFetcher):
	def __init__(self, location="New York"):
		super().__init__("weather")
		# 🔱 FIX: Cleaned up the URL formatting
		safe_loc = location.replace(" ", "+")
		self.url = f"https://v2.wttr.in/{safe_loc}?format=j1"

	def update(self):
		print(f"🔍 WEATHER: Accessing {self.url}")
		raw = self._get_json(self.url)
		
		if not raw:
			print("❌ WEATHER: No JSON returned from server.")
			return False
			
		try:
			# 🔱 FIX: Robust extraction
			current = raw['current_condition'][0]
			telemetry = {
				"temperature": current.get('temp_F'),
				"description": current.get('weatherDesc', [{}])[0].get('value'),
				"humidity": current.get('humidity'),
				"wind_speed": current.get('windspeedMiles'),
				"provider": "WTTR-v2"
			}
			return self.broadcast(telemetry)
		except KeyError as e:
			print(f"❌ WEATHER: Data format mismatch: {e}")
			return False

class SystemFetcher(BaseFetcher):
	def __init__(self):
		super().__init__("system")

	def update(self):
		try:
			with open("/proc/loadavg", "r") as f:
				load = f.read().split()[:3]
			return self.broadcast({"load": load, "status": "ONLINE"})
		except Exception as e:
			print(f"❌ SYSTEM: {e}")
			return False

class UpdateFetcher(BaseFetcher):
	"""
	Vember-OS Update Sentry.
	Compares local git HEAD with remote tracking branch.
	"""
	def __init__(self):
		super().__init__("updates")

	def update(self):
		print("📡 UPDATES: Checking GitHub for OS patches...")
		try:
			# Fetch latest metadata from origin
			subprocess.run(['git', 'fetch'], check=True, capture_output=True)
			
			# Compare hashes
			local_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
			remote_hash = subprocess.check_output(['git', 'rev-parse', '@{u}']).decode().strip()
			
			has_update = local_hash != remote_hash
			
			return self.broadcast({
				"update_available": has_update,
				"local_hash": local_hash[:7],
				"remote_hash": remote_hash[:7],
				"status": "PATCH_READY" if has_update else "UP_TO_DATE"
			})
		except Exception as e:
			return self.broadcast({"update_available": False, "status": "ERROR", "msg": str(e)})

def run_all_fetchers(location="New York"):
	"""
	Automatic Mode: Iterates through all registered sensors 
	and updates the DataHub. Used by the Scheduler.
	"""
	fetchers = [
		WeatherFetcher(location),
		SystemFetcher(),
		UpdateFetcher()
	]
	
	results = {}
	for f in fetchers:
		success = f.update()
		results[f.sensor_name] = success
		status = "✅" if success else "❌"
		print(f"{status} {f.sensor_name.upper()}: Update complete.")
	
	return results

if __name__ == "__main__":
	import argparse
	
	# Setup CLI arguments for Manual Mode
	parser = argparse.ArgumentParser(description="Vember-OS Fetcher Interface")
	parser.add_argument("--sensor", help="Run a specific sensor (weather, system, updates)")
	parser.add_argument("--location", default="New York", help="Location for weather sensor")
	args = parser.parse_args()

	print("🚀 Vember-OS: Fetcher Module Initiated")

	# List of all available fetchers
	fetchers = [
		WeatherFetcher(args.location),
		SystemFetcher(),
		UpdateFetcher()
	]

	if args.sensor:
		# --- MANUAL MODE ---
		# Find the specific sensor the user requested
		target = next((f for f in fetchers if f.sensor_name == args.sensor), None)
		if target:
			print(f"🛠️  Manual Trigger: {args.sensor.upper()}")
			target.update()
		else:
			print(f"❌ Unknown sensor: {args.sensor}. Available: weather, system, updates")
	else:
		# --- AUTOMATIC MODE ---
		print("🔄 Running Full Telemetry Sync...")
		for f in fetchers:
			f.update()
			print(f"✅ {f.sensor_name.upper()}: Update complete.")