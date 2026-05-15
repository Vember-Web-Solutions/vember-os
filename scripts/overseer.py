"""
🔱 VEMBER-OS: OVERSEER
Metadata: Enter summary of OVERSEER functionality here.
"""

# scripts/overseer.py (Hardened Vember Edition)
import subprocess
import json
import os


class VemberTestOverseer:
    def __init__(self, target_dir="tests/"):
        self.target_dir = target_dir
        self.raw_report_path = "scripts/report.json"
        self.ai_report_path = "scripts/overseer_report.json"

    def execute_and_report(self):
        # Run pytest quietly with the JSON reporter
        cmd = [
            "pytest",
            self.target_dir,
            "-q",
            "--no-header",
            "--json-report",
            f"--json-report-file={self.raw_report_path}",
        ]
        subprocess.run(cmd, capture_output=True, text=True)
        return self.analyze_results()

    def analyze_results(self):
        if not os.path.exists(self.raw_report_path):
            return {"passed": 0, "failed": 0, "failures": [], "status": "ERROR"}

        with open(self.raw_report_path, "r") as f:
            full_data = json.load(f)

        summary = {
            "passed": full_data["summary"].get("passed", 0),
            "failed": full_data["summary"].get("failed", 0),
            "failures": [],
        }

        # Extract only the critical failure data to save tokens and context
        for t in full_data.get("tests", []):
            if t["outcome"] == "failed":
                # Get the crash location safely
                crash = t.get("call", {}).get("crash", {})
                failure_node = {
                    "id": t["nodeid"],
                    "line_no": crash.get("lineno", "Unknown"),
                    "error": crash.get("message", "Logic Divergence Detected"),
                    "type": t.get("call", {}).get("longrepr", "").split("\n")[-1],
                }
                summary["failures"].append(failure_node)

        # Save for Arcade's ingestion
        with open(self.ai_report_path, "w") as f:
            json.dump(summary, f, indent=4)

        return summary

    def print_tactical_summary(self, summary):
        """The clean, surgical Pilot dashboard."""
        print("\n" + "═" * 45)
        print("🔱 VEMBER OS: MISSION READINESS")

        # Display green checks for passed nodes
        checks = " ".join(["✅" for _ in range(summary["passed"])])
        print(f"Nodes Nominal: {checks} ({summary['passed']})")

        if summary["failed"] > 0:
            print(f"Status:        ⚠️ {summary['failed']} LOGIC ERRORS DETECTED")
            print("═" * 45)
            for i, fail in enumerate(summary.get("failures", []), 1):
                print(f"\n[FAILURE {i}]: {fail['id']}")
                print(f"  ∟ Location:  Line {fail['line_no']}")
                print(
                    f"  ∟ Diagnostic: {fail['error'][:100]}..."
                )  # Truncate for clean view
        else:
            print("Status:        ✅ ALL SYSTEMS NOMINAL")
        print("═" * 45 + "\n")


if __name__ == "__main__":
    overseer = VemberTestOverseer()
    data = overseer.execute_and_report()
    overseer.print_tactical_summary(data)
