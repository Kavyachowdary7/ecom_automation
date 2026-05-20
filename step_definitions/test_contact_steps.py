from pytest_bdd import scenarios, given, when, then

import json
import time

from selenium.webdriver.common.keys import Keys

from pages.contact_page import ContactPage


scenarios("../features/contact.feature")


@given("user clicks contact menu")
def click_contact(driver):

    contact = ContactPage(driver)

    contact.click_contact_menu()


@when("user enters contact email")
def enter_email(driver):

    contact = ContactPage(driver)

    contact.enter_email(
        "test@gmail.com"
    )


@when("user enters registered contact name")
def enter_registered_name(driver):

    contact = ContactPage(driver)

    with open("data/users.json") as file:

        data = json.load(file)

    contact.enter_name(
        data["username"]
    )


@when("user enters message")
def enter_message(driver):

    contact = ContactPage(driver)

    contact.enter_message(
        "Testing contact module"
    )


@when("user clicks send message button")
def send_message(driver):

    contact = ContactPage(driver)

    contact.click_send_message()


@then("contact message should be sent successfully")
def verify_contact(driver):

    contact = ContactPage(driver)

    alert_text = (
        contact.wait_for_alert_and_accept()
    )

    assert "Thanks" in alert_text

    time.sleep(2)

    driver.switch_to.active_element.send_keys(
        Keys.ESCAPE
    )