import pytest
from pages.contact_page import ContactPage
from data.contact_data import CONTACT_FORM_DATA


@pytest.mark.smoke
# Краще
def test_contact_page_is_opened(contact_page: ContactPage) -> None:
    contact_page.open()
    assert contact_page.get_title() == "Contact"

@pytest.mark.regression
def test_avatar_is_visible(contact_page: ContactPage) -> None:
    contact_page.open()
    contact_page.check_avatar_is_visible()

@pytest.mark.regression
def test_avatar_is_loaded(contact_page: ContactPage) -> None:
    contact_page.open()
    contact_page.check_avatar_is_loaded()

@pytest.mark.regression
def test_contact_form_values(contact_page: ContactPage) -> None:
    # 1. Відкриваємо сторінку
    contact_page.open()

    # 2. Заповнюємо форму даними
    contact_page.fill_form(**CONTACT_FORM_DATA)

    # 3. Перевіряємо, що всі значення коректно записалися в інпути
    contact_page.verify_form_values(**CONTACT_FORM_DATA)