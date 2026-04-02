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
        """Returns a list of valid automation nodes."""
        nodes = []
        
        # Scan for .py files, respecting our Vember-OS privacy rules
        for file in self.ops_path.glob("*.py"):
            if not file.name.startswith(("private_", "__")):
                description = self.get_node_metadata(file)
                
                nodes.append({
                    "id": file.stem,
                    "display_name": file.stem.replace("_", " ").upper(),
                    "path": str(file),
                    "description": description,
                    "status": "READY"
                })
        
        # Sort alphabetically by display name
        return sorted(nodes, key=lambda x: x["display_name"])

if __name__ == "__main__":
    # Local Test for the Sandbox
    scanner = NodeScanner()
    print("🔱 VEMBER-OS | SCANNING REGISTRY...")
    for node in scanner.scan():
        print(f"[{node['status']}] {node['display_name']}: {node['description']}")