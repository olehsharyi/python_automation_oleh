# tests/test_multiple_windows.py

from config import WINDOWS_NEW_PAGE_URL
from pages.multiple_windows_page import MultipleWindowsPage


def test_open_new_window(
    multiple_windows_page: MultipleWindowsPage,
) -> None:
    multiple_windows_page.open()

    new_window = multiple_windows_page.open_new_window()

    multiple_windows_page.verify_new_window_title(new_window)


def test_open_new_page(
    multiple_windows_page: MultipleWindowsPage,
) -> None:
    multiple_windows_page.open()

    new_page = multiple_windows_page.open_new_page()
    print(new_page.url)
    multiple_windows_page.verify_new_window_title(new_page)
    multiple_windows_page.verify_page_url(new_page, WINDOWS_NEW_PAGE_URL)
