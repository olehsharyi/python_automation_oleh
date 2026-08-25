# tests/test_profile.py
import allure
import pytest
from playwright.sync_api import Page

from config import SUCCESS_URL
from pages.success_page import SuccessPage


@pytest.mark.smoke
@allure.epic("UI Automation")
@allure.feature("User Profile")
@allure.story("Session Restoration")
@allure.title("User is logged in automatically using storage state")
def test_user_is_already_logged_in(page: Page) -> None:
    """Test that verifies user session is restored via the stored auth state."""

    with allure.step("Navigate directly to the protected success page"):
        page.goto(SUCCESS_URL)

    with allure.step("Verify that 'Log out' button is visible"):
        logout_button = page.locator("a:has-text('Log out')")
        assert logout_button.is_visible(), (
            "User session was not restored, 'Log out' button is missing!"
        )

    with allure.step("Verify success header text"):
        success_page = SuccessPage(page)
        success_page.verify_successful_login()
