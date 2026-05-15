"""
🔱 VEMBER-OS: WINDFALL
Metadata: Multistage Code Reflection & Surgical Navigation Matrix. (Beta)
"""

import ast
import os
import re
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree
from rich.live import Live
from rich.columns import Columns
from rich.align import Align
from rich.text import Text
from rich.console import Group
from scripts.ui_core import VemberTheme as Theme
from scripts.vember_setup import TerminalInput


class Windfall:
	"""🔱 WINDFALL (Beta): Modular Code Architect."""

	def __init__(self):
		self.selection = 0
		self.file_index = 0
		self.window_start = 0
		self.window_size = 12
		self.mode = "NAVIGATE"  # NAVIGATE, REFLECT
		self.focus_path = ""
		self.metadata = "No Metadata Found."
		self.class_nodes = []
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

			if key == "up":
				if self.mode == "NAVIGATE":
					self.file_index = max(0, self.file_index - 1)
					if self.file_index < self.window_start:
						self.window_start = self.file_index
				else:
					self.selection = max(0, self.selection - 1)

			elif key == "down":
				if self.mode == "NAVIGATE":
					self.file_index = min(
						len(self.available_files) - 1, self.file_index + 1
					)
					if self.file_index >= self.window_start + self.window_size:
						self.window_start = self.file_index - self.window_size + 1
				else:
					self.selection = min(len(self.menu_items) - 1, self.selection + 1)

			elif key == "enter":
				if self.mode == "NAVIGATE":
					if self.available_files:
						self.focus_path = self.available_files[self.file_index]
						self._reflect_file()
						self.mode = "REFLECT"
				elif self.mode == "REFLECT":
					if self.selection == 2:  # Return
						break
					if self.selection == 0:  # Back to Select
						self.mode = "NAVIGATE"
					if self.selection == 1:  # Re-scan
						self._reflect_file()

	def _reflect_file(self):
		"""Extracts Metadata and Class/Method hierarchy."""
		self.class_nodes = []
		try:
			with open(self.focus_path, "r", encoding="utf-8") as f:
				raw_content = f.read()
				tree = ast.parse(raw_content)

			# Extract Metadata
			doc = ast.get_docstring(tree)
			if doc:
				meta_match = re.search(r"Metadata:\s*(.*)", doc, re.IGNORECASE)
				self.metadata = (
					meta_match.group(1) if meta_match else doc.split("\n")[0]
				)
			else:
				self.metadata = "[red]Missing Vember DNA Metadata Seal.[/]"

			# Map Classes and Methods
			for node in ast.iter_child_nodes(tree):
				if isinstance(node, ast.ClassDef):
					methods = [
						n.name for n in node.body if isinstance(n, ast.FunctionDef)
					]
					self.class_nodes.append({"name": node.name, "methods": methods})
				elif isinstance(node, ast.FunctionDef):
					# Handle top-level functions as well
					self.class_nodes.append(
						{"name": f"Func: {node.name}", "methods": []}
					)
		except Exception as e:
			self.metadata = f"[red]Error:[/] {str(e)}"

	def _generate_layout(self):
		# NODE 01: WINDFALL CONTROL
		menu_table = Table(show_header=False, box=None, padding=(0, 1))
		for idx, item in enumerate(self.menu_items):
			cur = "►" if idx == self.selection and self.mode == "REFLECT" else " "
			sty = (
				f"bold {Theme.SELECTED}"
				if idx == self.selection and self.mode == "REFLECT"
				else "white"
			)
			menu_table.add_row(cur, f"[{sty}]{item['label']}[/]")

		left_panel = Panel(
			menu_table,
			title=f"[{Theme.TITLE}]🔱 WINDFALL[/]",
			subtitle=f"[dim]{self.mode}[/]",
			border_style=Theme.ACTION,
			width=32,
		)

		# NODE 02: THE DYNAMIC BATTLEFIELD
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

			if self.window_start + self.window_size < len(self.available_files):
				content.add_row(" ", "[dim]... more files below[/]")

			renderable_content = content
		else:
			title = "CODE REFLECTOR"
			# Build the reflection group
			meta_text = Text(f"📜 {self.metadata}\n", style="italic yellow")

			node_tree = Tree(
				f"[{Theme.ACCENT}]📦 {os.path.basename(self.focus_path)}[/]"
			)
			for cls in self.class_nodes:
				c_node = node_tree.add(f"[bold cyan]Class:[/] {cls['name']}")
				for m in cls["methods"][:5]:  # Preview first 5 methods
					c_node.add(f"[dim]└─[/] [yellow]Method:[/] {m}")

			# Use Group to combine the Metadata text and the Tree
			renderable_content = Group(meta_text, node_tree)

		right_panel = Panel(
			Align.left(renderable_content),
			title=f"[{Theme.ACCENT}]{title}[/]",
			border_style=Theme.ACTION,
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
