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
