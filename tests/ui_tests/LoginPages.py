from BaseApp import BasePage
from selenium.webdriver.common.by import By


class LoginLocators:
    LOCATOR_LOGIN_FIELD = (By.NAME, "user-name")
    LOCATOR_LOGIN_BUTTON = (By.NAME, "login-button")
    LOCATOR_LOGIN_PASSWORD = (By.NAME, "password")


class LoginHelper(BasePage):

    def enter_login(self, login):
        search_field = self.find_element(LoginLocators.LOCATOR_LOGIN_FIELD)
        search_field.click()
        search_field.send_keys(login)
        return search_field

    def enter_button(self):
        button = self.find_element(LoginLocators.LOCATOR_LOGIN_BUTTON)
        button.submit()
        return button

    def enter_password(self,password):
        search_field = self.find_element(LoginLocators.LOCATOR_LOGIN_PASSWORD)
        search_field.click()
        search_field.send_keys(password)
        return search_field
