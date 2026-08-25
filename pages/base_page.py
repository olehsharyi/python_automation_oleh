from playwright.sync_api import Page


class BasePage:
    URL_PATH: str = ""

    def __init__(self, page: Page) -> None:
        self.page = page

    # Краще — якщо URL_PATH порожній, це помилка конфігурації
    def open(self) -> None:
        if not self.URL_PATH:
            raise NotImplementedError("URL_PATH має бути визначений в дочірньому класі")
        self.page.goto(self.URL_PATH)