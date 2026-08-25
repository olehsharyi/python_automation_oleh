from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class ContactPage(BasePage):
    URL_PATH = "https://practicetestautomation.com/contact/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.first_name_input = page.get_by_label("First")
        self.last_name_input = page.get_by_label("Last")
        self.email_input = page.get_by_role("textbox", name="Email *")
        self.message_input = page.get_by_label("Comment or Message")
        self.avatar = page.get_by_alt_text("Dmitry Shyshkin test automation instructor")
        self.title = page.get_by_role("heading", level=1)

    def get_title(self) -> str:
        """Повертає текст заголовка сторінки."""
        return self.title.inner_text()

    def verify_title(self, expected_title: str) -> None:
        """Перевірка заголовка сторінки з авто-очікуванням."""
        expect(self.title).to_have_text(expected_title)

    def check_avatar_is_visible(self) -> None:
        expect(self.avatar).to_be_visible()

    def check_avatar_is_loaded(self) -> None:
        is_loaded = self.avatar.evaluate("img => img.complete && img.naturalWidth > 0")
        assert is_loaded, "Картинка присутня в коді, але не завантажилася"

    def fill_form(
        self, first_name: str, last_name: str, email: str, message: str
    ) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.message_input.fill(message)

    def verify_form_values(
        self, first_name: str, last_name: str, email: str, message: str
    ) -> None:
        expect(self.first_name_input).to_have_value(first_name)
        expect(self.last_name_input).to_have_value(last_name)
        expect(self.email_input).to_have_value(email)
        expect(self.message_input).to_have_value(message)
