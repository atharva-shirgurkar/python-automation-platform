# Python Automation Platform

## Overview

This repository contains Python-based automation test suites developed using **PyTest**.

The current implementation includes a basic REST API testing framework using **HTTPX**. It uses reusable PyTest fixtures to initialize and manage API clients.

The framework supports:
- Configuration-driven API testing.
- Reusable HTTPX client initialization.
- Configurable base URL, request timeout, and HTTP headers.
- Automatic client cleanup through PyTest fixtures.
- Positive and negative API test scenarios.

Currently, the framework uses the JSONPlaceholder REST API for testing.

## Technology Stack

- **Python** — Programming language
- **PyTest** — Test framework and fixture management
- **HTTPX** — HTTP client for API requests
- **JSON** — Test configuration storage
- **Git** — Version control

## Prerequisites

Before executing the tests, ensure you have:

- Python 3 installed
- pip available
- Git installed

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/atharva-shirgurkar/python-automation-platform.git
```

**2. Navigate to the project directory**

```bash
cd python-automation-platform
```

**3. Create a virtual environment**

```bash
python3 -m venv .venv
```

**4. Activate the virtual environment**

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

**5. Install the dependencies**

```bash
python -m pip install -r requirements.txt
```

Run this command from the directory containing `requirements.txt`. Adjust the path if necessary.

## Configuration

The framework uses `test_config.json` to manage API configuration.

Example configuration:

```json
{
  "base_url": "https://jsonplaceholder.typicode.com",
  "timeout_seconds": 10,
  "headers": {
    "Accept": "application/json"
  }
}
```

Configuration parameters:

| Parameter | Description |
|---|---|
| `base_url` | Base URL of the application under test |
| `timeout_seconds` | HTTP request timeout in seconds |
| `headers` | Default HTTP headers sent with requests |

The configuration is loaded using the `test_config` fixture in `conftest.py`.

## Framework Structure

The current framework uses:

- **`conftest.py`** — Shared PyTest fixtures for configuration loading and HTTPX client management.
- **`config/test_config.json`** — API configuration including base URL, timeout, and headers.
- **`test_basic_api.py`** — Positive and negative REST API tests.
- **`requirements.txt`** — Python dependencies.
- **`pytest.ini`** — PyTest configuration, where applicable.

## Running Tests

Navigate to the repository root.

**Execute all discovered tests:**

```bash
python -m pytest -v
```

**Execute the API test module:**

```bash
python -m pytest API_Test_Framework/test_basic_api.py -v
```

**Display print statements and logs during execution:**

```bash
python -m pytest -v -s
```

## Current Test Coverage

The initial implementation includes:

| Test scenario | Expected HTTP status |
|---|---|
| Retrieve an existing post | 200 OK |
| Retrieve a nonexistent post | 404 Not Found |

API used: https://jsonplaceholder.typicode.com

## Planned Enhancements

Future development may include:

- Reusable HTTP request handling.
- Data-driven testing with PyTest parametrization.
- Environment-specific configuration.
- Response schema validation.
- GitHub Actions CI integration.
- Docker-based test execution.
- API and UI testing across multiple applications.

## Project Status

**Initial implementation:** Basic API tests and reusable HTTPX fixture implemented.

This project is being developed incrementally to demonstrate Python automation framework design, API testing, and integration testing skills.