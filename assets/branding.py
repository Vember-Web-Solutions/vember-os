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
    name: str
    primary: str
    secondary: str
    success: str
    warning: str
    alert: str
    text: str
    dim: str
    cursor: str
    selection: str
    border_nexus: str
    border_action: str
    bg: str = "#000000"


class VemberAssets:
    THEME_PRESETS = {
        "midnight": VemberTheme(
            name="Midnight",
            primary="#00f2ff",
            secondary="#0066ff",
            success="#00ff95",
            warning="#ffcc00",
            alert="#ff3300",
            text="#ffffff",
            dim="#444444",
            cursor="#ffff00",
            selection="#ffffff",
            border_nexus="#bd00ff",
            border_action="#ffcc00",
        ),
        "sakura": VemberTheme(
            name="Sakura",
            primary="#ff69b4",
            secondary="#ff1493",
            success="#98fb98",
            warning="#ffb7c5",
            alert="#dc143c",
            text="#fff0f5",
            dim="#8b668b",
            cursor="#ffc0cb",
            selection="#ffffff",
            border_nexus="#ff85c1",
            border_action="#ff69b4",
        ),
        "kuro": VemberTheme(
            name="Kuro",
            primary="#aaaaaa",
            secondary="#666666",
            success="#cccccc",
            warning="#888888",
            alert="#ff4444",
            text="#eeeeee",
            dim="#555555",
            cursor="#ffffff",
            selection="#dddddd",
            border_nexus="#777777",
            border_action="#999999",
        ),
        "shinto": VemberTheme(
            name="Shinto",
            primary="#dc143c",
            secondary="#8b0000",
            success="#228b22",
            warning="#ff8c00",
            alert="#b22222",
            text="#fff5f5",
            dim="#8b4513",
            cursor="#ffffff",
            selection="#ffeeee",
            border_nexus="#ff4500",
            border_action="#dc143c",
        ),
    }

    ACTIVE_THEME = THEME_PRESETS["midnight"]
    THEME = ACTIVE_THEME

    @classmethod
    def apply_theme(cls, key: str) -> None:
        theme_key = key.lower()
        if theme_key in cls.THEME_PRESETS:
            cls.ACTIVE_THEME = cls.THEME_PRESETS[theme_key]
            cls.THEME = cls.ACTIVE_THEME

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
