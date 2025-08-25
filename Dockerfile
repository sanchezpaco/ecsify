# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13

FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=1 \
  UV_PROJECT_ENVIRONMENT=/app/.venv \
  PATH="/app/.venv/bin:/root/.local/bin:${PATH}"

WORKDIR /app

RUN apt-get update \
  && apt-get install -y --no-install-recommends curl \
  && rm -rf /var/lib/apt/lists/*

RUN pip install uv

COPY pyproject.toml ./
COPY uv.lock ./
COPY README.md ./

RUN uv sync --frozen --no-dev

FROM base AS runtime

COPY ecsify/ ./ecsify/
COPY examples/ ./examples/

ENTRYPOINT ["python", "-m", "ecsify"]
CMD ["--help"]

FROM base AS test

COPY . .

RUN uv sync --extra dev

CMD ["pytest", "-q"]
