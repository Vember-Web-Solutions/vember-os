"""
🔱 VEMBER-OS BRANDING & THEME REGISTRY
Centralized identity management for the Windfall Engine.
"""
from dataclasses import dataclass

@dataclass
class VemberTheme:
	name: str
	primary: str    # Main borders / Logo
	secondary: str  # Sidebar / Accents
	text: str       # General content
	alert: str      # Warnings / Critical nodes
	bg: str = "black"

# 🎨 THEME LIBRARY
THEMES = {
	"VEMBER_DARK": VemberTheme(
		name="Vember Dark",
		primary="cyan",
		secondary="blue",
		text="white",
		alert="bright_red"
	),
	"VEMBER_GOLD": VemberTheme(
		name="Vember Gold",
		primary="yellow",
		secondary="gold3",
		text="white",
		alert="red"
	),
	"VOID": VemberTheme(
		name="Void",
		primary="white",
		secondary="grey37",
		text="grey70",
		alert="magenta"
	)
}

# 🔱 ASSET LIBRARY
LOGO_ANSI = """
	🔱  V E M B E R - O S
  ─────────────────────────────
  [ NODE-BASED ARCHITECTURE ]
"""

SPLASH_SUBTITLE = "INITIALIZING CORE SYSTEMS..."