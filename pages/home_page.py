import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):

    LAPTOPS = (
        By.XPATH,
        "//a[text()='Laptops']"
    )

    PRODUCT = (
        By.XPATH,
        "//a[text()='Sony vaio i5']"
    )

    NEXT_BUTTON = (
        By.CSS_SELECTOR,
        ".carousel-control-next"
    )

    def click_next(self):

        next_button = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.element_to_be_clickable(
                self.NEXT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            next_button
        )

        time.sleep(2)

    def click_laptops(self):

        self.click_element(
            self.LAPTOPS
        )

        time.sleep(3)

    def click_product(self):

        self.click_element(
            self.PRODUCT
        )

        time.sleep(2)

    def get_product_text(self):

        return self.get_text(
            self.PRODUCT
        )