"""
🔱 VEMBER-OS: BRANDING
Metadata: Enter summary of BRANDING functionality here.
"""
"""
🔱 VEMBER OS
"""
"""
🔱 VEMBER-OS: ASSET REGISTRY
Centralized design system. Defines the visual identity, iconography, 
and thematic color palettes for widgets and mesh navigation.
"""

from dataclasses import dataclass
from rich.panel import Panel

@dataclass
class VemberTheme:
    primary: str
    secondary: str
    success: str
    warning: str
    alert: str
    text: str
    dim: str
    cursor: str
    selection: str
    border_action: str = "#00f2ff"
    bg: str = "#000000"
    name: str = "ember"


class VemberAssets:
    THEME = VemberTheme(
        primary="#00f2ff",
        secondary="#0066ff",
        success="#00ff95",
        warning="#ffcc00",
        alert="#ff3300",
        text="#ffffff",
        dim="#444444",
        cursor="#ffff00",  # Example: Electric Yellow
        selection="#ffffff",  # Example: Pure White
        border_action="#00f2ff",
        name="ember",
    )
    ACTIVE_THEME = THEME

    @classmethod
    def apply_theme(cls, name: str):
        cls.ACTIVE_THEME = cls.THEME
        cls.ACTIVE_THEME.name = name
        return cls.ACTIVE_THEME

    # 🖼️ ICONS (Universal Registry)
    class Icons:
        # System
        KERNEL = "🔱"
        NODE   = "⬢"
        HUB    = "🕸️"
        LINK   = "🔗"

        # Atmospheric (Stratos-Link)
        TEMP     = "🌡️"
        OVERCAST = "☁️"
        SUNNY    = "☀️"
        SNOW     = "❄️"
        RAIN     = "🌧️"

        # System (Thermal Matrix)
        CPU    = "⚡"
        RAM    = "💾"
        THERM  = "🔥"

    # 🔱 LOGOS & BRANDING
    @classmethod
    def get_logo(cls):
        return f"[bold {cls.THEME.primary}]{cls.Icons.KERNEL}  V E M B E R - O S[/]\n[dim]─────────────────────────────[/]"

    @classmethod
    def splash_panel(cls):
        return Panel(
            cls.get_logo(),
            subtitle="[dim]INITIALIZING MESH TOPOLOGY...[/]",
            border_style=cls.THEME.secondary,
            expand=False
        )
