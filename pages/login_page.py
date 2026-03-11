from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    signin_btn = (By.ID, "signin")
    username_dropdown = (By.ID, "username")
    password_dropdown = (By.ID, "password")
    login_btn = (By.ID, "login-btn")

    def login(self, username, password):
        self._click_signin()
        self._select_username(username)
        self._select_password(password)
        self._click_login()
        self.logger.info(f"Login successful for user: {username}")


    def _click_signin(self):
        self.logger.info("Clicking sign-in button")
        self.click(self.signin_btn)

    def _select_username(self, username):
        self.logger.info(f"Selecting username: {username}")
        self.click(self.username_dropdown)
        user_option = (By.XPATH, f"//div[contains(text(),'{username}')]")
        self.click(user_option)

    def _select_password(self, password):
        self.logger.info("Selecting password")
        self.click(self.password_dropdown)
        password_option = (By.XPATH, f"//div[contains(text(),'{password}')]")
        self.click(password_option)

    def _click_login(self):
        self.logger.info("Clicking login button")
        self.click(self.login_btn)