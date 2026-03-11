from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    first_name = (By.XPATH, "//input[@id='firstNameInput']")
    last_name = (By.XPATH, "//input[@id='lastNameInput']")
    address = (By.XPATH, "//input[@id='addressLine1Input']")
    province = (By.XPATH, "//input[@id='provinceInput']")
    postal = (By.XPATH, "//input[@id='postCodeInput']")
    continue_btn = (By.XPATH, "//button[@id='checkout-shipping-continue']")
    download_receipt_btn = (By.XPATH, "//a[@id='downloadpdf']")

    def enter_shipping_details(self, firstname, lastname, address, city, state, zipcode):
        self.type_text(self.first_name, firstname)
        self.type_text(self.last_name, lastname)
        self.type_text(self.address, address)
        self.type_text(self.province, city)
        self.type_text(self.postal, str(zipcode))
        self.click(self.continue_btn)

    def download_receipt(self):
        self.click(self.download_receipt_btn)