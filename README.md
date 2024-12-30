# SemantiCLI

### Semantic search in the command line.
look up strings using semantic search, see cosine similarity between strings.

## Installation

From PyPI:
```bash
pip install semanticli
```

From source:
```bash
pip install .
```

## Quick Usage

```bash
smnti --help
smnti "Search Me" -f text.txt
cat Alice.txt | smnti "Deck of cards"
smnti -cs 0.6 -c 200 -o 10 -s \n -n "Big Ship" -f treasure.txt
```
## Command-Line Options
```
-V or --version: Print current version.

--debug: Print debug logs.

-cs or --cos-sim: Cosine similarity greater or equal threshold for printing a match (between 0-1), default is 0.8.

-v or --invert-match: Print anything below the cosine similiarity threshold.

-n or --line: Print file name, line numbers, and similarity.

-s sep_str or --separator sep_str: Separation string to divide with, default is \n\n.

-c size or --chunk size: Chunk size number, might be larger if didn't encounter the separator, default is 4000.

-o size or --chunk-overlap size: Overlap size number between chunks, default is 200.

-lm or --list-models: List installed embedding models.

-m model or --model model: Use specified model for this search only, default is mixedbread-ai/mxbai-embed-large-v1.

-im model or --install-model model: Install specified embeddings model from hugging face.

-rm model or --remove-model model: Uninstall specified model.
```
note:

SemantiCLI is using ONNX runtime for model inference. it can only install models that have "model.onnx" in their repo at hugginface.
## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yairzaf/semanticli.git
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

<!-- ## Features

- Modular command system
- Logging with debug mode
- Unit tests
- No external dependencies
- Cross-platform binary building -->