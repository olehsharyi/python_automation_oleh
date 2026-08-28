import allure
import pytest

from pages.iframe_page import IFramePage

@pytest.mark.regression
@allure.epic("UI Automation")
@allure.feature("IFrame")
@allure.story("Navigation")
@allure.title("Navigate to link: {link_name}")
@pytest.mark.parametrize(
    "link_name, expected_title",
    [
        ("Docs", "Installation"),
        ("MCP", "Playwright MCP"),
    ],
)
def test_iframe_navigation(
    iframe_page: IFramePage,
    link_name: str,
    expected_title: str,
) -> None:
    iframe_page.open()
    iframe_page.navigate_to(link_name)
    iframe_page.verify_heading(expected_title)


@pytest.mark.parametrize(
    "navigation_path, expected_heading",
    [
        (
            ("Docs", "Installation", "Installing Playwright"),
            "Installing Playwright",
        ),
        (
            ("Docs", "Installation", "What's Installed"),
            "What's Installed",
        ),
    ],
)
@pytest.mark.regression
@allure.epic("UI Automation")
@allure.feature("IFrame")
@allure.story("Table of Contents Navigation")
@allure.title("Navigate to TOC path: {navigation_path}")
def test_iframe_toc_navigation(
    iframe_page: IFramePage,
    navigation_path: tuple[str, ...],
    expected_heading: str,
) -> None:
    iframe_page.open()
    iframe_page.navigate_to(*navigation_path)
    iframe_page.verify_heading(expected_heading, level=2)
