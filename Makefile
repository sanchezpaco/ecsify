.PHONY: help install test test-coverage lint format format-check clean dev sync hello cli

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
