"""
================================================================================
🔱 VEMBER-OS: SETUP CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: SETUP_FORGE_NODE
Context Path:  /dev/setup.py

Environment calibration and Docker group verification.
================================================================================
"""

from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from assets.branding import VemberAssets

# Map the active theme from the centralized registry
Theme = VemberAssets.ACTIVE_THEME


class SetupNode:
    """The environment calibrator: handles Docker groups and system checks."""

    def __init__(self):
        self.selection = 0
        self.calibration_steps = ["Verify Docker", "Check Permissions", "System Init"]
        self.status_message = "Awaiting system handshake..."

    def verify_docker_environment(self):
        """Worker logic: Checks for docker engine binary."""
        # Add your existing sub-process check logic here
        return True, True

    def get_permissions_view(self, active_index=0):
        """Worker logic: Returns status strings for UI display."""
        _, in_docker_grp = self.verify_docker_environment()

        if in_docker_grp:
            return f"[{Theme.success}][ ACTIVE ][/]", "Socket Anchored", "Ready."
        return (
            f"[{Theme.warning}][ CALIBRATE ][/]",
            "Attach Docker socket",
            "Run sudo usermod",
        )

    def render(self):
        """Returns the UI component for the VemberCLI host controller."""

        table = Table(box=None, padding=(0, 1), show_header=False)
        for i, step in enumerate(self.calibration_steps):
            # Apply theme colors dynamically
            style = f"bold {Theme.primary}" if i == self.selection else "dim"
            prefix = f"[{Theme.primary}]▶[/]" if i == self.selection else "  "
            table.add_row(prefix, f"[{style}]{step}[/]")

        # Assemble the UI Panel
        return Panel(
            Align.center(table),
            title=f"[{Theme.primary}]SETUP_FORGE_NODE[/]",
            border_style=Theme.primary,
            padding=(1, 2),
        )
