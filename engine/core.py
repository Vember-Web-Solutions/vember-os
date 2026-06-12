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
import asyncio
import fcntl
import os
import re
import subprocess
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from typing import List, Dict, Optional


# --- GLOBAL WORKER (Required for Multiprocessing Pickling) ---
def _execute_node_worker(path: str) -> str:
	"""Isolated worker function for ProcessPoolExecutor."""
	try:
		result = subprocess.run(
			[sys.executable, path], capture_output=True, text=True, timeout=30
		)
		return result.stdout if result.returncode == 0 else result.stderr
	except Exception as e:
		return f"Error: {str(e)}"


def _parse_node_metadata(content: str, stem: str, file_path: Path) -> Dict:
	"""Extract display metadata from node source without executing it."""
	name = stem.replace("_", " ").title()
	description = "No data."

	desc_match = re.search(r"Description:\s*(.+)", content)
	if desc_match:
		description = desc_match.group(1).strip()

	titles = re.findall(r"VEMBER-OS:\s*([^\n]+)", content)
	if titles:
		readable = [title for title in titles if " " in title or "-" in title]
		name = (readable[-1] if readable else titles[-1]).strip()
		name = name.replace("-", " ").replace("_", " ").title()

	return {
		"id": stem,
		"name": name,
		"description": description,
		"path": str(file_path),
		"controls": {"ESC": "DETACH"},
	}


# --- SOVEREIGN COMPONENTS ---


class NodeScanner:
	"""High-speed AST-based metadata ingestion."""

	async def scan(self, directory: str = "nodes") -> List[Dict]:
		path = Path(directory)
		if not path.is_dir():
			return []
		tasks = [self._process_file(f) for f in sorted(path.glob("*.py"))]
		return [res for res in await asyncio.gather(*tasks) if res]

	async def _process_file(self, file_path: Path) -> Dict:
		"""Reads and parses file metadata without execution."""
		content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
		ast.parse(content)
		return _parse_node_metadata(content, file_path.stem, file_path)


class NodeRunner:
	"""Subprocess execution engine with non-blocking telemetry streaming."""

	def __init__(self, max_workers: int = 4):
		self.max_workers = max_workers
		self.executor = ProcessPoolExecutor(max_workers=max_workers)
		self.process: Optional[subprocess.Popen] = None
		self._output_buffer = ""
		self._is_running = False

	@property
	def is_running(self) -> bool:
		if self.process is None:
			return False
		if self.process.poll() is not None:
			self._is_running = False
		return self._is_running

	def execute(self, path: str):
		"""Launch a node script and stream stdout into the telemetry buffer."""
		self.stop()
		self._output_buffer = ""

		try:
			self.process = subprocess.Popen(
				[sys.executable, path],
				stdout=subprocess.PIPE,
				stderr=subprocess.STDOUT,
				text=True,
				bufsize=1,
			)
		except OSError as e:
			self._output_buffer = f"Error: {e}"
			return

		if os.name != "nt" and self.process.stdout:
			try:
				fd = self.process.stdout.fileno()
				flags = fcntl.fcntl(fd, fcntl.F_GETFL)
				fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
			except OSError:
				pass

		self._is_running = True

	def get_latest_output(self) -> str:
		"""Drain available subprocess output and return the full buffer."""
		if self.process and self.process.stdout:
			try:
				while True:
					chunk = self.process.stdout.read(4096)
					if not chunk:
						break
					self._output_buffer += chunk
			except BlockingIOError:
				pass

			if self.process.poll() is not None:
				self._is_running = False

		return self._output_buffer

	def stop(self):
		"""Terminate the active node process."""
		if self.process is None:
			return

		if self.process.poll() is None:
			self.process.terminate()
			try:
				self.process.wait(timeout=2)
			except subprocess.TimeoutExpired:
				self.process.kill()
				self.process.wait()

		self.process = None
		self._is_running = False

	async def run_batch(self, paths: List[str]):
		"""Dispatches paths to the process pool asynchronously."""
		loop = asyncio.get_running_loop()
		tasks = [
			loop.run_in_executor(self.executor, _execute_node_worker, p) for p in paths
		]
		return await asyncio.gather(*tasks)

	def shutdown(self):
		self.stop()
		self.executor.shutdown(wait=True)
