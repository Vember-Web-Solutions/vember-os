"""
🔱 VEMBER-OS: WINDFALL
Metadata: Surgical Anatomy Mapping & Escape-Protocol Navigation. (Beta)
"""

import ast
import os
import re
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.columns import Columns
from rich.align import Align
from rich.text import Text
from rich.console import Group
from scripts.ui_core import VemberTheme as Theme
from scripts.vember_setup import TerminalInput


class Windfall:
	def __init__(self):
		self.selection = 0
		self.file_index = 0
		self.anatomy_index = 0  # 🔱 Cursor for the Anatomy Table
		self.window_start = 0
		self.window_size = 12
		self.mode = "NAVIGATE"  # NAVIGATE, EXPLORE
		self.focus_path = ""
		self.metadata = "No Metadata Found."
		self.nodes = []
		self.available_files = []
		self.menu_items = [
			{"label": "Select Focus", "desc": "Browse modules"},
			{"label": "Reflect DNA", "desc": "Analyze module structure"},
			{"label": "Return to Console", "desc": "Sever forge link"},
		]

	def ignite(self, engine, live):
		self._refresh_file_list()
		os.system("cls" if os.name == "nt" else "clear")
		while True:
			live.update(self._generate_layout(), refresh=True)
			key = TerminalInput.get_key()

			# 🔱 UNIVERSAL ESCAPE / BACK
			if key in ["esc", "backspace"]:
				if self.mode == "EXPLORE":
					self.mode = "NAVIGATE"
					self.anatomy_index = 0  # Reset anatomy cursor
					continue
				elif self.mode == "NAVIGATE":
					break  # Exit Windfall to Main Menu

			if key == "up":
				if self.mode == "NAVIGATE":
					self.file_index = max(0, self.file_index - 1)
					if self.file_index < self.window_start:
						self.window_start = self.file_index
				elif self.mode == "EXPLORE":
					self.anatomy_index = max(0, self.anatomy_index - 1)
				else:
					self.selection = max(0, self.selection - 1)

			elif key == "down":
				if self.mode == "NAVIGATE":
					self.file_index = min(
						len(self.available_files) - 1, self.file_index + 1
					)
					if self.file_index >= self.window_start + self.window_size:
						self.window_start = self.file_index - self.window_size + 1
				elif self.mode == "EXPLORE":
					self.anatomy_index = min(
						len(self.nodes) - 1, self.anatomy_index + 1
					)
				else:
					self.selection = min(len(self.menu_items) - 1, self.selection + 1)

			elif key == "enter":
				if self.mode == "NAVIGATE" and self.available_files:
					self.focus_path = self.available_files[self.file_index]
					self._reflect_file()
					self.mode = "EXPLORE"
				elif self.mode == "EXPLORE":
					# Potential for Node 03 (SURGERY) here
					pass

	def _reflect_file(self):
		self.nodes = []
		try:
			with open(self.focus_path, "r", encoding="utf-8") as f:
				tree = ast.parse(f.read())
			doc = ast.get_docstring(tree)
			if doc:
				meta_match = re.search(r"Metadata:\s*(.*)", doc, re.IGNORECASE)
				self.metadata = (
					meta_match.group(1) if meta_match else doc.split("\n")[0]
				)
			else:
				self.metadata = "[red]Missing Vember DNA Metadata Seal.[/]"

			for node in ast.iter_child_nodes(tree):
				if isinstance(node, ast.ClassDef):
					methods = [
						n.name for n in node.body if isinstance(n, ast.FunctionDef)
					]
					self.nodes.append(
						{"type": "CLASS", "name": node.name, "count": len(methods)}
					)
				elif isinstance(node, ast.FunctionDef):
					self.nodes.append({"type": "FUNC", "name": node.name, "count": 1})
		except Exception as e:
			self.metadata = f"[red]Error:[/] {str(e)}"

	def _generate_layout(self):
		# NODE 01 (Static menu for now)
		menu_table = Table(show_header=False, box=None, padding=(0, 1))
		for idx, item in enumerate(self.menu_items):
			cur = "►" if idx == self.selection and self.mode == "MENU" else " "
			menu_table.add_row(cur, item["label"])

		left_panel = Panel(
			menu_table,
			title=f"[{Theme.TITLE}]🔱 WINDFALL[/]",
			border_style=Theme.ACTION,
			width=32,
		)

		# NODE 02 (Dynamic Battlefield)
		if self.mode == "NAVIGATE":
			title = "SELECT FOCUS"
			content = Table(box=None, show_header=False)
			visible_files = self.available_files[
				self.window_start : self.window_start + self.window_size
			]
			for i, f in enumerate(visible_files):
				abs_idx = self.window_start + i
				cur = "►" if abs_idx == self.file_index else " "
				sty = f"bold {Theme.ACCENT}" if abs_idx == self.file_index else "dim"
				content.add_row(cur, f"[{sty}]{f}[/]")
			renderable_content = content
		else:
			title = "CODE ANATOMY"
			meta_text = Text(f"📜 {self.metadata}\n", style="italic yellow")
			table = Table(
				box=None,
				show_header=True,
				header_style=f"bold {Theme.ACCENT}",
				padding=(0, 1),
			)
			table.add_column(" ", width=2)
			table.add_column("TYPE", style="dim", width=8)
			table.add_column("OBJECT NAME", style="white")
			table.add_column("METHODS", justify="right", style="cyan")

			for idx, node in enumerate(self.nodes):
				cur = "►" if idx == self.anatomy_index else " "
				row_style = (
					f"bold {Theme.SELECTED}" if idx == self.anatomy_index else "white"
				)
				type_label = (
					"[cyan]CLASS[/]" if node["type"] == "CLASS" else "[green]FUNC[/]"
				)
				table.add_row(
					cur,
					type_label,
					f"[{row_style}]{node['name']}[/]",
					str(node["count"]),
				)

			renderable_content = Group(meta_text, table)

		right_panel = Panel(
			Align.left(renderable_content),
			title=f"[{Theme.ACCENT}]{title}[/]",
			border_style=Theme.ACTION if self.mode != "NAVIGATE" else Theme.SUBTITLE,
			width=46,
			padding=(1, 2),
		)
		connector = Table.grid()
		connector.add_row("")
		connector.add_row("")
		connector.add_row(f" [{Theme.ACCENT}]══▶[/] ")
		return Align.center(
			Columns([left_panel, Align.center(connector), right_panel], align="center")
		)

	def _refresh_file_list(self):
		targets = ["scripts", "engine", "."]
		self.available_files = []
		for path in targets:
			if os.path.exists(path):
				files = [
					os.path.join(path, f)
					for f in sorted(os.listdir(path))
					if f.endswith(".py")
				]
				self.available_files.extend(files)
