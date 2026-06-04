import pytest
from unittest.mock import patch, MagicMock
from dev.vanguard import Vanguard
from pathlib import Path
import json


def test_vanguard_integrity_scan_logic():
	vanguard = Vanguard()

	# 1. Setup mock result file
	mock_results = {"summary": {"passed": 5, "failed": 0}}
	output_dir = Path("exports")
	output_dir.mkdir(exist_ok=True)
	report_file = output_dir / "test_results.json"

	with open(report_file, "w") as f:
		json.dump(mock_results, f)

	# 2. Mock subprocess
	with patch("subprocess.run") as mock_run:
		vanguard.run_integrity_scan()

		# 3. CRITICAL: Manually load the results after the scan call
		# (or ensure your run_integrity_scan calls this internally)
		vanguard.load_test_results()

		# DEBUG: Print the state to see what Vanguard actually parsed
		print(f"Vanguard State: {vanguard.test_results}")

		# Assertions
		assert mock_run.called
		assert vanguard.test_results["passed"] == 5
