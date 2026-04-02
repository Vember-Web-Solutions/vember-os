# 🔱 VEMBER-OS
**The Ultra-Flat, Node-Based Automation Hub**

![Python 3.13](https://img.shields.io/badge/python-3.13-blue?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker)
![E2EE](https://img.shields.io/badge/Security-E2EE_Encrypted-blueviolet?style=for-the-badge)
![Version](https://img.shields.io/badge/version-0.1.1a0-orange?style=for-the-badge)

Vember-OS is a lightweight, containerized operating environment designed to scan, manage, and execute Python-based automation nodes. Built with a focus on security and high-performance terminal interfaces, it provides a "Single Pane of Glass" for your automation scripts.

---

## 🏗️ Architecture Overview
Vember-OS utilizes an **Ultra-Flat Architecture** to minimize complexity and maximize speed within a Docker sandbox.

* **The Brain (`core.py`):** An AST-based (Abstract Syntax Tree) scanner that inspects automation nodes without executing them, ensuring safety and metadata accuracy.
* **The Face (`main.py`):** A high-performance Ncurses + Rich TUI (Terminal User Interface) providing a real-time dashboard for node management.
* **The Sandbox (`Docker`):** A fully isolated Debian-based environment using `uv` for lightning-fast dependency resolution.
* **The Vault (E2EE):** Future-proofed for End-to-End Encryption, ensuring all node-to-node communication and data persistence is cryptographically secured.

---

## 🕹️ Interface & Usage
The Vember Dashboard is divided into three functional zones:
1.  **Node Registry (Left):** Live list of all `.py` files detected in the `/ops` directory.
2.  **Node Inspector (Right):** Real-time metadata, docstring parsing, and path verification.
3.  **Command Bar (Bottom):** Hotkeys for navigation, rescanning, and execution.

### 🔱 How it Works
1.  **Drop a script** into the `ops/` folder.
2.  **Add a docstring** at the top (e.g., `"""Monitor CPU Usage"""`).
3.  **Boot the OS:** `docker compose run --rm vember-os`.
4.  **Navigate & Run:** Use the arrows to select and `ENTER` to execute.

---

## 📝 Feature Roadmap (TODO)
- [x] **Core Node Scanner:** AST-based metadata extraction.
- [x] **Docker Integration:** Python 3.13 sandbox with `uv` synchronization.
- [x] **Interactive Dashboard:** Ncurses-based TUI with sidebar navigation.
- [ ] **Execution Engine:** Subprocess-based node execution with UI suspension.
- [ ] **E2EE Layer:** Implementation of End-to-End Encryption for node data.
- [ ] **System Telemetry:** Live CPU/RAM monitoring in the dashboard header.
- [ ] **Secret Management:** Integration with `data/.env` for secure API handling.
- [ ] **Node Logs:** Dedicated view to see the output history of individual scripts.

---

## 🚀 Quick Start
```bash
# Clone the repository
git clone [https://github.com/your-repo/vember-os.git](https://github.com/your-repo/vember-os.git)

# Build the environment
docker compose build

# Launch the Hub
docker compose run --rm vember-os