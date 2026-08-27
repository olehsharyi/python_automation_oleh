import pytest
from playwright.sync_api import Page

from pages.iframe_page import IFramePage

@pytest.mark.parametrize(
    "link_name, expected_title",
    [
        ("Docs", "Installation"),
        ("MCP", "Playwright MCP"),
    ],
)
def test_iframe_navigation(
    page: Page,
    iframe_page: IFramePage,
    link_name: str,
    expected_title: str,
) -> None:
    iframe_page.open()
    iframe_page.click_link(link_name)
    iframe_page.verify_heading(expected_title)




@pytest.mark.parametrize(
    "toc_link,expected_heading",
    [
        ("Installing Playwright", "Installing Playwright"),
        ("What's Installed", "What's Installed"),
    ],
)
def test_iframe_toc_navigation(
    page: Page,
    iframe_page: IFramePage,
    toc_link: str,
    expected_heading: str,
) -> None:
    iframe_page.open()
    iframe_page.click_link("Docs")
    iframe_page.click_link("Installation")
    
    iframe_page.click_link(toc_link)
    
    iframe_page.verify_heading(expected_heading, level=2)
    