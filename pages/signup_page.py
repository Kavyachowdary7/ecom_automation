from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):

    SIGNUP_MENU = (By.ID, "signin2")

    USERNAME = (By.ID, "sign-username")

    PASSWORD = (By.ID, "sign-password")

    SIGNUP_BUTTON = (
        By.XPATH,
        "//button[text()='Sign up']"
    )

    def click_signup_menu(self):

        self.click_element(self.SIGNUP_MENU)

    def enter_username(self, username):

        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):

        self.enter_text(self.PASSWORD, password)

    def click_signup_button(self):

        self.click_element(self.SIGNUP_BUTTON)