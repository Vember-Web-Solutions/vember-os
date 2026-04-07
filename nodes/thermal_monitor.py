"""
🔱 VEMBER-OS THERMAL MATRIX (v1.0.5 Patch)
Real-time telemetry mapping for high-fidelity CPU thermal data.
Optimized for 12-core distribution and TrueColor status monitoring.
"""

import psutil
import time
import sys

# 🔱 Refactor Note: Removed unused random and theme imports to keep the node 
# footprint small. The TUI handles the final theme wrapping.

def get_status_color(value):
    """
    Maps percentage/temperature values to Vember-standard semantic colors.
    Returns Rich markup tags.
    """
    if value < 50:
        return "[cyan]"
    if value < 80:
        return "[yellow]" # Using yellow for mid-range visibility
    return "[bold red]"

def run_diagnostic():
    """
    Main execution loop. Streams unbuffered CPU data to the NodeRunner.
    """
    try:
        # Initialize CPU percent to seed the first reading
        psutil.cpu_percent(interval=None)
        
        while True:
            # 1. Stats Fetching
            temps = psutil.sensors_temperatures()
            # Search for common AMD/Intel thermal drivers
            thermal_keys = ["k10temp", "tctl", "coretemp", "cpu_thermal"]
            amd_key = next((k for k in temps.keys() if k in thermal_keys), None)
            
            package_temp = temps[amd_key][0].current if amd_key and temps[amd_key] else 0.0
            per_core_load = psutil.cpu_percent(interval=None, percpu=True)
            
            # 2. Frame Construction
            output = []
            temp_color = get_status_color(package_temp)
            
            output.append(f"[bold cyan]TOTAL CPU TEMP:[/] {temp_color}{package_temp:>6.1f}°C[/]")
            output.append("[dim]" + "— " * 15 + "[/]\n")
            
            # 3. 12-Core Distribution Mapping
            # We slice to 12 cores to maintain UI alignment in the Inspector
            for i, load in enumerate(per_core_load[:12]):
                color = get_status_color(load)
                bar_length = int(load / 10)
                
                # Composite Bar: Solid blocks for usage, dotted for headroom
                bar = f"{color}{'█' * bar_length}[/][dim]{'░' * (10 - bar_length)}[/]"
                output.append(f"[bold white]CORE {i:02d}[/] | {bar} | {color}{load:>5.1f}%[/]")
            
            # 4. The Vember-OS Refresh Handshake
            # The '--- REFRESH ---' tag tells main.py to wipe the buffer for this frame
            final_frame = "\n".join(output) + "\n--- REFRESH ---\n"
            
            sys.stdout.write(final_frame)
            sys.stdout.flush()
            
            # High-frequency update (2Hz)
            time.sleep(0.5)
            
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
    except Exception as e:
        sys.stdout.write(f"[bold red]THERMAL CRITICAL:[/] {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    run_diagnostic()