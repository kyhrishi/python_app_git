# Python App

This is a simple Python application with a `User` class using Pydantic and unit tests with Pytest.

## Features
- User model with name, email, and userid fields
- Email validation using Pydantic
- Unit tests for the User class

## Setup
1. Create a virtual environment:
   ```powershell
   python -m venv myenv
   .\myenv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Running Tests
To run the unit tests:
```powershell
pytest
```

## Linting
To check code style with flake8:
```powershell
flake8
```

## Coverage
To check test coverage:
```powershell
coverage run -m pytest
coverage report
```
