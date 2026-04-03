"""
NAME: THERMAL MATRIX | Real-time mapping of high-fidelity thermal data.
"""

import psutil
import time
import sys
import random

# 🔱 Update the function signature to have a default (None)
def get_status_color(value, theme=None):
    """Maps value to a color. Uses theme if provided, otherwise defaults to Vember Dark."""
    if value < 50:
        return f"[{theme.primary}]" if theme else "[cyan]"
    if value < 80:
        return f"[{theme.secondary}]" if theme else "[blue]"
    return f"[{theme.alert}]" if theme else "[bright_red]"

def run_diagnostic():
    try:
        while True:
            # Stats Fetch
            temps = psutil.sensors_temperatures()
            amd_key = next((k for k in temps.keys() if k in ["k10temp", "tctl"]), None)
            package_temp = temps[amd_key][0].current if amd_key else 0
            per_core_load = psutil.cpu_percent(interval=None, percpu=True)
            
            output = ""
            # 🔱 3. Text Label Update
            temp_color = get_status_color(package_temp)
            output += f"[bold cyan]TOTAL CPU TEMP:[/] {temp_color}{package_temp:>6.1f}°C[/]\n"
            output += "[dim]" + "— " * 15 + "[/]\n\n"
            
            # 🔱 1 & 2. Color Guide for Bars
            for i, load in enumerate(per_core_load[:12]):
                color = get_status_color(load)
                bar_length = int(load / 10)
                # Building the status-colored bar
                bar = f"{color}{'█' * bar_length}[/][dim]{'░' * (10 - bar_length)}[/]"
                output += f"[bold white]Core {i:02d}[/] | {bar} | {color}{load:>5.1f}%[/]\n"
            
            sys.stdout.write(output + "--- REFRESH ---\n")
            sys.stdout.flush()
            time.sleep(0.5)
    except KeyboardInterrupt:
        # 🔱 5. Exit Logic
        sys.exit(0)

if __name__ == "__main__":
    run_diagnostic()