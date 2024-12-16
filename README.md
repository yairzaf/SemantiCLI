# semanticli

A command line tool using Python's argparse.

## Installation

From PyPI:
```bash
pip install semanticli
```

From source:
```bash
pip install .
```

## Usage

```bash
semanticli greet Alice
semanticli greet Bob --count 3
semanticli version
semanticli --help
```

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/semanticli.git
cd semanticli
```

2. Set up development environment:
```bash
make dev
```

3. Activate the virtual environment:
```bash
# Linux/Mac:
source venv/bin/activate

# Windows:
.\venv\Scripts\activate
```

## Available Make Commands

- `make help` - Show available commands
- `make venv` - Create virtual environment
- `make install` - Install package and dependencies
- `make dev` - Set up development environment (venv + install)
- `make clean` - Remove virtual environment and build artifacts
- `make test` - Run tests
- `make lint` - Run linter checks
- `make format` - Format code using black
- `make binary-linux` - Create standalone Linux binary
- `make binary-windows` - Create standalone Windows binary (requires Wine on Linux/WSL)

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch from develop:
```bash
git checkout -b feature/amazing-feature develop
```

3. Set up development environment:
```bash
make dev
```

4. Make your changes and follow these guidelines:
   - Write meaningful commit messages following [Conventional Commits](https://www.conventionalcommits.org/)
   - Add tests for new functionality
   - Update documentation as needed
   - Follow the existing code style

5. Run tests and linting:
```bash
make test
make lint
```

6. Push to your fork:
```bash
git push origin feature/amazing-feature
```

7. Create a Pull Request to the `develop` branch

### Branch Naming Convention

- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `docs/*` - Documentation changes
- `refactor/*` - Code refactoring
- `release/*` - Release preparation

### Commit Message Format

```
feat: add new export command
fix: resolve argument parsing error
docs: update installation guide
test: add unit tests for export feature
refactor: restructure command handling
```

### After Pull Request Merge

Clean up your branches:
```bash
git checkout develop
git pull origin develop
git branch -d feature/amazing-feature
git push origin --delete feature/amazing-feature
```

## Building Binaries

Create standalone executable:

For Linux:
```bash
make binary-linux
# Binary will be in dist/semanticli
```

For Windows (from Linux/WSL):
```bash
# Install Wine if needed:
sudo apt-get install wine

make binary-windows
# Binary will be in dist/semanticli.exe
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Features

- Modular command system
- Logging with debug mode
- Unit tests
- No external dependencies
- Cross-platform binary building