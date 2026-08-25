# Python Test Automation Framework
[![Playwright Tests](https://github.com/olehsharyi/python_automation_oleh/actions/workflows/test.yml/badge.svg)](https://github.com/olehsharyi/python_automation_oleh/actions/workflows/test.yml)

A modular, scalable test automation framework built with **Python**, **Pytest**, and **Playwright**. Designed following the **Page Object Model (POM)** pattern to ensure high maintainability, reliability, and clean code standards.

## 🚀 Key Features

* **UI Automation:** Powered by Playwright (Sync API) for fast, resilient cross-browser testing.
* **API Automation:** *(Planned / In Progress)* Integration for REST API testing using Pytest and HTTP clients.
* **Design Pattern:** Strict Page Object Model (POM) architecture.
* **Data Management & Session Handling:**
  * Strongly-typed test data models using Python `dataclasses`.
  * **Session Storage State (`auth.json`):** Creates a fresh authenticated browser state once per test session and reuses it for protected tests.
* **Configuration:** Environment variable management via `python-dotenv`.
* **Reporting & Diagnostics:**
  * Automated screenshot capture on test failure and detailed pytest execution logging.
  * **Allure Reports:** Integrated reporting tool for rich, visual test results and step-by-step execution details.
* **Parallel Execution:** `pytest-xdist` for faster test execution.
* **Code Quality:** `ruff` for linting and formatting checks.
* **CI/CD:** GitHub Actions runs linting, formatting checks, and the automated test suite on pushes and pull requests.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Test Runner:** `pytest` (+ `pytest-xdist` for parallel execution)
* **Automation Tools:** `playwright`
* **Reporting:** `allure-pytest`
* **Utilities:** `python-dotenv`
* **Code Quality & Formatting:** `ruff`
* **CI/CD:** GitHub Actions

---

## ⚙️ How to Run Tests

### 1. Set up the virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
playwright install
```

### 3. Run tests

Run the complete test suite:

```powershell
pytest
```

Run tests in parallel:

```powershell
pytest -n auto
```

Run only smoke tests:

```powershell
pytest -m smoke
```

### 4. Generate Allure results

```powershell
pytest --alluredir=allure-results
```

Open the report locally:

```powershell
allure serve allure-results
```

### 5. Run code quality checks

Check linting:

```powershell
ruff check .
```

Check formatting without changing files:

```powershell
ruff format --check .
```

Format the project automatically:

```powershell
ruff format .
```

## 🔄 CI/CD

GitHub Actions runs automatically on pushes and pull requests to `main` and `master`.

The pipeline:

1. Installs Python dependencies.
2. Installs Playwright browsers.
3. Runs Ruff linting and formatting checks.
4. Creates `.env` from GitHub Secrets.
5. Runs the test suite in parallel.
6. Uploads `allure-results` as a workflow artifact, including when tests fail.

Authentication credentials are stored in GitHub Actions Secrets and are not committed to the repository.
