# Use the latest Python 3.13 on Debian Bookworm
FROM python:3.13-slim-bookworm

# Install Ncurses and essential system libs for the TUI
RUN apt-get update && apt-get install -y \
    libncurses5-dev \
    libncursesw5-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install UV (your speed-demon package manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Enable colors for the Vember-OS UI
ENV TERM=xterm-256color
ENV PYTHONUNBUFFERED=1

# Copy & Sync (Tracking the lockfile for the "Iron Triangle")
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen

COPY . .

# Launch the Vember Kernel
CMD ["uv", "run", "python", "main.py"]