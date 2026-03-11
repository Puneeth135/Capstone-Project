from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementNotInteractableException,
    NoSuchElementException
)
from utils.logger import get_logger


class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger()


    def wait_for_visibility(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Timeout waiting for visibility of element: {locator}")
            raise

    def wait_for_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.logger.error(f"Timeout waiting for element to be clickable: {locator}")
            raise

    def wait_for_all_elements(self, locator, timeout=None):
        try:
            wait = WebDriverWait(self.driver, timeout) if timeout else self.wait
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Timeout waiting for all elements: {locator}")
            raise


    def click(self, locator):
        try:
            element = self.wait_for_clickable(locator)
            element.click()
        except ElementNotInteractableException:
            self.logger.error(f"Element not interactable: {locator}")
            raise
        except NoSuchElementException:
            self.logger.error(f"Element not found: {locator}")
            raise

    def type_text(self, locator, text):
        try:
            element = self.wait_for_visibility(locator)
            element.clear()
            element.send_keys(text)
        except ElementNotInteractableException:
            self.logger.error(f"Element not interactable for typing: {locator}")
            raise

    def scroll_and_click(self, locator):
        try:
            element = self.wait_for_clickable(locator)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", element
            )
            self.driver.execute_script("arguments[0].click();", element)
        except ElementNotInteractableException:
            self.logger.error(f"Element not interactable for scroll-click: {locator}")
            raise
