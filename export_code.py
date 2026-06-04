import os
import ast
from pathlib import Path
from datetime import datetime


def get_ast_info(file_path):
	"""Parses Python files to extract structure using AST."""
	try:
		with open(file_path, "r", encoding="utf-8") as f:
			tree = ast.parse(f.read())

		info = {"imports": [], "classes": {}}
		info["globals"] = []
		
		for node in tree.body:
			if isinstance(node, (ast.Import, ast.ImportFrom)):
				info["imports"].append(ast.unparse(node))
			elif isinstance(node, ast.ClassDef):
				# Extract methods specifically for this class
				methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
				info["classes"][node.name] = methods
			elif isinstance(node, ast.FunctionDef):
				info["globals"].append(node.name)
				
		return info
	except Exception as e:
		return {"imports": [], "classes": [], "methods": [], "error": str(e)}


def main():
	# 1. Select Directory
	dirs = [
		d
		for d in os.listdir(".")
		if os.path.isdir(d) and not d.startswith((".", "_", ".venv"))
	]
	print("Available directories to export:")
	for i, d in enumerate(dirs):
		print(f"[{i}] {d}")

	try:
		choice = int(input("\nSelect directory index: "))
		target = dirs[choice]
	except (ValueError, IndexError):
		print("Invalid selection.")
		return

	# 2. Setup Export
	output = Path(f"exports/{target}_export.md")
	output.parent.mkdir(exist_ok=True)

	with open(output, "w", encoding="utf-8") as md:
		md.write(f"# 🔱 VEMBER OS: {target.upper()} DISTRICT EXPORT\n")
		md.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

		# 3. TOC
		md.write("## 📜 TABLE OF CONTENTS\n")
		files = sorted([f for f in Path(target).rglob("*.py")])
		for f in files:
			anchor = str(f).replace(os.sep, "-").replace(".", "-")
			md.write(f"* [{f}](#{anchor})\n")

		md.write("\n---\n\n")

		# 4. Content Loop
		for f_path in files:
			anchor = str(f_path).replace(os.sep, "-").replace(".", "-")
			struct = get_ast_info(f_path)

			md.write(f"### <a id='{anchor}'></a> 📄 FILE: {f_path}\n\n")
			md.write("#### 📜 METADATA\n\n> No Node Passport detected.\n\n")

			md.write(
				"#### 🚀 IMPORTS\n\n```python\n"
				+ ("\n".join(struct["imports"]) or "# None")
				+ "\n```\n\n"
			)

			md.write("#### 🏛️ CLASSES & GEARS\n\n")
			if not struct['classes']:
				md.write("No classes defined.\n\n")
			else:
				for cls_name, methods in struct['classes'].items():
					method_str = ", ".join(methods) if methods else "No methods defined."
					md.write(f"- **{cls_name}**: {method_str}\n")
			
			if struct['globals']:
				md.write(f"\n#### ⚡ GLOBAL GEARS: {', '.join(struct['globals'])}\n\n")
			# -----------------------------

			md.write("```python\n")
			md.write(f_path.read_text(encoding="utf-8"))
			md.write("\n```\n\n---\n\n")

	print(f"Export created at {output}")


if __name__ == "__main__":
	main()
