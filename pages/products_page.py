from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCT_TITLE = (
        By.XPATH,
        "//h2[text()='Sony vaio i5']"
    )

    def get_product_title(self):

        return self.get_text(
            self.PRODUCT_TITLE
        )