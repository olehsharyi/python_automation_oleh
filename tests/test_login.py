# tests/test_login.py

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.success_page import SuccessPage


@pytest.mark.smoke
def test_login_success(login_page: LoginPage, page: Page, credentials: dict) -> None:
    login_page.open()
    # Використовуємо дані з .env через фікстуру credentials
    login_page.login(credentials["username"], credentials["password"])

    success_page = SuccessPage(page)
    success_page.verify_successful_login()


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("student", "wrongpass", "Your password is invalid!"),
        ("wronguser", "Password123", "Your username is invalid!"),
    ],
)
def test_login_failure(
    login_page: LoginPage, username: str, password: str, expected_error: str
) -> None:
    login_page.open()
    login_page.login(username, password)
    login_page.verify_error_message(expected_error)