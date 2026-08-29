"""
🔱 VEMBER-OS: CORE
Metadata: Enter summary of CORE functionality here.
"""
"""
🔱 VEMBER OS
"""
"""
🔱 VEMBER-OS: CORE KERNEL
Sovereign components for Async Discovery and Parallel Execution.
"""

import ast
import os
import queue
import signal
import subprocess
import threading
from pathlib import Path
from typing import List, Dict


# --- SOVEREIGN COMPONENTS ---


class NodeScanner:
	"""High-speed AST-based metadata ingestion."""

	def scan(self, directory: str = "nodes") -> List[Dict]:
		path = Path(directory)
		if not path.is_dir():
			return []
		items = []
		for file_path in sorted(path.glob("*.py")):
			metadata = self._process_file(file_path)
			if metadata:
				items.append(metadata)
		return items

	def _process_file(self, file_path: Path) -> Dict:
		"""Reads and parses file metadata without execution."""
		try:
			content = file_path.read_text(encoding="utf-8")
			tree = ast.parse(content)
			return {
				"id": file_path.stem,
				"name": file_path.stem.replace("_", " ").title(),
				"description": ast.get_docstring(tree) or "No data.",
				"path": str(file_path),
				"controls": {"ESC": "BACK"},
			}
		except Exception:
			return {}

	async def scan_async(self, directory: str = "nodes") -> List[Dict]:
		return self.scan(directory)


class NodeRunner:
	"""Simple process runner used by the dashboard lifecycle."""

	def __init__(self):
		self.output_queue = queue.Queue()
		self.is_running = False
		self.process = None

	def execute(self, node_path):
		if self.is_running:
			return

		self.is_running = True

		def run():
			try:
				self.process = subprocess.Popen(
					["python3", "-u", node_path],
					stdout=subprocess.PIPE,
					stderr=subprocess.STDOUT,
					text=True,
					bufsize=1,
					preexec_fn=os.setsid,
				)
				if self.process.stdout:
					for line in iter(self.process.stdout.readline, ""):
						self.output_queue.put(line)
				self.process.wait()
			except Exception as e:
				self.output_queue.put(f"[bold red]Execution Error:[/] {str(e)}\n")
			finally:
				self.is_running = False
				self.process = None

		thread = threading.Thread(target=run, daemon=True)
		thread.start()

	def stop(self):
		if self.process:
			try:
				os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
			except Exception:
				self.process.terminate()
			self.is_running = False
			self.process = None

	def get_latest_output(self):
		out = []
		while not self.output_queue.empty():
			try:
				out.append(self.output_queue.get_nowait())
			except queue.Empty:
				break
		return "".join(out)

	def shutdown(self):
		self.stop()
