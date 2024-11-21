import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope='function')
def driver():
    firefox = webdriver.Firefox()
    firefox.maximize_window()
    firefox.get(Urls.SCOOTER_URL)

    yield firefox

    firefox.quit()