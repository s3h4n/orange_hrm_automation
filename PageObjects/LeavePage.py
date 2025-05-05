from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LeavePage(BasePage):
    """Page Object for the Leave Page"""

    # Locators
    LEAVE_HEADER = (By.XPATH, "//h6[contains(text(), 'Leave')]")
    STATUS_DROPDOWN = (
    By.XPATH, "//label[contains(text(), 'Show Leave with Status')]/following::div[contains(@class, 'oxd-select-text')]")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Page title
    LEAVE_PAGE_TITLE = "OrangeHRM"

    def __init__(self, driver):
        super().__init__(driver)

    def is_leave_page_loaded(self):
        """Check if leave page is loaded by verifying the header"""
        return self.is_visible(*self.LEAVE_HEADER)

    def get_leave_page_title(self):
        """Get the title of the leave page"""
        return self.get_title()