"""
🔱 VEMBER-OS: DATAHUB SERVICE
The central nervous system for state persistence. Provides a standardized 
API for telemetry ingestion and node synchronization.

Core Responsibilities:
* Atomic JSON operations with metadata injection.
* Data decoupling for multi-node visualization.
"""

import json
import os
import time
from datetime import datetime

class DataHub:
	def __init__(self, data_dir="data"):
		self.data_dir = data_dir
		if not os.path.exists(self.data_dir):
			os.makedirs(self.data_dir)

	def get_path(self, filename):
		# Ensure filename ends in .json
		if not filename.endswith(".json"):
			filename += ".json"
		return os.path.join(self.data_dir, filename)

	def write(self, filename, data):
		"""Standardized JSON writer with 'last_updated' injection."""
		path = self.get_path(filename)
		try:
			# We inject a system timestamp so the reader knows exactly 
			# when the data was written, regardless of file metadata.
			payload = {
				"metadata": {
					"last_updated": datetime.now().isoformat(),
					"source": "Vember-OS Core"
				},
				"payload": data
			}
			with open(path, 'w') as f:
				json.dump(payload, f, indent=4)
			return True
		except Exception as e:
			print(f"[DataHub Error] Write failed: {e}")
			return False

	def read(self, filename):
		"""Reads JSON and returns (payload, sync_time_string)."""
		path = self.get_path(filename)
		if not os.path.exists(path):
			return None, "FILE_MISSING"

		try:
			with open(path, 'r') as f:
				blob = json.load(f)
			
			# Extract the actual data and the timestamp
			data = blob.get("payload", {})
			raw_time = blob.get("metadata", {}).get("last_updated", "UNKNOWN")
			
			# Format time for the UI (HH:MM:SS)
			if raw_time != "UNKNOWN":
				dt = datetime.fromisoformat(raw_time)
				sync_str = dt.strftime("%H:%M:%S")
			else:
				sync_str = "ERR"

			return data, sync_str
		except Exception as e:
			print(f"[DataHub Error] Read failed: {e}")
			return None, "CORRUPT"

	def exists(self, filename):
		return os.path.exists(self.get_path(filename))