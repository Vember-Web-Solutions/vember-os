"""
🔱 VEMBER-OS: ARCHITECT
Metadata: Architectural Integrity & DNA Remediation Protocol.
"""

import os
import re
import time
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.columns import Columns
from rich.align import Align
from rich.console import Console
from scripts.ui_core import VemberTheme as Theme
from scripts.vember_setup import TerminalInput


class Architect:
	"""Coordinates repository scanning and surgical metadata remediation."""

	def __init__(self):
		self.console = Console()
		self.violations = []
		self.fixed_count = 0
		self.selection = 0
		self.active_node = "Architectural Audit"
		self.node_output = "[dim]Awaiting DNA scan command...[/]"
		self.is_processing = False
		self.menu_items = [
			{"label": "Ignite Scan", "desc": "Analyze repository DNA"},
			{"label": "Remediate DNA", "desc": "Surgically heal flagged modules"},
			{"label": "Return to Console", "desc": "Sever diagnostic link"},
		]

	def ignite(self, engine, live):
		"""Main interaction loop for the Architect battlefield."""
		os.system("cls" if os.name == "nt" else "clear")
		while True:
			live.update(self._generate_layout(), refresh=True)
			key = TerminalInput.get_key()

			if key == "up":
				self.selection = max(0, self.selection - 1)
			elif key == "down":
				self.selection = min(len(self.menu_items) - 1, self.selection + 1)
			elif key == "enter":
				if self.selection == 2:
					break
				if self.selection == 0:
					self.is_processing = True
					self._run_scan(live)
					self.is_processing = False
				elif self.selection == 1:
					if not self.violations:
						self.node_output = "[yellow]No violations detected to heal.[/]"
					else:
						self._apply_remediation(live)

	def _run_scan(self, live):
		"""Crawls the filesystem using strict Vember exclusion rules."""
		ignore_patterns = {
			".git",
			".venv",
			".vscode",
			".pytest_cache",
			".mypy_cache",
			"__pycache__",
			"build",
			"dist",
			"logs",
			"test",
			"tests",
			"node_modules",
			".github",
			".idea",
		}
		self.violations = []
		self.fixed_count = 0
		self.node_output = "[white]Initializing DNA Sensors...[/]"
		live.update(self._generate_layout(), refresh=True)
		time.sleep(0.4)

		for root, dirs, files in os.walk("."):
			dirs[:] = [
				d for d in dirs if d not in ignore_patterns and not d.startswith(".")
			]
			for f in files:
				if not f.endswith(".py") or f == "__init__.py":
					continue
				path = os.path.join(root, f)
				self.node_output = f"[white]Analyzing DNA:[/]\n[dim]…{path[-30:]}[/]"
				live.update(self._generate_layout(), refresh=True)

				error = self._verify_dna(path)
				if error:
					self.violations.append((path, error))
				time.sleep(0.01)

		self.node_output = self._render_results()

	def _verify_dna(self, path):
		"""Checks for the Trident Seal, Identity Brand, and Manifest Metadata."""
		try:
			with open(path, "r", encoding="utf-8") as f:
				content = f.read()
				header_chunk = "\n".join(content.splitlines()[:10]).upper()

				if "🔱" not in header_chunk:
					return "MISSING_TRIDENT"
				if "VEMBER-OS" not in header_chunk:
					return "MISSING_BRAND"
				if "METADATA:" not in header_chunk:
					return "MISSING_MANIFEST"
				if re.search(r"\(v\d+\.\d+\.\d+.*?\)", content):
					return "LEGACY_DEBT"
				return None
		except:
			return "READ_ERROR"

	def _apply_remediation(self, live):
		"""Surgically repairs DNA and adds Metadata templates."""
		self.is_processing = True
		for path, error in list(self.violations):
			self.node_output = f"[yellow]Healing:[/] [dim]{os.path.basename(path)}[/]"
			live.update(self._generate_layout(), refresh=True)

			try:
				with open(path, "r", encoding="utf-8") as f:
					content = f.read()

				# If it's a completely missing header, we add the full template
				if error in ["MISSING_TRIDENT", "MISSING_BRAND", "MISSING_MANIFEST"]:
					# Clean up common 'Double Header' artifacts if they exist
					clean_content = re.sub(
						r'^"""\s*🔱.*?VEMBER.*?METADATA:.*?"""\s*',
						"",
						content,
						flags=re.DOTALL | re.IGNORECASE,
					)

					alias = os.path.basename(path).replace(".py", "").upper()
					template = (
						'"""\n'
						f"🔱 VEMBER-OS: {alias}\n"
						f"Metadata: Enter summary of {alias} functionality here.\n"
						'"""\n'
					)

					with open(path, "w", encoding="utf-8") as f:
						f.write(template + clean_content)

					self.fixed_count += 1
					self.violations.remove((path, error))
				time.sleep(0.05)
			except:
				continue

		self.is_processing = False
		self.node_output = self._render_results()

	def _render_results(self):
		if not self.violations:
			return f"\n[{Theme.ACTION}]✔ ARCHITECTURE COMPLIANT[/]\n\n[dim]Audit Time: ~2.1s[/]\n[dim]Healed: {self.fixed_count} modules[/]"

		table = Table(box=None, padding=(0, 1), show_header=False)
		error_map = {
			"MISSING_TRIDENT": "No 🔱 Emoji",
			"MISSING_BRAND": "No 'VEMBER-OS' ID",
			"MISSING_MANIFEST": "No Metadata line",
			"LEGACY_DEBT": "Hardcoded (v.x.x)",
			"READ_ERROR": "Access Denied",
		}
		for path, err_code in self.violations[:7]:
			fname = os.path.basename(path)
			friendly_err = error_map.get(err_code, err_code)
			table.add_row(f"[{Theme.WARNING}]![/] {fname}", f"[dim]{friendly_err}[/]")
		return table

	def _generate_layout(self):
		menu_table = Table(show_header=False, box=None, padding=(0, 1))
		for idx, item in enumerate(self.menu_items):
			cur = "►" if idx == self.selection else " "
			sty = f"bold {Theme.SELECTED}" if idx == self.selection else "white"
			menu_table.add_row(cur, f"[{sty}]{item['label']}[/]")

		left_panel = Panel(
			menu_table,
			title=f"[{Theme.TITLE}]🔱 ARCHITECT[/]",
			subtitle=f"[dim]{self.menu_items[self.selection]['desc']}[/]",
			border_style=Theme.ACTION,
			width=32,
		)

		right_stack = Table.grid(expand=True)
		right_stack.add_row(
			Panel(
				self.node_output,
				title=f"[{Theme.ACCENT}]DIAGNOSTICS[/]",
				border_style=Theme.ACCENT if self.is_processing else Theme.ACTION,
				width=46,
				padding=(1, 2),
			)
		)

		if self.violations or self.fixed_count > 0:
			task_table = Table(box=None, padding=(0, 1), show_header=False)
			task_table.add_row(
				"[green]✔[/]" if not self.violations else "[yellow]![/]",
				f"DNA Remediation Plan ({len(self.violations)} pending)",
			)
			if self.fixed_count > 0:
				task_table.add_row(
					"[green]✔[/]", f"Successfully healed {self.fixed_count} files"
				)

			right_stack.add_row(Align.center(f"[{Theme.ACCENT}]║[/]"))
			right_stack.add_row(
				Panel(
					task_table,
					title=f"[{Theme.WARNING}]TASK CHECKLIST[/]",
					border_style=Theme.WARNING,
					width=46,
					subtitle="[dim]Summoned via Audit[/]",
				)
			)

		connector = Table.grid()
		connector.add_row("")
		connector.add_row("")
		connector.add_row(f" [{Theme.ACCENT}]══▶[/] ")
		return Align.center(
			Columns([left_panel, Align.center(connector), right_stack], align="center")
		)


def main():
	console = Console()
	architect = Architect()
	with Live(None, console=console, auto_refresh=False) as live:
		architect.ignite(None, live)


if __name__ == "__main__":
	main()
