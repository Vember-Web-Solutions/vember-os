import tomllib
import re
from pathlib import Path

def sync():
	# 1. Read version from pyproject.toml
	with open("pyproject.toml", "rb") as f:
		data = tomllib.load(f)
		version = data["project"]["version"]

	# 2. Update README.md badge
	readme_path = Path("README.md")
	content = readme_path.read_text()
	
	# Updated regex in sync_version.py to handle the new PEP 440 format
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