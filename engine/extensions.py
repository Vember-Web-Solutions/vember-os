"""
🔱 VEMBER-OS: EXTENSIONS
Metadata: Enter summary of EXTENSIONS functionality here.
"""
"""
🔱 VEMBER OS
"""
"""
🔱 VEMBER-OS: EXTENSIONS
Visual and functional augmentations for the Vember-OS ecosystem.
"""
from collections import deque
from rich.console import RenderableType
from rich.progress import ProgressBar
from rich.table import Table
from rich.text import Text

class VemberExtension:
	"""Base Extension: Maintains state and temporal buffers."""
	def __init__(self, label: str, width: int = 30, color: str = "cyan"):
		self.label = label
		self.width = width
		self.color = color
		self.buffer = deque([0.0] * width, maxlen=width)

	def update(self, value: float):
		"""Standardized ingestion for telemetry data."""
		self.buffer.append(float(value))

	def __rich__(self) -> RenderableType:
		raise NotImplementedError("Extensions must implement a __rich__ render method.")

class Sparkline(VemberExtension):
	"""Temporal Graph: High-density Unicode height mapping."""
	def __rich__(self) -> Text:
		levels = " ▂▃▄▅▆▇█"
		spark_str = ""
		for val in self.buffer:
			idx = int((max(0, min(val, 99)) / 100) * len(levels))
			spark_str += levels[idx]
		
		return Text.assemble(
			(f"{self.label:.<15}", self.color),
			(f" {spark_str}", "white")
		)

class StatusMetric(VemberExtension):
	"""Metric Bar: Label + Progress Bar + Current Value."""
	def __rich__(self) -> Table:
		table = Table.grid(expand=True)
		table.add_column(width=15) # Label
		table.add_column()         # Progress Bar
		table.add_column(width=8, justify="right") # Value %

		latest = self.buffer[-1]
		bar = ProgressBar(
			total=100, 
			completed=latest, 
			width=None, 
			complete_style=self.color,
			finished_style=self.color
		)
		
		table.add_row(
			Text(self.label, style=f"bold {self.color}"),
			bar,
			Text(f"{latest:>3.0f}%", style="dim")
		)
		return table
	
class NetworkStream(VemberExtension):
	"""Vertical Stream: Shows Up/Down flow with connection metadata."""
	def __init__(self, interface: str, ssid: str = "N/A", **kwargs):
		super().__init__(label=interface, **kwargs)
		self.ssid = ssid
		self.signal = 0  # 0-100

	def __rich__(self) -> Table:
		# Create a condensed 2-column flow
		table = Table.grid(expand=True)
		table.add_column(justify="left")   # Metadata (SSID/IFACE)
		table.add_column(justify="right")  # The "Stream" visuals

		# The 'Flow' Logic: We use the buffer to determine 'brightness' or 'density'
		# Top characters move up, bottom move down
		up_stream = "".join(["⇡" if val > 0 else " " for val in list(self.buffer)[-10:]])
		dn_stream = "".join(["⇣" if val > 0 else " " for val in list(self.buffer)[-10:]])

		metadata = Text.assemble(
			(f"📡 {self.label} ", self.color),
			(f"({self.ssid}) ", "dim"),
			(f"SIG: {self.signal}%", "green" if self.signal > 70 else "yellow")
		)

		streams = Text.assemble(
			("UP ", "dim"), (up_stream, "magenta"),
			(" | ", "white"),
			(dn_stream, "cyan"), (" DN", "dim")
		)

		table.add_row(metadata, streams)
		return table