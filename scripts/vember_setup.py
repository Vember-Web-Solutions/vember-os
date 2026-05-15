"""
🔱 VEMBER-OS: VEMBER_SETUP
Metadata: Enter summary of VEMBER_SETUP functionality here.
"""
"""
🔱 VEMBER OS
"""
import os
import sys
import subprocess
import time
import json
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.align import Align
from rich.columns import Columns
from scripts.ui_core import VemberTheme as Theme

# --- 🔱 GLOBAL CROSS-PLATFORM HANDSHAKE ---
# This ensures keyboard modules are visible to all classes globally
if os.name == "nt":
	import msvcrt
else:
	import tty
	import termios
	import fcntl


class TerminalInput:
	"""Handles raw OS-level keystrokes for zero-latency navigation."""

	@staticmethod
	def get_key() -> str:
		if os.name == "nt":
			if not msvcrt.kbhit():
				return ""
			key = msvcrt.getch()
			if key in (b"\x00", b"\xe0"):
				key = msvcrt.getch()
				if key == b"H":
					return "up"
				if key == b"P":
					return "down"
			elif key == b"\r":
				return "enter"
			elif key == b"\x08":
				return "backspace"
			return key.decode("utf-8", errors="ignore")
		else:
			fd = sys.stdin.fileno()
			old = termios.tcgetattr(fd)
			try:
				tty.setraw(sys.stdin.fileno())
				ch = sys.stdin.read(1)
				if ch == "\x1b":
					ch2 = sys.stdin.read(2)
					if ch2 == "[A":
						return "up"
					if ch2 == "[B":
						return "down"
				elif ch in ("\r", "\n"):
					return "enter"
				elif ch in ("\x7f", "\x08"):
					return "backspace"
				return ch
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old)


class IdentityManager:
	def __init__(self):
		self.state = {
			"User Name": {"val": "", "done": False},
			"User Email": {"val": "", "done": False},
			"GitHub Link": {"val": "Not Linked", "done": False},
		}

	def render_briefing(self, protocol_name):
		"""Clean system briefing for context switches."""
		# We use the theme accent for the protocol name to make it pop without the brackets
		return (
			f" [{Theme.ACCENT}]SYSTEM PROTOCOL:[/] [white]{protocol_name.upper()}[/]\n"
			f" ──────────────────────────────────────\n\n"
			f" This will suspend the Vember UI and launch\n"
			f" the GitHub CLI authentication flow.\n\n"
			f" 1. Follow the browser prompts.\n"
			f" 2. Complete the 2FA sequence.\n"
			f" 3. Return here once finished.\n\n"
			f" [{Theme.ACTION}]Press ENTER to ignite handshake...[/]"
		)

	def render_form(self, active_field, buffer, committed=False):
		lines = []
		for name, data in self.state.items():
			if name == active_field and not committed:
				lines.append(
					f"[{Theme.ACCENT}]► {name}:[/] [white]{buffer}[/][blink {Theme.ACCENT}]_[/]"
				)
			else:
				icon = f"[{Theme.ACTION}]✔[/]" if data["done"] else "[dim]○[/]"
				val = data["val"] if data["val"] else "..."
				lines.append(f"{icon} {name}: [dim]{val}[/]")

		if committed:
			lines.append(f"\n[{Theme.ACTION}]IDENTITY SYNCED[/]")
			if self.state["GitHub Link"]["done"]:
				lines.append(f"[white]GitHub commands enabled in terminal.[/]")
			lines.append(f"\n[dim]Press ENTER to return to menu...[/dim]")
		return "\n".join(lines)

	def ignite(self, engine, live):
		# 1. Git Identity Phase
		for field in ["User Name", "User Email"]:
			buffer = ""
			while True:
				engine.node_output = self.render_form(field, buffer)
				live.update(engine._generate_layout(), refresh=True)
				key = TerminalInput.get_key()
				if key == "enter" and buffer.strip():
					self.state[field] = {"val": buffer, "done": True}
					cmd = "user.name" if field == "User Name" else "user.email"
					subprocess.run(
						f'git config --global {cmd} "{buffer}"',
						shell=True,
						capture_output=True,
					)
					break
				elif key == "backspace":
					buffer = buffer[:-1]
				elif len(key) == 1 and key.isprintable():
					buffer += key

		# 2. GitHub Briefing Phase
		engine.active_node = "GitHub Handshake"
		while True:
			engine.node_output = self.render_briefing("GitHub Link")
			live.update(engine._generate_layout(), refresh=True)
			if TerminalInput.get_key() == "enter":
				break

		# 3. Context Switch
		live.stop()
		os.system('cls' if os.name == 'nt' else 'clear')
		# Professional splash for the black screen
		engine.console.print(f"\n\n [{Theme.ACCENT}]🔱 VEMBER OS // EXTERNAL AUTHENTICATION[/]")
		engine.console.print(f" [dim]Handshaking with github.com...[/]\n")
		
		subprocess.run("gh auth login", shell=True)

		# 4. Return and Confirm
		self.state["GitHub Link"] = {"val": "Linked", "done": True}
		os.system("cls" if os.name == "nt" else "clear")
		live.start()

		while True:
			engine.node_output = self.render_form(None, None, committed=True)
			live.update(engine._generate_layout(), refresh=True)
			if TerminalInput.get_key() == "enter":
				break

		engine._log_event("Identity Setup", "SUCCESS")


class SetupEngine:
	"""Main Setup Engine adhering to the High-Five Method Rule."""

	def __init__(self):
		self.console = Console()
		self.selection = 0
		self.active_node, self.node_output, self.is_processing = None, "", False
		self.log_file = "logs/vember_history.json"
		os.makedirs("logs", exist_ok=True)
		self.actions = [
			{"label": "Ignite Forge Sync", "id": "SYNC", "cmd": "uv sync"},
			{
				"label": "Build Docker Core",
				"id": "DOCKER",
				"cmd": "docker compose build",
			},
			{"label": "Identity & Git Setup", "id": "GIT_SETUP", "cmd": "IDENTITY"},
			{"label": "Return to Main Menu", "id": "EXIT", "cmd": ""},
		]

	def _get_diagnostics(self) -> Table:
		diag = Table(box=None, padding=(0, 2), show_header=False)
		checks = {
			"uv engine": "uv --version",
			"docker core": "docker --version",
			"git identity": "git config user.name",
		}
		for name, cmd in checks.items():
			res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
			passed = res.returncode == 0 and res.stdout.strip() != ""
			diag.add_row(
				name, f"[{Theme.ACTION}]✔[/]" if passed else f"[{Theme.WARNING}]❌[/]"
			)
		return diag

	def _log_event(self, action, status):
		entry = {
			"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			"user": Theme.USER_NAME,
			"action": action,
			"status": status,
		}
		hist = json.load(open(self.log_file)) if os.path.exists(self.log_file) else []
		hist.append(entry)
		with open(self.log_file, "w") as f:
			json.dump(hist, f, indent=4)

	def _generate_layout(self) -> Align:
		# 1. Build Menu (Separated from chained calls)
		menu = Table(box=None, padding=(0, 1), show_header=False)
		for idx, item in enumerate(self.actions):
			cur = f"[{Theme.ACCENT}]►[/{Theme.ACCENT}]" if idx == self.selection else ""
			sty = f"bold {Theme.SELECTED}" if idx == self.selection else "white"
			menu.add_row(cur, f"[{sty}]{item['label']}[/]")

		# 2. Build Left Content Grid
		left_grid = Table.grid(expand=True)
		left_grid.add_row(Align.center(f"[{Theme.TITLE}]VEMBER OS // SETUP GUIDE[/]"))
		left_grid.add_row(Align.center(f"[dim]Dependency Check[/]"))
		left_grid.add_row(Align.center(self._get_diagnostics()))
		left_grid.add_row("")
		left_grid.add_row(Align.center(menu))
		left_panel = Panel(
			left_grid, border_style=Theme.ACTION, width=38, title="[bold white]🔱[/]"
		)

		# 3. Build Right Node (If Active)
		if self.active_node:
			con_grid = Table.grid(expand=True)
			con_grid.add_row(""); con_grid.add_row(""); con_grid.add_row(""); con_grid.add_row(f" [{Theme.ACCENT}]══▶[/] ")

			# The right panel now uses the active node name as the title
			right_panel = Panel(
				f"\n[{Theme.ACCENT}]LOGS:[/]\n{self.node_output}", 
				border_style=Theme.ACTION if not self.is_processing else Theme.ACCENT, 
				width=42, 
				title=f"[{Theme.ACCENT}]{self.active_node}[/]",
				subtitle="[dim]Protocol Active[/]"
			)
			return Align.center(Columns([left_panel, Align.center(con_grid), right_panel], align="center"))

		return Align.center(left_panel)

	def _stream_process(self, action, live):
		"""Standardized streaming for system protocols with NoneType safety."""
		self.active_node = action["label"]
		self.is_processing = True
		self.node_output = "Initializing..."

		# 1. Ensure subprocess correctly pipes stdout
		proc = subprocess.Popen(
			action["cmd"], 
			shell=True, 
			stdout=subprocess.PIPE, # Required for .fileno() and .read()
			stderr=subprocess.STDOUT, 
			text=True, 
			bufsize=1
		)

		# 2. Verify stdout exists before configuring non-blocking IO
		if os.name != 'nt' and proc.stdout:
			try:
				fd = proc.stdout.fileno()
				fl = fcntl.fcntl(fd, fcntl.F_GETFL)
				fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
			except Exception:
				pass # Fallback if fcntl fails

		while proc.poll() is None:
			try:
				# 3. Check for stdout before reading to prevent 'NoneType' error
				if proc.stdout:
					out = proc.stdout.read(64)
					if out:
						# Clean and trim for the Vember UI box
						clean = out.strip().replace('\n', ' ')
						self.node_output = f"[white]>> {clean[-35:]}[/]"
			except Exception:
				pass # Catch read timeouts or empty buffers

			live.update(self._generate_layout(), refresh=True)
			time.sleep(0.05)

		proc.wait()
		self.is_processing = False
		self.node_output = f"[{Theme.ACTION}]PROTOCOL COMPLETE[/]"
		live.update(self._generate_layout(), refresh=True)

		# Log the successful engagement
		self._log_event(action["label"], "SUCCESS")

		# Persistence: Wait for user dismissal
		TerminalInput.get_key()
		self.active_node = None

	def run(self):
		sys.stdout.write("\033[?25l")
		os.system("cls" if os.name == "nt" else "clear")
		with Live(
			self._generate_layout(), console=self.console, auto_refresh=False
		) as live:
			while True:
				live.update(self._generate_layout(), refresh=True)
				key = TerminalInput.get_key()
				if key == "up":
					self.selection = max(0, self.selection - 1)
				elif key == "down":
					self.selection = min(len(self.actions) - 1, self.selection + 1)
				elif key == "enter":
					target = self.actions[self.selection]
					if target["id"] == "EXIT":
						break
					if target["id"] == "GIT_SETUP":
						self.active_node = "Identity Setup"
						IdentityManager().ignite(self, live)
						self.active_node = None
					else:
						self._stream_process(target, live)
		sys.stdout.write("\033[?25h")


# --- 🔱 THE ENTRY POINT ---
def main():
	try:
		engine = SetupEngine()
		engine.run()
	except KeyboardInterrupt:
		sys.stdout.write("\033[?25h")
		sys.exit(0)


if __name__ == "__main__":
	main()
