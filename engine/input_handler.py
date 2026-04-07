"""
🔱 VEMBER-OS NATIVE INPUT KERNEL (v1.0.5 Patch)
Low-level terminal abstraction using termios and select.
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
		self.fd = sys.stdin.fileno()
		self.old_settings = termios.tcgetattr(self.fd)
		
		self.thread = threading.Thread(target=self._listener, daemon=True)
		self.thread.start()

	def _listener(self):
		try:
			# 🔱 Add a check to see if we are in an interactive terminal
			if sys.stdin.isatty():
				tty.setcbreak(self.fd)
			
			while self.running:
				# Polling with select prevents the thread from blocking
				r, _, _ = select.select([sys.stdin], [], [], 0.1)
				if r:
					char = sys.stdin.read(1)
					# ... (rest of your arrow handling logic) ...
					self.input_queue.put(char)
		except Exception as e:
			# 🔱 If it fails, don't crash the OS, just log it
			print(f"🔱 INPUT_KERNEL_ERROR: {e}")
		finally:
			if sys.stdin.isatty():
				termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

	def stop(self):
		self.running = False
		termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

	def get_key(self):
		try:
			return self.input_queue.get_nowait()
		except queue.Empty:
			return None

	def stop(self):
		"""Restores terminal to standard mode."""
		self.running = False
		termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)