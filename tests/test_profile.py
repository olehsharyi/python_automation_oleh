# tests/test_profile.py
import allure
import pytest
from playwright.sync_api import Page


@pytest.mark.smoke
@allure.epic("UI Automation")
@allure.feature("User Profile")
@allure.story("Session Restoration")
@allure.title("User is logged in automatically using storage state")
def test_user_is_already_logged_in(page: Page) -> None:
    """Test that verifies user session is restored via auth.json,

    allowing direct access to protected pages without re-logging in.
    """

    # 1. Open the protected page directly (skipping the login form)
    with allure.step("Navigate directly to the protected success page"):
        page.goto("https://practicetestautomation.com/logged-in-successfully/")

    # 2. Verify that the user session is active (e.g., 'Log out' button is visible)
    with allure.step("Verify that 'Log out' button is visible"):
        logout_button = page.locator("a:has-text('Log out')")
        assert logout_button.is_visible(), (
            "User session was not restored, 'Log out' button is missing!"
        )

    # 3. Verify success header message
    with allure.step("Verify success header text"):
        success_message = page.locator("h1.post-title")
        assert success_message.text_content() == "Logged In Successfully"
