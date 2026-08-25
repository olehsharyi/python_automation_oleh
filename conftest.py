import os

import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright

from pages.contact_page import ContactPage
from pages.login_page import LoginPage

load_dotenv(dotenv_path=".env")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    """Configure global browser context settings."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "storage_state": "auth.json",
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict) -> dict:
    """Configure browser launch settings for test execution."""
    return {
        **browser_type_launch_args,
        "headless": True,
    }


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def contact_page(page) -> ContactPage:
    return ContactPage(page)


@pytest.fixture(autouse=True)
def log_test_name(request):
    print(f"\n🚀 Починаємо: {request.node.name}")
    yield
    print(f"✅ Завершено: {request.node.name}")


@pytest.fixture(scope="session")
def credentials() -> dict[str, str]:
    username = os.getenv("APP_USERNAME")
    password = os.getenv("APP_PASSWORD")

    assert username, "APP_USERNAME не знайдено у .env"
    assert password, "APP_PASSWORD не знайдено у .env"

    return {"username": username, "password": password}


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )


@pytest.fixture(scope="session", autouse=True)
def create_storage_state(playwright: Playwright, credentials: dict[str, str]) -> None:
    """Create a fresh authenticated storage state for each test session."""
    auth_file_path = "auth.json"

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(credentials["username"], credentials["password"])
    page.wait_for_url("**/logged-in-successfully/")

    context.storage_state(path=auth_file_path)
    browser.close()
