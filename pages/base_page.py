from playwright.sync_api import Page, expect


class BasePage:
    URL_PATH: str = ""

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        if not self.URL_PATH:
            raise NotImplementedError("URL_PATH має бути визначений в дочірньому класі")
        self.page.goto(self.URL_PATH, wait_until="domcontentloaded")

    def verify_url(self, expected_url: str) -> None:
        expect(self.page).to_have_url(expected_url)
