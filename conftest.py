import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()

    driver.get(
        "https://www.demoblaze.com/index.html"
    )

    yield driver

    driver.quit()