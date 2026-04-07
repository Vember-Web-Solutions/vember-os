"""
🔱 VEMBER-OS: VERSION SYNCHRONIZER
Utility for managing cross-component version alignment. Ensures the 
Project Manifest and Alpha Build numbers remain synchronized across branches.
"""

import tomllib
import re
from pathlib import Path

def sync():
	# 🔱 Find the project root (one level up from /scripts)
	root = Path(__file__).parent.parent
	
	pyproject_path = root / "pyproject.toml"
	readme_path = root / "README.md"

	# 1. Read version from pyproject.toml
	if not pyproject_path.exists():
		print(f"❌ Error: Could not find {pyproject_path}")
		exit(1)

	with open(pyproject_path, "rb") as f:
		data = tomllib.load(f)
		version = data["project"]["version"]

	# 2. Update README.md badge
	if not readme_path.exists():
		print(f"❌ Error: Could not find {readme_path}")
		exit(1)

	content = readme_path.read_text()
	
	pattern = r"version-(.*?)-orange"
	new_badge = f"version-{version}-orange"
	
	updated_content = re.sub(pattern, new_badge, content)
	
	if content != updated_content:
		readme_path.write_text(updated_content)
		print(f"🔱 VEMBER-OS | Version synced to {version}")
	else:
		print("🔱 VEMBER-OS | Version already up to date.")

if __name__ == "__main__":
	sync()