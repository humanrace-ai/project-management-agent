#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install Poetry if it's not already installed
if ! command_exists poetry; then
    echo "Poetry not found. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

# Ensure Poetry is in the PATH
if ! command_exists poetry; then
    echo "Poetry installation failed or not in PATH. Please install Poetry manually and try again."
    exit 1
fi

# Navigate to the project directory (assuming the script is in the root folder)
cd "$(dirname "$0")"

# Create pyproject.toml if it doesn't exist
if [ ! -f pyproject.toml ]; then
    echo "Creating pyproject.toml file..."
    cat << EOF > pyproject.toml
[tool.poetry]
name = "ai-hacker-league-pms"
version = "0.1.0"
description = "AI Hacker League Project Management System"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
fastapi = "^0.103.0"
uvicorn = {extras = ["standard"], version = "^0.23.0"}
sqlalchemy = "^2.0.0"
aiosqlite = "^0.19.0"
pydantic = "^2.0.0"
python-dotenv = "^1.0.0"
toml = "^0.10.2"

[tool.poetry.dev-dependencies]
pytest = "^7.0.0"
black = "^23.0.0"
mypy = "^1.0.0"
isort = "^5.0.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
EOF
    echo "pyproject.toml file created. Please update it with your project details."
fi

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat << EOF > .env
DATABASE_URL=sqlite+aiosqlite:///./project_manager.db
GITHUB_CLI_PATH=gh
GITHUB_TOKEN=your_github_personal_access_token
EOF
    echo "Please update the .env file with your GitHub personal access token."
fi

# Install project dependencies
echo "Installing project dependencies..."
poetry install

# Create necessary directories
mkdir -p src/api/endpoints src/models src/schemas src/crud src/utils templates

# Create empty __init__.py files
touch src/__init__.py src/api/__init__.py src/api/endpoints/__init__.py src/models/__init__.py src/schemas/__init__.py src/crud/__init__.py src/utils/__init__.py

# Create template files if they don't exist
for template in bug_report feature_request task; do
    if [ ! -f "templates/${template}.toml" ]; then
        echo "Creating ${template}.toml template..."
        touch "templates/${template}.toml"
    fi
done

# Activate the virtual environment and run the application
echo "Activating virtual environment and starting the FastAPI application..."
poetry run uvicorn src.main:app --reload

echo "Installation and setup complete. The FastAPI application should now be running."
