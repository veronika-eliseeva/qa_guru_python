import pytest

from selene import browser

@pytest.fixture(scope="session")
def browser():
    print("Браузер!")

    yield

    print("Закрываем браузер!")

