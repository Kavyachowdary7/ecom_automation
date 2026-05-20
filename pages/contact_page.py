from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactPage(BasePage):

    CONTACT_MENU = (
        By.XPATH,
        "//a[text()='Contact']"
    )

    EMAIL = (By.ID, "recipient-email")

    NAME = (By.ID, "recipient-name")

    MESSAGE = (By.ID, "message-text")

    SEND_MESSAGE = (
        By.XPATH,
        "//button[text()='Send message']"
    )

    def click_contact_menu(self):

        self.click_element(self.CONTACT_MENU)

    def enter_email(self, email):

        self.enter_text(self.EMAIL, email)

    def enter_name(self, name):

        self.enter_text(self.NAME, name)

    def enter_message(self, message):

        self.enter_text(self.MESSAGE, message)

    def click_send_message(self):

        self.click_element(self.SEND_MESSAGE)