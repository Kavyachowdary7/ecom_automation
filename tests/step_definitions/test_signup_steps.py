from pytest_bdd import (
    scenarios,
    given,
    when,
    then
)

import json
import time

from selenium.webdriver.common.keys import Keys

from pages.signup_page import SignupPage


scenarios("../features/signup.feature")


@given("user is on homepage")
def open_website(driver):

    # Homepage already opens from conftest.py
    pass


@when("user clicks signup menu")
def click_signup(driver):

    signup = SignupPage(driver)

    signup.click_signup_menu()


@when("user enters signup username")
def enter_signup_username(driver):

    signup = SignupPage(driver)

    # Generate unique username using timestamp
    username = (
        "user_" +
        str(int(time.time()))
    )

    # Save username temporarily
    data = {
        "username": username
    }

    with open(
        "data/users.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    signup.enter_username(username)


@when("user enters signup password")
def enter_signup_password(driver):

    signup = SignupPage(driver)

    password = "test@123"

    # Read existing username
    with open(
        "data/users.json",
        "r"
    ) as file:

        data = json.load(file)

    # Add password
    data["password"] = password

    # Save updated data
    with open(
        "data/users.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    signup.enter_password(password)


@when("user clicks signup button")
def click_signup_button(driver):

    signup = SignupPage(driver)

    signup.click_signup_button()


@then("signup should be successful")
def verify_signup(driver):

    signup = SignupPage(driver)

    alert_text = (
        signup.wait_for_alert_and_accept()
    )

    assert (
        "Sign up successful."
        in alert_text
    )

    time.sleep(1)

    # Close signup modal if still visible
    try:

        driver.switch_to.active_element.send_keys(
            Keys.ESCAPE
        )

    except Exception:

        pass

    time.sleep(1)