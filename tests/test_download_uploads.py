import allure

from pages.downloads_page import DownloadsPage


@allure.title("Test Download File")
def test_download_file(downloads_page: DownloadsPage) -> None:
    with allure.step("Open the downloads page"):
        downloads_page.open()

    with allure.step("Download the test.txt file"):
        download_path = downloads_page.download_test_txt_file()

    with allure.step("Verify the downloaded file"):
        downloads_page.verify_downloaded_file(
            download_path,
            "test-file.txt",
        )
