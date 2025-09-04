import pytest

from selene import browser

@pytest.fixture(scope="session")
def browser():
    print("Браузер!")

    yield

    print("Закрываем браузер!")

pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://duckduckgo.com/'

    yield