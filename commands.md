### 🛠️ Setup

Activate the virtual environment (Windows PowerShell):
```powershell
.venv\Scripts\Activate
```

Install dependencies:
```powershell
pip install -r requirements.txt
```

---

### 🚀 Running Tests

**Run all tests sequentially with Allure reporting:**
```powershell
pytest --alluredir=allure-results -v
```

**Run all tests in parallel (fast, using `pytest-xdist`):**
```powershell
pytest -n auto --alluredir=allure-results
```

**Run a specific test by file path and function name:**
```powershell
pytest tests/test_login.py::test_user_can_login --alluredir=allure-results
```

**Run a group of tests matching a keyword (`-k`):**
```powershell
pytest -k "login" --alluredir=allure-results
```

**Run tests by marker (e.g., regression):**
```powershell
pytest -m regression --alluredir=allure-results
```

**Run tests by marker, excluding specific ones:**
```powershell
pytest -m "regression and not slow" --alluredir=allure-results
```

**Run regression tests in parallel with Allure report generation:**
```powershell
pytest -m regression -n auto --alluredir=allure-results
```

---

### 📊 Reports & Code Quality

**View Allure report in browser:**
```powershell
allure serve allure-results
```

**Format code (Ruff):**
```powershell
ruff format .
```

**Check code for lint errors (Ruff):**
```powershell
ruff check .
```

**Check code and auto-fix minor issues (Ruff):**
```powershell
ruff check --fix .
```