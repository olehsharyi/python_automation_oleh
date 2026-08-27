# Python Test Automation Framework
[![Playwright Tests](https://github.com/olehsharyi/python_automation_oleh/actions/workflows/test.yml/badge.svg)](https://github.com/olehsharyi/python_automation_oleh/actions/workflows/test.yml)

A modular, scalable test automation framework built with **Python**, **Pytest**, and **Playwright**. Designed following the **Page Object Model (POM)** pattern to ensure high maintainability, reliability, and clean code standards.

## 🚀 Key Features

* **UI Automation:** Powered by Playwright (Sync API) for fast, resilient cross-browser testing, including robust **iframe handling and nested content navigation** via frame locators.
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