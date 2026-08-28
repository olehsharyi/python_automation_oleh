# tests/test_profile.py
import allure

from pages import JavaScriptAlertsPage


def test_accept_js_alert_with_ok(
    java_script_alerts_page: JavaScriptAlertsPage,
) -> None:
    """Test that accepts a JavaScript alert by clicking 'OK'."""

    with allure.step("Navigate to the JavaScript Alerts page"):
        java_script_alerts_page.open()

    with allure.step("Trigger JS Alert and accept it"):
        java_script_alerts_page.trigger_dialog(
            java_script_alerts_page.alert_button,
            java_script_alerts_page.accept_dialog,
        )

    with allure.step("Verify that the alert was accepted successfully"):
        java_script_alerts_page.verify_alert_accepted()


def test_dismiss_confirm_dialog(
    java_script_alerts_page: JavaScriptAlertsPage,
) -> None:
    """Test that dismisses a JavaScript alert by clicking 'Cancel'."""

    with allure.step("Navigate to the JavaScript Alerts page"):
        java_script_alerts_page.open()

    with allure.step("Trigger confirm dialog and dismiss it"):
        java_script_alerts_page.trigger_dialog(
            java_script_alerts_page.confirm_button,
            java_script_alerts_page.dismiss_dialog,
        )

    with allure.step("Verify that the alert was dismissed successfully"):
        java_script_alerts_page.verify_confirm_dismissed()


def test_accept_confirm_dialog(
    java_script_alerts_page: JavaScriptAlertsPage,
) -> None:
    """Test that accepts a JavaScript alert by clicking 'OK'."""

    with allure.step("Navigate to the JavaScript Alerts page"):
        java_script_alerts_page.open()

    with allure.step("Trigger confirm dialog and accept it"):
        java_script_alerts_page.trigger_dialog(
            java_script_alerts_page.confirm_button,
            java_script_alerts_page.accept_dialog,
        )

    with allure.step("Verify that the alert was accepted successfully"):
        java_script_alerts_page.verify_confirm_accepted()


def test_send_text_to_prompt_dialog(
    java_script_alerts_page: JavaScriptAlertsPage,
) -> None:
    """Test that sends text to a JavaScript prompt dialog and accepts it."""

    with allure.step("Navigate to the JavaScript Alerts page"):
        java_script_alerts_page.open()

    with allure.step("Trigger prompt dialog, send text, and accept it"):
        java_script_alerts_page.trigger_dialog(
            java_script_alerts_page.prompt_button,
            java_script_alerts_page.send_text_to_prompt,
            "Hello, Playwright!",
        )

    with allure.step("Verify that the prompt was accepted successfully"):
        java_script_alerts_page.verify_prompt_accepted("Hello, Playwright!")
