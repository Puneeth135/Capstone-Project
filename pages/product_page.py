from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):

    search_box = (By.XPATH, "//input[@placeholder='Search']")
    search_button = (By.XPATH, "//button[contains(text(),'Search')]")
    add_to_cart = (By.CSS_SELECTOR, ".shelf-item__buy-btn")
    shelf_items = (By.CLASS_NAME, "shelf-item")
    cart_icon = (By.ID, "shopping-cart")
    cart_content = (By.CSS_SELECTOR, ".float-cart__content")
    checkout_btn = (By.XPATH, "//div[@class='float-cart__footer']//button")

    def search_product(self, product_name):
        search = self.wait_for_visibility(self.search_box)
        self.wait.until(EC.element_to_be_clickable(self.search_box))
        search.clear()
        search.send_keys(product_name)
        self.click(self.search_button)
        self.wait_for_all_elements(self.shelf_items, timeout=30)

    def add_product(self):
        self.wait_for_all_elements(self.shelf_items)
        self.wait_for_clickable(self.add_to_cart)
        self.click(self.add_to_cart)
        self.wait_for_visibility(self.cart_content)

    def checkout(self):
        self.scroll_and_click(self.checkout_btn)