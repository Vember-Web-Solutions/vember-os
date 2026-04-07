"""
🔱 VEMBER-OS: NODE SCANNER
Metadata ingestion engine. Performs AST-based analysis of node scripts 
to extract descriptions, controls, and contextual navigation data.
"""

import ast
import os
import re

class NodeScanner:
	def scan(self, directory="nodes"):
		nodes = []
		if not os.path.exists(directory): return nodes

		for file in os.listdir(directory):
			if file.endswith(".py"):
				path = os.path.join(directory, file)
				metadata = self._get_node_metadata(path)
				
				# 🔱 Extract Node-Specific Controls for the Contextual Footer
				nodes.append({
					"id": file.replace(".py", ""),
					"name": metadata.get("Title", file.replace(".py", "")),
					"description": metadata.get("Description", "No description."),
					"path": path,
					"controls": metadata.get("Controls", {"ESC": "BACK"}) # Default fallback
				})
		return nodes

	def _get_node_metadata(self, path):
		"""Peeks at the file to extract Title, Description, and Control Maps."""
		try:
			with open(path, "r", encoding="utf-8") as f:
				content = f.read()
				tree = ast.parse(content)
				docstring = ast.get_docstring(tree) or ""
				
				metadata = {"Description": "No data.", "Controls": {"ESC": "BACK"}}
				
				for line in docstring.split("\n"):
					if ":" in line:
						key, value = line.split(":", 1)
						metadata[key.strip()] = value.strip()
				
				# 🔱 Advanced: Search for a 'NODE_CONTROLS' dict in the code itself
				control_match = re.search(r"NODE_CONTROLS\s*=\s*({.*?})", content, re.DOTALL)
				if control_match:
					metadata["Controls"] = ast.literal_eval(control_match.group(1))
					
				return metadata
		except Exception:
			return {}