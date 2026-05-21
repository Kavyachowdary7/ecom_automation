from pytest_bdd import scenarios, given, when, then

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


scenarios("../features/products.feature")


@given("user is on homepage")
def open_homepage(driver):
    pass


@when("user explores mobile products")
def mobiles(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Phones']"))
    ).click()

    time.sleep(1)


@when("user explores laptop products")
def laptops(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Laptops']"))
    ).click()

    time.sleep(1)


@when("user explores monitor products")
def monitors(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Monitors']"))
    ).click()

    time.sleep(1)


@then("products should display successfully")
def verify_products(driver):

    assert "Laptops" in driver.page_source

    assert "Phones" in driver.page_source

    assert "Monitors" in driver.page_source