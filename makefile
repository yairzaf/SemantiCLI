.PHONY: help venv install clean test lint format dev all

# Default target when just running 'make'
all: help

# Python executable to use
PYTHON = python3
VENV = venv
BIN = $(VENV)/bin/

help:
	@echo "Available commands:"
	@echo "  make venv       - Create virtual environment"
	@echo "  make install    - Install package and dependencies"
	@echo "  make dev        - Set up development environment (venv + install)"
	@echo "  make clean      - Remove virtual environment and build artifacts"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linter checks"
	@echo "  make format     - Format code using black"
	@echo "  make all        - Show this help message"

# Create virtual environment
venv:
	@echo "Creating virtual environment..."
	@$(PYTHON) -m venv $(VENV)
	@echo "Upgrading pip..."
	@$(BIN)pip install --upgrade pip

# Install package and dependencies
install: venv
	@echo "Installing development dependencies..."
	@$(BIN)pip install -r requirements-dev.txt
	@echo "Installing package in editable mode..."
	@$(BIN)pip install -e .

# Clean up generated files
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV)
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@rm -rf __pycache__/
	@rm -rf .pytest_cache/
	@rm -rf .coverage
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.pyd" -delete

# Run tests
test:
	@echo "Running tests..."
	@$(BIN)pytest

# Run linter
lint:
	@echo "Running flake8..."
	@$(BIN)flake8 src tests
	@echo "Running isort check..."
	@$(BIN)isort --check-only src tests

# Format code
format:
	@echo "Formatting code..."
	@$(BIN)black src tests
	@$(BIN)isort src tests

# Set up development environment
dev: clean install
	@echo "Development environment is ready!"
	@echo "Activate your virtual environment with:"
	@echo "  source $(VENV)/bin/activate  # Linux/Mac"
	@echo "  .\\$(VENV)\\Scripts\\activate  # Windows"

# Create Linux binary
binary-linux:
	@echo "Creating Linux binary..."
	@$(BIN)pyinstaller \
		--name $(PACKAGE_NAME) \
		--onefile \
		--clean \
		--strip \
		--add-data "src/$(PACKAGE_NAME)/*:$(PACKAGE_NAME)" \
		src/$(PACKAGE_NAME)/cli.py
	@echo "Binary created at dist/$(PACKAGE_NAME)"

# Create Windows binary (from Linux/WSL using Wine)
binary-windows:
	@echo "Creating Windows binary..."
	@echo "Checking if Wine is installed..."
	@which wine > /dev/null || (echo "Wine is required to build Windows binary on Linux" && exit 1)
	@echo "Installing Windows Python via Wine..."
	@$(BIN)pip install pyinstaller-cross-compilation
	@$(BIN)pyinstaller \
		--name $(PACKAGE_NAME) \
		--onefile \
		--clean \
		--strip \
		--target-platform win64 \
		--add-data "src/$(PACKAGE_NAME)/*;$(PACKAGE_NAME)" \
		src/$(PACKAGE_NAME)/cli.py
	@echo "Binary created at dist/$(PACKAGE_NAME).exe"