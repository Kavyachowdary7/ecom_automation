from pytest_bdd import scenarios, when, then

import time

from selenium.webdriver.common.keys import Keys

from pages.logout_page import LogoutPage


scenarios("../features/logout.feature")


@when("user clicks logout button")
def logout(driver):

    time.sleep(2)

    driver.switch_to.active_element.send_keys(
        Keys.ESCAPE
    )

    logout = LogoutPage(driver)

    logout.click_logout()


@then("user should logout successfully")
def verify_logout(driver):

    logout = LogoutPage(driver)

    assert (
        "Log in"
        == logout.get_login_text()
    )