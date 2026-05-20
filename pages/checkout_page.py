from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    PLACE_ORDER = (
        By.XPATH,
        "//button[text()='Place Order']"
    )

    NAME = (
        By.ID,
        "name"
    )

    COUNTRY = (
        By.ID,
        "country"
    )

    CITY = (
        By.ID,
        "city"
    )

    CARD = (
        By.ID,
        "card"
    )

    MONTH = (
        By.ID,
        "month"
    )

    YEAR = (
        By.ID,
        "year"
    )

    PURCHASE = (
        By.XPATH,
        "//button[text()='Purchase']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//h2[text()='Thank you for your purchase!']"
    )

    def click_place_order(self):

        self.click_element(
            self.PLACE_ORDER
        )

    def enter_name(self, name):

        self.enter_text(
            self.NAME,
            name
        )

    def enter_country(self, country):

        self.enter_text(
            self.COUNTRY,
            country
        )

    def enter_city(self, city):

        self.enter_text(
            self.CITY,
            city
        )

    def enter_card(self, card):

        self.enter_text(
            self.CARD,
            card
        )

    def enter_month(self, month):

        self.enter_text(
            self.MONTH,
            month
        )

    def enter_year(self, year):

        self.enter_text(
            self.YEAR,
            year
        )

    def click_purchase(self):

        self.click_element(
            self.PURCHASE
        )

    def get_success_message(self):

        return self.get_text(
            self.SUCCESS_MESSAGE
        )