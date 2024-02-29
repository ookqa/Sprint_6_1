import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    driver.quit()
