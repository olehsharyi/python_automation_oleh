from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_login_page_mocked_response(
    page: Page,
    login_page: LoginPage,
    credentials: dict[str, str],
):
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

    page.route("**/logged-in-successfully**", handle_route)

    login_page.open()
    login_page.login(credentials["username"], credentials["password"])

    assert was_intercepted["value"] is True, "Помилка: запит не був перехоплений!"
    expect(page.get_by_role("heading", level=1)).to_have_text(mocked_title)