"""
================================================================================
🔱 VEMBER-OS: NEXUS_NODE CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: NEXUS_AUTHORIZATION_NODE
Context Path:  /dev/nexus.py

Cryptographic identity notarization and session-state handshake manager.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

import hashlib
from rich.panel import Panel
from rich import box
from assets.branding import VemberAssets


class NexusNode:
    """🛡️ THE NEXUS: Cryptographic identity and authorization ledger."""

    def __init__(self, raw_data: str = "VEMBER_SESSION_ACTIVE"):
        self.status = "READY"
        self.signature = self._generate_signature(raw_data)

    def _generate_signature(self, data: str) -> str:
        """Generates a cryptographic-style fingerprint for the current session."""
        sha_hash = hashlib.sha256(data.encode()).hexdigest()
        return f"0x{sha_hash[:7].upper()}..."

    def __rich__(self):
        T = VemberAssets.ACTIVE_THEME

        # Build the ledger content dynamically
        ledger_content = (
            f" [dim]Status:[/] [bold {T.success}]{self.status}[/]\n"
            f" [dim]Signature:[/] [bold {T.border_nexus}]{self.signature}[/]"
        )

        # Encapsulate into the panel
        return Panel(
            ledger_content,
            title=f" [bold {T.border_nexus}]NEXUS AUTHORIZATION[/] ",
            title_align="center",
            box=box.ROUNDED,
            border_style=T.border_nexus,
            width=63,
        )
