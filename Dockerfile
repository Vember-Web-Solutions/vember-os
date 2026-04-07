# 🔱 VEMBER-OS CORE IMAGE (v1.0.5 Patch)
# Optimized for UV and Rich-Live Telemetry.
FROM python:3.13-slim-bookworm

# Install essential system utilities only
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/* 

# Inject UV (The Speed-Demon Package Manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

WORKDIR /app 

# 🔱 Environment Hardening
ENV TERM=xterm-256color
ENV COLORTERM=truecolor
ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy 

# Cache-efficient dependency synchronization
COPY pyproject.toml uv.lock README.md ./ 
RUN uv sync --frozen 

# Deploy Application Source
COPY . . 

# Launch the Vember Kernel
CMD ["uv", "run", "python", "main.py"]