from pathlib import Path

from playwright.sync_api import Download, Page

from config import DOWNLOADS_URL
from pages.base_page import BasePage


class DownloadsPage(BasePage):
    URL_PATH = DOWNLOADS_URL

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.test_txt_download_button = page.get_by_role(
            "link",
            name="test-file.txt",
        )

    def download_test_txt_file(self) -> Path:
        with self.page.expect_download() as download_info:
            self.test_txt_download_button.click()

        download: Download = download_info.value

        download_path = Path("downloads") / download.suggested_filename
        download_path.parent.mkdir(exist_ok=True)

        download.save_as(download_path)

        return download_path

    def verify_downloaded_file(
        self,
        download_path: Path,
        expected_filename: str,
    ) -> None:
        assert download_path.name == expected_filename
        assert download_path.exists()
