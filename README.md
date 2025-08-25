# ECSify

A CLI tool to simplify deployment of containers to AWS ECS.

## Project Structure

This is the scaffolding version showing the complete project structure:

```
ecsify/
├── __init__.py
├── __main__.py              # Entry point for python -m ecsify
├── cli.py                   # Click CLI entrypoint
├── models/                  # Pydantic data models
│   ├── __init__.py
│   ├── config.py           # Root configuration model
│   ├── task.py             # Task definition models
│   └── service.py          # Service definition models
├── parsers/                 # YAML parsing + validation
│   ├── __init__.py
│   ├── yaml_parser.py      # YAML file parsing
│   └── validator.py        # Configuration validation
├── aws/                     # AWS API clients
│   ├── __init__.py
│   ├── auth.py             # AWS credentials handling
│   └── ecs_client.py       # ECS service wrapper
├── deployment/              # Deployment orchestration
│   ├── __init__.py
│   ├── deployer.py         # Main deployment logic
│   └── dry_run.py          # Dry-run plan generation
├── utils/                   # Utilities
│   ├── __init__.py
│   ├── exceptions.py       # Custom exception classes
│   ├── logger.py           # Logging setup
│   └── merge.py            # Configuration merging
├── tests/                   # Test suite
├── examples/                # Example configurations
├── pyproject.toml           # Project configuration & dependencies
└── Makefile                 # Development commands
```

## Installation

### Prerequisites
- Python 3.9+
- pip (comes with Python)

### Install in Development Mode

```bash
# Clone the repository
git clone https://github.com/sanchezpaco/ecsify.git
cd ecsify

# Install in development mode
pip install -e .

# Install development dependencies (optional)
pip install -e ".[dev]"

# Or install individual development tools
pip install pytest pytest-cov black isort mypy types-PyYAML
```

### Alternative Installation Methods

#### Using uv (Modern Python Package Manager)

```bash
# Install uv first: https://docs.astral.sh/uv/
# Setup development environment
uv sync --dev
```

#### Using make (if available)

```bash
make dev  # Uses uv for setup
```

## Usage

## Usage

### Basic Commands

```bash
# Using python -m ecsify (recommended after pip install -e .)
python -m ecsify --help
python -m ecsify version
python -m ecsify apply
python -m ecsify apply --dry-run --env prod --service inventory

# Using uv (if installed with uv)
uv run ecsify apply
uv run ecsify apply --dry-run --env prod --service inventory

# JSON output for automation
python -m ecsify apply --json
```

### Available Commands

- `apply`: Deploy services to AWS ECS
  - `--dry-run`: Show deployment plan without executing
  - `--env`: Environment configuration to use (dev, staging, prod)
  - `--service`: Deploy only a specific service
  - `--file`: Custom configuration file to use
  - `--json`: Output in JSON format for automation
- `version`: Show ECSify version

### Development Commands

```bash
# Using make shortcuts (if make is available)
make hello         # Test CLI hello world
make cli           # Run CLI interactively
make test          # Run test suite
make test-coverage # Run tests with coverage
make lint          # Run linting (pylint + mypy)
make format        # Format code (black + isort)
make format-check  # Check code formatting
make clean         # Clean build artifacts

# Using pytest directly
python -m pytest                    # Run tests
python -m pytest -v                 # Run tests with verbose output
python -m pytest --cov=ecsify       # Run tests with coverage (requires pytest-cov)

# Using formatters directly
python -m black .                   # Format code
python -m isort .                   # Sort imports
python -m pylint ecsify             # Lint code
python -m mypy ecsify               # Type checking
```

## Status

This is a scaffolding version with basic CLI structure and hello world functionality.
The actual ECS deployment logic will be implemented in subsequent phases.

## Configuration

The project uses modern Python packaging standards with `pyproject.toml`:
- **Dependencies**: Runtime and development dependencies defined in `pyproject.toml`
- **Build system**: Uses `hatchling` as the build backend
- **Entry points**: Console script `ecsify` and module execution via `python -m ecsify`
- **Development tools**: Black, isort, pytest, mypy, pylint configured
- **Package metadata**: Version, description, authors, classifiers, URLs

### Key Configuration Sections

- `[project]`: Package metadata and dependencies
- `[project.scripts]`: Console script entry points
- `[project.optional-dependencies]`: Development dependencies
- `[tool.*]`: Tool-specific configurations (black, isort, pytest, etc.)

## Development Standards

- **Formatter**: Black (88 char line length)
- **Import sorting**: isort (black profile)
- **Linting**: pylint + mypy
- **Testing**: pytest with coverage >90%
- **Package manager**: uv (preferred) or pip
- **No comments in code**: Code explained by tests

## Development Phases

1. **Phase 1**: Core CLI (current - scaffolding complete)
2. **Phase 2**: Environment support & service selection
3. **Phase 3**: UX improvements
4. **Phase 4**: Advanced features

See ROADMAP.md for detailed implementation plan.