from selenium.webdriver.common.by import By
from .BasePage import BasePage


class DashboardPage(BasePage):
    """Page Object for the Dashboard Page"""

    # Locators
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT_OPTION = (By.XPATH, "//a[contains(text(), 'Logout')]")
    QUICK_LAUNCH_LEAVE = (By.XPATH, "//p[text()='My Leave']")

    # Page title
    DASHBOARD_PAGE_TITLE = "OrangeHRM"

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_loaded(self):
        """Check if dashboard page is loaded by verifying the header"""
        return self.is_visible(*self.DASHBOARD_HEADER)

    def get_dashboard_title(self):
        """Get the title of the dashboard page"""
        return self.get_title()

    def click_my_leave(self):
        """Click on My Leave from Quick Launch"""
        self.click_element(*self.QUICK_LAUNCH_LEAVE)

    def click_user_dropdown(self):
        """Click on user dropdown in the top right corner"""
        self.click_element(*self.USER_DROPDOWN)

    def click_logout(self):
        """Click on logout option from the user dropdown"""
        self.click_user_dropdown()
        self.click_element(*self.LOGOUT_OPTION)