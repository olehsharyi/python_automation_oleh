# tests/test_login.py
import allure
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.success_page import SuccessPage


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args: dict) -> dict:
    """Override global storage state for login tests

    to start with a clean browser session.
    """
    return {**browser_context_args, "storage_state": None}


@pytest.mark.smoke
@allure.epic("UI Automation")
@allure.feature("Authentication")
@allure.story("Successful Login")
@allure.title("Successful login with valid credentials")
def test_login_success(
    login_page: LoginPage,
    page: Page,
    credentials: dict,
) -> None:
    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Login with valid credentials"):
        login_page.login(
            credentials["username"],
            credentials["password"],
        )

    with allure.step("Verify successful login"):
        success_page = SuccessPage(page)
        success_page.verify_successful_login()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "student",
            "wrongpass",
            "Your password is invalid!",
        ),
        (
            "wronguser",
            "Password123",
            "Your username is invalid!",
        ),
        (
            "wronguser",
            "wrongpass",
            "Your username is invalid!",
        ),
    ],
)
@pytest.mark.smoke
@allure.epic("UI Automation")
@allure.feature("Authentication")
@allure.story("Unsuccessful Login")
@allure.title("Login fails with invalid credentials: {username}")
def test_login_with_invalid_credentials(
    login_page: LoginPage,
    username: str,
    password: str,
    expected_error: str,
) -> None:
    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Attempt login with invalid credentials"):
        login_page.login(username, password)

    with allure.step("Verify error message"):
        login_page.verify_error_message(expected_error)


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "",
            "Password123",
            "Your username is invalid!",
        ),
        (
            "student",
            "",
            "Your password is invalid!",
        ),
        (
            "",
            "",
            "Your username is invalid!",
        ),
    ],
)
@pytest.mark.smoke
@allure.epic("UI Automation")
@allure.feature("Authentication")
@allure.story("Login Validation")
@allure.title("Login validation: username='{username}', password='{password}'")
def test_login_validation(
    login_page: LoginPage,
    username: str,
    password: str,
    expected_error: str,
) -> None:
    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Submit login form"):
        login_page.login(username, password)

    with allure.step("Verify validation error"):
        login_page.verify_error_message(expected_error)
