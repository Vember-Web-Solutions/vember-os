import curses
import time
from windfall import Windfall
from core import NodeScanner
from runner import NodeRunner
from branding import THEMES, LOGO_ANSI

class VemberDashboard:
	def __init__(self):
		self.scanner = NodeScanner()
		self.windfall = Windfall(theme_key="VEMBER_DARK")
		self.runner = NodeRunner()
		
		self.selected_index = 0
		self.running = True
		self.nodes = []
		self.output_buffer = ""

	def show_splash(self, stdscr):
		"""Initial Boot Sequence"""
		stdscr.erase()
		h, w = stdscr.getmaxyx()
		logo_lines = LOGO_ANSI.splitlines()
		start_y = (h // 2) - (len(logo_lines) // 2)
		for i, line in enumerate(logo_lines):
			if start_y + i < h:
				stdscr.addstr(start_y + i, (w // 2) - (len(line) // 2), line)
		stdscr.refresh()
		time.sleep(1.5)

	def update_logic(self, key):
		"""Handles input and state changes."""
		self.nodes = self.scanner.scan()
		num_nodes = len(self.nodes)

		# 1. Capture Live Output
		new_output = self.runner.get_latest_output()
		if new_output:
			# If the node sends a refresh signal, clear the buffer first
			if "--- REFRESH ---" in new_output:
				# Only keep the text AFTER the last refresh signal
				self.output_buffer = new_output.split("--- REFRESH ---")[-2]
			else:
				self.output_buffer += new_output

		# 2. Key Handling
		if key in (ord('q'), 8, 27): # 27 is ESC
			if self.runner.is_running:
				self.runner.stop()
				self.output_buffer = ""
			else:
				self.running = False
		elif key == curses.KEY_F2:
			self.windfall.toggle_sidebar()
		elif key == curses.KEY_F3:
			self.windfall.toggle_inspector()
		elif key == curses.KEY_UP and self.selected_index > 0:
			self.selected_index -= 1
			self.output_buffer = "" # Clear buffer when switching nodes
		elif key == curses.KEY_DOWN and self.selected_index < num_nodes - 1:
			self.selected_index += 1
			self.output_buffer = "" # Clear buffer when switching nodes
		
		# 🔱 TRIGGER EXECUTION
		elif key in (curses.KEY_ENTER, 10, 13):
			if self.nodes and not self.runner.is_running:
				self.output_buffer = "🚀 Launching Node...\n"
				curr_node = self.nodes[self.selected_index]
				self.runner.execute(curr_node['path'])

	def _get_sidebar_content(self):
		content = ""
		for i, node in enumerate(self.nodes):
			prefix = "▶ " if i == self.selected_index else "  "
			if i == self.selected_index:
				# 🔱 Use the clean 'name' key we just created in core.py
				content += f"[bold cyan]{prefix}{node['name']}[/]\n"
			else:
				content += f"{prefix}{node['name']}\n"
		return content

	def _get_inspector_content(self):
		if not self.nodes:
			return "[dim]Scanning Registry...[/]"
		
		curr = self.nodes[self.selected_index]
		
		# 🔱 Clean Sections: Header (Name) + Body (Description)
		header = (
			f"[bold cyan]🔱 {curr['name']}[/]\n"
			f"[dim]{curr['description']}[/]\n"
			f"[dim]{'—' * 45}[/]\n"
		)

		if self.runner.is_running:
			return f"{header}[bold green]● LIVE TELEMETRY[/]\n\n{self.output_buffer}"
		
		return f"{header}\n[dim]Press ENTER to initialize...[/]"

	def _get_footer_content(self):
		return "[dim]ARROWS Navigate | ENTER Run | F2 Sidebar | F3 Inspector | Q Quit[/]"

	def run(self, stdscr):
		self.show_splash(stdscr)
		curses.curs_set(0)
		stdscr.nodelay(True)
		stdscr.keypad(True)

		while self.running:
			key = stdscr.getch()
			self.update_logic(key)
			h, w = stdscr.getmaxyx()

			frame = self.windfall.compose(w, h, {
				"sidebar": self._get_sidebar_content,
				"inspector": self._get_inspector_content,
				"footer": self._get_footer_content
			})
			
			stdscr.erase()
			try:
				for y, line in enumerate(frame.splitlines()):
					if y < h:
						stdscr.addstr(y, 0, line.rstrip()[:w - 1])
			except curses.error:
				pass

			stdscr.refresh()
			time.sleep(0.05)

if __name__ == "__main__":
	app = VemberDashboard()
	curses.wrapper(app.run)