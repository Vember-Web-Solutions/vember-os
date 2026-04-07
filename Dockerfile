# 🔱 VEMBER-OS: CONTAINER IMAGE
# Defines the secure, Docker-orchestrated environment for the 
# Vember-OS node automation ecosystem.

FROM python:3.13-slim-bookworm

# 🛠️ SYSTEM HARDENING: Install the "Autonomous Toolkit"
# Adding ca-certificates for SSL trust and openssh-client for future autonomy
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    openssh-client \
    ca-certificates \
    openssl \
    git \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/* # Inject UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

WORKDIR /app 

# 🔱 Environment Hardening
ENV TERM=xterm-256color
ENV COLORTERM=truecolor
ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy 
# Ensure Python sees the system's certificate store
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

COPY pyproject.toml uv.lock README.md ./ 
RUN uv sync --frozen 

COPY . . 

CMD ["uv", "run", "python", "main.py"]