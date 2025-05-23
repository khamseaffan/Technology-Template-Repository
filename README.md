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
## Testing
To run all of the test suite at once:  
```bash
pytest
   ```  
To run individual test files:  
```bash
pytest <path-to-specific-test-file>
   ```  
To run individual tests within a file:  
```bash
pytest <path-to-specific-test-file::name-of-individual-test>
   ```  

Note that to test individual tests you might have to set your PYTHONPATH correctly so Python can find local relative modules. For example (inside notifier_impl):  `PYTHONPATH=src pytest src/tests` runs tests

Additionally, when using local relative modules, you will need to add them to the python path of pytest so that they can be found as such: 

```toml
[tool.pytest.ini_options]
pythonpath = [
    "src/notifier_impl/src",
    "src/calculator/src",
    "src/logger/src"
]
```

## Linting 

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and code formatting. To run the linter:

```bash
ruff check .
```

To automatically fix issues:

```bash
ruff check . --fix
```

The configuration in `pyproject.toml` enforces strict code quality rules while ignoring specific cases where exceptions make sense. See the `[tool.ruff]` section in `pyproject.toml` for details.

## Internal Dependencies

In terms of specifying local relative dependencies, as per [this](https://github.com/astral-sh/uv/pull/640) pr, uv will automatically inject environment variables for you. 

uv add also supports it by adding `uv add --editable ./local-path/`; however, you must first build the dependencies to create a dist file.

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
