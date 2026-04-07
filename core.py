"""
🔱 VEMBER-OS NODE REGISTRY (v1.0.5 Patch)
Handles discovery, metadata extraction, and node state for the Vember-OS ecosystem.
Optimized with AST parsing for safety and mtime-caching for high-speed UI performance.
"""

import pathlib
import ast

class NodeScanner:
    def __init__(self, nodes_dir="nodes"):
        """
        Initializes the scanner with a target directory.
        :param nodes_dir: The directory containing .py node files.
        """
        self.nodes_path = pathlib.Path(nodes_dir)
        # Ensure the directory exists in the environment
        self.nodes_path.mkdir(parents=True, exist_ok=True)
        
        # 🔱 Performance Cache
        self._cache = []
        self._last_mtime = 0

    def get_node_metadata(self, file_path):
        """
        Uses Abstract Syntax Tree (AST) to extract docstrings without executing code.
        This is significantly safer than importing the file.
        """
        try:
            content = file_path.read_text(encoding="utf-8")
            tree = ast.parse(content)
            return ast.get_docstring(tree) or "No description provided."
        except Exception:
            return "Error: Metadata parsing failed."

    def scan(self, force=False):
        """
        Scans the ops directory for Python nodes.
        Uses mtime-based caching to avoid unnecessary disk I/O in the render loop.
        """
        try:
            current_mtime = self.nodes_path.stat().st_mtime
        except FileNotFoundError:
            return []

        # Return cached nodes if directory hasn't changed (unless forced)
        if not force and current_mtime <= self._last_mtime and self._cache:
            return self._cache

        nodes = []
        # Modern pathlib globbing (ignoring private/system files)
        for file in self.nodes_path.glob("*.py"):
            if file.name.startswith(("_", "private_")):
                continue
                
            raw_doc = self.get_node_metadata(file)
            
            # 🔱 Metadata Split Logic
            # Syntax: "Display Name | Detailed Description"
            if "|" in raw_doc:
                name_part, desc_part = raw_doc.split("|", 1)
            else:
                # Fallback: Use capitalized filename if pipe is missing
                name_part = file.stem.replace("_", " ").upper()
                desc_part = raw_doc

            nodes.append({
                "id": file.stem,
                "name": name_part.strip(),
                "description": desc_part.strip(),
                "path": str(file),
                "status": "READY"
            })

        # Sort alphabetically for consistent UI navigation
        self._cache = sorted(nodes, key=lambda x: x["name"])
        self._last_mtime = current_mtime
        return self._cache

if __name__ == "__main__":
    # Internal Registry Audit
    scanner = NodeScanner()
    print("🔱 VEMBER-OS | REGISTRY AUDIT")
    for node in scanner.scan():
        print(f"  [{node['status']}] {node['name']} -> {node['id']}")