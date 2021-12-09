import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestWebelements:

    @pytest.mark.firstName
    def test_find_by_firstName(self, open_Chrome: Chrome):
        search_field = open_Chrome.find_element(By.XPATH, "//*[@data-id=\"firstName\"]")

        assert search_field.is_displayed() , "No, firstName field is not found."

    @pytest.mark.password
    def test_find_password_field(self, open_Chrome: Chrome):
        search_field2 = open_Chrome.find_element(By.XPATH, "//*[@data-testid=\"login-password\"]")

        assert search_field2.is_displayed(), "No, password field is not found."

    @pytest.mark.log_facebook
    def test_find_log_facebook_field(self, open_Chrome: Chrome):
        search_field3 = open_Chrome.find_element(By.XPATH, "//*[@data-testid=\"login-facebook\"]")

        assert search_field3.is_displayed(), "No, login-facebook button is not found."

    @pytest.mark.log_google
    def test_find_log_google_field(self, open_Chrome: Chrome):
        search_field4 = open_Chrome.find_element(By.XPATH, "//*[@data-testid=\"login-google\"]")

        assert search_field4.is_displayed(), "No, login-google button is not found."

    @pytest.mark.log_apple
    def test_find_log_apple_field(self, open_Chrome: Chrome):
        search_field5 = open_Chrome.find_element(By.XPATH, "//*[@data-testid=\"login-apple\" and @role=\"button\"]")

        assert search_field5.is_displayed(), "No, login-apple button is not found."

    @pytest.mark.footer
    def test_find_footer(self, open_Chrome: Chrome):
        search_field6 = open_Chrome.find_element(By.XPATH, "//*[@id=\"footer\"]")

        assert search_field6.is_displayed(), "No, footer is not found."
