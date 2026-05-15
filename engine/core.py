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
import subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from typing import List, Dict, Any


# --- GLOBAL WORKER (Required for Multiprocessing Pickling) ---
def _execute_node_worker(path: str) -> str:
	"""Isolated worker function for ProcessPoolExecutor."""
	try:
		result = subprocess.run(
			["python", path], capture_output=True, text=True, timeout=30
		)
		return result.stdout if result.returncode == 0 else result.stderr
	except Exception as e:
		return f"Error: {str(e)}"


# --- SOVEREIGN COMPONENTS ---


class NodeScanner:
	"""High-speed AST-based metadata ingestion."""

	async def scan(self, directory: str = "nodes") -> List[Dict]:
		path = Path(directory)
		if not path.is_dir():
			return []
		tasks = [self._process_file(f) for f in path.glob("*.py")]
		return [res for res in await asyncio.gather(*tasks) if res]

	async def _process_file(self, file_path: Path) -> Dict:
		"""Reads and parses file metadata without execution."""
		content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
		tree = ast.parse(content)
		return {
			"id": file_path.stem,
			"description": ast.get_docstring(tree) or "No data.",
			"path": str(file_path),
		}


class NodeRunner:
	"""Isolated parallel execution engine."""

	def __init__(self, max_workers: int = 4):
		self.executor = ProcessPoolExecutor(max_workers=max_workers)

	async def run_batch(self, paths: List[str]):
		"""Dispatches paths to the process pool asynchronously."""
		loop = asyncio.get_running_loop()
		tasks = [
			loop.run_in_executor(self.executor, _execute_node_worker, p) for p in paths
		]
		return await asyncio.gather(*tasks)

	def shutdown(self):
		self.executor.shutdown(wait=True)
