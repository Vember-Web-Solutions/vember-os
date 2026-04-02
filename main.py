import curses
import time
from io import StringIO

# Resolved Rich Imports
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.table import Table

from core import NodeScanner

class VemberDashboard:
	def __init__(self):
		self.scanner = NodeScanner()
		
		self.console = Console(
			file=StringIO(), 
			force_terminal=True, 
			width=100, 
			color_system=None, # Strips ANSI colors
			safe_box=True      # Uses simpler box characters for better compatibility
		)

		self.selected_index = 0
		self.running = True
		self.nodes = []

	def update_logic(self, key):
		"""Handles input and state changes."""
		self.nodes = self.scanner.scan()
		num_nodes = len(self.nodes)

		if key == ord('q'):
			self.running = False
		elif key == ord('r'):
			self.selected_index = 0  # Reset on refresh
		elif key == curses.KEY_UP and self.selected_index > 0:
			self.selected_index -= 1
		elif key == curses.KEY_DOWN and self.selected_index < num_nodes - 1:
			self.selected_index += 1
		elif key in (curses.KEY_ENTER, 10, 13):
			# Placeholder for execution logic
			pass

	def build_render_tree(self):
		"""Constructs the Rich layout object."""
		layout = Layout()
		layout.split_column(
			Layout(name="header", size=3),
			Layout(name="body"),
			Layout(name="footer", size=3)
		)
		layout["body"].split_row(
			Layout(name="sidebar", ratio=1),
			Layout(name="inspector", ratio=2)
		)

		# Header
		layout["header"].update(Panel(
			"[bold cyan]🔱 VEMBER-OS v0.1.0[/] | [green]ENVIRONMENT: DOCKER/PY3.13[/]", 
			border_style="blue"
		))

		# Sidebar
		node_table = Table(show_header=False, box=None, expand=True)
		for i, node in enumerate(self.nodes):
			style = "bold reverse cyan" if i == self.selected_index else "white"
			prefix = "▶ " if i == self.selected_index else "  "
			node_table.add_row(f"[{style}]{prefix}{node['display_name']}[/]")
		
		layout["sidebar"].update(Panel(node_table, title="[magenta]NODES[/]", border_style="blue"))

		# Inspector
		if self.nodes:
			curr = self.nodes[self.selected_index]
			detail = f"[bold yellow]ID:[/] {curr['id']}\n[bold yellow]SRC:[/] {curr['path']}\n\n[white]{curr['description']}[/]"
			layout["inspector"].update(Panel(detail, title=f"[white]{curr['display_name']}[/]", border_style="cyan"))
		else:
			layout["inspector"].update(Panel("[dim]Scanning /ops...[/]"))

		# Footer
		layout["footer"].update(Panel("[dim]ARROWS Navigate | ENTER Run | R Rescan | Q Shutdown[/]", border_style="blue"))
		
		return layout

	def run(self, stdscr):
		"""The Main Ncurses Loop."""
		curses.curs_set(0)
		stdscr.nodelay(True)
		stdscr.keypad(True)

		# Explicitly check for color support
		if curses.has_colors():
			curses.start_color()
			curses.use_default_colors()

		while self.running:
			
			# 1. Update State
			key = stdscr.getch()
			self.update_logic(key)

			# 2. Render to String
			self.console.file = StringIO() # Clear the previous frame buffer
			render_tree = self.build_render_tree()
			self.console.print(render_tree)
			full_output = self.console.file.getvalue()
			
			# 3. Precise Ncurses Painting
			stdscr.erase() # Wipe the slate
			try:
				# Loop through the rendered lines and place them manually
				for y, line in enumerate(full_output.splitlines()):
					if y < curses.LINES - 1: # Prevent crashing on small windows
						stdscr.addstr(y, 0, line[:curses.COLS - 1])
			except curses.error:
				pass

			stdscr.refresh()
			time.sleep(0.05)

if __name__ == "__main__":
	app = VemberDashboard()
	curses.wrapper(app.run)