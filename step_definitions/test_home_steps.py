from pytest_bdd import (
    scenarios,
    given,
    when,
    then
)

import time

from pages.home_page import HomePage


scenarios("../features/home.feature")


@given("user is on homepage")
def open_homepage(driver):

    pass


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


@when("user clicks next banner")
def click_next_banner(driver):

    home = HomePage(driver)

    home.click_next()


@when("user clicks previous banner")
def click_previous_banner(driver):

    home = HomePage(driver)

    home.click_previous()


@then("homepage should load successfully")
def verify_homepage(driver):

    assert (
        "STORE"
        in driver.page_source
    )