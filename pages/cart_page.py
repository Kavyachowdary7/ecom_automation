import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    ADD_TO_CART = (By.XPATH, "//a[text()='Add to cart']")

    CART_MENU = (By.ID, "cartur")

    PRODUCT_NAME = (
        By.XPATH,
        "//td[text()='Sony vaio i5']"
    )

    def click_add_to_cart(self):

        self.click_element(self.ADD_TO_CART)

    def handle_cart_alert(self):

        return self.wait_for_alert_and_accept()

    def click_cart_menu(self):

        time.sleep(2)

        self.click_element(self.CART_MENU)

    def get_product_name(self):

        return self.get_text(self.PRODUCT_NAME)