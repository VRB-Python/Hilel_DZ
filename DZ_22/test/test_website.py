import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class TestWish:

    @pytest.mark.one
    def test_find_search_culons(self, open_via_chrome: Chrome):
        search_field = open_via_chrome.find_element(By.XPATH, "//*[@name=\"search\"]")
        search_button = open_via_chrome.find_element(By.XPATH, "//*[@type=\"button\" and @class=\"btn\"]")

        search_field.send_keys("кулон")
        search_button.click()

        found_result = open_via_chrome.find_elements(By.CSS_SELECTOR, ".product-layout [href^=\"https\"]")

        assert len(found_result) == 24, "No, its not"

    @pytest.mark.two
    def test_find_facebook(self, open_via_chrome: Chrome):
        window_main = open_via_chrome.window_handles[0]

        facebook_button = open_via_chrome.find_element(By.CSS_SELECTOR, ".facebook , [title=\"Facebook\"]")
        face_page = facebook_button.click()

        window_facebook = open_via_chrome.window_handles[1]
        open_via_chrome.switch_to.window(window_facebook)


        assert open_via_chrome.current_url == "https://www.facebook.com/brasletgelaniy", "NO, it is not Facebook page"
        open_via_chrome.switch_to.window(window_main)


    @pytest.mark.three
    def test_find_instagram(self, open_via_chrome: Chrome):
        window_main = open_via_chrome.window_handles[0]

        insta_button = open_via_chrome.find_element(By.CSS_SELECTOR, ".instagram , [title=\"Instagram\"]")
        face_page = insta_button.click()

        window_insta = open_via_chrome.window_handles[-1]
        open_via_chrome.switch_to.window(window_insta)

        assert open_via_chrome.current_url == "https://www.instagram.com/braslet_gelaniy/", "NO, it is not Instagram page" # я не маю інстаграму тому мене прости закидує на Login page
        open_via_chrome.switch_to.window(window_main)