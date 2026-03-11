import os
import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bstackdemo.com/")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs["setup"]
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        file_name = f"screenshots/{item.name}_{int(time.time())}.png"

        driver.save_screenshot(file_name)