import allure
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.regression
@allure.epic("UI Automation")
@allure.feature("Network Interception")
@allure.story("Login Page Mocked Response")
@allure.title("Verify mocked response for login request")
def test_login_page_mocked_response(
    page: Page,
    login_page: LoginPage,
    credentials: dict[str, str],
) -> None:
    mocked_title = "MOCKED_ERROR_STATE"
    was_intercepted = {"value": False}

    def handle_route(route, request):
        if "logged-in-successfully" in request.url:
            was_intercepted["value"] = True
            route.fulfill(
                status=200,
                content_type="text/html",
                body=f"""
                <html>
                    <body>
                        <h1>{mocked_title}</h1>
                    </body>
                </html>
                """,
            )
            return

        route.continue_()

    with allure.step("Configure route interception"):
        page.route("**/logged-in-successfully**", handle_route)

    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Login with valid credentials"):
        login_page.login(
            credentials["username"],
            credentials["password"],
        )

    with allure.step("Verify request was intercepted"):
        assert was_intercepted["value"] is True, (
            "Error: login request was not intercepted!"
        )

    with allure.step("Verify mocked response is displayed"):
        expect(
            page.get_by_role("heading", level=1)
        ).to_have_text(mocked_title)

