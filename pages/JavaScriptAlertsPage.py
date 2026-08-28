from collections.abc import Callable

from playwright.sync_api import Dialog, Locator, Page, expect

from config import ALLERT_URL
from pages.base_page import BasePage


class JavaScriptAlertsPage(BasePage):
    URL_PATH = ALLERT_URL

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.alert_button = page.get_by_role(
            "button",
            name="Click for JS Alert",
        )

        self.confirm_button = page.get_by_role(
            "button",
            name="Click for JS Confirm",
        )
        self.prompt_button = page.get_by_role(
            "button",
            name="Click for JS Prompt",
        )
        self.result = page.locator("#result")

    def accept_dialog(self, dialog: Dialog) -> None:
        dialog.accept()

    def dismiss_dialog(self, dialog: Dialog) -> None:
        dialog.dismiss()

    def send_text_to_prompt(self, dialog: Dialog, text: str) -> None:
        dialog.accept(text)

    def verify_alert_accepted(self) -> None:
        expect(self.result).to_have_text("You successfully clicked an alert")

    def verify_confirm_accepted(self) -> None:
        expect(self.result).to_have_text("You clicked: Ok")

    def verify_confirm_dismissed(self) -> None:
        expect(self.result).to_have_text("You clicked: Cancel")

    def verify_prompt_accepted(self, text: str) -> None:
        expect(self.result).to_have_text(f"You entered: {text}")

    def trigger_dialog(
        self,
        button: Locator,
        handler: Callable[..., None],
        *args: object,
    ) -> None:
        self.page.once(
            "dialog",
            lambda dialog: handler(dialog, *args),
        )
        button.click()
