"""
🔱 VEMBER-OS: UI_CORE
Metadata: Enter summary of UI_CORE functionality here.
"""
"""
🔱 VEMBER OS
"""
import os


class VemberTheme:
    """The visual DNA of Vember OS."""

    VERSION = "v1.0.4-dev"
    USER_NAME = os.environ.get("USER", "Developer").title()

    # Updated Palette from your screenshot
    PRIMARY = "bold white"  # Borders
    SECONDARY = "bold magenta"  # Passive / Windfall
    ACCENT = "bold cyan"  # Cursors / Brackets
    ACTION = "bold green"  # Success / Titles
    SELECTED = "orange1"  # Selection
    USER_COLOR = "bold green"  # Your Name
    WARNING = "red"  # Badges

    TITLE = "bold green"
    SUBTITLE = "magenta"

    @classmethod
    def get_panel_style(cls):
        return {
            "border_style": cls.PRIMARY,
            "padding": (1, 4),
            "expand": False,
            "width": 75,
        }
