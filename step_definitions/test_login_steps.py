from pytest_bdd import scenarios, given, when, then
import json

from pages.login_page import LoginPage


scenarios("../features/login.feature")


@given("user is on homepage")
def open_homepage(driver):
    pass


@when("user clicks login menu")
def click_login_menu(driver):

    login = LoginPage(driver)

    login.click_login_menu()


@when("user enters login username")
def enter_username(driver):

    login = LoginPage(driver)

    with open("data/users.json") as file:
        data = json.load(file)

    login.enter_username(data["username"])


@when("user enters login password")
def enter_password(driver):

    login = LoginPage(driver)

    with open("data/users.json") as file:
        data = json.load(file)

    login.enter_password(data["password"])


@when("user clicks login button")
def click_login_button(driver):

    login = LoginPage(driver)

    login.click_login_button()


@then("user should login successfully")
def verify_login(driver):

    login = LoginPage(driver)

    message = login.get_welcome_message()

    assert "Welcome" in message