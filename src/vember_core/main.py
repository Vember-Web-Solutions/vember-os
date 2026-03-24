"""
🔱 VEMBER-OS | CORE ORCHESTRATOR
File: main.py
Author: Vember-Web-Solutions
Description: The entry point for Vember-OS. Manages the lifecycle of 
			Resource Groups (Docker) and coordinates with the 
			Windfall Engine for display output.
"""

from vember_core.engine.windfall import Windfall
from vember_core.nodes.manager import DockerManager

class VemberCore:
	"""
	The central intelligence of the Vember Ecosystem.
	"""

	def __init__(self):
		# Initializing the 'Wayland' style display server
		self.engine = Windfall(mode="tui")
		self.is_running = True
		# Mock state for MVP testing
		self.state = {"title": "VEMBER CORE", "status": "ACTIVE"}
		self.node_manager = DockerManager()

	def boot(self):
		"""Initiates the Vember-OS boot sequence."""
		# ARCHITECTURE NOTE: We print a clear 'Booting' signal 
		# to ensure the user knows the process has started.
		print("🔱 Vember-OS is initializing...")
		
		while self.is_running:
			self._update_system_state()
			self._render_frame()
			
			# For the MVP 'Run' test, we stop after one frame 
			# so the terminal doesn't get flooded.
			self.is_running = False 

	def _update_system_state(self):
		"""Fetches real-time node data from Docker."""
		nodes = self.node_manager.get_node_status()
		self.state["nodes"] = nodes
		self.state["status"] = "NODES SYNCED"

	def _render_frame(self):
		"""Passes the current state to Windfall and PRINTS to terminal."""
		# 1. Ask Windfall to compose the header
		output = self.engine.draw_component("header", self.state)
		
		# 2. Physically send it to the terminal
		print(output)

def run():
	"""Package entry point for the 'vember' command."""
	os_instance = VemberCore()
	os_instance.boot()

if __name__ == "__main__":
	run()