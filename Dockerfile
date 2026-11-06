# ================================
# Level1: Env Builder
# ================================
FROM python:3.12-slim AS builder

# set environment var, not to write .pyc, not to buffer (to log)
ENV PYTHONDONTWRITEBYTECODE=1
	PYTHONUNBUFFERED=1
	UV_COMPILE_BYTECODE=1
	UV_LINK_MODE=copy

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# copy dependancies first with Docker buffer
COPY pyproject.toml uv.lock ./

# only install production environment dependancies, sync to system environment
# --frozen ensures to install by uv.lock, --no-dev ignores dev-dependancies
RUN uv sync --frozen --no-dev


# ================================
# Level2: Env Runner
# ================================
FROM python:3.12-slim AS runner

ENV PYTHONDONTWRITEBYTECODE=1
	PYTHONUNBUFFERED=1

WORKDIR /app

# create a common user, no root allowed
RUN useradd -m -u 1000 appuser

# copy venv and code from Builder without constructing tools like uv
COPY --from=builder /app/.venv /app/.venv
COPY --chown=appuser:appuser src/ ./src/

# add the bin dir of venv into PATH, so that we can run just with prompt
ENV PATH="/app/.venv/bin:$PATH"

# alter into common user
USER appuser

# startup the project
CMD ["python","src/myproject/main.py"]