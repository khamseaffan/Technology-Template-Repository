# Python-Project-Template

## Description

This repository serves as a template for designing and developing projects in Python. It is ready to use and includes features for build management, unit testing, continuous integration, static analysis, code style adherence, and component specification.

## Requirements

- **Python 3.8 or higher**
- pytest
- ruff
- mypy
- coverage
- uv

## Project Setup

To set up the project environment:

1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <repo-name>
   ```
3. Install UV, the package manager for dependency management:
   For macOS/linux

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Alternatively, for brew installation: [brew install uv](https://formulae.brew.sh/formula/uv) is sufficient.

   For Windows

   ```bash
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

4. Install the project dependencies:
   ```bash
   uv sync
   ```

## Running Unit Tests

This project uses `pytest` for running unit tests. To run all tests, use:

```bash
pytest
```

````

To run a specific test file:

```bash
pytest tests/integration/test_calculator_logger.py
```

To run a single test function inside a file:

```bash
pytest tests/integration/test_calculator_logger.py::test_function_name
```

To check code coverage while running tests:

```bash
coverage run -m pytest
coverage report -m
```

## Using This Template for a New Project

To create a new project using this template, follow these steps:

1. **Clone the template repository**:

   ```bash
   git clone <repo-url> my-new-project
   cd my-new-project
   ```

2. **Remove the existing Git history** (optional, for a fresh start):

   ```bash
   rm -rf .git
   git init
   git add .
   git commit -m "Initial commit from template"
   ```

3. **Modify `pyproject.toml` and `README.md` to reflect your project details**.

4. **Install dependencies and start developing**:
   ```bash
   uv sync
   ```

## Project Structure

This project follows a modular structure, with each component acting as its own package.

```
src/
│── calculator/      # Handles mathematical operations
│   ├── __init__.py
│   ├── calculator.py
│   ├── pyproject.toml
│── logger/          # Handles logging operations
│   ├── __init__.py
│   ├── logger.py
│   ├── pyproject.toml
│── notifier/        # Handles notification-related tasks
│   ├── __init__.py
│   ├── notifier.py
│   ├── pyproject.toml
tests/
│── integration/     # Integration tests
│── e2e/            # End-to-end tests
```

Each component (`calculator`, `logger`, `notifier`) is **installable separately** using:

```bash
uv pip install -e src/calculator
uv pip install -e src/logger
uv pip install -e src/notifier
```
````

## Contributions

We welcome any and all contributions and will be using GitHub to track bugs, feature requests, and pull requests.  
By contributing, you agree that your contributions will be licensed under the project's license.

## Bug Reports and Feature Requests

Use the provided templates to report any bugs and request new features. Please follow the templates accurately to help us understand and more efficiently address your issue.

## Pull Requests

When submitting a pull request:

- Use the pull request template provided in the repository and follow its instructions.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Additional Information

- This project uses CircleCI for continuous integration, which automatically runs tests and checks code formatting with ruff.
- The `.gitignore` file is configured to ignore Python-specific files and directories, such as `__pycache__` and the `venv` directory.
