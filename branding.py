"""
🔱 VEMBER-OS BRANDING & THEME REGISTRY (v1.0.5 Patch)
Centralized identity management for the Windfall Engine.
Defines the visual DNA, TrueColor palettes, and ANSI assets for the ecosystem.
"""

from dataclasses import dataclass

@dataclass
class VemberTheme:
    """Encapsulates the color DNA for the Vember-OS interface."""
    name: str
    primary: str    # Headers, Logo, and Main Borders
    secondary: str  # Sidebar borders and accents
    success: str    # Low-usage CPU states (0-50%)
    warning: str    # Mid-usage CPU states (51-80%)
    alert: str      # Critical CPU states / Errors
    text: str       # General paragraph content
    dim: str        # Non-essential UI elements
    bg: str = "#000000"

# 🎨 THEME LIBRARY (Upgraded to TrueColor Hex)
# Note: Rich will automatically downsample these if the terminal doesn't support them.
THEMES = {
    "VEMBER_DARK": VemberTheme(
        name="Vember Dark",
        primary="#00f2ff",    # Electric Cyan
        secondary="#0066ff",  # Deep Cobalt
        success="#00ff95",    # Neon Mint
        warning="#ffcc00",    # Warning Amber
        alert="#ff3300",      # Plasma Red
        text="#ffffff",       # Pure White
        dim="#444444"         # Graphite Grey
    ),
    "VEMBER_GOLD": VemberTheme(
        name="Vember Gold",
        primary="#ffcc00",
        secondary="#b8860b",
        success="#adff2f",
        warning="#ffa500",
        alert="#ff0000",
        text="#ffffff",
        dim="#555555"
    ),
    "VOID": VemberTheme(
        name="Void",
        primary="#ffffff",
        secondary="#333333",
        success="#aaaaaa",
        warning="#666666",
        alert="#ff00ff",
        text="#cccccc",
        dim="#222222"
    )
}

# 🔱 ASSET LIBRARY
# Using Rich markup inside the logo for integrated branding
LOGO_ANSI = """
[bold #00f2ff]🔱  V E M B E R - O S[/]
[dim]─────────────────────────────[/]
[#0066ff]  NODE-BASED ARCHITECTURE[/]
"""

SPLASH_SUBTITLE = "[dim]INITIALIZING CORE SYSTEMS...[/]"