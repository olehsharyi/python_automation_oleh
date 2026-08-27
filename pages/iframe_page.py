from playwright.sync_api import Page, expect

from config import IFRAME_URL
from pages.base_page import BasePage


class IFramePage(BasePage):
    URL_PATH = IFRAME_URL

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.iframe_1 = page.frame_locator("#iframe-1")

    def click_link(self, link_name: str) -> None:
        link = self.iframe_1.get_by_role("link", name=link_name, exact=True)
        link.scroll_into_view_if_needed()
        link.click()

    def verify_heading(self, expected_title: str, level: int = 1) -> None:
        heading = self.iframe_1.get_by_role("heading", level=level, name=expected_title)
        heading.scroll_into_view_if_needed()
        expect(heading).to_be_visible()
        expect(heading).to_have_text(expected_title)
