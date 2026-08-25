import os
import pytest
from dotenv import load_dotenv

from pages.contact_page import ContactPage
from pages.login_page import LoginPage

load_dotenv(dotenv_path=".env")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield

    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        page.screenshot(path=f"screenshots/{request.node.name}.png")