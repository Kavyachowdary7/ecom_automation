from pytest_bdd import scenarios, given, when, then, parsers

import time

from selenium.webdriver.common.keys import Keys

from pages.checkout_page import CheckoutPage


scenarios("../features/checkout.feature")


@given("product is already added to cart")
def product_exists(driver):

    pass


@when("user clicks place order")
def click_place_order(driver):

    checkout = CheckoutPage(driver)

    checkout.click_place_order()


@when("user enters checkout username")
def enter_checkout_username(driver):

    import json

    checkout = CheckoutPage(driver)

    with open("data/users.json") as file:

        data = json.load(file)

    checkout.enter_name(
        data["username"]
    )


@when(parsers.parse(
    'user enters country "{country}"'
))
def enter_country(driver, country):

    checkout = CheckoutPage(driver)

    checkout.enter_country(country)


@when(parsers.parse(
    'user enters city "{city}"'
))
def enter_city(driver, city):

    checkout = CheckoutPage(driver)

    checkout.enter_city(city)


@when(parsers.parse(
    'user enters card "{card}"'
))
def enter_card(driver, card):

    checkout = CheckoutPage(driver)

    checkout.enter_card(card)


@when(parsers.parse(
    'user enters month "{month}"'
))
def enter_month(driver, month):

    checkout = CheckoutPage(driver)

    checkout.enter_month(month)


@when(parsers.parse(
    'user enters year "{year}"'
))
def enter_year(driver, year):

    checkout = CheckoutPage(driver)

    checkout.enter_year(year)


@when("user clicks purchase button")
def click_purchase(driver):

    checkout = CheckoutPage(driver)

    checkout.click_purchase()


@then("order should be placed successfully")
def verify_order(driver):

    checkout = CheckoutPage(driver)

    success_message = (
        checkout.get_success_message()
    )

    assert (
        "Thank you for your purchase!"
        == success_message
    )

    time.sleep(2)

    driver.switch_to.active_element.send_keys(
        Keys.ESCAPE
    )

    time.sleep(2)