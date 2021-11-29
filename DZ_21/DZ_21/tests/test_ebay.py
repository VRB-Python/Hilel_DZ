from fixtures.test_fixtures import start_chrome
from data.data1 import name

def test_run_the_site(start_chrome):
    act = start_chrome.get(str(name))
    assert start_chrome.current_url == name