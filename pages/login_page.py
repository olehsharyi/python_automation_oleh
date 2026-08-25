from playwright.sync_api import Page, expect

from config import LOGIN_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL_PATH = LOGIN_URL

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.error_message = page.locator("#error")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def verify_error_message(self, expected_text: str) -> None:
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(expected_text)
