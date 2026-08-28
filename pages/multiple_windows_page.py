from playwright.sync_api import Page, expect

from config import WINDOWS_URL
from pages.base_page import BasePage


class MultipleWindowsPage(BasePage):
    URL_PATH = WINDOWS_URL

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.click_here_link = page.get_by_role("link", name="Click Here")

    def open_new_window(self) -> Page:
        with self.page.expect_popup() as popup_info:
            self.click_here_link.click()

        return popup_info.value

    def verify_new_window_title(self, popup: Page) -> None:
        expect(popup).to_have_title("New Window")

    def open_new_page(self) -> Page:
        with self.page.context.expect_page() as new_page_info:
            self.click_here_link.click()

            new_page = new_page_info.value

            return new_page
