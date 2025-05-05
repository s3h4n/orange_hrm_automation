from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time


class BasePage:
    """Base Page object that all page objects inherit from"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element(self, by_locator, locator_value):
        """Click on an element specified by locator"""
        self.wait.until(EC.element_to_be_clickable((by_locator, locator_value))).click()

    def send_text(self, by_locator, locator_value, text):
        """Send text to an element specified by locator"""
        element = self.wait.until(EC.visibility_of_element_located((by_locator, locator_value)))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by_locator, locator_value):
        """Get text from an element specified by locator"""
        element = self.wait.until(EC.visibility_of_element_located((by_locator, locator_value)))
        return element.text

    def is_visible(self, by_locator, locator_value):
        """Check if element is visible"""
        element = self.wait.until(EC.visibility_of_element_located((by_locator, locator_value)))
        return bool(element)

    def get_title(self):
        """Get the title of the current page"""
        return self.driver.title

    def take_screenshot(self, name):
        """Take a screenshot and save with the given name"""
        screenshots_dir = os.path.join(os.getcwd(), "Screenshots")
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path