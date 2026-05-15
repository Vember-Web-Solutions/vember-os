"""
🔱 VEMBER-OS: VANGUARD
Metadata: Environmental Integrity, Dependency Mapping & Logic Validation.
"""

import os
import subprocess
import time
import json
import re
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.columns import Columns
from rich.align import Align
from rich.console import Console
from scripts.ui_core import VemberTheme as Theme
from scripts.vember_setup import TerminalInput


class Vanguard:
    """Protects the environment via uv dependency audits and logic validation."""

    def __init__(self):
        self.console = Console()
        self.selection = 0
        self.active_node = "Environmental HUD"
        self.node_output = "[dim]Awaiting integrity scan...[/]"
        self.is_processing = False
        self.test_failures = []
        self.menu_items = [
            {"label": "Audit Packages", "desc": "Map uv managed dependencies"},
            {"label": "Validate Logic", "desc": "Engage pytest diagnostic suite"},
            {"label": "Return to Console", "desc": "Sever integrity link"},
        ]

    def ignite(self, engine, live):
        """Main interaction loop for the Vanguard battlefield."""
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

                self.is_processing = True
                if self.selection == 0:
                    self._audit_packages(live)
                elif self.selection == 1:
                    self._run_tests(live)
                self.is_processing = False

    def _audit_packages(self, live):
        """Uses uv to map current virtual environment state."""
        self.node_output = "[white]Querying uv package manager...[/]"
        live.update(self._generate_layout(), refresh=True)

        try:
            # Native uv call for ultra-fast dependency mapping
            result = subprocess.run(
                ["uv", "pip", "list", "--format", "json"],
                capture_output=True,
                text=True,
            )
            packages = json.loads(result.stdout)

            table = Table(
                box=None,
                padding=(0, 1),
                show_header=True,
                header_style=f"bold {Theme.ACCENT}",
            )
            table.add_column("PACKAGE", style="white")
            table.add_column("VERSION", justify="right", style="dim")

            # Show top packages to fit the node battlefield
            for pkg in packages[:12]:
                table.add_row(pkg["name"], f"v{pkg['version']}")

            self.node_output = table
        except Exception as e:
            self.node_output = (
                f"[{Theme.WARNING}]ERROR:[/] Connection to uv failed.\n[dim]{str(e)}[/]"
            )

    def _run_tests(self, live):
        """Executes logic validation and captures surgical failure data."""
        self.node_output = "[white]Engaging Logic Diagnostics...[/]"
        live.update(self._generate_layout(), refresh=True)
        self.test_failures = []

        # Run pytest in quiet mode to capture failures
        result = subprocess.run(
            ["pytest", "--tb=short", "-q"], capture_output=True, text=True
        )

        if result.returncode == 0:
            self.node_output = f"\n[{Theme.ACTION}]✔ ALL LOGIC TESTS PASSED[/]\n\n[dim]Environment is stable and secure.[/]"
        else:
            # Parse failures into human-readable strings for the remediation node
            lines = result.stdout.splitlines()
            for line in lines:
                if line.startswith("FAILED"):
                    # Clean up the path for the UI
                    clean_fail = line.replace("FAILED ", "").split("::")[-1]
                    self.test_failures.append(clean_fail)

            self.node_output = f"[{Theme.WARNING}]LOGIC BREACH DETECTED[/]\n[dim]{len(self.test_failures)} modules failed validation.[/]"

    def _generate_layout(self):
        """Assembles the Vanguard Battlefield view."""
        # NODE 01: VANGUARD MENU
        menu_table = Table(show_header=False, box=None, padding=(0, 1))
        for idx, item in enumerate(self.menu_items):
            cur = "►" if idx == self.selection else " "
            sty = f"bold {Theme.SELECTED}" if idx == self.selection else "white"
            menu_table.add_row(cur, f"[{sty}]{item['label']}[/]")

        left_panel = Panel(
            menu_table,
            title=f"[{Theme.TITLE}]🔱 VANGUARD[/]",
            subtitle=f"[dim]Manager: UV[/]",
            border_style=Theme.ACTION,
            width=32,
        )

        # NODE 02: SYSTEM HUD
        right_stack = Table.grid(expand=True)
        right_stack.add_row(
            Panel(
                self.node_output,
                title=f"[{Theme.ACCENT}]INTEGRITY HUD[/]",
                border_style=Theme.ACCENT if self.is_processing else Theme.ACTION,
                width=46,
                padding=(1, 2),
            )
        )

        # NODE 03: LOGIC REMEDIATION (The 'Card' summoned by failure)
        if self.test_failures:
            fail_table = Table(box=None, padding=(0, 1), show_header=False)
            for fail in self.test_failures[:5]:
                fail_table.add_row(f"[{Theme.WARNING}]![/] {fail[:35]}")

            right_stack.add_row(Align.center(f"[{Theme.ACCENT}]║[/]"))
            right_stack.add_row(
                Panel(
                    fail_table,
                    title=f"[{Theme.WARNING}]LOGIC REMEDIATION[/]",
                    border_style=Theme.WARNING,
                    width=46,
                    subtitle="[dim]Check tests/ for details[/]",
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
    """Standalone ignition for Vanguard Integrity checks."""
    console = Console()
    vanguard = Vanguard()
    with Live(None, console=console, auto_refresh=False) as live:
        vanguard.ignite(None, live)


if __name__ == "__main__":
    main()
