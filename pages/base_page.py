import time

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from selenium.common.exceptions import ElementClickInterceptedException

from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):

        self.driver = driver

    def click_element(self, locator):

        try:

            element = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.element_to_be_clickable(locator)
            )

            element.click()

            time.sleep(0.5)

        except (
            TimeoutException,
            ElementClickInterceptedException
        ):

            try:

                WebDriverWait(
                    self.driver,
                    5
                ).until(
                    EC.invisibility_of_element_located(
                        (By.CLASS_NAME, "modal-backdrop")
                    )
                )

            except:
                pass

            element = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.element_to_be_clickable(locator)
            )

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

            time.sleep(0.5)

    def enter_text(self, locator, text):

        element = WebDriverWait(
            self.driver,
            5
        ).until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        time.sleep(0.5)

        element.send_keys(text)

        time.sleep(0.5)

    def get_text(self, locator):

        text = WebDriverWait(
            self.driver,
            5
        ).until(
            EC.visibility_of_element_located(locator)
        ).text

        time.sleep(0.5)

        return text

    def wait_for_alert_and_accept(self):

        WebDriverWait(
            self.driver,
            5
        ).until(
            EC.alert_is_present()
        )

        alert = self.driver.switch_to.alert

        text = alert.text

        time.sleep(0.5)

        alert.accept()

        time.sleep(0.5)

        return text

    def find_element(self, locator):

        return WebDriverWait(
            self.driver,
            5
        ).until(
            EC.presence_of_element_located(locator)
        )