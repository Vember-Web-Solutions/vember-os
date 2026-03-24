"""
🔱 VEMBER-OS | NODE MANAGER
File: manager.py
Author: Vember-Web-Solutions
Description: Interfaces with the Docker SDK to monitor and manage 
            containerized resource groups.
"""

import docker
from typing import List, Dict, Any

class DockerManager:
    """
    Handles the 'Muscle' of Vember-OS.
    Translates Docker containers into Vember Nodes.
    """

    def __init__(self):
        try:
            self.client = docker.from_env()
        except Exception:
            self.client = None

    def get_node_status(self) -> List[Dict[str, Any]]:
        """
        Polls the local Docker daemon for container states.
        
        Returns:
            A list of dictionaries representing active/inactive nodes.
        """
        if not self.client:
            return [{"name": "Daemon", "state": "Offline"}]

        nodes = []
        # ARCHITECTURE NOTE: We only grab the first 5 containers for the MVP
        # to ensure the TUI remains performant.
        for container in self.client.containers.list(all=True)[:5]:
            nodes.append({
                "name": container.name,
                "state": container.status.upper()
            })
        return nodes