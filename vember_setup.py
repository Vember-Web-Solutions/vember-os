#!/usr/bin/env python3
import os
import sys
import subprocess
import platform
import time

# --- BOOTSTRAP BLOCK ---
# Ensure 'rich' is installed before we build the TUI
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Confirm
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.table import Table
except ImportError:
    print("[🔱 VEMBER OS] -> Bootstrapping TUI Engine (installing 'rich')...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich", "-q"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Confirm
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.table import Table

console = Console()


def run_cmd(cmd, shell=True, capture=True):
    """Run a command and return success/fail."""
    try:
        if capture:
            subprocess.check_output(cmd, shell=shell, stderr=subprocess.STDOUT)
        else:
            subprocess.check_call(cmd, shell=shell)
        return True
    except subprocess.CalledProcessError:
        return False


def check_dependencies():
    """Builds a Rich table to show dependency status."""
    table = Table(title="Dependency Check", style="magenta")
    table.add_column("Module", style="cyan", no_wrap=True)
    table.add_column("Status", justify="center")

    deps = {
        "uv (Astral)": "uv --version",
        "GitHub CLI": "gh --version",
        "Docker": "docker --version",
    }

    all_passed = True
    for name, cmd in deps.items():
        if run_cmd(cmd):
            table.add_row(name, "[green]✔ INSTALLED[/green]")
        else:
            table.add_row(name, "[red]❌ MISSING[/red]")
            all_passed = False

    console.print(table)
    return all_passed


def handle_windows_wsl():
    """The Kellen Protocol: Force WSL on Windows."""
    console.print(
        Panel(
            "[bold red]WINDOWS OS DETECTED[/bold red]\nVember OS requires a Linux kernel for privileged container execution.",
            border_style="red",
        )
    )

    if Confirm.ask(
        "Would you like to install Windows Subsystem for Linux (Ubuntu) now?"
    ):
        console.print(
            "[yellow]Initiating WSL Installation... You may be prompted for Administrator privileges.[/yellow]"
        )
        run_cmd("wsl --install", capture=False)
        console.print(
            Panel(
                "[bold green]WSL Installation Triggered.[/bold green]\n1. Please restart your computer if prompted.\n2. Open the 'Ubuntu' app from your Start Menu.\n3. Re-clone the repo and run this script inside Ubuntu.",
                border_style="green",
            )
        )
        sys.exit(0)
    else:
        console.print("[red]Setup aborted. Linux/WSL is strictly required.[/red]")
        sys.exit(1)


def configure_linux_permissions():
    """Fixes sudo and docker group permissions."""
    console.print("\n[magenta]🔱 Checking System Permissions...[/magenta]")
    user = os.environ.get("USER", "root")

    # Check Docker group
    if not run_cmd(f"groups {user} | grep docker"):
        if Confirm.ask(
            f"User '{user}' is not in the 'docker' group. Add them now? (Requires sudo)"
        ):
            run_cmd(f"sudo usermod -aG docker {user}", capture=False)
            console.print(
                "[green]✔ Added to docker group. (You may need to log out and back in for this to take effect)[/green]"
            )
    else:
        console.print("[green]✔ Docker permissions optimal.[/green]")


def sync_forge():
    """Uses uv to sync the environment."""
    console.print("\n[magenta]🔱 Synchronizing Local Forge...[/magenta]")
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Running 'uv sync'...", total=None)
        success = run_cmd("uv sync", capture=False)

    if success:
        console.print(
            "[bold green]✔ Environment Synchronized Successfully.[/bold green]"
        )
    else:
        console.print(
            "[bold red]❌ Failed to sync environment. Is 'uv' installed correctly?[/bold red]"
        )


def main():
    os.system("cls" if os.name == "nt" else "clear")
    console.print(
        Panel(
            "[bold magenta]🔱 VEMBER OS // LOCAL SETUP TOOLKIT[/bold magenta]\n[cyan]Initializing System Architecture...[/cyan]",
            border_style="magenta",
        )
    )
    time.sleep(1)

    os_name = platform.system().lower()

    if os_name == "windows":
        handle_windows_wsl()
    elif os_name in ["linux", "darwin"]:
        console.print(
            f"[green]✔ Native UNIX-like system detected ({os_name.upper()}).[/green]\n"
        )

        check_dependencies()
        configure_linux_permissions()

        if Confirm.ask("\nProceed with Virtual Environment Synchronization?"):
            sync_forge()

        console.print(
            Panel(
                "[bold green]ALL SYSTEMS NOMINAL.[/bold green]\nRun [cyan]docker compose up --build[/cyan] to ignite the core.",
                border_style="green",
            )
        )


if __name__ == "__main__":
    main()
