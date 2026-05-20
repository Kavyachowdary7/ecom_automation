from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LogoutPage(BasePage):

    LOGOUT = (By.ID, "logout2")

    LOGIN = (By.ID, "login2")

    def click_logout(self):

        self.click_element(self.LOGOUT)

    def get_login_text(self):

        return self.get_text(self.LOGIN)