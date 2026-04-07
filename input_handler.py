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
			tty.setcbreak(self.fd)
			while self.running:
				# Polling with select prevents the thread from 
				# getting stuck on sys.stdin.read
				r, _, _ = select.select([sys.stdin], [], [], 0.1)
				if r:
					char = sys.stdin.read(1)
					if char == '\x1b': # Handle Arrows
						r2, _, _ = select.select([sys.stdin], [], [], 0.05)
						if r2:
							char += sys.stdin.read(2)
					self.input_queue.put(char)
		finally:
			# Emergency restore if thread crashes
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