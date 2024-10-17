# AI Hacker League Project Management System

## Installation and Setup

This project uses Poetry for dependency management and packaging. Follow these steps to set up and run the application:

### Prerequisites

- Python 3.8 or higher
- Poetry (https://python-poetry.org/)
- GitHub CLI (https://cli.github.com/)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/ai-hacker-league-pms.git
   cd ai-hacker-league-pms/src
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up environment variables:
   Create a `.env` file in the `src` directory with the following content:
   ```
   DATABASE_URL=sqlite:///./test.db
   GITHUB_CLI_PATH=/path/to/gh
   GITHUB_TOKEN=your_github_personal_access_token
   ```
   Replace `/path/to/gh` with the actual path to your GitHub CLI executable and `your_github_personal_access_token` with your GitHub personal access token.

### Running the Application

1. Activate the Poetry virtual environment:
   ```
   poetry shell
   ```

2. Run the FastAPI application:
   ```
   uvicorn main:app --reload
   ```

   The application will start and be available at `http://localhost:8000`.

3. Access the API documentation:
   Open your web browser and go to `http://localhost:8000/docs` to view the Swagger UI documentation for the API.

### Running Tests

To run the tests, use the following command:
```
poetry run pytest
```

### Development

For development, you can use the following commands:

- Format code:
  ```
  poetry run black .
  ```

- Check code style:
  ```
  poetry run flake8
  ```

- Run type checking:
  ```
  poetry run mypy .
  ```

## Project Structure

```
src/
├── api/
│   └── endpoints/
│       ├── issues.py
│       ├── projects.py
│       └── templates.py
├── crud/
│   ├── issue.py
│   ├── project.py
│   └── template.py
├── models/
│   ├── issue.py
│   ├── project.py
│   └── template.py
├── schemas/
│   ├── issue.py
│   ├── project.py
│   └── template.py
├── utils/
│   ├── github_cli.py
│   └── template_loader.py
├── config.py
├── database.py
├── main.py
└── README.md
```

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
