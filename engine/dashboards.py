"""
🔱 VEMBER-OS CORE DASHBOARDS (v2.2.0)
The engine room for telemetry, lifecycle, and spatial mesh navigation.
"""
from rich.console import Group
from engine.windfall import Windfall
from engine.core import NodeScanner
from engine.runner import NodeRunner
from engine.widgets import OSHeader, OSToast, OSNodeInspector, OSActionMenu, OSMeshMap, OSFooter

class BaseDashboard:
	"""🔱 PLUMBING: Handles the background logic so the UI can stay clean."""
	def __init__(self):
		self.windfall = Windfall()
		self.runner = NodeRunner()
		
		# Telemetry State
		self.cpu_load = 0.0
		self.ram_load = 0.0
		self.temp_load = 0.0
		self.output_buffer = ""
		
		# Notification State
		self.active_toast = None
		self.toast_timer = 0
		
		# Application State
		self.running = True

	def trigger_toast(self, message, duration=40):
		"""🔱 ALERT: Pops a notification into the header stack."""
		self.active_toast = message
		self.toast_timer = duration

	def update_lifecycle(self):
		"""🔱 TICK: Must be called every frame to sync data and timers."""
		# 1. Decay Toasts
		if self.toast_timer > 0:
			self.toast_timer -= 1
		else:
			self.active_toast = None

		# 2. Sync Telemetry from NodeRunner 
		# FIX: Synchronized with runner.py method name
		self.output_buffer = self.runner.get_latest_output()
		self.sync_telemetry()

	def sync_telemetry(self):
		if "||DATA|" in self.output_buffer:
			try:
				data_segment = self.output_buffer.split("||DATA|")[1].split("|||")[0]
				parts = data_segment.split("|")
				self.cpu_load = float(parts[0])
				if len(parts) > 1: self.temp_load = float(parts[1])
			except (ValueError, IndexError):
				pass

	def handle_input(self, key):
		"""Override this in child classes for specific navigation."""
		pass

	def get_layout_map(self):
		"""Override this in child classes to define the Scene."""
		return {}

class MainDashboard(BaseDashboard):
	"""🔱 PRIMARY INTERFACE: Spatial Mesh Controller."""
	def __init__(self):
		super().__init__()
		self.scanner = NodeScanner()
		self.nodes = self.scanner.scan()
		self.selected_index = 0
		self.viewing_node = False

	def handle_input(self, key):
		if not self.nodes: return
		if key in ['a', '\x1b[D']: # Left
			self.selected_index = (self.selected_index - 1) % len(self.nodes)
		elif key in ['d', '\x1b[C']: # Right
			self.selected_index = (self.selected_index + 1) % len(self.nodes)
		elif key in ['\n', '\r']: # Enter
			if not self.viewing_node:
				self.viewing_node = True
				self.runner.execute(self.nodes[self.selected_index]['path'])
		elif key == '\x1b' or key.lower() == 'x': # Back
			self.viewing_node = False
			self.runner.stop()
		elif key.lower() == 'q':
			self.running = False
			
	def get_layout_map(self):
		self.update_lifecycle()
		current_node = self.nodes[self.selected_index] if self.nodes else None
		
		# Check if the runner is currently busy
		# We assume it's running the 'selected' node if viewing_node is true, 
		# but we store that index so it persists after detach.
		running_idx = self.selected_index if self.runner.is_running else None

		# 🔱 THE BIG SWAP: If we are 'in' a node, show the console output
		if self.viewing_node:
			viewport = lambda: OSNodeInspector(
				node_name=current_node['name'], 
				output=self.output_buffer
			)
			footer_actions = current_node.get('controls', {"ESC": "DETACH"})
		else:
			viewport = lambda: OSMeshMap(active_index=self.selected_index, running_index=running_idx)
			footer_actions = {"A/D": "NAV", "ENTER": "LAUNCH", "Q": "OFF"}

		return {
			"header": lambda: OSHeader(cpu=self.cpu_load, ram=self.ram_load),
			"viewport": viewport,
			"aside": lambda: OSActionMenu(node_data=current_node),
			"footer": lambda: OSFooter(actions=footer_actions)
		}