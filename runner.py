"""
🔱 VEMBER-OS NODE RUNNER (v1.0.5 Patch)
Handles asynchronous process execution for Vember-OS nodes.
Uses non-blocking thread-queues to stream real-time telemetry to the TUI.
"""

import subprocess
import threading
import queue
import os
import signal

class NodeRunner:
    def __init__(self):
        self.output_queue = queue.Queue()
        self.is_running = False
        self.process = None

    def execute(self, node_path):
        """
        Spawns a node process in a background thread.
        Uses unbuffered (-u) execution for real-time telemetry streaming.
        """
        if self.is_running:
            return

        def run():
            self.is_running = True
            try:
                # 🔱 1.0.5 Optimization: Added stderr redirect to stdout
                # This ensures we catch Python Tracebacks in the Inspector panel.
                self.process = subprocess.Popen(
                    ["python3", "-u", node_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    preexec_fn=os.setsid # Create process group for clean termination
                )

                # Stream lines from the process to the TUI queue
                if self.process.stdout:
                    for line in iter(self.process.stdout.readline, ''):
                        self.output_queue.put(line)
                
                self.process.wait()
            except Exception as e:
                self.output_queue.put(f"[bold red]Execution Error:[/] {str(e)}\n")
            finally:
                self.is_running = False
                self.process = None

        thread = threading.Thread(target=run, daemon=True)
        thread.start()

    def stop(self):
        """
        Forcefully terminate the running node and its children.
        """
        if self.process:
            try:
                # 🔱 1.0.5 Shift: Kill the entire process group
                # This stops any sub-shells the node might have opened.
                os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            except Exception:
                self.process.terminate()
            
            self.is_running = False
            self.process = None

    def get_latest_output(self):
        """
        Drains the queue and returns accumulated text.
        Returns an empty string if no new data is present.
        """
        out = []
        while not self.output_queue.empty():
            try:
                out.append(self.output_queue.get_nowait())
            except queue.Empty:
                break
        return "".join(out)