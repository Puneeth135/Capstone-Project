import os
from pathlib import Path
import time
import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.excel_reader import ExcelReader
from utils.logger import get_logger

logger = get_logger()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

excel = ExcelReader()
data = excel.get_data(
    os.path.join(BASE_DIR, "data", "test_data.xlsx"),
    "Sheet1"
)

# LOGIN TEST
@pytest.mark.parametrize("index", range(len(data)))
def test_login(setup, index):
    try:
        driver = setup
        login = LoginPage(driver)
        row = data.iloc[index]

        driver.get("https://bstackdemo.com/")
        username = row["username"]
        password = row["password"]
        logger.info("Login started")
        login.login(username, password)
        assert "StackDemo" in driver.title
        logger.info(f"Login successful for user: {username}")

    except AssertionError as e:
        logger.error(f"Login assertion failed: {e}")
        raise
    except Exception as e:
        logger.error(f"Login test failed with error: {e}")
        raise

# PRODUCT SEARCH
def test_product_search(setup):
    try:
        driver = setup
        login = LoginPage(driver)
        product = ProductPage(driver)

        row = data.iloc[0]
        driver.get("https://bstackdemo.com/")
        login.login(row["username"], row["password"])
        logger.info("Searching product")
        product.search_product(row["product"])
        logger.info(f"Product search successful for: {row['product']}")

    except Exception as e:
        logger.error(f"Product search test failed with error: {e}")
        raise


# ADD TO CART
def test_add_to_cart(setup):
    try:
        driver = setup
        login = LoginPage(driver)
        product = ProductPage(driver)

        row = data.iloc[1]
        driver.get("https://bstackdemo.com/")
        login.login(row["username"], row["password"])
        product.search_product(row["product"])
        logger.info("Adding product to cart")
        product.add_product()
        logger.info("Product added to cart successfully")

    except Exception as e:
        logger.error(f"Add to cart test failed with error: {e}")
        raise


# CHECKOUT
def test_checkout(setup):
    try:
        driver = setup
        login = LoginPage(driver)
        product = ProductPage(driver)
        cart = CartPage(driver)

        row = data.iloc[0]
        driver.get("https://bstackdemo.com/")
        login.login(row["username"], row["password"])
        product.search_product(row["product"])
        product.add_product()
        logger.info("Checkout started")
        cart.checkout_process()
        logger.info("Checkout process completed successfully")

    except Exception as e:
        logger.error(f"Checkout test failed with error: {e}")
        raise


# SHIPPING DETAILS
def test_shipping_details(setup):
    try:
        driver = setup
        login = LoginPage(driver)
        product = ProductPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        row = data.iloc[0]
        driver.get("https://bstackdemo.com/")
        login.login(row["username"], row["password"])
        product.search_product(row["product"])
        product.add_product()
        cart.checkout_process()
        logger.info("Entering shipping details")
        checkout.enter_shipping_details(
            row["firstname"],
            row["lastname"],
            row["address"],
            row["city"],
            row["state"],
            row["zipcode"]
        )
        logger.info("Shipping details entered successfully")

    except KeyError as e:
        logger.error(f"Missing shipping data field in Excel: {e}")
        raise
    except Exception as e:
        logger.error(f"Shipping details test failed with error: {e}")
        raise


# DOWNLOAD RECEIPT
def test_download_receipt(setup):
    try:
        driver = setup
        login = LoginPage(driver)
        product = ProductPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        row = data.iloc[0]
        driver.get("https://bstackdemo.com/")
        login.login(row["username"], row["password"])
        product.search_product(row["product"])
        product.add_product()
        cart.checkout_process()
        checkout.enter_shipping_details(
            row["firstname"],
            row["lastname"],
            row["address"],
            row["city"],
            row["state"],
            row["zipcode"]
        )
        logger.info("Downloading receipt")
        checkout.download_receipt()
        logger.info("Validating receipt")

        download_path = os.path.join(str(Path.home()), "Downloads")
        time.sleep(5)

        try:
            files = os.listdir(download_path)
        except FileNotFoundError as e:
            logger.error(f"Download directory not found: {download_path}")
            raise

        receipt_found = False
        for file in files:
            if "confirmation" in file.lower():
                receipt_found = True
                logger.info(f"Receipt file found: {file}")
                break

        assert receipt_found, "Receipt file not downloaded"
        logger.info("Receipt validation successful")

    except AssertionError as e:
        logger.error(f"Receipt validation failed: {e}")
        raise
    except Exception as e:
        logger.error(f"Download receipt test failed with error: {e}")
        raise