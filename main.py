"""VEMBER OS form-first bootstrap.

This branch intentionally strips the fragile runtime and UI layer back to a simple,
working interactive form before we re-introduce the richer presentation layer.
"""

import sys
from dataclasses import dataclass

from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel


@dataclass
class VemberConfig:
    project_name: str
    environment: str
    docker_enabled: bool
    ui_mode: str
    description: str

    def summary(self) -> str:
        return (
            f"Project: {self.project_name}\n"
            f"Environment: {self.environment}\n"
            f"Docker: {'enabled' if self.docker_enabled else 'disabled'}\n"
            f"UI mode: {self.ui_mode}\n"
            f"Description: {self.description}"
        )


def _ask(prompt: str, default: str | None = None, *, allow_empty: bool = False) -> str:
    suffix = f" [{default}]" if default is not None else ""
    while True:
        value = input(f"{prompt}{suffix}: ").strip()
        if value:
            return value
        if allow_empty:
            return default or ""
        if default is not None:
            return default
        print("This field is required.")


def _ask_bool(prompt: str, default: bool = True) -> bool:
    default_text = "Y/n" if default else "y/N"
    while True:
        value = input(f"{prompt} [{default_text}]: ").strip().lower()
        if not value:
            return default
        if value in {"y", "yes"}:
            return True
        if value in {"n", "no"}:
            return False
        print("Please answer yes or no.")


def collect_form() -> VemberConfig:
    print("\nVEMBER OS bootstrap form\n")

    project_name = _ask("Project name", default="vember-os")
    environment = _ask("Environment", default="dev")
    docker_enabled = _ask_bool("Enable Docker build support", default=True)
    ui_mode = _ask("UI mode", default="form-first")
    description = _ask(
        "Short description",
        default="Minimal shell for a clean rebuild",
        allow_empty=True,
    )

    return VemberConfig(
        project_name=project_name,
        environment=environment,
        docker_enabled=docker_enabled,
        ui_mode=ui_mode,
        description=description,
    )


def build_route_panel(route_name: str, config: VemberConfig) -> Panel:
    route_content = {
        "Bootstrap": "Bootstrap configuration is active.\nProject can be initialized and validated.",
        "Runtime": "Runtime layer is ready for rebuild.\nFocus on stable startup and screen state.",
        "Docker": "Docker orchestration is enabled.\nThe project can be built and launched in containers.",
        "Settings": "Settings are available for shell defaults.\nProject metadata is already loaded.",
    }
    return Panel(
        route_content.get(route_name, "System ready."),
        title=f"{route_name.upper()}",
        border_style="cyan",
        padding=(1, 2),
    )


def render_shell(config: VemberConfig, selected_index: int = 0, route_name: str | None = None) -> None:
    console = Console()
    layout = Layout(name="root")
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3),
    )

    layout["header"].update(
        Panel(
            "VEMBER OS",
            style="bold cyan",
            title="core",
            subtitle="stable build",
        )
    )

    menu_items = [
        "Bootstrap",
        "Runtime",
        "Docker",
        "Settings",
    ]
    menu_lines = []
    for idx, item in enumerate(menu_items):
        prefix = "▶" if idx == selected_index else " "
        menu_lines.append(f"[bold cyan]{prefix}[/] {idx + 1}. {item}")

    menu_panel = Panel(
        "\n".join(menu_lines),
        title="MAIN MENU",
        border_style="cyan",
        padding=(1, 2),
    )

    status_panel = Panel(
        "Bootstrap shell ready\nProject ready for build orchestration",
        title="SYSTEM STATUS",
        border_style="green",
        padding=(1, 2),
    )

    if route_name is None:
        body_panel = Align.center(
            Panel(
                "\n".join(
                    [
                        "[bold cyan]VEMBER OS[/] base shell is stable.",
                        "The form layer is working and the visual shell is loading cleanly.",
                    ]
                ),
                title="READY",
                border_style="cyan",
                padding=(1, 2),
            )
        )
    else:
        body_panel = build_route_panel(route_name, config)

    layout["body"].update(
        Group(
            status_panel,
            "",
            menu_panel,
            "",
            body_panel,
        )
    )

    layout["footer"].update(
        Panel(
            f"Project: {config.project_name} | Mode: {config.ui_mode} | Docker: {'enabled' if config.docker_enabled else 'disabled'}",
            style="green",
        )
    )
    console.print(layout)


def interactive_shell(config: VemberConfig) -> None:
    selected_index = 0
    current_route = None
    while True:
        print("\n" * 2)
        render_shell(config, selected_index=selected_index, route_name=current_route)
        key = input("Choose a menu item [1-4, q to quit]: ").strip().lower()
        if key in {"q", "quit", "exit"}:
            print("Exiting VEMBER OS shell.")
            return
        if key in {"1", "2", "3", "4"}:
            selected_index = int(key) - 1
            current_route = ["Bootstrap", "Runtime", "Docker", "Settings"][selected_index]
            continue
        if key in {"w", "up", "8"}:
            selected_index = (selected_index - 1) % 4
            current_route = ["Bootstrap", "Runtime", "Docker", "Settings"][selected_index]
            continue
        if key in {"s", "down", "2"}:
            selected_index = (selected_index + 1) % 4
            current_route = ["Bootstrap", "Runtime", "Docker", "Settings"][selected_index]
            continue
        if key in {"b", "back"}:
            current_route = None
            continue


def main() -> VemberConfig:
    config = collect_form()
    print("\nConfiguration accepted:\n")
    print(config.summary())
    interactive_shell(config)
    return config


if __name__ == "__main__":
    main()
