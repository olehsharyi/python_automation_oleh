# Python Test Automation Framework

A modular, scalable test automation framework built with **Python**, **Pytest**, and **Playwright**. Designed following the **Page Object Model (POM)** pattern to ensure high maintainability, reliability, and clean code standards.

## 🚀 Key Features

* **UI Automation:** Powered by Playwright (Sync API) for fast, resilient cross-browser testing.
* **API Automation:** *(Planned / In Progress)* Integration for REST API testing using Pytest and HTTP clients.
* **Design Pattern:** Strict Page Object Model (POM) architecture.
* **Data Management & Session Handling:** 
  * Strongly-typed test data models using Python `dataclasses`.
  * **Session Storage State (`auth.json`):** Optimizes test execution by caching user sessions, automatically logging in once per session and restoring the state for protected pages, while safely isolating login tests via custom fixture scopes (`scope="function"`).
* **Configuration:** Environment variable management via `python-dotenv`.
* **Reporting & Diagnostics:** 
  * Automated screenshot capture on test failure and detailed pytest execution logging.
  * **Allure Reports:** Integrated reporting tool for rich, visual test results and step-by-step execution details.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Test Runner:** `pytest` (+ `pytest-xdist` for parallel execution)
* **Automation Tools:** `playwright`
* **Reporting:** `allure-pytest`
* **Utilities:** `python-dotenv`
* **Code Quality & Formatting:** `ruff` (linter and code formatter)

---

## ⚙️ How to Run Tests

1. **Set up the virtual environment and install dependencies:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate
   pip install -r requirements.txt