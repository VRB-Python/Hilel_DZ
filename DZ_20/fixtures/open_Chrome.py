from selenium.webdriver import Chrome
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="session")
def open_Chrome():
    chrome_brow = Chrome(executable_path=ChromeDriverManager().install())
    chrome_brow.implicitly_wait(20)
    chrome_brow.maximize_window()
    chrome_brow.get("https://www.wish.com/?hide_login_modal=true")

    yield chrome_brow

    chrome_brow.quit()

