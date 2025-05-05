import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
import time


@pytest.fixture(scope="function")
def setup(request, browser="chrome"):
    """Fixture to setup the WebDriver for tests"""

    if browser.lower() == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser.lower() == "firefox":
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    request.cls.driver = driver

    # Yield the driver
    yield driver

    # Teardown - close the browser
    time.sleep(2)  # Small delay to see the final state before closing
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to take screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                driver = item.cls.driver
                screenshots_dir = os.path.join(os.getcwd(), "Screenshots")
                if not os.path.exists(screenshots_dir):
                    os.makedirs(screenshots_dir)

                timestamp = time.strftime("%Y%m%d_%H%M%S")
                screenshot_path = os.path.join(screenshots_dir, f"failure_{item.name}_{timestamp}.png")
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved to {screenshot_path}")
            except Exception as e:
                print(f"Exception while taking screenshot: {e}")