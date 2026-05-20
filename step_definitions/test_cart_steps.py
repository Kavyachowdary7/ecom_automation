from pytest_bdd import scenarios, given, when, then

from pages.home_page import HomePage
from pages.cart_page import CartPage


scenarios("../features/cart.feature")


@given("user selects laptop category")
def select_laptop_category(driver):

    home = HomePage(driver)

    home.click_laptops()


@when("user selects laptop product")
def select_product(driver):

    home = HomePage(driver)

    home.click_product()


@when("user clicks add to cart")
def add_to_cart(driver):

    cart = CartPage(driver)

    cart.click_add_to_cart()


@when("user accepts cart alert")
def accept_alert(driver):

    cart = CartPage(driver)

    alert_text = cart.handle_cart_alert()

    assert "Product added" in alert_text


@when("user opens cart page")
def open_cart(driver):

    cart = CartPage(driver)

    cart.click_cart_menu()


@then("product should be added to cart")
def verify_product(driver):

    cart = CartPage(driver)

    assert "Sony vaio i5" == cart.get_product_name()