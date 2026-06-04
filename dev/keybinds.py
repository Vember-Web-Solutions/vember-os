"""
================================================================================
🔱 VEMBER-OS: KEYBINDS CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: DEVELOPER_CONSOLE_KEYBINDS
Context Path:  /dev/keybinds.py

Asynchronous Background Worker Thread & Harvester Queue Input Matrix.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

import queue
from pynput import keyboard
from typing import Optional


class ConsoleInputMatrix:
	_input_queue: queue.Queue = queue.Queue()
	_listener: Optional[keyboard.Listener] = None
	_initialized: bool = False

	@classmethod
	def initialize_matrix(cls):
		"""Spins up the OS-level key listener background daemon."""

		def on_press(key):
			try:
				if key == keyboard.Key.up:
					cls._input_queue.put("UP")
				elif key == keyboard.Key.down:
					cls._input_queue.put("DN")
				elif key == keyboard.Key.enter:
					cls._input_queue.put("IGNITE_MODULE_CONTRACT")
			except Exception:
				pass

		cls._listener = keyboard.Listener(on_press=on_press)
		cls._listener.start()
		cls._initialized = True

	@classmethod
	def capture_action(cls) -> str:
		"""Extracts the latest keypress without blocking the UI thread."""
		if not cls._initialized:
			cls.initialize_matrix()

		try:
			return cls._input_queue.get_nowait()
		except queue.Empty:
			return ""

	@classmethod
	def shutdown_matrix(cls):
		"""Gracefully kills the hardware listener."""
		if cls._listener:
			cls._listener.stop()
			cls._initialized = False
