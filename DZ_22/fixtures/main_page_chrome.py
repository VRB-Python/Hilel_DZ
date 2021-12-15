import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def open_via_chrome():
    chrome_brow = Chrome(executable_path=ChromeDriverManager().install())
    # chrome_brow.implicitly_wait(10)
    chrome_brow.maximize_window()

    chrome_brow.get("https://wish-shop.com.ua/")

    yield chrome_brow

    chrome_brow.quit()
