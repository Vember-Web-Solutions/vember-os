import subprocess
import threading
import queue

class NodeRunner:
	def __init__(self):
		self.output_queue = queue.Queue()
		self.is_running = False
		self.process = None

	def execute(self, node_path):
		"""Spawns the node process in a separate thread."""
		if self.is_running:
			return

		def run():
			self.is_running = True
			try:
				# Identify runner based on extension
				cmd = ["python3", "-u", node_path] if node_path.endswith(".py") else ["bash", node_path]
				
				self.process = subprocess.Popen(
					cmd,
					stdout=subprocess.PIPE,
					stderr=subprocess.STDOUT,
					text=True,
					bufsize=1
				)

				for line in self.process.stdout:
					self.output_queue.put(line)
				
				self.process.wait()
			except Exception as e:
				self.output_queue.put(f"Error: {str(e)}")
			finally:
				self.is_running = False

		thread = threading.Thread(target=run, daemon=True)
		thread.start()

	def stop(self):
		"""Forcefully terminate the running node process."""
		if self.process:
			self.process.terminate()
			self.is_running = False
			self.process = None

	def get_latest_output(self):
		"""Drains the queue and returns accumulated text."""
		out = ""
		while not self.output_queue.empty():
			out += self.output_queue.get()
		return out