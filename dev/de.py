"""
================================================================================
🔱 VEMBER-OS: DOCKER_ENGINE CONTRACT PASSPORT
================================================================================
Family Stack:  DEVELOPER_CORE
Node Identity: DOCKER_REMEDIATION_ENGINE
Context Path:  /dev/docker.py

Handles manual container footprint polling and lifecycle build orchestration.
Authorized and signed under Vember OS decentralized system specifications.
================================================================================
"""

import docker
from docker import errors
import subprocess, os
import threading


class DockerEngine:
	"""🛠️ DOCKER_ENGINE: Unified lifecycle manager for Vember OS containers."""

	def __init__(self, target_container="vember_hub", image_name="vember-node"):
		self.target_container = target_container
		self.image_name = image_name

	def run_build_and_boot(self, controller):
		"""Unified background task: Build then Boot if offline."""
		def task():
			controller.status_msg = "⚡ BUILD: Compiling layers..."
			
			# 1. Build
			success = self._run_build_task()
			
			if success:
				controller.status_msg = "⚡ BUILD: Success. Checking status..."
				# 2. Boot (only if not already running)
				if not self.check_docker_online():
					controller.status_msg = "⚡ BOOT: Launching..."
					self._run_boot_task()
				controller.status_msg = "⚡ SYSTEM: Online (Stable)"
			else:
				controller.status_msg = "⚡ BUILD: Failed"
				
		threading.Thread(target=task, daemon=True).start()
		return True

	def _run_build_task(self):
		"""Internal: Silently execute docker compose build."""
		try:
			with open(os.devnull, "w") as devnull:
				subprocess.run(
					["docker", "compose", "build"],
					stdout=devnull,
					stderr=devnull,
					check=True,
				)
			return True
		except subprocess.CalledProcessError:
			return False

	def _run_boot_task(self):
		"""Internal: Boots the container using docker run."""
		try:
			# -d: Detached, --name: Identity for tracking
			subprocess.run(
				[
					"docker",
					"run",
					"-d",
					"--name",
					self.target_container,
					self.image_name,
				],
				stdout=subprocess.DEVNULL,
				stderr=subprocess.DEVNULL,
				check=True,
			)
			return True
		except subprocess.CalledProcessError:
			return False

	def get_container_size(self):
		"""🛡️ NEXUS_CORE: Queries container footprint with safety checks."""
		try:
			client = docker.from_env()
			container = client.containers.get(self.target_container)

			# 🔱 SAFETY CHECK: Ensure the container has an associated image
			if container.image is None:
				return "UNLINKED"

			# Use getattr for safer attribute access
			image_attrs = getattr(container.image, "attrs", {})
			size_bytes = image_attrs.get("Size", 0)

			return f"{round(size_bytes / (1024 * 1024), 1)} MB"

		except errors.NotFound:
			# 🔱 FIX: Now using the correctly imported errors module
			return "OFFLINE"
		except Exception:
			# Catch-all for other daemon issues
			return "ERROR"

	def check_docker_online(self) -> bool:
		"""Check if the target container is running."""
		try:
			# We use the target_container attribute initialized in __init__
			cmd = ["docker", "inspect", "-f", "{{.State.Running}}", self.target_container]
			result = subprocess.run(cmd, capture_output=True, text=True, check=False)
			return result.stdout.strip() == "true"
		except Exception:
			return False
