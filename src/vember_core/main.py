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
			"""Fetches nodes from Docker AND internal Vember apps."""
			# 1. Real Docker Nodes
			nodes = self.node_manager.get_node_status()
			
			# 2. Mock Vember Vector (The Finance Node)
			nodes.append({"name": "Vember-Vector", "state": "STANDBY"})
			
			self.state["nodes"] = nodes
			self.state["status"] = "ECOSYSTEM SYNCED"

	def _render_frame(self):
		"""Passes the full ecosystem state to Windfall."""
		# 1. Draw the OS Header
		header = self.engine.draw_component("header", self.state)
		print(header)

		# 2. Draw the Node Grid (Docker + Finance + Future Apps)
		if "nodes" in self.state:
			grid = self.engine.draw_component("node_grid", self.state)
			print(grid)

def run():
	"""Package entry point for the 'vember' command."""
	os_instance = VemberCore()
	os_instance.boot()

if __name__ == "__main__":
	run()