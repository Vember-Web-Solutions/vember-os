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
        # Skip git, env, and hidden folders
        if '.git' in root or 'venv' in root or '__pycache__' in root:
            continue
            
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.splitlines()

                    # 1. Check for Vember Header Symbol
                    if lines and "🔱" not in lines[1]:
                        print(f"❌ {path}: Missing 🔱 symbol in header.")
                        failed = True

                    # 2. Check for Legacy Version Strings in docstrings
                    # Looks for patterns like (v1.0.0)
                    if re.search(r"\(v\d+\.\d+\.\d+.*?\)", content):
                        print(f"❌ {path}: Found legacy version string.")
                        failed = True

                    # 3. Check Nodes for Description Parser Hook
                    if "nodes/" in path:
                        if "Description:" not in content:
                            print(f"❌ {path}: Missing 'Description:' hook for NodeScanner.")
                            failed = True

    if not failed:
        print("-" * 40)
        print("✅ AUDIT PASSED: Repository is compliant with Vember Standard.")
        return True
    else:
        print("-" * 40)
        print("🚨 AUDIT FAILED: Correct the issues above before merging.")
        return False

if __name__ == "__main__":
    if not check_files():
        sys.exit(1)