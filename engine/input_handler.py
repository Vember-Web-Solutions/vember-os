"""
🔱 VEMBER-OS: INPUT_HANDLER
Metadata: Enter summary of INPUT_HANDLER functionality here.
"""
"""
🔱 VEMBER OS
"""
"""
🔱 VEMBER-OS: INPUT HANDLER
Low-level terminal abstraction. Utilizes termios and select for 
non-blocking, raw-mode keyboard event capturing.
"""

import sys
import tty
import termios
import select
import queue
import threading

class KeyListener:
	def __init__(self):
		self.input_queue = queue.Queue()
		self.running = True
		self.fd = None
		self.old_settings = None
		self._tty_available = False

		try:
			self.fd = sys.stdin.fileno()
			self.old_settings = termios.tcgetattr(self.fd)
			self._tty_available = sys.stdin.isatty()
		except (AttributeError, OSError, termios.error):
			self.fd = None
			self.old_settings = None
			self._tty_available = False

		self.thread = threading.Thread(target=self._listener, daemon=True)
		self.thread.start()

	def _listener(self):
		try:
			if self._tty_available and self.fd is not None:
				tty.setcbreak(self.fd)

			while self.running:
				if not self._tty_available:
					break
				r, _, _ = select.select([sys.stdin], [], [], 0.1)
				if r:
					char = sys.stdin.read(1)
					self.input_queue.put(char)
		except Exception as e:
			print(f"🔱 INPUT_KERNEL_ERROR: {e}")
		finally:
			if self._tty_available and self.fd is not None and self.old_settings is not None:
				termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

	def stop(self):
		"""Restores terminal to standard mode when a TTY is active."""
		self.running = False
		if self._tty_available and self.fd is not None and self.old_settings is not None:
			termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

	def get_key(self):
		try:
			return self.input_queue.get_nowait()
		except queue.Empty:
			return None