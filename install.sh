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

# Install project dependencies
echo "Installing project dependencies..."
poetry install

# Activate the virtual environment
echo "Activating virtual environment..."
poetry shell <<EOF

# Run the FastAPI application
echo "Starting the FastAPI application..."
cd src
uvicorn main:app --reload

EOF

echo "Installation and setup complete. The FastAPI application should now be running."
