1. Create/Ensure Virtual Environment:
    - `uv venv  # Creates .venv if it doesn't exist`
2. Activate the Environment
    - `source .venv/bin/activate`
3. Sync all Dependencies (this will Install all project dependencies, including workspace members and development/test dependencies, into the activated environment.)
    - `uv sync --all-extras --all-groups --all-packages`
    > This command reads the root pyproject.toml, finds the workspace members, reads their pyproject.toml files (including the { workspace = true } dependencies), resolves everything, and installs them correctly into .venv
4. Run Pytest:
    `pytest .`