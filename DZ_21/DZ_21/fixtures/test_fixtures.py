import pytest
from time import sleep
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def start_chrome():
    chrome_driver = Chrome(executable_path=ChromeDriverManager().install())
    chrome_driver.maximize_window()
    sleep(5)
    yield chrome_driver
    chrome_driver.quit()