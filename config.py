from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

BASE_URL = "https://practicetestautomation.com"
LOGIN_URL = f"{BASE_URL}/practice-test-login/"
CONTACT_URL = f"{BASE_URL}/contact/"
SUCCESS_URL = f"{BASE_URL}/logged-in-successfully/"
AUTOMATE_NOW = "https://practice-automation.com/"
IFRAME_URL = f"{AUTOMATE_NOW}/iframe/"


def get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable '{name}' is not configured.")
    return value


def get_auth_storage_state_path() -> Path:
    worker_id = os.getenv("PYTEST_XDIST_WORKER", "main")
    if worker_id == "main":
        return BASE_DIR / "auth.json"
    return BASE_DIR / f"auth-{worker_id}.json"
