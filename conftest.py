import os
import pytest
from dotenv import load_dotenv

from pages.contact_page import ContactPage
from pages.login_page import LoginPage

from playwright.sync_api import Playwright

load_dotenv(dotenv_path=".env")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    """Configure global browser context settings (viewport and storage state)."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "storage_state": "auth.json",
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": True,
        "slow_mo": 500,
    }


# --- Фікстури сторінок ---

@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def contact_page(page) -> ContactPage:
    return ContactPage(page)


# --- Допоміжні фікстури ---

@pytest.fixture(autouse=True)
def log_test_name(request):
    print(f"\n🚀 Починаємо: {request.node.name}")
    yield
    print(f"✅ Завершено: {request.node.name}")


@pytest.fixture(scope="session")
def credentials() -> dict:
    username = os.getenv("APP_USERNAME")
    password = os.getenv("APP_PASSWORD")

    assert username, "APP_USERNAME не знайдено у .env"
    assert password, "APP_PASSWORD не знайдено у .env"

    return {
        "username": username,
        "password": password
    }


# --- Скріншоти при падінні ---

import allure
import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Зберігаємо результат тесту в item (для інших фікстур)
    setattr(item, "rep_" + rep.when, rep)

    # Якщо тест впав під час виконання — додаємо скріншот в Allure
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture(scope="session", autouse=True)
def create_storage_state(playwright: Playwright, credentials: dict[str, str]) -> None:
    """Fixture to generate and save storage state (auth.json) once per test session."""
    auth_file_path = "auth.json"

    # If the auth.json file already exists, we can skip re-logging in every time
    if os.path.exists(auth_file_path):
        return  # ← Змінили yield на return

    # Launch the browser to create a session
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Use your LoginPage object
    login_page = LoginPage(page)
    login_page.open()

    # Credentials are taken from the credentials fixture
    login_page.login(credentials["username"], credentials["password"])

    # Wait for a successful redirection to the secure page
    page.wait_for_url("**/logged-in-successfully/")

    # Save the session state into the auth.json file
    page.context.storage_state(path=auth_file_path)
    browser.close()
