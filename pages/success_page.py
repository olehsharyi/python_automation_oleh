from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class SuccessPage(BasePage):
    URL_PATH = "https://practicetestautomation.com/logged-in-successfully/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = page.get_by_role("heading", level=1)
        self.logout_button = page.get_by_role("link", name="Log out")

    def verify_successful_login(self) -> None:
        expect(self.page).to_have_url(self.URL_PATH)
        expect(self.title).to_have_text("Logged In Successfully")
        expect(self.logout_button).to_be_visible()