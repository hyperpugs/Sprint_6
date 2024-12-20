import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()