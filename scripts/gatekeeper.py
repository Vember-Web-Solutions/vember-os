"""
🔱 VEMBER-OS: GATEKEEPER
Quality Assurance script for branch merges and release readiness.
"""
import os
import sys
import re

def check_files():
    failed = False
    print("\n[🔱] VEMBER-OS ARCHITECTURAL AUDIT")
    print("-" * 40)

    for root, dirs, files in os.walk("."):
        # Skip system and environment folders
        if any(skip in root for skip in ['.git', 'venv', '__pycache__', 'build', 'dist']):
            continue
            
        for file in files:
            # 🔱 NEW: Ignore __init__.py and non-python files
            if file == "__init__.py" or not file.endswith(".py"):
                continue
                
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.splitlines()

                    # 1. Check for Vember Header Symbol
                    # Checking first 3 lines to be safe with different docstring styles
                    header_valid = any("🔱" in line for line in lines[:3])
                    if not header_valid:
                        print(f"❌ {path}: Missing 🔱 symbol in header.")
                        failed = True

                    # 2. Check for Legacy Version Strings
                    if re.search(r"\(v\d+\.\d+\.\d+.*?\)", content):
                        print(f"❌ {path}: Found legacy version string.")
                        failed = True

                    # 3. Check Nodes for Description Parser Hook
                    if "nodes/" in path:
                        if "Description:" not in content:
                            print(f"❌ {path}: Missing 'Description:' hook.")
                            failed = True
            except Exception as e:
                print(f"⚠️ {path}: Could not read file ({e})")

    return not failed

def main():
    if check_files():
        print("-" * 40)
        print("✅ AUDIT PASSED: Repository compliant with Vember Standard.")
        sys.exit(0)
    else:
        print("-" * 40)
        print("🚨 AUDIT FAILED: Correct issues before merging.")
        sys.exit(1)

if __name__ == "__main__":
    main()