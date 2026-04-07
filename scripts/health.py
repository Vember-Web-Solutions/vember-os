"""
🔱 VEMBER-OS: HEALTH SERVICE
Uptime validation utility. Provides a standardized heartbeat for 
verifying connectivity and service integrity.
"""

import subprocess
import time

class HealthCheck:
	def __init__(self, target="https://api.open-meteo.com"):
		self.target = target

	def check_network(self):
		"""
		Performs a system-level head request via Curl.
		Returns (bool: is_healthy, int: status_code, str: error_msg)
		"""
		try:
			# -I (Head only), -s (Silent), -o (Write output to /dev/null), -w (Write format)
			# This is the fastest way to check a 200 status without downloading anything.
			cmd = [
				'curl', '-I', '-s', '-o', '/dev/null', 
				'-w', '%{http_code}', 
				self.target
			]
			
			result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
			status_code = int(result.stdout.strip())

			if status_code == 200:
				return True, 200, "OK"
			elif status_code == 000:
				return False, 0, "SSL/Network Failure (Code 35/MTU)"
			else:
				return False, status_code, f"Unexpected Status: {status_code}"

		except subprocess.TimeoutExpired:
			return False, 408, "Gateway Timeout"
		except Exception as e:
			return False, 500, str(e)

	def wait_for_connectivity(self, retries=5, delay=2):
		"""Blocking check used during OS startup sequences."""
		print(f"📡 [SYSTEM.BOOT] Probing {self.target}...")
		for i in range(retries):
			healthy, code, msg = self.check_network()
			if healthy:
				print(f"✅ [SYSTEM.BOOT] Link Established (HTTP {code})")
				return True
			print(f"⚠️  [SYSTEM.BOOT] Attempt {i+1}/{retries} failed: {msg}")
			time.sleep(delay)
		return False

if __name__ == "__main__":
	# Internal Test
	# Test against a different weather provider
	tester = HealthCheck(target="https://wttr.in/New+York?format=j1")
	is_up, code, msg = tester.check_network()
	
	if is_up:
		print(f"💚 OS HEALTH: 200 OK - Link to {tester.target} is stable.")
	else:
		print(f"💔 OS HEALTH: CRITICAL - {msg} (Code {code})")