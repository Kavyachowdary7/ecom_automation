from pytest_bdd import scenarios, given, when, then

import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


scenarios("../features/home.feature")


@given("user is on homepage")
def open_homepage(driver):

    driver.get(
        "https://www.demoblaze.com/index.html"
    )

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.ID, "tbodyid")
        )
    )

    time.sleep(2)


@when("user scrolls homepage")
def scroll_homepage(driver):

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(2)

    driver.execute_script(
        "window.scrollTo(0, 0);"
    )

    time.sleep(2)


@then("homepage should load successfully")
def verify_homepage(driver):

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.ID, "nava")
        )
    )

    assert "STORE" in driver.page_source