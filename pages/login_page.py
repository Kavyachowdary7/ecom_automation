from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_MENU = (By.ID, "login2")
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    WELCOME_TEXT = (By.ID, "nameofuser")

    def click_login_menu(self):
        self.click_element(self.LOGIN_MENU)

    def enter_username(self, username):
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_TEXT)