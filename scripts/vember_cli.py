"""
🔱 VEMBER-OS: VEMBER_CLI
Metadata: Enter summary of VEMBER_CLI functionality here.
"""
"""
🔱 VEMBER OS
"""
import os
import sys

# 🔱 VEMBER PATH INJECTION
# This ensures 'scripts' is recognized as a module from the root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table
from rich.align import Align

from scripts.ui_core import VemberTheme as Theme


class CodexManager:
	"""The central help repository for Vember OS."""

	@staticmethod
	def render_help():
		table = Table(
			box=None,
			padding=(0, 2),
			show_header=True,
			header_style=f"bold {Theme.ACCENT}",
		)
		table.add_column("COMMAND", style="white")
		table.add_column("DESCRIPTION", style="dim")

		# Your specific aliases and help items
		table.add_row("uv run setup", "Launch the Forge Setup Guide")
		table.add_row("uv run cli", "Engage the Developer Console")
		table.add_row("gh auth status", "Check GitHub identity link")
		table.add_row("git checkout -b", "Create and switch to a new branch")

		return Panel(
			table,
			title=f"[{Theme.ACCENT}]VEMBER CODEX // COMMANDS[/]",
			border_style=Theme.ACTION,
			subtitle="[dim]Press ENTER to return[/]",
		)


class TerminalInput:
	"""Handles raw OS-level keystrokes for live cursor navigation."""

	@staticmethod
	def get_key() -> str:
		if os.name == "nt":
			import msvcrt

			key = msvcrt.getch()
			if key in (b"\x00", b"\xe0"):
				key = msvcrt.getch()
				if key == b"H":
					return "up"
				if key == b"P":
					return "down"
			elif key == b"\r":
				return "enter"
			elif key == b"\x03":
				raise KeyboardInterrupt
			return ""
		else:
			import tty
			import termios

			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)
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
				elif ch == "\x03":
					raise KeyboardInterrupt
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			return ""


class VemberCLI:
    """Live interactive menu controller enforcing the High-Five Method Rule."""

    def __init__(self):
        self.console = Console()
        self.selection = 0
        # New state variables for the Dual-Node UI
        self.active_node = None
        self.node_output = ""
        self.is_processing = False

        self.menu_items = [
            {
                "label": "Setup Local Forge",
                "cmd": "SETUP",
                "desc": "Initialize system dependencies",
            },
            {
                "label": "Review Codebase",
                "cmd": "ARCHITECT",
                "desc": "Audit architectural metadata",
            },
            {
                "label": "Vanguard Integrity",
                "cmd": "VANGUARD",
                "desc": "Audit dependencies & logic tests",
            },
            # 🔱 The 'Beta' Look
            {
                "label": f"Windfall Engine [bold red]NEW[/] [bold purple](Beta)[/]",
                "cmd": "WINDFALL",
                "desc": "Code Reflection & Generative Matrix",
            },
            {
                "label": "Commands & Help",
                "cmd": "CODEX",
                "desc": "Frequently used commands",
            },
            {
                "label": "Exit Developer Console",
                "cmd": "EXIT",
                "desc": "Sever connection to Forge",
            },
        ]

    def _generate_layout(self) -> Align:
        """The Master Engine: Merged with overflow protection."""
        # 1. Setup the Left Panel
        welcome_msg = f"[{Theme.PRIMARY}]Welcome, [/{Theme.PRIMARY}][{Theme.USER_COLOR}]{Theme.USER_NAME}[/][{Theme.PRIMARY}]. Select a protocol to engage.[/]"

        menu_table = Table(show_header=False, box=None, padding=(0, 2), pad_edge=False)
        menu_table.add_column("Cursor", justify="right", style=Theme.ACCENT)
        # Added no_wrap=True to prevent label wrapping
        menu_table.add_column("Label", no_wrap=True)

        menu_table.add_row("", welcome_msg)
        menu_table.add_row("", "")

        for idx, item in enumerate(self.menu_items):
            if idx == self.selection:
                menu_table.add_row("►", f"[bold {Theme.SELECTED}]{item['label']}[/]")
            else:
                color = Theme.SECONDARY if "Windfall" in item["label"] else "white"
                menu_table.add_row("", f"[{color}]{item['label']}[/]")
            if idx == len(self.menu_items) - 2:
                menu_table.add_row("", "")

        current_desc = self.menu_items[self.selection]["desc"]
        menu_table.add_row("", "")
        menu_table.add_row("", f"[{Theme.SUBTITLE}][italic]{current_desc}[/italic][/]")

        # Dynamic Width Calculation (Slimmer when side-node is active)
        panel_kwargs = Theme.get_panel_style().copy()
        panel_kwargs["width"] = 40 if self.active_node else 52

        action_bar = (
			f"[{Theme.ACCENT}]Navigate: [↑/↓][/] | [{Theme.ACTION}]Launch: [Enter][/]"
		)

        left_panel = Panel(
			menu_table,
			title=f"[{Theme.TITLE}]🔱 VEMBER OS // DEVELOPER CONSOLE[/]",
			subtitle=action_bar,
			**panel_kwargs,
		)

        # 2. Build the Right Node (Audit/Architect)
        if self.active_node:
            connector = Table.grid(expand=True)
            connector.add_row(""); connector.add_row(""); connector.add_row(f" [{Theme.ACCENT}]══▶[/] ")

            # Slim the right panel to 38 to ensure 40 + 38 fits on standard 80-char terminals
            right_panel = Panel(
				self.node_output,
				title=f"[{Theme.ACCENT}]{self.active_node}[/]",
				border_style=Theme.ACCENT if self.is_processing else Theme.ACTION,
				width=38, 
				subtitle="[dim]Protocol Active[/]",
				padding=(0, 1)
			)
            return Align.center(
				Columns(
					[left_panel, Align.center(connector), right_panel], align="center"
				)
			)

        return Align.center(left_panel)

    def _execute(self, cmd_id: str) -> None:
        """The Forge Dispatcher: Routing commands to specialized Battlefield nodes."""

        if cmd_id == "EXIT":
            sys.exit(0)

        # 🔱 SETUP ENGINE
        if cmd_id == "SETUP":
            from scripts.vember_setup import SetupEngine

            SetupEngine().run()
            return

        # 🔱 ARCHITECT ENGINE
        if cmd_id == "ARCHITECT":
            from scripts.architect import Architect
            from rich.live import Live

            with Live(None, console=self.console, auto_refresh=False) as live:
                Architect().ignite(self, live)
            return

        # 🔱 VANGUARD ENGINE
        if cmd_id == "VANGUARD":
            from scripts.vanguard import Vanguard
            from rich.live import Live

            with Live(None, console=self.console, auto_refresh=False) as live:
                Vanguard().ignite(self, live)
            return

        # 🔱 WINDFALL ENGINE (Phase 3 Rebirth)
        if cmd_id == "WINDFALL":
            from scripts.windfall import Windfall
            from rich.live import Live

            with Live(None, console=self.console, auto_refresh=False) as live:
                Windfall().ignite(self, live)
            return

        # 🔱 CODEX / HELP
        if cmd_id == "CODEX":
            self.active_node = "Vember Codex"
            self.node_output = CodexManager.render_help()
            return

        # Fallback for standard shell commands
        os.system("cls" if os.name == "nt" else "clear")
        subprocess.run(cmd_id, shell=True)
        input("\nPress ENTER to return...")

    def _render_menu(self) -> None:
        """Standardized refresh call for the Vember UI."""
        os.system("cls" if os.name == "nt" else "clear")
        self.console.print(self._generate_layout())
        self.console.print(Align.center(f"[dim]{Theme.VERSION}[/]"))

    def _handle_selection(self) -> bool:
        """Standardizes selection routing and removes legacy placeholders."""
        target = self.menu_items[self.selection]
        cmd_id = target["cmd"]

        if cmd_id == "EXIT":
            return False

        # 🔱 Removed the legacy 'if cmd_id == "WINDFALL"' block that was here
        # It now flows directly into the _execute routing below
        self._execute(cmd_id)
        return True

    def run(self) -> None:
        """The main interactive capture loop managing global cursor state."""
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

        try:
            while True:
                self._render_menu()
                key = TerminalInput.get_key()

                if key == "up":
                    self.selection = max(0, self.selection - 1)
                elif key == "down":
                    self.selection = min(len(self.menu_items) - 1, self.selection + 1)
                elif key == "enter":
                    should_continue = self._handle_selection()
                    if not should_continue:
                        break
        finally:
            os.system("cls" if os.name == "nt" else "clear")
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()


def main() -> None:
	try:
		cli = VemberCLI()
		cli.run()
	except KeyboardInterrupt:
		sys.stdout.write("\033[?25h")
		sys.stdout.flush()
		Console().print("\n[dim]Session terminated.[/dim]")
		sys.exit(0)


if __name__ == "__main__":
	main()
