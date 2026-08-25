# tests/test_login.py
import allure
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.success_page import SuccessPage


@pytest.mark.smoke
@allure.epic("UI Automation")
@allure.feature("Authentication")
@allure.story("Successful Login")
@allure.title("Successful login with valid credentials")
def test_login_success(login_page: LoginPage, page: Page, credentials: dict) -> None:
    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Enter credentials from .env and click login"):
        # Use credentials from .env via the fixture
        login_page.login(credentials["username"], credentials["password"])
    with allure.step("Verify successful login and redirection"):
        success_page = SuccessPage(page)
        success_page.verify_successful_login()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("student", "wrongpass", "Your password is invalid!"),
        ("wronguser", "Password123", "Your username is invalid!"),
    ],
)
@allure.epic("UI Automation")
@allure.feature("Authentication")
@allure.story("Unsuccessful Login")
@allure.title("Unsuccessful login for user: {username}")
def test_login_failure(
    login_page: LoginPage, username: str, password: str, expected_error: str
) -> None:
    with allure.step("Open login page"):
        login_page.open()

    with allure.step(f"Attempt to login with username '{username}'"):
        login_page.login(username, password)

    with allure.step(f"Verify error message appears: '{expected_error}'"):
        login_page.verify_error_message(expected_error)