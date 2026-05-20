import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    NEXT_BUTTON = (
        By.CLASS_NAME,
        "carousel-control-next"
    )

    PREVIOUS_BUTTON = (
        By.CLASS_NAME,
        "carousel-control-prev"
    )

    LAPTOPS = (
        By.XPATH,
        "//a[text()='Laptops']"
    )

    PHONES = (
        By.XPATH,
        "//a[text()='Phones']"
    )

    MONITORS = (
        By.XPATH,
        "//a[text()='Monitors']"
    )

    PRODUCT = (
        By.XPATH,
        "//a[text()='Sony vaio i5']"
    )

    def click_next(self):

        next_button = self.find_element(
            self.NEXT_BUTTON
        )

        # First banner movement
        self.driver.execute_script(
            "arguments[0].click();",
            next_button
        )

        time.sleep(2)

        # Second banner movement
        self.driver.execute_script(
            "arguments[0].click();",
            next_button
        )

        time.sleep(2)

        # Scroll down slightly
        self.driver.execute_script(
            "window.scrollBy(0, 300);"
        )

        time.sleep(2)

        # Scroll back to top
        self.driver.execute_script(
            "window.scrollTo(0, 0);"
        )

        time.sleep(2)

    def click_previous(self):

        previous_button = self.find_element(
            self.PREVIOUS_BUTTON
        )

        self.driver.execute_script(
            "arguments[0].click();",
            previous_button
        )

        time.sleep(2)

    def click_laptops(self):

        self.click_element(
            self.LAPTOPS
        )

        time.sleep(2)

    def click_phones(self):

        self.click_element(
            self.PHONES
        )

        time.sleep(2)

    def click_monitors(self):

        self.click_element(
            self.MONITORS
        )

        time.sleep(2)

    def click_product(self):

        self.click_element(
            self.PRODUCT
        )

        time.sleep(2)