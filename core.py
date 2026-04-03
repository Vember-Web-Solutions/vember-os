import pathlib
import ast

class NodeScanner:
	def __init__(self, ops_dir="ops"):
		self.ops_path = pathlib.Path(ops_dir)
		# Ensure the ops directory exists in the Docker sandbox
		self.ops_path.mkdir(parents=True, exist_ok=True)

	def get_node_metadata(self, file_path):
		"""Uses AST to peek at the file without executing it."""
		try:
			with open(file_path, "r") as f:
				tree = ast.parse(f.read())
				# Get the first docstring in the file
				docstring = ast.get_docstring(tree) or "No description provided."
				return docstring
		except Exception:
			return "Error parsing node metadata."

	def scan(self):
		nodes = []
		for file in self.ops_path.glob("*.py"):
			if not file.name.startswith(("private_", "__")):
				raw_doc = self.get_node_metadata(file)
				
				# 🔱 NEW SPLIT LOGIC:
				# If '|' exists, the left is the Name, the right is the Description
				if "|" in raw_doc:
					name_part, desc_part = raw_doc.split("|", 1)
				else:
					name_part, desc_part = file.stem.replace("_", " ").upper(), raw_doc

				nodes.append({
					"id": file.stem,
					"name": name_part.strip(), # This fixes the Sidebar
					"description": desc_part.strip(), # This fixes the Information Panel
					"path": str(file),
					"status": "READY"
				})
		return sorted(nodes, key=lambda x: x["name"])
	
if __name__ == "__main__":
	# Local Test for the Sandbox
	scanner = NodeScanner()
	print("🔱 VEMBER-OS | SCANNING REGISTRY...")
	for node in scanner.scan():
		print(f"[{node['status']}] {node['name']}: {node['description']}")