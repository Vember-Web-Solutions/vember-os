"""
🔱 VEMBER-OS ASSET REGISTRY (v2.0.0)
Centralized Design System for Widgets and Mesh Navigation.
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
    bg: str = "#000000"

class VemberAssets:
    # 🎨 THEMES
    THEME = VemberTheme(
        primary="#00f2ff",    # Electric Cyan
        secondary="#0066ff",  # Deep Cobalt
        success="#00ff95",    # Neon Mint
        warning="#ffcc00",    # Warning Amber
        alert="#ff3300",      # Plasma Red
        text="#ffffff",       # Pure White
        dim="#444444"         # Graphite Grey
    )

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