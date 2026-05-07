# 🔱 VEMBER-OS: CONTAINER IMAGE
FROM python:3.13-slim-bookworm

# 🛠️ SYSTEM HARDENING & IDENTITY: Install the "Autonomous Toolkit"
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    openssh-client \
    ca-certificates \
    openssl \
    git \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update \
    && apt-get install -y gh \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/* # Inject UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ 

WORKDIR /app 

# 🔱 Environment Hardening
ENV TERM=xterm-256color
ENV COLORTERM=truecolor
ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy 
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

COPY pyproject.toml uv.lock README.md ./ 
RUN uv sync --frozen

COPY . . 

CMD ["uv", "run", "python", "main.py"]