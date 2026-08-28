import allure
import pytest

from data.contact_data import CONTACT_FORM_DATA
from pages.contact_page import ContactPage


@pytest.mark.smoke
@allure.epic("UI Automation")
@allure.feature("Contact Page")
@allure.story("Page Navigation")
@allure.title("Contact page is opened and title is correct")
def test_contact_page_is_opened(contact_page: ContactPage) -> None:
    with allure.step("Open contact page"):
        contact_page.open()

    with allure.step("Verify page title"):
        contact_page.verify_title(ContactPage.PAGE_TITLE)


@pytest.mark.regression
@allure.epic("UI Automation")
@allure.feature("Contact Page")
@allure.story("Avatar Verification")
@allure.title("Avatar is visible")
def test_avatar_is_visible(contact_page: ContactPage) -> None:
    with allure.step("Open contact page"):
        contact_page.open()
    with allure.step("Check that avatar is visible"):
        contact_page.check_avatar_is_visible()


@pytest.mark.regression
@allure.epic("UI Automation")
@allure.feature("Contact Page")
@allure.story("Avatar Verification")
@allure.title("Avatar is loaded")
def test_avatar_is_loaded(contact_page: ContactPage) -> None:
    with allure.step("Open contact page"):
        contact_page.open()

    with allure.step("Check that avatar is loaded"):
        contact_page.check_avatar_is_loaded()


@pytest.mark.regression
@allure.epic("UI Automation")
@allure.feature("Contact Form")
@allure.story("Form Filling")
@allure.title("Contact form values are correctly saved and verified")
def test_contact_form_values(contact_page: ContactPage) -> None:
    with allure.step("Open contact page"):
        contact_page.open()

    with allure.step("Fill out the form with data"):
        contact_page.fill_form(**CONTACT_FORM_DATA)

    with allure.step("Verify that all values are correctly written into inputs"):
        contact_page.verify_form_values(**CONTACT_FORM_DATA)


@pytest.mark.parametrize(
    "email",
    [
        "invalid",
        "invalid@",
        "@example.com",
        "user@",
        "user example@example.com",
    ],
)
@pytest.mark.regression
@allure.epic("UI Automation")
@allure.feature("Contact Form")
@allure.story("Form Validation")
@allure.title("Contact form rejects invalid email: {email}")
def test_contact_form_rejects_invalid_email(
    contact_page: ContactPage,
    email: str,
) -> None:
    contact_page.open()

    contact_page.fill_form(
        "Oleh",
        "Sharyi",
        email,
        "Test message",
    )

    contact_page.verify_email_is_invalid()
