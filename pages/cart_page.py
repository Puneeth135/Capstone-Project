from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    checkout = (By.XPATH, "//div[@class='buy-btn']")

    def checkout_process(self):
        self.click(self.checkout)