.PHONY: help install test test-coverage lint format format-check clean dev sync hello cli docker-build docker-build-test docker-run docker-run-mount docker-test docker-sh docker-clean

# Docker settings
IMAGE ?= ecsify
TAG ?= latest
PYTHON_VERSION ?= 3.13
DOCKER_BUILD_ARGS = --build-arg PYTHON_VERSION=$(PYTHON_VERSION)

help:
	@echo "ECSify Development Commands (using uv)"
	@echo "====================================="
	@echo "sync        Sync dependencies with uv"
	@echo "install     Install package in development mode"
	@echo "test        Run test suite"
	@echo "lint        Run linting checks (pylint + mypy)"
	@echo "format      Format code with black and isort"
	@echo "format-check Check if code is formatted correctly"
	@echo "clean       Clean up build artifacts"
	@echo "dev         Setup development environment with uv"
	@echo "hello       Test ECSify CLI hello world"
	@echo "cli         Run ECSify CLI interactively"
	@echo ""
	@echo "Docker Commands"
	@echo "---------------"
	@echo "docker-build        Build runtime image (IMAGE=$(IMAGE) TAG=$(TAG))"
	@echo "docker-build-test   Build test image (pytest)"
	@echo "docker-run          Run CLI in container (use ARGS='--help' or 'apply --dry-run')"
	@echo "docker-run-mount    Run CLI mounting current dir to /app (dev)"
	@echo "docker-test         Run pytest in container"
	@echo "docker-sh           Open shell in runtime image"
	@echo "docker-clean        Remove built images"

sync:
	uv sync

install: sync
	uv pip install -e .

test:
	@echo "Running tests..."
	uv run pytest tests/ -v

test-file:
	@echo "Usage: make test-file SPEC=tests/test_cli.py"
	uv run pytest $(SPEC) -v

test-coverage:
	@echo "Running tests with coverage..."
	uv run pytest --cov=ecsify --cov-report=html --cov-report=term

lint:
	@echo "Running linting checks..."
	uv run pylint ecsify/
	uv run mypy ecsify/ --ignore-missing-imports

format:
	@echo "Formatting code..."
	uv run black ecsify/ tests/ --line-length=88
	uv run isort ecsify/ tests/

format-check:
	@echo "Checking code format..."
	uv run black --check ecsify/ tests/ --line-length=88
	uv run isort --check-only ecsify/ tests/

clean:
	@echo "Cleaning up..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

dev:
	@echo "Setting up development environment with uv..."
	uv sync --dev
	@echo "Development environment ready!"

hello:
	@echo "Testing ECSify CLI..."
	uv run python -m ecsify.cli apply --dry-run --env dev --service inventory

cli:
	uv run python -m ecsify.cli

docker-build:
	docker build -f Dockerfile $(DOCKER_BUILD_ARGS) --target runtime -t $(IMAGE):$(TAG) .

docker-build-test:
	docker build -f Dockerfile $(DOCKER_BUILD_ARGS) --target test -t $(IMAGE)-tests:$(TAG) .

docker-run: docker-build
	docker run --rm $(IMAGE):$(TAG) $(ARGS)

docker-run-mount: docker-build
	docker run --rm -it -v $(PWD):/app $(IMAGE):$(TAG) $(ARGS)

docker-test: docker-build-test
	docker run --rm $(IMAGE)-tests:$(TAG)

console: docker-build
	docker run --rm --entrypoint /bin/bash -it $(IMAGE)-tests:$(TAG)

docker-clean:
	- docker rmi -f $(IMAGE):$(TAG) 2>/dev/null || true
	- docker rmi -f $(IMAGE)-tests:$(TAG) 2>/dev/null || true
